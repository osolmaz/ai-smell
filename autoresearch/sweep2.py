"""Batch sweep: consecutive-sentence metrics without tuned constants."""
import bisect
import random
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harness import evaluate, load_corpus


def spines(seq):
    return [max(s["clauses"]) for s in seq if s["clauses"]]


def lens(seq):
    return [s["words"] for s in seq]


_pool = sorted(v for s in load_corpus().values() for v in spines(s))


def F(v):
    lo = bisect.bisect_left(_pool, v)
    hi = bisect.bisect_right(_pool, v)
    return (lo + hi) / 2 / len(_pool)


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 0.0


def von_neumann(xs):
    if len(xs) < 3:
        return 2.0
    mu = statistics.mean(xs)
    var = sum((x - mu) ** 2 for x in xs) / len(xs)
    if var == 0:
        return 2.0
    msd = mean((b - a) ** 2 for a, b in zip(xs, xs[1:]))
    return msd / var


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


CANDIDATES = {}


def cand(name):
    def deco(fn):
        CANDIDATES[name] = fn
        return fn
    return deco


@cand("G rank-flow min kernel (adjacent pairs)")
def g(seq):
    f = [F(v) for v in spines(seq)]
    return mean(min(a, b) for a, b in zip(f, f[1:]))


@cand("H rank-flow product kernel")
def h(seq):
    f = [F(v) for v in spines(seq)]
    return mean(a * b for a, b in zip(f, f[1:]))


@cand("I von Neumann ratio, sentence lengths")
def i(seq):
    return von_neumann(lens(seq))


@cand("J von Neumann ratio, spines")
def j(seq):
    return von_neumann(spines(seq))


@cand("K turning-point ratio, lengths")
def k(seq):
    xs = lens(seq)
    n = len(xs)
    if n < 4:
        return 1.0
    tp = sum(1 for a, b, c in zip(xs, xs[1:], xs[2:])
             if (b > a and b > c) or (b < a and b < c))
    return tp / (2 * (n - 2) / 3)


@cand("L permutation z of adjacent |diff|, lengths")
def l(seq):
    xs = lens(seq)
    if len(xs) < 4:
        return 0.0
    obs = mean(abs(b - a) for a, b in zip(xs, xs[1:]))
    rng = random.Random(0)
    sims = []
    for _ in range(200):
        p = xs[:]
        rng.shuffle(p)
        sims.append(mean(abs(b - a) for a, b in zip(p, p[1:])))
    mu = statistics.mean(sims)
    sd = statistics.stdev(sims)
    return (obs - mu) / sd if sd else 0.0


@cand("M Spearman lag-1, lengths")
def m(seq):
    xs = lens(seq)
    if len(xs) < 4:
        return 0.0
    a, b = ranks(xs[:-1]), ranks(xs[1:])
    ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = sum((x - ma) ** 2 for x in a) ** 0.5
    db = sum((y - mb) ** 2 for y in b) ** 0.5
    return num / (da * db) if da and db else 0.0


@cand("N adjacent min/max ratio, lengths")
def n(seq):
    xs = lens(seq)
    return mean(min(a, b) / max(a, b) for a, b in zip(xs, xs[1:]) if max(a, b))


@cand("O adjacent min/max ratio, spines")
def o(seq):
    xs = spines(seq)
    return mean(min(a, b) / max(a, b) for a, b in zip(xs, xs[1:]) if max(a, b))


@cand("P rank nPVI, spines (adjacent |rank diff|)")
def p(seq):
    f = [F(v) for v in spines(seq)]
    return mean(abs(b - a) for a, b in zip(f, f[1:]))


if __name__ == "__main__":
    for name, fn in CANDIDATES.items():
        print(f"\n##### {name}")
        evaluate(fn)
