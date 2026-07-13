# mcporter — MCP, made portable.

## Try it

mcporter auto-discovers the MCP servers already configured in Cursor, Claude Code/Desktop, Codex, Windsurf, OpenCode, and VS Code. Try it without installing anything.

`--json` produces a stable JSON envelope on stdout; human progress, prompts, and warnings always go to stderr so pipes stay parseable.

## What mcporter does

mcporter leans into the code-execution-with-MCP pattern Anthropic recommends: skip the giant tool-schema prompt, generate a small typed surface, and let the agent or the human call MCP servers like normal functions.

- Zero-config discovery. Reads your home config (`~/.mcporter/mcporter.json[c]`, or `$XDG_CONFIG_HOME/mcporter/mcporter.json[c]`), then `config/mcporter.json`, then imports from Cursor / Claude / Codex / Windsurf / OpenCode / VS Code. `${ENV}` placeholders are expanded; transports are pooled across calls.
- One-command CLI generation. mcporter generate-cli turns any MCP server into a ready-to-run CLI with embedded schemas, optional Rolldown/Bun bundling, and Bun-compiled binaries.
- Typed clients. mcporter emit-ts emits `.d.ts` interfaces or a ready-to-run client wrapping `createServerProxy()` so agents call MCP tools with full TypeScript types.
- Friendly composable API. createServerProxy() maps tools to camelCase methods, applies JSON-schema defaults, validates required arguments, and returns a `CallResult` with `.text()`, `.markdown()`, `.json()`, `.images()`, `.content()` helpers.
- Ad-hoc connections + auto-OAuth. Point the CLI at any MCP endpoint (HTTP, SSE, stdio) without touching config. Hosted MCPs that need a browser login (Supabase, Vercel, etc.) are auto-detected — `mcporter auth` promotes the definition to OAuth on the fly. See Ad-hoc connections.
- MCP bridge for agents. `mcporter serve` exposes daemon-managed keep-alive servers as one MCP server with namespaced `server__tool` tools, or as per-server HTTP paths that keep original tool names.
- OAuth & stdio ergonomics. Built-in OAuth caching, token refresh, log tailing, and stdio wrappers — same interface across HTTP, SSE, and stdio transports.

## Built for agents

mcporter is designed to be the layer between an MCP server and a coding agent. The pattern we recommend:

1. Configure the server once (or import from your editor of choice).
2. Run mcporter emit-ts to get a `.d.ts` of the tool surface.
3. Wire small per-server agent skills instead of one mega-schema prompt — small prompts, named tools, no unrelated schemas loaded.
4. For shareable workflows, generate a standalone CLI with mcporter generate-cli.

Because every transport flows through the same runtime, an agent that knows how to spawn `mcporter call` works with stdio servers, hosted HTTP MCPs, OAuth-gated services, and one-off URLs alike.

## Why a porter?

A porter carries luggage between trains. mcporter does the same for MCP servers: it carries tool calls, schemas, OAuth tokens, and stdio handles between your agent (or your terminal) and whichever MCP server happens to be at the other end of the line. You don't have to know the shape of the server ahead of time, and the runtime keeps the connection warm so repeat calls are cheap.

## Where to next

- Install — npm, npx, Homebrew, or the standalone Bun-compiled binary.
- Quickstart — your first list/call/resource in five minutes.
- Configuration — `mcporter.json`, imports, env interpolation, OAuth.
- CLI reference — every subcommand and flag.
- Ad-hoc connections — point at any MCP endpoint without editing config.
- Agent skills — exposing servers to agents the right way.
