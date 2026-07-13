"""Lexical diversity and word complexity across the corpus groups.

Metrics per document, all computed on the same stripped text as analyze.py:

- mtld: Measure of Textual Lexical Diversity (McCarthy & Jarvis 2010),
  length-insensitive unlike raw TTR. Higher = more diverse vocabulary.
- mean_word_len: mean characters per alphabetic word.
- long_word_pct: share of words with 7+ characters.
- syllables_per_word: heuristic syllable count per word.
- fk_grade: Flesch-Kincaid grade level (needs sentences; uses the same
  splitter as analyze.py).
- zipf_mean / rare_word_pct: mean Zipf frequency of content words and the
  share below Zipf 3.0 (roughly "outside the top ~30k words"), via the
  wordfreq package. Lower zipf_mean = rarer vocabulary.

Run: uv run --with wordfreq python3 analyze_lexical.py
"""
import json
import re
import statistics
from pathlib import Path

from analyze import load, split_sentences, CORPUS

try:
    from wordfreq import zipf_frequency
except ImportError:
    zipf_frequency = None

VOWELS = "aeiouy"


def syllables(word):
    w = word.lower().strip("'’")
    if not w:
        return 0
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and groups > 1:
        groups -= 1
    return max(groups, 1)


def mtld_pass(tokens, threshold=0.72):
    factors, types, count = 0.0, set(), 0
    for t in tokens:
        count += 1
        types.add(t)
        if len(types) / count <= threshold:
            factors += 1
            types, count = set(), 0
    if count:
        factors += (1 - len(types) / count) / (1 - threshold)
    return len(tokens) / factors if factors else float("inf")


def mtld(tokens):
    return (mtld_pass(tokens) + mtld_pass(tokens[::-1])) / 2


def analyze_lexical(path, group):
    text = " ".join(
        re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l)
        for l in load(path).splitlines()
        if l.strip() and not re.match(r"\s*#{1,6}\s", l)
    )
    words = [w for w in re.findall(r"[A-Za-z'’-]+", text) if w.upper() != "CODE"]
    tokens = [w.lower() for w in words]
    n = len(tokens)

    syl = [syllables(w) for w in words]
    sents = split_sentences(text)
    words_per_sent = n / max(len(sents), 1)
    syl_per_word = sum(syl) / n
    fk_grade = 0.39 * words_per_sent + 11.8 * syl_per_word - 15.59

    row = {
        "doc": path.stem,
        "group": group,
        "words": n,
        "mtld": round(mtld(tokens), 1),
        "mean_word_len": round(sum(len(w) for w in words) / n, 2),
        "long_word_pct": round(100 * sum(1 for w in words if len(w) >= 7) / n, 1),
        "syllables_per_word": round(syl_per_word, 2),
        "fk_grade": round(fk_grade, 1),
    }
    if zipf_frequency:
        zipfs = [zipf_frequency(t, "en") for t in tokens]
        known = [z for z in zipfs if z > 0]
        row["zipf_mean"] = round(statistics.mean(known), 2)
        row["rare_word_pct"] = round(
            100 * sum(1 for z in zipfs if 0 < z < 3.0) / n, 1)
    return row


if __name__ == "__main__":
    rows = []
    for group in ("ai", "human", "tweets", "self"):
        for f in sorted((CORPUS / group).glob("*.md")):
            rows.append(analyze_lexical(f, group))

    keys = [k for k in rows[0] if k not in ("doc", "group")]
    print("\t".join(["doc", "group"] + keys))
    for r in rows:
        print("\t".join([r["doc"], r["group"]] + [str(r[k]) for k in keys]))

    print("\ngroup summaries (mean [min..max]):")
    for group in ("ai", "human", "tweets", "self"):
        g = [r for r in rows if r["group"] == group]
        line = f"  {group:7s}"
        for k in keys:
            if k == "words":
                continue
            vals = [r[k] for r in g]
            line += f"  {k}={statistics.mean(vals):.2f} [{min(vals):.2f}..{max(vals):.2f}]"
        print(line)

    (Path(__file__).resolve().parent / "results_lexical.json").write_text(
        json.dumps({"docs": rows}, indent=2))
