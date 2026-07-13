# @TheAhmadOsman — long-form tweets

## 2026-04-07 (https://x.com/TheAhmadOsman/status/2041331757329285589)

If you’re running models locally, thinking “bigger memory pool = better AI box” falls apart the moment you care about actual speed.
Capacity decides whether the model fits.
Bandwidth decides whether the box feels alive or like it’s decoding through wet cement to produce 3 tokens per second.
That is why a 32GB RTX 5090 and RTX PRO 6000 can absolutely outrun a much larger unified-memory machine, while a Mac Studio M3 Ultra, DGX Spark, or Strix Halo box can still be the right answer when the model simply will not fit on a normal GPU (but will be a lot slower, and not help for multi-agentic workflows).
There’s a better way to think about it:
> Local AI hardware = capacity × bandwidth × software stack
Capacity tells you what fits.
Bandwidth tells you how hard the box can breathe.
The software stack tells you how much of the spec sheet you can actually cash out.
That is the mental model.
> Not “AI PC.”
Not “NPU TOPS.”
Not whatever crime against engineering was committed in a marketing deck this week.
## The Hardware Number You Should Actually Care About
Especially in the age of agents.
Memory bandwidth is not tokens per second.
But it is the cleanest first-pass way to separate local AI hardware into real performance tiers before you waste a week arguing with someone posting screenshots from a single prompt demo.
Here’s the current landscape:
1.8 TB/s class
- RTX PRO 6000 Blackwell, RTX 5090 → 1792 GB/s
800 GB/s class
- Mac Studio M3 Ultra → 819 GB/s
450–650 GB/s class
- Mac Studio M4 Max → 546 GB/s
- MacBook Pro M5 Max → 460–614 GB/s
- AMD Radeon AI PRO R9700 → 640 GB/s
- Tenstorrent Blackhole p150 → 512 GB/s
250–300 GB/s unified-memory class
- DGX Spark → 273 GB/s
- Mac mini M4 Pro → 273 GB/s
- Ryzen AI Max / Strix Halo → 256 GB/s
Thin-and-light AI PC class
- MacBook Air M5 → 153 GB/s
- Snapdragon X Elite → 135 GB/s
- Intel Lunar Lake → 136 GB/s
- Snapdragon X2 Elite → 152–228 GB/s
If you remember nothing else, remember this:
- capacity decides what fits
- bandwidth decides how hard it can breathe
- software decides how much of that you actually see
That is the whole game.
## Side Note: The Memory Tax People Mix Up
A lot of people collapse capacity and bandwidth into one blob.
That is how you end up making terrible hardware takes with supreme confidence.
A 32GB RTX 5090 and a 96GB RTX PRO 6000 Blackwell both have the same bandwidth.
But they live in completely different worlds once model size enters the chat.
> A DGX Spark gives you 128GB unified memory at 273 GB/s.
A Ryzen AI Max system can expose ~96GB as GPU memory.
A Mac Studio M3 Ultra goes up to 512GB at 819 GB/s.
Same topic.
Wildly different tradeoffs.
So no, bandwidth is not the whole story.
But it is the fastest way to stop being confused.
## What This Looks Like in Practice
Below ~150 GB/s, you are in thin-and-light territory.
That does not mean useless.
It means stop pretending it’s competing with workstation GPUs.
> Around 250–300 GB/s → unified memory starts getting interesting.
Around 450–650 GB/s → serious workstation tier.
At 800+ GB/s → expensive, powerful, and fun.
Local AI in 2026 is not one market.
It is five different markets pretending to be one.
## Discrete GPU Reality: Still the Bandwidth Kings
If the model fits, or you pool GPUs via NVLink (now mostly server-side) or Gen 5 PCIe and use Tensor Parallelism, discrete GPUs still dominate. This applies especially to NVIDIA GPUs given the wide software support.
- RTX PRO 6000 Blackwell → 96GB @ 1792 GB/s
- RTX 5090 → 32GB @ 1792 GB/s
- RTX 4090 → 24GB @ 1008 GB/s
What about AMD GPUs?
- RX 7900 XTX → 24GB @ 960 GB/s
- Radeon PRO W7900 → 48GB @ 864 GB/s
- AI PRO R9700 → 32GB @ 640 GB/s
Intel?
- Arc Pro B65 → 32GB @ ~608 GB/s
- Arc Pro B60 → 24GB @ ~456 GB/s
GPUs win because they can drink from a firehose.
They lose when the model doesn’t fit.
## Apple Reality: OK Bandwidth + Capacity Together
Apple’s entire story is:
> not the fastest, but usable
- Mac mini M4 → 120 GB/s
- MacBook Air M5 → 153 GB/s
- Mac mini M4 Pro → 273 GB/s
- MacBook Pro M5 Pro → 307 GB/s
- M5 Max → up to 614 GB/s
- Mac Studio M3 Ultra → 819 GB/s + up to 512GB memory
That last one is the key.
Apple wins when:
- you want one box
- you want silence
- you want stupid amounts of memory
- you don’t want to shard across GPUs
It loses when raw tokens/sec & concurrency matter more than everything else.
## DGX Spark: Coherent Memory + CUDA, Not a Bandwidth Monster
DGX Spark:
- 128GB unified memory
- 273 GB/s
- NVIDIA stack
That bandwidth is not impressive.
The coherent memory + software stack is.
It’s a developer appliance.
Not a raw performance monster. It has NVFP4 support, which gives it an advantage, but that is yet to mature.
## Strix Halo / Ryzen AI Max: The First Real x86 Contender
This is an interesting one.
- 256-bit LPDDR5X
- up to 128GB memory
- ~256 GB/s bandwidth
- up to ~96GB usable as GPU memory
This is also where Framework Desktop is interesting.
## The AI PC Trap
Most “AI PCs” are still bandwidth-starved.
- Snapdragon X Elite → 135 GB/s
- Intel Lunar Lake → 136 GB/s
- MacBook Air M5 → 153 GB/s
- Snapdragon X2 Elite → up to ~228 GB/s
That’s fine for:
- small models
- assistants
- edge workloads
It is not:
- 9B Dense model playground territory
- serious multi-agent workloads
- long-context stress testing
Physics still applies.
## Tenstorrent and the Wildcards
Tenstorrent:
- Wormhole n300 → 24GB @ 576 GB/s
- Blackhole p150 → 32GB @ 512 GB/s + 800G interconnect
Fully OSS stack. I am excited or this one to mature and hope they go on to become a strong contender in the AI space. We need more full opensource stacks.
They are real options depending on your stack and goals.
## Why Bigger Boxes Still Feel Slow
Because fitting ≠ serving.
Even if it fits, you still pay for:
- bandwidth during decode
- KV cache growth
- dequantization
- batching + concurrency
- scheduler quality
- framework overhead
This is why:
> “it runs” = demo “it serves” = system design
## Multi-GPU?
More GPUs ≠ linear scaling.
You are now buying:
- interconnect (PCIe vs NVLink vs RDMA)
- topology
- sync overhead
- software maturity
## The Only Mental Model That Matters
There is no giant chart you need to memorize.
There is just this:
1. What must fit?
2. What bandwidth tier do I need?
3. What software stack can actually deliver it?
Blunt version:
- NVIDIA → fastest raw speed
- Apple Ultra → biggest one-box memory
- Strix Halo → first real x86 unified-memory play
- DGX Spark → coherent NVIDIA appliance
- AMD / Intel Arc → rising alternatives
- Tenstorrent → fully opensource stack
Once you internalize this, you stop asking:
“Which hardware is best?”
You start asking:
“Which bottleneck am I buying?”
That is the real question.
Until next time.

