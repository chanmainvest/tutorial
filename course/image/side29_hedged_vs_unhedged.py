"""Side 29, §2.2 -- EFA (unhedged) vs HEFA (hedged) wealth path 2010-Apr 2026.

Wealth of $1 invested in EFA (iShares MSCI EAFE) vs HEFA (iShares
Currency Hedged MSCI EAFE).  HEFA inception was Jan 2014; pre-inception
years are simulated from EAFE local-currency returns.  Annual total
returns are embedded inline.

Annotated regimes:
  2014-2015  hedged wins (USD rallies)
  2017       unhedged wins (EUR rallies)
  2022       hedged wins (USD spikes)

Run:
    uv run python course/image/side29_hedged_vs_unhedged.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side29_hedged_vs_unhedged"


# (year, EFA total return USD, HEFA total return = EAFE local-cur pre-2014)
RET = {
    2010: ( 0.082,  0.060),
    2011: (-0.121, -0.105),
    2012: ( 0.188,  0.134),
    2013: ( 0.214,  0.269),
    2014: (-0.062,  0.054),
    2015: (-0.010,  0.050),
    2016: ( 0.014,  0.057),
    2017: ( 0.249,  0.166),
    2018: (-0.140, -0.102),
    2019: ( 0.219,  0.247),
    2020: ( 0.076,  0.053),
    2021: ( 0.110,  0.200),
    2022: (-0.168, -0.078),
    2023: ( 0.184,  0.190),
    2024: ( 0.035,  0.128),
    2025: ( 0.140,  0.130),
    2026: ( 0.050,  0.040),  # YTD through April 2026
}


def _series():
    years = sorted(RET.keys())
    efa = np.array([RET[y][0] for y in years])
    hef = np.array([RET[y][1] for y in years])
    cum_efa = np.concatenate([[1.0], np.cumprod(1 + efa)])
    cum_hef = np.concatenate([[1.0], np.cumprod(1 + hef)])
    yrs = np.array([years[0] - 1] + years)
    return yrs, cum_efa, cum_hef


LANG_STRINGS = {
    "en": {
        "title":    "$1 in EFA (unhedged) vs HEFA (hedged), 2010-Apr 2026",
        "subtitle": "Same EAFE basket. The hedge wins when USD rallies, loses when USD falls. Total return roughly equal; vol is not.",
        "xlabel":   "Year-end",
        "ylabel":   "Cumulative wealth ($)",
        "efa":      "EFA -- unhedged",
        "hef":      "HEFA -- hedged",
        "ann":      "Geometric ann. total return: EFA {e:.1%}  HEFA {h:.1%}",
        "footer":   "Sources: iShares EFA / HEFA fact-sheets. Pre-2014 HEFA backfilled with MSCI EAFE local-currency NR. 2026 partial (Q1).",
        "ann1415":  "2014-15\nUSD rallies\nHEFA +9pp",
        "ann17":    "2017\nUSD falls\nEFA +8pp",
        "ann22":    "2022\nUSD spike\nHEFA +9pp",
    },
    "hk": {
        "title":    "EFA(未對沖) vs HEFA(對沖)1 美元成長,2010-2026 年 4 月",
        "subtitle": "同一個 EAFE 籃子。美元升值時對沖勝出,美元貶值時相反。總回報接近;波動率不同。",
        "xlabel":   "年底",
        "ylabel":   "累計財富(美元)",
        "efa":      "EFA──未對沖",
        "hef":      "HEFA──對沖",
        "ann":      "幾何年化總回報:EFA {e:.1%}  HEFA {h:.1%}",
        "footer":   "資料:iShares EFA / HEFA 概覽。2014 年前 HEFA 以 MSCI EAFE 本幣 NR 回填。2026 為 Q1 部分數據。",
        "ann1415":  "2014-15\n美元升\nHEFA +9pp",
        "ann17":    "2017\n美元跌\nEFA +8pp",
        "ann22":    "2022\n美元飆升\nHEFA +9pp",
    },
    "tw": {
        "title":    "EFA(未避險) vs HEFA(避險)1 美元成長,2010-2026 年 4 月",
        "subtitle": "同一個 EAFE 籃子。美元升值時避險勝出,美元貶值時相反。總報酬接近;波動率不同。",
        "xlabel":   "年底",
        "ylabel":   "累計財富(美元)",
        "efa":      "EFA──未避險",
        "hef":      "HEFA──避險",
        "ann":      "幾何年化總報酬:EFA {e:.1%}  HEFA {h:.1%}",
        "footer":   "資料:iShares EFA / HEFA 概覽。2014 年前 HEFA 以 MSCI EAFE 本幣 NR 回填。2026 為 Q1 部分數據。",
        "ann1415":  "2014-15\n美元升\nHEFA +9pp",
        "ann17":    "2017\n美元跌\nEFA +8pp",
        "ann22":    "2022\n美元飆升\nHEFA +9pp",
    },
    "cn": {
        "title":    "EFA(未对冲) vs HEFA(对冲)1 美元成长,2010-2026 年 4 月",
        "subtitle": "同一个 EAFE 篮子。美元升值时对冲胜出,美元贬值时相反。总回报接近;波动率不同。",
        "xlabel":   "年底",
        "ylabel":   "累计财富(美元)",
        "efa":      "EFA──未对冲",
        "hef":      "HEFA──对冲",
        "ann":      "几何年化总回报:EFA {e:.1%}  HEFA {h:.1%}",
        "footer":   "资料:iShares EFA / HEFA 概览。2014 年前 HEFA 以 MSCI EAFE 本币 NR 回填。2026 为 Q1 部分数据。",
        "ann1415":  "2014-15\n美元升\nHEFA +9pp",
        "ann17":    "2017\n美元跌\nEFA +8pp",
        "ann22":    "2022\n美元飙升\nHEFA +9pp",
    },
}


def build_fig(s):
    yrs, cum_efa, cum_hef = _series()
    p = PALETTE_LIGHT

    # Escape $-signs (mathtext) for non-title strings used in annotations / footer.
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    fig, ax = plt.subplots(figsize=(11.0, 6.2))
    style_axes(ax, p)

    # Highlight regime years
    ax.axvspan(2013.5, 2015.5, color=p["red"],   alpha=0.05)
    ax.axvspan(2016.5, 2017.5, color=p["blue"],  alpha=0.05)
    ax.axvspan(2021.5, 2022.5, color=p["red"],   alpha=0.07)

    ax.plot(yrs, cum_efa, color=p["blue"],  linewidth=2.6, label=s["efa"])
    ax.plot(yrs, cum_hef, color=p["accent"],linewidth=2.6, label=s["hef"])

    # End-point dollar labels
    last_y = yrs[-1]
    ax.text(last_y + 0.15, cum_efa[-1], f"\\${cum_efa[-1]:.2f}",
            color=p["blue"], fontsize=10, va="center", fontweight="bold")
    ax.text(last_y + 0.15, cum_hef[-1], f"\\${cum_hef[-1]:.2f}",
            color=p["accent"], fontsize=10, va="center", fontweight="bold")

    # Regime annotations
    ax.text(2014.5, 0.78, s["ann1415"], fontsize=8.5, color=p["red"],
            ha="center", style="italic")
    ax.text(2017.0, 0.78, s["ann17"], fontsize=8.5, color=p["blue"],
            ha="center", style="italic")
    ax.text(2022.0, 0.78, s["ann22"], fontsize=8.5, color=p["red"],
            ha="center", style="italic")

    n = len(yrs) - 1
    ann_e = cum_efa[-1] ** (1 / n) - 1
    ann_h = cum_hef[-1] ** (1 / n) - 1

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24, color=p["fg"])
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.text(0, -0.135, s["ann"].format(e=ann_e, h=ann_h),
            transform=ax.transAxes, fontsize=9.5, color=p["fg"])
    ax.text(0, -0.18, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"], style="italic")

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.set_ylim(0.6, max(cum_efa.max(), cum_hef.max()) * 1.12)

    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
