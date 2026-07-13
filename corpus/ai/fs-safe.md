# fs-safe

Trusted Node.js code that has to touch caller-controlled paths inside a directory it owns gets one boundary it can rely on. `root()` returns a capability-style handle that resolves every relative path against a real directory, refuses anything that escapes it, pins the file you opened, and verifies the write landed where you intended.

Think Go's `os.Root`/`OpenInRoot` or Rust's cap-std, but for Node. `root()` is the product; everything else in this doc set — JSON stores, atomic writes, secret files, archive extraction, temp workspaces — is supporting cast for the same boundary.

## Why

`path.resolve(root, input).startsWith(root)` validates a string. It does not pin the file you opened, defend against a symlink retarget between check and use, reject hardlinked aliases, or verify that a write landed where you intended after a rename. `fs-safe` does those things, packaged so every call site picks up the same defense without re-implementing it.

This is a library-level guardrail, not OS-level isolation. It does not replace containers, seccomp, AppArmor, or filesystem permissions. It is for code that already runs with the privileges of its workspace and wants to stop trivial path tricks from escaping it. Typical fits: agent runtimes, plugin systems, upload extraction, local workspaces, CLIs — anywhere trusted code touches untrusted relative path names.

## Pick your path

- First time? Install, then walk through the Quickstart. Five minutes from `pnpm add` to a working root.
- Designing a workspace feature. Read the Security model before you trust the boundary, the Python helper policy before you pick deployment defaults, and the Errors reference so you know what to catch.
- Replacing ad-hoc atomic writes. Jump to Atomic writes or, for keyed JSON state, JSON files.
- Extracting an upload. Start at Archive extraction — handles ZIP and TAR with traversal, link, count, and byte limits.
- Running an agent in a sandbox. Private temp workspaces plus secret files cover the common scratch-and-credentials shape.
- Looking up a name. Use the reference section in the sidebar — every public function has a page.

## What you get

- root() — One boundary for read/write/move/remove inside a trusted directory.
- @openclaw/fs-safe/config — Process-global Python helper and lock-option defaults.
- Python helper policy — Choose `auto`, `off`, or `require` for POSIX fd-relative hardening.
- replaceFileAtomic — Sibling-temp + rename, fsync hooks, mode preservation, copy fallback.
- writeExternalFileWithinRoot — Stage external-library file output in private temp storage, then finalize under a root.
- writeJson / readJson — JSON state files with strict and lenient read variants.
- jsonStore — Single JSON state file with explicit fallback, atomic writes, and optional locking.
- fileStore — Managed multi-file/blob store with modes, stream writes, copy-in, pruning, and private mode.
- Private file-store mode — `fileStore({ private: true })` for private JSON/text state at 0600 under 0700 dirs.
- tempWorkspace — 0700 scratch dir with auto-cleanup.
- readSecureFile — Absolute file reads with fd pinning, permissions, owner, size, and timeout checks.
- walkDirectory — Budget-bounded recursive directory scan with symlink policy and filters.
- extractArchive — ZIP/TAR extraction with size, count, link, and traversal limits.
- Secret files — Mode-0600 credentials with size and TOCTOU defense.
- Permissions — POSIX mode and Windows ACL inspection/remediation helpers.
- acquireFileLock — Cross-process file lock with retry and fail-closed stale-lock handling.
- FsSafeError — Closed code union (with `policy`/`operational` category) you can branch on.
- pathScope() — Lower-level absolute-path boundary helper; lives behind `@openclaw/fs-safe/advanced`.

## Status

Currently `0.x` — APIs are stable in shape but may be tightened before `1.0`. The CHANGELOG tracks visible changes. Issues and PRs at the GitHub repo.

Released under the MIT license.
