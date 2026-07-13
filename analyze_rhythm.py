"""Sequential rhythm of sentence and clause lengths.

The global coefficient of variation in analyze.py ignores order: a text
that alternates short and long sentences scores the same as one with all
its short sentences bunched together. These metrics look at the sequence.

- npvi_sent: normalized Pairwise Variability Index over the sentence
  length series, 100 * mean(|a-b| / ((a+b)/2)) for adjacent pairs. The
  standard speech-rhythm measure (Grabe & Low 2002); 0 = every sentence
  the same length as its neighbor, higher = more local alternation.
- ac1_sent: lag-1 autocorrelation of sentence lengths. Positive = long
  sentences cluster in runs, negative = lengths alternate, zero = no
  sequential structure.
- npvi_clause / ac1_clause: the same over clause lengths, where clauses
  are the chunks between commas, semicolons, colons, dashes, and
  parentheses, plus sentence boundaries.
- clause_words: mean clause length in words.

Run: python3 analyze_rhythm.py (stdlib only)
"""
import json
import re
import statistics
from pathlib import Path

from analyze import load, split_sentences, CORPUS


def npvi(series):
    pairs = [(a, b) for a, b in zip(series, series[1:]) if a + b > 0]
    if not pairs:
        return 0.0
    return 100 * statistics.mean(2 * abs(a - b) / (a + b) for a, b in pairs)


def autocorr1(series):
    n = len(series)
    if n < 3:
        return 0.0
    mu = statistics.mean(series)
    var = sum((x - mu) ** 2 for x in series)
    if var == 0:
        return 0.0
    return sum((series[i] - mu) * (series[i + 1] - mu) for i in range(n - 1)) / var


def clause_lengths(sentence):
    chunks = re.split(r"[,;:—()]|\s--\s|\s-\s", sentence)
    return [len(re.findall(r"[\w'’-]+", c)) for c in chunks
            if re.findall(r"[\w'’-]+", c)]


def analyze_rhythm(path, group):
    body = "\n".join(
        re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l)
        for l in load(path).splitlines()
        if l.strip() and not re.match(r"\s*#{1,6}\s", l))
    sents = split_sentences(body)
    sent_lens = [n for _, n in sents]
    clauses = [c for s, _ in sents for c in clause_lengths(s)]
    return {
        "doc": path.stem,
        "group": group,
        "sentences": len(sent_lens),
        "npvi_sent": round(npvi(sent_lens), 1),
        "ac1_sent": round(autocorr1(sent_lens), 2),
        "clause_words": round(statistics.mean(clauses), 1),
        "npvi_clause": round(npvi(clauses), 1),
        "ac1_clause": round(autocorr1(clauses), 2),
    }


if __name__ == "__main__":
    rows = []
    for group in ("ai", "human", "tweets", "self"):
        for f in sorted((CORPUS / group).glob("*.md")):
            rows.append(analyze_rhythm(f, group))

    keys = [k for k in rows[0] if k not in ("doc", "group")]
    print("\t".join(["doc", "group"] + keys))
    for r in rows:
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

    (Path(__file__).resolve().parent / "results_rhythm.json").write_text(
        json.dumps({"docs": rows}, indent=2))
