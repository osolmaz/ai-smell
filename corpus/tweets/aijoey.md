# @aijoey — long-form tweets

## 2026-05-15 (https://x.com/aijoey/status/2055194286786859278)

quiet morning on the dgx spark.

laguna is loading.

container:
lmsysorg/sglang:dev-cu13-laguna-xs2

model:
poolside/Laguna-XS.2-NVFP4

runtime:
SGLang on localhost:30000

the machine saw Blackwell and chose its path:
fp4 gemm through flashinfer cudnn

then the model found its own shape:
CompressedTensorsW4A4Nvfp4MoE

no ceremony.
no benchmark yet.
just the sound of the stack settling into place.

first, the weights load.
then, the tokens.
then, we see what is true.

## 2026-05-15 (https://x.com/aijoey/status/2055226538979680412)

tested Poolside Laguna XS.2-NVFP4 on NVIDIA DGX Spark / GB10.

the docs were right to be cautious.

Poolside’s HF card says the NVFP4 checkpoint uses FP8 KV cache, and warns that FP8 KV can scramble output on non-Hopper GPUs. they suggest disabling the FP8 KV layers and using Marlin.

that matched what i saw locally.

the native / FlashInfer style FP4 paths looked promising at first, but on GB10 i kept getting bad or empty output.

best correct setup i could verify so far:

- hardware: NVIDIA DGX Spark / GB10
- model: Poolside Laguna XS.2-NVFP4
- runtime: vLLM
- path: Marlin
- CUDA graphs: on

not calling this a zero loss native FP4 setup yet.

just the best working path i could actually verify locally.

## 2026-06-03 (https://x.com/aijoey/status/2062133122125201701)

real world run with @NVIDIAAI Cosmos 3

    Ran every frame of a 15s highway clip (450 frames @ 30fps) through LocateAnything-3B on DGX Spark:

    - 450 frames × 14,105 boxes — every frame, real detections
    - 5.2s/frame avg (vs 12.7 BPS on H100) — GB10 holds its own
    - 7.8 GB VRAM — fits with room to spare on 128GB unified
    - IoU tracking + lane assignment — real trajectories, not synthetic 

cc: @PavloMolchanov

## 2026-06-17 (https://x.com/aijoey/status/2067313374375911689)

been testing MiniCPM-V 4.6 locally on my DGX Spark

this demo is an industrial gauge reader

i generated a synthetic control panel with a pressure gauge, temperature gauge, flow display, and tank level bar. because the panel is synthetic, i know the exact ground truth at every frame.

MiniCPM gets a frame and has to return structured JSON:
pressure_bar
temp_c
flow_lpm
level_pct

then i score each reading live:
pass = within 5% of full scale
drift = within 10%
miss = outside that

the scenario i was targeting is industrial visual ops. lots of real systems still have gauges, panels, status screens, meters, and legacy interfaces. i wanted to see if a small open source vision model could read that kind of interface and return values another system could actually use.

what i saw in practice: digital displays and tank level were easier. analog gauges were harder, especially between tick marks or while moving.

but the important part is that the output is measurable. it is not just a captioning demo. MiniCPM-V 4.6 had to read pixels, follow a schema, and produce structured data i could check against ground truth.

## 2026-06-19 (https://x.com/aijoey/status/2067923063086129476)

been deep in a weird little mac mini plus dgx spark workflow tonight.

codex app is running on the mac, but when i need vision inference i have it ssh into the spark, spin up vllm over there, and hit it from the mac like a local openai endpoint.

mac mini handles the workbench.
dgx spark handles the heavy inference.
ssh is the cable between them.

this is the part of local ai that feels underrated to me.

not everything has to run on the machine in front of you. the real setup is making all your machines feel like one machine.

## 2026-06-20 (https://x.com/aijoey/status/2068212734181724199)

Built a back-office agent swarm demo with MiniCPM5-1B.

128 concurrent agents on DGX Spark, served through vLLM continuous batching.

Each agent handled a different business ops queue:

invoice review
refund routing
compliance checks
HR/payroll issues
legal triage
IT security alerts
sales ops
logistics recovery
MiniCPM5-1B streamed 6,604 chunks across 128 agents in 1.48s.
The takeaway:
The value of 1B models is not just “can it answer well?”
It is:
“How many useful business decisions can it make at once?”
Not one giant agent doing everything slowly.
A swarm of tiny, cheap workers clearing practical queues in parallel.

cc: @OpenBMB @NVIDIAAI

