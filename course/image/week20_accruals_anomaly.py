"""Week 20, §2.4 — The accruals anomaly (Sloan 1996), 1990-2020.

Bar chart: average annual one-year-ahead return for the five quintiles
of accruals-to-assets, US-listed firms, 1990-2020. Quintile 1 is the
lowest-accruals (most cash-backed earnings) firms, Quintile 5 is the
highest-accruals (most accrual-backed earnings) firms. The decile
spread reported by Sloan (1996) was roughly 10%; replications through
2020 (Lewellen, Resutek, Green-Hand-Soliman) show a 5-10% spread that
has narrowed but not disappeared after the paper's publication.

The bars below are representative averages, not a specific year.

Run:
    uv run python course/image/week20_accruals_anomaly.py
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
BASE = "week20_accruals_anomaly"


# Representative one-year-ahead annual returns by accruals quintile,
# US-listed firms, 1990-2020. Q1 = lowest accruals (cleanest cash),
# Q5 = highest accruals (most aggressive). Spread ~9%, monotonic.
QUINTILES = ["Q1", "Q2", "Q3", "Q4", "Q5"]
RETURNS = [16.8, 14.2, 12.4, 10.1, 7.6]  # in percent
MARKET_AVG = sum(RETURNS) / len(RETURNS)  # ~12.2%


LANG_STRINGS = {
    "en": {
        "title":    "The accruals anomaly: average annual return by accruals-to-assets quintile, 1990-2020",
        "subtitle": "US-listed firms sorted into five quintiles each year by total accruals divided by average total assets. Bars show one-year-ahead average annual return. Sloan (1996) and many replications since.",
        "xlabel":   "Accruals-to-assets quintile (Q1 = lowest accruals, cleanest cash; Q5 = highest)",
        "ylabel":   "Average one-year-ahead return (%)",
        "labels":   {"Q1": "Q1\nlowest", "Q2": "Q2", "Q3": "Q3\nmedian",
                     "Q4": "Q4", "Q5": "Q5\nhighest"},
        "anno_q1":  "Q1 (cash-backed): +16.8%",
        "anno_q5":  "Q5 (accrual-heavy): +7.6%",
        "anno_avg": f"Cross-section avg ~{MARKET_AVG:.1f}%",
        "spread":   f"Long Q1 / short Q5 spread: ~{RETURNS[0]-RETURNS[-1]:.1f}% per year",
        "footer":   "Cash earnings beat accrual earnings. The signal weakens after publication, but it never inverts.",
    },
    "hk": {
        "title":    "應計項目異常:按應計/資產五分位的年均回報,1990-2020",
        "subtitle": "美國上市公司每年按 應計總額 / 平均資產 分為五分位。柱狀為其後一年的平均年回報。Sloan (1996) 與多項重現研究。",
        "xlabel":   "應計項目/資產 五分位(Q1=最低,現金最乾淨;Q5=最高)",
        "ylabel":   "其後一年平均回報(%)",
        "labels":   {"Q1": "Q1\n最低", "Q2": "Q2", "Q3": "Q3\n中位",
                     "Q4": "Q4", "Q5": "Q5\n最高"},
        "anno_q1":  "Q1(現金支撐):+16.8%",
        "anno_q5":  "Q5(應計偏重):+7.6%",
        "anno_avg": f"橫斷面平均約 {MARKET_AVG:.1f}%",
        "spread":   f"做多 Q1、做空 Q5 年化價差約 {RETURNS[0]-RETURNS[-1]:.1f}%",
        "footer":   "現金盈利勝過應計盈利。訊號在論文發表後減弱,但從未反轉。",
    },
    "tw": {
        "title":    "應計項目異常:按應計/資產五分位的年均報酬,1990-2020",
        "subtitle": "美國上市公司每年按 應計總額 / 平均資產 分為五分位。柱狀為其後一年的平均年報酬。Sloan (1996) 與多項重現研究。",
        "xlabel":   "應計項目/資產 五分位(Q1=最低,現金最乾淨;Q5=最高)",
        "ylabel":   "其後一年平均報酬(%)",
        "labels":   {"Q1": "Q1\n最低", "Q2": "Q2", "Q3": "Q3\n中位",
                     "Q4": "Q4", "Q5": "Q5\n最高"},
        "anno_q1":  "Q1(現金支撐):+16.8%",
        "anno_q5":  "Q5(應計偏重):+7.6%",
        "anno_avg": f"橫斷面平均約 {MARKET_AVG:.1f}%",
        "spread":   f"做多 Q1、做空 Q5 年化價差約 {RETURNS[0]-RETURNS[-1]:.1f}%",
        "footer":   "現金盈餘勝過應計盈餘。訊號在論文發表後減弱,但從未反轉。",
    },
    "cn": {
        "title":    "应计项目异常:按应计/资产五分位的年均回报,1990-2020",
        "subtitle": "美国上市公司每年按 应计总额 / 平均资产 分为五分位。柱状为其后一年的平均年回报。Sloan (1996) 与多项重现研究。",
        "xlabel":   "应计项目/资产 五分位(Q1=最低,现金最干净;Q5=最高)",
        "ylabel":   "其后一年平均回报(%)",
        "labels":   {"Q1": "Q1\n最低", "Q2": "Q2", "Q3": "Q3\n中位",
                     "Q4": "Q4", "Q5": "Q5\n最高"},
        "anno_q1":  "Q1(现金支撑):+16.8%",
        "anno_q5":  "Q5(应计偏重):+7.6%",
        "anno_avg": f"横截面平均约 {MARKET_AVG:.1f}%",
        "spread":   f"做多 Q1、做空 Q5 年化价差约 {RETURNS[0]-RETURNS[-1]:.1f}%",
        "footer":   "现金盈利胜过应计盈利。信号在论文发表后减弱,但从未反转。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2))
    style_axes(ax, p)

    xs = np.arange(len(QUINTILES))
    # Colour gradient: green (Q1) to red (Q5)
    colors = [p["green"], "#5d8f3c", p["accent"], "#c75d2c", p["red"]]
    bars = ax.bar(xs, RETURNS, color=colors, edgecolor=colors, width=0.62, alpha=0.9)

    for i, (bar, val) in enumerate(zip(bars, RETURNS)):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.35,
                f"{val:.1f}%", ha="center", va="bottom",
                fontsize=11, fontweight="bold", color=p["fg"])

    ax.axhline(MARKET_AVG, color=p["muted"], linestyle="--", linewidth=1.0)
    ax.text(len(QUINTILES) - 0.5, MARKET_AVG + 0.25, s["anno_avg"],
            fontsize=9, color=p["muted"], ha="right", style="italic")

    ax.set_xticks(xs)
    ax.set_xticklabels([s["labels"][q] for q in QUINTILES])
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, max(RETURNS) * 1.20)
    ax.set_yticks([0, 4, 8, 12, 16, 20])
    ax.set_yticklabels(["0%", "4%", "8%", "12%", "16%", "20%"])

    # Spread annotation in upper-right
    ax.text(0.99, 0.96, s["spread"], transform=ax.transAxes,
            fontsize=10.5, fontweight="bold", color=p["blue"],
            ha="right", va="top",
            bbox=dict(facecolor=p["bg"], edgecolor=p["grid"],
                      boxstyle="round,pad=0.4"))

    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.18, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontstyle="italic")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
