# Lesson Rewrite Guide — internal agent instructions

You are rewriting one or more lessons in this tutorial. **Read this guide
first**, then read the locked reference lessons before producing output.

## Repo orientation

Workspace root: `c:\Users\hevan\work\chanmainvest\tutorial`

- `course/SOUL.md` — Horace's investing philosophy. The voice + recurring
  callbacks (alpha=rare, four tranches, barbell, US-only investable,
  vol-tail-wags-dog, etc.) come from here.
- `course/week01_why_invest.md` and `course/week02_index_funds_etfs.md` —
  **LOCKED**, canonical templates. Match their structure, depth, tone.
- `course/week03_risk_and_return.md` — fully-rewritten week, also
  canonical. Use as length / structure reference.
- `course/week04_sixty_forty.md` — also rewritten; canonical.
- `course/side01_calculator.md` — canonical side-lesson structure.
- `course/image/week03_*.py`, `course/image/week04_*.py` — image script
  templates.
- `course/interactive/week03_holding_periods.html` — interactive template.
- `course/interactive/side01_calculator.html` — alt interactive template
  (no Plotly, custom DOM).
- `scripts/chart_helpers.py` — `apply_cjk_font()`, `PALETTE_LIGHT`,
  `style_axes()`, `render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)`
- `scripts/market_data.py` — `damodaran_annual_returns()`,
  `fred_series()`, `yahoo_history()`, `stooq_history()`, prefetch CLI.

## Canonical markdown structure

```
# Week N: <Title>

---

## Part 1: Reading Section

---

### 1. Why This Is Important
   <prose, 4 numbered reasons, ~200-350 words>

### 2. What You Need to Know

#### 2.1 <Subsection>
   <prose with at most one image reference per subsection>

#### 2.2 <Subsection>
   ...

(Aim for 4-7 numbered subsections, each ~150-400 words.)

### 3. Common Misconceptions
   <numbered list of 6-10, each 1-3 sentences>

### 4. Q&A Section
   <8-12 Q&A items, each Q one line, A 2-6 sentences>

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** ...
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

(Sections: INTRO, then walkthrough of the week's images and interactive
with VISUAL cues like `[VISUAL: image/<base>.png]`, then OUTRO. ~500-900
script lines.)
```

### Style anchors (from SOUL.md)

Where natural, weave in: 1 (alpha rare), 2 (40-yr regime change),
3 (stores of value = belief), 5 (5 alpha sources), 6 (vol-tail-wags-dog),
8 (momentum + mean-reversion), 12 (irrational > solvent), 13 (four
tranches), 14 (barbell), 15 (tax via options/margin), 16 (US-only
investable). Don't sticker — fold them in as Horace's voice.

### Hard rules

- Date frame: April 2026.
- US-listed equities only (per SOUL #16).
- **No ASCII charts or diagrams.** Reference PNGs + the interactive.
- Use real historical data via `scripts/market_data.py` (FRED preferred,
  or `damodaran_annual_returns()` for asset-class series 1928-2024).
- Use ASCII hyphen `-`, **not** Unicode minus (U+2212) — breaks CJK font.
- Title `pad=24` and any subtitle at `y=1.02` to prevent overlap.
- No `letterspacing` matplotlib property — manually space chars instead.

## Image script template

```python
"""<Week N>, §<x.y> — <chart title>.

<one-paragraph data + design note>

Run:
    uv run python course/image/<base>.py
"""

from __future__ import annotations
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)
from scripts.market_data import damodaran_annual_returns  # or fred_series, etc.

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "weekNN_topic"

LANG_STRINGS = {
    "en": { "title": "...", "subtitle": "...", "xlabel": "...", "ylabel": "...", ... },
    "hk": { ... },
    "tw": { ... },
    "cn": { ... },
}

def build_fig(s):
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    # ... draw using PALETTE_LIGHT colours ...
    style_axes(ax)
    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    return fig

if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
```

`render_for_all_locales` writes both `<base>_<lang>.png` for each of
`en/hk/tw/cn` AND the canonical `<base>.png` (= the en file).

## Interactive HTML template

Use a unique 2-letter CSS prefix per chart (`hp-`, `tp-`, etc.).

Required structure:
- Plotly 2.35.2 via CDN.
- IIFE wrapper around all JS.
- `:root { --xx-bg, --xx-text, --xx-muted, --xx-border, --xx-card,
  --xx-accent, ... }` and `html[data-theme="dark"] .xx-root, .xx-root[data-theme="dark"] { ... }`
- I18N dict for `en, hk, tw, cn`. Read locale via
  `new URLSearchParams(location.search).get('lang')` (default `en`).
- At least one slider OR toggle pill bar OR preset row.
- `MutationObserver` on `<html data-theme>` to re-render Plotly with the
  new theme palette.
- `parent.postMessage({type:'lesson-interactive-resize', height:h}, '*')`
  on init + on resize.
- All chart data **embedded inline** (no runtime fetch).
- Plotly config: `{displayModeBar:false, responsive:true}` and
  `hovermode: 'x unified'` where appropriate.

Reference:
- `course/interactive/week03_holding_periods.html` — slider + toggle
- `course/interactive/week01_three_portfolios.html` — preset pills
- `course/interactive/week01_money_supply.html` — line chart with theme

## Per-lesson workflow

1. Read this guide.
2. Read `course/SOUL.md`, `course/week01_*.md`, `course/week03_*.md`.
3. Read the existing OLD `course/weekNN_<name>.md` to extract the topic.
4. Read the matching reference scripts (`course/image/week03_*.py`,
   `course/interactive/week03_*.html`, `scripts/chart_helpers.py`,
   `scripts/market_data.py`).
5. Write new markdown (overwrite the old file in place).
6. Write 2-3 image scripts in `course/image/`.
7. Write 1 interactive in `course/interactive/`.
8. Run each image script: `cd tutorial; uv run python course/image/<base>.py`
   to confirm it renders.
9. Report files created.

## Naming

- Image: `course/image/weekNN_<topic_short>.py` → `<base>.png` +
  `<base>_{en,hk,tw,cn}.png`.
- Interactive: `course/interactive/weekNN_<topic_short>.html`.
- Markdown filename **must not change** — overwrite in place.