## 2026-04-09 (https://x.com/TheAhmadOsman/status/2042270126838358204)

running Qwen3.5 397B MoE (17B active/token)

on 4x DGX Sparks in FP8 (~400GB)

&gt; OpenCode driving
&gt; agent exploring its own config
&gt; probing all 4 Sparks (via ssh) + reporting thermals
&gt; inspecting how vLLM is serving it
&gt; collecting + analyzing its own stats

local AI is awesome https://t.co/yPWSbSKto8

## 2026-05-13 (https://x.com/TheAhmadOsman/status/2054602409243271250)

This is Alex Finn

He’s costed so many people their hard earned money during his Mac mini grift

Now he’ll reuse the same script for the DGX Spark

He doesn’t know how to highlight any hardware strengths/weaknesses

Zero substance or knowledge of local AI

Go grift something else https://t.co/c1MsGukUy9

## 2026-05-19 (https://x.com/TheAhmadOsman/status/2056810506153849107)

I didn’t go to Stanford

I grew up in Egypt

Worked my ass-off towards an education in Europe

+ Degrees in Computer Science &amp; Data Science in the US

This account is my track record, it’s a proof that I can see opportunities and capitalize on them

That’s why I tweet like this.

## 2026-05-20 (https://x.com/TheAhmadOsman/status/2057183854444843202)

