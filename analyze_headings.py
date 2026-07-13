"""Classify corpus headings against the write-monograph title rules.

Rules tested (agents/skills/write-monograph/SKILL.md, "Title Formatting"):
labels not sentences/slogans; sentence case not Title Case; no rote leading
"The"; no repeated rhetorical frame across sibling headings.
"""
import re
from collections import Counter
from pathlib import Path

CORPUS = Path(__file__).parent / "corpus"

# Base-form verbs that mark an imperative/slogan heading when they lead.
IMPERATIVES = {
    "keep", "reuse", "pick", "drive", "drop", "warm", "sync", "run", "use",
    "try", "get", "start", "read", "open", "jump", "think", "explore", "see",
    "install", "wire", "make", "build", "plays",
}
WH_FRAMES = re.compile(r"^(why|how|what|where)\b", re.I)


def headings(path: Path):
    out = []
    for line in path.read_text().splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            text = re.sub(r"`([^`]*)`", r"\1", m.group(2)).strip()
            text = re.sub(r"^#?\d+(\.\d+)*\.?\s*", "", text)  # strip manual numbers
            if text:
                out.append((len(m.group(1)), text))
    return out


def is_title_case(h: str) -> bool:
    words = [w for w in re.findall(r"[A-Za-z][\w'-]*", h)[1:] if len(w) > 3]
    if len(words) < 2:
        return False
    return sum(1 for w in words if w[0].isupper()) >= max(2, len(words) - 1)


def classify(h: str):
    tags = []
    first = re.findall(r"[A-Za-z][\w'-]*", h.lower())
    if not first:
        return tags
    if first[0] in IMPERATIVES:
        tags.append("imperative/slogan")
    if WH_FRAMES.match(h) or h.endswith("?"):
        tags.append("wh-frame or question")
    if "," in h and len(h.split()) <= 7:
        tags.append("comma couplet")
    if first[0] == "the" and len(first) > 1:
        tags.append("leading The")
    if is_title_case(h):
        tags.append("Title Case")
    if re.search(r"\b(is|are|was|does|has|have|fits|caps|stays?|hit|land)\b", h.lower()) or "imperative/slogan" in tags:
        tags.append("sentence/clause")
    return tags


all_rows = []
for group in ("ai", "human"):
    for f in sorted((CORPUS / group).glob("*.md")):
        hs = headings(f)
        if not hs:
            print(f"[{group}] {f.stem}: no headings (essay register)")
            continue
        tag_counter = Counter()
        flagged = []
        frame_starts = Counter(re.findall(r"^[\w'-]+", h)[0].lower() for _, h in hs if re.findall(r"^[\w'-]+", h))
        for _, h in hs:
            tags = classify(h)
            for t in tags:
                tag_counter[t] += 1
            if tags:
                flagged.append((h, tags))
        runs = {w: c for w, c in frame_starts.items() if c >= 3}
        n = len(hs)
        label_like = n - sum(1 for _, h in hs if classify(h))
        print(f"\n[{group}] {f.stem}: {n} headings, {label_like} clean noun-phrase labels")
        for t, c in tag_counter.most_common():
            print(f"    {t}: {c}/{n}")
        if runs:
            print(f"    repeated first-word frames: {runs}")
        for h, tags in flagged:
            print(f"      - {h!r}: {', '.join(tags)}")