## 2026-06-22 (https://x.com/aijoey/status/2069120682638651848)

today’s testing log:

step-3.7-flash-nvfp4 on the dgx spark.

this one got put on my radar by @sudoingX and @mr_r0b0t, so now i’m curious.

i want to see how it feels locally, how fast it moves, and if it earns a spot in my spark stack.

just me testing models, breaking stuff, and figuring out what’s actually useful.
cc: @StepFun_ai 
https://t.co/I5iXbadmnF

## 2026-06-26 (https://x.com/aijoey/status/2070348392257995172)

alright, ornith-1.0-35b is going on the dgx spark tonight.

i keep seeing people talk about this one, so i’m curious now.

supposedly it’s putting up crazy numbers for a 35b moe, and r/localllama is already making noise about it.

benchmarks are cool, but i want to see the part that actually matters:

does it feel good to use locally?
does it code well?
does it earn a spot in my stack?
we’ll find out.

## 2026-06-27 (https://x.com/aijoey/status/2070897563935391854)

we made it to the cluster. super cool!

i did have a hiccup. the gx10 choked during update via headless setup to local ui. i had to reboot it , i did have the other prerequisites setup so i just connected via nvidia sync and clicked on dashboard to updated from there. https://t.co/atV8mHZl1O

## 2026-06-30 (https://x.com/aijoey/status/2071966404006285560)

Ever seen Bruce’s Cylinder?

It’s a kinetic depth illusion: a bunch of flat moving dots on a screen suddenly look like a transparent 3D cylinder rotating in space. Your brain reconstructs depth from motion alone, even though there’s no actual 3D object there.

The fun part is that the rotation can feel ambiguous. If the depth cues are weak enough, your perception may flip which side is “front,” making the cylinder seem like it changes direction.

cc: codex

## 2026-07-01 (https://x.com/aijoey/status/2072154825563816335)

Agents can book meetings, write code, and answer questions.

But they can’t safely run real business operations until they can prove who they are, what they’re allowed to buy, and how much they’re allowed to spend.

So I built Trusted Agent Procurement for the Hermes Agent Accelerated Business Hackathon by @NVIDIAAI × @stripe × @NousResearch.

The demo uses GPU procurement as the example: an autonomous buyer agent verifies identity, proves spend authority, negotiates capacity, triggers a Stripe-style payment, receives provisioning, and leaves a full audit trail.

The pattern generalizes to SaaS seats, cloud credits, data purchases, vendor onboarding, and service contracts.

Repo: https://t.co/3FpPhfkPWW

## 2026-07-01 (https://x.com/aijoey/status/2072378410156884058)

Big thank you to @openhome for allowing me to be one of the first people to have this dev kit. 

First order of business is getting Hermes connected. 

Now less than 5min minutes checking out the openhome dashboard, I caught a loop with the agent personality Leonardo Da Vinci from the dash to my openhome device and they started to talk. I left them talking for like 15min. Was pretty damn cool hearing their thoughts. The video gives you a preview of the conversation.

## 2026-07-02 (https://x.com/aijoey/status/2072489639584129387)

tonight’s testing log: qwen3.6 27b nvfp4 on 1 dgx spark.

nvfp4 is a big deal for the dgx and soon to be rtx spark community because memory bandwidth is the wall everyone keeps running into.

the whole point is simple:

smaller precision, less memory pressure, better efficiency, and a real shot at running larger models on compact desktop hardware without turning the whole setup into a science project.

this is why these nvidia optimized checkpoints matter.

not just because they fit.

because they actually make local ai feel usable.

## 2026-07-02 (https://x.com/aijoey/status/2072626787654172983)

yeah this is where it starts getting fun.

this morning’s journey log:

getting hermes running with mixture of agents across 2 dgx sparks.

one spark gets qwen.

one spark gets nemotron.

then hermes sits in the middle and uses both instead of me depending on one model to handle everything.

that’s the part i’m testing this morning

two boxes on my desk, a bunch of local models, and me trying to see how far i can push this thing.

local ai is starting to feel less like “run one model” and more like building your own little team of brains.

## 2026-07-02 (https://x.com/aijoey/status/2072663235451388369)

Been setting up Hermes MoA to run fully local across two DGX Sparks. 
No OpenRouter, no hosted model calls.

One Spark runs the acting/aggregator model, the second runs a reference model, and Hermes combines them through MoA
while still keeping the normal agent loop + tools.

