# @vllm_project — long-form tweets

## 2026-05-06 (https://x.com/vllm_project/status/2052051210530914510)

🚀 Excited to be the exclusive day-0 launch partner for @lightseekorg's Tokenspeed project!

We've integrated Tokenspeed's MLA library, optimized specifically for agentic workloads with long context and multi-turn, purpose-built for Kimi 2.5/2.6 and DeepSeek R1 on NVIDIA Blackwell hardware! 

Try it out today with our preview image - nightly support coming soon!

## 2026-05-24 (https://x.com/vllm_project/status/2058358072020779391)

Thanks to the community report, we recently identified a PR https://t.co/QWboSmskkF that attempted to solve a non-existent issue and was submitted as part of a “PR training” workflow for resume building.

The contributor involved has been banned from the vLLM community.

This kind of low-signal contribution increases maintainer review overhead and creates unnecessary operational costs for open-source projects.

As AI coding agents make generating large volumes of small PRs increasingly cheap, open-source communities will need to explore new ways to preserve contribution quality and reviewer trust.

While we are investigating how to deal with AI slop, we continue to highly value contributions from real users solving real production problems.

If you have an important contribution that has not yet received maintainer attention, please email us at:

pr-review-request@vllm.ai

Using a verifiable company or university email, include:
- your production or research use case
- the problem you encountered
- how your contribution addresses it

This helps us better prioritize impactful contributions while keeping the vLLM community open and collaborative.

As AI makes virtual contributors look increasingly real, authentic human collaboration matters more than ever.

vLLM’s mission remains unchanged: to make LLM inference easy, fast, and cheap for everyone — and we will continue working toward that goal.

## 2026-05-30 (https://x.com/vllm_project/status/2060751889336291535)

vLLM v0.22.0 is out! 459 commits from 230 contributors (63 new). 🎉

Highlights: DeepSeek V4 hardening (NVFP4 fused MoE, full+piecewise CUDA graph, ROCm support), experimental Rust frontend in-Tree, batch-invariant Cutlass FP8 (28.9% lower e2e latency), Model Runner V2 advances, multi-tier KV cache offloading.

Thread 👇

## 2026-05-30 (https://x.com/vllm_project/status/2060751892268122531)

Engine core:

🐋 DeepSeek V4 matured into a dedicated package: NVFP4 fused MoE, full + piecewise CUDA graphs, MTP speculative decoding on ROCm, more fused kernels and ROCm parity fixes
🦀 Experimental Rust frontend moved in-tree 🚀
🛠️ Model Runner V2: oracle selection for Qwen3 dense by default, sleep-mode weight reload, `update_config`, shared KV-cache layers; auto-falls back to MRv1 when KV connectors are present
💾 KV cache offloading: Multi-tier support with Python filesystem secondary tier, DeepSeek V4 support, Mooncake disk offloading

## 2026-05-30 (https://x.com/vllm_project/status/2060751894994436327)

Hardware & performance:

⚡ Batch invariance: Cutlass FP8 path → 28.9% end-to-end latency improvement, compile-mode support on SM80, NVFP4 Cutlass linear path
🟢 NVIDIA Blackwell: FlashInfer MoE + FP4 GEMM for SM120/121; per-tensor FP8 CUTLASS on SM12.1
🔴 AMD ROCm: DeepSeek V4 functionality gains, flash sparse MLA Triton kernels, gluon paged MQA logits
💻 CPU / RISC-V: RVV-optimized attention kernels, fused GDN for AMX, experimental Triton + MRv2

## 2026-05-30 (https://x.com/vllm_project/status/2060751897733255534)

Models, serving, and what to know before upgrading:

🆕 New architectures: MiniCPM-V 4.6, InternS2 Preview, OpenVLA
🦅 Spec decode: custom callable proposers; Gemma3/Gemma4 multi-GPU fixes + batched vision encoders
🔧 Tool calling improvements across multiple model families

⚠️ Breaking:
• Removed deprecated `get_tokenizer` and `resolve_hf_chat_template` locations
• Eliminated deprecated MLA prefill arguments
• Cleaned up dead CUDA kernels and code

🙏 Thanks to all 230 contributors this cycle (63 new).

📖 Full release notes → https://t.co/fUAdzeCogu

## 2026-06-02 (https://x.com/vllm_project/status/2061621691995005301)

🎉 Congrats to @JetBrains on Mellum2-12B-A2.5B-Thinking, an open-source 12B MoE that activates just 2.5B params, handling both natural language and code with a 128K context.

