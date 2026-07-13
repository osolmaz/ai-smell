# @Rafa_Schwinger — long-form tweets

## 2026-06-14 (https://x.com/Rafa_Schwinger/status/2066230802439180447)

# The Verifier is the Moat

## How Fable was probably built, and why its lead is measured in months rather than years
Disclaimer: Everything here is personal inference with publicly available information, but don't bet against Rafadomis.
Every attempt to reverse engineer Claude Mythos and its public sibling Fable goes looking for an architectural secret, some parameter count or attention variant that the other labs missed, and that search is aimed at the wrong layer of the system. Anthropic briefed early partners that there was nothing unusual about the architecture, a claim that is single-sourced but consistent with how the model behaves. In a widely circulated May 2025 conversation, two of the lab's researchers said plainly that reinforcement learning in language models had finally worked, and that the property which decides where it works is whether the reward can be verified [1]. That evidence is more than a year old and belongs to the Claude 4 era, so it is precedent rather than proof of Mythos's exact pipeline, but it points the explanation off the network and onto the training signal, which is where the interesting variation now lives.

The compact way to state the situation is that the quality of a 2026 frontier model follows a single relation:

> capability ~= (base foundation) × (gradeable signal extracted on top)

The first factor is what the model knows and how cleanly it represents that knowledge. The second factor is the one that is now scarce and decisive, namely gradeable experience, meaning tasks whose outcomes can be checked cheaply and reliably so that training can reward what is actually correct rather than what merely reads well. Text is abundant, and for the leading labs raw compute is no longer the binding input; verifiable signal is the part that remains scarce.

It helps to separate two things that get conflated. Fable the product is a compound, routed system. When its classifiers detect a request in cybersecurity, biology and chemistry, or model distillation, the answer is served instead by Claude Opus 4.8, a fallback acknowledged in the launch materials and visible in Fable's evaluated model name on third-party leaderboards, which reads as Claude Fable 5 with an Opus 4.8 fallback [2][3]. Secondary readthroughs of the system card described a further throttle on frontier-AI-research requests, initially hidden and implemented through prompt modification, steering vectors, or LoRA-family weight edits; Anthropic later made it visible and conceded the hidden design had been a mistake [4]. Mythos the base model is a different thing. It looks like a single integrated network in the lineage Anthropic has described since Claude 3.7, where reasoning is a capability of one model rather than a separate model or a router [5]. Most of the intuition that Fable is a panel of models is really an observation about the product's plumbing. The core model is one network that, as described below, panels itself at inference time, and the more interesting possibility is that some of that paneling has been folded back into training.

# Two kinds of optimal data

If the binding input is verifiable signal, then the work of a frontier lab is the manufacture of optimal data, and that data arrives in two forms. The first is static: a dense, high-signal pretraining corpus. The second is interactive: verifiable environments, which are nothing more than data with a reward attached, a task plus a check on whether it was solved. The compute that once went into a single large pretraining run has been redistributed into a continuous parallel engine that manufactures and selects both kinds of data, generating synthetic corpora, running reinforcement-learning rollouts in environments, and sampling at test time. The compute did not vanish in this shift so much as change shape, which is part of why reinforcement learning has become, in practical terms, an inference-bound activity rather than a training-bound one.

# The recipe, in layers

The build stacks in layers, each with its own mechanism, its own piece of public evidence, and its own confidence level. (Anchor figures is an example of a  reference, not what the model used)


The base is built on dense, curated pretraining, and the reason this matters is measurable rather than rhetorical. Allen-Zhu and Li quantified knowledge capacity in bits and found that a one-to-seven ratio of useful to junk tokens degrades a model's storage efficiency by as much as a factor of twenty, and that prepending a provenance tag to documents, something as simple as a domain name, recovers most of that loss and takes the penalty from roughly twentyfold down to about twofold [6]. The lever is not more tokens but denser, cleaner, better-labeled ones, which is why rephrasing a noisy corpus such as C4 into clean variants buys roughly a threefold pretraining speedup, and why a mixture of about thirty percent high-quality synthetic data with seventy percent natural web text converges five to ten times faster at equal compute in the large-data regime [7]. These results are not Anthropic's, so they establish the technique class rather than the exact recipe, and the per-technique multipliers are bounded; synthetic pretraining is a real contributor to a cleaner substrate, not the whole jump.

