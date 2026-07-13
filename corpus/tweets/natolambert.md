# @natolambert — long-form tweets

## 2026-01-25 (https://x.com/natolambert/status/2015473455530225939)

Exciting addition to the RLHF Book on my DGX Spark arc is a bunch of single GPU, tinkering scripts for minimal examples of RL, reward models, etc. (and DPO like algorithms soon).

Right now has REINFORCE, RLOO, PPO, GRPO, Dr. GRPO, GSPO, CISPO, standard reward model, PRM, ORM.

H/t to Zafir Stojanovski an independent researcher for doing a lot of the groundwork.

Would really welcome issues, contributions, and suggestions as we build the RLHF book as a more central home for learning about post-training. I have plans for a lecture series later this year.

## 2026-05-27 (https://x.com/natolambert/status/2059676112415035527)

The most likely way continual learning manifests in the coming few years is through products used directly for knowledge work. 

Sort of how cursor can continually train their models with real-world data and RL, Claude, Copilot, and co will see if they can for knowledge work.

I was chatting with Ronak a few weeks ago when this was crystalizing for me, so it's fun to see a startup in that area.

## 2026-06-11 (https://x.com/natolambert/status/2065082135682383950)

The core part of this Anthropic Fable release saga is that there are many overlapping issues at once. Some of which operate on different timelines of the AI arc, and some have easier fixes. In my critiques, I asked for specific changes to some things, understanding that some things don't have an easy fix.

The simplest issue was an uneven application of safety domains in a way that was misleading to users. This was an implementation issue that overlaps with a values-based decision of what their customers should be doing. Many people including myself pointed out how it was insane to list core safety areas and then have one of them launch with a different safety mechanism, one which actively mislead users. Doing this from the guise of safety was a major misstep and in my opinion Anthropic got very justifiably raked over the coals for it. Don't release the model if you can't hit your safety targets.

A subissue here is the idea of silent manipulation. This again is a horrible precedent, and quite odd for a company that has done extensive, leading technical AI safety research on ideas like CoT monitoring and other emergent misalignment issues. Silent manipulation of users is baking in a misalignment to the system at its face level. This comes with a permanent degradation in user trust, which begets a less safe environment for AI. Users who don't have clear information on how AI works will not develop safe working patterns with it.

The more complex issues are with how Anthropic handles broader scientific engagement with their models. The safety classifiers launched with these models obviously have accuracy issues to start. I have priced in that there will be more false positives to start, that's life. It's Anthropic's business to degrade their products at release time, or make the trade off of user satisfaction versus revenue. Still, it is a very real sign of concentration of power that businesses can make such obviously user-harmful behaviors and still lead in the market. This concentration of power is only starting to set in and we could see even weirder signs of it in the coming years.

It is now simple enough for me to test Claude Fable in my workflows and know if I'm restricted. This is obviously a suboptimal equilibrium – i want the best intelligence I can get, without restrictions – but it is easy enough for me to make sense of and work with.

The specific issue of restricting access to AI research in particular was a bubbling and hard to fix issue with Anthropic specifically, and the frontier labs generally. There is a common view that the frontier labs will be the mediators of all major scientific innovations in the future, as the places with the best models and the compute for inference to solve major problems. This is a categorical error in how science works, which is a community evolution of accepted ideas, and the the evaluation of your ideas by (hopefully numerous) independent, other practitioners. You cannot have science advance only within a monolith.

As an AI researcher I'm very sad to have the latest models restricted, but I would expect Anthropic to do this eventually. I lost more trust over the silent manipulation than I would with a restriction in access. Anthropic has made it pretty clear that they only trust themselves as the mediators of cutting-edge AI research.

If I had a say, Anthropic should've proactively made a program to make sure researchers get access in the broader AI community without the safeguards. Academics, nonprofit workers myself, etc. have no reason to not get access. The only valid argument here is that they want to control frontier AI, which is a know your customer part of serving these models.

This worldview of science has personally motivated me greatly over the last year, and increasingly so this week, to make the open science of AI continue to be viable. Olmo was a wonderful success here. Still, building research infrastructure is different from working for access to the tools needed to do the trade.

## 2026-06-15 (https://x.com/natolambert/status/2066538953982066808)

This isn't very true. A big part of the problem is that the labs use the term distillation, which is a general post-training technique, in lieu of a specific issue of jailbreaking the API.  (1)

There is a second debate of *how* impactful distillation is, but it is definitely helpful. (2) This is entirely based on how the Chinese labs are jailbreaking the APIs to get reasoning traces out, which help bootstrap reasoning behaviors in new domains.

There's a third point (3) which I take an excerpt from my recent piece, where the labs need to be more transparent why especially point (2) is true. From the third piece:

"
On the point of distillation, my hypothesis is that API builders don’t have an easy time preventing hacks or jailbreaking because it’s a deeply grounded property of reasoning models to want to output the reasoning traces, and it would make the model far less intelligent to fully patch the behavior. This is based on a few assumptions:

