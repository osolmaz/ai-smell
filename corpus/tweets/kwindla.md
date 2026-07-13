# @kwindla — long-form tweets

## 2026-03-11 (https://x.com/kwindla/status/2031777618274763095)

NVIDIA Nemotron 3 Super launches today! We've been building voice agents with Super's pre-release checkpoints and running all our various tests and benchmarks.

Nemotron 3 Super matches both GPT-5.4 and GPT-4.1 in tool calling and instruction following performance on our realtime conversation, long context, real-world benchmarks. GPT-4.1 is the most widely used LLM today for production voice agents. So an open model that performs as well as GPT-4.1 on hard, voice-specific benchmarks is a big deal.

(Side note: we don't think a benchmark "tells the story" about a model's voice agent performance unless it tests model correctness across at least 20 human/agent conversation turns.)
  
The Nemotron models are *fully* open: weights, data sets, training code, inference code.

 Nemotron 3 Super is 120B params, with a hybrid Mamba-Transformer MoE architecture for efficient inference. You can run it on NVIDIA data center hardware or on a DGX Spark mini-desktop machine.
  
 1M token context.

Blog post with full benchmarks, thinking budget notes, inference setup on @Modal, and where we think this goes next. 👇

## 2026-06-04 (https://x.com/kwindla/status/2062639707079524705)

NVIDIA released a big, capable, fast, open source model today. This model, Nemotron 3 Ultra, is the first open model that saturates our aiewf-evals benchmark.
![HJ_19m9XMAAtcla.png](media/2062639707079524705/HJ_19m9XMAAtcla.png)
For voice agents, software copilots, and robotics, latency is just as important as model intelligence. Nobody will talk to a voice agent that takes 5 seconds to respond. If a software copilot or a robot can't react in nearly realtime, it's not useful.
We think about this as a Pareto frontier, with latency per-turn on one axis and per-turn success on the other axis.
![HJ_1Yl-WcAAKmQr.jpg](media/2062639707079524705/HJ_1Yl-WcAAKmQr.jpg)
Nemotron 3 Ultra scores 100% on the aiewf-evals voice agent benchmark, with a thinking budget of 128 tokens. Median latency is 541ms, running on NVIDIA B200 hardware. This is a new, and very exciting, point on the latency/intelligence Pareto frontier.
It's worth noting that this 541ms latency is not just "time to first token." It's the time it takes for the model to output the first token that we can stream/show/speak to the user — "time to first non-thinking token."
The latency we care about, for models that do "thinking," is a combination of raw TTFT (time to the first token, period, which will usually be a thinking-sequence token) and generation speed (tokens per second).
Speed is critical for the voice inference loops in voice agent systems. But speed is also important for many of the other subagents we build. Computer use, dynamic UI generation, information lookup and summarization -- all of these tasks are far, far more useful for human-in-the-loop use cases if they run quickly enough that the user can stay engaged and in the flow.
We always push hard before a big model release to optimize TTFT and single-user throughput so we can see how well a new model is likely to perform for the realtime AI use cases we focus on.
Nemotron 3 Ultra is fast on launch day! Really, really great work by the team at NVIDIA getting this model working great in open source inference stacks.
I've been experimenting with this model mostly using vLLM, deploying to 8xB200 boxes on Modal. Here's the optimal low-latency configuration as of today.
- 260ms TTFT (raw first token)
- 380 tokens/second per-request throughput
Note that for both multi-token prediction and full prefix caching to work, you'll need to apply a six-line patch to vLLM. Without this patch there's a "state space drift" that impacts inference accuracy for long-context requests.
> # 6-line patch to vllm/v1/core/single_type_kv_cache_manager.py (MTP × mamba prefix-cache fix).
# In the vllm-openai:v0.22.0 image it lives at:
#   /usr/local/lib/python3.12/dist-packages/vllm/v1/core/single_type_kv_cache_manager.py
# Apply the diff from https://github.com/vllm-project/vllm/pull/43650 (or our patch_vllm_mtp_cache_fix.py)
Environment variables:
> export VLLM_WORKER_MULTIPROC_METHOD=spawn
export VLLM_LOGGING_LEVEL=INFO
export SAFETENSORS_FAST_GPU=1
export TOKENIZERS_PARALLELISM=false

# Modal-specific: persist torch.compile/FlashInfer cache off the read-only image dirs.
# Outside Modal you can drop this (defaults to ~/.cache).

