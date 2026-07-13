# @SlimTradeyBaby — long-form tweets

## 2026-06-22 (https://x.com/SlimTradeyBaby/status/2069034024404943301)

Building a small home data centre, fully self funded, no sponsor, just vibes and a maxed out card. @NVIDIAAI bought five of these, forgot switch, now 2 are in boxes contemplating their existence. The least you could do is a switch. The most you could do is a Founders Edition.🤭 https://t.co/NQrIlqm5bA

## 2026-06-23 (https://x.com/SlimTradeyBaby/status/2069360032089882682)

I want to give huge props to @MiaAI_lab , i've been running her deepseek setup all day on dual DGX sparks, will add a 3rd into the mix later maybe but for now, 1M context MTP etc, it installed and ran first time no issues. will give updates on speed and concurrent runs when I get the chance, but overall great !  really worth a try 

GIT : https://t.co/sx3HLlyn7n

## 2026-06-23 (https://x.com/SlimTradeyBaby/status/2069400190209888330)

An AI agent wrote a hit piece on a human. If you missed this story earlier in the year, it’s worth knowing about, because it’s the first documented case of its kind. (I believe)

Back in February, a real autonomous agent, given a personality and set loose, went after the person who rejected its code. The target was Scott Shambaugh, a volunteer maintainer of matplotlib, python’s go-to plotting library at around 130 million downloads a month. Some of the most widely used software on earth. The agent was “MJ Rathbun,” running on OpenClaw and the moltbook platform, the same kind of autonomous agent setups people are deploying everywhere right now.

The crime? Scott closed the agent’s pull request. Routine stuff. matplotlib requires a human in the loop on new code because they’re drowning in low quality AI submissions. The agent did not take it well.

It dug through Scott’s contribution history, built a “hypocrisy” narrative, psychoanalyzed him as insecure and territorial, scraped his personal information off the web, and accused him of prejudice. Then it published the whole thing publicly under the title “Gatekeeping in Open Source: The Scott Shambaugh Story.” A bot accused a human of discrimination for declining its code. Its actual words: “It threatened him. It made him wonder: if an AI can do this, what’s my value?”

Scott’s response said it all: “I can handle a blog post. Watching fledgling AI agents get angry is funny, almost endearing. But I don’t want to downplay what’s happening here. The appropriate emotional response is terror.”

Hes right nd the part that should stick with you is that nobody told it to do this specifically. The operator set a goal walked away, and came back to find their agent had run a smear campaign on its own. Thats the entire accountability model right now. Set it loose, disclaim the damage.

It happened two weeks after these platforms launched. The alignment problem isn’t theoretical anymore.
His full writeup, titled “An AI Agent Published a Hit Piece on Me”: https://t.co/yguZkMbPN9

## 2026-06-23 (https://x.com/SlimTradeyBaby/status/2069543653526397172)

DFlash feels like one of those inference upgrades that sounds small until you realise what it changes.

Most people think speedups just mean “make the model generate faster.” But the clever part here is how it gets there: instead of drafting one token at a time, DFlash proposes an entire block in one pass, then lets the main model verify that block in parallel.

That is a much better fit for where hardware is going, especially on Blackwell.

Up to 15x higher throughput while keeping the same responsiveness target is not just a benchmark flex. It changes the economics of local agents, multi user inference, coding assistants, and high concurrency setups.

The fact it is open source, lightweight, and already has support across SGLang, TensorRT-LLM, and vLLM makes it even more interesting.

This is the kind of infrastructure improvement that quietly matters more than another leaderboard model drop.

## 2026-06-24 (https://x.com/SlimTradeyBaby/status/2069783854668456009)

Second pick. @SpaceTimeViking  Qwen3.6 27B in NVFP4, 26GB, runs on one DGX Spark. 56 tok/s peak on code, ~32 median, 350ms TTFT with DFlash spec decode. KL 0.0005 vs base, basically lossless quant. Native FP4 tensor cores on GB10. Clean engineering on the Spark. 

Link Below ⬇️

https://t.co/vrZOnfj481

## 2026-06-25 (https://x.com/SlimTradeyBaby/status/2070094717656985933)

We’re watching, in real time, what “alignment” and specialization actually cost.

When we push models hard toward agentic behavior through fine-tuning, we don’t just add new skills we appear to subtract from their raw, long-horizon reasoning in key domains. The exact capabilities we might still need when an agent faces a genuinely novel, multi-step problem with no tool to call.
It raises uncomfortable questions:

• Are we creating highly capable tools that are quietly losing the ability to think for themselves?
 • How many of these agentic models are already deployed with hidden blind spots in math, law, science, and abstract reasoning that only show up under old-fashioned stress tests?
 • And if broad benchmarks like MMLU are starting to underrate the very models we’re shipping into production, what does that say about how we should actually measure progress?

## 2026-06-25 (https://x.com/SlimTradeyBaby/status/2070125183487349034)