> You don't pick an inference engine first. You pick a hardware strategy, a workload shape, and a serving model. The engine follows.
That is the most useful way to think about LLM inference engines.
Series note: This is Part 3 in my series teaching Self-hosted LLMs / Local AI.
- Part 1: GPU Memory Math for LLMs (2026 Edition).
- Part 2: Memory Bandwidth for Local AI Hardware (2026 Edition).
Those two pieces explain the hardware capacity and bandwidth math.
This one explains the software layer that turns that hardware into usable inference.
## Engines
These tools serve different purposes / occupy different layers
- Local portability
- Consumer CUDA
- Apple unified-memory workflows
- Quantized inference
- Production serving
- Distributed orchestration
- Vendor-optimized datacenter execution
A useful mental model:
![HIySrnUW8AAlRr5.jpg](media/2057183854444843202/HIySrnUW8AAlRr5.jpg)
The inference engine is not "the model." It is the traffic cop, memory manager, kernel dispatcher, scheduler, cache accountant, parallelism planner, API surface, and sometimes the deployment framework.
The best engine matches your memory hierarchy, interconnect, quantization format, latency and throughput targets, model architecture, and operational maturity.
## The one-page decision guide
![HIySt_uXkAAL3dt.jpg](media/2057183854444843202/HIySt_uXkAAL3dt.jpg)
- Laptop / edge / odd hardware → llama.cpp
- Mac-first workflows → MLX / MLX-LM
- Single RTX local inference → ExLlamaV2
- 2-4+ NVIDIA / CUDA GPUs → ExLlamaV3
- General production serving → vLLM
- Long-context / MoE / routing → SGLang
- NVIDIA max performance → TensorRT-LLM
- Cluster orchestration → NVIDIA Dynamo
The rest of this guide explains why.
## What an inference engine actually does
An inference engine loads weights, tokenizes input, runs the forward pass, samples tokens, maintains the KV cache, and streams results. Serious engines also handle batching, scheduling, prefix caching, quantization, parallel execution, API serving, metrics, and distributed execution.
The workload has two phases:
Prefill reads the prompt and builds the initial KV cache. It is compute-intensive.
Decode generates one token at a time, repeatedly reading weights and KV cache. It is memory-bandwidth-bound. Decode speed tracks memory bandwidth more than peak compute.
That distinction explains almost everything:
- Short prompt, long answer: decode dominates → memory bandwidth and batching matter.
- Long prompt, short answer: prefill dominates → attention kernels and chunked prefill matter.
- Many users: scheduler quality matters → continuous batching, cache paging, fairness.
- Long context: KV cache dominates → paged attention, KV quantization, offload.
- MoE: expert routing dominates → expert parallelism, interconnect, grouped GEMMs.
- Multi-node: interconnect dominates → NVLink, RDMA, pipeline parallelism, disaggregation.
PagedAttention tackled KV cache fragmentation. FlashAttention used IO-aware tiling to cut HBM (High Bandwidth Memory) traffic. Speculative decoding drafts cheap tokens and verifies them in parallel. The recurring theme: inference performance is memory movement plus scheduling.
## The real bottlenecks
![HIySwctXUAAWvdU.jpg](media/2057183854444843202/HIySwctXUAAWvdU.jpg)
1. Memory bandwidth, not just VRAM size. VRAM determines fit. Bandwidth determines decode speed. Apple's M3 Ultra offers up to 819 GB/s unified-memory bandwidth. NVIDIA's H100 SXM lists 3.35 TB/s GPU memory bandwidth. Unified memory lets you fit models that would not fit in consumer VRAM. HBM lets you serve them faster when the model fits. Fit is not speed. Capacity is not bandwidth.
2. KV cache growth. KV cache grows with batch size and context length. Long-context workloads can run out of memory even when weights fit. PagedAttention partitions the KV cache into blocks, increasing utilization and supporting larger batches.
3. Interconnect. The moment a model crosses GPU boundaries (multi-GPUs), you pay communication cost. Tensor parallelism needs frequent all-reduce collectives. Pipeline parallelism communicates at stage boundaries. Expert parallelism needs all-to-all traffic for MoE. vLLM's docs note that without NVLink, pipeline parallelism can outperform tensor parallelism.
4. Scheduler quality. A good scheduler decides which requests enter the batch, how prefill and decode share the accelerator, whether long prompts block short decodes, and how to avoid starvation. Supporting batching is not the same as behaving like a production-ready scheduler.
5. Runtime overhead. CUDA graphs, kernel fusion, sampling overhead, tokenizer overhead, HTTP overhead, LoRA switching, and structured decoding all matter. At high scale, the annoying 2% overheads form a union and demand attention (no punt intended).
## The engine families
![HIySychWYAA9HOd.jpg](media/2057183854444843202/HIySychWYAA9HOd.jpg)
There are four broad families:
Portable local runtimes: llama.cpp, MLC LLM, ONNX Runtime GenAI, OpenVINO, Ollama-style tools. These care about "make it run here."
Apple/unified-memory runtimes: MLX and MLX-LM. These care about "use big shared memory and Apple's stack well."
Consumer CUDA quant engines: ExLlamaV2 and ExLlamaV3. These care about "make my 3090/4090/5090 box scream with low-bit weights."
Production serving engines: vLLM, SGLang, TensorRT-LLM, TGI, LMDeploy. These care about concurrent users, KV cache, batching, parallelism, observability, and cost per token.
Then there are orchestration layers like Dynamo that sit above engines and coordinate fleets, disaggregated prefill/decode, routing, and autoscaling.
## llama.cpp: the portability king
llama.cpp is the answer when the hardware is weird, constrained, offline, CPU-heavy, edge-oriented, or not a tidy NVIDIA datacenter node.
It supports Apple Silicon via ARM NEON, Accelerate, and Metal; x86 via AVX/AVX2/AVX512/AMX; RISC-V; low-bit quantization; CUDA; AMD via HIP; MUSA; Vulkan; SYCL; and CPU+GPU hybrid offload. That is why llama.cpp owns the "just make it run" lane.
The HTTP server is more capable than a "toy local runner". llama-server provides OpenAI-compatible routes, Anthropic Messages API compatibility, reranking, continuous batching, multimodal support, JSON schema constraints, function calling, speculative decoding, and a web UI.
The critical limitation: llama.cpp is not for serious multi-node production serving. Its RPC backend is explicitly documented as proof-of-concept, fragile, and insecure.
Verdict: Use llama.cpp when portability, offline operation, GGUF, or hybrid offload matter more than fleet-scale serving.
DO NOT use with Multi-GPUs
## MLX and MLX-LM: the Apple Silicon weapon
MLX is Apple's array framework for Apple Silicon, and MLX-LM is the LLM package built on it. It is a Mac-first ML stack.
The key hardware fact is unified memory. Apple Silicon gives the CPU and GPU direct access to the same memory pool. MLX arrays live in unified memory, and you choose the device when running the operation rather than moving arrays between separate memory spaces.
This changes the local inference tradeoff. On a discrete GPU system, the question is "does it fit in VRAM?" On an M-series Mac with large unified memory, the question becomes "does it fit in memory, and can the memory system feed the GPU fast enough?" Large quantized models can fit on machines where the same model would be impossible on a 24 GB consumer GPU.
However, it is also slower.
MLX-LM adds Hugging Face Hub integration, quantization, LoRA and full fine-tuning, distributed inference, and a large MLX Community model ecosystem. MLX is no longer Mac-only: it offers CUDA and CPU-only packages for Linux. Distributed communication supports MPI, Ring over TCP, JACCL for RDMA over Thunderbolt, and NCCL for CUDA.
MLX-LM's server itself warns that it is not recommended for production because it only implements basic security checks.
Verdict: Use MLX for Mac-first ML and LLM workflows. For high-concurrency public serving, start with a real serving stack.
## ExLlamaV2 and V3: consumer CUDA, tuned and fast
ExLlamaV2 is the local CUDA quantization engine for people who want a consumer NVIDIA GPU to punch above its weight. It supports paged attention, dynamic batching, prompt caching, KV cache deduplication, batched generation, streaming, and speculative decoding. The word to remember is local. It makes quantized models fast on modern CUDA GPUs, especially consumer cards.
Best fits: one RTX 3090/4090/5090 box, local coding assistant, local chat, EXL2 quantized models, and prosumer workstation use.
ExLlamaV3 extends the philosophy toward multi-GPU and MoE-local inference. It adds the EXL3 quantization format based on QTIP, flexible tensor-parallel and expert-parallel inference for consumer hardware, an OpenAI-compatible server through TabbyAPI, continuous dynamic batching, and multimodal support.
V3 is compelling when you have 2-4+ consumer NVIDIA GPUs or want local MoE. Expect caveats: some models do not support tensor or expert parallelism in ExLlamaV3.
Verdict: ExLlamaV2 is the enthusiast's local CUDA engine. ExLlamaV3 is the frontier for multi-GPU (2-4) local setups. Expect rougher edges for better capability.
## vLLM: the default open-source production server
vLLM is the first engine most teams should evaluate for serious opensource LLM serving.
It offers PagedAttention-based KV memory management, continuous batching, chunked prefill, prefix caching, CUDA/HIP graphs, extensive quantization (FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ, AWQ, GGUF), optimized attention and GEMM/MoE kernels, speculative decoding, torch.compile, and disaggregated prefill/decode/encode.
It is also flexible: tensor/pipeline/data/expert/context parallelism, streaming, structured outputs, tool calling, OpenAI-compatible and Anthropic Messages APIs, gRPC, multi-LoRA, and support for NVIDIA, AMD, x86/ARM/PowerPC CPUs, plus plugins for TPUs, Gaudi, Ascend, Apple Silicon, and more.
vLLM's docs note that multi-node deployments typically use Ray, and without NVLink, pipeline parallelism may beat tensor parallelism. The trap is assuming vLLM removes the need for systems thinking. You still need to tune batching, context length, GPU memory utilization, parallelism layout, and routing. vLLM gives you a very good engine; it still requires good System Design.
Verdict: If someone says "we need to serve open models in production," vLLM is the default starting point.
## SGLang: vLLM's systems-brained cousin
SGLang is what you reach for when the serving workload is ugly: structured outputs, long context, MoE, disaggregation, and routing.
It offers RadixAttention prefix caching, prefill-decode disaggregation, speculative decoding, continuous batching, paged attention, tensor/pipeline/expert/data parallelism, structured outputs, chunked prefill, and multi-LoRA batching. It supports NVIDIA, AMD, Intel Xeon, Google TPUs, Ascend NPUs, and more.
SGLang's differentiator is serving architecture. Its prefill-decode disaggregation separates compute-intensive prefill from memory-intensive decode into specialized instances, transferring KV cache between them. This prevents long prefill batches from interrupting decode and spiking token latency.
Verdict: SGLang is for teams whose bottleneck is no longer "can we run the model?" but "can we run it under hostile traffic without torching latency, memory, and cost?"
## TensorRT-LLM: maximum NVIDIA performance
TensorRT-LLM is the NVIDIA-max-performance stack. It is optimized, specialized, powerful, and not pretending to be portable.
It provides Python APIs to build TensorRT engines with state-of-the-art optimizations, plus Python and C++ runtimes. It includes custom kernels for attention, GEMMs, and MoE; prefill-decode disaggregation, Wide Expert Parallelism, speculative decoding; and a high-level Python API integrated with NVIDIA Dynamo and Triton Inference Server.
B200 GPUs can load FP4 weights with optimized kernels. H100 and later support FP8 quantization that can double performance and halve memory consumption versus 16-bit with minimal accuracy loss.
Where it shines: H100/H200/B200/GB200/GB300-class fleets, NVIDIA-only datacenters, FP8/FP4 deployment, multi-node serving, and MoE at scale. Where it is awkward: AMD, Apple, or Intel portability; fast-changing experimental models; small local setups; and teams that need "works on everything."
Verdict: If you are committed to NVIDIA and care about absolute performance, TensorRT-LLM belongs in the bake-off. You trade portability for performance. Tuned specialization but less features.
## The rest of the field
TGI is Hugging Face's production server with tracing, metrics, tensor parallelism, and continuous batching. Use it when HF integration and simplicity matter.
MLC LLM is the compiler-first universal deployment engine with OpenAI-compatible APIs across REST, Python, JavaScript, iOS, and Android. Best for "ship LLMs everywhere," especially browser, mobile, and native apps.
ONNX Runtime GenAI implements the full generative loop over ONNX Runtime and powers Foundry Local, Windows ML, and the VS Code AI Toolkit. It supports CPU, CUDA, DirectML, TensorRT-RTX, OpenVINO, QNN, WebGPU, and AMD GPU. Best for app deployment and ONNX workflows.
OpenVINO GenAI is the Intel-optimized story for Xeon CPUs, Arc GPUs, Core Ultra, and NPUs. It offers OpenAI-compatible serving with continuous batching and paged attention. Best for Intel hardware.
LMDeploy is a CUDA-focused toolkit with TurboMind for performance and PyTorch for accessibility. Most interesting for CUDA users who want an alternative to vLLM/SGLang/TensorRT-LLM.
NVIDIA Dynamo is a distributed orchestration layer above engines like vLLM, SGLang, and TensorRT-LLM, supporting disaggregation, intelligent routing, and multi-tier KV caching. Use it when single-engine serving is no longer enough.
Note: DO NOT USE Ollama.
## Hardware strategy recipes
![HIyS3rPWoAAICxo.jpg](media/2057183854444843202/HIyS3rPWoAAICxo.jpg)
CPU-only server: llama.cpp first. OpenVINO for Intel Xeon. ONNX Runtime GenAI for app/ONNX deployment.
MacBook / Mac Studio: MLX / MLX-LM for Mac-native workflows. llama.cpp for GGUF portability.
Single RTX 3090 / 4090 / 5090: ExLlamaV2 for EXL2 local inference. llama.cpp for GGUF or portability. vLLM if serving multiple users.
Dual or quad consumer RTX box: ExLlamaV3 for multi-GPU quantized inference or MoE. vLLM if serving behavior matters. SGLang if testing routing or long-context patterns.
8×H100 / H200 node: Start with vLLM or SGLang. Benchmark TensorRT-LLM if NVIDIA-only and performance justifies tuning. Use Dynamo when multi-node orchestration becomes necessary.
B200 / GB200 / GB300-class infrastructure: Benchmark TensorRT-LLM, SGLang, and vLLM. Add Dynamo for fleet-level orchestration, KV-aware routing, and autoscaling.
AMD MI300 / MI325 / MI350 / MI355: Start with vLLM or SGLang on ROCm. Avoid assuming NVIDIA benchmarks transfer cleanly.
Intel Xeon / Core Ultra / Arc: OpenVINO GenAI or OpenVINO Model Server. ONNX Runtime GenAI if app embedding matters.
Browser, mobile, app-native: MLC LLM / WebLLM or ONNX Runtime GenAI.
## Benchmarking: what to measure
Bad benchmark: "I got 180 tok/s."
![HIyS6ZyXoAA6C-8.jpg](media/2057183854444843202/HIyS6ZyXoAA6C-8.jpg)
Good benchmark includes:
Model: exact model, architecture, parameter count, active MoE params.
Weights: dtype, quant format, group size, calibration.
Engine: version, commit, backend, flags.
Hardware: GPU SKU, memory capacity, bandwidth, interconnect, CPU, RAM.
Workload: input/output length distributions, concurrency, streaming, shared prefixes, structured output.
Metrics: TTFT, TPOT, end-to-end latency, p50/p95/p99, tokens per second, requests per second, GPU memory usage, KV cache hit rate, prefill throughput, decode throughput, cost per 1M tokens.
Benchmarking Rules:
1. Never compare engines using only single-user tokens per second.
1. Test your actual prompt and output distribution.
1. Test with realistic concurrency.
1. Separate prefill from decode.
1. Track p95 and p99, not only averages.
1. Measure memory headroom at target context length.
1. Test cache reuse if your app has repeated prefixes.
1. Benchmark structured output separately; grammar adds overhead.
1. Benchmark LoRA and multi-LoRA separately.
1. Re-test after driver, CUDA, ROCm, model, or engine upgrades.
## Common mistakes
Choosing by VRAM capacity alone. VRAM determines fit. Bandwidth and scheduler determine speed. A large unified-memory machine can fit huge models, but an H100 decodes faster when the model fits due to much higher HBM bandwidth.
Using tensor parallelism on weak interconnect. Without NVLink or NVSwitch, test pipeline parallelism. vLLM's docs call this out for L40S-like setups.
Ignoring KV cache. Long context and concurrency can make KV cache the limiting factor. PagedAttention, prefix caching, KV quantization, and disaggregation are not optional at scale.
Treating local engines as production servers. llama.cpp server is capable. MLX-LM server is convenient. Ollama is pleasant yet SHOULD NOT BE USED.
However, production means security, observability, backpressure, routing, autoscaling, and SLA behavior. MLX-LM itself warns that its server is not recommended for production.
Assuming every quantization format is portable. GGUF, EXL2, EXL3, AWQ, GPTQ, FP8, FP4, MLX formats, and ONNX are not interchangeable. The right format is the one your engine has optimized kernels for.
Ignoring model architecture. Dense models, MoE, hybrid attention, multimodal models, and long-context variants stress different parts of the engine. Broad support does not mean every optimization works equally.
Trusting benchmark charts without workload shape. A chart for Llama 3.1 8B at 1K input / 128 output says little about a coding agent with 80K context running on Qwen 3.6 27B / Gemma 4 26B-A4B, or a RAG service with 500 concurrent users.
## The opinionated final map
Local AI user: LM Studio or Harbor for convenience. llama.cpp for control. MLX on Mac. ExLlamaV2/V3 for CUDA local performance.
Building a local agent: Any should work, but given what most people use; llama.cpp for portability. MLX if users are on Apple Silicon. vLLM if simulating production serving locally.
Serving an internal team: Start with vLLM. Use SGLang if structured outputs, long context, multi-LoRA, MoE, or routing matter.
Serving customers at scale: Benchmark vLLM, SGLang, and TensorRT-LLM. If routing and disaggregation matter, SGLang and Dynamo deserve attention.
NVIDIA datacenter: TensorRT-LLM for max performance. vLLM for flexibility. SGLang for complex serving. Dynamo for fleet orchestration.
Apple Silicon: MLX for native development. llama.cpp for GGUF. Unified memory is a capacity superpower with bandwidth tradeoffs, not HBM.
Edge, app, browser, or Windows-native: llama.cpp, MLC LLM, ONNX Runtime GenAI, or OpenVINO, depending on stack.
## Final principle
Inference Engines have consequences.
Pick the engine after answering these:
1. What hardware do I actually have?
1. Does the model fit in fast memory, or only in system/unified memory?
1. Is decode or prefill the bottleneck?
1. What context length and concurrency matter?
1. Are prompts shared enough for prefix caching?
1. Is the model dense, MoE, multimodal, or hybrid?
1. Do I need local convenience, production serving, or fleet orchestration?
1. What quantization format has optimized kernels on my target engine?
1. Is my interconnect PCIe, NVLink, NVSwitch, Ethernet, RDMA, or Thunderbolt?
1. Am I optimizing latency, throughput, cost, privacy, portability, or developer speed?
The engine follows the answers.
Until next time.
-Ahmad

