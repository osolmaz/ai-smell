# Clawpatch — Automated Code Review

## Overview

Clawpatch is an automated code review tool that goes beyond traditional linters. It maps a repo into semantic work units, asks a provider to review bounded context, and persists findings for audit and follow-up.

Unlike file-only scanners, clawpatch reviews feature records with entrypoints, owned files, nearby tests, and trust boundaries. Every finding includes severity, confidence, evidence, and a recommendation.

### Semantic Analysis

Reviews by feature records such as package bins, scripts, routes, Go/Rust/Swift commands, and config.

### Automated Patching

Runs an explicit `fix --finding` loop and records validation command results.

### Safety First

Clean worktree checks, no implicit commits, audit trail. Your code stays under your control.

### Resume Support

Persists runs, feature state, findings, and patch attempts in `.clawpatch/`.

### Rich Reports

Markdown reports and JSON state with severity levels, categories, and confidence scores.

### Codex Provider

Uses the local Codex CLI today, with strict JSON schemas around every provider result.

## Commands

- `clawpatch init` — Initialize project, detect config
- `clawpatch map` — Build semantic feature map
- `clawpatch status` — Show project/review state
- `clawpatch review` — Review features, find issues
- `clawpatch report` — Generate findings report
- `clawpatch fix` — Apply repairs for findings
- `clawpatch revalidate` — Verify fixes or findings
- `clawpatch doctor` — Check environment setup

## Initialization

The `init` command detects your project type and creates initial configuration.

This creates `.clawpatch/` directory with:

- `config.json` — User settings and preferences
- `project.json` — Detected project metadata (package manager, build tools, test commands)

Clawpatch auto-detects Node.js, TypeScript, Next.js, Python, Flask, FastAPI, Go, Rust/Cargo, SwiftPM, and common build tools. You can customize settings after initialization.

## Feature Mapping

The `map` command builds a semantic map of your codebase.

Features are semantic units like:

- Routes — Next.js app/pages routes plus Flask and FastAPI routes
- Commands — npm package bins plus Python, Go, Rust, and SwiftPM commands
- Packages — Go internal packages, Rust libraries, and Swift targets
- CLI scripts — Bin scripts and npm script handlers
- Tests — Test suites linked to their subjects

Each feature includes entrypoints, owned files, context files, and associated tests—giving AI reviewers the right context to understand your code.

## Code Review

The `review` command analyzes features for issues.

Reviews produce findings with:

- Category — bug, security, performance, docs-gap, test-gap, maintainability
- Severity — critical, high, medium, low
- Confidence — How certain the analysis is (high, medium, low)
- Evidence — Code snippets, file locations, and reasoning

Use `--limit` to review in batches. State is persisted so you can resume anytime.

## Findings

All findings are tracked in `.clawpatch/findings/` with:

- Status — open, fixed, wont-fix, false-positive, uncertain
- Metadata — Severity, category, confidence, timestamps
- Context — Feature info, affected files, evidence
- Patches — Associated fix attempts and validation results

Use `clawpatch report` to generate a Markdown report, or `--json` for structured output.

## Patching

The `fix` command runs the explicit repair loop for one finding.

Each patch goes through validation:

- Format check — Prettier/dprint/etc if configured
- Type check — TypeScript `tsc --noEmit` if applicable
- Lint check — ESLint/oxlint if configured
- Test check — Runs the configured test command

Validation results are recorded in a patch attempt. You review any worktree changes manually.

## Validation

The `revalidate` command re-checks a finding with the provider.

Use this to:

- Verify a finding is still valid after manual fixes
- Check if upstream changes resolved issues

## Safety Features

Clawpatch is designed with strict safety guarantees:

- No implicit changes — Never modifies code without explicit `fix` command
- No implicit commits — Does not commit, push, open PRs, or land changes today
- Clean worktree by default — Blocks fixes on dirty worktree (configurable)
- No destructive git ops — Never runs `reset --hard`, `clean`, etc.
- Audit trail — Review runs, findings, and patch attempts are persisted in `.clawpatch/`
- Schema validation — All provider responses validated before use
- Feature locks — Claimed feature records are unlocked after each run

All fixes are applied to your working directory for manual review. You maintain full control over what gets committed.

## Next Steps

Explore the full documentation to learn about:

- CI/CD Integration — Run review and reporting in GitHub Actions
- Custom Mappers — Support additional frameworks and languages
- Finding Templates — Create custom review rules
- Coding harnesses — Integrate agent CLIs and ACP adapters

Made with care by the OpenClaw team. Released under MIT license.
