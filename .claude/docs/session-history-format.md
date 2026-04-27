# Session History — Format Spec

The `/save-session` skill exports the current chat session to
`session_history/<YYYY-MM-DD>_from_<starting-git-hash>.log` (e.g.
`session_history/2026-04-16_from_afbc120.log`).

`<starting-git-hash>` is the short hash of `HEAD` at the moment the chat
session began — **not** the commit being created right now. The file
documents the work that happened on top of that baseline.

## Required header

The export script prepends this metadata block to the log, matching
Claude Code's `/export` formatting as closely as possible. Keep this
spec in sync if you change `.claude/skills/export-session.py`.

```
=== Session Metadata ===
Agent:           <CLI name + version, e.g. "Claude Code v2.1.104">
Model:           <main model id, e.g. "claude-opus-4-7[1m]">
Sub-agent models: <list of distinct models used by spawned sub-agents, or "none">
Started from:    <git short hash that HEAD pointed to when the session began>
Date:            <YYYY-MM-DD HH:MM local>

Token usage (this session, including all sub-agent calls):
  Input tokens:        <count>
  Output tokens:       <count>
  Cache read tokens:   <count>
  Cache write tokens:  <count>
  Total tokens:        <count>

Cost (USD, this session, including all sub-agent calls):
  Input:        $<x.xx>
  Output:       $<x.xx>
  Cache read:   $<x.xx>
  Cache write:  $<x.xx>
  Total:        $<x.xx>
========================
```

## Source of token & cost numbers

Pull the token + cost numbers from the same source `/cost` uses (the
JSONL transcript's `usage` records, summed across the main thread and
every sub-agent invocation). If a number truly cannot be determined,
write `unknown` rather than zero so it's obvious the value was missing
rather than free.

## Commit policy

- Commit the log file in the **same commit** as the code/content
  changes it produced (one self-contained commit per session).
- **Never push session logs to a public remote without first scrubbing
  any secrets** the conversation may have included.
