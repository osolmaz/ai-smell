# @mksglu — long-form tweets

## 2026-04-16 (https://x.com/mksglu/status/2044795540362178624)

225 sessions, 8,337 tool calls. I ran /ctx-insight on my own data and the numbers surprised me.

I read 5.2x more than I write. 1,992 files read, 386 written. I thought I was mostly writing code. Turns out I spend most of my AI time understanding code. Review mode 45% of the time, implementation only 34%. My context window overflows in just 4% of sessions, which apparently puts me well below the 60%+ most developers hit.

The part I didn't expect: 19 tasks running in parallel across 6 bursts saved me roughly 26 minutes. And my error rate is 2.7%, meaning almost everything lands on the first try. 143 commits in 225 sessions, but most sessions are pure research.

The commits come in focused bursts.

All of this was already sitting in a local SQLite database on my machine. Every session writes tool calls, errors, file edits, context overflows. I just never had a way to see it until now.

/ctx-insight to see yours. Nothing leaves your machine.

https://t.co/6qDtMec1UO

## 2026-05-02 (https://x.com/mksglu/status/2050566958219776250)

80 hours of AI pair programming. Here's what context-mode saved me.

→ $487.20 in API costs. Opus pricing. Real money, not estimates.
→ 22.3 hours of re-explaining context after compaction. Time I got back to ship.
→ 268 sessions resumed from memory. The agent never asked "what were we doing?"
→ 47 preferences auto-learned. "use TS strict" once, remembered forever.
→ 14,847 events indexed. Searchable across every session, every project.

Without context-mode  |████████████████████████████████████████| 6.2 MB
With context-mode     |█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 124 KB

98% of raw data never entered my conversation.
That's a 50× longer session. Same context window.

Multiply across a 13-engineer team:
$487 × 13 = $6,331/month saved
22 hours × 13 = 286 hours/month recovered

Open source. Local-first. No telemetry. No account. No SaaS lock-in.

https://t.co/6qDtMec1UO

## 2026-05-02 (https://x.com/mksglu/status/2050691887007150229)

context-mode v1.0.104 just shipped. ⚡

103K+ users · 12K+ stars · 829 forks · 14 platforms

The performance release.

Every session reclaims 1.8s on macOS, 7.5–12.5s on Windows. Plus parallel I/O, a live statusline, and a security layer that stops the model from leaking what it touches.

What's new:

→ Per-tool-call latency cut across all 14 adapters. Biggest: a 17,000× speedup on a memoized git worktree call that was forking on every ctx_* invocation. Bulk SQLite inserts replaced N-transaction loops.

→ Opt-in concurrency. ctx_batch_execute and ctx_fetch_and_index now accept concurrency: 1–8. Multi-URL research and gh API fan-outs finish 3–5× faster. Default stays 1 — existing callers unchanged.

→ Statusline. One line in ~/.claude/settings.json and Claude Code shows your savings live: "context-mode ● $21.92 saved this session · 83% efficient · 7h1m."

→ Lifetime stats. ctx_stats now reads across every past session: "5.8K events · 173 sessions · ~$22.45 saved lifetime." No telemetry. All local.

→ Security. Bearer tokens and api_keys in mcp__* tool_input masked before SQLite. ctx_fetch_and_index blocks AWS/GCP/Azure IMDS + file:// schemes. SHELL env override gated behind a basename allowlist.

→ Concurrency observability. ctx_stats now shows median + max concurrency per tool — tells you whether you're actually using the new feature, not just whether it's available.

→ Platform detection audit. Same 14 adapters, but every entry in PLATFORM_ENV_VARS verified against each platform's runtime source code. KILO bare, IDEA_HOME, JETBRAINS_CLIENT_ID — all dropped (no source evidence). Antigravity, Zed, Pi promoted.

→ Brew upgrade node no longer breaks context-mode. Cache-heal hooks self-heal stale Cellar paths. Windows hooks.json placeholders normalized on every boot. Cross-session bleed in 6 SessionStart adapters fixed.

