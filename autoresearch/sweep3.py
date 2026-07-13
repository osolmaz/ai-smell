"""Sweep the generalized family S_k = mean of products of k consecutive
rank-transformed spines, plus geometric-mean normalization."""
import bisect
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harness import evaluate, load_corpus

_pool = sorted(
    max(s["clauses"]) for seq in load_corpus().values()
    for s in seq if s["clauses"])


def F(v):
    return (bisect.bisect_left(_pool, v) + bisect.bisect_right(_pool, v)) / 2 / len(_pool)


def make_sk(k, geometric=False):
    def score(seq):
        g = [F(max(s["clauses"])) for s in seq if s["clauses"]]
        if len(g) < k:
            return 0.0
        prods = []
        for i in range(len(g) - k + 1):
            p = 1.0
            for j in range(k):
                p *= g[i + j]
            prods.append(p ** (1 / k) if geometric else p)
        return sum(prods) / len(prods)
    return score


if __name__ == "__main__":
    for k in (1, 2, 3, 4, 5):
        print(f"\n##### S_{k} (product over window {k})")
        evaluate(make_sk(k))
    for k in (2, 3, 4):
        print(f"\n##### S_{k} geometric (k-th root, comparable scale)")
        evaluate(make_sk(k, geometric=True))
