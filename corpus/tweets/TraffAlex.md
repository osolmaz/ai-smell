# @TraffAlex — long-form tweets

## 2026-06-14 (https://x.com/TraffAlex/status/2066236717015728227)

🖥️ Best Local LLMs for Consumer GPUs — llama.cpp Guide (June 2026)

What I actually run on consumer hardware right now. Every model below runs via llama.cpp with a simple one-liner — no Docker, no Python env, no cloud.

━━━ 8-16GB VRAM ━━━

🔹 Gemma 4-12B (Google)
• Smartest model in this size class — competes with stuff 2× bigger
• Unsloth's MTP GGUFs: 162 tok/s vs 52 tok/s normal (3× speedup)
• Minimum 8GB VRAM recommended for Q4_K_M quant
• GGUF → https://t.co/VWp818MB3D

🔹 LFM2.5-8B-A1B (LiquidAI)
• Hybrid MoE, only 1B active params — absurdly fast for its size
• Perfect for 8-12GB cards, MacBooks, or anyone on a tight budget
• GGUF → https://t.co/ZbOs4mXJDq

━━━ 16-32GB VRAM ━━━

🔹 Qwen3.6-27B (Qwen)
• Scored 1.00 on tool-efficiency benchmarks — best local agent available
• 40 deterministic tasks, 32k/128k context needle tests — all passed
• GGUF → https://t.co/n7K3sPvliE
• MTP version (faster) → https://t.co/gwdfnJTzcy

🔹 Qwopus3.6-27B-v2 (Jackrong)
• Best quantization of Qwen3.6-27B — topped 5 agent & coding benchmarks (1200 samples)
• If you're running Q4, this is the one to grab
• GGUF → https://t.co/tV1DFqXnOD
• MTP version → https://t.co/PMqz7V5ewv

🔹 Gemma 4-31B QAT (Google/Unsloth)
• QAT variant with MTP draft head: 76-125 tok/s (1.67× speedup)
• Excellent for multi-agent / subagent workflows
• GGUF → https://t.co/FgVsUX0YOB

🔹 Nex-N2-Mini (Nex AGI)
• Post-train of Qwen3.5-35B-A3B — MoE with only 3B active params
• Fits on 16GB+ VRAM, overflow loads from system RAM
• Adaptive thinking saves ~20% tokens with no quality loss
• For deep multi-step reasoning, nothing in this size comes close
• GGUF → https://t.co/oyC522a8Eh

━━━ Quick Picks ━━━

• 16GB all-rounder → Gemma 4-12B with MTP GGUFs
• 32GB all-rounder → Qwen3.6-27B / Qwopus-v2
• Agents & tool use → Qwen3.6-27B or Qwopus Q4
• Deep reasoning → Nex-N2-Mini (MoE, fits 16GB+)
• Tight budget → LFM2.5-8B-A1B
• Cheapest full build: 1× used RTX 3090 (24GB) + rest of PC ≈ $1000-1500

━━━ Setup on Windows ━━━

1. Download llama.cpp → https://t.co/et0J7Swua7 (latest .zip)
2. Extract to any folder (e.g. C:\llama.cpp)
3. Download a .gguf from the links above (Q4_K_M or Q5_K_M for best quality/speed balance)
4. Run one of the commands below depending on your hardware

━━━ Launch Commands ━━━

SINGLE GPU — Standard model (no MTP):

llama-server.exe ^
  -m C:\models\Qwen3.6-27B-Q5_K_M.gguf ^
  --ctx-size 180000 ^
  --flash-attn on ^
  --cache-type-k q4_0 ^
  --cache-type-v q4_0 ^
  --batch-size 1024 --ubatch-size 512 ^
  -ngl 100 ^
  -np 1 ^
  --port 8080 ^
  --jinja

SINGLE GPU — MTP model (faster inference):

llama-server.exe ^
  -m C:\models\Qwen3.6-27B-MTP-Q5_K_M.gguf ^
  --ctx-size 180000 ^
  --flash-attn on ^
  --cache-type-k q4_0 ^
  --cache-type-v q4_0 ^
  --batch-size 1024 --ubatch-size 512 ^
  --spec-type draft-mtp ^
  --spec-draft-n-max 3 ^
  -ngl 100 ^
  -np 1 ^
  --port 8080 ^
  --jinja

DUAL GPU — Split across two cards:

llama-server.exe ^
  -m C:\models\Qwen3.6-27B-Q5_K_M.gguf ^
  --ctx-size 180000 ^
  --flash-attn on ^
  --cache-type-k q4_0 ^
  --cache-type-v q4_0 ^
  --batch-size 1024 --ubatch-size 512 ^
  -ngl 100 ^
  --tensor-split 0.55,0.45 ^
  --main-gpu 0 ^
  -np 1 ^
  --port 8080 ^
  --jinja

DUAL GPU + MTP + Vision (multimodal):

llama-server.exe ^
  -m C:\models\Qwen3.6-27B-MTP-Q5_K_M.gguf ^
  --ctx-size 180000 ^
  --flash-attn on ^
  --cache-type-k q4_0 ^
  --cache-type-v q4_0 ^
  --batch-size 1024 --ubatch-size 512 ^
  --spec-type draft-mtp ^
  --spec-draft-n-max 3 ^
  -ngl 100 ^
  --tensor-split 0.60,0.40 ^
  --main-gpu 0 ^
  -np 1 ^
  --port 8080 ^
  --jinja ^
  --mmproj C:\models\mmproj-F16.gguf

━━━ Parameter Breakdown ━━━

-m <path>
  Path to your .gguf model file. Change this to wherever you downloaded it.

--ctx-size 180000
  Context window in tokens. 180k = huge context for long conversations or big codebases.
  Reduce to 32768 or 65536 if you don't need long context — uses less VRAM.

--flash-attn on
  Flash Attention — dramatically speeds up inference and reduces VRAM usage.
  Works on RTX 30xx/40xx/50xx. Always enable this.

--cache-type-k q4_0 / --cache-type-v q4_0
  Quantizes the KV cache (key/value attention cache) to 4-bit.
  This is what makes 180k context fit in VRAM. Without it, huge contexts eat all your memory.
  Quality impact is minimal — this is a free performance win.

--batch-size 1024 / --ubatch-size 512
  batch-size = how many tokens are processed in one forward pass (throughput).
  ubatch-size = micro-batch actually sent to the GPU per step.
  Higher = faster prompt processing but needs more VRAM.
  If you run out of VRAM, lower these (e.g. 512/256).