The numbers:

137 files changed. 11,541 added. 855 removed. 2,184 tests pass.

Your agent should be faster, more visible, and never leak credentials it touches.

Open source. Local-first. No telemetry.

https://t.co/zwyxP1fiaP

## 2026-05-04 (https://x.com/mksglu/status/2051305039071736258)

I'll be giving a short talk at @clawcon Istanbul on Wednesday, May 6.

"The Other Half of the Context Problem." Five minutes on why your AI coding agent keeps re-sending megabytes of stale tool output every turn, and what to actually do about it.

I ran the numbers on 80 hours of Opus pair programming. $487 saved, 22 hours of re-explaining I got back, 6.2 MB of raw output became 124 KB in context. That's a 98% reduction.

Three things I'll cover:

→ Intercept. Five lifecycle hooks pull tool output out of the conversation before it ever lands. 59 KB drops to 1.1 KB.

→ Think in Code. Send code to the data instead of pulling data into the model. 700 KB drops to 3.6 KB.

→ Session Persistence. 26 event categories carry over through compaction, so you stop re-teaching the agent your codebase every twenty minutes.

12.5K stars. 104K npm. 14 platforms. Open source, no telemetry.

Organized by @BuilderMare (@0xVeliUysal , @SolBridgeNW) through @clawcon and @openclaw. Special thanks to @iammurataslan.

İstanbul'daysan gel.

## 2026-05-04 (https://x.com/mksglu/status/2051328459289280710)

context-mode just crossed 120,000 users.

solo built. $0 funding. 14 AI coding agents: Claude Code, Cursor, Codex CLI, Gemini CLI, VS Code Copilot, JetBrains Copilot, OpenCode, OpenClaw, KiloCode, Qwen Code, Antigravity, Kiro, Zed, Pi.

98% context saved per session. 56 KB -> 299 bytes. 30 min sessions -> 3 hours.

I did not get here alone.

every issue, every PR, every DM, every retweet, every quiet install -> thank you. genuinely. you got us here. I will never stop being grateful for that.

now I need 3 partners to take this from 120k to a million:

-> DevRel who opens the camera in English
-> Growth Hacker who builds AI listening pipelines (no spam, no sock puppets)
-> Community lead who knows the dev creator graph cold

what you get now:
-> contributor credit pinned in README and every CHANGELOG
-> shoutout from the project account on every release
> public proof of work for your next interview

what you get if we raise:
-> first offer at market rate
-> founding equity, real numbers on paper

what you do not get:
-> salary today
-> vague equity with no math
-> a promise this works out

how to apply -> ship a public deliverable in the issue:

-> DevRel: 60 second demo, post the link
-> Growth: 3 contextual YouTube comments + your heuristic
-> Community: 5 creators + personalized DM drafts

first good one in each track wins. AI-assisted is fine. AI-pasted is obvious and disqualifies.

if you have ever wanted to ride a small OSS project from 120,000 to a million users before anyone else has heard about it -> this is that ride.

ship something:
https://t.co/b9T3vDIqNl

Mert

## 2026-05-04 (https://x.com/mksglu/status/2051338762811056553)

context-mode just made @nateherk's top 6 Claude Code skills out of 100+ tested.

watch skill #5 at 8:06 → https://t.co/zSvgiA31KG

every install, every issue, every share got us to:
→ 125,400+ users
→ 103.9k+ npm installs
→ 21.4k+ Claude Code marketplace installs
→ 14 agents supported

thank you Nate. thank you to every person who put context-mode here. genuinely. grateful.

## 2026-05-07 (https://x.com/mksglu/status/2052491520788357344)

context-mode is growing fully organically.

After @nateherk’s video, now @indiehackernws shared “Claude Code is Expensive. This MCP Server Fixes It (Context Mode)” and @selahattinunlu shared a Turkish video, “AI ajanının context'ini %98 küçült Context Mode”.

125.4K+ users  
14K+ GitHub stars  
14 agents supported