export VLLM_CACHE_ROOT=/cache/vllm
Full server command:
> vllm serve "$MODEL" \
  --host 0.0.0.0 --port 8000 \
  --served-model-name nemotron-3-ultra \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --kv-cache-dtype nvfp4 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.90 \
  --mamba-cache-dtype float16 \
  --mamba-ssm-cache-dtype float32 \
  --mamba-backend triton \
  --max-num-seqs 16 \
  --max-num-batched-tokens 32768 \
  --enable-chunked-prefill \
  --enable-prefix-caching \
   --mamba-cache-mode align \
    --reasoning-parser nemotron_v3 \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --async-scheduling \
    --no-enable-flashinfer-autotune \
    --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}' \
    --model-loader-extra-config '{"enable_multithread_load": true, "num_threads": 96}'
Here's a repo you should be able to just clone and then deploy to Modal from: https://github.com/kwindla/nemotron-3-ultra
@charles_irl has a great post on deploying Nemotron 3 Ultra to Modal using SGLang, if SGLang is your thing (or you just want to try both vLLM and SGLang): https://x.com/charles_irl/status/2062520838994416037
And here's the NVIDIA Nemotron 3 announcement post, with charts and graphs and a link to a fantastic technical report: https://x.com/NVIDIAAI/status/2062521325076299981

## 2026-06-04 (https://x.com/kwindla/status/2062640117383307340)

Looking at these numbers last night, I was realizing that I need to update the TTFT numbers for Nemotron 3 Super and Nemotron 3 Nano. The numbers in the aiewf-evals table are from the launch day for each of those models, and vLLM/SGLang have much better support now for hybrid/Mamba prefix caching, and more optimized kernels for Blackwell, now!

## 2026-06-07 (https://x.com/kwindla/status/2063712899168620801)

Join us on Tuesday at the AWS Builders Loft in San Francisco for a discussion of open-weight models on AWS.

I'll be talking about the NVIDIA Nemotron models and how we're evaluating, using, and customizing them for agentic use cases.

Registration link in the thread ... https://t.co/0x084Z5QHO

## 2026-06-23 (https://x.com/kwindla/status/2069414487287812556)

My favorite annual AI event is next week in San Francisco. Come hang out with me at the @aiDotEngineer World's Fair.

Go buy a ticket. Or, if you're a student, there's a great volunteer program.

The organizing team does a great job making the World's Fair a conference with great talks, an opportunity for deep-dive learning across multiple AI engineering domains, a gathering of people building the infrastructure for AI adoption, and an opportunity to see early what everyone will be talking about next year.

I'm doing a couple of talks. One on voice interfaces, with @neilzegh. And one about experimenting with new building blocks for "AI-native" software, software patterns for applications we couldn't have built at all before now and that we'll take for granted in a few years!

I get more requests than I can keep up with, via LinkedIn and email, to meet and talk about AI engineering, voice AI, and @pipecat_ai. Most of the year, my default response is, "I would love to but I can't, if you make a PR I'll try hard to look at it." AI Engineer World's Fair is the one time of year when I can say: if you'll be at the World's Fair, come find me. We'll geek out about what you're building and all the crazy ideas we both have!

## 2026-06-24 (https://x.com/kwindla/status/2069583286800674838)

I spend a lot of time thinking about the engineering building blocks for realtime AI. As the models we use get better, we do more things with them (and more *interesting* and complicated things). We upgrade our orchestration tooling and systems-level infrastructure to support these new use cases. Which gives us insight into what we'd like the next generation of models to do.

This co-design loop (to borrow from Jensen) of applications, orchestration, models, and infrastructure is great! We built the first generation of conversational voice agents with LLMs barely three years ago. Today, voice agents are deployed at scale by thousands of companies. That's possible because all of us working up and down the stack are listening to and learning from each other.

I'm so happy about this AssemblyAI release that bakes "context carryover" directly into the new Universal-3.5 Pro Realtime model and API.

A lot of the work we do in AI engineering boils down to context management. The speech to text, LLM, and text to speech models we use are amazing. But it takes a fair amount of engineering work to achieve production-level reliability.

We build state machines, multi-agent systems, subagents, do non-blocking compaction and summarization, and generally work hard to thread context through our voice agent pipelines to maximize agent performance. We need control over what context each model sees throughout each conversation.

This new AssemblyAI release is a big step forward in speech to text context management. If you're building voice agents, go check it out.

## 2026-06-24 (https://x.com/kwindla/status/2069819081511911696)

When I was in grad school, "Doctor Flemson or something" was one of our catch phrases. Funny only to us, but that's why you go to grad school, to find the people who share your obsessions and think the same niche jokes are funny.

