# Crabbox Docs

### Local loop, remote box

Keep your editor and git workflow. Crabbox rsyncs your dirty checkout to a leased remote box and streams the run back.

### Brokered, not BYO creds

A Cloudflare Worker holds provider credentials and serializes lease state. Your CLI only carries a bearer token.

### Cost-aware leases

TTL-bounded machines, monthly spend caps, and per-user / per-org / per-provider usage from the broker.

### Reuse what's warm

`crabbox warmup` keeps a box hot. Reuse it with `--id` across runs, SSH, and CI hydration.

### Many providers, one loop

Brokered Hetzner / AWS / Azure, delegated E2B / Daytona / Blacksmith / Semaphore, or static SSH targets - Linux, Windows, and macOS.

### Plays with Actions

`actions hydrate` reuses your repository's GitHub Actions setup steps so local runs land in the same hydrated workspace.

### Desktop in your browser

`crabbox webvnc` streams a Linux, macOS, or Windows desktop into the browser. Drive UI tests, capture screenshots, hand the live session to a teammate - no VPN.

### Proof for every run

`crabbox artifacts collect` bundles screenshots, video, JUnit summaries, logs, and lease metadata. Drop it on a PR as before/after evidence instead of scraping log output.

# Crabbox Docs

Warm a box, sync the diff, run the suite.

## What Crabbox is

Crabbox is a generic remote software testing and execution control plane. It keeps the local developer story unchanged: edit, save, run. The difference is where the command executes. Crabbox moves tests, builds, browser checks, platform validation, and review evidence onto owned or provider-backed remote capacity, then streams the result back to the caller.

It is for maintainers, contributors, and automation that need a repeatable way to run repository commands on a machine other than the local laptop. A `crabbox run` leases a brokered cloud machine, reuses a static SSH host, or delegates to a sandbox provider; syncs your tracked, non-ignored local files; executes the command remotely; streams stdout and stderr back; records evidence; and then releases or unclaims the target.

Use Crabbox when local compute is too small or slow, when a workflow needs a fresh disposable runner, when the target platform is remote, or when an AI agent or reviewer needs auditable command output from the exact environment that ran. It is not a CI service, a package manager, a production deployment platform, a hostile multi-tenant sandbox, or a tool that automatically sanitizes secrets from command output and artifacts.

An optional coordinator owns cloud provider credentials, lease state, cleanup, usage accounting, and cost guardrails so individual machines and CLIs never hold those. The coordinator runs either on Cloudflare Workers with a Durable Object or on Node.js with PostgreSQL.

The Node runtime can also own a dedicated private AWS workspace service: small allowlisted EC2 instances, no public address or SSH, task-role credentials, SSM bootstrap, and an authenticated create/status/delete API.

## How it fits together

The CLI is a Go binary (`cmd/crabbox`, `internal/cli`). Shared coordinator behavior lives in `worker/src`; Cloudflare and Node/PostgreSQL provide runtime adapters. For normal CLI leases, lifecycle calls go through the coordinator over HTTPS, but the data plane — SSH, rsync, and command execution — goes directly from the CLI to the runner host. The dedicated private AWS workspace API is the documented SSM-only exception. Runners hold no coordinator credentials; they are leaf nodes.

Crabbox selects one of three execution modes per provider:

- Brokered — for `aws`, `azure`, `daytona`, `gcp`, and `hetzner` when a broker URL is configured (`CRABBOX_COORDINATOR`). The coordinator provisions and tracks leases; the CLI still drives sync and command execution over SSH.
- Direct SSH — the same SSH-lease providers without a broker, plus static hosts (`provider: ssh`) and self-hosted/local providers. The CLI talks to the cloud or host API itself.
- Delegated — sandbox/proof runners (for example dynamic-session and Firecracker providers) that own sync and run end to end; there is no SSH lease.

Brokered Linux runners are vanilla Ubuntu boxes prepared by cloud-init with SSH, Git, rsync, and `/work/crabbox`. AWS and Azure can also broker Windows (normal and WSL2) and, on AWS, EC2 Mac desktop targets. Project runtimes come from Actions hydration or repo-owned setup.

## A run, end to end

1. The CLI loads config from flags, env, repo, user, and defaults.
2. The CLI mints a per-lease SSH key and slug, then `POST /v1/leases` on the broker (brokered mode) or provisions directly (direct mode).
3. The coordinator checks active-lease and monthly spend caps, reserves worst-case TTL cost, provisions a server with region/market fallback, and returns host / port / user / workdir / expiry / slug.
4. The CLI waits for the `crabbox-ready` marker, seeds remote Git when possible, rsyncs the Git file-list manifest, runs sync guardrails, and hydrates the configured base ref.
5. The CLI runs the command over SSH, streams output, records run events, and sends heartbeats.
6. The CLI releases the lease unless `--keep` is set. Kept leases still auto-release after the idle timeout, and the broker frees reserved cost when the lease closes.

See How Crabbox Works for the full picture, including warm-box reuse and the brokered-vs-direct paths. See the Source Map to trace any documented behavior back to code.

## Quick start

Each lease has a canonical id (`cbx_<12 hex>`) and a friendly slug; most commands accept either via `--id`. Run `crabbox doctor` to validate local config, broker/provider reachability, and SSH key availability before a long workflow, and `crabbox usage` to summarize recent spend by user, org, provider, and server type.

Pick whichever matches your intent:

- Start here: Getting started, How Crabbox Works, Concepts and glossary.
- Get the mental model: Vision, Architecture, Orchestrator, Runtime adapter stack, Broker auth and routing, Coordinator, Bring your own infrastructure, Slurm academic sandboxes.
- Deploy the coordinator: Infrastructure, Portable coordinator, Operations, Security.
- Use the CLI: CLI overview, Command reference, Feature reference, Configuration, Jobs, Pond, Actions hydration, Capsules, Checkpoints, Browser portal, Runtime adapter stack, Capabilities, Interactive desktop and VNC, Telemetry, Sync, Hermetic agent evidence.
- Operate it: Operations, Observability, Troubleshooting, Performance, Cost and usage, Lifecycle and cleanup.
- Set it up or audit it: Infrastructure, Portable coordinator, Security, Auth and admin, Repository onboarding, SSH keys, Source Map.

## About these docs

Markdown in this directory is the user-facing documentation source. Implementation truth stays in code; the Source Map lists the files behind each documented behavior. The documentation site is generated from these Markdown files by `scripts/build-docs-site.mjs` and deployed by `.github/workflows/pages.yml`. Pages must be enabled on the repository or organization for the workflow to publish.
