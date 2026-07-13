# @willdepue — long-form tweets

## 2026-06-21 (https://x.com/willdepue/status/2068775102259351576)

having a hard time enjoying twitter nowadays. feels like the way i use this app (tweeting whatever comes to mind, not being super careful with my words) is not sustainable

its just really not fun if everything i say has to be unimpeachable. i usually tweet as if i were taking to a friend, assuming people can charitably interpret the gist of what im trying to say. i‘m pretty sloppy with my words and often share half-developed thoughts, but that used to be fine

but i don’t think that makes sense anymore. i miss having a smaller account, most tweets of mine get way more engagement than they really should. i’m not being realistic about the weight things i say hold anymore

also im unfortunately sensitive to the criticism that this attention brings such that it doesnt feel worth it

like im the first to admit a lot of things i say are kinda retarded too. but thats the whole fun of twitter is just sampling at high temperature and saying shit. who cares

i also think the algo changing to be more mass market does rlhf you to tweet more slop. like nuanced takes don’t really make it out, tight, hyperbolic, catchy stuff does, so i start leaning that way and it’s a very bad habit

twitter used to be really good at keeping your content constrained to the people that would understand it. and this isnt true at all anymore 

i think the solution is to do only longform, or entirely move to an alt, or just stop sharing my thoughts altogether

## 2026-07-06 (https://x.com/willdepue/status/2074178395462848800)

A Stargate for Data

Labs are on a trajectory towards >$100B/year of data spend by 2030. As we begin the trillion-dollar compute project, we need to think about the equivalent civilizational-scale effort for the other core ingredient: data.

At the foundation of the scaling revolution is a simple empirical law: deep neural networks improve smoothly, near magically, as you scale two things in proportion — (1) the size of the model and (2) the amount of data you train on. And despite the scaling laws being brutally diminishing, we’ve successfully bitten the bullet of logarithmic scaling with exponentially larger clusters and datasets, and received incredible new capabilities in return.

But this exponential scaling is bound to hit some limits. Oddly enough, compute has compounded fairly smoothly without limit, with trillions flowing into hypercluster buildout. Instead, we’re starting to hit the limits of an exponential demand for data. Gone are the days of being purely in the compute-limited regime, where we had effectively infinite internet data but never enough GPUs, we’re now entering a data-limited regime.

Luckily, this limitation is coinciding with staggering improvements in AI capabilities. Incredibly, we seem to have a real line of sight towards automating a majority of knowledge work with the methods we have today. RL + pretraining, and the data for each, will be generally sufficient to achieve most economically valuable tasks, given some minimal algorithmic progress and continued compute scaling.

In a data-limited world, economic progress & scientific acceleration will be directly bottlenecked by our coverage in each domain. We need to see data collection as imperative, deserving the same civilizational ambition we’ve given compute.

The internet as a one-time subsidy

It’s underrated how much all progress in AI owes everything to the blessing of the internet, this one-time civilizational subsidy to deep learning, decades of unintentional accumulation of a perfect dataset: every book, blog post, image, video, paper, discussion, etc. all digitized and freely available. Without the internet, we’d likely see comparably minimal progress in AI today, and in fact, if you notice where systems currently underperform, it’s almost always a domain where web coverage is limited and data is private, expensive, non-digitized, or non-existent.

But we’re running out of it. There are only about 300 trillion tokens of useful public human text, and the internet doesn’t produce nearly enough new high-quality data to match what scaling demands — we’re soon to hit the limits of public data for pretraining. And though the advent of RL bought us reprieve — chain-of-thought RL needed a new form of untapped data, gradable math & coding tasks, also available online — we’re quickly running dry of hard tasks for RL as well.

Why do we need so much data anyways? Humans learn comparably in far less time, needing just one textbook where language models might need the equivalent of hundreds to learn a new topic. It’s possible we discover methods that are massively more data efficient — synthetic data, data efficient architectures, other exotic algorithms — but fundamental progress is slow and highly unpredictable, and the recipe we have just works today.

And, while I’m wary of getting too deep here, even arbitrary data efficiency can’t replace data that just doesn’t exist in the first place. There’s a massive amount of missing information on the web: the dark matter of the internet — tacit knowledge, undocumented processes, etc. — most of which was never published and lives only inside organizations, the physical world, or just in people’s heads. I’ll leave it here and say, for reasons far longer than I can fit in this post [1], it’s best to operate on the assumption that our insatiable desire for data will continue as it has for the last decade.

There will be >$100B/year in data spend by 2030

We’re not screwed yet, of course. Only a fraction of useful data in the world is on the public internet, the rest is stored inside private datasets, corporations, personal archives, universities, governments, and otherwise. Labs can and will continue to license these private datasets, or create them from scratch, like Anthropic’s book scanning project. And we’ll increasingly task human experts to manufacture new high-quality data, with a large fraction of hard RL training tasks already being sourced this way.