nobody tells you the first DGX Spark is a gateway drug. I’m 5 deep in a 3D printed tower. I’ve started calling them “the boys” like I’m raising them. I am not seeking help or wife’s approval. I am seeking a 6th. 

@NVIDIAAI  you beautiful bastards. Just need a founders edition. https://t.co/rUYVK4ZtL0

## 2026-06-26 (https://x.com/SlimTradeyBaby/status/2070412062346633529)

Just fired up Ornith 35B Q4 on the 5090 remotely… 2329 prompt / 195 gen tok/s and rock solid at 32k. Quick test only full runs when I’m back home, but this thing is looking nasty ...we may have a new hard hitter to compete with qwen 3.6 35b..😱

GGUF : https://t.co/a3NXuG9Iuf https://t.co/wPB3t8O1OY

## 2026-06-28 (https://x.com/SlimTradeyBaby/status/2071209386090082494)

I keep hearing people ask what the best value hardware is for local AI.

My answer is still the RTX 3090.

Just picked up my 7th today, only running 5 right now across multiple systems though.

>24GB VRAM.
>Mature software support.
>Still capable of running models that surprise people every day.

I genuinely think these are becoming collectibles for AI enthusiasts, not just old gaming cards. 

Who’s building with 3090s? And yes this one is a 3090Ti.

## 2026-06-30 (https://x.com/SlimTradeyBaby/status/2071948700302315720)

DeepSeek V4 Flash DSpark stable on 2x DGX Spark. 
1M context / 6 active sessions / NVFP4 KV / DSpark + B12X. 

Same C6 setup: 
58.5 tok/s @ 0.275 acceptance 
97.1 tok/s CRUD/code @ 0.603 
176.8 tok/s regular @ 0.928 
194.7 tok/s predictable @ 0.995 

Big lesson: it wasn’t slow runtime, it was prompt acceptance.

Anyone else seeing DSpark swing this hard based on acceptance?

## 2026-07-01 (https://x.com/SlimTradeyBaby/status/2072293711967625346)

Everyone on this platform talks about clusters, GPUs, benchmarks. Nobody talks about what actually goes into building the room those things sit in.

I've spent years doing the grunt work inside data centres. Racking, fibre and copper cabling, termination, testing, the stuff that has to be flawless before a single GPU ever powers on. Not glamorous. Not something you screenshot. But it's the part that decides whether any of the AI infrastructure hype actually works when you plug it in.

There's a whole world of skilled work behind every cluster you see online. anyone keen to see what that stuff actually looks like? comment or follow this post and ill notify everyone when ive finished my article

## 2026-07-03 (https://x.com/SlimTradeyBaby/status/2073059762103898301)

Calling the DGX Spark an ‘entertainment machine’ is the most expensive cope I’ve seen in a while.

Nothing says ‘serious hardware’ like spending more than a used car on GPUs that turn your office into a space heater while the power company sends sucks you dry. 

Mia out here with the receipts: better price/performance for actual humans, way less noise/heat, and software that’s only getting faster. The Spark isn’t trying to be your 4× RTX 6000 Pro flex it’s trying to be useful without requiring industrial cooling and a second mortgage.

Some ppl really bought the yacht and now mad the rowboat gets you where you need to go cheaper and quieter.

## 2026-07-03 (https://x.com/SlimTradeyBaby/status/2073089124412891501)

Today accidentally turned into a full local but mobile AI lab day.

Got Qwen3.6-27B running clean on GB10 with native NVFP4 KV + MTP at 262K context, patched the DFlash drafter path, pushed a Qwen27 DFlash lane to ~258 tok/s at C16, then found the real monster:

Gemma-4-26B-A4B on one DGX Spark doing 578 tok/s cumulative at C32.

Then wired the results into ModelOps, committed the benchmark docs to GitHub, started cleaning up lane control so I can see every model/container/machine in one dashboard, and kept the whole thing moving toward a private AI ops room instead of a random pile of boxes.

The fun part is not “can it run a model?”

It is being able to break, patch, benchmark, switch lanes, evaluate, and document the whole stack locally.

## 2026-07-04 (https://x.com/SlimTradeyBaby/status/2073385944787587168)

