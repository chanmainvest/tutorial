# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Investment education platform that transforms CFA-level knowledge into a structured tutorial course with YouTube content. The repository produces:
- A 52-week core course (beginner to advanced) in Markdown
- Side lessons for supplementary topics
- YouTube scripts with two-host format (experienced teacher + eager student)
- Python/JS animations for visual explanations
- Multilingual versions (English, HK Chinese, TW Chinese, CN Chinese)
- A static website with language toggle serving all course content

## Repository Structure

```
references/          # Source materials (CFA syllabus, calculator guide, YouTube strategy)
course/              # English course materials (weekN_*.md, sideN_*.md)
course/animation/    # Python/JS/emoji-art visual animations
course_hk/           # Hong Kong Chinese translations
course_tw/           # Taiwan Chinese translations
course_cn/           # Mainland China Chinese translations
docs/                # Static website serving all course content
```

## Reference Materials

Three key source documents in `references/` drive content creation:
- **profession_syllabus.md** — CFA Levels I-III curriculum mapped to retail trader competencies, organized by topic area with "common retail gaps" annotations
- **investment_youtube_strategy** — 5-tier YouTube content strategy (Newbie → Professional) with monetization and teaching philosophy
- **cfa_calculator_guide** — TI BA II Plus calculator walkthrough with keystroke examples

## Lesson Format

Every lesson (core and side) follows this structure:
1. **Reading section**: a) Why this is important, b) What you need to know, c) Common misconceptions, d) Common Q&A — with text and diagrams
2. **YouTube script section**: Same material adapted for two hosts (teacher + student), includes visual explanation descriptions and animation references

## Content Philosophy

- Teaching model: Macro context → Strategy concept → Tactical execution
- Progressive skill-building with forward/backward references between lessons
- Core course maps roughly to CFA curriculum but reordered for retail trader relevance
- Side lessons cover practical topics (calculator usage, specific instruments, real-world examples) that don't fit the weekly progression
- Animations should make abstract financial concepts tangible

## Build & Development

- **Website**: `cd docs && node build.js` — generates static HTML from all markdown files with language toggle (EN/HK/TW/CN). No external dependencies needed (uses built-in markdown parser).
- **Animations**: Python scripts in `course/animation/` using matplotlib — run individually (e.g., `python course/animation/week01_compound_growth.py`) to generate PNG visualizations
- **Translation**: `python translate.py` creates placeholder translations in course_hk/, course_tw/, course_cn/. Use `python translate.py --check` to see translation status. Financial terminology mappings are in the script.
- **Regeneration**: After editing any markdown file, re-run `node docs/build.js` to rebuild the website. Translations are automatically picked up if present.

## Language & Terminology Notes

- HK Chinese (繁體): Uses Hong Kong financial terminology (e.g., 股票, 窩輪)
- TW Chinese (繁體): Uses Taiwan financial terminology (e.g., 股票, 權證)
- CN Chinese (簡體): Uses Mainland China financial terminology (e.g., 股票, 权证)
- All three share Traditional/Simplified script differences plus distinct financial jargon