But collecting this data, unlike before, will be expensive. As the free internet dries up and demand for data rises, we should see labs investing equally in data as compute, likely spending a significant fraction of their compute budgets on data. As we see trillions spent on compute, we should also expect hundreds of billions spent on data (human data & collection budgets), given their equivalent importance. And, notably, data spend is already tracking this way: total data spend across vendors, not counting internal lab efforts, is already roughly $7 billion per year. It’s quite reasonable we’ll see >10x by 2030.

Data is the moat

Data becoming increasingly private will also majorly shift the competitive landscape. While compute is a commodity — everyone buys the same chips and builds the same clusters — data really isn’t. The big reason why frontier models have felt eerily similar to one another, until now, is they were trained on substantially the same internet (pretraining data variability across labs seems pretty low). As labs diverge onto more exclusive, manually collected corpora, I think models will begin to increasingly diverge.

OpenAI pulling ahead in mathematics and Anthropic in cybersecurity isn’t an accident. I really think laser-focused collection of high-quality midtraining tokens, custom RL tasks, environments, with dedicated research effort, has driven much of the visible progress in the last year. James Betker has an excellent blog about “the ‘it’ in a model is the dataset”: model architecture and compute buy you efficiency and order-of-magnitude performance, but ultimately, models, of any architecture, are such incredible approximators of their dataset that the core meat of a model boils down to just that, nothing else. Data is a major moat.

AGI long, ASI short

As I’ve tweeted before, I’m confident that, despite the narrative, the data labeling industry will continue to fuel great businesses and be an excellent AGI long, ASI short. The argument is just: By the time the AGI labs no longer need data, it’s probably over for everything else too [2]. In this frame, the last companies left should be the data companies, as the last speck of economically relevant data is sucked in. And these companies are already among some of the fastest-growing companies in history: Mercor, founded three years ago, is rumored to be doing $2 billion in revenue with something like a few million expert labelers under contract.

While these businesses are very non-stationary, what type of data is needed shifts constantly, I don’t think that diminishes their value. The long-tail of the economy is long, and the value isn’t diminishing as you extend farther into more obscure information: as models get more capable, the value of the marginal dataset goes up, not down. Automating a full job means covering its full distribution of tasks, tools, edge-cases, and long-horizon loops. There’s some O-ring logic to it: a dataset that buys a 1% bump can justify a previously unjustifiable collection cost when it’s the difference between a system that does 99% of a job and one that does all of it [3].

The competitive dynamics of the data industry are still evolving but as demand for data is increasingly niche, ultra high-quality, expert-generated, I think we’ll see real consolidation. Again, contra-narrative, we’ll probably see true competitive differentiation built on brand, quality control of data (which, from personal experience, can vary massively), as well as in network effects from the talent networks themselves over time. We’ve already seen rapidly shifting data type demand work in favor of incumbents, benefiting those with early knowledge of where the market is headed.

The binding constraint

It’s truly remarkable that we seem to have the recipe — pretraining + RL — to absorb most economically valuable work, despite being far from a lot of what we expected from “AGI”. The same way chess engines revealed we never needed general intelligence to solve chess, as we originally thought, we’ll soon realize that software, mathematics, and the vast majority of the economy (including physical, just running ~3 years behind!) are the same. If recursive self-improvement or some other algorithmic breakthrough arrives, that’s wonderful, but we really don’t have to wait for it. The binding constraint between here and an automated economy isn’t that, it’s data coverage: every app, workflow, edge case, process, etc. sitting in private stores or someone’s head.

Ultimately, while we make tremendous strides in more efficient model architectures, and clusters like Stargate equip us with zettaflop-scale compute, we really aren’t making rapid progress collecting the data we lack.

We’ll soon live in a world where we have the methods & compute to accelerate scientific progress or economic growth, but not the data. And we’re already there today: frontier models would surely be as good at accounting/many medical tasks/legal advice as they are at software engineering if we only had the same pretraining & RL coverage as we did for code.

I really want to drill this in: The speed at which we automate the economy is going to be directly rate-limited by our ability to collect data about it.

Worth noting that under this assumption, with data as defensible and directly proportional to economic & scientific progress, data should also be considered a national strategic asset like compute. Imagine what we’d do in a world where we had a Manhattan Project-effort for AI and needed to mobilize data collection as a limiting factor. We should be concerned about China, with greater state capacity and authoritarian economic control, being capable of mobilizing data collection at national scale, potentially compounding their economy and scientific output faster than us down the line.

A Stargate for data

I’m leaving my complete ideas for a future post, as this one is already far too long, so I’d really like to pose the question here. Stargate exists because we organized trillions of dollars, international strategy, gigawatts around compute as a fundamental ingredient. What would equivalent ambition look like for data?