-ngl 100
  Number of layers to offload to GPU. 100 = all layers on GPU (full offload).
  This is what you want if the model fits in your VRAM.
  If it doesn't fit, reduce this (e.g. -ngl 40) — remaining layers run on CPU/RAM.

--tensor-split 0.55,0.45
  How to split model layers across multiple GPUs. Values are ratios.
  0.55,0.45 = GPU 0 gets 55% of layers, GPU 1 gets 45%.
  Adjust based on your VRAM — give more to the card with more memory.
  Example: 0.70,0.30 for a 24GB + 12GB setup.
  Not needed for single GPU setups.

--main-gpu 0
  Which GPU handles the batch computation (the "orchestrator").
  Set to 0 (your primary GPU). The other GPU(s) handle their assigned layers.
  Minor performance impact — usually just leave it at 0.

-np 1
  Number of parallel slots (concurrent requests). 1 = one user at a time.
  Increase to 2-4 if you want multiple clients connected simultaneously.
  Each extra slot uses additional VRAM for its own KV cache.

--port 8080
  Which port the server listens on. Change if port 8080 is busy.

--jinja
  Enables Jinja2 template processing — required for proper chat formatting.
  Most modern models expect this. Always include it.

--spec-type draft-mtp
  Enables Multi-Token Prediction (MTP) speculative decoding.
  Only works with MTP GGUF models (downloaded separately).
  The model predicts multiple tokens at once and verifies them — big speed boost.

--spec-draft-n-max 3
  How many tokens the MTP draft head proposes per step.
  3 is a good default. Higher = potentially faster but more VRAM and may reduce quality.

--mmproj <path>
  Path to the multimodal projector file (for vision models).
  Enables image understanding — paste screenshots into the web chat.
  Only needed if you want vision capabilities. Omit for text-only use.

━━━ Your Hardware → Your Command ━━━

Single GPU (8-24GB VRAM):
  Use the "Single GPU" command. Change -m to your model path.
  8GB card → Gemma 4-12B Q4 or LFM2.5-8B
  12GB card → Gemma 4-12B Q5/Q6
  16GB card → Gemma 4-31B QAT Q4 or Nex-N2-Mini
  24GB card → Qwen3.6-27B Q4/Q5, Qwopus-v2, Gemma 4-31B QAT Q5/Q6

Dual GPU:
  Use the "Dual GPU" command. Adjust --tensor-split based on your VRAM ratio.
  24GB + 24GB → --tensor-split 0.50,0.50
  24GB + 12GB → --tensor-split 0.70,0.30
  24GB + 8GB → --tensor-split 0.75,0.25

Want speed? Use MTP versions of models with the "MTP" commands.

Want vision? Add --mmproj with the projector file from the model's HuggingFace repo.

5. Once running, you get:
   • Web chat UI → http://localhost:8080
   • OpenAI-compatible API → http://localhost:8080/v1
   • Playground → http://localhost:8080/playground

━━━ Why /v1 API Is the Killer Feature ━━━

One local endpoint replaces your entire cloud API bill. The /v1 endpoint is drop-in OpenAI-spec compatible — every tool that speaks OpenAI just works. No custom code, no glue layer.

Works out of the box with:
• IDEs: Cursor, Continue, Windsurf, Cline, Roo Code
• CLI tools: aider, Open Interpreter, OpenCode
• Frameworks: LangChain, LlamaIndex, LiteLLM
• Any OpenAI SDK (Python, Node, Go, Rust)

Why this beats cloud APIs:
• 100% private — code never leaves your machine
• $0 per token — no rate limits, no quotas, no surprise bills
• Works fully offline
• Zero telemetry, no training on your data
• Swap models by dropping in a different .gguf — no app changes needed
• Run 32k–128k context windows without burning money

Good combos:
• Cursor + Qwopus-v2 → near-frontier quality, zero API cost
• Continue + Qwen3.6-27B → best local coding agent
• aider + Gemma 4-12B MTP → 162 tok/s, feels instant
• OpenCode + Nex-N2-Mini → deep reasoning on 16GB

Set any OpenAI-compatible client to your local endpoint:
   set OPENAI_API_KEY=sk-dummy   (any non-empty string works)
   set OPENAI_BASE_URL=http://localhost:8080/v1
   # every OpenAI-compatible tool now hits your local GPU

Shoutouts: @0xSero @rS_alonewolf @witcheer @UnslothAI @LottoLabs

## 2026-06-27 (https://x.com/TraffAlex/status/2071020631072616698)

Outgrown 32–64 GB VRAM and unsure
what's next? (myself included 😅)

The answer: DGX Spark.
128 GB unified memory. $4,699.
Runs models your GPU can't even load.

Here's everything — 2x Spark cluster
setup, best models with benchmarks,
working docker commands, and the flags
that actually matter. All sourced from
tested community results on https://t.co/IrZFzgs2ry +
official NVIDIA docs.

🔩 HARDWARE — DGX Spark

• SoC: NVIDIA GB10 Grace Blackwell
• Memory: 128 GB unified (CPU + GPU
  shared pool)
• Price: $4,699 / unit
• Network: ConnectX-7 (CX7) 200GbE
  QSFP ports
• Storage: 4TB NVMe M.2 (encrypted)
• Size: 150mm x 150mm x 50.5mm
• Performance: 1 PFLOPS FP4

🔗 2x SPARK CLUSTER — "Sweet Spot"

(Tested and verified by @MiaAI_lab)

Hardware needed:
  • 2x NVIDIA DGX Spark
  • 1x QSFP cable (direct 200GbE
    link — full bandwidth, 1 cable)

