# @analogalok — long-form tweets

## 2026-06-08 (https://x.com/analogalok/status/2064002947680485858)

Run Gemma 4 26b MTP on 8 GB VRAM GPUs at 25+ tokens/second. Flags included!

local llm space is moving at terminal velocity.   only 3 days ago google released gemma 4 26b a4b qat quants. more efficient than before, ran on 8gb vram at 20 tok/sec.  

and now just a few hours ago, mainline llama.cpp merged a massive update and we just shattered our own record. decode throughput went 25-40% up on the same 8 GB VRAM setup!

Before MTP: 20 tps    ->   After MTP: 28 tps!

llama.cpp just officially merged PR #23398 ("add Gemma4 MTP"), bringing native Multi-Token Prediction (MTP) support to Gemma 4 models.

By running speculative drafting on the same 8GB VRAM RTX 4060 setup, my decode throughput on a 64k context instantly leaped to a blistering 25–27 tokens/sec thats 25-30% increase with the same hardware.

Here is the architectural catch you need to know:  Unlike the Qwen 3.5 and 3.6 series, which bake the MTP heads directly into the base GGUF, the Gemma 4 MTP head is not built in.  

You must download a separate, specialized MTP drafter GGUF (the assistant model) to act as the speculator. (I've dropped the download link in the replies).

copy and try the exact flags:

-m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf --spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.7 --spec-draft-model gemma-4-26b-A4B-it-assistant-Q4_0.gguf -c 64000 -v

n-max 4 and p-min 0.7 is also worth checking out. benchmark on your setup and workflow.

if you have a single 8 gb vram nvidia rtx 4060, 3060, 3070, 2080, 2070, grab the MTP drafter GGUF link in the comments and try it yourself.

Check it out even if you have asmaller or a larger gpu, such as a single rtx 3090, 4090, 3060, 2060.

MTP works for all gemma 4 sizes such as gemma 4 12b, gemma 4 31b etc. but remember to grab the correct mtp draft assistant models respectively.

what are you benchmarking today

## 2026-06-12 (https://x.com/analogalok/status/2065395762436129245)

You don't even need a laptop to learn local llms!

I just ran Unsloth Gemma 4 E2B QAT Multi Token Prediction (MTP) - 12 tokens/sec on a 6 years old phone's cpu with llama.cpp and termux!

Unsloth just dropped MTP draft assistant GGUFs for every Gemma 4 model. naturally I yolo'd it straight onto Android to see what happens.

not the 2 bit quant. UD-Q4_K_XL. works on any phone with ≥8 GB RAM.

# Device: Note 20 Ultra (6 years old)

-without MTP -> 7-9 tok/s
-with MTP        -> 9-12 tok/s

~20-30% faster on a phone. free speedup. I'll take it.

# copy the command:

LD_LIBRARY_PATH=. ./llama-server \
  -m ~/storage/shared/llm/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf \
  --spec-type draft-mtp \
  --spec-draft-model ~/storage/shared/llm/mtp-gemma-4-E2B-it.gguf \
  --spec-draft-n-max 4 \
  --spec-draft-p-min 0.6 \
  -c 4096 -t 4 --port 8080 --no-mmap -v

beginner friendly Termux guide to run ggufs with llama.cpp on android + HuggingFace model link in the comments. no excuses.

## 2026-06-14 (https://x.com/analogalok/status/2066277768732778983)

This is the most hilarious thing I saw and did today 

Ran gemma-4-12B-coder-fable5-composer2.5-v1-GGUF locally with 8 GB VRAM at 20+ tok/sec

Anthropic's Claude Fable 5 launched June 9.

By June 12 it was banned. I can't access it. You can't either.

But here's the twist: I'm running a model trained on its chain of thought at 20 tok/s on my RTX 4060 8GB.

Locally. Offline. No cloud. No export control.

Enter: Gemma4-12B-Coder GGUF (Q4_K_M)

Base: Google's gemma-4-12B-it

Fine-tuned on verifiable Python CoT data:

- Primary: Composer 2.5 real reasoning traces (only passing solutions kept)
- Auxiliary: Fable 5 used to redo the hard cases Composer missed.

Every training example's reasoning led to code that actually ran. No hallucinated logic.

Llama.cpp flags: 
-m gemma4-coding-Q4_K_M.gguf -cnv  -ngl 44 -c 64000 -v
(huggingface model link in comments) 

Flag breakdown:
 -ngl 44 → offload 44 layers to GPU (tune this for your VRAM)
 -c 64000 → 64K context window
 -cnv → conversation/chat mode
 -v → verbose output

The irony writes itself.

Anthropic spent weeks telling the world Fable 5 (mythos) is too powerful to release. Then released it. Then got banned from serving it, including their own researchers.

Meanwhile: a Gemma 4 12B fine tune, trained on Fable 5's reasoning, runs fully offline on my mid range consumer GPU 

No API. No cloud. Just me and llama.cpp.

This is why local AI matters.

Check out the model's link in the comments. How's your experience been with this model?

## 2026-06-15 (https://x.com/analogalok/status/2066605203093442583)

that nvidia 1080 (or any 8gb vram card) collecting dust in your drawer?
pull it out.

right now.

- run Unsloth Gemma 4 12B QAT MTP (dense) Q4_K_M → 15+ tokens/sec

- run Unsloth Gemma 4 26B QAT MTP (MoE) Q4_K_M → 15+ tokens/sec

these quants by google and unsloth are optimized for delivering maximum intelligence while being memory efficient. achieve high throughput with Multi Token Prediction support.

(model's huggingface links in the comments)

rtx 1080 8GB VRAM. $100 on eBay. a GPU from 2016.

a dual 1080 16 GB VRAM setup would just cost $200, letting you to run even larger models.

i'm running a full hermes agent on a single Nvidia RTX 4060, 8GB VRAM, 64k context, zero KV cache quantization. no compromise. vision + reasoning. (check out the comments for video)

people are paying for API access to intelligence that your old gaming GPU can run locally, privately, for free, right now.

and here's the part that should genuinely excite you:
this is the FLOOR. not the ceiling.

every model drop, your hardware gets smarter. same GPU. same VRAM. more capability. the intelligence comes to you.

if you have a single GTX 1070, GTX 1070 Ti, GTX 1080, RTX 2060 Super, RTX 2070, RTX 2070 Super, RTX 3060 Ti, RTX 3070, RTX 3070 Ti, RTX 4060, RTX 4060 Ti, RTX 5050, RTX 5060, RTX 5060 Ti or any 8 GB VRAM GPU

this is for you. you are not behind. you are early.

llama.cpp / ollama / lm studio. pick one. 30 minutes. 

you're running local AI that would've seemed impossible 6 months ago.

## 2026-06-16 (https://x.com/analogalok/status/2067023350866796962)

my 8 GB VRAM gaming laptop is absolutely going to hate me for this. but I still did it. 

ran a 31b dense model (Gemma 4 31b Q4) with only 8 GB VRAM 

last week I ran Gemma 4 26B A4B  a mixture of experts model on my RTX 4060 and hit 25–28 tokens/sec using llama.cpp's new MTP support. smooth. snappy. 

but MoE has a secret: it only activates 4B parameters per token despite having 26B total. that's why it flies.

so the real question started haunting me. what if I throw a full, no tricks, every parameter fires on every token, 31B DENSE model at the same machine?

# Hardware:
GPU: NVIDIA RTX 4060, 8 GB VRAM
RAM: 16 GB
CPU: Intel Core i7 H
Laptop. Gaming. Modest.

The model: gemma-4-31B-it-qat-UD-Q4_K_XL.gguf
(model's unsloth huggingface link in the comments)

This is Google DeepMind's flagship dense model in the Gemma 4 family that can run on single consumer GPU. It packs a hybrid attention architecture, supports up to 256K context natively, and is QAT (Quantization Aware Training) optimized, meaning it retains far more quality than standard post training quants at the same bit depth. This is NOT the MoE. This is 31 BILLION dense parameters, every single one of them loaded.

# the flags I used:

 -m gemma-4-31B-it-qat-UD-Q4_K_XL.gguf -cnv --spec-type draft-mtp --spec-draft-model mtp-gemma-4-31B-it.gguf --spec-draft-n-max 8 --spec-draft-p-min 0.6 -c 6000 -v

Multi Token Prediction (MTP) is still active here. Separate draft GGUF required, same as the 26B setup.

# Results:
→ Decode: ~3 tokens/sec
→ Prefill: ~2 tokens/sec
→ Context: 6000 tokens
→ Hardware crying quietly in the corner: yes

so is 3 tps actually usable?
For real time back and forth chat? Not ideal. You're not having a fluid conversation at 3 tps.

but slow ≠ useless. And this is where it gets genuinely interesting.

think about how senior devs actually work in a real team. But when something is architectural, deeply complex, or needs serious reasoning? they walk down the hall and escalate to the senior.

That's exactly the local AI agent architecture this unlocks:

→ Fast orchestrator model (Gemma 4 26B MoE at 25+ tps) handles routing, simple queries, tool calls, memory. The junior dev.

→ Gemma 4 31B dense is the senior, called only when the fast model genuinely hits a wall. Hard multi step reasoning. Complex code generation. Deep architectural decisions. The agentic loop stays fast. Only the hard hops touch the 31B. That's a legitimate production grade local AI architecture on a budget hardware. (requires 2 8gb gpus)

other workflows where 3 tps is completely fine:

- overnight batch jobs. summarize documents, extract structured data, review code. Fire it off. Sleep. wake up to results.
- One shot deep reasoning
- Silent code audit loops, you write and test, the 31B reviews diffs and flags issues in the background between your sprints
- Any workflow where output quality > output speed 

A few weeks ago, nobody was running a 30B+ dense model on a single consumer GPU with 8 GB VRAM. At all. Now we're doing it on an Intel i7-H gaming laptop with a NVIDIA RTX 4060, thanks to llama.cpp + QAT quants + MTP speculative drafting.

Google DeepMind said the Gemma 4 31B targets "consumer GPUs and workstations." They were not exaggerating. The hardware bar to run serious frontier class models locally keeps dropping.

the tools are here. the models are here. you just have to be willing to abuse your laptop a little.

what workflows would you actually run on a local 3 tps 31B dense model? genuinely curious. drop it below.

## 2026-06-17 (https://x.com/analogalok/status/2067338763811070210)

Google's Gemma 4 26B A4B QAT hits 25+ tokens/sec and 320+ tokens/sec prefill on 8 GB VRAM (RTX 4060) + 16 GB RAM using TurboQuant

Prefill just went from 200 → 320+ tok/s on the same 8GB card. 1.6x, no new hardware, no new quant, just a KV cache trick stacked on top of the Gemma 4 26B MoE setup from a few days ago.

A few days ago I posted Gemma 4 26B A4B hitting 28 tok/s decode on 8GB VRAM using native MTP. prefill was stuck around 200 tok/s. fair callout by the community.

So today I tested something I'd already been meaning to try: 

TheTom/llama-cpp-turboquant, the TurboQuant KV cache fork by Tom Turney (@no_stp_on_snek). 
(github link in the comments) 

thanks to him, the fork just got resynced to mainline, so MTP + TurboQuant now run together cleanly (I didnt see any meaningful gains by using MTP with this setup though but you can try).

The flags (No MTP):

-m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf -cnv -c 64000 --cache-type-k q8_0 --cache-type-v turbo3

Results on the same RTX 4060 8GB, tested with a 27k token prompt at 64k context loaded:

Prefill: 200 tok/s → 320+ tok/s
Decode: stayed above 25 tok/s (without MTP)

Why it works: TurboQuant uses walsh hadamard rotation + polar quantization on the KV cache. keys are sensitive to compression, values aren't much, so it splits the difference: K stays at q8_0, V drops to turbo3 (~3 bits). 

bonus from the memory savings: same 8GB card can now stretch to 100-120k context with minimal decode penalty. It should now be snappier with any agent harness such as hermes agent without compromise on intelligence.

If you're already running Gemma 4 on a small card, this stacks on top for free. Try --cache-type-k q8_0 --cache-type-v turbo3 on your setup and report back what your prefill/decode split looks like.

unsloth model gguf and llama.cpp turboquant fork links in the comments.

what's your prefill number before vs after?

## 2026-06-18 (https://x.com/analogalok/status/2067622227810656559)

Gemma 4 12B QAT (dense) achieves 1000+ tokens/sec prefill on 8GB VRAM with 120k context 

Gemma 4 12B QAT (dense), TurboQuant (Without MTP), RTX 4060 8GB VRAM:

Prefill: 1000+ tok/s (42% increase)
Decode: 25+ tok/s (25% increase)
Context: 120k (150% increase)

prefill was 700 tok/sec and decode 20 tok/sec with only 48k context without turbo quant (older test with mtp link in the comments)

llama.cpp TurboQuant flags:

-m gemma-4-12B-it-qat-UD-Q4_K_XL.gguf -c 120000 --cache-type-k q8_0 --cache-type-v turbo3 -ngl 99 --port 8080

tested with a 27k prompt, 120k context loaded.

-ngl 99 here isn't a typo, full 12B dense, every layer on GPU, on an 8GB card. that's the part worth sitting with. The model has vision, audio input, thinking/reasoning and fits your 8GB card.

TurboQuant's KV cache savings are what free up the room to do that at 120k context.

side by side with yesterday: 26B A4B MoE got 320+ tok/s prefill. this dense 12B is clearing 1000+

rig: RTX 4060 8GB · i7H · 16GB RAM

same two flags as yesterday, different model size: 

--cache-type-k q8_0 --cache-type-v turbo3

thanks to TheTom/llama-cpp-turboquant, TurboQuant fork of llama.cpp by Tom Turney (@no_stp_on_snek) to make this work.  

unsloth's model quant huggingface and the llama.cpp fork github link in the comments

Do you prefer a dense or a MoE for your 8GB card?

## 2026-06-19 (https://x.com/analogalok/status/2067928384777425337)

built a Vision + Voice AI assistant mobile app that runs 100% offline on a 6 year old android phone.

no cloud. no API. no internet. Gemma 4 E2B QAT + llama.cpp, fully on device.

put my android phone in flight mode.

no wifi. no data. no internet, period.

held an 1887 british coin up to the camera.
it looked at it, figured out exactly what it was, and said so, out loud.

fully offline vision + voice AI assistant, running on the same 6 year old phone CPU (Note 20 Ultra, samsung exynos chip, 12 GB RAM). no GPU acceleration. 

# brain 

llama.cpp in termux. serves an openai compatible /v1/chat/completions on localhost, so it's a drop-in replacement for cloud api.

# vision  

CameraX grabs the frame → compress to jpeg → base64 → straight into the json payload. no cloud roundtrip, no upload.

# voice 

android's native TTS speaks the answer back, async, so the UI doesn't freeze waiting on it.

had to bump OkHttp's timeout so the connection doesn't die while the chip is still cooking the response

# the exact command:

LD_LIBRARY_PATH=. ./llama-server -m gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf --mmproj mmproj-F16.gguf -c 6000 -t 4 --port 8080 --no-mmap -v

that's the entire cloud AI stack. running in a phone. in flight mode.

if your android phone has 8gb+ ram, you already own everything needed to run this. no laptop required.

private, on device, edge ai isn't the future. it's already here.

my beginner friendly termux + llama.cpp guide and the  unsloth quantized model huggingface link in the comments

## 2026-06-20 (https://x.com/analogalok/status/2068314930621956551)

I built a 100% offline, Screen Aware, Private Local AI Assistant. The data never leaves my phone.

runs 100% locally. llama.cpp. google's gemma 4 e2b qat on the phone cpu.

Yesterday: It saw the real world.
Today: It sees my screen.

Long press Home -> it reads the screen, understands context, and speaks the answer. No cloud. Total privacy.

it can now summarize screen, translate to other languages, and answer any questions regarding any document that i have on my screen, reply to messages and emails, all privately.

In the video: Opened a Wikipedia page, long pressed the Home button, and tapped "Summarize." The AI instantly read the screen, compressed the context, processed it locally, and spoke the summary out loud.

Zero data leaves the device. Airplane mode? Works perfectly.

I intercept that bitmap -> encode it to base64 -> pipe it directly into my local llama.cpp server (still running Gemma-4 E2B QAT via Termux in the background).

It returns the answer via a local OpenAI compatible /v1/chat/completions endpoint and triggers Native Android TTS.

Instead of paying a monthly subscription and uploading your personal data to a remote cloud, you have a private, screen aware Jarvis that runs seamlessly on a 6 year old Exynos chip.

Edge AI isn't the future. It's already running in our pockets.

What else would you want it to do?

Check the comments below for my beginner friendly guide on setting up the llama.cpp on android.

I have also attached link to unsloth's gemma 4 e2b gguf on huggingface.

## 2026-06-21 (https://x.com/analogalok/status/2068630029047869659)

gemma-4-12B-agentic-fable5-composer2.5 V2 is out.

the agentic upgrade to the model trained on Fable 5's reasoning. Running it now with TurboQuant llama.cpp on a single RTX 4060( 8 GB VRAM) at 30 tokens/second with full 25000 context and reasoning:

# The benchmarks

v2 is built for coding + agentic work. writing code, running commands, using tools, debugging, multi step technical tasks. The clearest signal is tau2 bench telecom, an agentic tool use benchmark whose diagnose → fix → verify loop mirrors real terminal/debugging work:

tau2 bench telecom numbers:

base Gemma 4 12B: ~15% 
this finetune: ~55%. (Self reported)

thats a huge jump

# TheTom/llama-cpp-turboquant flags:  

llama-server.exe -m gemma4-v2-Q4_K_M.gguf -ngl 99 -c 25000 --cache-type-k q8_0 --cache-type-v turbo3  --port 8080

Flag breakdown:

 -ngl 99 → full GPU offload
 -c 25000 → 25K context
 --cache-type-k q8_0 --cache-type-v turbo3 → mixed-precision KV cache — K at 8-bit, V at ~3-bit via TurboQuant (Walsh Hadamard rotated polar quant, Google's own KV-compression research). 

Not even merged into mainline llama.cpp. running it off a fork.

No API. No cloud. Just llama.cpp. well, a fork of it and any 6gb+ GPU.

If you tried yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF, check this out and share your experience with the models

## 2026-06-21 (https://x.com/analogalok/status/2068732169670025639)

six months ago this wasn't happening on 8gb vram.

running unsloth's Q4_K_XL quant of gemma 4 26b-a4b-it-qat, a sparse MoE model with only 4b active params on a single rtx 4060 laptop gpu, 8gb vram, 20+ tok/s decode. 

no cloud, no api, no offload hacks. just a gaming laptop on battery.

what makes it fit: google's QAT (quantization aware training), plus MTP (multi token prediction) support in the latest llama.cpp builds. 

that combo is the single biggest unlock for local inference on low vram. rtx 3060, rtx 3070, gtx 1070, gtx 1080, rtx 4050, rtx 4060, rtx 5050, rtx 5060 — any 6-8gb consumer gpu, old or new — this model runs on it.

world cup season, so i told it to build a soccer themed flappy bird clone. one shot, zero iteration, fully playable.

six months ago an 8gb model could barely clone vanilla flappy bird. now it's shipping a themed game from a sparse MoE model running locally on a laptop battery.

inference benchmarks: 

- decode throughput: 30 tok/s 
- context: 64k. 

this is the real unlock. 64k ctx is what makes a hermes agent loop viable locally on this model, not just single-turn chat.

llama.cpp flags: 

-m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf -c 64000 -cmoe --port 8080

game's deployed on my own site, built and shipped end to end with open source llm, zero closed source api dependency in the pipeline. link in the description.

gguf weights on huggingface, link in the comments. pull it down, run it on whatever 8gb card is sitting in your rig. try the game and tell me your score and what you want in v2.

local llms on consumer gpus stopped being a meme.

## 2026-06-21 (https://x.com/analogalok/status/2068757260642472206)

gemma 4 26b-a4b moe just rewrote the definition of "gaming laptop" in 2026.

old definition: a laptop that can run games. 
new definition: a laptop that can run games and ship them.

same gpu, same 8gb vram, same battery. the only thing that changed is what's sitting in vram. a sparse moe model that one shots a playable game instead of just rendering one.

local inference on a consumer gpu used to be the bottleneck. now it's the feature.

2026 spec sheet for gaming laptop just added a line item nobody saw coming: can it run a local llm well enough to build what it plays.

## 2026-06-22 (https://x.com/analogalok/status/2069047278275637604)

Gemma 4 12B (Dense) vs. Gemma 4 26B (MoE): Local game coding showdown  on a single RTX 4060 (8 GB VRAM).

gemma 4 12b (dense) just lost a 1 shot coding duel to its own Gemma 4 26b MoE sibling and the failure mode is the most "small model" thing ever 

ran the identical prompt on both, fully local, no internet, no cloud inference: build a soccer themed flappy bird clone as a single self contained html file. canvas game, js game loop, the whole thing.

setup for gemma 4 12b: 
lm studio, gguf q4 quant, 32k context, reasoning on, 39 layers offloaded to gpu, ~15 tokens/sec. pure local llm inference, on-device, zero api calls.

gemma 26b a4b moe: 
one shot. fully playable. zero bugs. shipped with actual oop architecture. es6 classes for Ball, Goal, Particle. superior collision math. that's senior dev on a deadline energy from a model running on a single 8 GB gpu.

12b dense: 
also built the skeleton in one shot but shipped broken. ball passes through the goalposts? no score. ball falls off screen? no game over. 

Architecture: The 26B model opted for modular, Object Oriented JS using ES6 classes (Ball, Goal, Particle). The 12B model used a simpler, flat procedural structure with global state objects, which made the state slightly harder to manage during debugging.

took 2 follow up prompts to fully fix:

rewrite collision detection + add out of bounds game over rules. clamp the vertical spawn range on goalposts so difficulty didn't randomly spike top to bottom

12b is still genuinely strong for the param count and very steerable through iteration, it just needs the extra rounds.

and yeah, it tracks with the actual llm benchmarks: 

- livecodebench v6 -> 26b 77.1% vs 12b 72.0% 
- codeforces elo -> 26b 1718 vs 12b 1659 
- MMLU Pro -> 26b 82.6% vs 12b 77.2%

small gaps on a leaderboard, way more visible the second a real game loop with physics and collision enters the chat. 

the actual differentiator isn't raw syntax or boilerplate, it's spatial reasoning and state management. exactly where moe's extra effective capacity shows up.

6-8 gb vram warriors: which models are you running for coding?

## 2026-06-23 (https://x.com/analogalok/status/2069320343744020905)

Hermes Agent just hit 1 TRILLION tokens in a single day on OpenRouter.

that's more volume than the next 9 agents on the leaderboard COMBINED 

kilo code, openclaw, claude code, cline, pi, lemonade, gdevelop, openhands, pi agent, all of them stacked together still don't touch hermes alone.

13.7M requests/day. 200K GitHub stars. 15,000+ contributors.

And @NousResearch ships fast. like, embarrassingly fast:

- Just announced: Computer use via @trycua now works on Windows & Linux (macOS already supported)
- 2 days ago: Blank Slate mode. start with just a provider, model, file ops & terminal, then build your agent exactly how you want it.

nous research is shipping faster than the rest of the industry can write changelogs.

The numbers don't lie. The momentum doesn't lie.

Hermes is quietly becoming the default agent layer for the internet.

## 2026-06-23 (https://x.com/analogalok/status/2069422623508079054)

I just got Gemma 4 26B A4B MoE model running fully locally with Hermes agent on an 8GB RTX 4060 and it's now backtesting trading strategies end to end, no hand holding.

If you’re a trader or work on Wall Street, you don’t want to miss this.

Yes. fully automated. No cloud. No APIs beyond market data. 

# Here's what I did:

Setup:

- Model: Gemma 4 26B-A4B QAT (MoE), Q4_K_XL Unsloth's quant (link in the comments) 
- Inference: llama.cpp (turboquant fork by @no_stp_on_snek link in the comments)
- Hardware: RTX 4060, 8GB VRAM + 16GB RAM only (with 50 other chrome tabs open)
- Context: 64K

llama.cpp turboquant flags:
-m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf -c 64000 --cache-type-k q8_0 --cache-type-v turbo3 --port 8080

turboquant helps achieve high prefill and decode throughput for interactive sessions.

throughput with Hermes agent: 
decode: 25+ tokens/sec
prefill: 250+ tokens/sec

# Then I gave the agent one task:

Backtest a strategy:

- Buy when RSI crosses above 30
- Sell at +2% profit or -1% stoploss
- No overlapping positions
- Use Google stock via yfinance
- Generate a full HTML report with candlestick charts + signals

What happened next was wild. It didn't just write code, it ran the entire workflow itself:

Audited the environment (pip list, dependency check)

Hit a ModuleNotFoundError, multiple Python installs were conflicting

Ran where python to map every interpreter on the system

Manually selected the correct Python 3.13 path and re ran the script

Wrote a clean statevmachine backtester (strict no overlapping trades logic)

Patched a yfinance MultiIndex quirk that would've crashed the script

Built Plotly candlestick + RSI charts with buy/sell markers

Calculated win rate, PnL, and summary stats
Exported a polished single file HTML report. check the report at the end of the video or in the comments.

Biggest takeaway: local LLMs aren't just "chat assistants" anymore. They debug their own environment, write production code, and ship a finished deliverable on consumer hardware, for $0 in API costs. 

If you're still calling local models "toys," you're already behind.

This is just the beginning.

Hermes agent just surpassed 1 trillion tokens in a single day on OpenRouter. Think about the scale of total token generation happening right now.

Disclaimer: This is not financial advice. Consult a professional before making any trading decisions.

## 2026-06-23 (https://x.com/analogalok/status/2069464925345550528)

The capabilities are kinda insane too. it runs smoothly even on potato hardware with the right optimizations. Ive used it to build and deploy games, and even backtest trading strategies, all 100% locally on a single RTX 4060 (8GB VRAM) with just 16GB RAM on a $1K gaming laptop. 25+ decode and 250+ prefill throughput, turboquant with hermes agent. good enough for interactive sessions as well as automated loops 

https://t.co/LvCX9Sg5HO

## 2026-06-25 (https://x.com/analogalok/status/2070086574897864887)

Best llama.cpp flags to run Gemma 4 26b A4B MoE with Hermes Agent - 8 GB VRAM 

after the previous post, a lot of you in the replies said running Gemma 4 26B A4B, a 26 billion parameter MoE model on a consumer 8GB GPU interactively with Hermes agent was physically impossible.

Let me be clear: paying OpenAI for API calls is just a tax on not understanding your own hardware.

You absolutely CAN run the Gemma-4-26B-A4B-it QAT (Unsloth Q4_K_XL) completely locally on an Nvidia RTX 4060 8GB VRAM, an RTX 4060 Ti, RTX 3060 Ti, or even an RX 7600.

But you have to know how to tune your memory stack.

I spent the last 24 hours benchmarking every edge case in the llama.cpp TurboQuant fork.

Here are the answers to the top three questions lighting up in the replies: "Is -cmoe necessary?", "What’s the difference between q8_0 and turbo3?", and "Which is faster?"

Let me break down the black magic:

1) "How does a 26B model fit in 8GB VRAM?"
It’s a Mixture of Experts (MoE). It has 26B total parameters, but only 4B Active parameters (A4B) during any given token generation. With 4 bit quantization, the active weights sip VRAM. The real boss fight isn't the model, it’s the KV cache and the multimodal vision projector (--mmproj).

2)  When is -cmoe (CPU MoE) actually necessary?
Only when you are actively overflowing your VRAM and hitting system swap.

If you try to load a massive 250K context window AND the multimodal vision projector (mmproj) on an 8GB GPU, OS will panic swap to system RAM. My decode dropped to a miserable < 1 token/sec. Unusable.

The Fix: Slap on the -cmoe flag. This forces the inactive MoE weights into your 16GB of system RAM but keeps the attention mechanism, embeddings, and KV cache on the GPU.

Result? The speed instantly recovered to 130 prefill / 20 decode tok/sec.

Caveat: If you’re running a standard 64K context without image capabilities, DO NOT use -cmoe. It will needlessly bottleneck your GPU with CPU latency. Let the GPU eat.

3) q8_0 vs TurboQuant (turbo3): Which is faster?
TurboQuant is absolute wizardry. It uses Walsh Hadamard rotations to compress your V cache down to about 3.125 bits per value. But compression comes with a mathematical "tax" during the dequantization phase on your GPU.

Here is the golden rule:

- If VRAM is bleeding: Use turbo3. At 250K text context, it squeezed the cache just enough to keep everything entirely on the GPU, giving me a buttery 210 prefill / 20 decode tok/sec without needing -cmoe.
- If VRAM is safe (e.g., 64K context): Use q8_0. Because q8_0 is computationally lighter to unpack, it runs faster when space isn't an issue. At 64K, my RTX 4060 peaked at 300 prefill / 25 decode tok/sec using standard 8-bit cache.

The TL;DR for 8GB GPUs:

Short 64K Context? -> Full GPU + q8_0 cache (Max Speed: 25+ tok/s)

250K Text Only? -> Full GPU + turbo3 cache (Optimal: 20 tok/s)

250K + Vision Projector? -> -cmoe + q8_0 cache (Lifesaver: 20 tok/s)

We are running autonomous Hermes agents writing strict state machine trading bots, auditing their own environments, and generating HTML candlestick charts locally on gaming laptops.

Local AI is no longer a toy for nerds. It is a localized, private, zero cost production environment. If you don't understand how to deploy this, you are ngmi.

Check the attached Cheat Sheet matrix for the exact command line flags to use based on your context length.

## 2026-06-27 (https://x.com/analogalok/status/2070859518414885325)

I freaked out when my WiFi router suddenly died. then realized my autonomous Hermes agent is running fully local, nothing stopped.

Hermes Agent + Gemma 4 26B A4B QAT MoE, 100% local on my laptop, building my side projects while I scroll my phone

zero API calls. zero cost. 100% private. fully offline.

This might be the most satisfying thing I’ve watched in a while.

last post: showed Hermes + local Gemma 4 26B pull off backtest a trading strategy. this time I asked it to develop something i'd use myself everyday:

# A full unpacked extension with:

- React side panel UI
- Local llama.cpp backend (offline AI)
- Live tab sync + status tracking
- Auto context extraction via Readability.js

Vision on Demand → captures viewport screenshots as compressed JPEGs

Deterministic action system -> model outputs tokens -> directly controls page scrolling

It planned everything first. Then started executing step by step. all i did was say 'ok'. only once.

# What’s wild:

- It reports back after every phase
- Auto compresses context when nearing limits
- Actualy, stays on track

llama.cpp flags:

-m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf -c 64000 --cache-type-k q8_0 --cache-type-v q8_0 --port 8080

# Performance on a single NVIDIA RTX 4060 (8GB VRAM) + 16 GB DDR4 RAM Gaming Laptop:

- 300 tokens/sec prefill
- 25+ tokens/sec decode

More than usable for real dev workflows.

This isn’t AI demo territory anymore.
This is autonomous local software actually building things.

## 2026-06-28 (https://x.com/analogalok/status/2071186840825242008)

The AI race is no longer about who talks best. It’s about who ships fastest.

Elon just signaled something bigger than a model update.

Grok 4.5 is reportedly already in private beta at SpaceX and Tesla, trained from scratch on a 1.5T V9 foundation model with supplemental Cursor data. 

Early evals are said to be close to, or even beyond, Claude Opus territory.

What stands out most is the pace: RL is still improving the model every day, and Musk says new models will ship monthly this year. Yes u heard that right. Every single month.

## 2026-06-28 (https://x.com/analogalok/status/2071244829544317232)

gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF 

V/s 

Gemma 4 12b QAT base

Animation Test

llama.cpp flags: 
-m gemma-4-12B-it-qat-UD-Q4_K_XL.gguf -ngl 99 -c 16000 -v --port 8080

25 tokens/sec decode on a single rtx 4060 (8 gb vram)

the finetuned model v2 is built for coding + agentic work, writing code, running commands, using tools, debugging, multi step technical tasks. The clearest signal is tau2-bench telecom, an agentic tool use benchmark whose diagnose -> fix -> verify loop mirrors real terminal/debugging work. But fails at animation test. I have tried several times, same result. It also emits less number of tokens for this task as compared to the base model. 

Share your experience below if you have tried this one out

## 2026-06-30 (https://x.com/analogalok/status/2072033470868812083)

Raw Prompt: 

create an endless space shooter game that gets difficult progressively. A very realistic spaceship shoots enemies coming from the front. can collect new weapons and coins. a very realistic Jupiter like planet visible nearby to create realistic space background. very high quality graphics and gameplay. you can use any libs via cdn. single html file.

## 2026-06-30 (https://x.com/analogalok/status/2072087948477210982)

wait, claude code web app chat is not “just a chatbot” anymore?

it’s basically an agent with a sandboxed linux machine attached!

i asked claude sonnet 5 (extra high reasoning) to build a single file html game, a pretty standard stress test i use.

expected: it thinks a bit, maybe cites skills, spits out code.

Instead it:

- spun up a working directory
- wrote the code
- ran scripts to validate syntax
- launched a headless chromium via playwright
- executed the game
- took screenshots
- debugged issues based on output

iterated until it worked

no idea when this shipped, but this is genuinely wild. lemme know if i've been living under a rock.

## 2026-07-02 (https://x.com/analogalok/status/2072650920697934132)

Local AI optimization is officially outpacing hardware decay. 

I spent the last 3 hours building llama.cpp from scratch and benchmarking Google DeepMind’s new Gemma 4 26B A4B MoE on a prehistoric 8 year old, $500 NVIDIA Tesla T4 GPU.

The results absolutely break the conventional rules of inference.

Here is the raw data running unsloth/gemma-4-26B-A4B-it-qat-GGUF via llama.cpp on a completely free Google Colab Linux (Ubuntu) instance:

- 35k context: [ Prompt: 788.8 t/s | Gen: 47.4 t/s ] (-ngl 99) 
- 80k context: [prefill: 490.8 t/s | decode: 20.4 t/s ] 
- 180k context: [ Prompt: 242.4 t/s | Gen: 11.1 t/s ] 
- 250k context: [ Prompt: 220.2 t/s | Gen: 8.9 t/s ]

llama.cpp flags: 
./build/bin/llama-cli -m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf -p "Explain the concept of open source software to a 10 year old." -n 24000 -ngl 99 -c 250000

Yes, I shoved a quarter million tokens of context into a 2018 data center card, and it generated at nearly 9 tokens/sec decode throughput without a single Out Of Memory (OOM) crash. 

For the hardware nerds, here is the exact environment from my nvidia-smi: 

- Driver Version: 580.82.07  
- CUDA Version: 13.0 
- GPU: Tesla T4 (Turing Architecture)  
- VRAM: 15360MiB (16GB GDDR6) 
- Power: Sipping just 16W at idle, capped at 70W TDP

Google DeepMind really cooked with the Gemma 4 26B MoE (Mixture of Experts) architecture. But the real heroes here are the open source chads. Combining Unsloth's QAT (Quantization Aware Training) quant with the brutal C++ efficiency of llama.cpp allows us to push 50 tokens/sec on hardware that belongs in a museum.

What does this mean for you? 16GB VRAM is the ultimate sweet spot for local AI enthusiasts right now.

If you own a single RTX 4060 Ti 16GB, RTX 4070 Ti Super, RTX 4080, the new RTX 5070 Ti 16GB, an older 30 series like the RTX 3080 Ti Laptop card, or cloud GPUs like the A10G and L4 you are sitting on an AI goldmine. You already own the future.

You don't need to rent cloud APIs. You just need to compile your tools correctly and let your VRAM do the heavy lifting.

If you have a 16 GB VRAM GPU, run this and share your numbers for the community. Model's huggingface link in the comments.

## 2026-07-02 (https://x.com/analogalok/status/2072785983746277543)

you're paying $20/mo for something your $500 GPU can already do.

Gemma 4 26B A4B QAT MoE + Hermes Agent running on a single RTX 4060 (8GB VRAM).

Built a vision capable, 100% free, 100% local, private AI assistant that lives in my Chrome browser. No API keys. No cloud. No subscriptions. 100% vibe coded. 0% handholding.

It has full context of whatever's on my screen can answer questions, summarize pages, extract data, and see images. Same local model handles everything, no external calls, ever.

keep reading for the model and hermes agent tips i learnt while building this locally.

Here's the exact setup for anyone running local LLMs on 6-8 GB VRAM:

llama.cpp server flags (on my NVIDIA RTX 4060 8gb VRAM):

 -m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf --cache-type-k q8_0 --cache-type-v q8_0 -c 150000 --port 8080

Throughput with quantization:
Prefill: 200-250 tokens/sec
Decode: 20-25 tokens/sec

reduce context if oom on 6 gb vram card.

Key learnings:

- Quantize KV cache to q8 for faster prefill/decode. Prefill goes from 100-150 (unquantized) to 200-250 tok/s (q8).
- But watch out, once actual context grows past ~50k tokens on high entropy workloads, q8 KV quantization can cause hallucinations. Low entropy workloads are mostly unaffected. If you see it happening, drop the quantization. This is common across all local models.
- In Hermes Agent settings -> Memory & Context, bump compression threshold from default 0.5 to 0.7. Default triggers way too frequent context compression and eats time.

Up next: add persistent memory, web search, tool calling, streaming output and whatever you suggest.

Running a 26B MoE with vision + 150k context window on 8GB VRAM would've sounded impossible 6 months ago.

Works the same on the NVIDIA RTX 3060 Ti, 3070, 4060 Ti, 5060, 2080, or any 8GB card. VRAM is the only requirement.

Local AI agents are closer than people think. You just need to know where the knobs are.

Model's Unsloth quant hugging face link in the comments.

Have you tried Hermes agent by @NousResearch yet?

What are you building with local LLMs? Drop it below, let's see what this community is shipping.

## 2026-07-03 (https://x.com/analogalok/status/2073015008615911446)

This is the way.

If you still haven't found a real use case for local LLMs, start here.

Save tokens. Cut cost. Let your big model delegate simple async workloads to a local one running on your own box. use the larger model to verify.

Even 8GB VRAM is enough to get started.

Stuck on Qwen 3.5 9B with 6-8GB VRAM? Try Gemma 4 12B (dense) or Gemma 4 26B (MoE) instead.

Q4 quants of Gemma 4 12B fit entirely in VRAM. The 26B MoE will need some RAM offload, but it's worth it.

Expected throughput @ 8GB VRAM:
- Gemma 4 12B -> prefill: 500-1000 tok/s | decode: 20-30 tok/s
- Gemma 4 26B MoE -> prefill: 200-300 tok/s | decode: 20-30 tok/s

Stack KV cache quantization + turboquant + MTP (multi token prediction) to push throughput further.

Local models aren't a toy anymore. They're infra. 

have questions? shoot them in the comments

## 2026-07-04 (https://x.com/analogalok/status/2073369420563370351)

Free NVIDIA GPU with 16 GB VRAM GPU for Running Local LLMs!

If you want to master local LLMs but you're waiting until you can afford a $1,500 GPU, you're honestly not going to make it.

The open source AI ecosystem is moving way too fast for you to wait on your budget to catch up. Especially when you can build a bleeding edge inference engine from scratch right now, completely for free.

You don't need a heavy local rig to start. Google is literally letting you use an enterprise grade NVIDIA Tesla T4 GPU for $0/hour. 

At standard cloud computing rates (~$0.20/hr), Google Colab’s 4 hour daily free tier hands you roughly $24 worth of data center tier GPU compute every single month. And most people just waste it.

Let’s talk about the hardware you get access to for free.

The NVIDIA Tesla T4 is an absolute workhorse:

- Architecture: NVIDIA Turing (TU104)
- VRAM: 16GB GDDR6 (320 GB/s bandwidth)
- Compute: 320 Tensor Cores | 2560 CUDA Cores
- Performance: 130 TOPS INT8 | 8.1 TFLOPS FP32
- Power: Sipping energy at a max 70W TDP  

This is the exact same hardware I used to run DeepMind's Gemma 4 26B A4B QAT MoE at a 250,000 context window without a single Out Of Memory (OOM) crash.

If you have a web browser and 10 minutes, you have everything you need. I’ve put together a fully documented, cell by cell Google Colab notebook that teaches you exactly how to do this.

Here is what the notebook actually teaches you:

- How to provision an Ubuntu Linux environment with CUDA 13.0 and verify your driver stack.

- How to pull the source code and compile the latest llama.cpp C++ binaries from scratch, specifically optimizing the build for your exact GPU using the -DCMAKE_CUDA_ARCHITECTURES=native flag.

- How to directly download quantized local LLMs (GGUF format) straight from HuggingFace using the CLI.
- How to manage 16GB VRAM limits, offload neural network layers to the GPU, and push massive context windows.

Compile raw llama.cpp, ollama run a model, or spin up the LM Studio CLI. Pick whatever stack you are comfortable with. just start building.

No hardware. No credit card. No excuses.

Bookmark this post right now so you don't lose the tutorial.

Even if you don't have time to run it today, you are going to want this workflow in your engineering toolkit.

The link to the free Colab Notebook is in the comments below. Lemme know if you need more tutorials like this.

## 2026-07-04 (https://x.com/analogalok/status/2073388012864753765)

this one flag makes llama.cpp compile 5x faster

If you are compiling llama.cpp from source and it’s taking 20 minutes, you are doing it wrong.

By default, CMake builds CUDA support for every NVIDIA architecture in existence (Pascal, Volta, Turing, Ampere, Ada, Blackwell). You are literally burning compile time for GPUs you don't even own.

Add this single flag to your CMake command to build 5x faster: 

-DCMAKE_CUDA_ARCHITECTURES=native

Here is exactly what this does under the hood: It forces the compiler to look at the specific GPU currently sitting in your rig and optimizes the C++ binary strictly for that hardware.

The final binary file size shrinks massively.

You get absolute peak, hardware locked inference optimization.

The only catch is that the binary becomes hardware locked. If you build it on a 3090, it might not run on an RTX 5090. But if you’re building local AI pipelines, you should be compiling natively on the host machine anyway.

I baked this exact optimization flag (along with the full environment setup to build llama.cpp from scratch, download and run gemma 4 26b a4b moe form HuggingFace GGUF downloads and running it) directly into the free Colab Notebook. check the comments

bookmark this and give it a go next time you build llama.cpp

## 2026-07-06 (https://x.com/analogalok/status/2074119267344327023)

I can't afford a $2,000 GPU is officially a dead excuse. 

yesterday I showed you how to unlock an enterprise grade 16GB NVIDIA GPU for $0.

your immediate response? "How do I run BIGGER models?" "How do I push massive context windows without OOM crashes?"

Fine. Let’s double the compute.

Today, we are securing a Dual GPU cluster with 32GB of VRAM for free.

At standard cloud rates (~$0.40/hr for dual cards), Kaggle is handing you roughly $12 of free, heavy duty GPU compute every single month.

And instead of compiling C++ from source like yesterday, we are dropping in pre built CUDA binaries. You can have a massive 26 Billion parameter model running in literally under 2 minutes on this free ubuntu instance.

The Specs you are getting for $0:

- 2x NVIDIA Tesla T4 GPUs (turing architecture)
- 32GB GDDR6 VRAM Total
- 5120 CUDA Cores
- 30 GBs of Massive RAM
- 60 GBs of Storage
- Optional single p100 (pascal architecture, 16gb vram)

But here is the engineering reality: Throwing multiple GPUs at a Local LLM doesn't magically make it faster. If you don't understand how data moves across a motherboard, you will completely choke your inference engine.

Here is a 60 second masterclass on multi GPU parallelism in llama.cpp for you to experiemtn.

When you split a model across two GPUs, you have two choices:

1. Tensor Parallelism (Flag: -sm tensor) This mathematically slices every single neural layer in half. Both GPUs compute simultaneously. 
Because each card only holds half the equation, they must constantly synchronize their math for every single token. 

2. Pipeline Parallelism (Flag: -sm layer) This is the default. It chops the model sequentially. GPU 0 gets layers 1-20, GPU 1 gets layers 21-40.
It acts like a factory assembly line. GPU 0 processes the prompt, hands the data over the PCIe lane exactly once, and goes idle while GPU 1 finishes the math.

Benchmark on both and post your numbers!

In today's tutorial, I’ve built a clean Python dictionary configuration block so you can seamlessly experiment with the heavy hitting flags:  

-ngl 99 (Offload all layers to both GPUs)  
-c 250000 (Push a massive 250k context window)

With 32GB of VRAM and Pipeline Parallelism, you can easily load DeepMind's Gemma 4 26B A4B MoE, ingest entire codebases into the prompt, and never see an Out of Memory core dump. I could easily manage 62 tokens/sec decode without any additional optimizations.

No compilation time. No credit card. Zero excuses.

Bookmark this post right now so you don't lose this multi GPU configuration workflow. Don't forget to share it so it reaches every GPU poor person struggling with compute.

I’ve put together a brand new, cell by cell Kaggle notebook specifically for this Dual T4 setup.

The link to the free Notebook is in the comments below. Let me know what massive models you're spinning up today.

## 2026-07-06 (https://x.com/analogalok/status/2074125802862772243)

I’m publishing free local AI tutorials, hardware benchmarks, and zero cost setups like this every single day. If this workflow brought you value today, drop a follow. It costs you $0, keeps you on the bleeding edge, and signals me to keep open sourcing these resources for the timeline.

## 2026-07-09 (https://x.com/analogalok/status/2075252751429403017)

Stop blindly trusting the default multi GPU settings for your Local LLMs. You are literally leaving 25% performance on the table.

I spent the last 3 hours melting free dual Nvidia T4 GPUs to finally settle the Llama.cpp debate: Layer vs Tensor split.

The results completely flip how you should architect RAG vs. Chat pipelines. Here is the raw data:

If you’re running models that exceed a single GPU’s VRAM, llama.cpp gives you two ways to split the weights: Layer Mode (Pipeline Parallelism) and the experimental Tensor Mode (Tensor Parallelism).

The docs give you the theory, but I wanted the empirical data.

I loaded up the unsloth's Q4_K_XL quant of Gemma 4 26B QAT (MoE) on a dual T4 GPU rig.

Crucially, this setup uses standard PCIe interconnects. NO high speed NVLink. I wrote a script to scale the context window from 10k up to a brutal 50k tokens, clearing the VRAM between runs to see exactly where the hardware chokes.

Here is what the benchmarks actually prove:

# THE BEST for RAG: Layer Mode

llama.cpp flag: llama-server -m gemma-4-26B-A4B-it-qat-UD-Q4_K_XL.gguf -ngl 99 -c 60000 -fa on --split-mode layer --host 127.0.0.1 --port 8080

If you are building document summarization, RAG pipelines, or processing massive payloads, --split-mode layer is your god tier flag.

At the 50,000 token mark: 
- Layer Mode Prefill: 1,223 tokens/sec 
- Tensor Mode Prefill: 979 tokens/sec

The Verdict: Layer mode is 25% faster at eating massive prompts.

WHY?: Layer mode splits the network sequentially. GPU 0 does its math, then hands the baton to GPU 1. It minimizes cross GPU traffic. If your GPUs are communicating over standard PCIe lanes, this prevents your interconnect from bottlenecking the prefill.

# THE BEST for CHAT: Tensor Mode

llama.cpp flag:
llama-server -m model.gguf -ngl 99 -c 60000 -fa on --split-mode tensor --host 127.0.0.1 --port 8080

If you are building an interactive Chat UI or an AI coding assistant, human perceived latency (Decode Speed) is everything. This is where --split-mode tensor shines.

Across the entire benchmark matrix: 
- Tensor Mode Decode: 52 to 57 tokens/sec 
- Layer Mode Decode: 44 to 52 tokens/sec

The Verdict: Tensor mode generates output tokens roughly 16% faster.

The "Why": Tensor Parallelism splits the individual matrix multiplications across the GPUs. Both GPUs work simultaneously to predict the next token, speeding up generation.

I packaged the entire 50k stress test code and data visualization scripts into a fully reproducible Kaggle Notebook. The notebook is completely plug and play. it automatically pulls the Gemma 26B GGUF from huggingface, fetches the prebuilt llama.cpp CUDA binaries, and runs the entire multi GPU matrix so you don't have to compile a thing.

Fork the code, run it on your own hardware, and see the bottleneck for yourself. Or run the same notebook with different models and post your results. Link to the Notebook with free 2x Nvidia T4 GPUs in the comments.

## 2026-07-09 (https://x.com/analogalok/status/2075308822806380846)

building stateless ai agents in 2026 is a joke. while you've been fighting with raw RAG pipelines, hermes agent quietly perfected a 3 tier memory stack that acts exactly like L1/L2/L3 cache for your agent. 

if your llm still wakes up like a newborn every session, read this.

interacting with most ai agents is like living in an infinite groundhog day loop. they have the object permanence of a goldfish. every single session you are forced to re inject your stack, your rules, and what you literally just built together 12 hours ago. it’s brutal friction.

hermes agent by @NousResearch  fixed this by treating agent memory like cpu architecture. it doesn't just dump everything into a vector db. it uses three distinct layers, each operating at a different speed.

# tier 1: the L1 cache (MEMORY.md & USER.md)

this is the agent's working brain. it’s just two tiny, heavily constrained markdown files stored locally.

- USER.md (1.3k chars) holds your profile, skill level, and comms preferences.
- MEMORY.md (2.2k chars) holds environment quirks, tool rules, and project conventions.

because the capacity is strictly capped, it forces the agent to be efficient. when it hits 80% capacity, the agent natively self consolidates. it merges related entries into hyper dense summaries so only the absolute highest signal facts survive. this tier is frozen and injected into the system prompt at the start of every session. zero latency.

# tier 2: the L2 archive (full text SQLite)
every CLI and messaging conversation you’ve ever had is silently logged into a local SQLite db. the agent has tools to actively query weeks of past chat history via full text search.

the tradeoff is elegant: tier 1 is always in context but tiny. tier 2 is infinite but requires an active search + LLM summarization to retrieve. critical facts live in memory. everything else is searchable on demand.

# tier 3: the L3 gigabrain (external providers)

this is where it gets actually insane. hermes ships with an entire ecosystem of external memory plugins that run passively alongside the built in tiers.

you run hermes memory setup and you can bolt on entirely different cognitive architectures. it prefetches relevant context in the background before every turn, and extracts new memories the second the session ends.

# here is the full lineup of brains you can plug in:

- honcho: AI native psychological profiling. the agent uses "dialectic reasoning" (arguing with itself in the background) to form persistent conclusions about you. multi agent ready. - cloud (paid)

- holographic: local only SQLite fact store using HRR (Holographic Reduced Representations) for algebraic queries. it has a "trust scoring" system where you rate its memories, and an auto contradict tool to spot conflicting facts. - local (free)

- hindsight: pure knowledge graph memory. the agent uses a hindsight_reflect tool to natively synthesize entirely separate historical nodes into new insights. - cloud/local (free/paid)

- openviking: self hosted filesystem style knowledge trees. uses tiered loading (L0 to L2) so it never nukes your context window. - self hosted (free)

- byterover: portable CLI based memory. does "pre compression extraction", saving insights right before your context window gets truncated. - cloud/local (free/paid)

- mem0: completely hands off server side LLM extraction with auto deduplication. runs via cloud, docker, or entirely in process (OSS). cloud/self hosted (paid/free)

- retaindb: cloud memory API built for teams that uses delta compression and categorizes into 7 specific memory types. - cloud (paid)

- supermemory: full session graph ingest. features "context fencing" to strip recalled memories from captured turns to prevent recursive memory pollution. - cloud (paid)

- memori: structured long term memory with background tool aware capture, strict project attribution, and explicit explicit recall tools for facts. - cloud (paid/free)

this is what actual stateful AI looks like. a fast, constrained working memory layer that self optimizes, backed by a massive, searchable archive, augmented by specialized graph/vector databases.

if your agent doesn't remember that weird docker bug you fixed together last tuesday, you are building toys. ngmi.

what’s your current memory stack looking like? are we trusting cloud graphs or keeping it local with holographic sqlite? drop it below

## 2026-07-10 (https://x.com/analogalok/status/2075523240370610644)

if you're running a multi GPU llama.cpp setup and you've never touched --split-mode, you're running it wrong for at least one of your two most common workloads. ran the numbers on 2x T4s, plain PCIe, no NVLink, 10k to 50k context. the gap between the two modes isn't small, and it isn't even constant.

quick recap for the new people: llama.cpp gives you two ways to split a model across GPUs that don't fit on one card.

- layer mode (pipeline parallelism): GPU0 does its layers, hands off to GPU1, done. sequential. 
- tensor mode (tensor parallelism, still experimental): both GPUs compute part of every matmul, every layer, in parallel. syncs constantly.

conventional wisdom says tensor mode needs NVLink or it's DOA on PCIe. I ran it on 2x T4s. bog standard PCIe. no NVLink. gemma 26B QAT (MoE), Q4_K_XL, context scaled 10k -> 50k, VRAM cleared between every run.

prefill (prompt processing) - layer mode wins, and it's not close: at 50k context: layer = 1223 tok/s, tensor = 979 tok/s. that's 25% left on the table if you default to tensor for a RAG or long context pipeline. layer mode only hands off activations once per GPU boundary, so a slow interconnect barely matters. tensor mode syncs after every single layer. on PCIe that adds up fast when you're compute bound already.

decode (token generation) - tensor mode wins. but here's the part I missed the first time:
the gap isn't constant. it grows with context.

10k tokens: tensor beats layer by ~10% (57.5 vs 52 tok/s)

50k tokens: tensor beats layer by ~16% (52.3 vs 45 tok/s)

layer mode's decode speed decays faster as context grows. tensor mode's decays slower. why: this isn't just about compute, it's about where the KV cache lives. in layer mode, the entire KV cache for a given layer sits on whichever single GPU owns that layer, so as your context grows, that one GPU alone eats the growing memory bandwidth cost. 

in tensor mode the KV cache is sharded across both GPUs along with the weights, so that cost gets split. the longer your conversation gets, the more this compounds in tensor mode's favor.

none of this needed NVLink. two free T4s on Kaggle, standard PCIe. if your interconnect is even worse than that your mileage will vary, but the mechanism (KV cache sharding vs KV cache concentration) doesn't change. only the magnitude will.

full reproducible notebook in the replies. pulls the gguf, pulls prebuilt llama.cpp cuda binaries, runs the entire 10k-50k matrix, spits out these exact charts. 

fork it, run it on your own rig, post your numbers.

## 2026-07-10 (https://x.com/analogalok/status/2075573655002927543)

90% of "AI developers" just download pre packaged GGUF files from Hugging Face, hit run, and call it a day.

The top 10% know how to pull the raw safetensors, run the math, and quantize massive models into Q4_K_M themselves.

If you think llama.cpp can only execute models, you’re missing the best part of the open source ecosystem. It’s a high performance optimization suite. Manually stripping 69% of the VRAM footprint off a brand new model architecture is where real infrastructure value is made.

If you want to actually master local inference and deploy models like Google’s massive Gemma 4 12B it on consumer NVIDIA hardware using llama.cpp, you need to learn this pipeline. Let's build it. 

I just took the raw 22.7 GB Gemma 4 baseline and manually compressed it down to a 7.02 GB Q4_K_M GGUF artifact using llama.cpp. That is a 69% reduction in footprint.

No quality loss. No VRAM bottlenecks. Just native, hardware accelerated C++ inference running a full 2,50,000 token context window on a dual NVIDIA Tesla T4 setup.

Stop melting your VRAM on unoptimized weights and stop relying on other people's pipelines. Own your stack.

I mapped this entire architecture from dynamic binary fetching to raw quantization and real time GPU streaming into a single, bulletproof notebook.

Notebook link is in the comments below.

Bookmark this blueprint for your next deployment and tell me which quantization works best for your workflow and model.

## 2026-07-10 (https://x.com/analogalok/status/2075602279596781958)

I’m publishing free local AI tutorials, hardware benchmarks, and zero cost setups like this every single day. If this workflow brought you value today, drop a follow. It costs you $0, keeps you on the bleeding edge, and signals me to keep open sourcing these resources for the timeline.

## 2026-07-11 (https://x.com/analogalok/status/2075943220136309064)

If you don't own a GPU or have one yet don't know how to run gguf models from hugginface using llama.cpp, you have to choices:

1) keep waiting 

