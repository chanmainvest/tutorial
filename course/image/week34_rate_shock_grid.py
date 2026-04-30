"""Week 34, §2.2 — Estimated price impact of a parallel +100bps shock by asset class.

Pure constants chart: each asset class is plotted with its standard
duration-implied response to a +100bps shock at the long end. Bonds,
equity styles, REITs in red; gold and the dollar (which respond
through different channels) in muted colours.

Run:
    uv run python course/image/week34_rate_shock_grid.py
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
BASE = "week34_rate_shock_grid"

# Asset class, response (% price change for +100bps), category
ROWS = [
    ("5Y_UST",    -4.5, "bond"),
    ("10Y_UST",   -8.0, "bond"),
    ("30Y_UST",  -16.0, "bond"),
    ("VALUE",     -3.0, "equity"),
    ("GROWTH",   -12.0, "equity"),
    ("REITS",    -10.0, "rrei"),
    ("GOLD",      -2.0, "alt"),
    ("USD",       +2.0, "alt"),
]

LANG_STRINGS = {
    "en": {
        "title":    "Estimated price impact of a parallel +100bps rate shock",
        "subtitle": "Constant-duration estimates at mid-2026 yields. Bonds and growth equity share the same duration ladder.",
        "xlabel":   "Asset class",
        "ylabel":   "Estimated price change (%)",
        "labels": {
            "5Y_UST":  "5y UST",
            "10Y_UST": "10y UST",
            "30Y_UST": "30y UST",
            "VALUE":   "Value equity (VTV)",
            "GROWTH":  "Growth equity (QQQ)",
            "REITS":   "REITs (VNQ)",
            "GOLD":    "Gold (GLD)",
            "USD":     "USD (DXY)",
        },
        "ann_dur":  "Bonds: linear in duration",
        "ann_eq":   "Stocks ride the same ladder",
        "ann_alt":  "Different driver:\ngold via real rates,\nUSD via rate spread",
        "footer":   "Sign convention: +100bps = rates rise. Gold and USD are mid-range estimates; both can move in either direction depending on whether the shock is real or nominal.",
    },
    "hk": {
        "title":    "+100bps 平行加息對各資產類別的估算價格衝擊",
        "subtitle": "以 2026 年中孳息率水平做基準,各類資產的久期估算。債券與成長股共用同一條久期梯。",
        "xlabel":   "資產類別",
        "ylabel":   "估算價格變動(%)",
        "labels": {
            "5Y_UST":  "5 年國債",
            "10Y_UST": "10 年國債",
            "30Y_UST": "30 年國債",
            "VALUE":   "價值股(VTV)",
            "GROWTH":  "成長股(QQQ)",
            "REITS":   "房託(VNQ)",
            "GOLD":    "黃金(GLD)",
            "USD":     "美元(DXY)",
        },
        "ann_dur":  "債券:跌幅與久期成正比",
        "ann_eq":   "股票坐在同一條梯上",
        "ann_alt":  "不同驅動因子:\n黃金看實質利率,\n美元看利差",
        "footer":   "符號慣例:+100bps 即利率上升。黃金與美元為中段估值;若衝擊源於實質或名義利率,可能朝任一方向波動。",
    },
    "tw": {
        "title":    "+100bps 平行升息對各資產類別的估算價格衝擊",
        "subtitle": "以 2026 年中殖利率水平做基準,各類資產的存續期估算。公債與成長股共用同一條存續期階梯。",
        "xlabel":   "資產類別",
        "ylabel":   "估算價格變動(%)",
        "labels": {
            "5Y_UST":  "5 年公債",
            "10Y_UST": "10 年公債",
            "30Y_UST": "30 年公債",
            "VALUE":   "價值股(VTV)",
            "GROWTH":  "成長股(QQQ)",
            "REITS":   "REITs(VNQ)",
            "GOLD":    "黃金(GLD)",
            "USD":     "美元(DXY)",
        },
        "ann_dur":  "公債:跌幅與存續期成正比",
        "ann_eq":   "股票位於同一條階梯",
        "ann_alt":  "不同驅動因子:\n黃金看實質利率,\n美元看利差",
        "footer":   "符號慣例:+100bps 即利率上升。黃金與美元為中段估值;若衝擊源於實質或名義利率,可能朝任一方向移動。",
    },
    "cn": {
        "title":    "+100bps 平行加息对各资产类别的估算价格冲击",
        "subtitle": "以 2026 年中收益率水平为基准,各类资产的久期估算。债券与成长股共享同一条久期阶梯。",
        "xlabel":   "资产类别",
        "ylabel":   "估算价格变动(%)",
        "labels": {
            "5Y_UST":  "5 年国债",
            "10Y_UST": "10 年国债",
            "30Y_UST": "30 年国债",
            "VALUE":   "价值股(VTV)",
            "GROWTH":  "成长股(QQQ)",
            "REITS":   "REITs(VNQ)",
            "GOLD":    "黄金(GLD)",
            "USD":     "美元(DXY)",
        },
        "ann_dur":  "债券:跌幅与久期成正比",
        "ann_eq":   "股票位于同一阶梯",
        "ann_alt":  "不同驱动因子:\n黄金看实际利率,\n美元看利差",
        "footer":   "符号约定:+100bps 即利率上升。黄金与美元为中段估值;若冲击源于实际或名义利率,可能朝任一方向波动。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.4))
    style_axes(ax, p)

    keys = [k for k, _, _ in ROWS]
    vals = [v for _, v, _ in ROWS]
    cats = [c for _, _, c in ROWS]
    labels = [s["labels"][k] for k in keys]

    color_map = {
        "bond":   p["blue"],
        "equity": p["red"],
        "rrei":   p["orange"],
        "alt":    p["accent"],
    }
    colors = [color_map[c] for c in cats]

    x = np.arange(len(vals))
    bars = ax.bar(x, vals, color=colors, edgecolor=p["fg"], linewidth=0.7, width=0.7)

    for i, b in enumerate(bars):
        v = vals[i]
        ax.text(b.get_x() + b.get_width() / 2,
                v + (0.6 if v >= 0 else -0.6),
                f"{v:+.1f}%",
                ha="center",
                va="bottom" if v >= 0 else "top",
                fontsize=10, fontweight="bold",
                color=p["fg"])

    ax.axhline(0, color=p["fg"], linewidth=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, ha="right", fontsize=9.5)

    ax.set_ylim(-19, 5.5)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Annotation brackets
    ax.text(1, -18.0, s["ann_dur"], color=p["blue"],
            fontsize=9, ha="center", fontweight="bold")
    ax.text(3.5, -14.0, s["ann_eq"], color=p["red"],
            fontsize=9, ha="center", fontweight="bold")
    ax.text(6.5, -7.5, s["ann_alt"], color=p["accent"],
            fontsize=9, ha="center", fontweight="bold")

    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.5,
             color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
