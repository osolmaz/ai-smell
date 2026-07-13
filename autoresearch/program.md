# Rhythm-tell autoresearch program

Goal: find a scalar feature of the sentence sequence (word counts and
clause lengths per sentence, in document order) that separates the 10 AI
landing pages from the 8 human baselines as widely as possible.

Rules, in the spirit of karpathy/autoresearch:

- `harness.py` is fixed. Only `feature.py` is edited between runs.
- `feature.py` must define `score_doc(seq)` where `seq` is a list of
  `{"words": int, "clauses": [int, ...]}` in document order. Stdlib only.
- The feature must read the sequence, not the text: rhythm, cadence,
  length evolution, clause structure, windowed and convolution-style
  statistics are in bounds; anything lexical is out of bounds.
- One experiment = one edit to `feature.py`, then `python3 harness.py`.
- Keep a result only if auc = 1.000 and loo = 18/18; among keepers,
  maximize margin_pct. Log every run in `journal.md` with the idea, the
  numbers, and keep/discard.
- The self and tweets numbers are context only; never select on them.
