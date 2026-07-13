# @kunchenguid — long-form tweets

## 2026-05-02 (https://x.com/kunchenguid/status/2050648794640113947)

ok @steipete's acpx is a godsend https://t.co/jFuIzg7WWm

just added it in gnhf v0.1.31, and boom - gnhf now supports almost any agent harness you can name

for anyone building bring-your-own-agent apps, highly recommend calling acpx instead of building your own abstraction https://t.co/5tCv1TtJ3M

## 2026-05-15 (https://x.com/kunchenguid/status/2055322969682198818)

built a dead simple chrome extension for my wife and myself. sharing here as free open source as usual

Simple Words

we find ourselves spending too much time wordsmithing our email replies, just to make sure we sound friendly and respectful

this chrome extension is really simple and quite literally a gpt wrapper that only does one thing - one click turning what you mean to what's ready to send

it runs on your own api key, subscription or local LLM. the extension itself is free and open source. if you tried it out, would be keen to hear how it works for you!

extension: https://t.co/JFUZ3gQfux

repo: https://t.co/iKkspmOmMI

## 2026-05-17 (https://x.com/kunchenguid/status/2055868990971658725)

good read, but this is nothing new

people already knew how to be unhappy for centuries:
- chase after money and status
- compare yourself with others
- blame society for your inaction

that’s how millionaires can still complain about their lives

the fix is extremely easy:
- find a real mission and chase after it
- walk your own path and compare with your past self
- take an action to improve yourself. not tomorrow. not later. NOW

## 2026-05-22 (https://x.com/kunchenguid/status/2057700714626105412)

i'm strongly against model companies focusing too much on harness, but i would love to hear if anyone has a strong argument for it

my reason against it:

if openai didn't build GPT 5.5, no one else can. this is their core competence

if openai didn't build codex cli and app, we have opencode and t3code. building harness is NOT their core competence

this is not saying products like claude code, codex aren't good - i genuinely think these are top tier products built by really talented people

my point is - the world might be a better place if model companies focus more on their core capability and give us better, faster, safer and cheaper models, rather than competing with the ecosystem in the application layer

what do you think?

## 2026-06-15 (https://x.com/kunchenguid/status/2066573353985651148)

several people pointed out i was wrong about the Fable shutdown in my post below

turns out i was indeed, and i appreciate the corrections. i learned  a few things from this discussion so i want to be transparent and share the learnings broadly as well

i still think the broad shutdown of Fable 5 is a bad outcome, and i think doing this as an emergency lever on a product that was not built around this constraint is a bad way to govern frontier models

but my original reaction “using foreign national as the gate for AI models seems dumb and practically unenforceable” proved to be incorrect

the biggest thing i learned is that “foreign person / foreign national” is not some random new category the government invented on the fly here

it's already a common concept under the export control law. controlled technology or source code can count as exported when it is released to a foreign person inside the US. and the law already has its machinery for that case.

if the model is treated like a controlled dual-use technology, the product can be forced toward an identity-verification regime: government ID, age/identity checks, citizenship or residency status, customer screening, etc

many online services like banks, gambling apps and some other regulated products already do that all the time

it would be very expensive, user-hostile, privacy-sensitive, and business-model-changing for an AI API/product. but “annoying and product-breaking” is different from “unenforceable.”

so a better version of my take is:

1.⁠ ⁠legally, the government does have existing export-control concepts that can target foreign persons, including within the US.

2.⁠ ⁠technically, Anthropic or any lab could build KYC-style access control if forced to

3.⁠ ⁠practically, current AI products were not designed around this, so a sudden order can easily turn into “turn it off for everyone” until the access-control surface exists, which is not ideal

4.⁠ ⁠strategically, this still has big costs: it makes US AI products less reliable for global users, pushes other countries and companies toward domestic/open alternatives, and may weaken the exact ecosystem advantage the US wants to preserve. it also negatively impacts foreign employees working for US companies including the frontier AI labs themselves

## 2026-06-18 (https://x.com/kunchenguid/status/2067650728290824269)

time to reveal the next big gun in my agentic engineering setup - Firstmate!

it's the only agent session i directly talk to now. if you find it mentally exhausting to juggle between all the agent sessions, this is the solution