On that substrate sits reinforcement learning against verifiable rewards (RLVR) , and this is the decisive layer. The algorithmic core across the field is some variant of GRPO, which dispenses with a separate value network and estimates advantages from groups of sampled rollouts scored by a reward. The hard engineering is not the optimizer but the reward. The binding requirement for a useful environment is soundness, meaning that a high reward must actually correspond to the task being solved rather than gamed, and making a verifier robust to that gaming is the part practitioners consistently report as the real bottleneck, harder than scaling the environment count [9]. It is also why outcome-only rewards prove insufficient for long tasks and labs move toward process rewards that score intermediate steps, a point that recurs below. Anthropic treats environment construction as a standing function rather than a one-off research effort: it staffs a dedicated Environment Scaling team whose posting describes designing reward signals and building quality-assurance frameworks to catch reward hacking [8]. The investment is real, though the posting frames the work around new verticals and does not by itself establish that verifier-RL outranks scale.

One detail from that same 2025 conversation sharpens the picture and should be read as a telegraph rather than a measurement. The researchers noted that the lab had, until then, spent on the order of a million dollars on reinforcement learning against hundreds of millions on base-model pretraining, holding RL deliberately small until they were confident the algorithm was right, with the obvious implication that the spend would scale once it was [1]. A reading of the Mythos jump as a large, validated scale-up of verifier-RL on top of a fresh foundation is consistent with that intent, even though the lab has disclosed no figures for Mythos itself.

Coding deserves its own line, because it explains the center of gravity of the whole enterprise. Code is the one domain that is simultaneously long-horizon and cheaply verifiable: it demands planning, tool use, stateful context, and error recovery, and yet the result can be checked by compiling it and running tests. That combination makes coding the highest-value environment to manufacture, which is why every serious lab's agentic story tends to be told first in code [34]. Not all of the signal is synthetic or learned by self-play. A patent that came to Anthropic through the Adept acquisition covers the computer-use subsystem, and it describes generating agentic trajectories both by intercepting human interface actions and by collecting on-policy feedback from the agent's own runs, a heterogeneous stack rather than pure human imitation [19].

The model now helps build its successor, though not autonomously. By Anthropic's own accounting the current systems give researchers roughly a fourfold uplift in output, and on one fixed code-optimization task the measured speedup rose from about threefold to about fifty-twofold over a year, a figure the lab itself cautions should not be read as a real-world training speedup [17]. Set against that, the threshold the lab uses to define genuinely automated AI research, the point at which it would compress something like two years of progress into one, sits closer to fortyfold, and the system card states that Mythos does not cross it [18]. The flywheel is real and steep, and people still turn it.

# Why it thinks clearly

Clear reasoning is graded correctness at a single step. A model trained where being right is checkable, where code compiles or fails and a proof closes or does not, is selected for reasoning that survives the check rather than reasoning that merely sounds plausible, which is why these systems read as lucid in mathematics and software and stay ordinary in domains where quality is a matter of taste and no cheap verifier exists. The same logic extends into inference. Since Claude 3.7, Anthropic has sampled several parallel attempts, discarded the ones that fail visible regression tests, and ranked the survivors with a learned scoring model, a best-of-N-with-a-verifier procedure that raised its SWE-bench result from 63.7 to 70.3 percent and that it applied to GPQA and AIME as well [5]. The effort control on the current models is that same mechanism exposed as a dial, deciding how much verification to buy per answer. The honest caveat is that this is Claude-3.7-era evidence, so it is precedent for the family's approach rather than a description of Mythos's exact procedure, and there is a live and unsettled dispute, made most sharply in a Tsinghua result, about whether this kind of reinforcement learning installs genuinely new reasoning or mainly sharpens and narrows toward modes the base model already contained [16].

# Why it endures

Sustained agentic work over many hours is graded correctness across many steps, and it is the ability most often misattributed to the size of the context window. The million-token window reached the 4.6 line in March 2026 [33], obtained by the standard route of continued pretraining on long documents plus RoPE or YaRN rescaling, a comparatively cheap extension that is not where endurance lives. Long tasks fail because per-step errors accumulate, and a model that conditions on its own earlier mistakes grows more error-prone as those mistakes pile up in the context. The relationship runs in both directions: marginal gains in single-step accuracy compound into exponential gains in the length of task a model can finish, so a model that is correct 99.9 percent of the time per step completes runs that sink a model correct 99 percent of the time, a difference too small to register on a short benchmark that becomes the entire story on a long one. The same work shows that this self-conditioning is not removed by scaling the model, though deliberate test-time reasoning suppresses it [10], which quietly unifies the two abilities, since the test-time thinking that sharpens single-step correctness also damps the error cascade that kills long runs.