a) Chinese labs are not just showing up as customers to Anthropic’s API and paying for tokens in the intended input-output form. If the Chinese labs are paying for intended use behaviors, despite being banned by the terms and conditions, I don’t have a lot of sympathy for the frontier labs manifesting policy actions against this.
b) Reasoning traces are disproportionately effective at seeding behavior in downstream models.
c) Leading labs work very hard to patch the pipeline of these jailbreaks.

So, my logical conclusion is that the model companies would have to weaken their economic position to fully protect their IP. If this is the case, Anthropic would get a lot more sympathy from the AI research community by being transparent. It would also be far easier to have informed policy discussions, and not rely on me proposing Occam’s razor explanations for what the API jailbreaking looks like.
"

There's no need to misinform people because the labs use a bad term. The labs use this term partially to make the discourse confusing, as you're doing.

(1) See https://t.co/GiEoZXCgHP
(2) See: https://t.co/PPD0gYr2wv
(3) See: https://t.co/GoLGmZWPxT

## 2026-06-15 (https://x.com/natolambert/status/2066538987100250127)

This isn't very true. 

A big part of the problem is that the labs use the term distillation, which is a general post-training technique, in lieu of a specific issue of jailbreaking the API.  (1)

There is a second debate of *how* impactful distillation is, but it is definitely helpful. (2) This is entirely based on how the Chinese labs are jailbreaking the APIs to get reasoning traces out, which help bootstrap reasoning behaviors in new domains.

There's a third point (3) which I take an excerpt from my recent piece, where the labs need to be more transparent why especially point (2) is true. From the third piece:

"
On the point of distillation, my hypothesis is that API builders don’t have an easy time preventing hacks or jailbreaking because it’s a deeply grounded property of reasoning models to want to output the reasoning traces, and it would make the model far less intelligent to fully patch the behavior. This is based on a few assumptions:

a) Chinese labs are not just showing up as customers to Anthropic’s API and paying for tokens in the intended input-output form. If the Chinese labs are paying for intended use behaviors, despite being banned by the terms and conditions, I don’t have a lot of sympathy for the frontier labs manifesting policy actions against this.
b) Reasoning traces are disproportionately effective at seeding behavior in downstream models.
c) Leading labs work very hard to patch the pipeline of these jailbreaks.

So, my logical conclusion is that the model companies would have to weaken their economic position to fully protect their IP. If this is the case, Anthropic would get a lot more sympathy from the AI research community by being transparent. It would also be far easier to have informed policy discussions, and not rely on me proposing Occam’s razor explanations for what the API jailbreaking looks like.
"

There's no need to misinform people because the labs use a bad term. The labs use this term partially to make the discourse confusing, as you're doing.

(1) See https://t.co/GiEoZXCgHP
(2) See: https://t.co/PPD0gYr2wv
(3) See: https://t.co/GoLGmZWPxT

## 2026-06-22 (https://x.com/natolambert/status/2069055254961021150)

TMax: An open RL recipe for terminal agents

I’m very excited to get to share a new RL paper today that I got to have a small part in – a type of paper I suspect we’ll see much more of in the future. The key is that RL research is very different today, in mid-2026, than what most observers have in their context. The average conception of an RL paper is grounded in the RLVR revolution of early 2025, where many people could use vanilla RLVR libraries to hillclimb on math benchmarks. Crucially, this style of math work could be done on base models or fairly stably on already trained models. With agents, the tasks of focus are very hard, requiring complex tool-use, harnesses where the model automatically manages its history, and much more training to make smaller eval improvements. We’re shifting from a renaissance of RL study to rapidly needing to improve its empirical rigor and common community engagements.

TMax is the best open data for hillclimbing on frontier terminal tasks. It’s been validated with rigorous experiments, and if the authors wanted to just form a “RL environments startup” they could probably sell it for millions of dollars. This data work is some of my favorite stuff to be around in my 2.5+ years at Ai2.

As a general summary, the recipe is open data and recipe lessons from hillclimbing the Qwen 3.5 smaller, dense models on terminal tasks. These models are super hard to hillclimb in this area, as they’re already trained heavily on the task. The training is very infrastructure-dependent, and most of the RL innovations are more designed to make training stable than to improve the rate of learning.

I strongly recommend this paper. I joke around that I was happy to be an author just so I had to read it twice! You can find Hamish’s thread sharing more here or read the paper here. You can click through to find the model weights, the data, and even some fun further artifacts to study like all the RL rollouts from a training run – where the model sometimes became aware that it was being tested.

The biggest takeaway I have from following this work, and more of the work in the community, is how important recipe work is. Let me define “recipe work.” It is a style of paper that explains all the steps you need to make crucial model improvements – data, algorithm, codebase, pitfalls, etc.

Getting started in meaningful RL experiments today is a substantial expense. There are a ton of companies, an entire industry emerging really, around the idea of taking open-weight language models and finetuning them with RL on your domain-specific tasks. What I see in many projects is that getting an initial baseline is very hard. This phase, which can cost weeks and anywhere from $10K to $1M+, feels like spinning your wheels (A fun fact is that an RL step on a model like Nvidia Nemotron 3 Ultra on Tinker costs $1K and a meaningful RL run would be hundreds of steps – credit Edward Hu). It takes a lot of time to get traction in learning signal on meaningful, hard RL tasks.

