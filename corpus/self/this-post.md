
*Note: this post is fully AI generated. It was written interactively, in a back and forth with an agent, under the very [kill-ai-smell](https://github.com/osolmaz/tools/blob/main/agents/skills/kill-ai-smell/SKILL.md) skill it describes, as a demonstration of that skill.*

Everyone knows the feeling by now. You open a page, read two paragraphs, and something tells you a model wrote it. The tells have become cultural shorthand, with the em dash as the poster child, but most of the discourse stays at the level of vibes. I wanted to know whether the feeling corresponds to anything you can measure, so my agent and I ran a small stylometric study, and the answer turned out to be a clear yes. A handful of surface metrics, all computable with regular expressions and a sentence splitter, separate generated copy from human writing by an order of magnitude, in several cases with no overlap between the groups at all.

This post walks through the corpus, the metrics, and the numbers, and ends with the [kill-ai-smell skill](https://github.com/osolmaz/tools/blob/main/agents/skills/kill-ai-smell/SKILL.md) that came out of the exercise.

## The corpus

For the AI side I needed pages that read as generated in the wild, and I had convenient specimens close to home. Ten project sites from the OpenClaw ecosystem (crabbox.sh, mcporter.sh, gitcrawl.sh, clawpatch.ai, fs-safe.io, spogo.sh, imsg.sh, wacli.sh, gogcli.sh and goplaces.sh) have landing copy written largely by agents, and I decided to keep those pages as they are and use them as data. Their prose comes to 4,853 words after stripping code blocks. These pages were written by GPT 5.5, so the measurements characterize that model's copy. They do not necessarily generalize to other models, whether Claude or open-weight ones like GLM and Kimi.

For the human side I wanted texts that are provably human, which means they had to be frozen before language models could have touched them. Five are essays and documentation: the [SQLite testing documentation](https://www.sqlite.org/testing.html), Joel Spolsky's 2000 essay ["Things You Should Never Do"](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/), a [2018 antirez blog post](http://antirez.com/news/122), Paul Graham's 2009 ["Maker's Schedule, Manager's Schedule"](http://www.paulgraham.com/makersschedule.html), and Julia Evans' 2019 ["Get your work recognized: write a brag document"](https://jvns.ca/blog/brag-documents/). The other three attack the register objection directly, because landing copy and essays are different animals regardless of author. They are the [ripgrep README at its 2016 tag](https://github.com/BurntSushi/ripgrep/blob/0.4.0/README.md), the [Redis README at 3.2.0](https://github.com/redis/redis/blob/3.2.0/README.md) from the same year, and the [Requests README at v2.13.0](https://github.com/psf/requests/blob/v2.13.0/README.rst) from 2017, each taken at an old git tag whose commit history proves its date. A README that sells a tool is the fairest comparison for a landing page that sells a tool. The human set comes to 15,317 words, and every rate below is normalized per 1,000 words so the corpora are comparable.

The exact texts I measured are archived in the [ai-smell repository](https://github.com/osolmaz/ai-smell) and listed in the [appendix](#appendix-the-corpus), so anyone can rerun the numbers against the same input.

## The metrics

The measuring script strips code, splits sentences, and counts things. There is no model in the loop and no judgment call in any metric. That is the point of the exercise. If the tells are real, they should be detectable by grep, and anyone should be able to reproduce the numbers. The scripts, the corpus, and the figures live in the [ai-smell repository](https://github.com/osolmaz/ai-smell).

The chart below shows every document against every metric, with the AI pages in orange and the human baselines in blue. The prose after it sticks to the ratios, because the ratios are the story, and the raw ranges are collapsed underneath for anyone who wants to check them.

<img class="desmeller-fallback" src="/img/ai-de-smeller/metrics.svg" alt="Six-panel bar chart comparing em-dash rate, exactly-three-list rate, labeled-bullet share, first-person rate, fragment-sentence share, and type-token ratio across all eighteen documents">
<div class="desmeller-charts" id="desmeller-metrics" style="display:none"></div>

<details markdown="1">
<summary markdown="span">Raw ranges per metric</summary>

| Metric | AI set (10 docs) | Human set (8 docs) |
| --- | --- | --- |
| Em dashes /1k words | 0.0–61.3 | 0.0–4.7 |
| Exactly-three lists /1k words | 6.3–15.9 | 0.0–2.0 |
| Labeled bullets, % of all bullets | 53–100% | 0–11% |
| Fragment sentences (≤4 words) | 3.6–41.9% | 1.4–17.4% |
| First person /1k words | 0.0–2.1 | 0.0–50.9 |
| Type-token ratio (first 280 words) | 0.59–0.69 | 0.53–0.67 |

</details>

The em-dash gap is the famous one, and it is real but weaker than its reputation. Averaged over each corpus, the AI pages use em dashes at roughly eighteen times the human rate, and the heaviest page lands one every sixteen words. But the tell only works in one direction. Three of the ten AI pages use fewer em dashes than the 2016 ripgrep README, and one uses none at all. A page drowning in dashes is almost certainly generated. A page without them proves nothing.

Exactly-three lists ("A, B, and C") turn out to be the better punctuation-level tell. Every AI page produces them at least three times the rate of every human text, with no overlap anywhere. Even the most triad-prone human text, Joel's essay, sits at a third of the most restrained AI page. Averaged over the corpora the gap is about nineteen-fold, and unlike the em dash, no AI page escapes it.

The labeled bullet was the discovery of the study for me. It is the bullet that opens with a short label, then a period, colon, or dash, then one sentence of elaboration. Here is a real one from mcporter.sh:

> Typed clients. mcporter emit-ts emits `.d.ts` interfaces or a ready-to-run client wrapping `createServerProxy()` so agents call MCP tools with full TypeScript types.

The metric is the share of a document's bullets that follow this shape. On the AI pages it is roughly four of every five, and on one page every single bullet does it. In the human baselines the share never reaches one in eight, and five of the eight human texts never use the shape at all; their bullets are plain items, like file names or flags, without the label-and-elaboration mold. If you have seen an AI-written landing page, you have seen walls of these, and it turns out the wall is more diagnostic than the punctuation.

Fragment sentences, the verbless punches of four words or fewer, sit in between. Most AI pages run high, and the worst writes two of every five sentences that way, but the groups overlap. The deliberately punchy Requests README out-fragments three of the AI pages. Fragments corroborate rather than convict.

First person taught me the opposite lesson. It looked like a strong tell until the corpus got fairer. Against essays the gap is enormous, since the antirez post averages more than one first-person word per sentence and the ten AI pages together contain exactly one. But the pre-LLM READMEs behave like the AI pages here. The Requests README has no first person at all, and ripgrep and Redis barely any. Authorial voice turns out to track register rather than authorship, so it works as a confirming signal at best. Vocabulary variety weakened the same way. Generated copy rotates in a fresh synonym at every mention, which pushes its lexical diversity high, and the AI pages do cluster at the top of the range. But the Requests README, which is deliberately punchy marketing prose, scores right among them, so the metric separates registers more than it separates authors. The human tendency it gestures at is still real, though. Human writers reuse the established word for a thing and repeat phrases for emphasis. Joel opens three consecutive paragraphs with "You are throwing away", and a model would never.

## Structural tells

Beyond the counters, we tested two structural claims, and both held on the larger corpus.

The first is identity deferral, which I wrote about in [Good READMEs say what tools are](https://solmaz.io/x/2071475602163654969/). Generated copy describes what a tool does and dodges saying what it is. In sentences where the tool name is the grammatical subject, action claims outnumber identity claims five to one across the ten pages. The raw ratio alone proves little, since prose about a known subject is naturally verb-led. The positional version is the tell. All three pre-LLM READMEs establish identity in their opening lines: "ripgrep is a line oriented search tool", "Requests is the only Non-GMO HTTP library for Python", and Redis opens its first section with the literal heading "What is Redis?". Among the ten AI pages, exactly one does the same. Four open with headless fragments like "A local-first GitHub triage tool for maintainers and agents.", which name a category but carry no subject and no verb, and the remaining five open with benefit imperatives or setup instructions like "Keep your editor and git workflow."

The second is heading register, and it produced a fun inversion. Title Case, the thing style guides nag about, belongs to the humans here. The SQLite docs use it in a fifth of their headings, as was the convention of their era, while the AI pages write modern sentence case throughout. What convicts the AI headings is rhetoric. About a third of the AI headings are slogans, imperatives, or rhetorical frames rather than labels; in the human set the share is one in ten, and those are mostly mild FAQ-style questions like "Why should I use ripgrep?". The strongest single shape is what I now call the comma couplet, a parallel two-beat slogan like "Local loop, remote box", "Two jobs, one binary" or "Small surface, clear split". It appears eleven times across five of the ten sites. The human set produces it exactly once, and the exception is instructive. It is the title "Maker's Schedule, Manager's Schedule", a deliberate one-off rather than a house pattern stamped down a page.

There is also a tell that only becomes visible when you put the pages side by side. Six of the ten sites have a "Pick your path" section, seven make a "five minutes" time-to-value promise, eight have a "Status" section, and six close with the exact sentence "Released under the MIT license." Each page looks fine alone. Together they reveal one prompt's house style stamped across unrelated projects.

## A minimal detector

The expanded corpus simplified the detector, because the two structural metrics turned out to need no help. Flag a page as AI-flavored when exactly-three lists exceed 3 per 1,000 words or the labeled-bullet share exceeds 30%. Either rule alone classifies all eighteen documents correctly. The em dash dropped out of the detector. It convicts a page when present in bulk, but three of the ten AI pages use fewer em dashes than the 2016 ripgrep README, so its absence clears nothing.

Plotting the two structural metrics against each other shows how much margin the thresholds have. Every human text sits in the bottom-left corner, below both lines, and every AI page sits far outside both.

<img class="desmeller-fallback" src="/img/ai-de-smeller/detector.svg" alt="Scatter plot of exactly-three-list rate against labeled-bullet share for all eighteen documents, with dashed threshold lines showing the human texts clustered near the origin and the AI pages far outside both thresholds">
<div class="desmeller-charts" style="display:none">
  <div id="desmeller-detector" class="desmeller-chart"></div>
</div>

Eighteen documents make a demonstration rather than a validated classifier. The first version of this study used only essays and documentation as baselines, which left the objection that the metrics were separating registers rather than authors, so the corpus now includes three pre-LLM READMEs that sell tools the way the AI pages do. The structural gaps survived that control untouched, while two metrics that looked strong against essays alone, first person and lexical diversity, collapsed into register signals. That is the argument for keeping the baselines adversarial. The next escalation would be a large sample of post-LLM, human-written landing pages, but the sizes of the surviving gaps, three-fold at the closest edge and roughly twenty-fold on average with no overlap, make me confident the structural metrics would hold.

## Long-form tweets in the wild

The corpora above have ground truth, which is what makes the thresholds checkable. The place people actually want a detector is the feed, where there is none, so as a last exercise we pointed the same counters at tweets. I keep a personal archive of tweets captured while browsing, about 27,000 at the time of writing, and from it we built one sample per account, made of every original long-form tweet (over 280 characters) in date order, for every account with at least 2,000 words of such text. That produced 42 accounts, my own included, and each sample is archived in the [ai-smell repository](https://github.com/osolmaz/ai-smell/tree/main/corpus/tweets) with a source link per tweet.

The chart puts the 42 samples over three metric pairs, with the ground-truth pages and baselines left in faintly in every panel so the wild samples can be read against the corpus that set the thresholds. The first panel repeats the detector chart exactly, same axes, same limits, same two thresholds. Every panel also carries one more point, a green diamond for this post itself, measured the same way as everything else.

<img class="desmeller-fallback" src="/img/ai-de-smeller/tweets.svg" alt="Three vertically stacked scatter panels of 42 tweet-account samples, with the AI pages, the human baselines, and this post itself shown in every panel: the detector's triad and labeled-bullet axes with thresholds, em dashes against exactly-three lists, and em dashes against fragment sentences">
<div class="desmeller-charts" style="display:none">
  <div id="desmeller-tweets-detector" class="desmeller-chart"></div>
  <div id="desmeller-tweets-dash-triads" class="desmeller-chart"></div>
  <div id="desmeller-tweets-dash-frags" class="desmeller-chart"></div>
</div>

Nothing here is a verdict, since none of these samples has a known author process. Under the unchanged rules of the first panel, seven of the 42 accounts trip the detector. Four cross the triad line, three cross the labeled-bullet line, and none cross both. On the landing pages the tells came bundled, every page far past both thresholds at once, while in the feed each flagged account trips exactly one rule. The bullet share also rests on smaller counts here, since a thread carries far fewer bullets than a landing page, and one of the three flagged accounts crosses the line on just two labeled bullets. So the thresholds transfer, but the confidence does not; a verdict in the feed would need feed-specific baselines.

The other two panels show where the feed does and does not resemble the corpus. On the dash axes, six accounts run past every human baseline, topped by one at 34.5 dashes per 1,000 words, denser than eight of the ten AI pages; but the dash already dropped out of the detector on the ground-truth corpus, and it stays out here. Fragment share spreads the accounts across the whole range the two corpora span, so it separates nothing in the feed either.

The account whose long posts sent me down this path is one of the three past the bullet line. Its sample writes 41 labeled bullets out of 90, a 46% share, half again past a threshold that no pre-LLM baseline came near, while its dash and triad rates sit mid-field. The counters flag it rather than clear it, with the caveat above about register. Its long posts also share a hook template the counters never measure. They open with lines like "90% of AI developers just...", pivot on "It's not X. It's Y.", and close with "Let me explain." That is the next metric worth building, and the tweet samples are archived so anyone can beat me to it.

## The de-smeller

The practical output of all this is [kill-ai-smell](https://github.com/osolmaz/tools/blob/main/agents/skills/kill-ai-smell/SKILL.md), a skill in my [tools repo](https://github.com/osolmaz/tools) that any coding agent can load. It covers the tells from punctuation up through page structure, and every rule carries a bad example next to a rewrite, because the rewrite teaches the hard half of the lesson. Fixing a smell means restructuring the sentence. Swapping an em dash for a punchy colon changes nothing.

The most instructive moment of the project happened while writing it up. My agent, fresh off measuring contrast rhetoric as a top tell, produced a report whose highlighted callout was titled "The strongest tells are structural, not lexical". The detector fires on its own author. That lesson is now the second paragraph of the skill. Knowing the rules is no defense, because these patterns are how models write by default, so the sweep has to be mechanical, applied to your own output, and repeated on the text that describes the sweep.

Feel free to steal the skill, and if you run the metrics on a corpus of your own, I would love to see the numbers.

## Appendix: the corpus

Every text is archived as measured in the [ai-smell repository](https://github.com/osolmaz/ai-smell), which is the maintained home of the study. It holds the corpus, the analysis scripts, the raw results, and the figures. The AI pages were captured from the live sites in July 2026, with code blocks still in place (the script strips them before counting).

The corpus splits into four groups there:

- [corpus/ai](https://github.com/osolmaz/ai-smell/tree/main/corpus/ai) holds the ten OpenClaw landing pages.
- [corpus/human](https://github.com/osolmaz/ai-smell/tree/main/corpus/human) holds the eight pre-LLM baselines: the SQLite testing docs, essays by Joel Spolsky (2000), antirez (2018), Paul Graham (2009), and Julia Evans (2019), and the ripgrep, Redis, and Requests READMEs at their 2016–2017 git tags.
- [corpus/tweets](https://github.com/osolmaz/ai-smell/tree/main/corpus/tweets) holds the 42 long-form tweet samples, one file per account, date-sorted, with a link back to each tweet.
- [corpus/self](https://github.com/osolmaz/ai-smell/tree/main/corpus/self) holds this post itself, archived as measured, provably AI-written by its own disclaimer. Written under the kill-ai-smell skill, it clears the detector from the other side, with zero em dashes, exactly-three lists at a quarter of the threshold, and no labeled bullets. The tells are a default, not a fingerprint, and a model instructed against them stops producing them.

<script defer src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script defer src="/assets/js/ai-de-smeller.js"></script>
