# @GergelyOrosz — long-form tweets

## 2026-05-20 (https://x.com/GergelyOrosz/status/2057196503559541244)

Why is Rust different than many/most programming languages? Alice Ryhl works on Google's Android Rust team, is a Rust language team advisor, and is a core maintainer of Tokio (the most widely-used async runtime in Rust) Timestamps:

00:00 Intro
04:09 Tokio: an overview
05:11 What Alice likes about Rust
12:48 Rust for TypeScript engineers
13:51 Moving from C++ to Rust
14:34 Memory safety
18:12 Garbage collection tradeoffs
21:46 Ownership, references, and borrowing
26:59 Unsafe in Rust
31:21 Crates and Cargo
35:55 Language design and RFCs
43:02 Building new features
46:30 Editions vs. versions
49:47 Getting paid to work on Rust
51:27 Contributing to Rust
53:03 Rust in the Linux kernel
55:45 AI use cases for Rust
1:01:35 Learning Rust
1:03:54 Book recommendation

Brought to you by:

• @AntithesisHQ  – verify your system’s correctness without human review or traditional integration tests – and avoid bugs or outages. https://t.co/AKYm4cbVCU

• @sentry – application monitoring software considered “not bad” by millions of developers https://t.co/uoolyqTjhe

Three things worth knowing about Rust:

1. Rust was designed to turn implicit failures into compile errors.

Where other languages allow you to forget something, Rust makes an omission into a compilation error for things like null checks, uninitialized variables, or error propagation with the ‘?’ character. If you mess something up, it’s almost certain your program will not compile. If it does, at the very least you should see a lint warning.

2. Refactoring in Rust is safe and easy, thanks to the compiler.

Alice: “I change a return type or struct field, then just fix the compiler errors until the compiler stops shouting. And then once I’ve done that, I’ve updated every place I need to update.” Rust’s focus on correctness makes refactoring it more straightforward than dynamically-typed languages and Java-style typed ones are to refactor.

3. “Editions” allow Rust to make breaking changes without ‘breaking’ anyone’s code.

Rust editions (2015, 2018, 2021, 2024) can be mixed freely across crates. A library on the 2021 edition works seamlessly with a binary on the 2024 edition. This is how Rust evolves syntax (like adding async/await as keywords) without forcing an ecosystem-wide migration.

Thanks a lot, Alice for this great discussion! And for your work on Rust.

## 2026-05-22 (https://x.com/GergelyOrosz/status/2057773000536002897)

I used AI to double check my annual closing statements of my company - fed it bank statements, accounting statements etc, parallel to my accountant going thru it as well.

It found some good stuff, but also hallucinated a bunch of other, nonexistent problems. I feel more and more LLMs are excellent tools... in the hands of professionals who can easily confirm hallucination vs real stuff.

## 2026-05-25 (https://x.com/GergelyOrosz/status/2058893554076758119)

That feeling of: "I'm in the middle of the code... oh, this is such a nasty hack. OK, let me clean it up as I go. [2 hours pass] OK, it's done, now let me get back to where I was."

It just never happens as organically as I use AI agents. I no longer spot stuff as I don't "live in" the code...

## 2026-05-27 (https://x.com/GergelyOrosz/status/2059688730659524730)

Why is the creator of OpenCode pretty skeptical about AI productivity gains, and the hype around AI? A very conversation @thdxr (and lots of truth bombs:)

Timestamps:

00:00 Intro
07:03 Dax’s path into tech
09:04 Early startup experience
13:16 Getting involved with open source
16:13 OpenCode
23:17 Anthropic banning OpenCode
30:34 From terminal to GUI
32:34 OpenCode’s business model
36:33 Why inference is profitable
39:11 GPU bottlenecks
40:54 AI hype
45:50 AI spending
48:47 Dax’s memo
55:41 Dax’s skepticism of predictions
58:58 Engineering culture at OpenCode
1:02:38 How building works at OpenCode
1:05:36 Taste and quality
1:11:32 Dax’s work setup
1:12:35 The role of engineers and EMs
1:15:50 Advice for engineers
1:18:12 Book recommendation

Brought to you by:

• @AntithesisHQ  – verify your system’s correctness without human review or traditional integration tests – and avoid bugs or outages https://t.co/AKYm4cbVCU

• @WorkOS  – everything you need to make your app enterprise ready https://t.co/aiAee0oF5h

• @turbopuffer  – a vector and full-text search engine built on object storage. It’s fast, cheap, and extremely scalable https://t.co/w9y67Gs8ab

Three interesting thoughts from Dax:

1. No AI-native coding agent company is “winning” by being better with AI.

Dax says that none of OpenCode’s competitors are crushing them, and that nobody is using AI so well that others cannot compete.

2. Most software engineers profit from AI as time gained, not increased output — unless you change incentives!