Mellum2 runs natively in vLLM from day 0, with reasoning parser and tool calling for agentic workflows.

🔗 https://t.co/72E6HDOHNf

## 2026-06-08 (https://x.com/vllm_project/status/2064013506882703421)

🎉 Meet vLLM-Omni v0.22.0, a major upgrade for omnimodal world models and production-grade multimodal serving.

🌍 Day-0 @NVIDIAAI Cosmos 3 world models: text, image, audio, video, and action, in and out.
🤖 Robot serving: DreamZero + OpenPI realtime API.
🎙️ Production TTS: Qwen3-TTS, Qwen3-Omni, VoxCPM2 and more.
🎨 Faster image/video/diffusion: Wan 2.2, HunyuanVideo 1.5, LTX-2.3.
⚡ Broader quantization (FP8/INT8, MXFP4/MXFP8, W4A16, ModelOpt) and hardware coverage.

339 commits, 124 contributors, 52 of them new. Thank you all. 🙌

🔗 https://t.co/76ttSM6FHs

## 2026-06-15 (https://x.com/vllm_project/status/2066401115089121653)

Hardware & performance:

🟢 NVIDIA: FP8 FlashInfer attention for ViT, Triton MoE on Hopper by default, CUTLASS FP8 scaled-mm padding bypass (+20%), MoE-permute buffer pre-alloc (+9–14%), NUMA auto-binding on DGX B300
🔴 AMD ROCm: ROCm 7.2.3, native W4A16 + fused-MoE W4A16 kernels for RDNA3 (gfx1100), AITER top-k/top-p sampler by default, attention-sink support in AITER FA
🔵 Intel XPU: vllm-xpu-kernel v0.1.7, block FP8 MoE, a DeepSeek-V4 attention decode path, transparent sleep mode
💻 CPU & more: zentorch-accelerated W8A8/W4A16 on AMD Zen CPUs, RISC-V RVV WNA16 helpers, a PowerPC SHM communicator, an arm64 CI image

## 2026-06-16 (https://x.com/vllm_project/status/2066950636428775693)

🎉 Day-0 support for in vLLM, available today in v0.23.0!

Congrats to @Zai_org on GLM-5.2, a flagship model built for long-horizon coding agents.

✨ 1M-token context, built to hold project-scale engineering work in a single run
✨ Tuned for long-horizon coding: large-scale implementation, automated research, and performance optimization
✨ One task can carry a full dev workflow, from requirements to a deployable product across platforms
✨ Client-side and mobile engineering, including an on-device debugging loop

Try it out running it on vLLM today:
🔗 https://t.co/tRduouqn6e

## 2026-06-18 (https://x.com/vllm_project/status/2067629972941132269)

🎉 Congrats to @poolsideai on Laguna M.1, a new open-weights agentic coding model. Day-0 support landed in vLLM v0.21.0.

🧠 70-layer sparse MoE: 225B total params, 23B active per token, 256K context
🔀 256 experts with top-k=16 routing, built for long-horizon agentic coding
🛠️ Native interleaved reasoning between tool calls, toggleable per request, Apache 2.0

Recipe 🔗 https://t.co/lDG8poco5g

## 2026-06-23 (https://x.com/vllm_project/status/2069494027431649404)

🙏 Thanks to the @NVIDIAAI team for highlighting DFlash support on vLLM!

With DFlash speculative decoding, swapping EAGLE-3 for a DFlash checkpoint is a config-only change — no code edits needed.

It runs through the open-source Speculators library, which links the DFlash drafter to the target model's hidden states in the vLLM inference path.

On Gemma-4 31B on a single Blackwell Ultra GPU, this delivers up to 5.8x higher throughput at the same concurrency over autoregressive decoding:
🧮 Math500 — 5.8x
➕ GSM8K — 5.3x
💻 HumanEval — 5.6x
🐍 MBPP — 4.4x

Read the blog here! 👇

## 2026-06-26 (https://x.com/vllm_project/status/2070364532296536346)

Excited to see @cohere open-source how they use AI coding agents to maintain their vLLM fork. 🙌

Keeping a long-lived fork in sync is tricky. Their agent treats it as a control loop: rebase onto each upstream release, run tests, diagnose, fix, repeat until green. Weeks of work down to days.

Bonus: the skills are open source (cohere-ai/vllm-skills) and the agent's fix went back upstream for everyone. 🔧