## 2026-05-21 (https://x.com/TheAhmadOsman/status/2057268825326796906)

DROP EVERYTHING

The bible for running LLMs locally is now available online to read for free

Covers what to use on

- Laptop / edge / odd hardware
- Mac-first workflows
- Single RTX GPUs
- 2-4+ NVIDIA / CUDA GPUs
- General production serving
- Long-context / MoE / routing
- NVIDIA max performance
- Cluster orchestration

Software

- llama.cpp
- MLX / MLX-LM
- ExLlamaV2
- ExLlamaV3
- vLLM
- SGLang
- TensorRT-LLM
- NVIDIA Dynamo

You should read this, and if you cannot now then you most definitely wanna bookmark it for later

Local AI FTW

## 2026-05-25 (https://x.com/TheAhmadOsman/status/2059009658187296873)

The single highest-leverage move an individual can still make in 2026 is this:

Buy a GPU and run real workloads on them every day.

- Not rent tokens.
- Not fine-tune on someone else’s cluster.
- Own the silicon + the weights + the serving stack.

I’ve been doing this since 2023 with my own GPUs. The intuition, debugging ability, and taste you develop when the hardware is yours is impossible to replicate through APIs.

The window is still open. It won’t be forever.

## 2026-06-03 (https://x.com/TheAhmadOsman/status/2062312164455862286)