![HKyiS5nWkAACpY8.jpg](media/2066230802439180447/HKyiS5nWkAACpY8.jpg)

The remedy on the training side is learned context management. An agent that branches into a sub-task and folds it down to a summary can match or beat a long-context baseline while carrying an active context an order of magnitude smaller, 32K against 327K tokens, provided the folding is trained directly with step-level process rewards, because a sparse terminal reward turns out to be too weak to teach it [11]. That result comes from an open 36B model rather than from Anthropic, so it demonstrates the mechanism rather than the specific implementation, but it locates the real constraint precisely. The KV cache grows linearly with sequence length and dominates serving cost, so the durable trick is to keep the active context small rather than to enlarge the nominal window, and endurance reads as a trained competence in context discipline rather than as a property of window size.
Third-party measurement is consistent with this. METR places Mythos at the top of its autonomous time-horizon table, but the honest version of that statement is careful: the model registers a fifty-percent-success horizon of at least sixteen hours, with a very wide confidence interval running from roughly 8.5 to 55 hours, and METR itself notes that measurements past sixteen hours are unreliable on the current suite, since only a handful of its tasks run that long [12]. There is no comparable figure for GPT-5.5 or for the recent Opus point releases, so this is a ceiling reading rather than a clean ranking, which matters for the comparison below.

# Why it beats Opus 4.8

Because capability is multiplicative, Opus 4.8 loses on both factors at once. It is the polished end of the previous foundation, its reinforcement learning ran on that weaker base, and RL is ceiling-bounded by the base it sharpens, which is the practical content of the contested Tsinghua claim that the method narrows toward existing modes rather than adding new ones [16]. Mythos is a newer and costlier foundation with more long-horizon verifier-RL on top; Opus 4.8 is an older foundation with less. The two shipped twelve days apart, which is why recency was never the explanation, and why the gap is one of construction rather than calendar.

# Why it only edges its peers on the grid

On aggregate public benchmarks the leading models are close. The most-cited snapshot, from an earlier generation, put the top OpenAI, Anthropic, and Google models within about a point of one another on a composite index, near enough to call a tie [31]. That observation is true and worth stating, but it understates the real situation, because aggregate benchmarks are short-horizon and increasingly saturated, and they cannot see the place where the separation actually lives. The meaningful gap is in long-horizon autonomy and multi-hour optimization, where a small per-step reliability advantage compounds into a decisive one over hundreds of steps, and where no shared public benchmark resolves the differences. The recipe that produces that advantage is convergent, so the edge that remains is depth and integration rather than secrecy, and the clearest way to read the field is a scorecard ranked by proximity to Anthropic's environment foundry.

The vendor market that supplies these environments has formed quickly, with several firms now valued in the billions, and Anthropic itself has reportedly discussed spending more than a billion dollars on RL environments in a single year [26]. DeepSeek's openness is the most useful single window onto the method, since it publishes what Anthropic only implies, and the recent V4 recipe is especially telling: it forks the base into per-domain specialists and then consolidates them by on-policy distillation from a panel of more than ten teacher models [40], which is a compound, panel-shaped structure that lives at training time rather than at serving time. That is the cleanest available hint that Fable's apparent self-paneling could be partly a property of how the base was trained. The Chinese labs show the recipe and lack the compute; the American labs hold the compute and hide the recipe.

# GPT-5.5 against Fable

Taking Opus 4.7 as the public Anthropic proxy, since raw Mythos was never sold, the head-to-head splits by domain rather than favoring one model [27].




![HKyhf05WEAAo4vN.png](media/2066230802439180447/HKyhf05WEAAo4vN.png)

The cyber row is the one that matters most and the one that resists clean measurement: OpenAI's rating is a self-graded safety assessment, and the Mythos characterization is Anthropic's own and contested in magnitude. No clean long-horizon comparison exists, since METR has no published horizon for GPT-5.5 and Mythos already sits past the reliable ceiling. The Vending-Bench row is the useful corrective against reading long-horizon strength as blanket dominance, because on open-ended agentic tasks without a crisp verifier the Anthropic line has not led, which fits the pattern that the advantage concentrates wherever the work is both long and cheaply checkable. The picture is near-parity on the grid, with the genuine and larger separation living in long-horizon, verifiable autonomy, exactly where measurement is weakest.