Dax says the natural way for software engineers to “cash out” their AI tooling gains is with time savings, by doing the same work as before, but faster. Until compensation and motivation structures change, most teams should expect output to stay flat while engineers go home earlier. There’s nothing wrong with this, but AI vendors sell a different outcome to CFOs: increased output.

3. AI code generation mutes the “guilt” of doing the wrong thing, but this builds up tech debt.

Pre-AI, writing a hack felt bad, the second time it felt really bad, and by the third time you’d often just refactor in order to fix up the code. Now, the agent hides the hack, which skews devs’ judgment and results in less tech debt being cleaned up.

## 2026-06-05 (https://x.com/GergelyOrosz/status/2062950817611514219)

Small news to most, big news to me: The Software Engineer’s Guidebook is the best-selling tech book in Hungary, a few days after the Hungarian translation launched!

(This is the 8th language it was translated to!)

The best-selling list in the largest books retailer in the country: https://t.co/LC9NlmsExJ

## 2026-06-11 (https://x.com/GergelyOrosz/status/2065052608738279555)

The postmortem from Coinbase's 10-hour outage is out and... damn

They run global trading from a single region because of latency. OK, I understand.

BUT they have no automated failover prepared!

Are they praying the region never goes down?? Doesn't compute for me... https://t.co/54DtsArYlf

## 2026-06-11 (https://x.com/GergelyOrosz/status/2065080846441234451)

I am so fed up with products I pay for polluting the user interface with AI-related visual clutter

Google Docs now has a Gemini button hovering with no way to turn off. I do NOT want it or need it.

How can I get rid of it @OfficialLoganK? I am fed up with these growth hacks https://t.co/zDEm2owYo8

## 2026-06-13 (https://x.com/GergelyOrosz/status/2065799895089332432)

It’s such a head scratcher. Tried to talk to the company a while back. After months of knocking on doors (CTO, CEO, Head of DevRel) no one responded. I pinged one of their US investors who responded in hours and pulled some strings… for a seemingly annoyed Comms person to get in touch to say they might have time in 3 weeks… it was then that I just gave up. Like they wanted secrecy

Still don’t know what they do, and I’m in Europe lol

## 2026-06-17 (https://x.com/GergelyOrosz/status/2067180039024603496)

I opened Facebook, saw AI-generated videos in my feed (undisclosed that its AI, of course, commenters clearly not noticing it). Wanted to report it.

Facebook has no way to do so.

Makes you realize Facebook *wants* users to post AI videos and it drives their business... https://t.co/deKN1hW1Ip

## 2026-06-21 (https://x.com/GergelyOrosz/status/2068733026499228013)

Someone asked for career advice about a big decision (leave Big Tech job for a startup, vs stay longer or join another Big Tech)

My suggestion was:

1. Talk to others as well
2. Make lists
3. Figure out what you want ~5 years from now
4. Talk with your SO
5. Listen to your gut

Do it in this order to get more data, but then reverse order for usefulness of input :)

## 2026-06-21 (https://x.com/GergelyOrosz/status/2068740969806041595)

This whole "Dialog" is so much for the "world's elite" that I got invited in March to the next oneL

It looks exactly like many other conferences except this doesn't have much of an agenda, and too few tech ppl for my liking

Looked too off-topic to me so did not bother to RSVP https://t.co/urDeQ4jTjq

## 2026-06-22 (https://x.com/GergelyOrosz/status/2069189073520971952)

On one end, this is big news: Meta is paying $900M to be able to hire Kunal Shah to lead WhatsApp. It suggests massive investment.

So can anyone at Meta explain why critical WhatsApp teams like Integrity have been drastically reduced via layoffs, forced data labeling &amp; reorgs?

## 2026-06-24 (https://x.com/GergelyOrosz/status/2069878282208555376)

How are tech interviews changing, what is wrong with the CAP theorem, and what skills are becoming more important than coding, for devs? It was great to finally do an in-person episode with @neetcode1 , the founder of NeetCode.

Timestamps:

00:00 Intro
02:57 Neet’s take on coding interviews
06:41 Getting into tech
08:56 Why Neet isn't a fan of the CAP theorem
13:12 Quitting Amazon after two months
18:22 Google vs Amazon
22:26 The origins of NeetCode
25:27 Leaving Google to go all in on NeetCode
32:02 Why Neet doesn't fix every bug
39:26 The value of coding interview prep
42:57 Systems thinking and domain expertise
47:28 Hiring at Big Tech
52:15 Tech stack at NeetCode
57:57 The NeetCode redesign contest
1:01:46 The future of software engineers
1:09:04 Hot takes: AGI, AI skill erosion, personality traits
1:22:49 “Maybe some people should just give up”
1:24:39 How to be a standout engineer
1:27:55 Book recommendation

Brought to you by:

• @AntithesisHQ – verify your system’s correctness without human review or traditional integration tests – and avoid bugs or outages. https://t.co/AKYm4cbVCU

• @sentry application monitoring software considered “not bad” by millions of developers https://t.co/uoolyqTjhe