Worth a read 👇
https://t.co/y9xudrkqw9

## 2026-06-26 (https://x.com/vllm_project/status/2070569806940848328)

GLM-5.2 in NVFP4 is ready to serve in vLLM 🚀

@NVIDIAAI's official NVFP4 checkpoint of GLM-5.2 on Blackwell cuts the memory footprint vs FP8 while matching its accuracy across reasoning, coding, and long-context benchmarks.

Serve it today with:
vllm serve nvidia/GLM-5.2-NVFP4

🤗 https://t.co/utHk49BULz

## 2026-06-28 (https://x.com/vllm_project/status/2071116236591948227)

🎉 Unlimited-OCR from @Baidu_Inc now runs in vLLM. One-shot parsing of entire books with constant KV cache, powered by Reference Sliding Window Attention (R-SWA).

🧠 R-SWA keeps KV cache fixed throughout decoding — no memory blowup, no slowdown, no matter how long the output gets.
📄 Transcribe 40+ pages in a single forward pass under a 32K context budget, with remarkably low edit distance even at scale.
🪶 35% faster than DeepSeek-OCR at 6K output tokens, with fully constant TPS and GPU memory.

🔗 Recipe: https://t.co/gBAvAP7vyG
🤗 Weights: https://t.co/9hnfOt3Ab7 

🙏 Thanks to the @BaiduAI_News team for the collaboration.

## 2026-06-29 (https://x.com/vllm_project/status/2071427198947639757)

🎙️ Serving TTS isn't the same problem as serving an LLM. It has to hit a first-audio budget of a few hundred ms, keep audio continuous across streaming chunks, and sustain enough concurrent streams per GPU to keep serving cost down. It's also a multi-stage pipeline where each stage bottlenecks differently, so no single recipe carries across models. vLLM-Omni TTS team tuned a different lever for each of four TTS models:

🗣️ Qwen3-TTS: decouple connector chunking from the Code2Wav decode window, batch the Stage-0 decode preprocessing. +61.5% audio throughput on H20×2, P99 latency nearly halved.
🌊 VoxCPM2: whole-forward torch.compile, plus CFM/LocDiT decode-tail batching across requests. +172% audio throughput.
🎚️ Higgs Audio V3: move the multi-codebook decode state machine into GPU-resident tensors. 2.7x speedup.
🐟 Fish Speech S2 Pro: a model-specific q_len=1 Triton attention kernel for the pure-decode path.

Full engineering deep-dive on how we picked each lever:
🔗 https://t.co/ZVROwJwYoT

## 2026-06-29 (https://x.com/vllm_project/status/2071483552106233993)

Great to see the @NVIDIAAI Nemotron team put out a step-by-step guide for self-hosting Nemotron-3-Ultra 550B without a datacenter. Four compact DGX Spark boxes pool into a single OpenAI-compatible endpoint, served from vLLM's official out-of-the-box container.

If you're building a private cluster of your own, don't miss this guide:
🔗 https://t.co/6kxdG5Ztde

🤖 Then wire that endpoint into your agent workflows, all on hardware you own.

## 2026-06-29 (https://x.com/vllm_project/status/2071736211048452141)

🥂 Join us for a happy hour during @aiDotEngineer World's Fair this Thursday 7/2 in San Francisco, co-hosted with @inferact and @novita_labs!

Casual conversation on open weight models, inference, and infra with fellow builders, founders, and researchers.

📍Hosted at the @inferact office , no conference ticket required!

RSVP here:
https://t.co/5c7ZBcExhM

## 2026-06-30 (https://x.com/vllm_project/status/2072096072676323389)

We're resuming the vLLM meetup series! Teaming up with @CrusoeAI  for an evening meetup on open source inference in San Francisco🥂 

The event features:
🔹 Talks from vLLM core maintainers
🔹 Talks from Crusoe on running vLLM in production
🔹 Drinks, snacks, and time for chatting with the key builders in AI infrastructure

📍 a16z, San Francisco: 180 Townsend St
🗓 Tuesday, July 21 

Spots are limited, so register early!
RSVP: https://t.co/8JyZau4srI

## 2026-07-01 (https://x.com/vllm_project/status/2072159562992619991)

vLLM v0.24.0 is out! 571 commits from 256 contributors (77 new). 🎉