Indie Hacker News video:
https://t.co/gC9R5MoDFh

Selahattin Ünlü video:
https://t.co/njY8C1hQaG

genuinely grateful.

## 2026-05-10 (https://x.com/mksglu/status/2053484717408698488)

context-mode v1.0.112 just shipped.🫡

14.2K+ GitHub stars · 993 forks · 15 platforms · 157K+ users

The community release.

44 contributors. 33 pull requests. 42 reported issues closed. The biggest external-contribution release context-mode has ever cut.

What's new:

→ Case-fold migration. macOS and Windows users with mixed-case project paths now stop silently splitting their session history into two DBs. Canonical project-dir hash + one-shot legacy file rename. Linux is a no-op. Worktree separation preserved — different physical paths still get different DBs. No data loss on upgrade.

→ FTS5 content store hardened with the same dual-hash migration. SQLite WAL/SHM sidecars travel with the rename. Both-exist case never overwrites — the fix can never destroy data it was meant to protect.

→ OMP (Oh My Pi) joins as the 15th officially supported platform. Native hook enforcement via HookAPI: tool_call, tool_result, session_start, session_before_compact. One plugin, every AI coding tool — now including Pi's terminal-native sibling.

→ Statusline goes SQLite-backed. Per-PID sidecar JSON files retired. Statusline now reads directly from SessionDB, so cross-process state is consistent and the file count under ~/.claude/ stops growing per-process.

→ Three independent community security patches. DNS-rebinding gap closed in ctx_fetch_and_index SSRF guard. ctx_insight execSync replaced with spawnSync. ctx_index now enforces the Read deny-policy and closes a TOCTOU window via fd-bound reads.

→ Cursor Marketplace plugin shipping. context-mode is now a first-class Cursor plugin — discovery, hook coverage, runtime distribution all handled.

→ Pi adapter completion. Routing through PiAdapter.getSessionDir, MCP bridge bootstrap awaited in before_agent_start, lifecycle events corrected, session timestamps parsed as UTC. Five fixes from four contributors.

→ Codex compact hook support landed. Codex sessions now persist resume snapshots through compaction, matching Claude Code parity.

→ Windows hardening sweep. bun.exe absolute path resolution for npm-installed Bun, MS Store Python stubs filtered, non-ASCII tmpdir paths handled, FTS5 detection on Linux + Node 22.5+. Every Windows-class report from the v1.0.111 window got addressed.

→ UX cleanup. Byte formatter dropped the noisy "(0.00 MB)" parentheticals — single-unit auto-decimals (Grafana / CloudWatch convention). Plus three architectural deepenings: adapter interface narrowed, hooks helper rebound to bundled TS, ctx_purge extracted into a deep purgeSession() module.

→ Statusline goes SQLite-backed. Per-PID sidecar JSON files retired. Statusline now reads directly from SessionDB, so cross-process state is consistent and the file count under ~/.claude/ stops growing per process.

→ Three independent community security patches. DNS-rebinding gap closed in ctx_fetch_and_index SSRF guard. ctx_insight execSync replaced with spawnSync. ctx_index now enforces the Read deny-policy and closes a TOCTOU window via fd-bound reads.

→ Three architectural deepenings. Adapter interface narrowed (12 adapters lose 2 path methods). Hooks helper rebound to the bundled TS — no more parallel JS drift. ctx_purge extracted into a deep purgeSession() module: handler 75 → 25 LOC, dual-hash uniformly applied across 5 file kinds.

The numbers:

132 commits. 218 files changed. 19,547 insertions. 3,207 deletions. 2,773 tests pass. Typecheck clean. Zero new regressions.

This release is about one thing:

shipping is a team sport. 44 people made it possible.

Open source. Local-first. No telemetry.

https://t.co/rFPmVFyXje

## 2026-05-14 (https://x.com/mksglu/status/2054751403793404127)

context-mode v1.0.130 just shipped.

14.6K GitHub stars, 1,029 forks, 73 contributors, 15 AI coding tools, 3 OS, one plugin.