The useful part: it’s not hardcoded to my models. The repo lets you point Hermes at whatever local OpenAI-compatible endpoints you already run: vLLM, llama.cpp, Ollama, LM Studio, SGLang, etc.

/learn
https://t.co/xoXcLum9FB

Basically:
local models -> router -> Hermes custom provider -> MoA

Still early, but the goal is simple: make private multi-model agent workflows easier for people with local hardware.
cc: @NousResearch @NVIDIAAI @Alibaba_Qwen

## 2026-07-02 (https://x.com/aijoey/status/2072663237393309864)

Left: Qwen 3.6 27B argues for humanoid robots
Right: Nemotron 30B argues for task-specific designs
Then Qwen reads both arguments and delivers the verdict.

Everything running locally via Hermes Agent's Mixture of Agents feature.

Prompt: Debate whether humanoid form factor is the right bet for general-purpose robots, or if task-specific morphologies win. Agents argue opposing sides, aggregator delivers a verdict with the strongest evidence from each

## 2026-07-04 (https://x.com/aijoey/status/2073281743537254909)

if you're not using Hermes desktop yet, you're missing out on something special. i was only using cli because of my headless sparks.

i have it on my mac mini, from there i can also ssh into my dgx sparks via nsync. think about how you use codex app , and bring that mindset over. very powerful use cases when you have multiple devices on your network all being captured in a thread here. 

nothing comes this close on how you can easily add your api's. too smooth!!

just my late night thoughts as im hacking away here.

## 2026-07-04 (https://x.com/aijoey/status/2073459564473668083)

been on a weird arc the last few months and figured i'd write it down before i forget.

started with hermes-hud. just wanted to see what the agents on my machine were actually doing. terminal only, no server spin up.

then i bought a dgx spark at microcenter and everything got louder.

late nights turned into benchmarks. gemma 4 31b with mtp on gb10. 1.65x to 1.74x tok/s. hermes agent did most of the legwork. i ran the whole thing from telegram like a psycho.

4 weeks in i had one model locally. a month later it was 19 models and 665gb of weights sitting on disk. no cs degree. no bootcamp. just breaking things until the numbers made sense.

shipped spark-doctor because i was tired of guessing how the spark was doing. power caps, unified memory pressure, docker health, vllm/ollama setups. built it for other new spark owners figuring it out the hard way.

this week i stacked a second spark on my desk. qwen on one box. nemotron on the other. hermes in the middle running mixture of agents instead of me praying one model can do everything.

local ai stopped feeling like "run one model" and started feeling like building a little team of brains on your desk.

still breaking things. still learning the machine. that's the whole point.

## 2026-07-05 (https://x.com/aijoey/status/2073824819565453393)

now running @ToNYD2WiLD MiMo-V2.5 + DFlash Speculative Decoding + FP8 KV on 2x DGX Spark

my 2nd prompt was "pick one of your specialties on the creative work strengths and create something to impress me. lets see what it does.

ps: im using Hermes agent desktop on my Mac mini https://t.co/v65yM3R4IV

## 2026-07-06 (https://x.com/aijoey/status/2074136566667043186)

bigger models are only half the story.

the real unlock is making those models actually run fast, fit in memory, and deploy cleanly on real hardware.

nvidia model optimizer 0.45.0 is one of those updates that matters because it pushes more of the stack toward efficient inference.

nvfp4, mxfp4 to nvfp4 conversion, active moe cost accounting.

not flashy on the surface, but this is the kind of tooling that makes local AI and compact NVIDIA systems way more practical.

## 2026-07-06 (https://x.com/aijoey/status/2074254220392362155)

today's rabbit hole: squeezing a 295b-parameter moe (hunyuan hy3, nvfp4) out of two dgx sparks over 200gbe roce.

what i learned the hard way:

• tp=2 beats pp=2 for single-stream (14.5 vs 12 tok/s)

• jumbo frames: free but no decode gain, tiny all reduces are latency bound

• fastsafetensors ooms 128gb unified memory (pinned staging doubles the weights)

• mtp speculative decode works after patching vllm's draft layer for nvfp4… and is still slower across 2 nodes. the interconnect taxes the draft pass more than the acceptance rate pays back.

landed at 14.5 tok/s single stream, 31 tok/s aggregate. video: 4 concurrent prompts, live, unedited, 1×. 295b params in my house, no cloud.

this is where I stop for now until we get more support. 

cc: @TencentHunyuan @NVIDIAAI

## 2026-07-07 (https://x.com/aijoey/status/2074459412530438198)