Highlights: MiniMax-M3 support (FP8/MXFP4 + broad AMD tuning), DeepSeek-V4 keeps maturing (FlashInfer sparse index cache, prefill chunk-planning, now on SM120), Model Runner V2 now handles quantized models by default, a new unified Streaming Parser Engine for tool-calls + reasoning, DiffusionGemma, DeepEP v2 for wide expert parallelism, and a maturing Rust frontend.

Thread 👇

## 2026-07-01 (https://x.com/vllm_project/status/2072159565991628834)

Engine core & models:

🆕 New models: MiniMax-M3 (FP8/MXFP4/sparse GQA + extensive AMD/ROCm tuning), DiffusionGemma (incl. a CPU path), Hierarchical Reasoning Model, OpenMOSS
🐋 DeepSeek-V4 keeps maturing: a FlashInfer sparse index cache (2–4% TTFT), prefill chunk-planning (+4% E2E throughput), a cluster-cooperative topK kernel for low latency, now enabled on SM120 alongside GLM-5.1, plus XPU + ROCm attention/MoE paths
🛠️ Model Runner V2: now supports quantized models by default, enables GraniteMoE by default, migrates Qwen + DeepSeek-V2 MoE, and adds DFlash speculative decoding
🔌 Streaming Parser Engine: one engine for tool-call + reasoning parsing across Qwen3, MiniMax-M2, GLM-4.7/5.1/5.2, and Nemotron V3

## 2026-07-01 (https://x.com/vllm_project/status/2072159568357134523)

Hardware & performance:

🟢 NVIDIA: SM90 CUTLASS FP8 odd-M via swap_ab (180–290% kernel speedup), tuned fused_moe FP8 for Qwen3-Next-80B on H100 (+25%), native DSA indexer decode on SM100, and the final kernel migration onto the libtorch stable ABI
🔴 AMD ROCm: Torch 2.11, fused all-reduce + RMSNorm + per-group FP8 quant, a fused softplus-sqrt-topk MoE router under AITER, and a DSv4 flash-decode split-K kernel
🔵 Intel XPU: sequence-parallel support, torch-xpu 2.12, vllm-xpu-kernels v0.1.10, W4A16 int4 MoE, and DeepSeek-V4 attention/MoE paths
💻 CPU & more: 2.5× faster ASR CPU preprocessing, CPU W4A16 INT4 MoE, cgroup memory-aware KV sizing, RISC-V oneDNN INT8

## 2026-07-01 (https://x.com/vllm_project/status/2072413378669134306)

🚀 Qwen3.6-27B-NVFP4 is inference ready with vLLM on NVIDIA Blackwell GPUs.

This checkpoint is optimized for Blackwell and reduces GPU memory requirements by ~2.5x for local AI with open-source models.

🧠 27B params, Hybrid Attention
📊 NVFP4 evals: 86.3 on MMLU Pro, 85.5 on GPQA Diamond
🛠️ Exclusively supported on vLLM as the runtime engine

Get started from the Hugging Face checkpoint: https://t.co/TDA75Mqam6

## 2026-07-02 (https://x.com/vllm_project/status/2072545387639189798)

🚀 @deepseek_ai's DSpark speculative decoding now runs natively in vLLM!

What it is: a semi-autoregressive drafter that proposes several tokens in parallel with non-causal sliding-window attention, then verifies them in a single pass. Output stays identical, decoding takes fewer steps.

How vLLM runs it: it reuses the existing SparseMLA backends instead of custom attention kernels, captures the full draft backbone and sampling loop in one CUDA graph, and works with prefix caching and FP8 KV cache.

Performance on DeepSeek-V4-Pro-DSpark (verified on NVIDIA 8×B300 GPUs):
- ~250 tokens/s at batch size 1
- average acceptance length ~5
- 12-42% higher acceptance than MTP across draft depths

Run with vLLM nightly today:
vllm serve deepseek-ai/DeepSeek-V4-Pro-DSpark -tp 8 --trust-remote-code --kv-cache-dtype fp8 --speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"greedy"}'

DSpark Core PR: https://t.co/Yyo6rYX4jG

Thanks @deepseek_ai for open-sourcing DSpark, and to @NVIDIAAI and the vLLM community for landing it! 🙏

## 2026-07-02 (https://x.com/vllm_project/status/2072545389434331604)

And it's not locked to DeepSeek's checkpoints. 🧩

