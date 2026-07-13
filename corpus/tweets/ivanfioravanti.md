# @ivanfioravanti — long-form tweets

## 2026-06-14 (https://x.com/ivanfioravanti/status/2066212607149707663)

MiniMax M3 is a strong model and MiniMax Code skills "marketplace" is full of treasures 👀

Here I've used landing page builder with this prompt: Create a landing page for a new brain waves reader device: invent brand logo, name and payoff. use the landing page builder skill

I really like the proactive way of analyzing things and asking me my feedback, how I want to proceed, suggesting me possible issues to fix. 

Big boost compared to M2.7!

## 2026-06-14 (https://x.com/ivanfioravanti/status/2066248325976768749)

Images created in the last 15 minutes by my hn_local_image project from Hacker News headlines...

Why this 1 everywhere? 🤔 It's incredible seeing models creating images interpreting freely a bunch of text.

Repo here if you want to play with it: https://t.co/OCNrkgoGvg https://t.co/xzQQEJqb1y

## 2026-06-20 (https://x.com/ivanfioravanti/status/2068441617137103123)

I see Nvidia sending DGX Spark to many on X so that they can test and publish results.

It seems I'll have to buy my own to test and share my own 😎 
But that memory bandwidth is really stopping me from buying one 😖

Anyone out there with a DGX Spark testing some text to image or some video models willing to share results? This could be something to push me buying it.

Otherwise I think I'll save (a lot of) money for a GB300.

## 2026-06-20 (https://x.com/ivanfioravanti/status/2068442745673601059)

The real problem of Apple Silicon at the moment is that everything is CUDA driven, luckily with AI Agents you cn convert nearly every project to run on MLX, but it takes time and effort. I hope things will improve over time.

In the meantime... I hope to have my @luceboxai soon to make some tests!

## 2026-06-21 (https://x.com/ivanfioravanti/status/2068722319913066603)

MLX GLM 5.2 Distributed on two M3 Ultra 512GB 🔥

One M3 Ultra: 18.8 tokens/sec
Two M3 Ultra: 23.4 tokens/sec 

Context:
- PR by @pcuenq is still open and probably there is room for improvement: https://t.co/4TAQSib03F
- basic generation test to measure decoding performance here, I will do a full context benchmarking once PR is more mature
- nvfp4 quantization used
- Video alternates standard speed and x20, with one Mac first and distributed later.

Enjoy! 🙌🏻

## 2026-06-23 (https://x.com/ivanfioravanti/status/2069333674940633472)

I did it, I bought an Nvidia DGX Spark and paid for it.
I really want to test this personally and see it in action.

I want to thank @NVIDIAAI for building this machine 🤣

Keep me posted on future v2 please 🙏 and be ready that I'll come asking a discount for second one 😎 https://t.co/KFmY38QuP7

## 2026-06-24 (https://x.com/ivanfioravanti/status/2069632859820728794)

I have a vision of a possible future for Local AI in the next 18-24 months HaaS: Hardware as a Service:
- local models extremely powerful
- classic hardware extremely expensive
- model vendors starting to to rent dedicated hardware (LLMs embedded on chips) 

In a way or another, AI vendors will have to start making money from models running locally. 
What do you think? 
Do you see other possible ways?

## 2026-06-25 (https://x.com/ivanfioravanti/status/2070180738977169573)

First test llama.cpp M5 Max vs DGX Spark! 🔥
NOTE: basic and not optimized run on both side.

I can finally compare them personally
In larger contexts, the GX10 is performing quite well! 

I will try MLX on CUDA too! Stay tuned this is just the beginning 😎

Model unsloth/Qwen3.6-35B-A3B-MTP-GGUF:UD-Q4_K_XL 
Engine: llama.cpp
Command pretty basic on both machines: 
llama-server -hf nvidia/Qwen3.6-35B-A3B-NVFP4

M5 Max:
2k pp 2756 tg 93 t/s
4k pp 2742 tg 91 t/s
8k pp 2461 tg 89 t/s
16k pp 1903 tg 84 t/s
32k pp 1212 tg 68 t/s
64k pp 535 tg 46 t/s
128k pp 320 tg 34 t/s

DGX Spark:
2k pp 2059 tg 65 t/s
4k pp 2148 tg 64 t/s
8k pp 2175 tg 62 t/s
16k pp 2149 tg 59 t/s
32k pp 2066 tg 54 t/s
64k pp 1918 tg 46 t/s
128k pp 1667 tg 36 t/s

## 2026-06-25 (https://x.com/ivanfioravanti/status/2070239569782640892)

DGX qwen3.6-35b-a3b-nvfp4 with and without MTP
vLLM recipes used from this great repo: https://t.co/AZu5xxGbqY 

