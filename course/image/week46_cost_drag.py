"""Week 46, §2.3 — Annualised return after costs as a function of round-trip cost,
for four turnover regimes.

Each strategy starts at the same 4% gross alpha. Net return = gross - turnover * cost.
Turnover by frequency: annual rebalance ~0.5, monthly ~6, weekly ~50, daily ~252.

Run:
    uv run python course/image/week46_cost_drag.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week46_cost_drag"

GROSS = 0.04  # 4% gross alpha baseline
COSTS_BPS = np.array([0, 5, 10, 20, 30, 50, 75, 100], dtype=float)
STRATS = [
    ("annual",  0.5,   "blue",   "Annual rebalance (~0.5x/yr)"),
    ("monthly", 6.0,   "green",  "Monthly rebalance (~6x/yr)"),
    ("weekly",  50.0,  "accent", "Weekly rebalance (~50x/yr)"),
    ("daily",   252.0, "red",    "Daily rebalance (~252x/yr)"),
]

LANG_STRINGS = {
    "en": {
        "title":    "Costs eat alpha: net return vs round-trip transaction cost",
        "subtitle": "Each strategy starts at 4% gross alpha. Net = gross - turnover x cost. Daily traders lose all alpha at 30 bps; weekly cross zero before 100 bps.",
        "xlabel":   "Round-trip transaction cost (bps)",
        "ylabel":   "Net annualised return",
        "footer":   "Realistic April-2026 costs: SPY/mega-caps ~3 bps, S&P large-caps ~10 bps, Russell 2000 small-caps ~50 bps. The high-turnover lines cross zero inside the realistic cost range.",
        "labels":   ["Annual (tau=0.5)", "Monthly (tau=6)", "Weekly (tau=50)", "Daily (tau=252)"],
        "zero":     "Zero alpha",
        "gross":    "Gross alpha = 4%",
    },
    "hk": {
        "title":    "成本吞噬阿爾法:每筆交易來回成本與淨回報",
        "subtitle": "每個策略起點均為 4% 毛阿爾法。淨回報 = 毛阿爾法 - 換手率 x 成本。每日交易者在 30 bps 已耗盡阿爾法;每週交易者在 100 bps 前跌穿零線。",
        "xlabel":   "每筆交易來回成本(bps)",
        "ylabel":   "年化淨回報",
        "footer":   "2026 年 4 月實際成本:SPY 等大型 ETF ~3 bps,標普大型股 ~10 bps,Russell 2000 小型股 ~50 bps。高換手線在現實成本範圍內已跌穿零。",
        "labels":   ["每年(tau=0.5)", "每月(tau=6)", "每週(tau=50)", "每日(tau=252)"],
        "zero":     "零阿爾法",
        "gross":    "毛阿爾法 = 4%",
    },
    "tw": {
        "title":    "成本吞噬 alpha:每筆交易來回成本與淨報酬",
        "subtitle": "每個策略起點均為 4% 毛 alpha。淨報酬 = 毛 alpha - 週轉率 x 成本。每日交易者在 30 bps 已耗盡 alpha;每週交易者在 100 bps 前跌破零線。",
        "xlabel":   "每筆交易來回成本(bps)",
        "ylabel":   "年化淨報酬",
        "footer":   "2026 年 4 月實際成本:SPY 等大型 ETF ~3 bps,標普大型股 ~10 bps,Russell 2000 小型股 ~50 bps。高週轉線在現實成本範圍內即跌破零。",
        "labels":   ["每年(tau=0.5)", "每月(tau=6)", "每週(tau=50)", "每日(tau=252)"],
        "zero":     "零 alpha",
        "gross":    "毛 alpha = 4%",
    },
    "cn": {
        "title":    "成本吞噬 alpha:单笔来回成本与净回报",
        "subtitle": "每个策略起点均为 4% 毛 alpha。净回报 = 毛 alpha - 换手率 x 成本。每日交易者在 30 bps 已耗尽 alpha;每周交易者在 100 bps 前跌破零线。",
        "xlabel":   "单笔来回成本(bps)",
        "ylabel":   "年化净回报",
        "footer":   "2026 年 4 月实际成本:SPY 等大型 ETF ~3 bps,标普大盘股 ~10 bps,罗素 2000 小盘股 ~50 bps。高换手线在现实成本范围内已跌破零。",
        "labels":   ["每年(tau=0.5)", "每月(tau=6)", "每周(tau=50)", "每日(tau=252)"],
        "zero":     "零 alpha",
        "gross":    "毛 alpha = 4%",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=160)
    style_axes(ax, p)

    color_map = {
        "blue":   p["blue"],
        "green":  p["green"],
        "accent": p["accent"],
        "red":    p["red"],
    }

    x = COSTS_BPS
    for (key, tau, ckey, _label), label in zip(STRATS, s["labels"]):
        net = GROSS - tau * (x / 10000.0)
        ax.plot(x, net * 100.0, color=color_map[ckey], linewidth=2.6,
                marker="o", markersize=5, label=label)
        # endpoint annotation (clipped to chart range so text stays visible)
        last = net[-1] * 100.0
        text_y = max(min(last, 5.5), -78.0)
        if last < -80:
            txt = f"{last:+.0f}%"
        else:
            txt = f"{last:+.1f}%"
        ax.text(x[-1] + 1.5, text_y, txt,
                color=color_map[ckey], fontsize=9, fontweight="bold",
                va="center", ha="left")

    # zero alpha line
    ax.axhline(0, color=p["fg"], linewidth=0.9, linestyle="-", alpha=0.5)
    ax.text(x[-1] + 1.0, 0.4, s["zero"], fontsize=8.5,
            color=p["muted"], ha="left", va="bottom")

    # gross alpha annotation
    ax.text(x[0] + 0.5, GROSS * 100.0 + 0.4, s["gross"], fontsize=9,
            color=p["muted"], ha="left", va="bottom", style="italic")

    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_xticks(COSTS_BPS)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:+.0f}%"))
    ax.set_ylim(-80, 7)
    ax.set_xlim(-3, 115)
    ax.legend(loc="lower left", fontsize=9.5, frameon=False)

    fig.suptitle(s["title"], fontsize=13.5, fontweight="bold", y=0.995, x=0.06, ha="left")
    fig.text(0.06, 0.945, s["subtitle"], fontsize=10, color=p["muted"])
    fig.text(0.06, 0.015, s["footer"], fontsize=9, color=p["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