Local AI hardware = capacity × bandwidth × software stack

- Capacity tells you what fits
- Bandwidth tells you how hard the box can breathe
- The software stack tells you how much of the spec sheet you can actually cash out.

Hardware by Memory Bandwidth
- Mac Studio M3 Ultra: up to 512GB @ 819 GB/s
- RTX PRO 6000 Blackwell: 96GB @ 1792 GB/s
- RTX 5090: 32GB @ 1792 GB/s
- RTX 4090: 24GB @ 1008 GB/s
- RX 7900 XTX: 24GB @ 960 GB/s
- Radeon PRO W7900: 48GB @ 864 GB/s
- AMD Radeon AI PRO R9700: 32GB @ 640 GB/s
- Intel Arc Pro B65: 32GB @ ~608 GB/s
- Tenstorrent Wormhole n300: 24GB @ 576 GB/s
- Tenstorrent Blackhole p150: 32GB @ 512 GB/s + 800G
- MacBook Pro M5 Max: 460-614 GB/s
- MacBook Pro M5 Pro: 307 GB/s
- DGX Spark: 128GB @ 273 GB/s (coherent + CUDA)
- Mac mini M4 Pro: 273 GB/s
- Ryzen AI Max / Strix Halo: ~256 GB/s (~96GB usable GPU)
- MacBook Air M5: 153 GB/s
- Snapdragon X2 Elite: 152-228 GB/s
- Intel Lunar Lake: 136 GB/s
- Snapdragon X Elite: 135 GB/s
- Mac mini M4: 120 GB/s
- Arc Pro B60: 24GB @ ~456 GB/s