2)this colab on a free NVIDIA t4 GPU (16 GB VRam) shows u how to build llama.cpp from source, grab gguf from huggingface and actually run inference.no waiting required

The link to the colab notebook is in the comments. Start with ollama or lm studio if llama.cpp is overwhelming. start somewhere.

## 2026-07-12 (https://x.com/analogalok/status/2076307056840368220)

A lot of people starting with local LLMs hear "quantization" and assume it's just one thing. It's not. There are two things you can quantize. the model weights and the KV cache and they do very different jobs. Let me explain.

Weight quantization is what everyone means when they say "I quantized a model." You take the raw weights and compress the precision, FP16 down to Q8, Q5, Q4_K_M, etc. This shrinks the model file itself. It's a one time, static compression. In my last post I took Gemma 4 12b (dense) from a 22.7GB baseline down to a 7.02GB Q4_K_M GGUF, a 69% reduction and once that file is built, that number never moves again.

KV cache quantization is different. The KV cache isn't part of the model file at all. It's memory allocated at runtime to store the key/value tensors for every token you generate. It has no fixed size, it grows with every token in your context window. You can run the smallest, most aggressively quantized model on earth and still blow up your VRAM if the cache itself is sitting in FP16 and your context is long.

llama.cpp lets you quantize the cache independently with --cache-type-k and --cache-type-v, dropping it from FP16 down to Q8_0 or Q4_0. Same core idea as weight quantization, just applied to a completely different slice of your memory budget. One thing worth remembering: K is more sensitive to quantization than V. If you're deciding where to be conservative, protect K first and push V harder.

But it's not free. KV cache quantization is lossy, you're compressing the actual keys and values the model attends over, so output quality does take a hit. Newer open source models have gotten noticeably more resilient to this, but that resilience has a ceiling. Running Hermes as a coding agent at higher context, I noticed the degradation stays invisible early on, then becomes noticeable once the real task context pushes past roughly 50k tokens.

There's also a dequantization tax nobody mentions. Most GPUs don't have native compute kernels for every quantized format, so those quantized values often get dequantized back to FP16 or BF16 on the fly before the actual matmul runs. You save memory and bandwidth, but you pay some of it back in compute overhead. The VRAM savings aren't free, they're a trade.

Two knobs. Two separate bottlenecks. Static disk footprint vs dynamic runtime VRAM, and both come with their own cost when you push them too far. If you're only touching one of them, you're leaving performance and headroom on the table.

KV cache quantization comes down to adding two flags to your llama.cpp command. That same repo already lets you quantize the model itself, so the full pipeline, weights and cache, runs through one tool. I put the entire thing into a free Kaggle notebook, quantize your own model, quantize the cache, and run it end to end on free NVIDIA GPUs. Notebook link in the comments.
