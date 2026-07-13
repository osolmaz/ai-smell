"""Constant-free variant (exp H): consecutive rank flow.

Rank each sentence's longest clause against the pooled spine
distribution of the whole unlabeled corpus (the empirical CDF stands in
for any word-count constant), then convolve with a product kernel over
adjacent sentence pairs: score = mean of F(spine_i) * F(spine_i+1).

A document scores high only when flowing sentences come consecutively.
That is the sequential part of the tell: the same rank transform
averaged per sentence in isolation gives a 17% margin, and requiring
two in a row gives 35%.

On the ground-truth corpus: auc 1.000, leave-one-out 18/18, margin
+35% (crabbox 0.17 vs ripgrep 2016 at 0.24). The fixed-ramp feature.py
still holds the widest margin (+55%) but encodes the 10-to-15-word
ramp; this variant's only structural choices are the adjacent pair and
the corpus-derived CDF.

The sweep in sweep2.py also records the negative result: every pure
order statistic with the level removed (von Neumann ratio, turning
points, permutation-normalized jaggedness, Spearman lag-1, adjacent
min/max ratios, rank nPVI) fails to separate the groups (auc 0.51 to
0.89). The rhythm tell needs the level; sequence order alone does not
carry it.
"""
import bisect
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harness import load_corpus

_POOL = None


def _pool():
    global _POOL
    if _POOL is None:
        _POOL = sorted(
            max(s["clauses"]) for seq in load_corpus().values()
            for s in seq if s["clauses"])
    return _POOL


def _cdf(v):
    p = _pool()
    return (bisect.bisect_left(p, v) + bisect.bisect_right(p, v)) / 2 / len(p)


def score_doc(seq):
    f = [_cdf(max(s["clauses"])) for s in seq if s["clauses"]]
    if len(f) < 2:
        return 0.0
    return sum(a * b for a, b in zip(f, f[1:])) / (len(f) - 1)