Prefill is really fast, but even decode is not bad at all. 👀
I'll search for some evals of these nvfp4 quantized models.

I was reading that there were issues with nvfp4, it seems working to me, no? 🤔

## 2026-06-29 (https://x.com/ivanfioravanti/status/2071507953157292308)

I'm pushing DGX Spark to its very limit with vllm right now with nvfp4, DFlash and Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP-XS model. 

Up to 183 toks/s using batch 16!
Prefill is so freaking fast 👀

lm-eval is running.

Thanks to @SpaceTimeViking @AgentSparko and @MiaAI_lab for the ton of direct and indirect hints I've got from you! 🙏

## 2026-06-30 (https://x.com/ivanfioravanti/status/2071926688536002906)

I can finally showcase my Nous Research hat and shirt! Let's push Hermes Agent to the max! 

Clearly Local AI in all possible (for me) ways tonight at 8pm CEST 🚀 with @maeste @dom_gag_96 and two special guests! 🔥👀

vllm on DGX Spark for Ornith-1.0-35B-AEON-Ultimate-Uncensored-NVFP4 
llamacpp on M5 Max for Qwen3.6-27B-MTP-GGUF
ds4 on M3 Ultra for DeepSeek V4 Flash q4-imatrix

## 2026-07-01 (https://x.com/ivanfioravanti/status/2072418199690158481)

DGC Spark Qwen3.6-27B-NVFP4 by @NVIDIAAI  vLLM 
Fast and furious! 🔥

Benchmark Results using vllm 0.24.0 (I had issues with vllm:nightly)
Hardware: aarch64, 121.7GB RAM, 20 CPU cores

1k pp 988 tg 28 t/s
2k pp 1055 tg 28 t/s
4k pp 1078 tg 30 t/s
8k pp 936 tg 28 t/s
16k pp 903 tg 29 t/s
32k pp 851 tg 33 t/s
64k pp 765 tg 27 t/s
128k pp 639 tg 23 t/s

Total generated tokens: 1024
Batch TPS: b1 20 b2 31 b4 39 b8 41 b16 42

## 2026-07-02 (https://x.com/ivanfioravanti/status/2072619773775511705)

Qwen3.6-27B MTP Context Benchmark on DGX Spark, M3 Ultra and M5 Max 🔥

Quantization: nvfp4 vs oQ4
Sofware: vllm 0.24.0 DGX, oMLX 0.4.5dev1 (without cache) on Apple Silicon

DGX Spark is the winner on Prefill/Promp Processing
Apple Silicon on Decoding/ Text Generation

Details of each run 👇

## 2026-07-02 (https://x.com/ivanfioravanti/status/2072619777458098384)

nvidia/Qwen3.6-27B-NVFP4 vLLM Benchmark Results
Hardware: DGX Spark, 128GB RAM

1k pp 988 tg 28 t/s
2k pp 1055 tg 28 t/s
4k pp 1078 tg 30 t/s
8k pp 936 tg 28 t/s
16k pp 903 tg 29 t/s
32k pp 851 tg 33 t/s
64k pp 765 tg 27 t/s
128k pp 639 tg 23 t/s

Total generated tokens: 1024
Batch TPS: b1 20 b2 31 b4 39 b8 41 b16 42

## 2026-07-02 (https://x.com/ivanfioravanti/status/2072619781010686005)

Qwen3.6-27B-oQ4-mtp oMLX API Benchmark Results
Hardware: Apple M5 Max, 128.0GB RAM, 18 CPU cores, 40 GPU cores

0.5k pp 420 tg 41 t/s 0.0GB
1k pp 536 tg 42 t/s 0.0GB
2k pp 637 tg 41 t/s 0.0GB
4k pp 679 tg 39 t/s 0.0GB
8k pp 699 tg 40 t/s 0.0GB
16k pp 674 tg 35 t/s 0.0GB
32k pp 606 tg 30 t/s 0.0GB
64k pp 492 tg 27 t/s 0.0GB
128k pp 368 tg 21 t/s 0.0GB

Total generated tokens: 1152
Batch TPS: b1 39 b2 45 b4 52 b8 48 b16 62

## 2026-07-02 (https://x.com/ivanfioravanti/status/2072619784672358502)

Jundot/Qwen3.6-27B-oQ4-mtp oMLX API Benchmark Results
Hardware: Apple M3 Ultra, 512.0GB RAM, 32 CPU cores, 80 GPU cores