Verdict

- GPUs are still the bandwidth kings

- Apple wins: stupid amounts of memory, don’t want to shard across GPUs
- Apple loses: when raw tokens/sec & concurrency matter more

- DGX Spark: coherent memory + NVIDIA stack

- Strix Halo / Ryzen AI Max: first real x86 unified-memory contender

- Tenstorrent: fully OSS stack, excited to see this mature

Fitting ≠ serving

Even if it fits, you still pay for
- bandwidth during decode
- KV cache growth
- dequantization
- batching + concurrency
- scheduler quality
- framework overhead

The only mental model that matters:

1. What must fit?
2. What bandwidth tier do I need?
3. What software stack can actually deliver it?

In short:
- NVIDIA → fastest raw speed
- Apple Studio M3 Ultra → biggest one-box memory
- Strix Halo → first real x86 unified
- DGX Spark → coherent NVIDIA dev appliance
- AMD / Intel Arc → rising alternatives
- Tenstorrent → fully opensource stack

Do ask: “which bottleneck am I buying?”

Not: “which hardware is best?”

## 2026-06-08 (https://x.com/TheAhmadOsman/status/2063935919481106560)

How to go about learning all of this?

1st: Start with the serving engine view

- vLLM: PagedAttention, continuous batching, prefix caching, CUDA graphs

- SGLang: RadixAttention/prefix reuse, speculative decoding, MoE, structured/agent workloads

- TensorRT-LLM: NVIDIA peak stack, FP8/FP4, Wide-EP, disaggregated serving

- FlashInfer: reusable kernel/operator library for attention/GEMM/MoE/sampling

2nd: Go down the stack

- Triton tutorials → custom fused kernels

- CUTLASS/CuTe → Tensor Core GEMM and Blackwell/Hopper details

- FlashAttention papers → attention algorithm/kernel co-design

- PagedAttention paper → KV-cache memory management

- MoE docs → routing + grouped GEMM + all-to-all

- Nsight profiling → stop guessing

3rd: Do this mini-project sequence

1. Implement RMSNorm in Triton; compare to PyTorch

2. Implement fused SiLU × gate

3. Implement simple FP16 matmul; compare to cuBLAS/rocBLAS

4. Implement paged KV lookup for decode attention

5. Add FP8 KV cache with per-block scales

6. Implement toy top-k sampling on GPU

7. Implement tiny MoE dispatch + grouped GEMM

8. Integrate one custom op into vLLM or SGLang and profile end-to-end

## 2026-06-14 (https://x.com/TheAhmadOsman/status/2065953682277961968)

Got online to dozens of emails from builders and investors on my Opensource AI Must Win declaration

Apparently someone posted it on HN yesterday and it was the 2nd highest voted of the day

Over the next few weeks I will be in discussions with researchers, investors, and others to ensure we bring that vision to life

More soon

## 2026-06-16 (https://x.com/TheAhmadOsman/status/2066692532440797374)

PROP TIP

Running LLMs locally? Give them web access

My setup:

- SearXNG: candidate source discovery

- Firecrawl: known-URL scraping and crawling

