# Interactive Chart Style — Canonical Pattern

The Week 1 charts `interactive/week01_money_supply.html` and
`interactive/week01_us_debt_m2.html` are the canonical reference
for all interactive chart components in this course. Read this file
before creating a new interactive chart, or before editing an existing
one to match the family. (Week 1's `week01_shadow_cpi.html` predates
this convention and uses Plotly legend-click for series toggle instead
of explicit toggle buttons — treat it as the deviation, not the model.)

The components are designed to be embedded as iframes by the website
build (`scripts/build.py`) on top of the static PNG, with a toggle so
the user can fall back to the static image.

## File structure

- **Single self-contained HTML file** under `interactive/`,
  named `weekNN_topic.html` (or `sideNN_topic.html`) to match the
  static image at `image/weekNN_topic.png` so the build can
  pair them automatically.
- **Only external dependency:** Plotly from CDN, pinned to a specific
  version:

  ```html
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js" charset="utf-8"></script>
  ```

  No bundlers, no npm, no shared JS/CSS. Each chart is a single
  reviewable HTML file.
- All JS lives in **one IIFE at the bottom of the file** so identifier
  collisions across charts on the same page are impossible:

  ```html
  <script>
  (function () {
      // ...everything...
  })();
  </script>
  ```
- All CSS classes use a **2-letter component prefix** (`ms-` for money
  supply, `ud-` for US debt, etc.). Pick a fresh 2-letter prefix per
  chart to avoid CSS leakage when the host page embeds without an
  iframe.

## CSS theme variables (light + dark)

Every chart defines its own scoped colour palette via CSS custom
properties on `:root` (light theme) and `html[data-theme="dark"]
.<prefix>-root` (dark theme):

```css
:root {
    --ms-bg: #fdfbf5;
    --ms-text: #1a2332;
    --ms-muted: #6b7280;
    --ms-border: #d6d3c4;
    --ms-card: #fdfbf5;
    --ms-accent: #b8860b;          /* gold — site accent */
    --ms-c-us: #0d47a1;            /* per-series colours */
    /* ... */
}
html[data-theme="dark"] .ms-root,
.ms-root[data-theme="dark"] {
    --ms-bg: #0f1724;
    --ms-text: #e6e6e6;
    --ms-muted: #9aa3b2;
    --ms-border: #2a3441;
    --ms-card: #0f1724;
    --ms-c-us: #5a8dee;            /* lighter, higher-contrast in dark */
    /* ... */
}
```

The accent colour is the site gold (`#b8860b`). Series colours pick
darker tones for light, lighter tones for dark. Background and card
colours match the site's cream / deep-navy theme — do not invent new
backgrounds.

JS reads computed values via:

```js
function getCssVar(name) {
    return getComputedStyle(ROOT).getPropertyValue(name).trim();
}
function darkMode() {
    return document.documentElement.getAttribute("data-theme") === "dark";
}
```

…and feeds them into Plotly's `paper_bgcolor`, `plot_bgcolor`, axis
`color`, `gridcolor`, line `color`, and hover label colours. This is
why the chart re-renders on theme change — Plotly's colours are baked
into the layout, not driven by CSS.

## Theme-change reactivity

A `MutationObserver` on `<html data-theme>` triggers a full re-render
(and toggle rebuild, where applicable) so the chart instantly matches
when the user flips the site theme:

```js
const themeObserver = new MutationObserver(() => { buildToggles(); render(); });
themeObserver.observe(document.documentElement, {
    attributes: true, attributeFilter: ["data-theme"],
});
```

## iframe height sync via postMessage

The host page embeds the chart as an iframe and resizes it to the
content's actual height. The chart reports its scroll height upward:

```js
function reportHeight() {
    try {
        var h = Math.ceil(document.documentElement.scrollHeight);
        parent.postMessage({ type: 'lesson-interactive-resize', height: h }, '*');
    } catch (e) { /* sandboxed — ignore */ }
}
if (typeof ResizeObserver !== 'undefined') {
    new ResizeObserver(reportHeight).observe(document.body);
}
window.addEventListener('resize', reportHeight);
setTimeout(reportHeight, 50);
setTimeout(reportHeight, 500);
```