# The two regimes

The objective is intelligence per unit of energy and price, pursued in two modes. 

At the frontier, capability is bought almost regardless of cost, and Fable is priced near twice Opus 4.8 for roughly 5.7 percent more on public benchmarks [31]. In the fleet, the same capability is distilled down and served cheaply: Haiku 4.5 reaches the previous Sonnet generation's coding level, landing at 73.3 percent on SWE-bench Verified, slightly above the 72.7 percent that Sonnet 4 posted on the same benchmark, at one third the cost and more than twice the speed, and it is positioned as an inexpensive sub-agent that a larger planner orchestrates [13][14]. The broader efficiency frontier, measured as intelligence per watt, improved about 5.3-fold over two years, though that figure is drawn from local and edge inference rather than datacenter serving and should be read with that scope in mind [15]. One caution belongs in plain sight: the cleaner econometric versions of this two-regime story, along with the specific energy and chip-count figures that have circulated for Anthropic, did not survive scrutiny, so only the qualitative shape, expensive discovery at the frontier and cheap distilled deployment in the fleet, should be trusted.

# Why its strength and its danger coincide

The domains where reward is cheapest to verify, code and security foremost among them, are also the domains where a model most decisively exceeds people, which is why the same capability that makes Fable the strongest coding system also lets it find live vulnerabilities. Partners reported on the order of ten thousand high or critical findings in the first month, of which 1,752 were assessed by six independent security firms at a 90.6 percent true-positive rate, leaving on the order of fifteen hundred independently confirmed; both numbers come from Anthropic's own disclosure rather than from outside skeptics, which is the right way to weight them [29]. The same verifiability that drives the cyber result shows up on the biological side, where graders estimated that red-team protocols which would have taken dozens of working days were produced in roughly sixteen hours, a near-hundredfold compression that the system card treats as close to a qualifying threshold [18]. The export-control order that took both models offline on the twelfth of June followed a demonstration, reported through a partner, that the model could be driven into autonomous vulnerability discovery; Anthropic characterized the triggering jailbreak as narrow and disputed that it defeated the safeguards generally, but the order stood and the models went dark [30]. Excellence and hazard occupy the same coordinate here, since the cyber capability that defines the model is also what drew the regulatory action that pulled it.

# How another lab replicates it

The playbook compresses to a single instruction, win the factory rather than the model, and then to a short list of moves:

1.  Build the data-and-environment foundry as a standing function, staffed for environment generation, reward and verifier design, and reward-hacking quality assurance, rather than treating it as a research side project.
1.  Go deep on long-horizon, verifiable environments with process rewards, since the short-horizon kind, unit tests and math answers, is already commoditized and the gap lives in the multi-hour tasks.
1.  Densify the base by curating, deduplicating, tagging provenance, and mixing high-quality synthetic data to raise bits per token.
1.  Spend test-time compute through best-of-N with a verifier, and expose it as an effort control.
1.  Acquire human demonstrations for the domains that cannot yet be auto-graded, as Anthropic did through Adept.
1.  Run a two-regime fleet, distilling the frontier into cheap sub-agents under a planner.
1.  Where compute is the constraint, compete on algorithmic efficiency the way the Chinese labs do, with KV-cache reduction, extreme-sparse mixtures of experts, and GRPO.

None of these moves is secret. The moat is their integration, and the years of iteration behind a verifier that can actually be trusted.

# What cannot be seen

