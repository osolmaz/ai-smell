"""Stylometric comparison of AI-flavored landing copy vs pre-LLM human prose."""
import json
import re
import statistics
from collections import Counter
from pathlib import Path

CORPUS = Path(__file__).resolve().parent / "corpus"

ABBREV = ["e.g.", "i.e.", "vs.", "etc.", "Mr.", "Dr.", "St.", "cf.", "approx."]


def load(path: Path) -> str:
    text = path.read_text()
    # strip fenced code blocks and tables
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = "\n".join(l for l in text.splitlines() if not l.strip().startswith("|"))
    # inline code -> neutral token so punctuation inside code doesn't count
    text = re.sub(r"`[^`]+`", "CODE", text)
    return text


def split_sentences(prose: str):
    t = prose
    for a in ABBREV:
        t = t.replace(a, a.replace(".", "\u0000"))
    # protect decimals / version numbers
    t = re.sub(r"(\d)\.(\d)", "\\1\u0000\\2", t)
    parts = re.split(r"(?<=[.!?])\s+", t)
    out = []
    for p in parts:
        p = p.replace("\u0000", ".").strip()
        words = re.findall(r"[A-Za-z0-9'’-]+", p)
        if len(words) >= 1:
            out.append((p, len(words)))
    return out


def analyze(path: Path, group: str):
    raw = load(path)
    lines = [l for l in raw.splitlines() if l.strip()]
    headings = [l for l in lines if re.match(r"\s*#{1,6}\s", l)]
    bullets = [l for l in lines if re.match(r"\s*([-*+]|\d+\.)\s", l)]
    body_lines = [l for l in lines if l not in headings]
    # drop list markers so they don't count as spaced-hyphen dashes
    stripped_body = [re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l) for l in body_lines]
    text = " ".join(stripped_body)
    words = re.findall(r"[A-Za-z0-9'’-]+", text)
    n_words = len(words)
    k = 1000.0 / n_words

    sents = split_sentences("\n".join(body_lines))
    lens = [n for _, n in sents]
    mean_len = statistics.mean(lens)
    stdev_len = statistics.stdev(lens)

    # punctuation (em dash: — or -- or spaced hyphen used as dash)
    em = len(re.findall(r"—|--| - ", text))
    semi = text.count(";")
    colon = len(re.findall(r"[a-zA-Z]:\s", text))

    # labeled bullets: "- Label — desc", "- **Label.** desc", "- Label. desc" (label <= 5 words)
    labeled = 0
    for b in bullets:
        m = re.match(r"\s*[-*+]\s+(?:\*\*)?([^—:.]{1,60}?)(?:\*\*)?\s*(?:[—:.]|\u2014)\s+\S", b)
        if m and len(m.group(1).split()) <= 5:
            labeled += 1

    # tells
    contrast = len(re.findall(r",\s*not\s+|\bnot\s+\w+[^.;]{0,30},\s*but\b|\bUnlike\b|\brather than\b|\binstead of\b", text))
    notjust = len(re.findall(r"\bnot (just|only|merely)\b", text, re.I))
    triads = len(re.findall(r"\b[\w'’-]+,\s+[\w'’-]+,\s+and\s+[\w'’-]+\b", text))
    longlists = len(re.findall(r"\b[\w'’-]+(?:,\s+[\w'’-]+){3,},?\s+(?:and|or)\s+[\w'’-]+\b", text))
    no_anaphora = len(re.findall(r"\bno\s+[\w-]+(?:\s+[\w-]+)?,\s*no\s+[\w-]+", text, re.I))

    # sentence openers
    openers = Counter(s.split()[0].lower() for s, n in sents if n >= 3)

    # pronouns
    fp = sum(1 for w in words if w.lower() in ("i", "we", "my", "our", "me", "us"))
    sp = sum(1 for w in words if w.lower() in ("you", "your", "yours"))

    # fragments (verbless punch): sentences <= 4 words
    frags = sum(1 for _, n in sents if n <= 4)
    long_s = sum(1 for _, n in sents if n >= 35)

    # lexical diversity on a fixed window for comparability (shortest doc ~280 words)
    window = [w.lower() for w in words[:280]]
    ttr = len(set(window)) / len(window)

    hist = Counter()
    for n in lens:
        hist[min(n // 5 * 5, 50)] += 1

    return {
        "doc": path.stem,
        "group": group,
        "words": n_words,
        "sentences": len(sents),
        "mean_sentence_len": round(mean_len, 1),
        "stdev_sentence_len": round(stdev_len, 1),
        "cv_sentence_len": round(stdev_len / mean_len, 2),
        "frag_pct": round(100 * frags / len(sents), 1),
        "long_pct": round(100 * long_s / len(sents), 1),
        "em_dash_per_1k": round(em * k, 1),
        "semicolon_per_1k": round(semi * k, 1),
        "colon_per_1k": round(colon * k, 1),
        "bullet_line_pct": round(100 * len(bullets) / max(len(lines), 1), 1),
        "labeled_bullets": labeled,
        "labeled_bullet_pct_of_bullets": round(100 * labeled / len(bullets), 1) if bullets else 0.0,
        "headings_per_1k": round(len(headings) * k, 1),
        "contrast_per_1k": round(contrast * k, 2),
        "not_just_per_1k": round(notjust * k, 2),
        "triads_per_1k": round(triads * k, 2),
        "long_lists_per_1k": round(longlists * k, 2),
        "no_anaphora": no_anaphora,
        "first_person_per_1k": round(fp * k, 1),
        "second_person_per_1k": round(sp * k, 1),
        "ttr_280": round(ttr, 3),
        "top_openers": openers.most_common(5),
        "len_hist": dict(sorted(hist.items())),
    }


results = []
for group in ("ai", "human", "tweets"):
    for f in sorted((CORPUS / group).glob("*.md")):
        results.append(analyze(f, group))

# cross-document template phrases within the AI set
ai_texts = {f.stem: load(f).lower() for f in (CORPUS / "ai").glob("*.md")}
phrases = [
    "pick your path", "out of scope", "five minutes", "released under the mit license",
    "for agents", "status", "quickstart", "why ", "— see", "agent-friendly",
]
templates = {p: sorted(d for d, t in ai_texts.items() if p in t) for p in phrases}

out = {"docs": results, "ai_shared_phrases": templates}
(Path(__file__).resolve().parent / "results.json").write_text(json.dumps(out, indent=2))

hdr = ["doc", "group", "words", "mean_sentence_len", "cv_sentence_len", "frag_pct",
       "em_dash_per_1k", "semicolon_per_1k", "colon_per_1k", "bullet_line_pct",
       "labeled_bullet_pct_of_bullets", "contrast_per_1k", "triads_per_1k",
       "no_anaphora", "first_person_per_1k", "second_person_per_1k", "ttr_280"]
print("\t".join(hdr))
for r in results:
    print("\t".join(str(r[h]) for h in hdr))
print("\nAI-set shared template phrases:")
for p, docs in templates.items():
    if len(docs) >= 2:
        print(f"  {p!r}: {len(docs)}/{len(ai_texts)} -> {', '.join(docs)}")
print("\nTop sentence openers per doc:")
for r in results:
    print(f"  {r['doc']} ({r['group']}): {r['top_openers']}")
