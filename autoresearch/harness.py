"""Fixed evaluation harness for the rhythm-tell search (do not modify).

Modeled on karpathy/autoresearch: this file is the equivalent of
prepare.py (fixed data prep and metric), feature.py is the equivalent of
train.py (the one file the agent edits), and journal.md is the log of
experiments.

The task: find a scalar feature of a document's *sentence sequence* (the
per-sentence word counts and clause-length lists, in order) that
separates the 10 AI landing pages from the 8 human baselines. Features
must be computed from the sequence only, so punctuation counts, bullet
shapes, and word identity are out of bounds; rhythm, cadence, and length
evolution are in bounds.

The metric, printed per run:

- auc: rank separation between groups (1.0 = perfect).
- margin_pct: with perfect separation, the gap at the closest edge as a
  percentage of the midpoint between the edges. This is the number to
  maximize. Without perfect separation it is negative (the overlap).
- loo: leave-one-out check. For each document, the threshold is set at
  the midpoint of the remaining 17; pass means the held-out document
  still classifies correctly. 18/18 required to keep a result.
- self/tweets: reported for context, never used for selection.

Run: python3 harness.py
"""
import importlib.util
import re
import statistics
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from analyze import load, split_sentences, CORPUS          # noqa: E402
from analyze_rhythm import clause_lengths                   # noqa: E402


def doc_sequence(path):
    """The per-sentence sequence: [{'words': int, 'clauses': [int, ...]}]."""
    body = "\n".join(
        re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l)
        for l in load(path).splitlines()
        if l.strip() and not re.match(r"\s*#{1,6}\s", l))
    return [{"words": n, "clauses": clause_lengths(s)}
            for s, n in split_sentences(body)]


def load_corpus():
    docs = {}
    for group in ("ai", "human", "tweets", "self"):
        for f in sorted((CORPUS / group).glob("*.md")):
            docs[(group, f.stem)] = doc_sequence(f)
    return docs


def auc(pos, neg):
    """P(random pos > random neg), ties counted half."""
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def evaluate(score_doc):
    docs = load_corpus()
    ai = [(k[1], score_doc(v)) for k, v in docs.items() if k[0] == "ai"]
    hu = [(k[1], score_doc(v)) for k, v in docs.items() if k[0] == "human"]
    ai_s = [s for _, s in ai]
    hu_s = [s for _, s in hu]

    direction = 1 if statistics.mean(ai_s) >= statistics.mean(hu_s) else -1
    a = auc([direction * s for s in ai_s], [direction * s for s in hu_s])

    hi = ai_s if direction == 1 else hu_s
    lo = hu_s if direction == 1 else ai_s
    edge_hi, edge_lo = min(hi), max(lo)
    mid = (edge_hi + edge_lo) / 2
    margin_pct = 100 * (edge_hi - edge_lo) / abs(mid) if mid else 0.0

    labeled = [(s, 1) for s in ai_s] + [(s, 0) for s in hu_s]
    loo_pass = 0
    for i in range(len(labeled)):
        rest = labeled[:i] + labeled[i + 1:]
        r_hi = min(s for s, g in rest if (g == 1) == (direction == 1))
        r_lo = max(s for s, g in rest if (g == 1) != (direction == 1))
        thr = (r_hi + r_lo) / 2
        s, g = labeled[i]
        pred = 1 if (direction * s > direction * thr) else 0
        loo_pass += (pred == g)

    self_s = [score_doc(v) for k, v in docs.items() if k[0] == "self"][0]
    tw = sorted((score_doc(v), k[1]) for k, v in docs.items() if k[0] == "tweets")

    print(f"auc={a:.3f}  margin_pct={margin_pct:+.1f}  loo={loo_pass}/18  "
          f"direction={'ai-high' if direction == 1 else 'ai-low'}")
    print(f"  ai edge:    {edge_hi if direction == 1 else edge_lo:.3f}  "
          f"({min(ai, key=lambda t: direction * t[1])[0]})")
    print(f"  human edge: {edge_lo if direction == 1 else edge_hi:.3f}  "
          f"({max(hu, key=lambda t: direction * t[1])[0]})")
    print(f"  ai:    " + "  ".join(f"{d}={s:.2f}" for d, s in sorted(ai, key=lambda t: t[1])))
    print(f"  human: " + "  ".join(f"{d}={s:.2f}" for d, s in sorted(hu, key=lambda t: t[1])))
    print(f"  self (post): {self_s:.3f}")
    n_ai_side = sum(1 for s, _ in tw
                    if direction * s > direction * (edge_hi + edge_lo) / 2)
    print(f"  tweets past midpoint threshold: {n_ai_side}/42  "
          f"extremes: {tw[0][1]}={tw[0][0]:.2f} .. {tw[-1][1]}={tw[-1][0]:.2f}")
    return a, margin_pct, loo_pass


if __name__ == "__main__":
    mod_path = Path(sys.argv[1] if len(sys.argv) > 1 else
                    Path(__file__).parent / "feature.py")
    spec = importlib.util.spec_from_file_location("feature", mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    evaluate(mod.score_doc)
