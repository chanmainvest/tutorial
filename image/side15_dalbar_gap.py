"""Side 15, §1 — The Dalbar behaviour gap.

Two-panel chart:
  - LEFT: annualised return bars across 10y / 20y / 30y trailing
    windows ending December 2024. S&P 500 vs average equity-fund
    investor (representative DALBAR QAIB long-run figures, also
    consistent with Morningstar Mind-the-Gap follow-on studies).
  - RIGHT: cumulative wealth on a $100k initial over the 30y window
    at the two CAGRs (S&P 10.2%/yr vs investor 6.8%/yr) -> $1.86M
    vs $720k -> ~$1.14M forfeited.

Run:
    uv run python course/image/side15_dalbar_gap.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "side15_dalbar_gap"

WINDOWS  = ["10y", "20y", "30y"]
SP500    = [0.120, 0.099, 0.102]   # S&P 500 trailing annualised through Dec 2024
INVESTOR = [0.080, 0.060, 0.068]   # Avg equity-fund investor (Dalbar long-run)
INITIAL  = 100_000.0
YEARS_30 = 30
SP_CAGR  = SP500[2]
INV_CAGR = INVESTOR[2]

LANG_STRINGS = {
    "en": {
        "title":    "The Dalbar gap: S&P 500 vs the average investor",
        "subtitle": "Trailing annualised returns ending Dec 2024 + cumulative wealth on $100,000 initial over 30 years.",
        "left_xlabel":  "Trailing window",
        "left_ylabel":  "Annualised return",
        "right_xlabel": "Years",
        "right_ylabel": "Wealth ($)",
        "fund":     "S&P 500",
        "investor": "Avg fund investor",
        "gap":      "behaviour gap",
        "wealth_gap": "gap = ${gap:,.0f}\n({mult:.1f}x starting balance)",
        "footer":   "Behaviour costs ~3-4 pp/yr (Dalbar headline) or ~1.5-2 pp/yr (Vanguard / Morningstar replications). Compounded 30y, even the conservative read forfeits multiples of the starting balance.",
        "sp_label": "S&P 500: ${v:,.0f}",
        "inv_label": "Investor: ${v:,.0f}",
    },
    "hk": {
        "title":    "Dalbar 落差:標普 500 vs 平均投資者",
        "subtitle": "截至 2024 年 12 月之滾動年化回報 + 10 萬美元起始本金、30 年的累積財富。",
        "left_xlabel":  "滾動窗口",
        "left_ylabel":  "年化回報",
        "right_xlabel": "年數",
        "right_ylabel": "財富 ($)",
        "fund":     "標普 500",
        "investor": "平均基金投資者",
        "gap":      "行為落差",
        "wealth_gap": "落差 = ${gap:,.0f}\n(起始本金的 {mult:.1f} 倍)",
        "footer":   "行為每年蝕約 3-4 個百分點(Dalbar 頭條),或約 1.5-2 個百分點(Vanguard / Morningstar 修正)。30 年複利下,即使保守估計也蝕去起始本金的數倍。",
        "sp_label": "標普 500:${v:,.0f}",
        "inv_label": "投資者:${v:,.0f}",
    },
    "tw": {
        "title":    "Dalbar 落差:標普 500 vs 平均投資人",
        "subtitle": "截至 2024 年 12 月之滾動年化報酬 + 10 萬美元起始本金、30 年的累積財富。",
        "left_xlabel":  "滾動窗口",
        "left_ylabel":  "年化報酬",
        "right_xlabel": "年數",
        "right_ylabel": "財富 ($)",
        "fund":     "標普 500",
        "investor": "平均基金投資人",
        "gap":      "行為落差",
        "wealth_gap": "落差 = ${gap:,.0f}\n(起始本金的 {mult:.1f} 倍)",
        "footer":   "行為每年損失約 3-4 個百分點(Dalbar 頭條),或約 1.5-2 個百分點(Vanguard / Morningstar 修正)。30 年複利下,即使保守估計也損失起始本金的數倍。",
        "sp_label": "標普 500:${v:,.0f}",
        "inv_label": "投資人:${v:,.0f}",
    },
    "cn": {
        "title":    "Dalbar 落差:标普 500 vs 平均投资者",
        "subtitle": "截至 2024 年 12 月之滚动年化回报 + 10 万美元起始本金、30 年的累积财富。",
        "left_xlabel":  "滚动窗口",
        "left_ylabel":  "年化回报",
        "right_xlabel": "年数",
        "right_ylabel": "财富 ($)",
        "fund":     "标普 500",
        "investor": "平均基金投资者",
        "gap":      "行为落差",
        "wealth_gap": "落差 = ${gap:,.0f}\n(起始本金的 {mult:.1f} 倍)",
        "footer":   "行为每年损失约 3-4 个百分点(Dalbar 头条),或约 1.5-2 个百分点(Vanguard / Morningstar 修正)。30 年复利下,即使保守估计也损失起始本金的数倍。",
        "sp_label": "标普 500:${v:,.0f}",
        "inv_label": "投资者:${v:,.0f}",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.5, 6.0), dpi=150,
                                   gridspec_kw={"width_ratios": [1.0, 1.05]})
    style_axes(axL, p)
    style_axes(axR, p)

    # ---- LEFT panel: bar chart of trailing CAGRs ---------------------
    x = np.arange(len(WINDOWS))
    w = 0.36

    bars_f = axL.bar(x - w / 2, SP500,    width=w, color=p["accent"],
                     label=s["fund"], edgecolor="none")
    bars_i = axL.bar(x + w / 2, INVESTOR, width=w, color=p["blue"],
                     label=s["investor"], edgecolor="none")

    for xi, fr, ir in zip(x, SP500, INVESTOR):
        axL.add_patch(plt.Rectangle(
            (xi - w / 2, ir), w, fr - ir,
            facecolor=p["red"], alpha=0.18, edgecolor=p["red"],
            linewidth=0.8, hatch="///",
        ))
        gap = fr - ir
        axL.annotate(
            f"-{gap*100:.1f} pp",
            xy=(xi, (fr + ir) / 2),
            ha="center", va="center",
            fontsize=10, fontweight="bold",
            color=p["red"],
        )

    for bar, val in zip(bars_f, SP500):
        axL.text(bar.get_x() + bar.get_width() / 2, val + 0.003,
                 f"{val*100:.1f}%", ha="center", va="bottom",
                 fontsize=10, fontweight="bold", color=p["accent"])
    for bar, val in zip(bars_i, INVESTOR):
        axL.text(bar.get_x() + bar.get_width() / 2, val + 0.003,
                 f"{val*100:.1f}%", ha="center", va="bottom",
                 fontsize=10, fontweight="bold", color=p["blue"])

    gap_patch = plt.Rectangle((0, 0), 1, 1,
                              facecolor=p["red"], alpha=0.18,
                              edgecolor=p["red"], hatch="///",
                              label=s["gap"])
    handles, labels = axL.get_legend_handles_labels()
    handles.append(gap_patch)
    labels.append(s["gap"])
    axL.legend(handles, labels, loc="upper right", frameon=False, fontsize=9.5)

    axL.set_xticks(x)
    axL.set_xticklabels(WINDOWS)
    axL.set_xlabel(s["left_xlabel"])
    axL.set_ylabel(s["left_ylabel"])
    axL.set_ylim(0, max(SP500) * 1.25)
    axL.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))

    # ---- RIGHT panel: cumulative wealth on $100k -------------------
    yrs = np.arange(0, YEARS_30 + 1)
    sp_path  = INITIAL * (1.0 + SP_CAGR)  ** yrs
    inv_path = INITIAL * (1.0 + INV_CAGR) ** yrs

    axR.plot(yrs, sp_path,  color=p["accent"], linewidth=2.6, label=s["fund"])
    axR.plot(yrs, inv_path, color=p["blue"],   linewidth=2.6, label=s["investor"])
    axR.fill_between(yrs, inv_path, sp_path,
                     color=p["red"], alpha=0.18, hatch="///",
                     edgecolor=p["red"], linewidth=0.6)

    sp_end  = sp_path[-1]
    inv_end = inv_path[-1]
    gap_end = sp_end - inv_end
    mult_end = gap_end / INITIAL

    axR.scatter([YEARS_30, YEARS_30], [sp_end, inv_end],
                color=[p["accent"], p["blue"]], s=55, zorder=5,
                edgecolor="white", linewidth=1.2)
    axR.annotate(
        s["sp_label"].format(v=sp_end),
        xy=(YEARS_30, sp_end), xytext=(YEARS_30 - 13.5, sp_end + 90_000),
        fontsize=10, color=p["accent"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["accent"], lw=0.8),
    )
    axR.annotate(
        s["inv_label"].format(v=inv_end),
        xy=(YEARS_30, inv_end), xytext=(YEARS_30 - 13.5, inv_end - 230_000),
        fontsize=10, color=p["blue"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["blue"], lw=0.8),
    )

    # Gap callout in the middle of the shaded band.
    mid_y = (sp_path[20] + inv_path[20]) / 2
    axR.text(20, mid_y,
             s["wealth_gap"].format(gap=gap_end, mult=mult_end),
             fontsize=10.5, color=p["red"], fontweight="bold",
             ha="center", va="center",
             bbox=dict(facecolor="white", edgecolor=p["red"],
                       boxstyle="round,pad=0.35", alpha=0.92))

    axR.set_xlabel(s["right_xlabel"])
    axR.set_ylabel(s["right_ylabel"])
    axR.set_xlim(0, YEARS_30 + 0.5)
    axR.set_ylim(0, sp_end * 1.18)
    axR.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda v, _: f"${v/1e6:.1f}M" if v >= 1e6 else f"${v/1e3:.0f}k"
    ))
    axR.legend(loc="upper left", frameon=False, fontsize=9.5)

    # ---- title + footer --------------------------------------------
    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 x=0.01, y=0.98, ha="left")
    fig.text(0.01, 0.93, s["subtitle"], fontsize=10, color=p["muted"])
    fig.text(0.01, 0.005, s["footer"], fontsize=9, color=p["muted"], style="italic")

    fig.tight_layout(rect=[0, 0.03, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