Setup (from official NVIDIA
      dgx-spark-playbooks on GitHub):

  1. Make sure both units have the
     same username:
     $ whoami
     (if not: sudo useradd -m nvidia
      && sudo usermod -aG sudo nvidia
      && sudo passwd nvidia
      && su - nvidia)

  2. Physically connect QSFP cable,
     identify active interface:
     $ ibdev2netdev
     (look for "Up" — each port has
      2 names, use enp1s0f... not
      enP2p...)

  3. Network config — choose ONE:

     A) Automatic (link-local) —
        1 QSFP cable only:
        $ sudo tee /etc/netplan/
          40-cx7.yaml > /dev/null
          <<EOF
        network:
          version: 2
          ethernets:
            enp1s0f0np0:
              link-local: [ ipv4 ]
            enp1s0f1np1:
              link-local: [ ipv4 ]
        EOF
        $ sudo chmod 600 /etc/netplan/
          40-cx7.yaml
        $ sudo netplan apply

     B) Manual static IPs
        (recommended):
        # Node 1:
        $ sudo tee /etc/netplan/
          40-cx7.yaml > /dev/null
          <<EOF
        network:
          version: 2
          ethernets:
            enp1s0f0np0:
              addresses:
                - 192.168.100.10/24
              dhcp4: no
            enp1s0f1np1:
              addresses:
                - 192.168.200.12/24
              dhcp4: no
        EOF
        # Node 2:
        $ sudo tee /etc/netplan/
          40-cx7.yaml > /dev/null
          <<EOF
        network:
          version: 2
          ethernets:
            enp1s0f0np0:
              addresses:
                - 192.168.100.11/24
              dhcp4: no
            enp1s0f1np1:
              addresses:
                - 192.168.200.13/24
              dhcp4: no
        EOF
        $ sudo chmod 600 /etc/netplan/
          40-cx7.yaml
        $ sudo netplan apply

     C) Manual CLI (temporary —
        resets on reboot):
        # Node 1:
        $ sudo ip addr add
          192.168.100.10/24
          dev enp1s0f1np1
        $ sudo ip link set
          enp1s0f1np1 up
        # Node 2:
        $ sudo ip addr add
          192.168.100.11/24
          dev enp1s0f1np1
        $ sudo ip link set
          enp1s0f1np1 up

  4. Passwordless SSH:
     $ ssh-keygen -t ed25519
     $ ssh-copy-id user@192.168.100.11

     Or use official script:
       $ bash ./discover-sparks
       (from dgx-spark-playbooks)

  5. Verify connectivity both
     directions:
     $ ssh 192.168.100.11 hostname
     $ ssh 192.168.100.10 hostname

  6. NCCL test — confirm distributed
     communication works
     (driver versions must match on
      both units)

  🔙 Rollback (if something breaks):
     $ sudo rm /etc/netplan/
       40-cx7.yaml
     $ sudo netplan apply
     Or for CLI method:
     $ sudo ip addr del
       192.168.100.10/24
       dev enp1s0f0np0

  🐛 Troubleshooting:
     "Network unreachable"
       → verify netplan YAML,
         run sudo netplan apply
     SSH failures
       → re-run ./discover-sparks,
         enter passwords
     Node 2 not visible
       → check QSFP cable,
         confirm IP config
     NCCL fails
       → driver versions MUST be
         identical on both units

🏆 BEST MODELS — What Runs

  1x DGX Spark:
    • Qwen 3.6 35B NVFP4
      → 256k ctx, 110 tok/s
      (Alibaba, April 2026,
       Apache 2.0 license)
    • DeepSeek V4 Flash REAP
      → HF: 0xSero/
        DeepSeek-v4-Flash-REAP
    • Qwen 3.6 27B
      → 256k ctx, 19 tok/s
    • Nemotron Super
      → NVIDIA's own model,
        optimized for DGX Spark

  2x DGX Sparks ← SWEET SPOT
    (recommended by @MiaAI_lab):
    • DeepSeek V4 Flash
      → 1M ctx, 40-45 tok/s
        (1 session)
        ~79 tok/s with 3 concurrent
        sessions (NVFP4 quantization)
        Repo: https://t.co/ZfQSdSBJoe
          deepseek-ai/
          DeepSeek-V4-Flash-DSpark
    • Step-3.7-Flash (StepFun)
      → 256k ctx, image support,
        30 tok/s
        Available via NVIDIA NIM

  4x DGX Sparks:
    • GLM 5.2 NVFP4 (Zhipu)
      → ~20 tok/s, 1M context
    • 2x DeepSeek V4 Flash
      (each on its own 2x Spark pair)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 HOW TO RUN — vLLM Docker
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  A) Single Spark — Best model:

     $ docker run -d --name vllm \
       --ipc=host \
       --restart unless-stopped \
       --gpus all -p 8000:8000 \
       -e HF_TOKEN="$HF_TOKEN" \
       -v ~/.cache/huggingface:\
       /root/.cache/huggingface \
       vllm/vllm-openai:cu130-nightly \
       vllm serve nvidia/\
       NVIDIA-Nemotron-3-Super-\
       120B-A12B-NVFP4 \
       --served-model-name \
         nemotron-3-super \
       --trust-remote-code \
       --max-model-len 131072 \
       --gpu-memory-utilization 0.85 \
       --max-num-seqs 4 \
       --reasoning-parser \
         nemotron_v3 \
       --enable-auto-tool-choice \
       --tool-call-parser \
         qwen3_coder

  B) 2x Spark — Distributed
     inference:

     Add --tensor-parallel-size 2
     to the serve command.

     # Node 1:
     $ docker run -d --name vllm \
       --ipc=host --network=host \
       --gpus all \
       -e HF_TOKEN="$HF_TOKEN" \
       -v ~/.cache/huggingface:\
       /root/.cache/huggingface \
       vllm/vllm-openai:cu130-nightly \
       vllm serve deepseek-ai/\
       DeepSeek-V4-Flash-DSpark \
       --tensor-parallel-size 2 \
       --max-model-len 1048576 \
       --gpu-memory-utilization 0.85 \
       --max-num-seqs 4 \
       --trust-remote-code

     # Node 2 — same model + same
     --tensor-parallel-size 2
     (vLLM auto-discovers the second
      node over 200GbE link)

  C) Quick start — Qwen 3.6 35B
     NVFP4 (1x Spark):

     $ docker run -d --name vllm \
       --ipc=host \
       --gpus all -p 8000:8000 \
       -e HF_TOKEN="$HF_TOKEN" \
       -v ~/.cache/huggingface:\
       /root/.cache/huggingface \
       vllm/vllm-openai:cu130-nightly \
       vllm serve Qwen/\
       Qwen3.6-35B-NVFP4 \
       --max-model-len 262144 \
       --gpu-memory-utilization 0.85 \
       --max-num-seqs 4 \
       --trust-remote-code