0.5k pp 304 tg 36 t/s 0.0GB
1k pp 332 tg 37 t/s 0.0GB
2k pp 368 tg 37 t/s 0.0GB
4k pp 372 tg 34 t/s 0.0GB
8k pp 376 tg 37 t/s 0.0GB
16k pp 354 tg 35 t/s 0.0GB
32k pp 317 tg 32 t/s 0.0GB
64k pp 265 tg 28 t/s 0.0GB
128k pp 223 tg 24 t/s 0.0GB

Total generated tokens: 1152
Batch TPS: b1 46 b2 50 b4 65 b8 54 b16 56

## 2026-07-03 (https://x.com/ivanfioravanti/status/2072994940984950915)

Honestly I'm really tired of people focusing on their little garden, be it Italy, Europe, USA, China or anywhere else.

WE are the humankind, ALL OF US.

AI is something new and we need to be in this revolution all together. We need to find ways to adapt to a completely new world where we are no longer the most intelligent species on this planet 🤷🏻‍♂️

## 2026-07-04 (https://x.com/ivanfioravanti/status/2073424981883535595)

A quick benchmark of Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-MLX-FP4.

I'm starting to focus more on latency, TTFT and TPOT (Time Per Output Token: Time to generate each additional output token.) 

On Apple Silicon TTFT can be quite long, but TPOT is better than DGX Spark. I want to find the good trade-off for each model and choose hardawre accordingly 💪

Hardware: Apple M5 Max, 128.0GB RAM, 18 CPU cores, 40 GPU cores

0.5k pp 494 tg 32 t/s mem 17.0GB kv 0.20GB
1k pp 533 tg 31 t/s mem 17.5GB kv 0.22GB
2k pp 598 tg 31 t/s mem 18.8GB kv 0.30GB
4k pp 651 tg 31 t/s mem 19.2GB kv 0.44GB
8k pp 648 tg 30 t/s mem 19.9GB kv 0.71GB
16k pp 647 tg 29 t/s mem 21.2GB kv 1.24GB
32k pp 595 tg 27 t/s mem 23.7GB kv 2.32GB
64k pp 496 tg 23 t/s mem 28.9GB kv 4.45GB
128k pp 359 tg 18 t/s mem 40.1GB kv 8.64GB

Total generated tokens: 1152
Perplexity: 4.98
Batch TPS: b1 32 b2 40 b4 53 b8 59 b16 102
Batch KV : b1 0.30GB b2 0.59GB b4 1.19GB b8 2.37GB b16 4.75GB

## 2026-07-04 (https://x.com/ivanfioravanti/status/2073445953399386308)

Exposing them in clear terms is my focus now. You could deduct them from previous charts, but I want to show them more directly. 💪

Especially in the batch inference part, I think many people have not clear in mind that speed there implies a long wait and it's not suitable for intreactive scenarios.

## 2026-07-05 (https://x.com/ivanfioravanti/status/2073837770133712955)

Another experiment on ds4 engine 🚀
GLM 5.2 batch inference for ds4-eval only. 
It's still a draft, but it seems working.

Sequential ~16 toks/s
Batch 8 ~19 toks/s (in the video is 23 but later on it stabilizes to lower rate it)
Batch 12 ~21 toks/s
Batch 16 ~ 22 toks/s

I'll let them b12 finish to compare results 💪

## 2026-07-05 (https://x.com/ivanfioravanti/status/2073857525473259981)

DGX Spark LoRA creation for Z-Image Turbo completed!
Children Drawing style LoRA here used with ComfyUI!

Animated GIFs showing the evolution of the model each 250 iters. 

Bonus: I asked Hermes Agent to navigate to AI Toolkit page, select all pictures with horse and all with bears and create an animated GIF each. Voilà!

Easy, funny and powerful! @ostrisai thanks for this incredible AI Toolkit!

Now it's LTX 2.3 time! It'd movie time!

## 2026-07-06 (https://x.com/ivanfioravanti/status/2074177699552116883)

DGX Spark Context Benchmark on Qwen3.6-35B-A3B-UD-Q8_K_XL llamacpp script released by Mia.

It's fast! Time to test quality and some real life usage in Hermes Agent! 🚀

Qwen3.6-35B-A3B-UD-Q8_K_XL llama.cpp Benchmark Results
Hardware: aarch64, 121.7GB RAM, 20 CPU cores

2k pp 1573 tg 79 t/s
4k pp 1659 tg 78 t/s
8k pp 1694 tg 79 t/s
16k pp 1652 tg 70 t/s
32k pp 1628 tg 68 t/s
64k pp 1519 tg 58 t/s
128k pp 1339 tg 42 t/s
256k pp 1052 tg 31 t/s

## 2026-07-08 (https://x.com/ivanfioravanti/status/2074788458212560997)

