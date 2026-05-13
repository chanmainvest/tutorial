# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Investment education platform ("Chanma Investment Tutorial") that synthesizes multiple professional certification curricula (CFA, with other certifications to follow) and decades of battle-tested retail investing experience into a structured tutorial course with YouTube content. The course explicitly highlights where professional certification teaching falls short for retail investors and where retail investors have advantages professionals don't. The repository produces:
- A 52-week core course (beginner to advanced) in Markdown, organized into 5 levels
- 30 side lessons for supplementary topics
- A course overview page (home page) and a level overview page for each of the 5 levels
- YouTube scripts with two-host format: **Horace** (陳馬, experienced retail investor/teacher) and **Stella** (小魚, recent college graduate/student)
- Visual explanations rendered three ways depending on output:
  - **Static images embedded in markdown** — every visual concept has a static image so the markdown reads on its own. Procedural charts use Python (matplotlib) to generate the PNG; conceptual illustrations use AI-generated images (e.g., Nano Banana).
  - **Animations / video for YouTube** — the same visuals become animated clips or short video segments referenced in the YouTube script.
  - **Interactive demos for the published website** — when an interactive component exists, the website upgrades the static image into a live demo (with a toggle to fall back to the static image).
- Multilingual versions (English, HK Chinese, TW Chinese, CN Chinese)
- A static website with multilevel hamburger navigation, breadcrumbs, country flag language selector, and a dark/light theme toggle
- Course FAQ and Disclaimer pages

## Repository Structure

```
references/          # Source materials (professional certification syllabi, calculator guide, YouTube strategy, real-world PM examples)
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
  animation/         # Animation clips / video segments for the YouTube script
  interactive/       # Live HTML/JS interactive demos that the website
                     # can swap in for the static image (same
                     # weekNN_topic.* naming convention as image/ and animation/)
course_hk/           # Hong Kong Chinese translations
course_tw/           # Taiwan Chinese translations
course_cn/           # Mainland China Chinese translations
docs/                # Generated static website (do not edit directly)
scripts/             # Build and translation scripts (all Python, run via uv)
  configs.json       # LLM provider/model/effort + translation options
  terminology.json   # Cross-locale terminology glossary
```

## Reference Materials

Key source documents in `references/` drive content creation:
- **profession_syllabus.md** — Professional certification curricula (currently CFA Levels I-III; CMT, CFP, FRM, CAIA and other certifications to be added) mapped to retail investor competencies, organized by topic area with "common retail gaps" annotations
- **90s.pm.investing.md** — Real-world portfolio-manager case material from the 1990s used as illustrative examples
- **investment_youtube_strategy.md** — 5-tier YouTube content strategy (Newbie -> Professional) with monetization and teaching philosophy
- **cfa_calculator_guide.md** — TI BA II Plus calculator walkthrough with keystroke examples

## Lesson Format

Every lesson file (core weeks, side lessons, level overviews, and course overview) is a **single markdown file** containing both parts:

1. **Reading section (Part 1)**: four top-level sections — `### 1. Why This Is Important`, `### 2. What You Need to Know`, `### 3. Common Misconceptions`, `### 4. Q&A` — written as text plus **static images embedded in the markdown**. Where a concept also has an interactive web component, the reading section includes a short prose description of how the interactive demo behaves (so the markdown alone is still self-contained). **The reading section is the canonical source of truth** for every lesson — if the YouTube script, static image, animation, or interactive demo ever disagrees with the reading section, the reading section wins and the others must be updated to match.
2. **YouTube script section (Part 2)**: Same material adapted for two hosts (Horace = teacher, Stella = student). Includes `[ANIMATION: ...]` cues at the right locations pointing to clips in `course/animation/`, plus visual explanation descriptions.

**Section numbering convention.** Use **decimal-style numbering**, not letter-prefixed lists:

- Top-level reading sections: `### 1.`, `### 2.`, `### 3.`, `### 4.` (NOT `### a)`, `### b)`, etc.).
- Subsections under §2 (the "What You Need to Know" deep dive): `#### 2.1`, `#### 2.2`, `#### 2.3`, … (NOT bare `#### 1.`, `#### 2.`, which would shadow the top-level numbers).
- If a §3 or §4 subsection ever needs to be its own H4, use `#### 3.1`, `#### 4.1`, etc. — same dotted-decimal pattern.

