# imsg — Messages.app from your terminal

## Try it

After granting Full Disk Access (covered in the Quickstart), every workflow is a one-liner.

`--json` emits newline-delimited JSON on stdout; human progress and warnings always go to stderr so pipes stay parseable.

## What imsg does

- Local-first reads. Chats, history, and attachments come straight from `~/Library/Messages/chat.db` — no network round-trip, no daemon.
- Live streams. `imsg watch` follows filesystem events on `chat.db` and falls back to a lightweight poll when macOS drops the event.
- Send through Messages.app. Text, attachments, and standard tapbacks ride Messages' AppleScript automation surface — no private send APIs.
- Group-aware. Direct chats, group threads, participants, GUIDs, and per-chat account routing hints all show up in JSON output.
- Built for agents. Stable JSON-RPC over stdio, deterministic JSON schemas, and `imsg completions llm` for in-context CLI help.
- Contacts integration. Resolves names from your Address Book when permission is granted, while keeping raw handles in the output.
- Attachment-aware. Reports filenames, UTIs, byte counts, and resolved paths. Optional `--convert-attachments` exposes model-friendly CAF→M4A and GIF→PNG variants.
- Linux read-only preview. Linux builds can inspect an existing Messages database copied from macOS. They do not send, mutate, or connect to Messages.app.

## Pick your path

- Trying it. Install → Quickstart. Five minutes from `brew install` to a streaming watch.
- Reading on Linux. Linux read-only preview covers copying an existing database from macOS and running read-only commands.
- Wiring up an agent. JSON output and JSON-RPC cover the stable contracts; completions shows how to feed the CLI reference into an LLM.
- Analyzing local history. Statistics explains logical counts, timezone-aware date buckets, and optional media totals.
- Inspecting Send Later. `imsg scheduled list --json` reads future scheduled rows directly from local history; no bridge or SIP change required.
- Inspecting chat backgrounds. `imsg chat-background status --chat-id --json` reads local background metadata, cache presence, and the newest set/clear event without mutating the chat.
- Sending messages. Send and React explain text/file/group sends and how the Tahoe ghost-row check works.
- Diagnosing access. Permissions and Troubleshooting.
- Advanced IMCore. Read receipts, typing, status, launch. SIP-disabled and increasingly limited on macOS 26.

## Project

Active development; the changelog tracks what shipped recently. Released under the MIT license. Not affiliated with Apple.
