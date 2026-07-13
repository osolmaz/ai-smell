# @_avichawla — long-form tweets

## 2026-06-13 (https://x.com/_avichawla/status/2065727218991735000)

Karpathy said something you'll regret ignoring:

"Remove yourself as the bottleneck. Maximize your leverage. Put in very few tokens, and a huge amount of stuff happens on your behalf."

Loop engineering is the exact thing that does that.

In a hand-run session, the operator handles two things:

- deciding what the agent runs next
- and checking its output before the next step

Both are manual, and both decide how far the agent gets on its own without the operator.

Loop engineering moves both steps into the system.

A core operating structure surrounds the loop, and the diagram below depicts it.

- A schedule decides what to run
- Loop is the maker that produces the work
- A separate checker agent grades the output
- A file on disk holds the state they both read.

The loop runs until either done, max iterations, or an exhausted budget.

Here are some practical engineering considerations:

1) A model grading its own output justifies what it already did instead of catching where it failed.

That's why a separate checker's findings return to the maker as the next instruction. And the cycle repeats until the checker finds nothing left to fix.

2) A loop with no stop condition burns tokens, and the cost climbs fast once sub-agents and long runs add up.

That's why the exit must be set before the loop runs, not while it is running.

A simple exit could be:
↳ fix only the major issues, run one final pass, and stop after two loops, with "all tests pass and lint clean" as the rule that ends it.

3) State has to live on disk, not in context.

The model forgets everything between runs, so an MD file or a knowledge graph holds what is done and what is still open.

Each run reads it and writes back to it, which lets a loop pick up again after days.

4) The lower the verification bar, the safer the loop.

Boring, repetitive checks like a stale version string or a missing test are trivial to verify, so a loop runs them with little risk while the operator is away.

Judgment-heavy work is loopable too, but only as far as the checker can confirm the result.

Let's look at how an unattended loop fails in two ways.

1) It reports done when nothing is actually verified.

The separate checker exists to prevent it, but it merges code faster than anyone reads it, so over weeks, the team stops understanding its own codebase while every check stays green.

Green tests say the code passed the tests, not that anyone knows what shipped. Someone still has to read what the loop merges.

2) The checker keeps a running loop honest, but it only catches failures inside a run.

The harness around the loop, like the prompts, tools, and checks wrapped around the model, still drifts and breaks in production as models change.

That repair loop is usually run by hand based on observability traces.

My co-founder wrote a detailed walkthrough (with code) on making that harness repair itself, where a failing trace gets diagnosed, the fix is verified against the exact input that failed, and the failure is locked as a regression test so it cannot recur.

Read it below.

## 2026-06-16 (https://x.com/_avichawla/status/2066803525007691808)

Researchers made KMeans 200x faster.

And the new technique also beats approaches like cuML and FAISS.

Flash-KMeans is an IO-aware implementation of exact KMeans that redesigns the algorithm around modern GPU bottlenecks.

By attacking the memory bottlenecks directly, Flash-KMeans achieves:

- 33x speedup over cuML
- 200x speedup over FAISS

This speedup comes from how it moves through GPU memory.

Standard KMeans runs in two steps, and both are bottlenecked by reads and writes to GPU memory:

1) The first step matches every point to its nearest centroid.

Standard KMeans computes the full point-to-centroid distance matrix, writes it out to GPU memory, then reads it back to find each nearest centroid. That write-then-read round trip is the bottleneck.

Flash-KMeans combines the distance calculation with the nearest-centroid step, so the result is computed on-chip and the full matrix is never written out.

2) The second step recomputes each centroid by averaging the points assigned to it.

Standard KMeans has thousands of threads writing into the same centroid slots at once, so they stall waiting for their turn.

Flash-KMeans sorts points by cluster first, turning scattered writes into sequential reductions that read and write memory in one efficient pass.

Using these two optimizations at the million-scale, Flash-KMeans completes a standard KMeans iteration in a few milliseconds.

The video below depicts this in action.

Several reasons why this is important:

KMeans has always been an offline primitive. Something you run once to preprocess data and move on.

These speedups make the approach viable in several runtime-critical systems.

↳ Vector indices like FAISS use KMeans to build search indices. Faster KMeans means you can re-index dynamically as data changes.

↳ LLM quantization methods need KMeans to find optimal weight codebooks, per layer, repeatedly. What takes hours could now take minutes.

↳ MoE models need fast token routing at inference time. Flash-KMeans makes it viable to run this inside the inference loop, not just in preprocessing.

I have shared the paper in the replies.

That said, memory is the real constraint Flash-KMeans solves, and the problem is not just limited to clustering. The vectors a RAG system stores after indexing create similar bottlenecks.

I wrote a detailed walkthrough recently on cutting this vector memory by 32x with binary quantization, querying 36M+ vectors in a few milliseconds.

Read it below.

## 2026-07-05 (https://x.com/_avichawla/status/2073746091795960237)

Stanford researchers did it again.

They just built the agent-native version of Git.

When an agent works on a longer task, the run builds up a lot of state.

This includes files edited/created, a dev server, a database, installed packages, KV cache, etc.

Say the agent is at step 10 and makes a mistake, maybe it misreads a traceback and rewrites a file that was actually fine.

The tests start failing, and the run goes off track, although everything through step eight was correct.

By default, the agent just tries to fix it, which creates more edits and tool calls. This burns more tokens and grows the context.

The other options are a person stepping in to redirect it or restarting the whole run from step one.

That's wasteful, because it pays for every model/tool call again and re-prefills the context. Moreover, since an agent's run is non-deterministic, it doesn't reproduce the same early steps anyway.

The reason it's hard to just jump back exactly to a previous correct step and resume from there is that the trajectory is only a message log.