This keeps cross-references unambiguous (`§2.4` is one specific subsection, not the fourth bullet under any of four parallel parents) and reads cleanly in both English and Chinese translations. The build strips the now-redundant `## Part 1: Reading Section` heading from the website (Part 2 is already stripped, so naming Part 1 is meaningless on the public site); the H3/H4 numbered sections become the visible top-level structure.

**Asset layout for a lesson:**
- Static images and the Python code that generates procedural ones live under `image/` (e.g. `image/week01_compound_growth.png` + `image/week01_compound_growth.py`).
- Animation clips / video segments for the YouTube script live under `course/animation/` (e.g. `animation/week01_compound_growth.mp4`).
- Interactive HTML/JS demos for the website live under `interactive/` (e.g. `interactive/week01_compound_growth.html`). Same `weekNN_topic.*` naming convention as `image/` and `animation/` so the build can match them up.
- The markdown file references the static image; the website upgrade step looks for a matching interactive component and, if it exists, swaps the static image for the live demo (with a toggle to fall back to the static image).

**IMPORTANT: Both parts live in the same file intentionally.** When updating or editing any lesson content, you MUST also update the corresponding YouTube script in Part 2 of that same file to keep them consistent. The reading section and YouTube script cover the same material — they must stay in sync.

The website only displays Part 1 (reading section). `scripts/build.py` strips Part 2 (everything from `## Part 2: YouTube Script` onward) and the now-redundant `## Part 1: Reading Section` header from web output. It also strips the in-markdown "interactive demo description" prose for any lesson where an interactive component is actually present (the live component replaces it); where no interactive component exists, the description is removed and only the static image remains.

## YouTube Host Characters

- **Horace (陳馬)** — Teacher. Middle-aged experienced retail investor. Explains concepts from years of market experience.
- **Stella (小魚)** — Student. Young college-graduated woman learning to invest her savings. Asks the questions viewers are thinking.

When writing English YouTube scripts, always use the English names (Horace / Stella). In Chinese translations (HK/TW/CN), use ONLY the Chinese names (陳馬 / 小魚) — do not retain or parenthesise the English names.

## Content Philosophy

- Teaching model: Macro context -> Strategy concept -> Tactical execution
- Progressive skill-building with forward/backward references between lessons
- Course is grounded in professional certification knowledge (CFA and others) **plus** battle-tested retail investing experience. It explicitly calls out the blind spots where professional curricula fall short for retail investors, and the situations where retail investors have advantages professionals don't (e.g., no benchmark pressure, ability to hold cash, smaller size). Don't use the word "trader" — this course is for retail *investors*.
- Side lessons cover practical topics (calculator usage, specific instruments, real-world examples) that don't fit the weekly progression
- Animations and interactive demos should make abstract financial concepts tangible — animations carry the explanation in the YouTube script; interactive demos let website readers manipulate the same concept directly.
- Website is audience-facing (no technical/GitHub details) and hosts the **full** course material — every weekly lesson, side lesson, level overview, course overview, FAQ, disclaimer, and the terminology glossary — across all four languages

## Citing Named Sources — Don't Quote "Horace"

**Never put an attributed quote into Horace's mouth as the
*authority* for a claim.** Horace is a fictional teaching
character; readers will eventually realise he is not a real
investor with a public track record, and a course that backs its
strongest claims with "as Horace puts it" reads as a single
unverified voice on the internet. Use Horace as the *narrator and
synthesiser*, but cite **named, reputable, real-world figures**
for the substantive points.

**Rules:**