free &amp; open source as always - details below 👇 https://t.co/UEvPoPv3iK

## 2026-06-18 (https://x.com/kunchenguid/status/2067728608584675465)

pro tip: disable Claude Code "auto memory" to improve its quality

you can do so by typing "/memory", select auto memory and turn it off. this can also be done with setting env var CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

why? 

- i've seen so many times that stale memory caused the agent to make bad decisions. the information it puts into those memory files are inherently stale in a constantly-evolving project, and the agent would often trust the memory instead of looking up latest information

- it stores memory into a claude-only location that other agents don't share. this is anthropic deliberately trying to create vendor lock-in. as a user, it's much better to disable "auto memory" and make claude store memory into standard locations such as AGENTS.md or AGENTS.local.md that is agent-agnostic and portable

## 2026-06-21 (https://x.com/kunchenguid/status/2068835459682496592)

X might just be the only platform whose head of product is publicly executing engagement farms almost every day

this really makes X a rare place where i genuinely believe good original content will win

having grown my account here i feel one interesting problem left is that it’s not quite easy to cold start a new account without some spectacular entrance, so there are still lots of interesting people with good stuff to share but don’t quite get the reach. perhaps this is more human nature but would love to see the platform helping solve it somehow

## 2026-06-24 (https://x.com/kunchenguid/status/2069640707749679194)

the person who created google workspace CLI got fired by google

having been at big tech for decades, let me take an educated guess on what happened here -

1. with a company at this size, you have to think of different internal departments as completely different companies. see how deepmind has their own "CEO"? different leaders have their own kingdoms and agenda

2. Justin was DevRel - not on the core product team. unfortunately this meant from the workspace leadership's POV Justin was a random guy popping out of nowhere. i bet Justin here didn't get upfront alignment from google workspace leadership before shipping this workspace CLI

3. now put yourself into the shoes of workspace leadership for a second - maybe you already have a product team working on this. maybe you have a plan to monetize it differently, not for free. maybe you have other ideas for what this CLI ought to be. but now a random guy just shipped this to the public without talking to you - this now forced your hands, and made you look bad internally for not being able to ship it from your own product team. you even set up internal processes to prevent this from happening, but looks like the due process was being skipped. so of course that's unacceptable

that is the unfortunate reality of working in a big company - you can't just ship things, even if they are good. you are not supposed to charge ahead as an individual and play hero. you are part of a team and need to join the game

## 2026-06-30 (https://x.com/kunchenguid/status/2072058052480778248)

openclaw finally released their mobile apps and it started a storm of criticism because the apps have the "vibe coded" vibe

here's my take on the whole drama from an unbiased point of view -

1. i condemn people who would shit on a free open source project, and do so with an entitled attitude instead of offering constructive feedback or direct help. they are mostly doing so to feel superior and to generate engagement as an "influencer"

2. people are confused about what Peter is doing after joining openai, and i don't blame them because it's genuinely confusing

my understanding is he's now full time working for openai, which is a supporter of openclaw but does not own or run it. so openclaw is now more in the hands of the open source maintainer team

3. in this shitstorm, we're starting to hear Peter say "it wasn't me. it was the maintainers" which IMO is not a good messaging when openclaw is clearly still a big part of his personal brand

as someone whose bio says "ClawFather" i think a better messaging is to take full ownership and start talking about what he could do to improve the project, not as a day to day contributor but as a leader whose prior work had a massive influence, and who still has the power to influence the future of openclaw

"we're actively looking for talented designers to join the maintainers team" would be received better than pure defense

4. speaking of product design, traditionally open source is a thing only for programmers. but this is a very direct example that as a piece of software gets more and more adoption and popularity, the user expectation rises with it

UX design skills are often being under-valued in the programmers' world (speaking as a programmer myself) and a programmer would bring in a design only when they "have to"

in an era where coding is increasingly done by AI, i think the mindset has to change. open source projects that have a prominent user interface should proactively look for people with good UX design skills to join the core team, and programmers ourselves should start to learn and care more about crafting the experience as well

5. openclaw has a real perception crisis right now - not sure if the team fully internalized this or not

