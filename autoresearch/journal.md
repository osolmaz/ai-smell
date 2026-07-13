# Experiment journal

Metric to maximize: margin_pct (gap at the closest edge as a share of
the midpoint), subject to auc = 1.000 and leave-one-out 18/18. The
feature sees only the sentence sequence: per-sentence word counts and
clause lengths, in order. 46 experiments run on 2026-07-14.

## Generation 1: pooled clause statistics (exps 1-8)

- Exp 1, mean clause length (the known separator): margin +1.1%, loo
  16/18. Separates but the edge is a coin flip (gitcrawl 5.59 vs
  ripgrep 5.65). Baseline.
- Exp 3 median clause, exp 4 sentence-weighted mean: +9.6% at best.
- Exp 2 long-clause share, exp 5 short-run length, exp 6 windowed
  convolution of clause means, exp 7 rolling-min sentence length, exp 8
  fully-telegraphic-sentence share: all fail auc 1.000. The pooled
  distribution of clause lengths is mostly shared between the groups;
  the signal had to be per-sentence. DISCARDED.

## Generation 2: the sentence's longest clause (exps 9-15)

The pivot that worked: score each sentence by its single longest clause
(its "spine"), then aggregate.

- Exp 9, mean spine: +12.5%, loo 18/18. First solid keeper.
- Exps 10-15 (median spine, spine share at threshold 10, worst-window
  spines, word-weighted, capped, log-mean): +7.6% to +28.1%. The share
  form (exp 11) beat the mean forms.

## Generation 3: where do the spines sit in the sequence (exps 19-26, 29-31)

- Exp 21, longest spineless run (drought) normalized by length: +36.7%.
- Exp 23, drought at spine threshold 11: +37.5%.
- Exp 29, windowed drought (length-robust): +22.9%.
- Run-mass and RMS variants (24-26), worst-window share (30), 90th
  percentile run (31): weaker or loo failures. Droughts are good but
  not the peak.

## Generation 4: threshold sweep on spine share (exps 16-18, 27-28, t15-t18)

- Share of sentences whose spine reaches t words, for t = 9..18:
  +14.0, +28.1, +29.1, +30.6, +34.8, +54.4 (t=14), +57.7 (t=15), then
  collapse to -3.0 at t=16. The t=15 peak is a knife edge (crabbox and
  ripgrep swap sides one threshold later). DISCARDED as overfit.

## Generation 5: smooth ramps and combinations (exps 32-46)

- Exp 34-36, 39 and the parameter sweep: replace the hard threshold
  with a linear ramp on the spine. Margins +39% to +54% across every
  parameterization tried (8-14, 9-14, 10-14, 9-15, 9-16, 10-16, 11-16,
  8-15), all auc 1.000, all loo 18/18. A plateau.
- Exp 40, ramp times (1 - drought): +57.5%, but sensitive to the
  drought threshold (+10.8% at t=13). DISCARDED for the simpler ramp.
- Exp 37 spine dominance, exp 38 spine word-mass, exp 41 pure sentence
  length (control): fail. The signal is specifically the longest
  uninterrupted clause, not sentence length and not word mass.

## Winner: long-clause flow (feature.py)

Mean over sentences of clamp((longest_clause - 10) / 5, 0, 1).
auc 1.000, loo 18/18, margin +55.0%. AI pages 0.01-0.17, humans
0.29-0.66, the post 0.32, tweets 0.12-0.77 with 6 of 42 on the AI side
of the midpoint.

Reading: every human text, however punchy its register, keeps writing
sentences that contain one uninterrupted clause of 10-15+ words, the
flowing main clause. GPT 5.5's landing copy inserts a punctuation break
before a clause can run that long. Pure sentence length fails as a tell
(the AI pages write long sentences too); what they do not write is a
long *unbroken* stretch inside the sentence. The tell is the absence of
flow, and it is continuous, sequence-based, and robust across its
parameterization on this corpus.

## Generation 6: removing the constants (sweep2.py, feature_relative.py)

Question: does the tell survive without the 10-and-15-word ramp?

- Rank flow (mean pooled-CDF percentile of each sentence's spine, no
  constants): +17%, loo 18/18. The empirical CDF works as a
  data-derived ramp, at a third of the margin.
- Consecutive rank flow (product kernel over adjacent pairs,
  feature_relative.py): +35%, loo 18/18. Requiring two flowing
  sentences in a row doubles the constant-free margin; the min kernel
  gives +12.7%.
- Every level-free order statistic fails: von Neumann ratio on lengths
  (auc 0.76) and spines (0.69), turning-point ratio (0.79),
  permutation-normalized adjacent difference (0.89), Spearman lag-1
  (0.88), adjacent min/max ratios (0.86, 0.80), rank nPVI on spines
  (0.51). Within-sentence relative forms (spine minus median clause,
  spine over median) also fail (0.86, 0.68).

Conclusion: the sequence order alone does not carry the tell; the level
of the longest clause does, and the order adds margin on top of it.
The constant-free hierarchy is 17% (level via ranks), 35% (level plus
consecutiveness), 55% (hand-ramped level, feature.py).

## Generation 7: the general family, and a correction (sweep3.py)

The pair product generalizes to S_k = mean over the document of the
product of k consecutive rank-transformed spines. S_1 is the
Mann-Whitney/Wilcoxon rank-sum statistic of the document's spines
against the corpus pool; S_2 is the generation-6 feature.

Raw margins grow monotonically with k (S_1 +17.0, S_2 +35.0, S_3
+52.4, S_4 +65.4, S_5 +76.7, all auc 1.000 loo 18/18), but this is
mechanical: multiplying more values in (0,1) stretches relative
differences the way raising to a power does. Normalize the scale with
the k-th root and the family collapses: S_2 +16.5, S_3 +15.3, S_4
+13.8, all slightly *below* S_1's +17.0. AUC and LOO, which are
invariant to monotone rescaling, are identical across the family.

Correction to generation 6: "requiring two in a row doubles the
constant-free margin" was a scale artifact. The sequential window adds
nothing beyond the level once the scale is fixed.

Final elegant form of the constant-free tell: S_1, the Mann-Whitney
AUC of the document's per-sentence longest unbroken runs against a
reference corpus. One line, no parameters, classic interpretation:
P(random run from this document > random run from the corpus). The
hand-ramped feature.py keeps the widest raw margin (+55%) but S_1 is
the form to report.