💡 CRITICAL FLAGS & TIPS

  • --gpu-memory-utilization 0.85
    → leaves room for OS, kernel
      page cache, container

  • --max-num-seqs 4
    → above 4 concurrent streams,
      bandwidth tax outweighs
      batching gains

  • --max-model-len
    → set per model
      (131072 / 262144 / 1048576)

  • --kv-cache-dtype fp8
    → optional, eases memory strain
      (may affect predictability)

  • NVFP4 → pre-quantized, NEVER
    add --quantization flag, engine
    auto-detects

  • Keep CUDA graphs active
    → default behavior, don't
      disable

  • Quantization/MoE backends
    → default to auto, usually
      optimal

  • Cache models before serving
    → download weights first
      (safetensors = 10-15 min
       default load)

  • Try InstantTensor /
    fastsafetensors
    → faster weight loading

  • Warm-up request after boot
    → fire a tiny request to warm
      JIT kernels (~25s cold start)

  • Pin specific image digest
    → don't rely on moving nightly
      tags in production

🔌 EXPANDING TO BIGGER CLUSTERS

  For 4-8 Sparks, you'll need
  a 200GbE switch:

  • MikroTik CRS504
    → up to 4 Sparks
    (~1% slower vs direct 200Gb)
  • Check MikroTik's lineup for
    8-port 200GbE options

  (Note: specific switch model
   numbers from original source
   could not be independently
   verified — check https://t.co/GXCkIFqxE3
   for current 200GbE lineup)

📚 OFFICIAL RESOURCES

  • NVIDIA DGX Spark page:
    https://t.co/RZg1dX8gfq
    workstations/dgx-spark/

  • Buy ($4,699):
    https://t.co/wSm7BPxbAV
    developer/dgx-spark/

  • Playbooks (GitHub):
    https://t.co/wvU99eF6K0
    dgx-spark-playbooks

  • 2x Connect guide:
    nvidia/connect-two-sparks/

  • vLLM guide:
    https://t.co/fqSjes5oyT
    vllm-dgx-spark

  • User Manual:
    https://t.co/7pTT2eZ7af
    dgx-spark/

  • Quick Start PDF:
    https://t.co/0vDag1IpAB
    Solutions/dgx-spark/
    DGX-Spark-Quick-Start-Guide.pdf