even before the mobile app release, people have been rightfully complaining about the fragility of the core openclaw especially how often it breaks during an update. many people tried hermes and stuck with it purely because it's perceived and talked about as the more stable alternative. maybe openclaw has already improved but perception take time to heal

and now with the mobile app release not quite meeting some people's bar for a high profile project like this, there's a real risk that more and more people start to associate openclaw with "low quality software" - i see openclaw as something quite monumental and would absolutely hate to see that happen, but i really think the risk is there and it's better we acknowledge it

and now because of Peter's connection with openai, this perception crisis actually affects more than people think, because if haters and competitors successfully landed a narrative that "openclaw is low quality", then all the tokenmaxxing and loop engineering stories and thought leadership start to fall apart

my hope is the openclaw team doesn't take offense from the shitstorm and instead extract some truth from it - graduate from the "yeah it's just an open source project it can have rough edges and you can't criticize us volunteers" phase into something more mature that can continue to justify and keep up with their level of popularity

## 2026-07-06 (https://x.com/kunchenguid/status/2073926590116032939)

my hot take on how much AI code we should review -

you should review as much code from AI as your engineering director reviewed your code before AI

here’s the chain of thought:

- why do we even use AI to code? it’s to allow us to ship more

- how much more should a single developer be able to ship now, compared to pre-AI? i see us going from 1-10x in the past 3 years, and on a trajectory to hit the 100x magnitude soon

- that means every developer is going to own as much scope as a pre-AI director of engineering

- i haven’t met a single eng director who said their team’s codebases were perfect and exactly how they would like it to be. why? because people who try to achieve that will fail to become a director

- how do directors handle that level of complexity? it’s absolutely not by reviewing and micro-managing every engineer’s code. it’s through managing the culture, workflows, resource allocation, guardrails and measurable outcomes 

- when a director sees the team struggle on productivity or quality, they might lean in and try to understand the state of the codebase to develop some intuition for how to improve things systematically. even this is often done with the help from their principal engineers - i believe this is the right balance for how we should manage AI

so, if we want to get a massive boost from AI, we must be prepared to operate in a way that allows us to manage much higher complexity, which requires that we remove ourselves as a bottleneck and manage the outcome at a different level

shape your AI agents’ workflows - are they doing adversarial review? are there good automated tests? are they presenting evidence before shipping? are they doing phased rollout? are there good metrics to catch problems?

survey your agents for feedback - ask them to reflect on their past sessions and report biggest problems causing them to struggle, and allocate enough tokens to get those problems fixed

focus on outcomes - are your agents doing busy work? do you truly understand customer requirements and what work is worth doing? are your agents’ work generating the business outcome you expect?

that’s how we truly scale

## 2026-07-09 (https://x.com/kunchenguid/status/2075353225004556556)

right now i have fable still in the subscription with limits just reset; i have gpt 5.6 just added to the mix; and i have grok 4.5 also working super well

after using all of these for a while, i suspect something really interesting is about to happen

tl;dr - i think anthropic is in serious trouble

1. portfolio competitiveness

opus and sonnet (who still remembers they have haiku?) are basically not even worth using any more. both gpt 5.6 and grok 4.5 are just outright better

fable is the only real competitive option from anthropic now, but it's not even going to stay in the subscription for a while. it's also super slow and expensive

not having enough focus on efficiency and being obsessed with intelligence upper bound might have just led anthropic down a bad road

2. compute constraint

an interesting side effect of grok becoming so good is that its demand might explode, especially with cursor now heavily doubling down on grok

if grok suddenly gets a lot of usage, it will need compute. and xAI may not want to rent compute to anthropic any more

if anthropic can't secure more compute, they will be in trouble because there's just no way to grow the business

3. modalities

both openai and xAI started investing in multi-modality since the beginning, while anthropic tunnel-visioned into text and code

now i find myself increasingly rely on openai's image generation and grok's video generation. if i can only keep one subscription i would have no choice but to drop anthropic because i do need the other modalities

overall at this rate, what's going to happen is that the vast majority of agentic work will be done by non-anthropic models, and only very occasionally other models will escalate hard problems to fable as an advisor

my advice for consumers remains the same as what I've been saying for a while - get ready for a multi-agent, multi-vendor world. use tools that allow you to freely switch between models, and build a setup where you can use the right model for the right task
