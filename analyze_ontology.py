"""Test the 'AI lacks ontology' claim: is-claims vs does-claims.

Motivated by https://solmaz.io/x/2071475602163654969/ ("Good READMEs say what
tools are") and the write-readme skill: GPT-flavored copy describes what a
tool *does* but rarely states what it *is*.
"""
import re
from pathlib import Path

CORPUS = Path(__file__).parent / "corpus"

# Subject aliases per document (the "thing being described").
SUBJECTS = {
    "crabbox": ["crabbox"],
    "mcporter": ["mcporter"],
    "gitcrawl": ["gitcrawl"],
    "clawpatch": ["clawpatch"],
    "fs-safe": ["fs-safe", "root()", "CODE"],
    "spogo": ["spogo"],
    "imsg": ["imsg", "CODE"],
    "wacli": ["wacli", "CODE"],
    "gogcli": ["gog", "CODE"],
    "goplaces": ["goplaces", "CODE"],
    "sqlite-testing": ["sqlite"],
    "joel-rewrite": ["netscape", "the code", "old code", "new code"],
    "antirez-terminology": ["redis", "terminology", "political correctness"],
    "ripgrep-2016": ["ripgrep", "rg", "CODE"],
    "requests-2017": ["requests"],
    "redis-2016": ["redis"],
}

IDENTITY = re.compile(r"^(?:is|are|was|were|'s|remains?)\s+(?:a|an|the|one|itself)\b", re.I)
PSEUDO = re.compile(r"^(?:is|are)\s+(?:designed|built|meant|intended|made)\b", re.I)


def load(path: Path) -> str:
    text = path.read_text()
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = "\n".join(
        l for l in text.splitlines()
        if not l.strip().startswith(("#", "|")) and l.strip()
    )
    text = re.sub(r"`[^`]+`", "CODE", text)
    return text


def sentences(text: str):
    t = text.replace("e.g.", "eg").replace("i.e.", "ie").replace("etc.", "etc")
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split()) >= 2]


def classify_opening(sent: str, aliases) -> str:
    """Identity (copula or bare NP), or verb-led."""
    s = sent.strip()
    low = s.lower()
    for a in aliases:
        al = a.lower()
        if low.startswith(al):
            rest = s[len(a):].strip()
            if IDENTITY.match(rest):
                return "identity (copula)"
            return "verb-led"
    # Bare noun-phrase opening: "A local-first GitHub triage tool for ..."
    if re.match(r"^(?:A|An|The)\s+[\w-]+", s) and not re.search(
        r"\b(runs?|sync(s|es)?|turns?|keeps?|streams?|maps?|builds?|reads?|talks?)\b",
        " ".join(s.split()[:6]), re.I,
    ):
        return "identity (bare NP)"
    return "verb-led"


print(f"{'doc':22} {'group':6} {'opening classification':24} {'name-subj':>9} "
      f"{'is-a':>5} {'does':>5} {'does:is':>8}")
for group in ("ai", "human"):
    for f in sorted((CORPUS / group).glob("*.md")):
        if f.stem not in SUBJECTS:  # pure essays: is/does framing not applicable
            continue
        text = load(f)
        sents = sentences(text)
        aliases = SUBJECTS[f.stem]
        opening = classify_opening(sents[0], aliases) if sents else "n/a"

        is_a = does = subj = 0
        for s in sents:
            low = s.lower()
            for a in aliases:
                al = a.lower()
                idx = low.find(al)
                # subject position: sentence start (allow one leading word like "But")
                if idx in (0,) or (0 < idx <= 15 and low[:idx].count(" ") <= 1):
                    rest = s[idx + len(a):].strip()
                    if not rest:
                        continue
                    subj += 1
                    if IDENTITY.match(rest) or PSEUDO.match(rest):
                        is_a += 1
                    elif re.match(r"^[a-z']", rest, re.I) and rest.split()[0].lower() not in ("and", "or"):
                        does += 1
                    break
        ratio = f"{does / is_a:.1f}" if is_a else ("inf" if does else "-")
        print(f"{f.stem:22} {group:6} {opening:24} {subj:>9} {is_a:>5} {does:>5} {ratio:>8}")

print("\nOpening sentences (first body sentence per doc):")
for group in ("ai", "human"):
    for f in sorted((CORPUS / group).glob("*.md")):
        sents = sentences(load(f))
        if sents:
            first = sents[0][:110] + ("..." if len(sents[0]) > 110 else "")
            print(f"  [{group}] {f.stem}: {first}")