- Camofox: browser fallback when JS/interaction gets annoying

Search → Extract → Interact

Tell your favorite agent to set this up, then wire it into your local models

> Watch them suddenly become way more useful

You’re welcome

## 2026-06-20 (https://x.com/TheAhmadOsman/status/2068344843563085829)

Spending time learning graphs and networking theory is one of the highest-ROI investments you can make. It quietly compounds across distributed systems, AI, infrastructure, markets, and even social dynamics.

Solid starters: Barabási – Network Science; Easley/Kleinberg – Networks, Crowds, and Markets; MIT – Math for CS; Diestel – Graph Theory; Kleinberg/Tardos – Algorithm Design; Spielman – Spectral Graph Theory; Roughgarden AGT; CS224W; NetworkX, Gephi, SNAP, PyG.

## 2026-06-21 (https://x.com/TheAhmadOsman/status/2068737893611327932)

You run Kernels, not models

The model is just a graph

The Inference Engine serves as a scheduler, optimizer, and executor

But the actual work? That happens in the Kernels

- MatMul Kernels
- Attention Kernels
- RMSNorm Kernels
- KV cache Kernels
- Quantized linear Kernels
- Sampling Kernels
- Fused “please don’t write this back to memory 9 times” Kernels

Same model, same GPU, same VRAM
Wildly different performance

Because one stack is using optimized fused Kernels that understand your hardware

And the other stack is playing hot potato with tensors through 47 tiny launches and pretending the GPU is the problem

Bad Kernels make people say:
“this model is slow”

Good Kernels make people say:
“wait how is this running locally?”

This is why Inference Engines and the Kernels implemented within them matter

The model is the recipe
The hardware is the kitchen
The Kernels are the knives, pans, burners, and the chef not cutting onions with a spoon

Most people benchmark models
The real ones benchmark the Kernels underneath

## 2026-06-21 (https://x.com/TheAhmadOsman/status/2068769896016531789)

Why do I focus on Inference Engines/Software Stacks for your hardware?

- 2x RTX 3090s: ~14.5 tok/s → ~64 tok/s moving to vLLM w/ TP=2

- RTX PRO 6000: ~32 tok/s → ~110 tok/s moving to Sglang

So:

- CUDA/2+ GPUs: ExLlamaV3/vLLM/Sglang &gt; llama.cpp

- Edge: llama.cpp &gt; Ollama https://t.co/5WXSlPrrOB

## 2026-06-21 (https://x.com/TheAhmadOsman/status/2068831569318391942)

INCREDIBLE RESOURCE

The MOST COMPLETE GUIDE for understanding LLMs from first principles is now available online to read for free

Covers the model mechanics

- Tokens / tokenizers
- Transformers
- Attention
- KV cache
- Prefill vs decode
- Decoding controls
- Model packages
- Chat templates
- Long context
- RAG
- Agents / tools
- Fine-tuning
- Multimodal models

Then connects that to running models locally

- What "local" really means
- Open-weight vs opensource
- Quantization
- VRAM math
- Hardware tiers
- File formats / load safety
- Runtimes / serving modes
- Model selection
- Privacy
- Failure modes
- Benchmarks
- Practical setup paths

You should read this, and if you cannot now then you most definitely wanna bookmark it for later

Opensource AI FTW

## 2026-06-22 (https://x.com/TheAhmadOsman/status/2068944091405303916)

Let me make Local AI easy for you

Give Codex Cli the article below &amp; tell it:

- Infer the right Inference Engine from your hardware + article below
- Use uv+venv
- Pick the right kernels
- Tune flags, batching, KVCache, etc
- Optimize for your hardware &amp; chosen model

See? Easy https://t.co/1SSk4K1LTS

## 2026-06-22 (https://x.com/TheAhmadOsman/status/2069044900755292592)

The Ultimate Step-By-Step LLM Engineering Projects Roadmap (2026 Edition)

- Build a tokenizer
- Learn embeddings
- Implement RoPE / ALiBi
- Hand-wire attention
- Build MHA
- Build a Transformer block
- Train a mini-former
- Compare objectives
- Build sampling
- Speculative decoding
- KV cache
- MQA / GQA / MLA
- Long context
- FlashAttention
- Hardware budgets
- Toy MoE
- Sparse model trade-offs
- State-space / linear attention
- Diffusion language models
- Data pipelines
- Synthetic data
- Scaling laws
- SFT / DPO / RLHF / GRPO
- Quantization
- Serving stacks
- Eval harnesses
- RAG
- Tool use / agents
- Vision-language adapters
- Interpretability
- Red-team suite
- Full capstone model system

One request: Choose an Opensource AI lab when you make it

Opensource is where humanity gets to keep the tools

DM me when you've made it ;)

## 2026-06-27 (https://x.com/TheAhmadOsman/status/2070966129762480373)

Wanna replace Anthropic/OpenAI? START WITH THIS

The bible for running LLMs locally is now available online to read for free

Covers what to use on

- Laptop / edge / odd hardware
- Mac-first workflows
- Single RTX GPUs
- 2-4+ NVIDIA / CUDA GPUs
- General production serving
- Long-context / MoE / routing
- NVIDIA max performance
- Cluster orchestration

Software

- llama.cpp
- MLX / MLX-LM
- ExLlamaV2
- ExLlamaV3
- vLLM
- SGLang
- TensorRT-LLM
- NVIDIA Dynamo

You should read this, and if you cannot now then you most definitely wanna bookmark it for later

Opensource & Local AI FTW

## 2026-06-30 (https://x.com/TheAhmadOsman/status/2072067611282854291)