It records what the agent said and which tools it called, but not the live state underneath.

That state includes things like memory, open file handles, child processes, installed packages, /tmp, and KV cache. None of that is in the log.

Git can version the files, but it doesn't snapshot the running process or the KV cache. Checking out step eight moves the files back, but the process is still sitting in step-ten memory with a cold cache.

Shepherd is a runtime layer by Stanford that records the run as a trace of typed events rather than a flat log.

Each agent-environment interaction becomes a commit, similar to Git, but it tracks the live run.

Its commit includes the agent process and the filesystem together, copy-on-write, so a branch carries the actual state and not just the files.

Going back to a previous step is then a single call that forks from that commit and continues from the exact state.

The copy-on-write fork is roughly five times faster than docker commit, and because the prompt prefix through step eight is unchanged, the KV cache is reused over 95% on replay, so early steps aren't reprocessed again.

Once the run can be forked, a meta-agent can sit on top and operate it. It watches the trace and reverts as soon as it looks wrong, before the bad write is committed.

In practice, it's just Python calling fork, replay, and revert on the trace, rather than a separate control plane wired into the harness.

Not everything is reversible though.

Files and sandbox changes undo themselves, but a database write has no automatic undo, so it needs a matching undo step set up in advance.

Something external, like a sent email or a real charge, can't be undone, so the supervisor's job there is to catch it before it fires.

They tested this on a few public benchmarks. On CooperBench, where two agents work on the same codebase, adding a live supervisor took the pair-coding pass rate from 28.8% to 54.7%.

It's still early and labeled alpha. The benefit mostly shows up when a run gets branched a lot over a heavy sandbox state, which is exactly where restarting wastes the most tokens and time.

If Git was made to make file changes reversible, Shepherd is trying to do the same thing for a live agent run.

Shepherd Repo: https://t.co/5e8W5oxY6F

(don't forget to star it ⭐ )

That said, Shepherd reverts a bad step inside a run. The harness around it, the prompts, tools, and checks the supervisor relies on, still drifts across runs as models and dependencies change.

Akshay wrote about making that harness repair itself, where a failing trace gets diagnosed, the fix is verified against the exact input that failed, and the failure is locked as a regression test so it can't recur.

Read it below.

## 2026-07-12 (https://x.com/_avichawla/status/2076253133517598859)

NVIDIA researchers built a new transformer variant.

One small change to the layers made:

- decoding 1.7x faster
- long-reasoning accuracy up 6.5 points

In a typical transformer architecture, every attention layer computes Q, K, and V.

NVIDIA's tweak adds a fourth projection, which predicts what the next layer will need.

To understand why they did this, let's first see what happens in a Transformer architecture during inference right now.

Sparse attention was an attempt to handle long-context inference. Instead of attending to every cached token, modern designs score the KV cache in blocks, keep the top-k, and attend only to those.

That cuts attention compute and bandwidth, but this still leaves us with two problems.

> First, the KV cache still grows with every generated token.

At 100K+ context, it no longer fits in GPU memory and gets offloaded to CPU RAM.

Now every layer must first copy its selected KV blocks from CPU memory back to the GPU. That copy is slow, the GPU sits idle while it waits, and the stall repeats at every layer of every decode step.

> Second, the selection step itself is not free.

Standard selectors score every candidate block with every query head in a GQA group (grouped-query attention, where several query heads share one KV head), then softmax each head's scores and sum them across the group.

During decode, the sparse attention itself is cheap because there is only one query token.

But the expensive part is deciding which blocks to attend to, and that cost keeps growing with context length.

Both problems trace back to the same design in today's sparse attention methods, i.e., the attention query drives the block selection.

Selection needs the query vector Q, and Q only exists once its layer is already running. By then, it's too late to fetch anything early.

The query also drags its multi-head layout into selection, so all that scoring computation runs just to make one top-k decision.

A recent paper from NVIDIA and MIT called SparDA breaks this coupling with one architectural change.

Each layer now emits four projections instead of three:

↳ Q, K, V, and a Forecast.

The Forecast from layer L predicts which KV blocks layer L+1 will need.

Layer L+1's own query performs the sparse attention over those selected blocks.

This one change fixes both problems.

Since the next layer's block set is known while the current layer is still computing, the runtime fetches those blocks from CPU memory on a separate CUDA stream.

The copy overlaps with the current layer's compute, so the GPU no longer waits for it.

And since the Forecast is separate from the attention query, it doesn't need one score per query head.

SparDA uses one Forecast head per GQA group, which removes the per-query-head scoring loop and skips the softmax step entirely.

DeepSeek did something similar in DSA, where a small indexer picks important tokens instead of the query doing it.

SparDA applies the same idea to blocks and adds the prefetch angle that DSA doesn't touch.

The cost of the change is small.

The Forecast adds just 33.5M parameters on an 8B model (0.41%), and only those projections are trained, using a KL loss that matches the original selector's block distribution.

On MiniCPM4.1-8B and NOSA-8B, accuracy matches or beats the sparse baseline, with NOSA-8B gaining +6.5 on long reasoning.

Prefill runs up to 1.25x faster and decode up to 1.7x faster than the sparse offload baseline.

There's one more benefit.

Because prefetch hides the offload cost, most of the KV cache can live in CPU RAM, and the freed GPU memory fits much bigger batches, pushing decode throughput up to 5.3x over the non-offload sparse baseline.

That said, this lookahead will only pay off during decode with CPU offload. During prefill, all keys already live on the GPU, so the gain there comes purely from the cheaper selection.

Here's the paper: https://t.co/aOszIa8YDZ

I wrote a first-principles breakdown of how the KV cache works. It walks through why the model stores keys and values at all, why the cache grows with every token, and a comparison of LLM generation speed with and without KV caching.

Read it below.
