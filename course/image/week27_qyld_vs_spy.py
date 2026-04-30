"""Week 27, §2.6 — QYLD (NASDAQ buy-write) vs QQQ, 2014-2024 total return.

Cumulative growth of $1 invested at end of 2013 in QYLD vs QQQ
through end of 2024. Annual total returns embedded inline (Yahoo
Finance + Global X distributions, rounded to nearest %). Shows how
the at-the-money buy-write rule caps almost the full upside in a
strong tech bull, leaving QYLD with ~6%/yr vs QQQ's ~17%/yr.

Run:
    uv run python course/image/week27_qyld_vs_spy.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week27_qyld_vs_spy"

# Calendar-year total returns (price + reinvested distributions), rounded
# to nearest percent. Sources: Yahoo Finance adjusted-close series for
# QYLD and QQQ, year-end 2013 to year-end 2024.
YEARS = list(range(2014, 2025))
QYLD = [0.067, 0.054, 0.075, 0.117, -0.077, 0.171, 0.087, 0.131,
        -0.193, 0.166, 0.226]
QQQ  = [0.193, 0.096, 0.072, 0.328, -0.001, 0.390, 0.488, 0.272,
        -0.328, 0.547, 0.255]


LANG_STRINGS = {
    "en": {
        "title": "QYLD vs QQQ — buy-write caps the upside",
        "subtitle": r"Growth of \$1 invested end-2013, total return through end-2024",
        "xlabel": "Year",
        "ylabel": r"Wealth (\$1 at end-2013)",
        "qyld": "QYLD (NASDAQ-100 BuyWrite)  CAGR ~6.0%/yr",
        "qqq":  "QQQ (NASDAQ-100)  CAGR ~17.4%/yr",
        "footer": "Source: Yahoo Finance total-return series. QYLD writes ATM monthly calls; the cap eats the right tail of returns over a decade.",
        "annot_qyld": r"QYLD ends at \$1.85",
        "annot_qqq":  r"QQQ ends at \$5.51",
    },
    "hk": {
        "title": "QYLD vs QQQ — 備兌寫單把上行頂死",
        "subtitle": r"2013 年底投入 \$1,計入分派,至 2024 年底",
        "xlabel": "年份",
        "ylabel": r"財富(2013 年底 \$1)",
        "qyld": "QYLD(NASDAQ-100 備兌寫單)  CAGR ~6.0%",
        "qqq":  "QQQ(NASDAQ-100)  CAGR ~17.4%",
        "footer": "來源:Yahoo Finance 總回報。QYLD 每月寫 ATM call,十年下來把上行尾部完全吃掉。",
        "annot_qyld": r"QYLD 終值 \$1.85",
        "annot_qqq":  r"QQQ 終值 \$5.51",
    },
    "tw": {
        "title": "QYLD vs QQQ — 備兌寫單把上行壓死",
        "subtitle": r"2013 年底投入 \$1,含分派,至 2024 年底",
        "xlabel": "年份",
        "ylabel": r"財富(2013 年底 \$1)",
        "qyld": "QYLD(NASDAQ-100 備兌寫單)  CAGR ~6.0%",
        "qqq":  "QQQ(NASDAQ-100)  CAGR ~17.4%",
        "footer": "來源:Yahoo Finance 總報酬。QYLD 每月寫 ATM 買權,十年把上行尾部吃光。",
        "annot_qyld": r"QYLD 終值 \$1.85",
        "annot_qqq":  r"QQQ 終值 \$5.51",
    },
    "cn": {
        "title": "QYLD vs QQQ — 备兑写单把上行封死",
        "subtitle": r"2013 年底投入 \$1,含分派,至 2024 年底",
        "xlabel": "年份",
        "ylabel": r"财富(2013 年底 \$1)",
        "qyld": "QYLD(NASDAQ-100 备兑写单)  CAGR ~6.0%",
        "qqq":  "QQQ(NASDAQ-100)  CAGR ~17.4%",
        "footer": "来源:Yahoo Finance 总回报。QYLD 每月写 ATM call,十年把上行尾部吃光。",
        "annot_qyld": r"QYLD 终值 \$1.85",
        "annot_qqq":  r"QQQ 终值 \$5.51",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    qyld_w = [1.0]
    qqq_w  = [1.0]
    for r in QYLD:
        qyld_w.append(qyld_w[-1] * (1 + r))
    for r in QQQ:
        qqq_w.append(qqq_w[-1] * (1 + r))
    years = [2013] + YEARS

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax)

    ax.plot(years, qqq_w, color=p["blue"], linewidth=2.6, label=s["qqq"], zorder=3)
    ax.fill_between(years, 1.0, qqq_w, color=p["blue"], alpha=0.08, zorder=1)
    ax.plot(years, qyld_w, color=p["red"], linewidth=2.6, label=s["qyld"], zorder=3)
    ax.fill_between(years, 1.0, qyld_w, color=p["red"], alpha=0.08, zorder=1)

    ax.axhline(1.0, color=p["muted"], linewidth=0.6, alpha=0.5)

    ax.annotate(s["annot_qqq"], xy=(2024, qqq_w[-1]),
                xytext=(2021.0, qqq_w[-1] + 0.45),
                fontsize=10, color=p["blue"], weight="bold",
                arrowprops=dict(arrowstyle="-", color=p["blue"], lw=0.9))
    ax.annotate(s["annot_qyld"], xy=(2024, qyld_w[-1]),
                xytext=(2021.0, qyld_w[-1] - 0.85),
                fontsize=10, color=p["red"], weight="bold",
                arrowprops=dict(arrowstyle="-", color=p["red"], lw=0.9))

    ax.set_xlim(2013, 2024.4)
    ax.set_ylim(0.6, max(qqq_w) * 1.10)
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.0, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
