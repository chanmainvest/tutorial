# Code Review

_Generated: 2026-04-21 14:09 UTC — 8 comment(s)_

---

## CLAUDE.md

### `@CLAUDE.md:L7`
> **Highlighted text:**
> Investment education platform ("Chanma Investment Tutorial") that transforms CFA-level knowledge into a structured tutorial course with YouTube content. The repository produces:
>
> not just CFA knowledge, see the README.md

### `@CLAUDE.md:L49-51`
> **Highlighted text:**
> profession_syllabus.md — CFA Levels I-III curriculum mapped to retail trader competencies, organized by topic area with "common retail gaps" annotations
>
> the profession_syllabus not just have the CFA, it has other certification syllabus too

### `@CLAUDE.md:L57-58`
> **Highlighted text:**
> Reading section (Part 1): a) Why this is important, b) What you need to know, c) Common misconceptions, d) Common Q&A — written as text plus static images embedded in the markdown. Where a concept also has an interactive web component, the reading section includes a short prose description of how the interactive demo behaves (so the markdown alone is still self-contained).
>
> the reading section is the source of other course material, if there are disagreement, the reading section is the right one

### `@CLAUDE.md:L61-63`
> **Highlighted text:**
> Animation clips and interactive web components live under course/animation/ (e.g. animation/week01_compound_growth.html or a video file).
>
> interactive web component has its own folder, the file follow the same naming convention.

### `@CLAUDE.md:L78-83`
> **Highlighted text:**
> Core course maps roughly to CFA curriculum but reordered for retail trader relevance
>
> we need to know CFA and other professional certificate's knowledge, but this course will point out the blind spot and where they fell short.  it emphasis on battle test experience, apply to retail investor.  don't use the word trader, user investor.  there are some thing retail can do but not professional.

### `@CLAUDE.md:L78-83`
> **Highlighted text:**
> Animations should make abstract financial concepts tangible
>
> also the interactive demo

### `@CLAUDE.md:L89-95`
> **Highlighted text:**
> Website: uv run python scripts/build.py — generates static HTML from all markdown files with multilevel hamburger navigation, breadcrumbs, country flag language selector, dark/light theme toggle, and prev/next page buttons. YouTube scripts are stripped from web output. Where a matching interactive component exists in course/animation/, the corresponding static image is replaced with the live component (the user can toggle back to the static image).
>
> interactive component lives under interactive folder, not animation folder

### `@CLAUDE.md:L89-95`
> **Highlighted text:**
> Regeneration: After editing any markdown file, re-run uv run python scripts/build.py to rebuild the website.
>
> don't regenerate or retranslate unless explicitly instructed.  as I am editing into more details, I don't need full rebuild or full retranslate

---
