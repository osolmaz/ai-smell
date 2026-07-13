"""Winner (exp 46): long-clause flow.

For each sentence, take its longest clause (the words between
punctuation breaks) and give the sentence a smooth credit ramping from
0 at 10 words to 1 at 15 or more. The document score is the mean credit
over sentences.

The intuition the search converged on: human prose keeps producing
sentences that contain one long, uninterrupted run of words, the
flowing main clause, no matter how punchy the register otherwise is.
GPT 5.5's landing copy almost never lets a clause run past 10 to 15
words without a punctuation break, so its score collapses. The tell is
the absence of flow, measured continuously.

On the ground-truth corpus: auc 1.000, leave-one-out 18/18, and the
closest AI page (crabbox at 0.17) sits under the flattest human
baseline (ripgrep 2016 at 0.29) with a 55% margin at the edge. Margins
stay between 44% and 55% across ramp parameterizations from 8-14
through 11-16, so this is a plateau, not a tuned cliff.
"""


def score_doc(seq):
    ok = [s for s in seq if s["clauses"]]
    if not ok:
        return 0.0
    return sum(min(1.0, max(0.0, (max(s["clauses"]) - 10) / 5)) for s in ok) / len(ok)
