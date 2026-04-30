"""Week 35, §2.4 — Altman Z-score time series for GE, F, AAPL.

Three line series with the 1.81 (distress) and 2.99 (safe) horizontal
threshold lines. Z values are approximate from public 10-K data using
the original Altman (1968) public-firm formula:
    Z = 1.2(WC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(MVE/TL) + 1.0(S/TA)

  GE 2010-2024: drifted from gray-zone recovery (~2.5) into distress
                by 2017-2019 (~1.2-1.5), recovered post-spinoff to >3
                by 2024.
  F  2018-2024: persistently parked in low gray-zone (1.4-1.7).
  AAPL 2020-2024: deeply safe (5-7) the entire stretch.

Run:
    uv run python course/image/week35_zscore_distress.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week35_zscore_distress"


GE_YEARS  = list(range(2010, 2025))
GE_Z      = [2.45, 2.55, 2.62, 2.58, 2.40, 1.95, 1.82, 1.42, 1.18, 1.55,
             1.62, 2.05, 2.45, 3.10, 3.55]

F_YEARS   = list(range(2018, 2025))
F_Z       = [1.55, 1.50, 1.18, 1.72, 1.45, 1.60, 1.68]

AAPL_YEARS = list(range(2020, 2025))
AAPL_Z     = [5.45, 6.85, 6.05, 6.40, 5.80]

THRESH_DISTRESS = 1.81
THRESH_SAFE     = 2.99


LANG_STRINGS = {
    "en": {
        "title":    "Altman Z-score: GE 2010-2024, Ford 2018-2024, Apple 2020-2024",
        "subtitle": "Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E. Below 1.81 = distress band; 1.81-2.99 = gray zone; above 2.99 = safe. Trend dominates altitude.",
        "xlabel":   "Fiscal year",
        "ylabel":   "Altman Z-score",
        "ge":       "GE (industrial conglomerate)",
        "f":        "Ford (deep-cyclical auto)",
        "aapl":     "Apple (capital-light brand)",
        "lbl_distress": "Distress (Z < 1.81)",
        "lbl_safe":     "Safe (Z > 2.99)",
        "anno_ge2018":  "GE 2018: Z=1.18, dividend cut",
        "anno_aapl":    "AAPL: deeply safe entire period",
        "anno_f":       "F: gray zone for years",
        "footer":   "GE drifted into distress for three years before the 2018 dividend cut. The trend was the signal.",
    },
    "hk": {
        "title":    "Altman Z 分數:GE 2010-2024、福特 2018-2024、蘋果 2020-2024",
        "subtitle": "Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E。低於 1.81 為困境帶;1.81-2.99 為灰色區;高於 2.99 為安全。趨勢比絕對水平重要。",
        "xlabel":   "財政年度",
        "ylabel":   "Altman Z 分數",
        "ge":       "GE(工業綜合企業)",
        "f":        "福特(深週期汽車)",
        "aapl":     "蘋果(輕資產品牌)",
        "lbl_distress": "困境(Z < 1.81)",
        "lbl_safe":     "安全(Z > 2.99)",
        "anno_ge2018":  "GE 2018:Z=1.18,削減股息",
        "anno_aapl":    "AAPL:整段時期深度安全",
        "anno_f":       "F:多年位於灰色區",
        "footer":   "GE 在 2018 削減股息前已連續三年處於困境帶。趨勢就是訊號。",
    },
    "tw": {
        "title":    "Altman Z 分數:GE 2010-2024、福特 2018-2024、蘋果 2020-2024",
        "subtitle": "Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E。低於 1.81 為困境帶;1.81-2.99 為灰色區;高於 2.99 為安全。趨勢比絕對水平重要。",
        "xlabel":   "會計年度",
        "ylabel":   "Altman Z 分數",
        "ge":       "GE(工業綜合企業)",
        "f":        "福特(深景氣循環汽車)",
        "aapl":     "蘋果(輕資產品牌)",
        "lbl_distress": "困境(Z < 1.81)",
        "lbl_safe":     "安全(Z > 2.99)",
        "anno_ge2018":  "GE 2018:Z=1.18,削減股利",
        "anno_aapl":    "AAPL:整段時期深度安全",
        "anno_f":       "F:多年位於灰色區",
        "footer":   "GE 在 2018 削減股利前已連續三年處於困境帶。趨勢就是訊號。",
    },
    "cn": {
        "title":    "Altman Z 分数:GE 2010-2024、福特 2018-2024、苹果 2020-2024",
        "subtitle": "Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E。低于 1.81 为困境带;1.81-2.99 为灰色区;高于 2.99 为安全。趋势比绝对水平重要。",
        "xlabel":   "财政年度",
        "ylabel":   "Altman Z 分数",
        "ge":       "GE(工业综合企业)",
        "f":        "福特(深周期汽车)",
        "aapl":     "苹果(轻资产品牌)",
        "lbl_distress": "困境(Z < 1.81)",
        "lbl_safe":     "安全(Z > 2.99)",
        "anno_ge2018":  "GE 2018:Z=1.18,削减股息",
        "anno_aapl":    "AAPL:整段时期深度安全",
        "anno_f":       "F:多年位于灰色区",
        "footer":   "GE 在 2018 削减股息前已连续三年处于困境带。趋势就是信号。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(12, 6.4))
    style_axes(ax, p)

    # Shaded bands
    ax.axhspan(0, THRESH_DISTRESS, color=p["red"], alpha=0.06, zorder=0)
    ax.axhspan(THRESH_DISTRESS, THRESH_SAFE, color=p["accent"], alpha=0.06, zorder=0)
    ax.axhspan(THRESH_SAFE, 8.0, color=p["green"], alpha=0.06, zorder=0)

    # Threshold lines
    ax.axhline(THRESH_DISTRESS, color=p["red"], linestyle="--",
               linewidth=1.2, alpha=0.75)
    ax.axhline(THRESH_SAFE, color=p["green"], linestyle="--",
               linewidth=1.2, alpha=0.75)

    ax.text(2010.2, THRESH_DISTRESS - 0.18, s["lbl_distress"],
            fontsize=9, color=p["red"], fontweight="bold")
    ax.text(2010.2, THRESH_SAFE + 0.10, s["lbl_safe"],
            fontsize=9, color=p["green"], fontweight="bold")

    # Series
    ax.plot(GE_YEARS, GE_Z, color=p["blue"], linewidth=2.4,
            marker="o", markersize=6, label=s["ge"])
    ax.plot(F_YEARS, F_Z, color=p["red"], linewidth=2.4,
            marker="s", markersize=6, label=s["f"])
    ax.plot(AAPL_YEARS, AAPL_Z, color=p["accent"], linewidth=2.4,
            marker="^", markersize=7, label=s["aapl"])

    # Annotations
    ax.annotate(s["anno_ge2018"],
                xy=(2018, 1.18), xytext=(2014.5, 0.30),
                fontsize=9.5, color=p["blue"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["blue"], lw=1.2))
    ax.text(2024.2, AAPL_Z[-1], s["anno_aapl"],
            fontsize=9, color=p["accent"], va="center",
            fontstyle="italic")
    ax.text(2021.5, 0.85, s["anno_f"],
            fontsize=9, color=p["red"], fontstyle="italic")

    ax.set_xlim(2009.5, 2027.5)
    ax.set_ylim(0, 7.5)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xticks(list(range(2010, 2025, 2)))

    ax.legend(loc="upper left", fontsize=10, framealpha=0.92)

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontstyle="italic")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