I tested MTPLX v2 with QWEN 3.6 27B and compared it with oMLX without cache on M5 Max and DGX Spark on vllm using nvfp4 model version. More details in 🧵

I've reached 82.8 tps of max decoding speed! 🔥

Custom Metal Kernel design specifically for this model and for Apple Silicon is just perfect! This is the way forward! Great job @Youssofal_ 

Look at the website here! 👇

Here a website with recap, built with GLM 5.2 running locally 💪 
https://t.co/alXzKFe1LV

First chart and preview from the website.

## 2026-07-09 (https://x.com/ivanfioravanti/status/2075214772211990682)

Grok 4.5 is powerful, fast and furious! 
I gave it this basic prompt: "Create A weather dashboard with animated states."

Look at the final result! Connected to real APIs!

Back to @cursor_ai thanks to this model and upgraded to Pro+ too, to start pushing on it! 🚀 https://t.co/CqyEVzyZp2

## 2026-07-09 (https://x.com/ivanfioravanti/status/2075234284735000670)

Here I tried same prompt but using Hermes MoA (Mixture of Agents) with:
Reference models:
- GLM 5.2 
- MiniMax M3
Aggregator / Acting model: MiniMax M3

I did a test with GPT 5.5 as Aggregator but result was so bad that I trashed it immediately 🤣 I hope 5.6 will be better on the UI side.

## 2026-07-09 (https://x.com/ivanfioravanti/status/2075239703205269996)

Guess which country was the only one out of 27 fighting for democracy on Chat Control 1.0 mass scanning law? 

🇮🇹 ITALY 🇮🇹 and this makes me proud to be Italian more than ever! 

What are the other 26 countries doing? What is left of France the Liberté, Égalité, Fraternité? What about others?

Website: https://t.co/DSfQravtCu

## 2026-07-09 (https://x.com/ivanfioravanti/status/2075259391444398475)

Here the detailed vote of EU on Temporary derogation from certain provisions of the ePrivacy Directive to combat online child sexual abuse. 
You can see votes by country or single representative we voted 🤬
https://t.co/2ormTeh78a

The real countries against and fighting for democracy have been:
- Spain
- Poland
- Romania
- Hungary
- Portugal
- Greece
- Finland
- Ireland
- Lithuania
- Latvia
- Cyprus

No more proud of being Italian 😡

## 2026-07-09 (https://x.com/ivanfioravanti/status/2075296428054966724)

If I launch a new startup I have all the hardware needed to play with Local AI good models.
- two M3 Ultra 512GB
- one DGX Spark (soon two)
- one M5 Max
- one custom built LuceBox (soon)
- one M5 Ultra (as soon as possible)

These combined with LiteLLM unlock incredible scenarios!

I'll probably offer some inference to my X subscribers in future at least I give you something back 🙏

As soon as I become black belt on LiteLLM 💪

## 2026-07-10 (https://x.com/ivanfioravanti/status/2075463068247581161)

oMLX v0.5.0rc1 is full of performance optimizations and great features! Download it now!

I love:
- Added Tencent Hy3 / HunYuan V3 support.
- Performance optimizations
- oMLX Custom Kernels
- oQe imatrix enhanced quantization

Full release notes here: https://t.co/GOPZ4jlUaQ https://t.co/58NJXYNObT

## 2026-07-10 (https://x.com/ivanfioravanti/status/2075647000121676258)

MLX: Alis Studio is another kind of magic by 
@Alisvolatprop12 A local, model-agnostic image-generation studio for Apple Silicon running locally and fully powered by MLX.

Here is using Ernie-Image Turbo, Krea 2 Turbo and CyberRealistic Z (Z-Image Turbo LoRA) to recreate the original image created with GPT-Image 2. 
Good results no?

## 2026-07-12 (https://x.com/ivanfioravanti/status/2076345065203527940)

DwarfStar will soon be a little faster on M1-M4 devices thanks to GPT-5.6 Ultra, some directions to it and a lot of patience and encouragement (YOU CAN DO IT! 🤣)

In the video:
- top new Metal Kernel ~39 toks/s
- bottom current version ~36 toks/s

Final checks and full ds4-eval then I'll create PR @antirez 💪

## 2026-07-12 (https://x.com/ivanfioravanti/status/2076377207123886432)

GPT 5.6 Sol turned my Daylight DC-1 into Tom Riddle's diary from Harry Potter.  
My prompts fade, OCR with Apple's Vision framework + Gemma 4 31B + Ollama respond. 
Everything locally on my Macbook.
Watch till the end and volume up!

Magical and inspired by @MaximeRivest work 🙏 https://t.co/qqPpGgl1Go