🐦 KEY SOURCES (https://t.co/IrZFzgs2ry)

  • @MiaAI_lab
    — tested models, benchmarks,
      2x sweet spot config
    (34K views on original tweet)

  • @WescheNex1q
    — cluster switch recommendations

  • @mr_r0b0t
    — GitHub playbooks, NCCL tips

  • @sudoingX
    — DGX Spark vs AMD Strix Halo
      benchmarks

  • @aijoey
    — real setup photos + experience

## 2026-06-28 (https://x.com/TraffAlex/status/2071270583271129229)

Every Mac Studio SOLD OUT except
the 96GB. 

The local AI revolution isn't coming.
It's here. And Apple Silicon is winning.

Here's everything — which Mac to buy,
best models with real benchmarks,
working commands, and the math that
makes Mac beat $13K+ GPU rigs.

All sourced from tested community
results on https://t.co/IrZFzgs2ry + official specs.

━━━━━━━━━━━━━━━
🍎 HARDWARE
━━━━━━━━━━━━━━━

M4 Max ($1,999+):
• 14-core CPU → 16-core
• 32-core GPU → 40-core
• 36GB → 64GB unified
• 410–546 GB/s bandwidth
• 512GB → 8TB SSD
• 50-80W AI load
• Near silent

M3 Ultra ($3,999+):
• 28-core CPU → 32-core
• 60-core GPU → 80-core
• 96GB → 192GB → 512GB
• 800–819 GB/s bandwidth
• 1TB → 16TB SSD
• 100-200W AI load
• Near silent

⚠️ No M4 Ultra exists. M4 Max lacks
UltraFusion interconnect.

━━━━━━━━━━━━━━━
⚡ WHY MAC > GPU
━━━━━━━━━━━━━━━

The secret: Unified Memory.

On PC, GPU has separate VRAM (8-24GB).
Models that don't fit won't run.

On Mac, ALL RAM is shared CPU + GPU.
128GB Mac runs 70B models that need
dual RTX 3090 NVLink on PC.

M3 Ultra 512GB runs DeepSeek V3
(671B params) locally.

PC equivalent?
17× RTX 3090 = $13,000+
+ 3.7kW power + cooling.

Mac M4 Max:
• 128GB unified, 546 GB/s
• 70B Q4 → ~15 tok/s
• 50-80W, silent, ~$3,000

Mac M3 Ultra:
• 512GB unified, 819 GB/s
• 70B Q4 → ~25 tok/s
• 100-200W, silent, ~$10,000

RTX 5090:
• 32GB VRAM, 1792 GB/s
• 70B Q4 → won't fit
• 575W, loud, ~$2,200

Mac doesn't win on speed.
It wins on CAPACITY + SILENCE.

━━━━━━━━━━━━━━━
🏆 BEST MODELS
━━━━━━━━━━━━━━━

M4 Max 64GB:
• Qwen 3.6-35B-A3B Q4 ⭐
  ~20GB, 35-55 tok/s
  3B active/token, 262K ctx
  → 2026 DEFAULT for Mac

• Qwen 3.6-27B Q4
  ~16.8GB, 18-28 tok/s
  Best coding (77.2 SWE-bench)

• Gemma 4 26B-A4B Q4
  ~15GB, 30-45 tok/s, 256K ctx

• Llama 3.3 70B Q4
  ~40GB, 8-15 tok/s

M4 Max 128GB:
• Qwen 3.6-35B-A3B bf16
  ~70GB, 20-35 tok/s full precision

• Llama 4 Scout Q4 (MoE)
  ~58GB, 25-35 tok/s, 10M ctx

• Llama 3.3 70B Q6
  ~55GB, 8-15 tok/s max quality

M3 Ultra 192GB:
• DeepSeek V4-Flash Q4-Q6
  140-180GB, frontier MoE

• Qwen3 235B-A22B Q6-Q8
  140-180GB, 4-8 tok/s

M3 Ultra 512GB:
• Llama 3.1 405B Q3
  ~150GB, 2-4 tok/s frontier

• DeepSeek V3 Q4 (671B)
  466GB peak, 21→5.8 tok/s
  Runs on Mac. 17× RTX 3090 equiv.

━━━━━━━━━━━━━━━
📊 BENCHMARKS
━━━━━━━━━━━━━━━

@ivanfioravanti ROYAL RUMBLE
(66K views)
Ornith-1.0-35B Q8 via llama.cpp

M3 Ultra 512GB → DGX Spark 128GB:
• 1K ctx: 87 t/s vs 58 t/s
• 4K ctx: 77 t/s vs 58 t/s
• 16K ctx: 68 t/s vs 54 t/s
• 32K ctx: 58 t/s vs 50 t/s
• 64K ctx: 47 t/s vs 44 t/s
• 128K ctx: 33 t/s vs 35 t/s

→ Mac wins small/mid context
→ Spark holds steady at large ctx

DeepSeek V3 M3 Ultra 512GB (MLX):
• 69 tok ctx: 21 tok/s generate
• 1.1K tok ctx: 17.8 tok/s
• 15.7K tok ctx: 5.8 tok/s

MLX vs Ollama (M4 Max):
• Llama 8B: 48 vs 42 tok/s
• Qwen MoE: 55 vs 45 tok/s
• Llama 70B: ~18 vs ~15 tok/s
→ Big models converge
→ Bandwidth is the bottleneck

━━━━━━━━━━━━━━━
🚀 HOW TO RUN
━━━━━━━━━━━━━━━

Ollama (easiest):
$ curl -fsSL https://t.co/VFyIyXed51 | sh
$ ollama run qwen3.6:35b-a3b-q4_K_M
$ ollama run qwen3.6:27b
$ ollama run llama3.3:70b
$ ollama run gemma4:26b-a4b-q4

MLX-LM (fastest):
$ pip install mlx-lm
$ mlx_lm.generate \
  --model mlx-community/Qwen3.6-35B-A3B-4bit \
  --prompt "Hello"

llama.cpp (max control):
$ llama-server -hf MODEL \
  -c 65536 -fa on --swa-full \
  --n-gpu-layers 999 --no-mmap \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --batch-size 2048 \
  --ubatch-size 2048 \
  --threads 20 \
  --ctx-size 160000

LM Studio (best GUI):
→ Native Apple Silicon app
→ MLX + llama.cpp backend
→ Visual model browsing

━━━━━━━━━━━━━━━
💡 KEY INSIGHTS
━━━━━━━━━━━━━━━

🧠 MoE = Game Changer
Qwen 3.6-35B-A3B: 35B total,
only 3B ACTIVE per token.
File ~20GB, feels like 3B model.
262K context. Apache 2.0.
THIS is the 2026 default.

📏 Bandwidth > Generation
M3 Max (400 GB/s) is FASTER
than M4 Pro (273 GB/s) on LLMs.
Check bandwidth, not chip gen.

💰 Quantization:
• 64GB: Q4_K_M for 70B
• 128GB: Q5_K_M or Q8_0
• 192GB+: bf16 for MoE

⚡ Performance:
• Close Chrome/Electron apps
• Reduce ctx: --num-ctx 4096
• Lower quant = faster
• Warm-up after boot (~25s)

🔋 Annual Power (8hr/day):
• M4 Max: ~$42-63
• M3 Ultra: ~$79-158
• RTX 4090: ~$276-355
• 2× RTX 3090: ~$552-631

━━━━━━━━━━━━━━━
🛒 BUYING GUIDE
━━━━━━━━━━━━━━━

$1,599–1,999 → Mac Mini M4 Pro 48GB
35B MoE easy, 70B tight

$2,500–3,500 → Mac Studio M4 Max 64GB
70B Q4 at 8-15 t/s
Qwen MoE at 35-55 t/s

$3,500+ → M4 Max 128GB / M3 Ultra
70B Q6/Q8, multiple models

$10,000 → M3 Ultra 512GB
405B, DeepSeek V3, anything
$10K vs $13K+ for 17× RTX 3090

━━━━━━━━━━━━━━━
🔮 NEXT: M5 Ultra
━━━━━━━━━━━━━━━

@Youssofal_ (36.9K views)
• Two M5 Max fused
• 768GB unified
• 1,228 GB/s bandwidth
• Expected ~$25K (Oct 2026+)

MTPLX predictions:
• Qwen 3.6 27B Q4 → 125-150 TPS
• GLM 5.2 Q4 → 28 TPS
• Current M5 Max → 50-60 TPS
• Fused matmul kernel → 75 TPS

⚠️ Based on unreleased kernel math

━━━━━━━━━━━━━━━
🔌 MEMORY CHEAT SHEET
━━━━━━━━━━━━━━━

Qwen 3.5 9B → 16GB min, ~6.6GB Q4
Qwen 3 14B → 16GB min, ~9GB Q4
Qwen 3.6-27B → 24GB min, ~16.8GB Q4
Qwen 3.6-35B-A3B ⭐ → 32GB, ~20GB
Gemma 4 26B-A4B → 24GB, ~15GB Q4
Llama 3.3 70B → 48GB, ~40GB Q4
Llama 4 Scout → 64GB, ~58GB Q4
DeepSeek V4-Flash → 96GB, ~140GB Q4
Qwen3 235B-A22B → 128GB, ~88GB Q4
Llama 405B → 128GB, ~150GB Q3

━━━━━━━━━━━━━━━
📚 RESOURCES
━━━━━━━━━━━━━━━

https://t.co/39Nywnq8ug
https://t.co/e8A7FFwUw7
https://t.co/mH4OFJrmFT
https://t.co/6tuvJtGqG4
https://t.co/QcFbdzk9dW
https://t.co/uZIWTLdzsw

━━━━━━━━━━━━━━━
🐦 https://t.co/S7Jj8gA15K SOURCES
━━━━━━━━━━━━━━━

@AlexFinn (136.5K)
→ Mac Studio sold out

@0xSero (74.9K)
→ Best models by VRAM tier

@ivanfioravanti (66K)
→ M3 Ultra vs Spark benchmarks

@Youssofal_ (36.9K)
→ M5 Ultra math

@alpinesnow23 (3.2K)
→ M5 Max 128GB AI stack

https://t.co/d9tPzp63wA
→ Best Local LLMs 2026

https://t.co/uLM5OQkrjj
→ DeepSeek V3 benchmarks

## 2026-06-29 (https://x.com/TraffAlex/status/2071638856328220776)

RTX 5090 — $3,999, 32GB, 160 tok/s.
Mac M4 Max — $3,500, 64GB, 55 tok/s.
DGX Spark — $4,699, 128GB, 60 tok/s.

One is fastest. One is silent.
One is the upgrade path for both.

Real June 2026 prices, real
benchmarks. Here's EVERYTHING —
which GPU, which Mac, or the
DGX Spark YOU should buy:

━━━━━━━━━━━━━━━━━━
🎯 THE THREE PATHS
━━━━━━━━━━━━━━━━━━

1. 🟢 GPU RIG (NVIDIA consumer cards)
   → Cheapest entry, fastest raw speed
   → Loud, hot, complex multi-GPU setups

2. 🔵 DGX SPARK (NVIDIA dev appliance)
   → $4,699, 128GB unified, 1 PFLOPS FP4
   → Clusterable, enterprise-grade, compact

3. 🍎 MAC STUDIO (Apple Silicon)
   → Silent, unified memory, $2.5K-$14K
   → Runs 671B models nobody else can touch

━━━━━━━━━━━━━━━━━━
⚠️ IMPORTANT — Price Reality Check
━━━━━━━━━━━━━━━━━━

⚠️ RTX 5090 has $1,999 MSRP but real price
   in June 2026 is $3,658-$4,329 on Amazon
   (~$3,999 used). MSRP is meaningless.

⚠️ Apple raised Mac prices 25-33% in June
   2026. M3 Ultra 512GB peaked at $14,299
   and is now DISCONTINUED / sold out.

⚠️ All prices below are REAL market prices
   in June 2026, not MSRP.

━━━━━━━━━━━━━━━━━━
💰 PRICE TIERS — What You Actually Pay
━━━━━━━━━━━━━━━━━━

$1,050 — Single used RTX 3090 (24GB)
  → Cheapest path to 24GB VRAM
  → Runs 30B-35B MoE at full speed

$2,100 — 2x used RTX 3090 (48GB)
  → Best VRAM/$ ratio
  → Runs 70B-80B models (quantized)

$2,500 — Mac Studio M4 Max 36GB (base)
  → Silent, 35B MoE at 35-55 tok/s

$3,500 — Mac Studio M4 Max 64GB
  → 70B Q4 inference, still near silent

$3,999 — RTX 5090 (32GB) actual price
  → Fastest single consumer GPU
  → 1,792 GB/s, 575W, no NVLink

$4,699 — DGX Spark (128GB unified)
  → The bridge between GPU and Mac
  → NVFP4, 200GbE, clusterable

$5,299 — Mac Studio M3 Ultra 96GB (base)
  → Big MoE models (DeepSeek V4-Flash)

$5,958 — RTX 5090 + RTX 4090 (56GB combo)
  → Killed $430/month OpenAI bill
  → (@gippp69 under-desk lab)

$7,999 — 2x RTX 5090 (64GB via PCIe)
  → Blazing speed, no unified memory
  → ~1,150W, serious cooling needed

$9,449 — 2x DGX Spark bundle + cable
  → 256GB unified, 200GbE fabric
  → Sweet spot for distributed inference

$14,299 — Mac M3 Ultra 512GB
  → Runs DeepSeek V3 (671B params)
  → ⚠️ DISCONTINUED, sold out everywhere
  → Refurb ~$14,609 on eBay

$17,850 — 17x RTX 3090 rig
  → What PC needs to match 512GB Mac
  → 3.7kW power + enterprise cooling
  → $13K+ was old pricing, now ~$17.8K

━━━━━━━━━━━━━━━━━━
📊 BENCHMARKS — Qwen3.6 35B-A3B Q4
━━━━━━━━━━━━━━━━━━

(From @stevibe — 391.3K views)

RTX 3090 ($1,050)     → 49.78 tok/s, TTFT 852ms
RTX 4090 ($2,470)     → 118.93 tok/s, TTFT 686ms
RTX 5090 ($3,999)     → 160.37 tok/s, TTFT 409ms
DGX Spark ($4,699)    → 59.98 tok/s, TTFT 228ms

(From @sudoingX — 194.2K views, llama.cpp)

RTX 3090 → 112 tok/s (MoE, active params only!)

(Mac M4 Max 64GB — community tested)

Qwen3.6-35B-A3B Q4 → 35-55 tok/s

━━━━━━━━━━━━━━━━━━
📊 BENCHMARKS — Qwen3.5:27B

(From @xdgjp — single card, linear scaling)

RTX 3090 → ~20 tok/s
RTX 4090 → ~40 tok/s
RTX 5090 → ~60 tok/s

(From @YebHavinga — dual 3090, vLLM TP=2)

2x RTX 3090 → 38-48 tok/s
  → Single 5090: ~44 tok/s at 32K
  → Dual 3090 nearly matches single 5090
  → For 1/4 the price

━━━━━━━━━━━━━━━━━━
🏆 WHAT EACH PATH RUNS BEST
━━━━━━━━━━━━━━━━━━

SINGLE RTX 3090 ($1,050 used, 24GB):
  • Qwen 3.5 27B Q4 → 20-35 tok/s
  • Qwen 3.5 35B MoE Q4 → 112 tok/s ⚡
  • Qwen 3.6 35B-A3B Q4 → ~50 tok/s
  • Llama 3.3 70B Q3 → tight, possible
  • 350W, ~$13/month electricity

DUAL RTX 3090 (~$2,100 used, 48GB):
  • Qwen3-Coder 80B Q4 → 46 tok/s
  • Qwen 3.5-27B vLLM TP=2 → 38-48 tok/s
  • Qwen 3.6-27B AutoRound → 79 tok/s
    (code), 56 tok/s (narrative)
  • 700W+, needs quality PSU + case

SINGLE RTX 5090 ($3,999 actual, 32GB):
  • Qwen3.6 35B-A3B → 160 tok/s ⚡
  • Qwen3.5:27B → ~60 tok/s
  • Qwen 3.5 9B → 50+ tok/s
  • 575W, fastest single card period
  • No NVLink — multi-GPU via PCIe only

DUAL RTX 5090 (~$7,999, 64GB):
  • Llama 3.3 70B Q4 → comfortable
  • DeepSeek V4-Flash Q4 → fits
  • 1,150W+, serious power + cooling

RTX 5090 + 4090 (~$5,958, 56GB):
  • RTX 5090 + RTX 4090 in one box
  • Proxmox + local Qwen/DeepSeek/Llama
  • Killed $430/month OpenAI bill
  • (@gippp69 — 69.8K views)

10x RTX 4090 (~$25K+, 240GB VRAM):
  • 288GB fast VRAM total
  • Multiple large LLMs in parallel
  • $340/month electricity vs $11K/month
    in closed API bills
  • (@marfinxx — enterprise home lab)

DGX SPARK ($4,699, 128GB unified):
  • Qwen 3.6 35B NVFP4 → 110 tok/s
  • DeepSeek V4 Flash (1M ctx)
    → 40-45 tok/s (single session)
  • Nemotron Super → optimized native
  • 2x Spark cluster: ~79 tok/s
    (3 concurrent sessions, NVFP4)
  • Compact, 1 PFLOPS FP4, 200GbE

MAC STUDIO M4 MAX 36GB ($2,499 base):
  • Qwen 3.6-35B-A3B Q4 → 35-55 tok/s
  • Llama 3.3 70B Q4 → 8-15 tok/s
  • 50-80W, near silent

MAC STUDIO M4 MAX 64GB ($3,500):
  • Qwen 3.6-35B-A3B bf16 → 20-35 tok/s
  • Llama 4 Scout Q4 → 25-35 tok/s
  • Llama 3.3 70B Q6 → 8-15 tok/s

MAC STUDIO M3 ULTRA 96GB ($5,299+):
  • DeepSeek V4-Flash Q4-Q6 → frontier
  • Qwen3 235B-A22B Q6-Q8 → 4-8 tok/s
  • 100-200W, near silent

MAC STUDIO M3 ULTRA 512GB ($14,299):
  ⚠️ DISCONTINUED — sold out everywhere
  • Llama 3.1 405B Q3 → 2-4 tok/s
  • DeepSeek V3 Q4 (671B params!) → 5.8 tok/s
  • Beats $17K+ 17× RTX 3090 rig
  • Was the king. Now gone.

━━━━━━━━━━━━━━━━━━
⚡ SPEED COMPARISON — tok/s
━━━━━━━━━━━━━━━━━━

Qwen3.6 35B-A3B (Q4, single card/unit):
  RTX 5090 ($3,999)     → 160 tok/s ⚡ fastest
  RTX 4090 ($2,470)     → 119 tok/s
  DGX Spark ($4,699)    → 60 tok/s
  RTX 3090 ($1,050)     → 50 tok/s
  Mac M4 Max 64GB       → 35-55 tok/s

Qwen3.5 27B (single card/unit):
  RTX 5090 → 60 tok/s
  2x RTX 3090 → 38-48 tok/s
  RTX 4090 → 40 tok/s
  RTX 3090 → 20 tok/s

MoE (Qwen3.5 35B-A3B active only):
  RTX 3090 → 112 tok/s (only 3B active!)
  Mac M4 Max → 35-55 tok/s

━━━━━━━━━━━━━━━━━━
🧠 CAPACITY COMPARISON — What Fits
━━━━━━━━━━━━━━━━━━

24GB (single 3090/4090):
  → 30B Q4 comfortable
  → 70B Q3 tight (offload needed)

32GB (single 5090):
  → 30B Q4-Q5 comfortable
  → 70B Q4 tight

48GB (dual 3090):
  → 80B Q4 fits (full VRAM)
  → 70B Q4 comfortable

56GB (5090 + 4090 combo):
  → 70B Q4 with room for ctx
  → Separate models per GPU

64GB (dual 5090 / Mac 64GB):
  → 70B Q4-Q6 comfortable
  → 120B Q4 possible

128GB (DGX Spark / Mac 128GB):
  → 120B bf16 runs
  → 235B Q4 possible (Mac)
  → Spark: 1M context DeepSeek V4

512GB (Mac M3 Ultra — discontinued):
  → 671B params ran locally
  → Nothing else at this price (was)

━━━━━━━━━━━━━━━━━━
🔇 POWER & NOISE COMPARISON
━━━━━━━━━━━━━━━━━━

Annual cost (8hr/day, $0.15/kWh, 365 days):
  Mac M4 Max       → ~$42/year   ($3.50/mo)
  DGX Spark        → ~$70/year   ($5.80/mo, est.)
  Mac M3 Ultra     → ~$88/year   ($7.30/mo)
  RTX 3090         → ~$153/year  ($12.80/mo)
  2x RTX 3090      → ~$307/year  ($25.60/mo)
  RTX 4090         → ~$197/year  ($16.40/mo)
  RTX 5090         → ~$252/year  ($21.00/mo)
  2x RTX 5090      → ~$504/year  ($42.00/mo)
  10x RTX 4090     → ~$1,970/year ($164/mo)
  17x RTX 3090     → ~$2,600/year ($217/mo)

Noise level:
  Mac Studio       → near silent 🤫
  DGX Spark        → low fan noise
  Single GPU       → quiet to moderate
  Dual GPU         → noticeable fan noise
  10+ GPU rack     → loud 📢

━━━━━━━━━━━━━━━━━━
🤔 WHICH ONE DO YOU NEED?
━━━━━━━━━━━━━━━━━━

"Cheapest possible entry":
  → Used RTX 3090 ($1,050)
  → 24GB, 35B MoE at 112 tok/s

"Best speed per dollar":
  → Used dual RTX 3090 ($2,100)
  → 48GB, nearly matches 5090 speed
  → For 50% of the price

"Silent workstation + AI":
  → Mac Studio M4 Max 64GB ($3,500)
  → Also edits video, writes code, runs AI

"Maximum raw inference speed":
  → RTX 5090 ($3,999)
  → 160 tok/s on 35B-A3B, fastest period

"Big models, no compromises":
  → DGX Spark ($4,699)
  → 128GB unified, clusterable
  → Actually available (Mac 512GB is gone)

"Maximum parallel inference":
  → Multi-GPU rig (2x-10x cards)
  → Separate models on separate GPUs
  → $2K-$25K+ depending on scale

"If you find a M3 Ultra 512GB in stock":
  → Grab it. They discontinued it.
  → $14,299 is the price now.

━━━━━━━━━━━━━━━━━━
💡 KEY INSIGHTS
━━━━━━━━━━━━━━━━━━

🔥 GPU RIG wins on RAW SPEED
  RTX 5090 at 160 tok/s beats
  everything in single-card inference.
  But 32GB VRAM caps model size.
  Real price: $3,999 (not $1,999).

🧠 MAC won on CAPACITY + SILENCE
  512GB unified at $14K was unmatched.
  Ran 671B models. Used $7/month
  in electricity. DISCONTINUED.
  M4 Max 64GB remains the value play.

🔗 DGX SPARK wins on AVAILABILITY
  Actually in stock at $4,699.
  128GB unified. Cluster to 2x/4x/8x.
  Mac 512GB is gone. Spark is the new
  "big unified memory" option.

💰 Dual RTX 3090 = Best VRAM/$ VALUE
  2x used RTX 3090 ($2,100) = 48GB
  → Beats single 5090 on capacity
  → Nearly matches on speed (vLLM TP=2)
  → 1/4 the price of single 5090

📈 MoE CHANGES EVERYTHING
  Qwen3.6-35B-A3B: 35B total,
  only 3B active per token.
  Runs at 112 tok/s on a $1,050 3090.
  THIS is the sweet spot for GPU rigs.

📉 Mac 512GB is GONE
  The M3 Ultra 512GB was the undisputed
  king for local AI. Apple discontinued it.
  If you see one — buy it. They're not
  making more. M5 Ultra expected Oct 2026.

💸 RTX 5090 MSRP is FICTION
  Listed at $1,999. Real price $3,999.
  NVIDIA raised prices, scalpers scalped,
  supply never met demand. The $1,999
  number is meaningless in June 2026.

━━━━━━━━━━━━━━━━━━
📊 QUICK REFERENCE TABLE
━━━━━━━━━━━━━━━━━━

Setup              $        VRAM  ⚡35B-A3B  Watts
━━━━━━━━━━━━━━━━━━
RTX 3090 (used)    1,050    24GB   50 tok/s   350
2x RTX 3090        2,100    48GB  38-48 t/s   700
Mac M4 Max 36GB    2,499    36GB  35-55 t/s    80
Mac M4 Max 64GB    3,500    64GB  35-55 t/s    80
RTX 5090 (actual)  3,999    32GB  160 tok/s   575
DGX Spark          4,699   128GB   60 tok/s   100
Mac M3 Ultra 96GB  5,299    96GB  8-15 t/s    200
                    (70B Q4)
2x RTX 5090        7,999    64GB  ~280 t/s*  1150
                    *(dual TP)
Mac M3 Ultra 512GB 14,299   512GB  2-4 t/s    200
                    (405B Q3, DISCONTINUED)

━━━━━━━━━━━━━━━━━━
🔌 THE REAL UPGRADE PATH
━━━━━━━━━━━━━━━━━━

$1,050 → Single RTX 3090 (used)
  Learn local AI. Run 30B-35B MoE.
  Understand quantization, context,
  frameworks (ollama, vLLM, llama.cpp).

$2,100 → Add second RTX 3090
  48GB VRAM. Run 70B-80B models.
  Learn tensor parallelism, vLLM.

$4,699 → DGX Spark (replace or add)
  128GB unified. Cluster-capable.
  Run DeepSeek V4 Flash, 1M context.
  ⬅️ THIS is where you land when
      you hit the multi-GPU VRAM ceiling.

$9,449 → 2x DGX Spark cluster
  256GB unified, 200GbE interconnect.
  Run DeepSeek V4, GLM 5.2, anything.

$14,299+ → Mac M3 Ultra 512GB
  (if you can find one — discontinued)
  OR wait for M5 Ultra (expected Oct 2026)
  OR 4x DGX Spark cluster ($18,898)

━━━━━━━━━━━━━━━━━━
📚 RESOURCES
━━━━━━━━━━━━━━━━━━

GPU pricing & benchmarks:
  https://t.co/0OHnbCpcyk → real-time price tracker
  https://t.co/Nl8w2FYxj4
  https://t.co/LRZOwpLae3

NVIDIA DGX Spark:
  https://t.co/EBdvOBgDh7
    dgx-spark/
  https://t.co/zmpdCAgGHY
  https://t.co/aymDB7BAVf

Mac Studio AI:
  https://t.co/39Nywnq8ug
  https://t.co/e8A7FFwUw7
  https://t.co/mH4OFJrmFT

Communities:
  https://t.co/d9tPzp63wA → Best Local LLMs 2026
  https://t.co/T3no5AEFHa → DGX Spark vs Mac

━━━━━━━━━━━━━━━━━━
🐦 KEY SOURCES (https://t.co/IrZFzgs2ry)
━━━━━━━━━━━━━━━━━━

@stevibe (391.3K views)
  → RTX 3090/4090/5090/Spark vs
     Qwen3.6 35B-A3B benchmarks

@sudoingX (194.2K views)
  → GPU → model recommendations
     (3060→3090→2x3090 tested)

@xdgjp
  → RTX 3090/4090/5090 Qwen3.5:27B
     linear scaling benchmarks

@YebHavinga
  → Dual 3090 vLLM benchmarks
     (38-48 tok/s, nearly = 5090)

@MemoryReboot_ (5.5K views)
  → Dual 3090 Qwen3.6-27B AutoRound
     (79 tok/s code, 56 tok/s narrative)

@gippp69 (69.8K views)
  → RTX 5090 + 4090 under-desk lab
     killed $430/month OpenAI bill

@marfinxx
  → 10x RTX 4090 rig, 288GB VRAM
     $340/month vs $11,000/month API

@stableAPY (735 views)
  → Multi-model setup (3090 + 3060)
     4 Qwen models, Hermes agents

━━━━━━━━━━━━━━━━━━
⚠️ UNVERIFIED CLAIMS
━━━━━━━━━━━━━━━━━━

  • 160 tok/s RTX 5090 on 35B-A3B
    → @stevibe's benchmark, ollama
      backend (not vLLM/SGLang)
    → vLLM may push higher
  • Dual 5090 ~280 tok/s → estimated
    from single-card scaling, not
    independently tested
  • DGX Spark ~100W → estimated from
    official TDP range, not measured
    under sustained AI load
  • Specific electricity costs → based
    on $0.15/kWh US average, varies
    significantly by region
  • RTX 5090 actual price $3,658-$4,329
    → confirmed by multiple trackers
    (bestvaluegpu, GPU Poet, Tom's HW)
  • M3 Ultra 512GB discontinued → per
    Macworld, Best Buy listings, Reddit
  • Apple June 2026 price hikes → per
    https://t.co/T3no5AEFHa, Reddit

━━━━━━━━━━━━━━━━━━
⚠️ KNOWN LIMITATIONS
━━━━━━━━━━━━━━━━━━

GPU rigs:
  • No unified memory → model must fit
    in single card's VRAM (or use TP)
  • RTX 5090 has NO NVLink support
  • Multi-GPU via PCIe = bandwidth tax
  • Power, noise, heat are real factors
  • Used cards = no warranty, mining risk

DGX Spark:
  • 128GB great but not 512GB
  • $4,699 per unit (2x = $9,449)
  • 200GbE switch needed for 4+ units
  • Linux-only, less "just works"
  • Original $3,999 price is gone

Mac Studio:
  • Slower raw inference than GPU rigs
  • M3 Ultra 512GB discontinued
  • M4 Max maxes at 64GB (not 128GB)
  • Apple raised prices 25-33% June 2026
  • No FP8/BF16 native acceleration
    (uses Apple's MLX quantization)
  • Can't do NVIDIA ecosystem (CUDA,
    TensorRT-LLM, Triton)