Anthropic wants the public to see one thing: the careful lab, the safety lab, the grown-up in the room trying to keep frontier AI from running off a cliff. However, the pattern around Anthropic does not look like caution by itself. It looks like a company wrapping a business model in moral language, then using that language to justify opaque model behavior, anti-competitive access rules, regulatory pressure, and a future where builders, startups, researchers, and Opensource communities stay downstream of a few blessed frontier labs.

Imagine a compiler that emits worse binaries when it thinks you are building a competing compiler. Imagine a microscope that blurs certain samples because the manufacturer dislikes the research direction. Imagine a debugger that lies only when your codebase resembles a future rival.

Anthropic can learn from the internet, copyrighted books, code, public knowledge, user feedback if permitted, synthetic data, and its own models. But if a developer uses Claude to bootstrap a competitive open assistant, Anthropic calls foul. The company argues that safety controls may be lost and that competing models undermine the investment required to build frontier systems.

The fight is whether intelligence becomes something people can own, inspect, modify, run locally, fine-tune, study, route, and improve, or whether it becomes a subscription permission layer run by companies that can refuse, degrade, surveil, retain, revoke, reroute, or lobby away your access.

Anthropic's moat is being a permission regime. On daily basis, competitors and acquisition targets discover that access can disappear. The company asks governments to bless safety frameworks, deployment gates, incident reporting, evaluation regimes, and even future pauses that incumbents are best positioned to survive.

If a coding or research model secretly changes the quality, direction, or reliability of an answer because it classified the user as doing disallowed frontier work, the tool is no longer merely "safe." It is untrustworthy.

If Anthropic wants to be treated like a public-interest safety institution, it cannot behave like a hypersensitive platform monopolist whenever a customer gets too close to building alternatives.

Yes, companies protect their IP. But Anthropic is not selling a normal SaaS widget. It is selling cognition as infrastructure. Once cognition becomes infrastructure, anti-competitive access control stops being a normal vendor dispute and becomes a social bottleneck.

Anthropic repeatedly converts safety, security, and responsible deployment into mechanisms of control over who may build and what could be built.

We cannot trust them.

## 2026-07-07 (https://x.com/TheAhmadOsman/status/2074599175094981012)

Hey my friend, cool setup. If 8x RTX PRO 6000s is the real goal, I’d treat it like a serious infra build, not a workstation. I wouldn’t optimize around attempting to reuse DDR4. This will be a 100k+ machine and you’ll be glad you did it right. You can always sell the DDR4 to recoup costs. Once you are chasing lots of PCIe Gen5 lanes, you’re basically in DDR5/ECC RDIMM territory anyway. GENOAD8X feels like strong fit here with MCIO and CPayne PCBs: 7x Gen5 x16 + 1x Gen5 x8, and no need for bifurcation. True 8x16 is rare of course because it soaks up 128 lanes before storage/networking. Biggest questions are 240V power, panel headroom for the increased electrical load, system airflow, and cooling. You can absolutely stay air cooled even with a full power deployment like this (it’s actually the most common setup for commercial servers below the enterprise data center tier), and you’ll just be sizing and installing dedicated cooling which will of course also have its own power requirements. A lot of good options here. Happy to talk it through anytime.

## 2026-07-08 (https://x.com/TheAhmadOsman/status/2074866037632418066)

Local AI hardware = capacity X bandwidth X software stack

- Capacity tells you what fits
- Bandwidth tells you how hard the box can breathe
- The software stack tells you how much of the spec sheet you can actually cash out.

Hardware by Memory Bandwidth
- Mac Studio M3 Ultra: up to 512GB @ 819 GB/s
- RTX PRO 6000 Blackwell: 96GB @ 1792 GB/s
- RTX 5090: 32GB @ 1792 GB/s
- RTX 4090: 24GB @ 1008 GB/s
- RX 7900 XTX: 24GB @ 960 GB/s
- Radeon PRO W7900: 48GB @ 864 GB/s
- AMD Radeon AI PRO R9700: 32GB @ 640 GB/s
- Intel Arc Pro B65: 32GB @ ~608 GB/s
- Tenstorrent Wormhole n300: 24GB @ 576 GB/s
- Tenstorrent Blackhole p150: 32GB @ 512 GB/s + 800G
- MacBook Pro M5 Max: 460-614 GB/s
- MacBook Pro M5 Pro: 307 GB/s
- DGX Spark: 128GB @ 273 GB/s (coherent + CUDA)
- Mac mini M4 Pro: 273 GB/s
- Ryzen AI Max / Strix Halo: ~256 GB/s (~96GB usable GPU)
- MacBook Air M5: 153 GB/s
- Snapdragon X2 Elite: 152-228 GB/s
- Intel Lunar Lake: 136 GB/s
- Snapdragon X Elite: 135 GB/s
- Mac mini M4: 120 GB/s
- Arc Pro B60: 24GB @ ~456 GB/s

Verdict

- GPUs are still the bandwidth kings

- Apple wins: stupid amounts of memory, don't want to shard across GPUs
- Apple loses: when raw tokens/sec & concurrency matter more

- DGX Spark: coherent memory + NVIDIA stack

- Strix Halo / Ryzen AI Max: first real x86 unified-memory contender

- Tenstorrent: fully OSS stack, excited to see this mature

Fitting != serving

Even if it fits, you still pay for
- bandwidth during decode
- KV cache growth
- dequantization
- batching + concurrency
- scheduler quality
- framework overhead

The only mental model that matters:

1. What must fit?
2. What bandwidth tier do I need?
3. What software stack can actually deliver it?

In short:
- NVIDIA -> fastest raw speed
- Apple Studio M3 Ultra -> biggest one-box memory
- Strix Halo -> first real x86 unified
- DGX Spark -> coherent NVIDIA dev appliance
- AMD / Intel Arc -> rising alternatives
- Tenstorrent -> fully opensource stack

Do ask: "which bottleneck am I buying?"

Not: "which hardware is best?"
