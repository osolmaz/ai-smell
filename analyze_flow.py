"""Sentence flow: the run-percentile metric found by the autoresearch loop.

For each sentence, take its longest run: the longest stretch of words
with no punctuation break (sentences are split at commas, semicolons,
colons, dashes, and parentheses; the longest piece is the run). Rank
that run length against every run in the whole corpus using the pooled
empirical CDF, which turns it into a percentile in [0, 1] and replaces
any hand-picked word-count threshold. The document's flow score is the
mean percentile:

    flow = (1/n) * sum_i F(run_i)

This is the Mann-Whitney/Wilcoxon rank-sum statistic of the document's
runs against the corpus pool: the probability that a randomly chosen
sentence-run from the document is longer than a randomly chosen run
from the corpus. Human prose keeps producing sentences with one long
unbroken run and scores high; the AI landing pages break every sentence
with punctuation before a run can develop and score low. On the
ground-truth corpus the groups separate completely (AUC 1.000,
leave-one-out 18/18).

The metric came out of an autoresearch-style search; the full history,
including the sliding-window generalization S_k and why it collapses
back to this S_1 form, is in autoresearch/journal.md.

Run: python3 analyze_flow.py
"""
import bisect
import json
import re
import statistics
from pathlib import Path

from analyze import load, split_sentences, CORPUS
from analyze_rhythm import clause_lengths

GROUPS = ("ai", "human", "tweets", "self")


def doc_spines(path):
    body = "\n".join(
        re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l)
        for l in load(path).splitlines()
        if l.strip() and not re.match(r"\s*#{1,6}\s", l))
    return [max(clause_lengths(s)) for s, _ in split_sentences(body)
            if clause_lengths(s)]


if __name__ == "__main__":
    spines = {}
    for group in GROUPS:
        for f in sorted((CORPUS / group).glob("*.md")):
            spines[(group, f.stem)] = doc_spines(f)

    pool = sorted(v for sp in spines.values() for v in sp)

    def cdf(v):
        return (bisect.bisect_left(pool, v) + bisect.bisect_right(pool, v)) / 2 / len(pool)

    rows = []
    for (group, doc), sp in spines.items():
        rows.append({
            "doc": doc,
            "group": group,
            "sentences": len(sp),
            "mean_run": round(statistics.mean(sp), 1),
            "flow": round(sum(cdf(v) for v in sp) / len(sp), 3),
            "spines": sp,
        })

    print("doc\tgroup\tsentences\tmean_run\tflow")
    for r in rows:
        print(f"{r['doc']}\t{r['group']}\t{r['sentences']}\t{r['mean_run']}\t{r['flow']}")

    print("\ngroup summaries (mean [min..max]):")
    for group in GROUPS:
        vals = [r["flow"] for r in rows if r["group"] == group]
        print(f"  {group:7s}  flow={statistics.mean(vals):.3f} "
              f"[{min(vals):.3f}..{max(vals):.3f}]")

    edge_ai = max(r["flow"] for r in rows if r["group"] == "ai")
    edge_hu = min(r["flow"] for r in rows if r["group"] == "human")
    thr = (edge_ai + edge_hu) / 2
    n_below = sum(1 for r in rows if r["group"] == "tweets" and r["flow"] < thr)
    print(f"\nedges: worst AI {edge_ai:.3f}, flattest human {edge_hu:.3f}, "
          f"midpoint threshold {thr:.3f}")
    print(f"tweet samples below threshold: {n_below}/"
          f"{sum(1 for r in rows if r['group'] == 'tweets')}")

    (Path(__file__).resolve().parent / "results_flow.json").write_text(
        json.dumps({"docs": rows, "edges": {
            "ai": round(edge_ai, 3), "human": round(edge_hu, 3),
            "threshold": round(thr, 3)}}, indent=2))
