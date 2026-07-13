"""Multi-sentence cadence: does the document stamp one sentence shape?

analyze_rhythm.py measures how much adjacent sentence lengths differ.
These metrics look at the shape of each sentence (its clause structure)
and at runs of similar shapes across neighboring sentences, which is
where the generated essay cadence lives: long sentence after long
sentence, each balanced into clauses of similar size.

Per document:

- stamp_rate: share of adjacent sentence pairs with similar length
  (ratio under 1.5) and clause count within 1 of each other. High =
  the same sentence shape repeated back to back.
- clause_balance: over sentences with 3+ clauses, mean of
  min(clause)/max(clause) length within the sentence. High = clauses
  cut to matching sizes ("clause, clause, and clause").
- balanced_long_pct: share of sentences that are 18+ words, 3+ clauses,
  and internally balanced (min/max >= 0.4). The ChatGPT essay sentence
  as one number.
- drift: std of the rolling 5-sentence mean length divided by the std
  of the raw series. Low = the local cadence never wanders; high = the
  document moves between textures.

Run: python3 analyze_cadence.py (stdlib only)
"""
import json
import re
import statistics
from pathlib import Path

from analyze import load, split_sentences, CORPUS
from analyze_rhythm import clause_lengths


def sentence_shapes(path):
    body = "\n".join(
        re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l)
        for l in load(path).splitlines()
        if l.strip() and not re.match(r"\s*#{1,6}\s", l))
    shapes = []
    for s, n in split_sentences(body):
        shapes.append({"words": n, "clauses": clause_lengths(s)})
    return shapes


def analyze_cadence(path, group):
    shapes = sentence_shapes(path)
    lens = [s["words"] for s in shapes]
    n = len(shapes)

    similar = 0
    for a, b in zip(shapes, shapes[1:]):
        hi, lo = max(a["words"], b["words"]), min(a["words"], b["words"])
        if lo > 0 and hi / lo <= 1.5 and abs(len(a["clauses"]) - len(b["clauses"])) <= 1:
            similar += 1
    stamp_rate = similar / max(n - 1, 1)

    balances = []
    for s in shapes:
        c = s["clauses"]
        if len(c) >= 3:
            balances.append(min(c) / max(c))
    clause_balance = statistics.mean(balances) if balances else 0.0

    balanced_long = sum(
        1 for s in shapes
        if s["words"] >= 18 and len(s["clauses"]) >= 3
        and min(s["clauses"]) / max(s["clauses"]) >= 0.4)
    balanced_long_pct = 100 * balanced_long / max(n, 1)

    drift = 0.0
    if n >= 8:
        w = 5
        rolling = [statistics.mean(lens[i:i + w]) for i in range(n - w + 1)]
        sd = statistics.stdev(lens)
        drift = statistics.stdev(rolling) / sd if sd else 0.0

    return {
        "doc": path.stem,
        "group": group,
        "sentences": n,
        "stamp_rate": round(100 * stamp_rate, 1),
        "clause_balance": round(clause_balance, 2),
        "balanced_long_pct": round(balanced_long_pct, 1),
        "drift": round(drift, 2),
    }


if __name__ == "__main__":
    rows = []
    for group in ("ai", "human", "tweets", "self"):
        for f in sorted((CORPUS / group).glob("*.md")):
            rows.append(analyze_cadence(f, group))

    keys = [k for k in rows[0] if k not in ("doc", "group")]
    print("\t".join(["doc", "group"] + keys))
    for r in rows:
        if r["group"] != "tweets":
            print("\t".join([r["doc"], r["group"]] + [str(r[k]) for k in keys]))

    print("\ngroup summaries (mean [min..max]):")
    for group in ("ai", "human", "tweets", "self"):
        g = [r for r in rows if r["group"] == group]
        line = f"  {group:7s}"
        for k in keys:
            if k == "sentences":
                continue
            vals = [r[k] for r in g]
            line += f"  {k}={statistics.mean(vals):.2f} [{min(vals):.2f}..{max(vals):.2f}]"
        print(line)

    (Path(__file__).resolve().parent / "results_cadence.json").write_text(
        json.dumps({"docs": rows}, indent=2))
