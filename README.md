# ai-smell

This repository is a stylometric study of AI writing tells: the corpus,
scripts, results, and figures behind the blog post
[Building an AI de-smeller](https://solmaz.io/ai-de-smeller) and the
[kill-ai-smell](https://github.com/osolmaz/tools/blob/main/agents/skills/kill-ai-smell/SKILL.md)
agent skill. The starting point was an observation that several OpenClaw
project landing pages read as AI-written. Instead of cleaning them up, we
kept them as specimens and asked whether the tells could be measured, and
which ones separate generated copy from human writing most cleanly. The
study was later expanded from 9 to 18 ground-truth documents to control
for register, plus 42 in-the-wild tweet samples.

The AI side of the corpus is the landing and docs copy of ten OpenClaw
project sites (crabbox.sh, mcporter.sh, gitcrawl.sh, clawpatch.ai,
fs-safe.io, spogo.sh, imsg.sh, wacli.sh, gogcli.sh, goplaces.sh), 4,853
words of prose after stripping code blocks. The human side is eight texts
that are provably human because they were frozen before language models
existed, 15,317 words in total. Five are essays and documentation: the
SQLite testing documentation, Joel Spolsky's 2000 essay on rewrites, a
2018 antirez blog post, Paul Graham's 2009 "Maker's Schedule, Manager's
Schedule", and Julia Evans' 2019 brag-documents post. Three are READMEs
captured at old git tags, whose commit history proves their date and whose
register matches the AI pages: ripgrep at 0.4.0 (2016), Redis at 3.2.0
(2016), and Requests at v2.13.0 (2017). All rates below are normalized per
1,000 words so the corpora are comparable.

## What was measured

The main script (`analyze.py`) strips code blocks and inline code, then
measures each document for punctuation rates (em dashes, semicolons,
colons), sentence-length distribution and fragment share, bullet-line
share and labeled bullets (a bullet that opens with a label of at most
five words, then a period, colon, or dash, then elaboration, reported
as a share of all bullets), contrast rhetoric, exactly-three lists,
anaphora chains, first- and second-person rates, type-token ratio,
sentence openers, and template phrases shared across the AI sites. Two
follow-up scripts test claims from existing writing guidance.
`analyze_ontology.py` tests the identity-deferral claim from the solmaz.io
post "Good READMEs say what tools are" and the write-readme skill.
`analyze_headings.py` classifies every heading against the write-monograph
title rules. Full numbers land in `results.json`.

## Headline numbers

The table gives the range across documents in each group.

| Metric | AI set (10 docs) | Human set (8 docs) |
| --- | --- | --- |
| Em dashes /1k | 0.0–61.3 | 0.0–4.7 |
| Exactly-three lists /1k | 6.3–15.9 | 0.0–2.0 |
| Labeled bullets, % of bullets | 53–100% | 0–11% |
| Fragment sentences (≤4 words) | 3.6–41.9% | 1.4–17.4% |
| First person /1k | 0.0–2.1 | 0.0–50.9 |
| Type-token ratio (first 280 words) | 0.59–0.69 | 0.53–0.67 |

The triad and labeled-bullet gaps have no overlap between groups. The
notorious AI vocabulary ("delve", "landscape") barely appears in either
corpus, so on this evidence the strongest tells are structural.

## Findings

**1. Labeled bullets are the signature layout unit.** Between 53% and 100%
of bullets on the AI pages follow one shape, a short noun-phrase label
followed by a separator and one sentence of elaboration ("Zero-config
discovery. Reads your home config..."). The human baselines top out at 11%
(the 2016 Redis README), and five of the eight never write the shape at
all. This one feature separates the corpora more cleanly than em dashes.

**2. Sentence rhythm is bimodal.** AI copy alternates verbless punches of
two to four words ("Actively developed.") with feature enumerations of 25
words or more. Human prose keeps a steadier band. Joel Spolsky also writes
short sentences, but his are full clauses with subjects and verbs.

**3. Enumeration comes in threes, or goes maximal.** Exactly-three lists
run 6 to 16 per 1,000 words in the AI set against 0 to 2 in the baselines,
about nineteen-fold on the corpus averages with no overlap at the edges.
When AI copy exceeds three items it chains five to seven verb phrases with
semicolons, which makes wacli and crabbox the semicolon outliers at 11 to
16 per 1,000 words while every human text stays under 3.

**4. The em dash is a one-directional tell.** The corpus averages differ
roughly eighteen-fold, and the heaviest page (clawpatch) lands one em dash
every sixteen words. But three AI pages use fewer em dashes than the 2016
ripgrep README and gogcli uses none, so a page drowning in dashes is
almost certainly generated while a page without them proves nothing.

**5. First person and lexical diversity are register signals.** Against
essays alone both looked like strong tells: the whole AI set contains a
single first-person word while every essay has a narrator. The pre-LLM
READMEs broke both metrics. The Requests README has zero first person and
scores a type-token ratio right among the AI pages. What survives is the
qualitative human tendency to repeat deliberately for emphasis (Joel opens
three consecutive paragraphs with "You are throwing away..."), while
generated copy swaps in a fresh synonym at every mention.

**6. One skeleton ships across the ten sites.** "Pick your path" appears
on six sites, a "five minutes" time-to-value promise on seven, a "Status"
section on eight, and the exact closer "Released under the MIT license."
on six. Each page looks fine alone. Side by side they reveal a house style
produced by one prompt.

**7. Openings defer identity.** The solmaz.io claim holds with a nuance.
All three pre-LLM READMEs establish identity in their opening lines
("ripgrep is a line oriented search tool...", "Requests is the only
Non-GMO HTTP library...", Redis's first section heading is literally
"What is Redis?"). Among the ten AI pages exactly one (clawpatch) opens
with a copula. Four open with headless noun-phrase fragments that carry
category information with no subject and no verb (gitcrawl, spogo, wacli,
goplaces), and the remaining five open with imperative benefits or setup
instructions. Counting sentences where the tool name is the grammatical
subject, action predicates outnumber identity predicates 26 to 5 across
the AI set. The raw ratio alone does not separate the groups, because
body prose about a known subject is naturally verb-led (SQLite runs 18 to
2). The tell is positional.

**8. Heading style inverts the expected offense.** Classifying all 94 AI
headings and 80 human headings against the write-monograph title rules
produced an inversion. Title Case belongs to the humans here, appearing in
8 of 39 SQLite headings ("Boundary Value Tests") as a convention of its
era, while the AI pages already write sentence case. The AI headings fail
differently. About a third are rhetoric rather than labels, against one in
ten for the humans, and the human flags are mostly mild FAQ questions
("Why should I use ripgrep?"). The comma couplet, a parallel two-beat
slogan ("Local loop, remote box", "Two jobs, one binary", "Small surface,
clear split"), appears eleven times across five AI sites and once in the
human set, as the deliberate title "Maker's Schedule, Manager's Schedule".
Imperative slogans ("Pick your path", "Reuse what's warm") and wh-frames
("Why spogo", "What you get") fill out the rest, and gitcrawl stamps one
frame four times in a row ("I want to try it / wire up an agent / triage
a busy repo").

## Long-form tweets in the wild

A third corpus group (`corpus/tweets/`, built by `sample_tweets.py` from
the private xtap-store archive) holds one sample per account: every
original long-form tweet (>280 chars), date-sorted, for the 42 accounts
with at least 2,000 words of such text. There is no ground truth for
these. Applying the page detector unchanged, seven of the 42 accounts
trip it: four cross the triad line (topped by 5.4 per 1,000 words) and
three cross the labeled-bullet line (topped by a 78% share), and none
crosses both, unlike the landing pages where every document sat far past
both thresholds at once. The bullet share rests on smaller counts in the
feed, since threads carry far fewer bullets than landing pages, and one
flagged account crosses on just two labeled bullets, so the thresholds
transfer but the confidence does not. The motivating account (analogalok)
is one of the three past the bullet line, with 41 labeled bullets out of
90 (46%) while its dash and triad rates sit mid-field. Its long posts
also share a hook template ("Let me explain", "It's not X. It's Y.")
that these counters do not measure.

## A minimal detector

Two thresholds each classify all eighteen documents correctly on their
own: exactly-three lists above 3 per 1,000 words, or labeled-bullet share
above 30% of bullets. The em dash dropped out of the detector because its
absence clears nothing (see finding 4), and first person dropped out as a
register signal (finding 5). With eighteen documents these numbers are
still hypotheses rather than a validated classifier. The register
objection is partially addressed by the three pre-LLM READMEs, which sell
tools the way the AI pages do; the natural next escalation is a large
sample of post-LLM, human-written landing pages.

## Contents and reproduction

The corpus lives in `corpus/ai/` (the ten site pages, fetched 2026-07-13),
`corpus/human/` (the eight baselines; the essays were fetched by
`fetch_human.py` or by hand, the READMEs from raw.githubusercontent.com at
their tags), `corpus/tweets/` (the 42 account samples, built by
`sample_tweets.py` from a private tweet archive), and `corpus/self/` (the
blog post itself, archived as measured).

To reproduce the numbers, run `python3 analyze.py`, which writes
`results.json` and prints the per-document table. `analyze_ontology.py`
covers finding 7, `analyze_headings.py` covers finding 8, and
`analyze_lexical.py` (run via `uv run --with wordfreq python3
analyze_lexical.py`) writes `results_lexical.json` with MTLD lexical
diversity, word length, syllable, readability, and Zipf word-frequency
metrics. `export_web_data.py` writes `figures/data.json`, the compact
per-document dataset behind the blog post's interactive Chart.js
figures, and `render_figures.py` renders the blog figures into
`figures/` (it needs matplotlib and adjustText, for example via `uv run
--with matplotlib --with adjustText python3 render_figures.py`). All
scripts resolve the corpus relative to the repository root.

## License

[MIT](LICENSE)
