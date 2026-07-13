# gitcrawl

A local-first GitHub triage tool for maintainers and agents. Sync issues and PRs into SQLite for search, clustering, and terminal review; use Octopool for the pooled `gh` cache that used to live here.

## Two jobs, one binary

`gitcrawl` mirrors a GitHub repository's issues and pull requests into local SQLite, then layers semantic clustering and full-text search on top so a maintainer (or an agent acting on their behalf) can triage threads without burning live search quota.

- Local SQLite first. All issues, PRs, comments, reviews, files, commits, checks, and workflow runs land in the platform default SQLite database. Queries hit the disk, not GitHub.
- Octopool for `gh`. The old `gitcrawl gh` cache moved to Octopool, which owns the shared org-authenticated GitHub relay.
- Semantic clustering. OpenAI embeddings group related reports, with deterministic GitHub reference evidence (`#123`, `pull/123`) preventing weak similarity bridges from forming mega-clusters.
- Terminal UI. `gitcrawl tui` is a keyboard- and mouse-driven cluster browser with bidirectional sort, jump-to-number, neighbors, and member-level governance actions.
- Agent-friendly JSON. Every command supports `--json` for clean automation surfaces.

## Pick your path

### I want to try it

Quickstart walks you from `git clone` to a populated cluster view in five minutes.

### I want to wire up an agent

Use gitcrawl search for local discovery and Octopool migration for pooled `gh` reads.

### I want to triage a busy repo

Read the maintainer archive workflow for the first-run checklist, then Sync to bring data local, Clustering, and the TUI for the triage loop.

### I want the full reference

Commands lists every flag and JSON field. Configuration covers env vars and paths.

## Project status

Early bootstrap. The implementation is being built in small commits — see the changelog for what shipped recently.

The product contract in SPEC.md is the source of truth for what is in and out of scope.

## Out of scope

- Local HTTP API
- Hosted service runtime
- Browser web UI
- GitHub write-back actions (use `gh` for those)

## License

Released under the MIT license.
