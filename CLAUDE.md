# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Investment education platform ("Chanma Investment Tutorial") that transforms CFA-level knowledge into a structured tutorial course with YouTube content. The repository produces:
- A 52-week core course (beginner to advanced) in Markdown, organized into 5 levels
- 30 side lessons for supplementary topics
- A course overview page (home page) and a level overview page for each of the 5 levels
- YouTube scripts with two-host format: **Horace** (陳馬, experienced retail trader/teacher) and **Stella** (小魚, recent college graduate/student)
- Visual explanations rendered three ways depending on output:
  - **Static images embedded in markdown** — every visual concept has a static image so the markdown reads on its own. Procedural charts use Python (matplotlib) to generate the PNG; conceptual illustrations use AI-generated images (e.g., Nano Banana).
  - **Animations / video for YouTube** — the same visuals become animated clips or short video segments referenced in the YouTube script.
  - **Interactive demos for the published website** — when an interactive component exists, the website upgrades the static image into a live demo (with a toggle to fall back to the static image).
- Multilingual versions (English, HK Chinese, TW Chinese, CN Chinese)
- A static website with multilevel hamburger navigation, breadcrumbs, country flag language selector, and a dark/light theme toggle
- Course FAQ and Disclaimer pages

## Repository Structure

```
references/          # Source materials (CFA syllabus, calculator guide, YouTube strategy)
course/              # English course materials
  overview.md        # Course overview (serves as website home page)
  level1_overview.md # Level 1-5 overview pages
  ...
  week01_*.md        # 52 weekly lessons
  side01_*.md        # 30 side lessons
  disclaimer.md      # Legal disclaimer
  faq.md             # Course FAQ
  image/             # Static PNG images embedded in lessons + the Python
                     # code that generated them (one .py per .png where
                     # the image is procedural)
  animation/         # Animation clips / interactive web components that
                     # the website can swap in for static images
course_hk/           # Hong Kong Chinese translations
course_tw/           # Taiwan Chinese translations
course_cn/           # Mainland China Chinese translations
docs/                # Generated static website (do not edit directly)
scripts/             # Build and translation scripts (all Python, run via uv)
  configs.json       # LLM provider/model/effort + translation options
  terminology.json   # Cross-locale terminology glossary
```

## Reference Materials

Three key source documents in `references/` drive content creation:
- **profession_syllabus.md** — CFA Levels I-III curriculum mapped to retail trader competencies, organized by topic area with "common retail gaps" annotations
- **investment_youtube_strategy.md** — 5-tier YouTube content strategy (Newbie -> Professional) with monetization and teaching philosophy
- **cfa_calculator_guide.md** — TI BA II Plus calculator walkthrough with keystroke examples

## Lesson Format

Every lesson file (core weeks, side lessons, level overviews, and course overview) is a **single markdown file** containing both parts:

1. **Reading section (Part 1)**: a) Why this is important, b) What you need to know, c) Common misconceptions, d) Common Q&A — written as text plus **static images embedded in the markdown**. Where a concept also has an interactive web component, the reading section includes a short prose description of how the interactive demo behaves (so the markdown alone is still self-contained).
2. **YouTube script section (Part 2)**: Same material adapted for two hosts (Horace = teacher, Stella = student). Includes `[ANIMATION: ...]` cues at the right locations pointing to clips in `course/animation/`, plus visual explanation descriptions.

**Asset layout for a lesson:**
- Static images and the Python code that generates procedural ones live under `course/image/` (e.g. `image/week01_compound_growth.png` + `image/week01_compound_growth.py`).
- Animation clips and interactive web components live under `course/animation/` (e.g. `animation/week01_compound_growth.html` or a video file).
- The markdown file references the static image; the website upgrade step looks for a matching interactive component and, if it exists, swaps the static image for the live demo (with a toggle to fall back to the static image).

**IMPORTANT: Both parts live in the same file intentionally.** When updating or editing any lesson content, you MUST also update the corresponding YouTube script in Part 2 of that same file to keep them consistent. The reading section and YouTube script cover the same material — they must stay in sync.

The website only displays Part 1 (reading section). `scripts/build.py` strips Part 2 (everything from `## Part 2: YouTube Script` onward) from web output. It also strips the in-markdown "interactive demo description" prose for any lesson where an interactive component is actually present (the live component replaces it); where no interactive component exists, the description is removed and only the static image remains.

## YouTube Host Characters

- **Horace (陳馬)** — Teacher. Middle-aged experienced retail trader. Explains concepts from years of market experience.
- **Stella (小魚)** — Student. Young college-graduated woman learning to invest her savings. Asks the questions viewers are thinking.

When writing English YouTube scripts, always use the English names (Horace / Stella). In Chinese translations (HK/TW/CN), use ONLY the Chinese names (陳馬 / 小魚) — do not retain or parenthesise the English names.

## Content Philosophy

