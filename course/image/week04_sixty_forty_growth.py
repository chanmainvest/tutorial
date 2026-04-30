"""Week 4, §2.2 — Cumulative real wealth: stocks, bonds, 60/40.

Annual rebalanced 60/40 from 1928 onward, real terms (after CPI),
log scale. Damodaran annual dataset.

Run:
    uv run python course/image/week04_sixty_forty_growth.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week04_sixty_forty_growth"

LANG_STRINGS = {
    "en": {
        "title":    "Cumulative real wealth, $1 invested in 1928",
        "subtitle": "Annual rebalanced 60/40 captures most of equity's compounding with materially smaller drawdowns. Real terms after CPI, log scale.",
        "xlabel":   "Year",
        "ylabel":   "Real wealth ($, log scale)",
        "stocks":   "100% S&P 500",
        "bonds":    "100% 10-year Treasury",
        "sixty":    "60/40 (annual rebalance)",
        "ann":      "Geometric ann. real return: stocks {s:.1%}  ·  60/40 {m:.1%}  ·  bonds {b:.1%}",
    },
    "hk": {
        "title":    "1928 年投入 1 美元的累計實質財富",
        "subtitle": "每年再平衡的 60/40 拿到大部分股票的複利,回撤明顯較小。CPI 調整後實質、對數軸。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(美元,對數軸)",
        "stocks":   "100% 標普 500",
        "bonds":    "100% 十年期國債",
        "sixty":    "60/40(每年再平衡)",
        "ann":      "幾何年化實質回報:股票 {s:.1%}  ·  60/40 {m:.1%}  ·  債券 {b:.1%}",
    },
    "tw": {
        "title":    "1928 年投入 1 美元的累計實質財富",
        "subtitle": "每年再平衡的 60/40 取得大部分股票的複利,回檔明顯較小。CPI 調整後實質、對數軸。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(美元,對數軸)",
        "stocks":   "100% 標普 500",
        "bonds":    "100% 十年期公債",
        "sixty":    "60/40(每年再平衡)",
        "ann":      "幾何年化實質報酬:股票 {s:.1%}  ·  60/40 {m:.1%}  ·  債券 {b:.1%}",
    },
    "cn": {
        "title":    "1928 年投入 1 美元的累计实质财富",
        "subtitle": "每年再平衡的 60/40 拿到大部分股票的复利,回撤明显较小。CPI 调整后实质、对数轴。",
        "xlabel":   "年份",
        "ylabel":   "实质财富(美元,对数轴)",
        "stocks":   "100% 标普 500",
        "bonds":    "100% 十年期国债",
        "sixty":    "60/40(每年再平衡)",
        "ann":      "几何年化实质回报:股票 {s:.1%}  ·  60/40 {m:.1%}  ·  债券 {b:.1%}",
    },
}


def _series():
    df = damodaran_annual_returns()
    sp = df["SP500"]
    bd = df["TBond10Y"]
    cpi = df["CPI"]
    rs = (1 + sp) / (1 + cpi) - 1   # real stock
    rb = (1 + bd) / (1 + cpi) - 1   # real bond
    # 60/40 rebalanced annually in real terms
    mix = 0.6 * rs + 0.4 * rb
    cum_s = (1 + rs).cumprod()
    cum_b = (1 + rb).cumprod()
    cum_m = (1 + mix).cumprod()
    return df.index, cum_s, cum_b, cum_m, rs, rb, mix


def build_fig(s):
    yrs, cs, cb, cm, rs, rb, rm = _series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10, 5.6))
    style_axes(ax, p)

    ax.plot(yrs, cs, color=p["red"], linewidth=2.2, label=s["stocks"])
    ax.plot(yrs, cm, color=p["accent"], linewidth=2.6, label=s["sixty"])
    ax.plot(yrs, cb, color=p["blue"], linewidth=2.2, label=s["bonds"])

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    n = len(rs)
    ann_s = cs.iloc[-1] ** (1 / n) - 1
    ann_b = cb.iloc[-1] ** (1 / n) - 1
    ann_m = cm.iloc[-1] ** (1 / n) - 1

    # End-value labels
    last_y = yrs[-1]
    for cum, color, txt in [(cs, p["red"], "stocks"),
                             (cm, p["accent"], "60/40"),
                             (cb, p["blue"], "bonds")]:
        ax.text(last_y + 0.6, cum.iloc[-1], f"${cum.iloc[-1]:,.0f}",
                color=color, fontsize=9, va="center", fontweight="bold")

    ax.text(0, -0.15, s["ann"].format(s=ann_s, m=ann_m, b=ann_b),
            transform=ax.transAxes, fontsize=9, color=p["muted"])

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