Several things remain genuinely out of view, and it is more useful to mark them than to paper over them:
- The base architecture, dense or mixture-of-experts, is unresolved, and the rumored ten-trillion-parameter and tiered-attention specifics have no primary support and are contradicted by the more careful throughput-based size estimates.
- The test-time and integrated-reasoning evidence is from the Claude 3.7 era, so it is precedent for the family rather than a current spec.
- The per-domain profile cannot be measured cleanly, because Fable's public scores are confounded by its safety routing; the routing trips only a single-digit percentage of sessions, and the clean unblocked numbers belong to a model that was never sold.
- The internal-teacher hypothesis, a too-dangerous-to-deploy model distilling safer students, stays unresolved and is weakened by the repeated finding that self-generated data tends to match or beat distillation from a larger teacher, so a hybrid of dense self-generated signal plus fresh RL is the more defensible reading than a single hidden oracle.
- The gains are not uniform: alongside the cyber and biological step-changes, the same system card reports a regression in one mundane place, a higher rate of fabricated references than the prior model.
- The energy and pricing numbers were refuted, leaving only the qualitative two-regime shape.
# Conclusion
The claim that survives all of this is narrow, and I think it is correct. A model is as clear and as persistent as the verifiable signal it was trained against. Clear thinking is graded correctness at a single step, endurance is graded correctness across many, and both are produced by the same environment foundry, with dense pretraining as the substrate and test-time compute as the way to buy more verification when an answer is worth it. The achievement is a factory rather than a secret, the deepest pipeline anyone has yet built for manufacturing verifiable signal with a model trained against it, which is also why, on the lab's own reckoning of how fast the recipe is spreading, the lead is best measured in months rather than years.

# References

