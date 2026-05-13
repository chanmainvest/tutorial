"""Side Lesson 10, §1 — Dividend ETF comparison: SCHD/VYM/DGRO/NOBL/SPYI.

Three grouped bars per ETF: trailing 5-year annualised total return,
trailing 5-year dividend CAGR, and current TTM yield. Numbers are
April-2026 fund-issuer fact-sheet snapshots. SPYI launched Aug 2022,
so its 5y total-return is reported as the live since-inception
annualised figure and its dividend growth is essentially zero by
construction (premium-write distribution scales with IV, not earnings).

Run:
    uv run python course/image/side10_div_etf_compare.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side10_div_etf_compare"


# (ticker, 5y total-return CAGR %, 5y dividend CAGR %, TTM yield %)
# April-2026 reference snapshots; SPYI has only ~3.5y live history so
# its TR is the since-inception annualised number and div growth is
# pinned at ~0 (option-premium distribution, not corporate dividend
# growth).
ROWS = [
    ("SCHD",  10.4, 10.0, 3.6),
    ("VYM",    9.9,  6.2, 2.9),
    ("DGRO",  11.6,  9.6, 2.3),
    ("NOBL",   9.2,  7.0, 2.0),
    ("SPYI",   9.5,  0.5, 12.0),
]


LANG_STRINGS = {
    "en": {
        "title":    "Dividend ETF comparison — April 2026",
        "subtitle": "Trailing 5-year total return, dividend CAGR, and TTM yield. SPYI is a covered-call ETF; its dividend growth is near-zero by construction.",
        "ylabel":   "%",
        "footer":   "Sources: Schwab/Vanguard/iShares/ProShares/Neos fund pages, distribution histories. SPYI 5y TR uses since-inception (Aug-2022) annualised return.",
        "leg_tr":   "5y total-return CAGR (%)",
        "leg_dg":   "5y dividend CAGR (%)",
        "leg_yld":  "Current TTM yield (%)",
    },
    "hk": {
        "title":    "派息 ETF 比較 — 2026 年 4 月",
        "subtitle": "近 5 年總回報、股息年增率、最近 12 個月收益率。SPYI 是備兌認購 ETF,其股息增長按結構接近零。",
        "ylabel":   "%",
        "footer":   "來源:Schwab、Vanguard、iShares、ProShares、Neos 基金頁面、配息紀錄。SPYI 5 年總回報採自 2022 年 8 月成立以來年化值。",
        "leg_tr":   "5 年總回報年化(%)",
        "leg_dg":   "5 年股息年增率(%)",
        "leg_yld":  "最近 12 個月收益率(%)",
    },
    "tw": {
        "title":    "派息 ETF 比較 — 2026 年 4 月",
        "subtitle": "近 5 年總回報、股息年增率、最近 12 個月殖利率。SPYI 為備兌買權 ETF,其股息增長依結構接近零。",
        "ylabel":   "%",
        "footer":   "來源:Schwab、Vanguard、iShares、ProShares、Neos 基金頁面、配息紀錄。SPYI 5 年總回報採自 2022 年 8 月成立以來年化值。",
        "leg_tr":   "5 年總回報年化(%)",
        "leg_dg":   "5 年股息年增率(%)",
        "leg_yld":  "最近 12 個月殖利率(%)",
    },
    "cn": {
        "title":    "分红 ETF 对比 — 2026 年 4 月",
        "subtitle": "近 5 年总回报、股息年增率、最近 12 个月收益率。SPYI 是备兑看涨 ETF,其股息增长按结构接近零。",
        "ylabel":   "%",
        "footer":   "来源:Schwab、Vanguard、iShares、ProShares、Neos 基金页面、分红记录。SPYI 5 年总回报采自 2022 年 8 月成立以来年化值。",
        "leg_tr":   "5 年总回报年化(%)",
        "leg_dg":   "5 年股息年增率(%)",
        "leg_yld":  "当前 12 个月收益率(%)",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    tickers = [r[0] for r in ROWS]
    tr  = [r[1] for r in ROWS]
    dg  = [r[2] for r in ROWS]
    yld = [r[3] for r in ROWS]

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax)
    x = np.arange(len(tickers))
    w = 0.27
    b1 = ax.bar(x - w, tr,  w, color=p["blue"],   edgecolor="white", linewidth=0.7,
                label=s["leg_tr"], zorder=3)
    b2 = ax.bar(x,     dg,  w, color=p["green"],  edgecolor="white", linewidth=0.7,
                label=s["leg_dg"], zorder=3)
    b3 = ax.bar(x + w, yld, w, color=p["accent"], edgecolor="white", linewidth=0.7,
                label=s["leg_yld"], zorder=3)

    for bars, vals in zip((b1, b2, b3), (tr, dg, yld)):
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, v + 0.18,
                    f"{v:.1f}", ha="center", va="bottom",
                    fontsize=9, fontweight="bold", color=p["fg"])

    ax.set_xticks(x)
    ax.set_xticklabels(tickers, fontsize=11, fontweight="bold")
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.set_ylim(0, max(max(tr), max(dg), max(yld)) * 1.18)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5, ncol=3)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.5, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