Always send `{ type: 'lesson-interactive-resize', height: <int> }` —
the build's iframe wrapper listens for exactly that message shape.
Leave the two trailing `setTimeout` calls in: they handle the case
where ResizeObserver fires before Plotly's first paint.

## `?lang=` query param + localized strings table

The chart picks its language from `?lang=` (the website appends this
when embedding so the chart matches the page locale):

```js
const I18N = {
    en: { /* keys */ },
    hk: { /* keys */ },
    tw: { /* keys */ },
    cn: { /* keys */ },
};
function currentLang() {
    const p = new URLSearchParams(window.location.search);
    const l = (p.get("lang") || "en").toLowerCase();
    return I18N.hasOwnProperty(l) ? l : "en";
}
const T = I18N[currentLang()];
```

All four locales **must** be present (`en`, `hk`, `tw`, `cn`). Use the
locale conventions from `scripts/terminology.json` — HK uses HK
financial vocabulary, TW uses TW vocabulary, CN uses Simplified +
Mainland vocabulary. Do not share strings across locales by reference;
each locale gets its own object even if two values would currently be
identical (HK and TW often diverge on a single term later).

Each `T` entry carries the chart's labels: preset names, axis titles,
series names (long for legend / hover, **short** for toggle pills and
unified-hover rows), stat-card titles, and the caption.

After building DOM, call an `applyI18n()` that writes every static
label out of `T` (button text, headings, caption innerHTML). Don't
hard-code English in the HTML body — it's only there as a default that
`applyI18n()` overwrites.

### CJK label considerations

CJK strings are visually 1.5–2× wider per character than the same
English text. To keep the chart usable in HK/TW/CN:

- Always provide a **short** form for any string that lands in a
  toggle pill, a chip, a hover-row name, or a unified-hover bullet.
  English keys end with `_short` (e.g. `cur_us_short: "USD"`,
  `cur_us_short: "美元"`).
- Use the long form for the legend and the stat-card title; use the
  short form for hover lines, toggles, and any space-constrained UI:
  ```js
  hovertemplate: "<b>" + T["cur_" + c.key + "_short"] + ": %{y:.0f}</b><extra></extra>",
  txt.textContent = T["cur_" + c.key + "_short"];
  ```
- The toggle row can wrap (`flex-wrap: wrap`), but each individual
  pill must not — keep its label one-or-two chars in CJK ("美元",
  "M2", "國債") so it never breaks mid-character.
- For unified hover (`hovermode: "x unified"`) every visible series'
  label appears in the same tooltip; long names quickly overflow the
  chart in CJK. Always use the short name in `hovertemplate`.

## Toggle button pattern (canonical)

The canonical "show/hide series" UI is a row of **explicit toggle
pills above the chart** — not Plotly's legend-click. Each pill is a
`<label>` wrapping a hidden checkbox plus a coloured dot and the
short label, with an `.active` class driven by the checkbox state and
a `--cur-color` CSS var so the active border + dot pick up the
series colour:

```css
.ms-cc-toggle {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 0.85rem; color: var(--ms-text); font-weight: 600;
    cursor: pointer; padding: 4px 10px; border-radius: 999px;
    border: 1px solid var(--ms-border);
    background: var(--ms-card); user-select: none;
}
.ms-cc-toggle input[type="checkbox"] { display: none; }
.ms-cc-toggle .ms-cc-dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: var(--ms-muted); transition: background 0.15s;
}
.ms-cc-toggle.active { border-color: var(--cur-color, var(--ms-accent)); }
.ms-cc-toggle.active .ms-cc-dot { background: var(--cur-color, var(--ms-accent)); }
.ms-cc-toggle.disabled { opacity: 0.5; cursor: not-allowed; }
```

`buildToggles()` rebuilds the row from a `SERIES`/`CURRENCIES` array
each render (so theme changes pick up new colours):