- **[1]** Sholto Douglas and Trenton Bricken on Dwarkesh Patel (May 2025), on verifiable-reward RL and the deliberately small early RL budget: https://www.dwarkesh.com/p/sholto-trenton-2
- **[2]** Claude Fable 5 and Mythos 5 launch, routing of restricted domains to Opus 4.8: https://www.anthropic.com/news/claude-fable-5-mythos-5
- **[3]** Fable 5 model entry showing the "Opus 4.8 Fallback" configuration and routing behavior: https://artificialanalysis.ai/models/claude-fable-5
- **[4]** System-card readthrough describing the frontier-AI-research throttle and Anthropic's subsequent reversal: https://thezvi.substack.com/p/claude-fable-5-and-mythos-5-the-system
- **[5]** Claude 3.7 Sonnet, best-of-N with a verifier (63.7 to 70.3 on SWE-bench) and integrated reasoning: https://www.anthropic.com/news/claude-3-7-sonnet
- **[6]** Allen-Zhu and Li, Physics of Language Models 3.3, knowledge capacity and the provenance-tag result: https://arxiv.org/abs/2404.05405
- **[7]** WRAP, rephrasing the web (~3x on C4): https://arxiv.org/abs/2401.16380 ; Demystifying Synthetic Data (30/70 mix, 5 to 10x): https://arxiv.org/html/2510.01631v1
- **[8]** Anthropic "Environment Scaling" research-engineer posting, reward design and reward-hacking QA: https://jobs.menlovc.com/companies/anthropic/jobs/67669113-research-engineer-environment-scaling
- **[9]** Epoch AI, FAQ on RL environments, on reward-hacking soundness as the binding constraint: https://epoch.ai/gradient-updates/state-of-rl-envs
- **[10]** Long-horizon execution and self-conditioning, including exponential error compounding: https://arxiv.org/abs/2509.09677
- **[11]** Context-Folding and FoldGRPO, 32K versus 327K active context with process rewards: https://arxiv.org/abs/2510.11967
- **[12]** METR task-completion time horizons, including the reliability ceiling above sixteen hours: https://metr.org/time-horizons/
- **[13]** Claude Haiku 4.5, 73.3 on SWE-bench Verified at one third the cost and over twice the speed: https://www.anthropic.com/news/claude-haiku-4-5
- **[14]** Claude 4, source for Sonnet 4's 72.7 on SWE-bench Verified: https://www.anthropic.com/news/claude-4
- **[15]** Intelligence per Watt (Stanford), 5.3-fold over two years for local and edge inference: https://arxiv.org/abs/2511.07885
- **[16]** RLVR and whether RL adds new reasoning (Tsinghua, contested): https://arxiv.org/abs/2504.13837
- **[17]** Anthropic on recursive self-improvement, the ~4x uplift and the ~52x single-task figure with its caveat: https://www.anthropic.com/institute/recursive-self-improvement
- **[18]** Mythos Preview system card mirror, the ~40x automated-R&D threshold, the cyber "step-change," and the biological-uplift estimate: https://gist.github.com/Michaelliv/0677ab6a64312211e38b7a99a03c5f61
- **[19]** Patent US 12,437,238 B1 (via Adept), generation of agentic trajectories from intercepted human actions and on-policy feedback: https://pubchem.ncbi.nlm.nih.gov/patent/US-12437238-B1
- **[20]** DeepSeek-V3.2, 1,800+ environments, GRPO, six specialists distilled to one: https://arxiv.org/abs/2512.02556
- **[21]** DeepSeek-V2, source for the ~93 percent KV-cache reduction from MLA: https://arxiv.org/abs/2405.04434
- **[22]** Qwen3-Coder, 20,000 parallel executable environments and execution-driven code RL: https://qwenlm.github.io/blog/qwen3-coder/
- **[23]** Kimi K2, the verifiable-rewards gym, rubric self-critique, 1T / 32B-active MoE, MuonClip: https://arxiv.org/abs/2507.20534
- **[24]** AlphaProof in Nature (2025), AlphaZero-style RL with a Lean verifier and test-time RL: https://www.nature.com/articles/s41586-025-09833-y ; Silver and Sutton, "The Era of Experience"
- **[25]** OpenAI "Synthetic RL" team posting (environments and feedback): https://openai.com/careers/researcher-synthetic-rl-san-francisco/
- **[26]** The environment vendor market and Anthropic's reported >$1B environment spend: https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/
- **[27]** GPT-5.5 versus Opus 4.7 benchmark splits and pricing: https://www.datacamp.com/blog/gpt-5-5-vs-claude-opus-4-7
- **[28]** GPT-5.5 cybersecurity rating, high but below critical, no full-chain exploit: https://deploymentsafety.openai.com/gpt-5-5/cybersecurity
- **[29]** Glasswing update, the 10,000+ partner findings and the independently assessed 1,752 / ~1,587 confirmed: https://www.anthropic.com/research/glasswing-initial-update
- **[30]** Export-control order of June 12 and the disputed jailbreak: https://www.axios.com/2026/06/12/anthropic-trump-mythos-fable-national-security
- **[31]** Three-way aggregate near-tie (earlier generation): https://the-decoder.com/new-artificial-analysis-benchmark-shows-openai-anthropic-and-google-locked-in-a-three-way-tie-at-the-top/ ; Fable priced near twice Opus for 5.7 percent more: https://the-decoder.com/anthropics-claude-fable-5-costs-twice-as-much-for-5-7-percent-more-performance/
- **[32]** xAI RL-environment and "Macrohard" hiring (up to $440k): https://job-boards.greenhouse.io/xai/jobs/4916837007
- **[33]** One-million-token context general availability on the 4.6 line (March 2026): https://karangoyal.cc/blog/claude-opus-4-6-1m-context-window-guide
- **[34]** The RL-environment market and coding as the meta-domain: https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why
- **[35]** MiniMax-M2, 229.9B-total / 9.8B-active MoE, the "Forge" RL infrastructure, M2.7 self-debugging: https://arxiv.org/abs/2605.26494
- **[36]** GLM-4.5, expert specialization then unified self-distillation: https://arxiv.org/abs/2508.06471
- **[37]** Meta Muse Spark, an RL scaling law at more than 10x compute efficiency: https://ai.meta.com/blog/introducing-muse-spark-msl/
- **[38]** Amazon Nova 2 technical report (tau2-Bench 77.7, SWE-Verified 70.0): https://assets.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf
- **[39]** Microsoft MAI-Thinking-1, its first reasoning model (SWE-Bench Pro 53 percent): https://microsoft.ai/news/introducing-mai-thinking-1/
- **[40]** DeepSeek V4 post-training, the "ten teachers, one student" recipe (secondary analysis of the V4 report): https://maximelabonne.substack.com/p/deepseek-v4-ten-teachers-one-student

## 2026-06-15 (https://x.com/Rafa_Schwinger/status/2066504785071595687)

Yes, but Dario is notoriously risk adverse so I believe the sequence of events was synthetic data foundry was fruitful -> therefore an even bigger model would make so much more sense now -> RSI and regulatory capture now possible

They are hurrying the government intervention because they don't have much time before someone gets a giant data factory like theirs.

## 2026-07-02 (https://x.com/Rafa_Schwinger/status/2072651897199108222)

@ivanfioravanti One tip for the Spark is that it has low bandwidth and high compute power, so it would probably work better at very high batch rates instead of just one. In particular, for the 3.6, you could try setting up some crazy workflows with, I don't know, 50 to 100 contexts in parallel
