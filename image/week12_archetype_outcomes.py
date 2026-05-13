"""Week 12, §2.6 — Cumulative real wealth of the five archetype portfolios, 1928-2024.

US = SP500. Ex-US = SP500 with a 1.0% annual drag (proxy). Bonds = TBond10Y.
TIPS (proxy) = TBond10Y. Gold = embedded annual price-derived returns
(constant pre-1971 under gold-standard / Bretton Woods, then actual). Cash =
TBill3M. All series deflated by CPI to real terms; portfolios rebalanced
annually.

Run:
    uv run python course/image/week12_archetype_outcomes.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week12_archetype_outcomes"

# (US, exUS, bonds, TIPS, gold, cash) - same as week12_archetype_allocations.
ARCHETYPES = [
    ("early",   [0.65, 0.20, 0.05, 0.00, 0.05, 0.05]),
    ("mid",     [0.50, 0.15, 0.20, 0.05, 0.05, 0.05]),
    ("late",    [0.35, 0.10, 0.30, 0.10, 0.10, 0.05]),
    ("retired", [0.25, 0.05, 0.35, 0.15, 0.10, 0.10]),
    ("fire",    [0.40, 0.10, 0.10, 0.05, 0.20, 0.15]),
]

# Annual gold nominal returns, 1928..2024. Pre-1968 mostly zero under
# the gold standard / Bretton Woods, with the 1933-34 US revaluation
# step. Post-1971 derived from year-end London PM fixings.
GOLD_NOMINAL = [
    0.0000, 0.0000, 0.0000, 0.0000, 0.0000,           # 1928-1932
    0.2738, 0.3293,                                   # 1933 (devaluation), 1934 (revaluation)
    0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,   # 1935-1940
    0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,   # 1941-1946
    0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,   # 1947-1952
    0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,   # 1953-1958
    0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,   # 1959-1964
    0.0000, 0.0000, 0.0000,                           # 1965-1967
    0.1971, -0.1599, 0.0682, 0.1569, 0.4920,          # 1968-1972
    0.7297, 0.6614, -0.2480, -0.0410, 0.2264,         # 1973-1977
    0.3700, 1.3186, 0.1255, -0.3260, 0.1494,          # 1978-1982
    -0.1650, -0.1900, 0.0583, 0.1955, 0.2446,         # 1983-1987
    -0.1567, -0.0226, -0.0369, -0.0849, -0.0580,      # 1988-1992
    0.1735, -0.0209, 0.0118, -0.0451, -0.2147,        # 1993-1997
    -0.0083, 0.0085, -0.0606, 0.0233, 0.2480,         # 1998-2002
    0.1950, 0.0536, 0.1836, 0.2295, 0.3110,           # 2003-2007
    0.0341, 0.2688, 0.2951, 0.1077, 0.0568,           # 2008-2012
    -0.2780, -0.0019, -0.1142, 0.0803, 0.1299,        # 2013-2017
    -0.0115, 0.1836, 0.2443, -0.0358, 0.0023,         # 2018-2022
    0.1305, 0.2806,                                    # 2023-2024
]


LANG_STRINGS = {
    "en": {
        "title":    "Cumulative real wealth of the five archetype portfolios, $1 in 1928",
        "subtitle": "Annual rebalanced. Real terms after CPI, log scale. 1928-2024 Damodaran + gold series.",
        "xlabel":   "Year",
        "ylabel":   "Real wealth ($, log scale)",
        "early":    "Early career",
        "mid":      "Mid career",
        "late":     "Late career",
        "retired":  "Retired",
        "fire":     "FIRE / barbell",
        "ann":      "Geometric annualised real returns",
    },
    "hk": {
        "title":    "五個原型組合的累計實質財富,1928 年投入 1 美元",
        "subtitle": "每年再平衡;CPI 調整後實質、對數軸。1928-2024 Damodaran 加黃金序列。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(美元,對數軸)",
        "early":    "職涯早期",
        "mid":      "職涯中期",
        "late":     "職涯後期",
        "retired":  "退休後",
        "fire":     "FIRE / 槓鈴",
        "ann":      "幾何年化實質回報",
    },
    "tw": {
        "title":    "五個原型組合的累計實質財富,1928 年投入 1 美元",
        "subtitle": "每年再平衡;CPI 調整後實質、對數軸。1928-2024 Damodaran 加黃金序列。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(美元,對數軸)",
        "early":    "職涯早期",
        "mid":      "職涯中期",
        "late":     "職涯後期",
        "retired":  "退休後",
        "fire":     "FIRE / 槓鈴",
        "ann":      "幾何年化實質報酬",
    },
    "cn": {
        "title":    "五个原型组合的累计实质财富,1928 年投入 1 美元",
        "subtitle": "每年再平衡;CPI 调整后实质、对数轴。1928-2024 Damodaran 加黄金序列。",
        "xlabel":   "年份",
        "ylabel":   "实质财富(美元,对数轴)",
        "early":    "职涯早期",
        "mid":      "职涯中期",
        "late":     "职涯后期",
        "retired":  "退休后",
        "fire":     "FIRE / 杠铃",
        "ann":      "几何年化实质回报",
    },
}


def _real_returns():
    df = damodaran_annual_returns()
    cpi  = df["CPI"]
    sp   = df["SP500"]
    bd   = df["TBond10Y"]
    bill = df["TBill3M"]
    gold_nom = pd.Series(GOLD_NOMINAL, index=df.index, name="Gold")
    # Real returns by sleeve.
    r_us    = (1 + sp)         / (1 + cpi) - 1
    r_exus  = (1 + sp - 0.01)  / (1 + cpi) - 1   # 1% annual drag proxy
    r_bd    = (1 + bd)         / (1 + cpi) - 1
    r_tips  = (1 + bd)         / (1 + cpi) - 1   # proxy = nominal bonds
    r_gold  = (1 + gold_nom)   / (1 + cpi) - 1
    r_cash  = (1 + bill)       / (1 + cpi) - 1
    return df.index, np.column_stack([r_us, r_exus, r_bd, r_tips, r_gold, r_cash])


def build_fig(s):
    p = PALETTE_LIGHT
    yrs, R = _real_returns()
    archetype_colors = {
        "early":   p["red"],
        "mid":     p["accent"],
        "fire":    p["purple"],
        "late":    p["teal"],
        "retired": p["blue"],
    }
    plot_order = ["early", "mid", "fire", "late", "retired"]
    arch_lookup = dict(ARCHETYPES)

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    style_axes(ax, p)

    summaries = []
    for key in plot_order:
        w = np.array(arch_lookup[key])
        port = R @ w
        cum = (1 + port).cumprod()
        ax.plot(yrs, cum, color=archetype_colors[key], linewidth=2.0,
                label=s[key])
        n = len(port)
        ann = cum[-1] ** (1 / n) - 1
        summaries.append((key, ann, cum[-1]))
        # End label
        ax.text(yrs[-1] + 0.7, cum[-1], f"${cum[-1]:,.0f}",
                color=archetype_colors[key], fontsize=9, va="center",
                fontweight="bold")

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Annualised return summary footer
    parts = [f"{s[k]} {a:.1%}" for k, a, _ in summaries]
    ax.text(0, -0.16, s["ann"] + ":  " + "  -  ".join(parts),
            transform=ax.transAxes, fontsize=9, color=p["muted"])

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout(rect=[0, 0.02, 0.97, 1])
    return fig


if __name__ == "__main__":
    assert len(GOLD_NOMINAL) == 97, f"expected 97 gold years, got {len(GOLD_NOMINAL)}"
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
