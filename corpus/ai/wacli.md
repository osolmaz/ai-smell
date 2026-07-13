# wacli — WhatsApp in your terminal

A script-friendly WhatsApp CLI built on whatsmeow. One binary pairs as a linked WhatsApp Web device, syncs messages and status broadcasts into a local SQLite store, and exposes search, send, media, contact, and group commands with predictable output for terminals, shell pipelines, and coding agents.

## Why wacli

- Local mirror, fast search. All synced messages land in a SQLite store with an FTS5 index; offline `messages search` returns hits in milliseconds.
- Chat state controls. Archive, pin, mute, and mark chats read/unread from the CLI, then filter `chats list` by those states.
- Stable output. Human-readable tables by default, `--json` to stdout for scripts, NDJSON `--events` for long-running commands. Human progress, prompts, and errors stay on stderr so pipes stay clean.
- Single binary. No daemon, no plugin host. Run `wacli auth`, then `wacli sync --follow` to keep the store warm.
- Built for agents. `--read-only` (or `WACLI_READONLY=1`) blocks every command that mutates WhatsApp or local state. Store locks prevent two instances from racing on the same device identity.
- Boundable storage. `sync` warns when storage is uncapped; `--max-messages`/`--max-db-size` cap local growth. Send retries are bounded; media uploads/downloads cap at 100 MiB.
- Best-effort history. `history coverage` shows local anchors, `history fill --dry-run` plans candidate chats, and `history backfill` requests older messages per chat from your primary device.

## Pick your path

- Trying it. Read Install, then Quickstart. Pair, sync, and send your first message in under five minutes.
- Using multiple WhatsApp accounts. Read Accounts for named account stores and `--account`.
- Searching old chats. Read Sync for the sync model and History for coverage planning and on-demand backfill.
- Managing chat state. Read Chats for archive, pin, mute, and read/unread commands.
- Managing local storage. Read Store for stats, dry-run cleanup, and local-only pruning.
- Sending from scripts. Read Send for recipient resolution, channels, status broadcasts, replies, mentions, files, and reactions.
- Mirroring address-book names. Read Contacts import-system to import macOS Contacts display names into local wacli metadata.
- Wiring up an agent. Pair `--read-only`, `--json`, and `--events` from Overview; read Doctor for self-checks.
- Building companion tools. Read Companion integrations for safe read-only SQLite and JSON integration patterns.
- Looking up a flag. Open the per-command pages from Overview.

## Status

Core implementation is in place. The CHANGELOG tracks shipped behavior. WhatsApp Web is not a published API; expect occasional breakage from upstream protocol changes — `wacli` follows `whatsmeow` upstream.

## Out of scope

- Guaranteed full-history export (WhatsApp Web history is best-effort).
- A daemon, MCP server, web UI, or GUI.
- End-to-end "contact creation" inside WhatsApp; local aliases and tags only.

## Disclaimer

`wacli` is a third-party tool that uses the WhatsApp Web protocol via `whatsmeow`. It is not affiliated with WhatsApp or Meta. Use at your own risk; pairing as a linked device is subject to WhatsApp's terms.

Released under the MIT license.
