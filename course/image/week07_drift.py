"""Week 7, §2.1 — 60/40 drift vs annual rebalance over 2010-2019.

Stacked-area weight composition for two policies on a $100,000 starting
60/40 portfolio: top panel never rebalances (drift to ~75/25 by 2019),
bottom panel rebalances back to 60/40 every January.

Annual returns from Damodaran (SP500 total return, TBond10Y total return).

Run:
    uv run python course/image/week07_drift.py
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
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week07_drift"

START_YEAR = 2010
END_YEAR = 2019
START_VAL = 100_000.0
TARGET_STOCK = 0.60

LANG_STRINGS = {
    "en": {
        "title":      "How a 60/40 portfolio drifts in a single decade",
        "subtitle":   "$100,000 invested 60/40 on Jan 1, 2010. Top: never rebalance. Bottom: rebalance every January.",
        "ylabel":     "Portfolio value ($)",
        "xlabel":     "Year",
        "stocks":     "Stocks (S&P 500)",
        "bonds":      "10-year Treasury",
        "panel_no":   "Never rebalance — ends at {sp:.0f}/{bp:.0f}",
        "panel_yes":  "Annual rebalance — ends at {sp:.0f}/{bp:.0f}",
        "end_label":  "End: ${v:,.0f}",
    },
    "hk": {
        "title":      "60/40 組合在一個十年的漂移",
        "subtitle":   "2010 年 1 月 1 日投入 10 萬美元、60/40 配置。上:從不再平衡。下:每年一月再平衡。",
        "ylabel":     "組合市值(美元)",
        "xlabel":     "年份",
        "stocks":     "股票(標普 500)",
        "bonds":      "十年期國債",
        "panel_no":   "從不再平衡 — 末段比例 {sp:.0f}/{bp:.0f}",
        "panel_yes":  "每年再平衡 — 末段比例 {sp:.0f}/{bp:.0f}",
        "end_label":  "末值:${v:,.0f}",
    },
    "tw": {
        "title":      "60/40 組合在一個十年的漂移",
        "subtitle":   "2010 年 1 月 1 日投入 10 萬美元、60/40 配置。上:從不再平衡。下:每年一月再平衡。",
        "ylabel":     "組合市值(美元)",
        "xlabel":     "年份",
        "stocks":     "股票(標普 500)",
        "bonds":      "十年期公債",
        "panel_no":   "從不再平衡 — 末段比例 {sp:.0f}/{bp:.0f}",
        "panel_yes":  "每年再平衡 — 末段比例 {sp:.0f}/{bp:.0f}",
        "end_label":  "末值:${v:,.0f}",
    },
    "cn": {
        "title":      "60/40 组合在一个十年的漂移",
        "subtitle":   "2010 年 1 月 1 日投入 10 万美元、60/40 配置。上:从不再平衡。下:每年一月再平衡。",
        "ylabel":     "组合市值(美元)",
        "xlabel":     "年份",
        "stocks":     "股票(标普 500)",
        "bonds":      "十年期国债",
        "panel_no":   "从不再平衡 — 末段比例 {sp:.0f}/{bp:.0f}",
        "panel_yes":  "每年再平衡 — 末段比例 {sp:.0f}/{bp:.0f}",
        "end_label":  "末值:${v:,.0f}",
    },
}


def _simulate():
    df = damodaran_annual_returns()
    yrs = [y for y in df.index if START_YEAR <= y <= END_YEAR]
    sp = df.loc[yrs, "SP500"].to_numpy()
    bd = df.loc[yrs, "TBond10Y"].to_numpy()

    # x-axis: end of year 2009 (year 0) through end of 2019 (year 10).
    x = np.array([START_YEAR - 1] + yrs)

    # No rebalance.
    s_no = [START_VAL * TARGET_STOCK]
    b_no = [START_VAL * (1 - TARGET_STOCK)]
    for i, _ in enumerate(yrs):
        s_no.append(s_no[-1] * (1 + sp[i]))
        b_no.append(b_no[-1] * (1 + bd[i]))
    s_no = np.array(s_no)
    b_no = np.array(b_no)

    # Annual rebalance back to TARGET_STOCK each Jan.
    s_re = [START_VAL * TARGET_STOCK]
    b_re = [START_VAL * (1 - TARGET_STOCK)]
    for i, _ in enumerate(yrs):
        s_new = s_re[-1] * (1 + sp[i])
        b_new = b_re[-1] * (1 + bd[i])
        total = s_new + b_new
        s_re.append(total * TARGET_STOCK)
        b_re.append(total * (1 - TARGET_STOCK))
    s_re = np.array(s_re)
    b_re = np.array(b_re)

    return x, s_no, b_no, s_re, b_re


def _plot_panel(ax, x, s_arr, b_arr, s, label_fmt_key, lang):
    p = PALETTE_LIGHT
    style_axes(ax, p)
    total = s_arr + b_arr
    ax.fill_between(x, 0, b_arr, color=p["blue"], alpha=0.85, label=s["bonds"])
    ax.fill_between(x, b_arr, total, color=p["red"], alpha=0.85, label=s["stocks"])
    # Subtle target line at 60% of total at each x for reference.
    ax.plot(x, total * (1 - TARGET_STOCK), color=p["fg"], linewidth=0.9,
            linestyle=":", alpha=0.7)

    end_total = total[-1]
    end_sp = s_arr[-1] / end_total * 100.0
    end_bp = b_arr[-1] / end_total * 100.0
    ax.set_title(s[label_fmt_key].format(sp=end_sp, bp=end_bp),
                 fontsize=11, color=p["fg"], loc="left", pad=8)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, max(end_total, total.max()) * 1.05)

    # End-value label
    ax.text(x[-1], end_total, "  " + s["end_label"].format(v=end_total),
            color=p["fg"], fontsize=9, va="center", fontweight="bold")


def build_fig(s):
    p = PALETTE_LIGHT
    x, s_no, b_no, s_re, b_re = _simulate()

    fig, axes = plt.subplots(2, 1, figsize=(10, 7.0), sharex=True)
    fig.set_facecolor(p["bg"])

    _plot_panel(axes[0], x, s_no, b_no, s, "panel_no", "")
    _plot_panel(axes[1], x, s_re, b_re, s, "panel_yes", "")

    axes[1].set_xlabel(s["xlabel"], fontsize=10)
    axes[0].legend(loc="upper left", frameon=False, fontsize=10)

    fig.suptitle(s["title"], fontsize=13, fontweight="bold", x=0.05, ha="left", y=0.985)
    fig.text(0.05, 0.95, s["subtitle"], fontsize=10, color=p["muted"])
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