```js
function buildToggles() {
    // preserve heading + any "axis toggle" siblings, clear the rest
    const heading = HOST.querySelector(".ms-cc-label");
    HOST.innerHTML = "";
    if (heading) HOST.appendChild(heading);
    SERIES.forEach(s => {
        const colorVar = getCssVar(s.color);
        const lbl = document.createElement("label");
        lbl.className = "ms-cc-toggle" + (enabled[s.key] ? " active" : "")
            + (s.required ? " disabled" : "");
        lbl.style.setProperty("--cur-color", colorVar);
        const cb = document.createElement("input");
        cb.type = "checkbox";
        cb.checked = enabled[s.key];
        cb.disabled = s.required;
        cb.addEventListener("change", () => {
            enabled[s.key] = cb.checked || s.required;
            lbl.classList.toggle("active", enabled[s.key]);
            render();
        });
        const dot = document.createElement("span");
        dot.className = "ms-cc-dot";
        const txt = document.createElement("span");
        txt.textContent = T["cur_" + s.key + "_short"];
        lbl.appendChild(cb); lbl.appendChild(dot); lbl.appendChild(txt);
        HOST.appendChild(lbl);
    });
}
```

### Default visibility rules

- Every series declares `default: true|false` and optionally
  `required: true` (cannot be turned off; e.g. USD as the comparison
  baseline in money_supply).
