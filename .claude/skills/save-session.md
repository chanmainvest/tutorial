---
name: save-session
description: Export session history to session_history/ folder with cost info, then commit
user-invocable: true
---

# Save Session

When the user invokes /save-session, do the following:

1. Run `py -3 .claude/skills/export-session.py` from the project root. This script reads the current session's JSONL transcript and writes a readable log to `session_history/<date>_from_<git-hash>.log`.

2. Show the user the output path.

3. Run git add and commit:
   ```
   git add session_history/
   git commit -m "Save session <date> from <hash>"
   ```

Do NOT push to remote.