The Speculators library (https://t.co/pLpZP4xqfA) lets you train and package DSpark draft models in a standard, HF-compatible format that vLLM loads directly. Already validated on Qwen3-8B and GLM-5.2. Run it on vLLM nightly now:

vllm serve zai-org/GLM-5.2-FP8 -tp 8 --speculative-config '{"method":"dspark","model":"RedHatAI/GLM-5.2-speculator.dspark-preview","num_speculative_tokens":7,"attention_backend":"FLASH_ATTN","draft_sample_method":"greedy"}'

speculators support PR: https://t.co/ZIuOMe7zP1

Thanks to the @RedHat_AI team for the Speculators integration! 🙏

## 2026-07-03 (https://x.com/vllm_project/status/2072942203966812438)

🎙️ @Alibaba_Qwen's Qwen3-Omni listens, reasons, and talks back. Serving that in real time is a pipeline problem, not a single model: a multimodal Thinker, then Talker → Code2Wav for the speech.

Each stage bottlenecks differently, so the wins come from optimizing them layer by layer. One neat trick: under load, replicate only the two speech stages and let the heavy multimodal Thinker run once. At high concurrency that lands first audio in ~0.6s instead of ~6s, speech faster than real time, and ~5.4x the throughput on the same GPUs.

Built with @AntGroup's Super Computing Technology (SCT) team and the vLLM-Omni team. The blog breaks down the full stack, one bottleneck at a time 👇
🔗 https://t.co/aKWZdhNzMU

## 2026-07-06 (https://x.com/vllm_project/status/2073954865374543910)

Congrats to @MistralAI on Leanstral 1.5! 🎉

An Apache-2.0 Lean 4 proof agent that punches way above its size:
🧩 MoE: 119B total, just 6B active
 📐 100% on miniF2F 
 🎓 New SOTA on FATE-H (87%) & FATE-X (34%)
 ⚡ 587/672 on PutnamBench at ~$4/problem

Read the blog below or serve it on vLLM today!
https://t.co/XQIionVYPC

## 2026-07-06 (https://x.com/vllm_project/status/2074147504254517529)

🎉 @TencentHunyuan's Hy3, the full release following the Hy3 Preview, runs natively in vLLM from day 0, with tool-call and reasoning parsers and MTP speculative decoding, verified on @NVIDIA and @AMD hardware.

Hy3 is a Mixture-of-Experts model built for agentic workflows, coding, and long-horizon reasoning, and it's Apache 2.0. 295B total parameters with just 21B active, 192 experts with top-8 routing, GQA attention, a 256K context window, and a 3.8B MTP layer for speculative decoding. Ships in BF16 and FP8.

Full recipe (exact flags, FP8, MTP, hardware): https://t.co/N4yn1LlgjZ

## 2026-07-08 (https://x.com/vllm_project/status/2074916256600490385)

Big news from @hmellor_  + @huggingface team🙌! 

In v0.25.0 the Transformers modeling backend hits parity with hand-written vLLM models.

Now 450+ transformers architectures run in vLLM at native speed with zero porting. Integrate once with transformers to get vLLM's fused kernels, torch.compile, and CUDA graphs for free.

Read about the changes below 👇

## 2026-07-09 (https://x.com/vllm_project/status/2075063247837757474)

🎉 Congrats to the @MosiAI_Official team on MOSS-Transcribe-Diarize-0.9B, an open, end-to-end model for multi-speaker long-audio transcription, with day-0 support in vLLM.

Most setups chain ASR + diarization + alignment (WhisperX-style). This one does all three in a single generative pass. It transcribes the speech, tags who is speaking, and emits timestamps together:

[0.11][S01] Good morning![1.03]
[1.11][S02] Morning, guys![1.34]

A Whisper-style audio encoder feeds a Qwen3-style causal decoder, so a recording up to ~90 minutes goes in as one shot, no chunking or stitching. Keyword biasing lets you prime names, product codes, and domain terms so proper nouns come out right. Useful for meeting notes, interviews, call-center QA, and podcast transcription.

🔗 https://t.co/tTBqjY3vrL

## 2026-07-12 (https://x.com/vllm_project/status/2076217859928453275)

vLLM v0.25.0 is out! 558 commits from 232 contributors (64 new). 🎉

Highlights: Model Runner V2 is now the default for all dense models, the legacy PagedAttention implementation is retired, the Transformers backend now runs as fast as native vLLM, a new unified Streaming Parser Engine, universal speculative decoding across heterogeneous vocabularies (TLI) plus new DSpark and DFlash drafters, and new models including Hy3 and Unlimited OCR.

Thread 👇