- Default to **showing the headline series** that the lesson is
  actually arguing about. Hide series that are useful supplements but
  add visual noise (e.g. TWD/HKD off by default in money_supply since
  they're regional drill-downs).
- A required series renders with `.disabled` styling and a disabled
  checkbox so the user sees it can't be toggled, but the visual
  treatment still reads as "on".

## Chart layout (Plotly)

Identical layout block across the family. Copy this verbatim and only
adjust margins / axis titles:

```js
const layout = {
    margin: { l: 64, r: 28, t: 12, b: 44 },
    paper_bgcolor: colorBg, plot_bgcolor: colorBg,
    font: { family: "Segoe UI, Helvetica, Arial, sans-serif", color: colorText, size: 12 },
    xaxis: {
        title: { text: T.xaxis, font: { color: colorMuted, size: 11 } },
        gridcolor: colorGrid, zerolinecolor: colorGrid, color: colorText,
        tickformat: "d",
        showspikes: true, spikemode: "across", spikedash: "dot",
        spikecolor: colorMuted, spikethickness: 1,
    },
    yaxis: {
        title: { text: yLabel, font: { color: colorMuted, size: 11 } },
        gridcolor: colorGrid, zerolinecolor: colorGrid, color: colorText,
    },
    legend: {
        orientation: "h", x: 0.5, xanchor: "center",
        y: 1.06, yanchor: "bottom",
        font: { size: 11 }, bgcolor: "rgba(0,0,0,0)",
    },
    hovermode: "x unified",
    hoverlabel: { bgcolor: colorBg, bordercolor: colorMuted, font: { color: colorText } },
};
Plotly.react(CHART, traces, layout, { displayModeBar: false, responsive: true });
```

Key invariants:

- `hovermode: "x unified"` plus `xaxis.showspikes: true` give the
  year-by-year crosshair that every chart in the family advertises in
  its caption.
- `displayModeBar: false` — never expose Plotly's toolbar.
- `responsive: true` — required for the iframe height-report loop.
- Always `Plotly.react(...)` (not `Plotly.newPlot`) inside `render()`
  so re-renders (theme change, toggle, mode switch) are diffed
  instead of redrawn.
- Computed `colorGrid` is theme-aware:
  `darkMode() ? "rgba(255,255,255,0.08)" : "rgba(0,0,0,0.07)"`.

## Time-window controls (preset pills + slider)

The "10Y / 25Y / 45Y / Max" preset row + start-year slider is the
default time-axis UX:

```html
<div class="ms-presets" id="ms-presets" role="tablist">
    <button type="button" data-years="10">10Y</button>
    <button type="button" data-years="25">25Y</button>
    <button type="button" data-years="45">45Y</button>
    <button type="button" data-years="max" id="ms-preset-max" class="active">Max</button>
</div>
```

```js
PRESETS.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
        PRESETS.querySelectorAll("button").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        preset = btn.dataset.years;
        if (preset === "max") {
            SLIDER.disabled = true;
        } else {
            SLIDER.disabled = false;
            startYear = YEARS[YEARS.length - parseInt(preset, 10)];
        }
        render();
    });
});
```

`Max` disables the slider; any other preset enables it and clamps
`startYear` so the window never overruns the data range.

## Mode toggle pattern (e.g. YoY vs Cumulative, linear vs log)

Two flavours used in the family:

- **Radio group** (shadow_cpi: YoY % vs Cumulative price level) —
  semantically a single-choice mode switch:

  ```html
  <div class="sc-mode-controls">
      <label><input type="radio" name="sc-mode" value="yoy" checked> <span id="sc-mode-yoy">YoY % change</span></label>
      <label><input type="radio" name="sc-mode" value="cumul"> <span id="sc-mode-cumul">Cumulative price level (indexed = 100 at start)</span></label>
  </div>
  ```

- **Single checkbox pill** (us_debt_m2: linear vs log) — for binary
  modifiers, dock on the right of the toggle row with `margin-left:
  auto;` (and reset to `0` in the mobile media query):

  ```css
  .ud-axis-toggle { margin-left: auto; /* ... */ }
  @media (max-width: 640px) { .ud-axis-toggle { margin-left: 0; } }
  ```

Either pattern: the handler updates a module-scoped `mode` / `useLog`
variable and calls `render()`, which switches axis title, `type`
(`linear` | `log`), `tickformat`, and `hovertemplate` accordingly.

## Stats cards (below the chart)

Three (or N) summary cards in a CSS grid, each with a coloured
left-border that matches the series:

```css
.ms-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 10px; margin-top: 14px; }
.ms-stat { background: var(--ms-card);
           border: 1px solid var(--ms-border);
           border-left: 4px solid var(--ms-muted);
           border-radius: 8px; padding: 10px 12px; }
@media (max-width: 640px) { .ms-stats { grid-template-columns: 1fr; } }
```

Inside `render()`, recompute and rewrite the cards each time so
window/toggle changes update the numbers. Each card is `name` (uppercase
muted label), `val` (large tabular number), `detail` (small muted line
— typically "from <baseYear>" or "× window start").

## Mobile / narrow-viewport rules

Every chart includes the same `@media (max-width: 640px)` block that:

- collapses the stats grid to a single column,
- shrinks chart height from 460px to 380px,
- shrinks preset pills,
- resets any `margin-left: auto` toggles to `margin-left: 0` so they
  don't get pushed off-screen.

## Checklist for a new interactive chart

1. Pick a fresh 2-letter CSS prefix.
2. Light + dark CSS-var palettes (use site cream / deep-navy
   backgrounds, gold accent, distinct per-series colours).
3. IIFE wrapper, single HTML file, Plotly CDN script tag.
4. `I18N` table with all four locales (`en`, `hk`, `tw`, `cn`); short
   forms for every label that hits a toggle pill or hover row.
5. `currentLang()` reads `?lang=`, defaults to `en`.
6. Explicit toggle pills above the chart (NOT legend-click), built by
   `buildToggles()` from a `SERIES` array; rebuild on theme change.
7. Default visibility rules — headline series on, supplements off,
   required-baseline series locked on.
8. Plotly layout block with `hovermode: "x unified"`,
   `xaxis.showspikes`, `displayModeBar: false`, `responsive: true`,
   theme-aware grid colour. Use `Plotly.react`.
9. Preset pills + start-year slider for the time axis (`Max` disables
   the slider).
10. Optional mode toggle (radio group for choices, right-docked pill
    checkbox for binary modifiers).
11. Stats cards in a CSS grid below the chart, recomputed each render.
12. Mobile media query (single-column stats, smaller chart, reset
    `margin-left`).
13. `MutationObserver` on `<html data-theme>` → rebuild toggles +
    re-render.
14. `postMessage({ type: 'lesson-interactive-resize', height })` height
    reporting via ResizeObserver + window resize + two `setTimeout`
    primings.
15. `applyI18n()` rewrites every static label from `T` after DOM is
    built.