The most-upvoted complaint about Claude Code on HN this month: "limits exhaust in minutes nowadays."

Right behind it: "easy to spend 30 EUR a day when providing it with a lot of context."

And: "Despite my best efforts at /compact instructions, by the time we are ready to implement, the nuance is lost."

Three different complaints. Same root cause.

Your context window is full of garbage. Repeated file reads. Stale tool outputs. Logs nobody asked for. Every npm test that fired 50K bytes you'll never look at.

context-mode keeps the important parts in a local SQLite database. Your AI talks less, remembers more, costs less.

The proof on this single conversation:

→ 14 MB stayed OUT of my context window
→ 18,632 captures across 159 projects, locally indexed
→ 70 days of usage, no cloud, no telemetry

Two weeks of work behind v1.0.130: 18 patches, 60 community issues closed, multi-window UX restored after a rollback we wrote down in an ADR so it can't happen again.

https://t.co/6qDtMec1UO

## 2026-05-24 (https://x.com/mksglu/status/2058550509481480658)

context-mode keeps raw tool output out of your AI agent's context window. 🫡

98% reduction · 15 platforms · 15.5K stars · 1.1K forks · No telemetry

Used across teams at:
Microsoft · Google · Meta · Amazon · IBM · NVIDIA · ByteDance · Stripe · Datadog · Salesforce · GitHub · Red Hat · Supabase · Canva · Notion · Hasura · Framer · Cursor

One dev, 5 days of work, measured by `ctx_stats`:

Without context-mode    3.0 MB  ████████████████  778K tokens
With context-mode       140 KB  █░░░░░░░░░░░░░░░   36K tokens
95% kept out · 22× longer runtime before /compact

What it does:

→ Sandboxed execution in 12 languages. Only what you console.log() enters your conversation. Raw stdout, file contents, HTTP bodies stay out.

→ Unified persistent memory across 26 event categories. Survives /compact, --resume, version upgrades. One install captured 19,990 events across 198 projects. Your agent never re-learns your codebase.

→ Multi-strategy search. BM25 + Reciprocal Rank Fusion. Porter stemming + trigram substring tokenizers. Proximity rerank. Typo correction. One query reaches indexed docs, decisions, prior errors.

→ TTL-aware web indexing. ctx_fetch_and_index caches per-URL; repeat lookups skip the network. Custom per-call TTL.

→ 15 platforms, one plugin. Claude Code, Cursor, Codex, Gemini CLI, OpenCode, VS Code Copilot, JetBrains AI Assistant, Zed, Antigravity, Qwen Code, OMP — same hooks, same memory, same numbers.

The bottom line:

$87 of Opus 4 tokens not burned in 5 days. ~$3,920/year at 10-dev team scale. 4 months of Cursor Pro paid for itself in the first install month.

Open source. Local-first. No telemetry.
https://t.co/q8ipFHA3dO

## 2026-06-07 (https://x.com/mksglu/status/2063628334026625125)

You ship Claude Code, Cursor, or Copilot to your engineers. Then you can't tell what they're actually doing.

Context Mode Insight is out today.

Ask your own AI agent:
→ "Who on my team is stuck and on what?"
→ "How is Mobile doing compared to Backend this sprint?"
→ "Which engineers' AI sessions predict shipped commits?"

Insight runs on structured events from 15 AI coding tools. Never prompts, never source code. Three doors in: Dashboard, REST API, remote MCP.

Built on context-mode, already on 250,000+ developer machines. OSS stays free. 

Thanks to the open-source community.

## 2026-06-07 (https://x.com/mksglu/status/2063700829048111394)

This is exactly why we built Context Mode as open source. We’re seeing 90%+ efficiency gains in real AI coding workflows.

The next step is Context Mode Insight for B2B teams: helping C-levels and EMs understand where AI credits are going, how AI tools are being used, and where engineers are getting blocked, based on 220+ actionable patterns.

AI coding needs an observability layer now. Context Mode is becoming that layer.