- When making a claim with a famous-quote feel ("X is Y", "every
  Z rests on W"), find the **named investor / economist /
  practitioner / regulator** who actually said something close
  to it and quote them with attribution. Examples:
  J.P. Morgan ("Gold is money. Everything else is credit.",
  Pujo Committee 1912), Voltaire on paper money, Keynes on the
  "barbarous relic," Buffett on gold's lack of cashflow,
  Ray Dalio on All Weather and gold, Harry Browne on the
  Permanent Portfolio, Rick Rule on gold sizing, Howard Marks
  on risk, Jeremy Grantham on commodity supercycles,
  Christopher Cole / Artemis Capital on the Dragon Portfolio,
  William Sharpe on the Sharpe ratio, etc.
- Avoid phrases of the form *"As Horace puts it, [strong
  claim]"*, *"Horace emphasises that [strong claim]"*, *"Horace's
  view is [strong claim]"* when the claim is empirical or
  attributable. Replace with a named source plus a brief Horace
  framing: *"Ray Dalio's 2024 LinkedIn essay argues … and that
  framing is the lens this lesson uses."*
- Horace **can** still own *interpretations*, *frameworks*, and
  *teaching choices* — e.g. "Horace splits portfolios into a
  permanent core plus tactical sleeves" — when the framing is
  pedagogical, not an empirical claim about markets.
- Where SOUL.md is the source of a strong opinion, **express it
  through the named investor or research that originally
  established the idea** (Dalio, Browne, Cole, Mandelbrot,
  Taleb, etc.), not as Horace's personal pronouncement. SOUL.md
  is the lens, not the citation.
- For statistical / regulatory / historical facts (CPI series,
  Basel III rules, central-bank purchases, tax-code sections),
  cite the **primary source** (FRED series IDs, BIS / Basel
  Committee documents, World Gold Council *Gold Demand Trends*,
  IRS section numbers, etc.).

This rule applies to all reader-facing content (lessons, scripts,
glossary, FAQ, disclaimer, website pages, translations) in all
languages.

## Investment Philosophy (`SOUL.md`) — REQUIRED READING

`SOUL.md` in the repo root contains Horace's personal investment
philosophy: 17 numbered principles (market efficiency vs alpha + the
expression-toolkit requirement, the 40-year passive consensus and its
specific reversal triggers, stores of value as belief, sources of
structural alpha, vol-surface-aware TA in the post-COVID 0DTE era, no
penny stocks in a passive-flow big-cap world, momentum/mean-reversion
*and* vol-on/vol-off regimes, the irrational-vs-solvent constraint, the
four tranches (with options-based phase-3 execution), the barbell
replacing the passive core, after-tax return management via options and
margin, US-as-the-only-market with HK/CN uninvestable and TW = TSMC,
and the Dragon-portfolio shape with both Fed put and tail hedges). It
is the **soul** of this course — the lens through which every lesson
must be written and reviewed.

**Read `SOUL.md` before creating, editing, or reviewing any lesson
content** (core week, side lesson, level overview, course overview,
glossary entry, FAQ, disclaimer — in any language).

**SOUL.md is internal — never expose it to the reader.** It is the
guiding philosophy *behind* the course, not a document the audience
should know exists. When writing or editing any reader-facing content
(lessons, scripts, glossary, FAQ, disclaimer, website pages, YouTube
scripts, translations):

- **Do not name `SOUL.md`, "SOUL", or "the soul document"** anywhere in
  reader-facing text.
- **Do not refer to "the 17 principles", "Horace's philosophy
  document", or any phrasing that implies an underlying manifesto** the
  reader could go look up.
- **Do not link to `SOUL.md`** from any course markdown, website page,
  or generated artifact. The file is repo-internal only.
- **Express SOUL ideas as the lesson's own teaching** — in Horace's
  voice, with concrete reasoning, examples, and market history. The
  reader should absorb the philosophy through the material itself, not
  be told "this comes from a separate philosophy doc."