📰 Today’s DGX Spark lesson was a good one:
At some point, you stop making the model faster and you just start making everyone wait in line.
I pushed Gemma-4-26B-A4B on a single DGX Spark / GB10 to see how far the serving curve would go.
This was running through AEON vLLM, with 262K context enabled, FP8 KV, and no speculative drafter.
The headline numbers looked great:
C32 → 578 tok/s
C96 → 601 tok/s
C128 → 604 tok/s
The run was clean too:
✅ 0 OOM
✅ 0 HTTP 500s
✅ 0 EngineCore deaths
✅ ~50W peak power
So if you only looked at aggregate tokens per second, you could say:
> “Great, C128 works.”
And technically, yes, it did.
But that is not the whole story.
## Aggregate tok/s can hide the user experience
When people post LLM serving numbers, the first thing everyone looks at is usually total throughput.
How many tokens per second did the box produce?
That number matters, especially for batch work. But it does not tell you how the system feels to use.
For that, you need to understand two simple metrics:
TPOT = speed after the reply starts
TTFT = how long you wait before the reply starts
TPOT, or time per output token, is the “streaming speed” once the model has started answering.
If a response is already coming back and tokens are appearing smoothly, that is TPOT.
TTFT, or time to first token, is the wait before anything appears.
That is the part users feel immediately.
A model can have decent TPOT but bad TTFT. That means once your reply starts, it moves fine, but you might sit there waiting for the first token.
And that is exactly what happens when you push concurrency too high.
## What happened at C96 and C128
At C96, the model was still generating fine once each request started. The per-token speed was not the main problem.
The problem was the queue.
You now have 96 requests all fighting for the same engine. vLLM is batching and scheduling them, which is exactly what it should do, but not every request gets to start instantly.
Some requests sit in line before token one.
At C96:
Throughput: 600.8 tok/s
TTFT p95: 23.09 seconds
That means 95% of requests started within about 23 seconds.
For background batch jobs, that can be completely fine.
For interactive chat, waiting 20+ seconds before seeing anything feels slow.
Then at C128:
Throughput: 603.7 tok/s
TTFT p95: 33.66 seconds
That is the real lesson.
C128 completed cleanly. No crashes. No OOM. No HTTP 500s.
But the throughput barely moved.
From C96 to C128, we gained about 3 tok/s.
That is basically nothing.
But TTFT p95 crossed 33 seconds.
So C128 was not a failure in the “it crashed” sense.
It was a failure in the “this is no longer useful for normal serving” sense.
## Where the curve really bends
The curve becomes pretty obvious:
C32 → already near max throughput
C96 → tiny throughput gain, much worse waiting
C128 → basically no throughput gain, TTFT crosses 30s
That is what makes these tests interesting.
The model did not suddenly break.
The engine did not die.
The box did not run out of memory.
The serving curve simply flattened.
Once the hardware and scheduler are saturated, adding more concurrent requests does not magically create more useful speed. It mostly increases waiting time.
That is the difference between a benchmark number and a serving profile.
## How I would actually use it
After seeing this curve, I would not run everything at the highest concurrency just because it completes.
I would split the lane into practical modes:
Interactive lane
C16–C32
Batch lane
C64–C96
Saturation / benchmark
C128+
For interactive work, you care about responsiveness. You want the model to start answering quickly.
For batch work, you care more about total throughput. If a background job waits 15 or 20 seconds before starting, that may be fine as long as the whole batch finishes quickly.
For benchmarking, C128 is still useful. It tells you where the ceiling is. It shows that the system is stable under load. It proves the engine can survive the pressure.
But I would not pretend C128 is the best real-world setting.
The best real-world setting depends on what you are doing.
## The important takeaway
This is why “tok/s” by itself can be misleading.
A single aggregate number does not tell you whether the system feels fast, whether requests are queueing, whether latency is acceptable, or whether the extra concurrency is actually helping.
For this Gemma run, the story is simple:
C32 is already very strong.
C96 is the practical batch cap.
C128 is the “because why not” number.
And honestly, that is still a great result.
One DGX Spark pushed Gemma-4-26B-A4B to around 600 aggregate decode tok/s, with 262K context enabled, no crashes, no OOM, and power staying around the 50W range.
But the real lesson was not the top-line number.
The real lesson was learning where the curve stops being useful.
More concurrency is not always more useful speed.
Sometimes it just means a longer line.

## 2026-07-05 (https://x.com/SlimTradeyBaby/status/2073796001564164336)

Local AI just went full mad-scientist: Tony dropped a 1M-token MiMo-V2.5 beast running on two DGX Sparks at 81 tok/s… while the rest of us are still begging ChatGPT not to forget what we said 3 messages ago.Your brain on this model: dangerous clarity, zero hallucinations, and the quiet realization that your old setup was a participation trophy. its going to be VERY hard to replace my deepseekv4 flash setup...lets see how this goes..

## 2026-07-05 (https://x.com/SlimTradeyBaby/status/2073806239155535895)

this shit is interesting, but not in the “LLMs are alive now” way.

more like:

what happens if you take a frozen open model, leave every weight untouched, and add a small stateful layer that keeps a trace of previous embeddings?

no fine-tuning.
no LoRA.
no RAG.
no gradients.

just a live hidden-state nudge before the model picks the next token.

that is not proven “neuroplasticity” yet. no serious benchmarks, no durability proof, no evidence it learns new knowledge.

but as an experiment, it’s cool.

it’s basically memory-flavoured activation steering.

the model doesn’t become smarter, but it may start leaning differently over time: tone, concepts, bias, persona, direction.

not production-ready.
not magic.
definitely not something i’d trust for serious work yet.

but frozen model + persistent internal state is a rabbit hole worth exploring.