That phrase is from the 1987 Apple "Knowledge Navigator" concept video. It's a great video. Squarely in the lineage of Vannevar Bush, J. C. R. Licklider, and Alan Kay, but prescient in its own right. The video shows a foldable tablet, a touch-screen interface, a conversational voice assistant with a strong personality and access to both personal and global information, realtime video generation, realtime computer vision, seamless video call integration, delegation of complex tasks for autonomous execution, and what we might today call "continual learning."

None of these ideas are particularly surprising to us in 2026. But Apple made this video 40 years ago. Before the Internet. Before most computer users had even seen a mouse, much less a touch screen.

What *will* be surprising to some people is that we can actually build this today. The team at @tavus re-created "Knowledge Navigator" using their conversational video agent tech stack and posted a video, captured in a single take.

"Re-interpreted" is probably an even better description of this project than "re-created." The original video features an academic (portrayed by an actor) preparing a lecture. The Tavus video captures actual use of this real personal assistant application: some recreational 3d printing, some vibe coding with Claude Code. "Let me model you a tapered adapter right now," delivered in my terrible version of a British accent, is my new catch phrase.

Response times are very fast, including the 3d model generation. Tavus worked with @cerebras on the video. I posted recently about how fast Kimi K2.6 is on Cerebras and how well the model does on my benchmarks. If you haven't spent much time with K2.6, it's worth watching the video just to get an intuitive sense of the speed, natural conversation dynamics, and structured data strength of this model.

I'm always, always impressed by the Tavus team. (After grad school, you move to San Francisco to find even more people who share your obsessions.) @hassaanraza wrote a wonderful, meditative blog post on the experience of building and using this new version of a knowledge navigator. Link in thread.

## 2026-06-25 (https://x.com/kwindla/status/2070144624694317421)

I've been updating the Voice AI and Voice Agents Guide. We're doing another print edition, for the AI Engineer World's Fair next week. 

We did the first version of the guide 17 months ago for the AI Engineer New York Summit. Some things have changed a lot in a year and a half! The biggest change is that there are now open models we can use for production voice agents.

In fact, open models are strictly better than any of the proprietary models today, when taking into account TTFAT (time to first answer token).

Latency is critical for conversational voice. We need TTFAT times faster than ~700ms to use a model in production. And we care a lot about the P95 metric for latency (not just the P50).

Most of the LLMs released in the last year are "thinking" models, models designed to emit thinking tokens before generating an answer.

Thinking tokens take time to produce, so they increase the answer latency significantly compared to earlier models that just generated answer tokens immediately. Latency goes up in an unpredictable way, as well. (The spread between P50 and P95 increases.)

The best open models today are thinking models, just like the best closed models are. But with open models we can optimize inference for fast TTFAT, by trading off against batch throughput efficiency, or by configuring thinking budgets in specific ways, by configuring our hardware stack differently, or by tuning our low-level inference code with TTFAT micro-optimizations.

So our voice agent benchmarks now show two different Pareto frontiers: one for open models and one for closed models. And the open model frontier is ahead of the closed model frontier. Few people would have predicted this, 17 months ago when we wrote the first version of the guide.

Lots of caveats, of course. Claude Opus 4.8 and GPT-5.5 are still the best models from a pure "intelligence" perspective. For a given hard problem, they will give you a better answer than any open model, most of the time. And there are not yet any inference providers serving TTFAT-optimized open models that saturate our voice benchmarks in the same flexible, pay-as-you-go way that Anthropic and OpenAI serve Claude and GPT models.

Of course, Anthropic and OpenAI (or AWS and Azure) could offer TTFAT-optimized inference endpoints. (This is clear from first principles, but also: Claude voice mode is very, very fast!) So far, though, they haven't done so.

But if you have significant inference volume and an engineering team that is capable of running inference clusters, using open weights models for production voice agents is now a real option.

## 2026-07-02 (https://x.com/kwindla/status/2072524488701599972)

.@neilzegh and I are doing a fireside chat Thursday morning at @aiDotEngineer on Expo Stage 3 SW at 11:40.

The theme is "Voice is the universal interface." And we agree about that.

But the idea is to throw hot takes back and forth: from the different perspectives of ML research and AI engineering. It's the "AI Engineer" World's Fair, though, so obviously all my hot takes are the correct ones.

## 2026-07-10 (https://x.com/kwindla/status/2075443503174402259)

New realtime transcription model from the team at @cartesia.

A very large number (and wide variety) of production voice agents use Cartesia text-to-speech models. The company's voice models score very high in both human and quantitative testing. Now there's a similarly high-scoring speech-to-text model from Cartesia, too.
