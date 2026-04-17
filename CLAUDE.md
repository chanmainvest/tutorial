# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Investment education platform ("Chanma Investment Tutorial") that transforms CFA-level knowledge into a structured tutorial course with YouTube content. The repository produces:
- A 52-week core course (beginner to advanced) in Markdown, organized into 5 levels
- 30 side lessons for supplementary topics
- Level overview pages for each of the 5 levels
- YouTube scripts with two-host format: **Horace** (陳馬, experienced retail trader/teacher) and **Stella** (小魚, recent college graduate/student)
- Python animations for visual explanations
- Multilingual versions (English, HK Chinese, TW Chinese, CN Chinese)
- A static website with dropdown navigation, breadcrumbs, and country flag language selector
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
  animation/         # Python matplotlib visual animations
course_hk/           # Hong Kong Chinese translations
course_tw/           # Taiwan Chinese translations
course_cn/           # Mainland China Chinese translations
docs/                # Generated static website (do not edit directly)
scripts/             # Build and translation scripts (all Python)
```

## Reference Materials

Three key source documents in `references/` drive content creation:
- **profession_syllabus.md** — CFA Levels I-III curriculum mapped to retail trader competencies, organized by topic area with "common retail gaps" annotations
- **investment_youtube_strategy** — 5-tier YouTube content strategy (Newbie -> Professional) with monetization and teaching philosophy
- **cfa_calculator_guide** — TI BA II Plus calculator walkthrough with keystroke examples

## Lesson Format

Every lesson file (core weeks, side lessons, level overviews, and course overview) is a **single markdown file** containing both parts:

1. **Reading section (Part 1)**: a) Why this is important, b) What you need to know, c) Common misconceptions, d) Common Q&A — with text and diagrams
2. **YouTube script section (Part 2)**: Same material adapted for two hosts (Horace = teacher, Stella = student), includes visual explanation descriptions and animation references

**IMPORTANT: Both parts live in the same file intentionally.** When updating or editing any lesson content, you MUST also update the corresponding YouTube script in Part 2 of that same file to keep them consistent. The reading section and YouTube script cover the same material — they must stay in sync.

The website only displays Part 1 (reading section). YouTube scripts are in the markdown source but filtered out during site generation by `scripts/build.py` (it strips everything from `## Part 2: YouTube Script` onward).

## YouTube Host Characters

- **Horace (陳馬)** — Teacher. Middle-aged experienced retail trader. Explains concepts from years of market experience.
- **Stella (小魚)** — Student. Young college-graduated woman learning to invest her savings. Asks the questions viewers are thinking.

When writing YouTube scripts, always use these names. In Chinese translations, keep English names but their Chinese names may be used parenthetically.

## Content Philosophy

- Teaching model: Macro context -> Strategy concept -> Tactical execution
- Progressive skill-building with forward/backward references between lessons
- Core course maps roughly to CFA curriculum but reordered for retail trader relevance
- Side lessons cover practical topics (calculator usage, specific instruments, real-world examples) that don't fit the weekly progression
- Animations should make abstract financial concepts tangible
- Website is audience-facing (no technical/GitHub details) — course overview page, not README

## Build & Development

All scripts are Python. No Node.js dependencies required for the build pipeline.

- **Website**: `py -3 scripts/build.py` — generates static HTML from all markdown files with dropdown navigation, breadcrumbs, country flag language selector, and prev/next page buttons. YouTube scripts are automatically stripped from web output.
- **Animations**: Python scripts in `course/animation/` using matplotlib — run individually (e.g., `python course/animation/week01_compound_growth.py`) to generate PNG visualizations.
- **Translation status**: `py -3 scripts/translate.py --check` to see what needs translation.
- **Auto-translate**: `py -3 scripts/translate-batch.py --locale all` — translates via Claude API with sonnet 4.6 thinking. Requires `ANTHROPIC_API_KEY` env var and `pip install anthropic`.
- **Full pipeline**: `bash scripts/build-all.sh` — checks translations, auto-translates if API key set, rebuilds website.
- **Regeneration**: After editing any markdown file, re-run `py -3 scripts/build.py` to rebuild the website.

## Website

- **URL**: https://chanmainvest.github.io/tutorial/
- Home page uses `course/overview.md` (not README.md)
- Single-panel layout with top navigation bar (no sidebar)
- Dropdown menus for each level + side lessons
- Breadcrumb navigation: Chanma Investment Tutorial > Level N > Week N: Topic
- Country flag emoji language selector (EN/HK/TW/CN)
- Prev/next buttons in page footer
- FAQ and Disclaimer linked in site footer
- Professional trust-building theme (serif body font, dark navy navigation, gold accents)

## Language & Terminology Notes

- HK Chinese (繁體): Uses Hong Kong financial terminology (e.g., 股票, 窩輪, 通脹, 對沖, 沽空)
- TW Chinese (繁體): Uses Taiwan financial terminology (e.g., 股票, 權證, 通膨, 避險, 放空)
- CN Chinese (簡體): Uses Mainland China financial terminology (e.g., 股票, 权证, 通胀, 对冲, 做空)
- All three share Traditional/Simplified script differences plus distinct financial jargon
- Full terminology glossary is maintained in `scripts/translate-batch.py` TERMINOLOGY dictionary
