# @dwarkesh_sp — long-form tweets

## 2026-05-15 (https://x.com/dwarkesh_sp/status/2055324348332871779)

New blackboard lecture w @ericjang11

He walks through how to build AlphaGo from scratch, but with modern AI tools.

Sometimes you understand the future better by stepping backward. AlphaGo is still the cleanest worked example of the primitives of intelligence: search, learning from experience, and self-play. You have to go back to 2017 to get insight into how the more general AIs of the future might learn.

Once he explained how AlphaGo works, it gave us the context to have a discussion about how RL works in LLMs and how it could work better – naive policy gradient RL has to figure out which of the 100k+ tokens in your trajectory actually got you the right answer, while AlphaGo’s MCTS suggests a strictly better action every single move, giving you a training target that sidesteps the credit assignment problem. The way humans learn is surely closer to the second.

Eric also kickstarted an Autoresearch loop on his project. And it was very interesting to discuss which parts of AI research LLMs can already automate pretty well (implementing and running experiments, optimizing hyperparameters) and which they still struggle with (choosing the right question to investigate next, escaping research dead ends). Informative to all the recent discussion about when we should expect an intelligence explosion, and what it would look like from the inside.

Timestamps:

0:00:00 – Basics of Go
0:08:06 – Monte Carlo Tree Search
0:31:53 – What the neural network does
1:00:22 – Self-play
1:25:27 – Alternative RL approaches
1:45:36 – Why doesn’t MCTS work for LLMs
2:00:58 – Off-policy training
2:11:51 – RL is even more information inefficient than you thought
2:22:05 – Automated AI researchers

## 2026-05-18 (https://x.com/dwarkesh_sp/status/2056450047328628837)

.@gwern saw AI scaling coming before almost anyone outside OpenAI.

How was he able to predict this trend?

He told me that his core idea was that intelligence is just compute, data, and parameters - no clever algorithm needed.

He didn't come to this view in a eureka moment. He just read paper after paper and nudged his priors a little each time, until the trend seemed obvious.

## 2026-05-19 (https://x.com/dwarkesh_sp/status/2056856368745726238)

One of the most important and under appreciated trends in the world right now. 

1. 100s of billions of dollars will soon be available to solve big problems (making the world resilient to ASI, ending factory farming, etc).
2. The projects and organizations which will  turn billions of 2027/28 dollars into impact need to be started NOW.
3. We need really talented people to start and run and work for these new projects. What @nanransohoff calls general managers, who feel personally resposible for solving one of the world’s important problems.

What is especially scarce are detailed visions about what making AI go well looks like. These will help inform what problems these new projects ought to work on.

## 2026-05-20 (https://x.com/dwarkesh_sp/status/2057174752993980831)

.@ericjang11 tried using transformers for his Go bot, but they couldn't beat ResNets.

The reason gets at something general about architectures.

ResNets are biased towards the local. Nearby things matter more, and a useful pattern in one place is a useful pattern anywhere.

Transformers are biased the other way, towards global context, with every position able to attend to every other.

Most Go fighting is local, and a useful local pattern learned in one position can be applied anywhere in the board.

A ResNet's inductive bias means it gets these insights about Go for free. But a transformer has to pay for them.

## 2026-05-20 (https://x.com/dwarkesh_sp/status/2057229028881510630)

Monte Carlo Tree Search training corrects the model move by move, while current LLM training only tells it whether the whole trajectory worked.

MCTS is preferable if you can get it. But nobody's managed to get MCTS to work for language models.

In his blackboard lecture @ericjang11 talked to me about why:

## 2026-05-26 (https://x.com/dwarkesh_sp/status/2059349154854555708)

A large portion of animal intelligence doesn't require any learning, claims @karpathy: it's baked into DNA.

AI models, by contrast, start from random weights. They have to learn their intelligence, mostly by imitating the internet.

This is so different that Andrej thinks it's a fundamentally different kind of intelligence: LLMs are more like ghosts than animals.

## 2026-05-27 (https://x.com/dwarkesh_sp/status/2059755945530622100)

.@gwern almost thinks there's no such thing as general intelligence.

Humans and AIs just learn a large number of individual specialized tricks. In any given situation we're doing search over special cases, nothing more.

What matters is just the number of individual tricks that we can search over - which is mostly determined by compute.

## 2026-06-04 (https://x.com/dwarkesh_sp/status/2062564414142972041)

Human beings whose emotional centres are damaged, even if their intelligence is still intact, have terrible decision-making skills.

Whatever role emotions are playing in humans, it's necessary for agency.

Ilya speculates that the equivalent for AIs is something to do with value functions - and that it might not emerge through pre-training alone.

## 2026-06-07 (https://x.com/dwarkesh_sp/status/2063753306296746276)

In medieval times, within the arms race of ever more demonic torture devices, some sadistic genius came up with the idea of the Little Ease.

This was a prison cell built so small in every dimension that a grown man could not stand upright in it nor lie down at full length nor properly sit.

The pain is relentless and without relief and inflicted by one's own body. Prisoners were known to go insane within a few days. A stay at the Little Ease was considered even more cruel than the rack, the thumbscrew, and the other ghoulish machinery of the Tower of London.

A breeding pig will spend her whole life in a version of that box.

These are social, roaming creatures (more intelligent than dogs) who will never leave this corset of steel.

They have been selectively bred to be bigger than their frames can support. Yet we put them in cells so confined that they cannot comfortably sit, and their attempts to do so (for example, by sneaking their limbs into adjacent stalls) reliably lead to fractures and sprains.