Obviously, scaling data collection, a heterogeneous mass of information across the economy, isn’t going to be as clear as scaling compute, as a homogenous infrastructural effort. A core division will be first, coverage — all uncaptured knowledge sitting across the economy/science/physical world and all that simply isn’t recorded — and, secondly, sheer volume in the domains we already train on: more hard math tasks, more high-quality web text, way more coding data, more legal drafts, etc.

I have a post coming soon which breaks down my proposals. There’s a lot of room for creativity. Quickly, we’ll probably want to start with a deep census of what we have and what we’re missing, predict what the 2030 model will still be bad at and work backward to what we should be collecting today. You can probably license a large amount, leveraging high lab valuations to buy datasets or companies altogether. There’s an adversarial nature to a lot of this collection with firms, so there’s lots of engineering to do this correctly. We should go convince important companies to turn off deletion policies, even if we’re not buying from them yet. Data flywheels in consumer products will be massive. Confidential training, government legislation for grant-funded research, running companies at a loss for their data, etc.

We’re headed towards hundreds of billions in expenditure, national prioritization, and major data limitation on the horizon. We have a great opportunity to think creatively about what a megaproject for data would look like: How do we, deliberately this time, construct the next internet’s worth of data?

Footnotes:

[1]: I’ll probably soon publish my much longer post explaining my position on data efficiency and why the value of this data is still pretty high in most worlds regardless of new algorithms.

[2]: The “AGI freeroll” bet: heads you win, tails ASI flips the world upside down anyways.

[3]: We already see a glint of validation of this point, given the data market is strongly tilting towards ultra-high-quality agentic data, rather than unskilled labeling — niche expert workflows, live environments, and evaluations requiring increasingly obscure talent & knowledge — yet shows increasing, not decreasing, revenues.

## 2026-07-06 (https://x.com/willdepue/status/2074189053248094467)

@ishan__1111 It's a really hard question, but I think the answer is no. I'm hiding a ton of complexity in this essay: pretraining, RL, environments vs. tasks, all with different dynamics. In short, inference compute scaling alone seems to miss a lot of important aspects of model intelligence.

## 2026-07-06 (https://x.com/willdepue/status/2074191244633506258)

@absenteewarlord It's a good point, but I think (1) my error bars on ASI/RSI are wide — and include 'never' — plus (2) progress on fundamental problems is really slow. And given most of this data will still be critical even in a continual learning/RSI world, so why not go get it now?

## 2026-07-06 (https://x.com/willdepue/status/2074202260855500929)

@peeyuzz Again very complex topic, hard to answer. But synthetic data, as most people use the word, is still very crude as a sizable but quickly diminishing multiplier of data you already have. Most of the data we're missing doesn't exist anywhere at all, synthetic data doesn't fix that.

## 2026-07-06 (https://x.com/willdepue/status/2074272067109704154)

I have a lot of thoughts about this that I’ll share later, but ultimately, the point I’m making in the A Stargate for Data is majorly about missing or low coverage data, which simple data efficiency wins won’t solve at all.

There’s another key point too: so long as these methods don’t lead to deeply better models, just the same model but trained with less data, while also costing much more compute, one would always wish we just had more data and could train efficiently as normal. Under this frame, data efficiency isn’t that important, it’s just a workaround limited data in an uninteresting way.

You could imagine a world where our current LLM training recipe truly is actually universally compute optimal and that you can only trade compute for data at great efficiency cost. I don’t believe this is true, I strongly believe we’re off the efficient frontier, that there should exist much better radically different algorithms that can learn faster than humans, all with less compute not more. 

But most regularization methods and ensembling and etc are basically operating in this space: throw efficiency away, get data back. And if it’s easier and no different to just get more internet to train on, why not do that instead?

Ultimately, the real “data efficiency” wins in the world are never named data efficiency wins, they’re just normal compute wins: Muon lets models achieve higher performance, in less time, with less steps: performance per token is higher. If you’re going to find real breakthroughs on sample efficiency, you have to first consider why a decade of deep learning iteration never found it as a way to increase compute-optimal performance!

For example, I’m very partial to the view that our  objectives might be deeply off, that data efficiency with respect to pretraining metrics is the wrong place to look. I think the church of compression at all costs might have gone too far. Why do we care about test loss? We don’t: We care about the downstream things it correlates with. It’s somewhere here, outside of the normal frame, you might find something deeply substantive.

I really enjoyed the recent NextLat paper recently, which seemed to show better internal representations from multi-token/latent prediction. A main exploration of mine right now is whether predictive-coding inspired ideas, where models don’t just predict the next token but also their beliefs about the next & future token, might have a big effect. This additional objective will likely hurt test loss, but who cares! The hope is that the model learns a deeper understanding of the world, which I’m skeptical is well measured by that.
