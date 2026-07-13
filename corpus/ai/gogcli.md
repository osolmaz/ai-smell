# gog — Google Workspace in your terminal

## Try it

After you store an OAuth client and authorize an account (Quickstart walks through the five-minute version), everything is a one-liner.

`--json` produces a stable JSON envelope on stdout, `--plain` produces TSV; human progress, prompts, and warnings always go to stderr so pipes stay parseable.

## What gog does

- One binary, every API. Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Apps Script, Contacts, People, Tasks, Classroom, Chat, Groups, Keep, and Workspace Admin.
- Stable output. `--json` for scripts, `--plain` TSV for `awk`, human output on stderr.
- Runtime discovery. `gog schema --json` exposes command shape, stable exit codes, output modes, and effective safety state.
- Multi-account, multi-client. Many Google accounts and OAuth client projects in one config; OAuth, direct access tokens, ADC, and Workspace service accounts all supported.
- One automation contract. Humans, scripts, CI, and agents use the same commands, with JSON/TSV output, non-interactive operation, stable exit codes, runtime read-only enforcement, untrusted-content wrapping, command guards, and baked safety profiles.
- Preview-first audits. Drive `tree`, `du`, `inventory`; Contacts `dedupe` previews by default and requires explicit `--apply` for guarded merges; raw API JSON dumps never mutate remote state.
- Generated reference. Every command has a docs page, and service-level agent skills are generated from the same `gog schema --json` contract.

The short version is in Why gog: workflow-first commands, stdout as an API, identity routing, layered safety, and a contract generated from the live binary.

## Pick your path

- Trying it. Install → Quickstart. Five minutes from `brew install` to your first authenticated query.
- Understanding the design. Why gog explains what the project optimizes for and where its boundaries are.
- Wiring up automation. Automation, Safety Profiles, and Agent skills. Discover the active contract and lock the binary down before handing it to an untrusted caller.
- Serving MCP tools. MCP server exposes typed, allowlisted tools for agent clients without a generic command bridge.
- Discovering runtime contracts. Automation explains root help, schema metadata, safety controls, and stable exit codes.
- Polling local events. Drive and Docs polling persists cursors and optionally invokes trusted shell hooks.
- Persisting auth and state. Paths and State covers `GOG_HOME`, per-kind directories, XDG paths, and legacy compatibility.
- Running Workspace at scale. Auth Clients for service accounts, named OAuth clients, and domain-wide delegation.
- Managing Workspace. Workspace Admin covers user creation, cleanup, organizational units, and group administration.
- Backing up an account. Backup before pointing `gog backup push` at a busy mailbox.
- Selecting private Photos media. Photos Picker keeps access limited to items the user explicitly chooses.
- Managing YouTube. YouTube covers API-key reads, account OAuth, subscriptions, playlists, and mutation safety.
- Grouping Docs edits atomically. Google Docs request batches covers persisted, revision-locked request queues and explicit recovery modes.
- Verifying real API behavior. Live testing covers the dedicated-account smoke suite, cleanup, retries, and optional infrastructure.
- Looking up a flag. The Command Index has a generated page for every subcommand.
- Comparing Discovery-driven CLIs. Reproduce the gog and gws evaluation instead of relying on a stale feature table.

## Project

Active development; the changelog tracks what shipped recently. Goals and non-goals live in the spec. Released under the MIT license. Not affiliated with Google.