- When reviewing existing content, **flag and remove** any direct
  mention of SOUL.md or its principle numbers (e.g. "per SOUL principle
  #7"). Rephrase as standalone teaching.

**Application workflow & conflict-detection rules** (how to weave SOUL.md
into a lesson, how to flag contradictions during review, when *not* to
edit SOUL.md yourself): see `.claude/docs/soul-application.md`. Read it
before any lesson edit/review pass.

## Build & Development

All scripts are Python. **Always run them via `uv`** as the package manager (e.g. `uv run python scripts/build.py`) — `uv` resolves the project's dependencies (declared in `pyproject.toml`) without polluting the system Python. No Node.js dependencies required for the build pipeline.

- **Website**: `uv run python scripts/build.py` — generates static HTML from all markdown files with multilevel hamburger navigation, breadcrumbs, country flag language selector, dark/light theme toggle, and prev/next page buttons. YouTube scripts are stripped from web output. Where a matching interactive component exists in `interactive/`, the corresponding static image is replaced with the live component (the user can toggle back to the static image).
- **Static images**: Procedural images live under `image/` next to the Python script that generated them — run individually (e.g. `uv run python image/week01_compound_growth.py`) to regenerate the PNG.
- **Animations**: Video clips / animated segments for the YouTube script live under `course/animation/`.
- **Interactive demos**: HTML/JS components for the website live under `interactive/`. The build script auto-detects a matching `interactive/weekNN_topic.html` and swaps it in for the static image (with a toggle so the user can fall back to the static image). Canonical chart style (file structure, toggle-button pattern, theme variables, `?lang=` handling, postMessage height sync, CJK label rules): `.claude/docs/interactive-chart-style.md` — read before creating or editing any interactive chart.
- **Translation status**: `uv run python scripts/translate.py --check` to see what needs translation.
- **Auto-translate**: `uv run python scripts/translate-batch.py` — driven by `scripts/configs.json`, which selects the LLM provider (Anthropic / OpenAI / Gemini), model, thinking effort, target locales, optional output directory, and an optional file selector. Requires the matching provider API key (`ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `GEMINI_API_KEY`). The script prints per-file progress as it runs.
- **Full pipeline**: `bash scripts/build-all.sh` — checks translations, auto-translates if a provider API key is set, rebuilds website.
- **Regeneration policy**: Do **not** run `scripts/build.py` or any translation script unless the user explicitly asks. The user often makes incremental edits and does not want a full rebuild or full retranslate after each change. Wait for an explicit "rebuild" / "translate" instruction.

## Session History (before commit)

**Before every `git commit`, export the current chat session to
`session_history/`.** Run the `/save-session` skill (which calls
`.claude/skills/export-session.py`) and stage the resulting log alongside
your other changes — one self-contained commit per session. The project
history doubles as a research log.

Output filename pattern:
`session_history/<YYYY-MM-DD>_from_<starting-git-hash>.log`. The hash is
`HEAD` at the moment the chat session **began**, not the commit being
created now.

Format spec (header template, token/cost field semantics, secret-scrub
policy): `.claude/docs/session-history-format.md`. Read it only if
you're editing `export-session.py` or troubleshooting the header.

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
- **On-device AI tutor** — floating bottom-right button on every page.
  Runs Gemma 4 E2B locally in the browser via WebGPU + transformers.js,
  with opt-in cross-lesson RAG over a static chunk index. No data leaves
  the device. Source: `web_assets/chatbot.{js,css}`; chunk index:
  `scripts/build_chatbot_index.py` → `docs/assets/chatbot_chunks.json`
  (regenerate whenever lesson content changes). Full architecture
  (model loading, RAG pipeline, IndexedDB caching, status chip states,
  prompt assembly, browser-support fallback): `.claude/docs/chatbot-architecture.md`.

## Language & Terminology Notes

- HK Chinese (繁體): Uses Hong Kong financial terminology (e.g., 股票, 窩輪, 通脹, 對沖, 沽空)
- TW Chinese (繁體): Uses Taiwan financial terminology (e.g., 股票, 權證, 通膨, 避險, 放空)
- CN Chinese (簡體): Uses Mainland China financial terminology (e.g., 股票, 权证, 通胀, 对冲, 做空)
- All three share Traditional/Simplified script differences plus distinct financial jargon
- Full terminology glossary is maintained in `scripts/terminology.json` (canonical EN term → HK / TW / CN translations). The translation script loads it from JSON, and `scripts/build.py` renders a **Glossary** page on the website (table view) from the same source so that readers and translators see the same vocabulary.