i got tencent’s 295b hy3 running 100% locally on two nvidia dgx sparks, then open sourced the whole setup.

not just scripts. every benchmark, every failed config and why it failed, two vllm bug fixes, plus an agents.md your ai agent can read to operate the cluster itself.

27 tok/s
256k context
100% local
p.s. yesterday I spent all day with this model 

cc: @TencentHunyuan 
cc: @NVIDIAAI 
https://t.co/zGdLGgwOeF

## 2026-07-07 (https://x.com/aijoey/status/2074599367667802239)

nvidia ai just handed dgx spark owners a real gift.

nemotron labs 3 puzzle 75b a9b nvfp4 is basically built for this box.

75b total, 9.3b active, nvfp4, mamba plus moe, 256k context in the config, and it actually fits on one spark with room to breathe.

on one spark, nvfp4 is the obvious move.

on two sparks, you get options. keep nvfp4 and push longer context / local agents harder, or test fp8 if you want to trade memory for precision.

## 2026-07-08 (https://x.com/aijoey/status/2074997941660463106)

1 DGX Spark · Nemotron Puzzle 75B NVFP4 · Grok 4.5 audit

BEFORE
• 1× GB10, MTP×3, solid solo decode (~38–42 tok/s)
• max_num_seqs=1 → 4 “parallel” requests = 1 at a time
• 4-stream aggregate ≈ one stream (~40 tok/s) · the rest queued

AFTER (same model, same Spark, config only)
• max_num_seqs=4 · prefix cache on · batched tokens 8192 · GMU 0.88
• Solo still ~36–40 tok/s (decode was already fine)
• 4 live streams at once → ~75 tok/s aggregate

Video = real wall-clock @ 30 fps, no speedup. Local vLLM.

cc: @nvidia , @SpaceXAI @grok 

no resistance for inference engineering

## 2026-07-09 (https://x.com/aijoey/status/2075038411400831473)

A/B on 2× DGX Spark, prod untouched.

NVIDIA Nemotron Labs Puzzle 75B-A9B NVFP4
Same flags both nodes: 1× GB10, MTP×3, prefix cache, max_num_seqs=4

Spark 1 (Hermes prod): vLLM 0.22.1 (NGC)
Spark 2 (idle peer):   vLLM 0.23.1rc1 Spark build

Warm results:
• Solo mean: 37.7 → 39.9 tok/s (+6%)
• 4-stream aggregate: 135 → 142 tok/s (+5%)
• Structured 43→46 · Code 38→42 · Prose ~31 flat

Newer vLLM works. Small win. Not cutting over prod yet.

Recipe: https://t.co/mC8tIuqy1o

cc: @NVIDIAAI @grok @SpaceXAI

## 2026-07-10 (https://x.com/aijoey/status/2075403131010388330)

Here’s NVIDIA ARDY running locally on a DGX Spark. It generates Unitree G1 compatible humanoid motion from natural language input, then plays the result in a virtual viewer. The video shows the generated motion in action. No physical robot here, just the model and a simulated G1 body.

## 2026-07-10 (https://x.com/aijoey/status/2075410618010497312)

MiniMax just closed a $2B funding round              
                                                           
But the wildest part? Their CEO committed 1% of company   
equity to the open source community.                      
                                                           
Most AI labs treat OSS like a marketing exercise. These guys are actually putting real money behind it. 

Congrats @RyanLeeMiniMax @MiniMax_AI

## 2026-07-10 (https://x.com/aijoey/status/2075664955312165026)

I got the channel setup. I'm warning you. I'm very organic lol. nothing will be professional. im not doing any fancy editing and stuff. i really just want to share whats new and what im using in ai and tech.

link: https://t.co/DDeLa9vPjI

i just had an hr long live session on tiktok with @OnlyTerp  
and i was told it was very natural as if we were talking over coffee. i like that.

## 2026-07-12 (https://x.com/aijoey/status/2076135592748782016)

the hard part of running local ai isn’t loading one model.

it’s what happens after you add the second, third, or fourth gpu box.

different endpoints. different dashboards. ssh sessions everywhere. no simple way to see what’s healthy, what’s running, or where the traffic is going.

so i’ve been building honeycomb.

one openai compatible endpoint for the entire fleet, with a live map that shows every machine, routes requests, tracks performance, and lets me control everything from my mac, ipad, or phone.

still early, but the home lab is starting to feel like a real ai fleet.

more soon. 🍯