What we need as a community is a way for people to study small ablations to established RL recipes, as most labs won’t have the resources to do it from scratch in a meaningful way. This is what I hope TMAX can be for terminal agents, or the start of. Yes the training jobs are expensive, as the paper documents a standard training job being 8 nodes of H100s (2 train 6 inference) for 2-3 days, but that is approaching something academics can study. The establishment of this recipe took O(100) of these training jobs to get right.

This isn’t my first time trying to establish this direction. When we launched Olmo 3 we had the “RL Zero“ model families, which are clean RL runs from a base model on a certain domain. This type of recipe-dependent work is a clear indicator that meaningful post-training work today looks much more like pretraining work of years past. We need decision-making ladders, clear ways of seeing small improvements in the models, stability, and so on.

Part of this is down to academic gatekeepers, who won’t reward a paper doing very clean empirical work to push a recipe 1-2% up. They’ll favor a “new algorithm” that matches results, or something sort of bogus. My hope is that we can have multiple, stable, clear recipes across agent types, so innovations can be tested more clearly in multiple domains. (If you’re working on this, please reach out – I’m happy to support if I can, but I likely can’t reply to every email).

As a quick aside, the RL frameworks in vogue today seem to be SLIME and SkyRL. The libraries of choice have shifted throughout these seasons in RL, which further contributes to a form of fragility in the literature. A bit of continuity will go a long way.

So, go read this paper. It’s a really great example of how seemingly simple data and infrastructure work can be very hard and impactful. It’s also got me looking for more applications of Divergence Proximal Policy Optimization (DPPO) as another small evolution to the best RL algorithms of the day, by virtue of being a bit more stable by improving token-level clipping.

## 2026-06-23 (https://x.com/natolambert/status/2069439017750609972)

New lecture for the book! Nominally about synthetic data, but mostly is a walk through of the distillation literature from the Hinton 2015 paper to multi-teach on-policy distillation of today!

At 7.4 hours of video in my post-training brain dump and counting :)

It was fun to stare at the math long enough and talk through the 3-4 core changes that needed to be made to the original formulation to have on-policy distillation be ready for the mainstream like it is today (and in RL frameworks).

Otherwise, I include a bit of a history lesson for how synthetic data generally slowly took over all post-training data research (it wasn't always the case)! Then I do some 101 review on constitutional AI, rubrics, and other popular methods.

00:00 The emergence of synthetic data
10:50 Background on teacher-student knowledge-distillation
24:47: On-policy distillation (OPD, MOPD, and OPSD)
37:11 Constitutional AI & AI Feedback
45:50 Rubrics as rewards & conclusions

Ofc, watch on YouTube etc.

## 2026-06-24 (https://x.com/natolambert/status/2069788933668638839)

Another quick lecture -- I've been asked many times for prereq's to my book and what you should know, so built a little lecture (with GLM 5.2) to cover some more basics.

Topics include:

00:00 Introduction & Course Prerequisites
01:37 Language Models Overview
02:47 The LM Head
04:29 Softmax & Log-Probabilities
06:13 Anatomy of an LM Training Example
06:37 Computing LLM Probabilities (+Phoebe the Dog)
09:52 Three Common Masks in Post-Training
11:03 A Small Decoding Review
12:14 Training an LM: Cross-Entropy
13:23 Optimization & Fine-Tuning
13:55 Pretraining to Midtraining to SFT Pipeline
15:25 Probability Essentials: KL Divergence & Entropy
19:36 Sigmoid & Pairwise Likelihood
20:29 Reinforcement Learning Framing (MDP)
22:28 Transitioning Tools into Post-Training
23:12 Recommended Resources & Wrap-Up

Happy learning and I'm still taking questions from during the course for Q&A videos.

## 2026-06-30 (https://x.com/natolambert/status/2071972882264268923)

When we were in China, @xeophon and I made a quick detour to visit Meituan. They continue to be one of our favorite open model builders, as they're showing how a variety of companies can succeed here and baffle a lot of people as to why they're making models.

Meituan is one of the larger tech companies in China. They're building LLMs to add services to their own products. In China the notion of the "super app" is very popular, so this dream of more services for users with AI is very natural there. 

With this, Meituan wants to own the full stack of how they deliver value to their users. When we visited, they were very unassuming about everything. We just met a few people from the LLM team, a quick meeting about building models. 

They build general foundational reasoning models, and then fine-tune it further for their products. They can release the general model to support the ecosystem and learn how it can be used.

Their focus was very clearly on ownership, and a hint of cost-saving, so the recent news of v2 being trained on asics fits with that mentality. They want to deliver real products to users with low cost.

Companies like this will keep building models in China. It's a small micro study of how different the players in the AI ecosystem are. Kimi, Z ai, etc are all much flashier offices, come across as the "hot new thing" but Meituan has the talent and resources to build models as well.

Congrats to the Meituan team & thx for having us!