• Google Cloud Run – fully managed platform that runs your code directly on top of Google’s scalable infrastructure. Run frontend and backend services, batch jobs, host LLMs, and agents without managing infrastructure.  https://t.co/DJ2ll32kV5

Three interesting parts from this convo:

1. The CAP theorem’s “two of three” framing is widely taught but technically shaky.

Navi felt that is an awkward theorem that is incomplete, and felt validated when Martin Kleppmann publicly criticized it too. This is a good reminder that it’s worth thinking for yourself, and not accepting theorems as true, without understanding them.

2. The Neetcode YouTube channel took off after Navi posted that he’ll post less because he got into Google.

Before he shared that he got a software engieneering job at Google – back at that time, one of the most competitive companies to get into – there were not many people watching the Neetcode channel. Sharing that he got into Google turned out to be the best “sales pitch” though: and suddenly, people wanted to understand what he’d practiced that helped him get this job!

3. Predictions of coding’s death haven’t materialized as expected. Despite dramatic AI model improvements, Navi does not observe most engineers aren’t being laid off. In fact, he sees the opposite: devs doing more work than before!

## 2026-06-28 (https://x.com/GergelyOrosz/status/2071105819089973716)

I'm now past 50 anecdotes on the job market, and it feels there's a catch-22 position repeating:

1. Companies struggling to hire certain profiles (product-minded engineers, devtools infra etc)

2. Inbound apps are SUPER noisy, so most co's give up on them

3. Devs with the above skillset are submitting applications... but rarely ever make it thru the massive noise of inbound applications

So #1 never finds #3 and both #1 and #3 wonder what is going on

## 2026-06-28 (https://x.com/GergelyOrosz/status/2071378540872770007)

What happens when the most capable coding model (Fable / GPT-5.6) is banned by the US government, and the sending most capable is an open model?

What happens: a LOT of businesses and devs simply move to use the open model (GLM-5.2) via inference providers. Cheaper + better! https://t.co/k7dpOZMGqF

## 2026-06-29 (https://x.com/GergelyOrosz/status/2071627826328191398)

Naming and shaming a founder who has outsourced their complete business to AI, resulting in AI slop, noise, and me not wanting to ever talk to them.

I am not even sure any more if this is a real person or just a fake persona an AI bot is using.

AI slop like this is terrible. https://t.co/strIJD8vlv

## 2026-06-30 (https://x.com/GergelyOrosz/status/2071841293488267470)

One thing that is, indeed, killing PagerDuty, is that back in 2014, there was no Twilio-like service to deliver pages reliably. PD have their own, custom notifications delivery system.

But customers won't pay for that any more. And PD competitors offer a LOT more, for less!

https://t.co/u1sl513q9l

## 2026-07-01 (https://x.com/GergelyOrosz/status/2072353357956857880)

A story of why Meta signaling they don't care about engineers a few months back is resulting in resignations month later:

1. A long-tenured dev I know lost faith in Meta leadership, put out feelers at top startups

2. A few weeks ago, got an offer at a high-growth startup. Was hesitating

3. Meta leadership did a half-hearted u-turn, signaling "oh sorry, our bad, we actually care about y'all"

4. This dev talked internally at Meta w leadership chain, and just about started to believe things could change, and the right move is to stay (network, impact, TC, comfort etc)

5. Said startup had more of their team talk with this dev, also with investors, upped their comp offer, and outlined how much more autonomy this dev would have there

6. The dev realized they already felt a part of this startup, and actually would contribute meaningfully (vs at Meta being dependent on the next mood change of upper leadership)

7. Startup offer accepted, resignation handed in at Meta

This was just one such story. Meta will lose so much standout engineers this year: the damage was done recklessly (but Meta as a business will be just fine)

## 2026-07-06 (https://x.com/GergelyOrosz/status/2074112943365497196)

Amusing observation:

Many of us devs are becoming as opinionated and knowledgeable about SOTA models (and their coding performance) like we used to be about programming languages and the tips-and-tricks to be more productive with them

Meanwhile we don't really talk about programming languages all that much...

## 2026-07-07 (https://x.com/GergelyOrosz/status/2074443468420604082)

Interesting thing I heard from a founder of an early-stage AI startup in SF:

Hiring is damn hard for them b/c the type of devs that pass the hiring bar for their founding engineer (onsite) role are... the types of devs who also happen to hired by the AI labs in SF or get accepted to YC as well! And so most folks choose those options instead...

## 2026-07-08 (https://x.com/GergelyOrosz/status/2074921870189597149)

"We would never be comfortable to give a 3rd party tool access to our database"

- from a dev at a mid-sized company that built its own coding harness that is used by 70%+ of all PRs

They would not let any vendor run this kind of infra, so they brought it in-house. They are super happy they did this

I sense this will be the norm for companies above the "small" size. Code + data is the IP of a company. Why would you hand it over to a third party?
