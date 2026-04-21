# Edit Report

## Source
Review comment on `CLAUDE.md:L8-15`: *"add course overview and level overview"*

User instruction: apply this guidance to `README.md`.

## Changes to `README.md`

### 1. Course overview link (top of file)
Inserted a "Start here" line right after the intro paragraph, pointing to the course overview page.

```diff
 A comprehensive 52-week investment education course ...

+**Start here:** [Course Overview](course/overview.md) — what the course covers, who it is for, and how to work through it.
+
 ## Course Philosophy
```

### 2. Per-level overview links
Added a one-line link to the matching level overview page directly under each Level heading, before its weeks table.

| Heading | Link added |
|---|---|
| `### Level 1: Foundation (Weeks 1-12) - Beginner` | `[Level 1 Overview](course/level1_overview.md)` |
| `### Level 2: Intermediate (Weeks 13-24)` | `[Level 2 Overview](course/level2_overview.md)` |
| `### Level 3: Advanced (Weeks 25-36)` | `[Level 3 Overview](course/level3_overview.md)` |
| `### Level 4: Sophisticated (Weeks 37-46)` | `[Level 4 Overview](course/level4_overview.md)` |
| `### Level 5: Expert (Weeks 47-52)` | `[Level 5 Overview](course/level5_overview.md)` |

Pattern used in each spot:

```diff
 ### Level N: ...
+
+[Level N Overview](course/levelN_overview.md)
+
 | Week | Title | Summary |
```

## Files Touched
- `README.md` — 6 insertions (1 course overview link + 5 level overview links)

## Files Verified (not edited)
- `course/overview.md` — exists
- `course/level1_overview.md` … `course/level5_overview.md` — all exist

## Review Comment Status
Originally deleted after applying, then restored at user request:
- Current ID: `c22cb907-4ada-4aef-9b38-b5036bea03de`
- Location: `CLAUDE.md:L8-15`
- Saved to: `logs/batch_review/review_comments.json`