- Teaching model: Macro context -> Strategy concept -> Tactical execution
- Progressive skill-building with forward/backward references between lessons
- Core course maps roughly to CFA curriculum but reordered for retail trader relevance
- Side lessons cover practical topics (calculator usage, specific instruments, real-world examples) that don't fit the weekly progression
- Animations should make abstract financial concepts tangible
- Website is audience-facing (no technical/GitHub details) and hosts the **full** course material — every weekly lesson, side lesson, level overview, course overview, FAQ, disclaimer, and the terminology glossary — across all four languages

## Build & Development

All scripts are Python. **Always run them via `uv`** as the package manager (e.g. `uv run python scripts/build.py`) — `uv` resolves the project's dependencies (declared in `pyproject.toml`) without polluting the system Python. No Node.js dependencies required for the build pipeline.

- **Website**: `uv run python scripts/build.py` — generates static HTML from all markdown files with multilevel hamburger navigation, breadcrumbs, country flag language selector, dark/light theme toggle, and prev/next page buttons. YouTube scripts are stripped from web output. Where a matching interactive component exists in `course/animation/`, the corresponding static image is replaced with the live component (the user can toggle back to the static image).
- **Static images**: Procedural images live under `course/image/` next to the Python script that generated them — run individually (e.g. `uv run python course/image/week01_compound_growth.py`) to regenerate the PNG.
- **Animations / interactive components**: Files live under `course/animation/` (HTML/JS for interactive demos, video clips for YouTube).
- **Translation status**: `uv run python scripts/translate.py --check` to see what needs translation.
- **Auto-translate**: `uv run python scripts/translate-batch.py` — driven by `scripts/configs.json`, which selects the LLM provider (Anthropic / OpenAI / Gemini), model, thinking effort, target locales, optional output directory, and an optional file selector. Requires the matching provider API key (`ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `GEMINI_API_KEY`). The script prints per-file progress as it runs.
- **Full pipeline**: `bash scripts/build-all.sh` — checks translations, auto-translates if a provider API key is set, rebuilds website.
- **Regeneration**: After editing any markdown file, re-run `uv run python scripts/build.py` to rebuild the website.

## Session History (before commit)

**Before every `git commit`, export the current chat session to `session_history/`.** Run the `/save-session` skill (which calls `~/.claude/skills/export-session.py`) and then stage the resulting log alongside your other changes. The intent is to preserve a readable, Claude-Code-`/export`-style transcript of the work that produced each commit so the project history doubles as a research log.

Output filename pattern: `session_history/<YYYY-MM-DD>_from_<starting-git-hash>.log` (e.g. `session_history/2026-04-16_from_afbc120.log`). The `<starting-git-hash>` is the short hash of `HEAD` at the moment the chat session began, **not** the commit being created right now — the file documents the work that happened on top of that baseline.

**Required header** (prepended to the log by the export script — keep this in sync if you change the script). Match Claude Code's `/export` formatting as closely as possible, then add this metadata block at the very top before the conversation transcript:

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

Pull the token + cost numbers from the same source `/cost` uses (the JSONL transcript's `usage` records, summed across the main thread and every sub-agent invocation). If a number truly cannot be determined, write `unknown` rather than zero so it's obvious the value was missing rather than free.

Commit the log file in the **same commit** as the code/content changes it produced (one self-contained commit per session). Never push session logs to a public remote without first scrubbing any secrets the conversation may have included.

## Website

- **URL**: https://chanmainvest.github.io/tutorial/
- Home page uses `course/overview.md` (not README.md)
- Single-panel layout with a top navigation bar (no sidebar)
- **Multilevel hamburger menu** anchored to the top-right corner: top level lists Levels 1-5 + Side Lessons + Glossary; each Level expands into its weekly lessons
- Breadcrumb navigation: Chanma Investment Tutorial > Level N > Week N: Topic
- Country flag emoji language selector (🇬🇧 EN / 🇭🇰 HK / 🇹🇼 TW / 🇨🇳 CN) in the top bar
- Dark/light theme toggle next to the language selector. Both themes are designed to look professional (light: cream background with dark navy text and gold accents; dark: deep navy background with warm off-white text and gold accents). The user's choice persists in `localStorage`.
- Prev/next buttons in page footer
- FAQ, Disclaimer, and Glossary linked in site footer
- Professional trust-building theme (serif body font, dark navy navigation, gold accents)

## Language & Terminology Notes

- HK Chinese (繁體): Uses Hong Kong financial terminology (e.g., 股票, 窩輪, 通脹, 對沖, 沽空)
- TW Chinese (繁體): Uses Taiwan financial terminology (e.g., 股票, 權證, 通膨, 避險, 放空)
- CN Chinese (簡體): Uses Mainland China financial terminology (e.g., 股票, 权证, 通胀, 对冲, 做空)
- All three share Traditional/Simplified script differences plus distinct financial jargon
- Full terminology glossary is maintained in `scripts/terminology.json` (canonical EN term → HK / TW / CN translations). The translation script loads it from JSON, and `scripts/build.py` renders a **Glossary** page on the website (table view) from the same source so that readers and translators see the same vocabulary.