They cannot sweat, yet have nothing to roll around in to cool themselves off. Except their own manure, which (contrary to the common misconception) they are so averse to (thanks to their strong sense of smell) that new sows will often suffer from constipation to avoid soiling the space from which they eat and sleep.

Here is how the writer Matthew Scully described what saw at one of Smithfield’s “gestation barn”:

> “Sores, tumors, ulcers, pus pockets, lesions, cysts, bruises, torn ears, swollen legs everywhere. Roaring, groaning, tail biting, fighting, and other “Vices,” as they’re called in the industry. Frenzied chewing on bars and chains, stereotypical “vacuum” chewing on nothing at all, stereotypical rooting and nest building with imaginary straw. And “social defeat,” lots of it, in every third or fourth stall some completely broken being you know is alive only because she blinks and stares up at you … creatures beyond the power of pity to help or indifference to make more miserable, dead to the world except as heaps of flesh into which the [insemination] rod may be stuck once more and more flesh reproduced.”

—

The Save Our Bacon Act is trying to unroll the few state protections we have against this barbaric cruelty - for example California’s Prop 12 - which banned the sale of pork from pigs kept in gestation crates.

It’s incredibly important we don’t end up with this sort of federal preemption.

SOB will not only kill the most important animal welfare related laws in the US of the past decade, but more importantly, it will also restrict ALL future legislative progress (aka how the animal welfare movement has gotten its biggest wins).

The Senate is currently deciding whether to add the SOB Act to the Farm Bill.

With relatively little money now, we can discourage the most pivotal senators in the Ag committee from backing this amendment.

Defeating this bill is even more important given the amount of philanthropic funding I expect to come online in the next year or two.

It will plausibly be over 10x more expensive to repeal SOB than to prevent it from passing in the first place.

All that money that could be spent transforming our society's relationship to mass animal suffering will instead have to be spent just getting us back to where we are right now.

That's why money spent now fighting this bill (and I mean right NOW) is so effective.

If you’re in a position to donate six figures, please DM me.

## 2026-06-12 (https://x.com/dwarkesh_sp/status/2065464765863039281)

Lots of people think it's obvious that humans learn by imitation, starting with babies imitating their parents.

Richard Sutton thinks this is completely wrong.

Sutton basically thinks direct imitation plays almost no role in animal learning, and at most a small role in human intelligence.

When one animal ends up doing the same thing as another, he thinks this is the result of RL-style trial-and-error, not direct imitation.

And if imitation isn't really a kind of learning, then training LLMs to imitate humans isn't really Bitter Lesson–pilled.

## 2026-06-30 (https://x.com/dwarkesh_sp/status/2071994830813532481)

Always so much fun to chat with @3blue1brown 

AI has been making much faster progress in math than in other fields.

As a result, mathematics is showing us, very concretely, what AI progress in other fields will look like.

Even within mathematics, there's a jagged landscape. What does it look like?

What is the nature of the most important conceptual breakthroughs in the history of mathematics, and how different are they from what AIs are currently able to do?

Does AI (on net) increase or decrease human understanding of the field?

How big is the overhang from having AIs systematically try to connect ideas already in the literature?

And what advice does Grant have for aspiring mathematicians, coders, and other students who are passionate about fields that are being most transformed upon by AI?

0:00:00 – AI is discovering new proofs. Is that AGI?
0:11:32 – The verification loop on conceptual breakthroughs can be a century long
0:26:12 – Will we understand an AI proof of the Riemann hypothesis?
0:38:08 – Can AI find the hidden bridges between fields?
0:53:48 – Why real-world tasks don’t fit into RL environments
1:07:07 – Good writing requires theory of mind that AI still lacks
1:16:02 – Why learning will still depend on human curation

Look up Dwarkesh Podcast on Spotify, Apple Podcasts, YouTube, etc.

## 2026-07-10 (https://x.com/dwarkesh_sp/status/2075619763972141539)

Adam Brown (@A_G_I_Joe) is back!

General relativity is said to be the most beautiful idea the human mind has ever produced.

Most of us will never get to fully appreciate its elegance by taking the 20-lecture graduate course Adam taught on it at Stanford.

But in the video below, Adam distills the key idea at its heart so clearly and compellingly that even I could keep up lol.

At the core of general relativity, Einstein is trying to figure out the principle behind a particular coincidence: that the mass that resists acceleration and the mass that gravity pulls on just happen to be exactly the same. Adam then leads us through the path of insight which Einstein called his “happiest thought.”

Then Adam lectures on black holes. First, by showing how even under special relativity you could create a perpetual motion machine if black holes weren't truly black. And then, by explaining why the observations of an infalling observer and a distant bystander to the black hole would be so radically different

Adam leads Blueshift, the team at Google DeepMind cracking science and reasoning.

Which gave us the opportunity to discuss at the very end how close we are to AIs that could rediscover general relativity from scratch. Stay till the close for some philosophy of science.

0:00:00 – The coincidence that led Einstein to general relativity
0:16:42 – Gravity is a consequence of curved spacetime, not a force
0:31:46 – Why black holes prevent unlimited energy extraction
0:47:12 – Black holes are the ultimate power plants
1:13:50 – What falling into a black hole would actually feel like
1:18:51 – The three ways we know black holes are real
1:24:21 – The first time we saw gravity bend light
1:29:33 – How far can AI get without experimental evidence?

Look up Dwarkesh Podcast on YouTube/Spotify to watch. Enjoy!
