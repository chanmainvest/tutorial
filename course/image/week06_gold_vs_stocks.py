"""Week 6, §2.3 — Cumulative real wealth: gold vs S&P 500 vs 60/40.

$1 invested in 1971, real terms (CPI-adjusted), log scale, through
2024. Three lines plus shaded windows where gold dominated equities.

Equity / bond / CPI from Damodaran annual dataset.
Gold from FRED GOLDAMGBD228NLBM annual averages, with offline
fallback (annual averages embedded in week06_gold_real.py).

Run:
    uv run python course/image/week06_gold_vs_stocks.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns, fred_series  # noqa: E402
from week06_gold_real import GOLD_FALLBACK  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week06_gold_vs_stocks"

LANG_STRINGS = {
    "en": {
        "title":    "Real wealth from $1 invested in 1971: gold vs S&P 500 vs 60/40",
        "subtitle": "Real (CPI-adjusted), log scale. Gold dominates in three windows; equities dominate the other three decades.",
        "xlabel":   "Year",
        "ylabel":   "Real wealth ($, log scale)",
        "stocks":   "100% S&P 500",
        "gold":     "100% gold",
        "sixty":    "60/40 (annual rebalance)",
        "win_a":    "Gold > stocks\n1971-1980",
        "win_b":    "Gold > stocks\n2001-2011",
        "win_c":    "Gold > stocks\n2020-2024",
        "ann":      "Geometric ann. real return: stocks {s:.1%}  ·  60/40 {m:.1%}  ·  gold {g:.1%}",
    },
    "hk": {
        "title":    "1971 年投入 1 美元的累計實質財富:黃金 vs 標普 500 vs 60/40",
        "subtitle": "CPI 調整後實質、對數軸。黃金在三段窗口跑贏;股票在另外三十年大幅領先。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(美元,對數軸)",
        "stocks":   "100% 標普 500",
        "gold":     "100% 黃金",
        "sixty":    "60/40(每年再平衡)",
        "win_a":    "黃金跑贏\n1971-1980",
        "win_b":    "黃金跑贏\n2001-2011",
        "win_c":    "黃金跑贏\n2020-2024",
        "ann":      "幾何年化實質回報:股票 {s:.1%}  ·  60/40 {m:.1%}  ·  黃金 {g:.1%}",
    },
    "tw": {
        "title":    "1971 年投入 1 美元的累計實質財富:黃金 vs 標普 500 vs 60/40",
        "subtitle": "CPI 調整後實質、對數軸。黃金在三段窗口跑贏;股票在另外三十年領先。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(美元,對數軸)",
        "stocks":   "100% 標普 500",
        "gold":     "100% 黃金",
        "sixty":    "60/40(每年再平衡)",
        "win_a":    "黃金勝出\n1971-1980",
        "win_b":    "黃金勝出\n2001-2011",
        "win_c":    "黃金勝出\n2020-2024",
        "ann":      "幾何年化實質報酬:股票 {s:.1%}  ·  60/40 {m:.1%}  ·  黃金 {g:.1%}",
    },
    "cn": {
        "title":    "1971 年投入 1 美元的累计实质财富:黄金 vs 标普 500 vs 60/40",
        "subtitle": "CPI 调整后实质、对数轴。黄金在三段窗口跑赢;股票在另外三十年大幅领先。",
        "xlabel":   "年份",
        "ylabel":   "实质财富(美元,对数轴)",
        "stocks":   "100% 标普 500",
        "gold":     "100% 黄金",
        "sixty":    "60/40(每年再平衡)",
        "win_a":    "黄金跑赢\n1971-1980",
        "win_b":    "黄金跑赢\n2001-2011",
        "win_c":    "黄金跑赢\n2020-2024",
        "ann":      "几何年化实质回报:股票 {s:.1%}  ·  60/40 {m:.1%}  ·  黄金 {g:.1%}",
    },
}


def _gold_annual() -> pd.Series:
    """Annual-average USD/oz gold price, 1971-2024."""
    try:
        df = fred_series("GOLDAMGBD228NLBM", start="1970-01-01")
        s = df.iloc[:, 0].astype(float).dropna()
        s.index = pd.to_datetime(s.index)
        ann = s.resample("YE").mean()
        ann.index = ann.index.year
        ann = ann.loc[1971:2024]
        if len(ann) >= 50:
            return ann
    except Exception:
        pass
    yrs = list(range(1971, 2025))
    return pd.Series([float(GOLD_FALLBACK[y]) for y in yrs], index=yrs, dtype=float)


def _series():
    dam = damodaran_annual_returns()
    dam = dam.loc[1971:2024]
    sp = dam["SP500"]
    bd = dam["TBond10Y"]
    cpi = dam["CPI"]

    rs = (1 + sp) / (1 + cpi) - 1
    rb = (1 + bd) / (1 + cpi) - 1
    rm = 0.6 * rs + 0.4 * rb

    gold = _gold_annual()
    nom_g = gold.pct_change().fillna(0.0)
    real_g = (1 + nom_g) / (1 + cpi.reindex(gold.index)) - 1
    real_g.iloc[0] = 0.0

    cs = (1 + rs).cumprod()
    cm = (1 + rm).cumprod()
    cg = (1 + real_g).cumprod()
    return cs, cm, cg, rs, rb, rm, real_g


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    cs, cm, cg, rs, rb, rm, rg = _series()
    p = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(10.4, 5.8))
    style_axes(ax, p)

    for x0, x1, lbl in [
        (1971, 1980, s["win_a"]),
        (2001, 2011, s["win_b"]),
        (2020, 2024, s["win_c"]),
    ]:
        ax.axvspan(x0, x1, color=p["accent"], alpha=0.10, zorder=0)
        ax.text((x0 + x1) / 2, 0.62, lbl, ha="center", fontsize=8.4,
                color=p["muted"], transform=ax.get_xaxis_transform())

    ax.plot(cs.index, cs.values, color=p["red"], linewidth=2.0, label=s["stocks"])
    ax.plot(cg.index, cg.values, color=p["accent"], linewidth=2.0, label=s["gold"])
    ax.plot(cm.index, cm.values, color=p["blue"], linewidth=2.2, label=s["sixty"])

    ax.set_yscale("log")
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    last_y = int(cs.index.max())
    n = len(rs)
    ann_s = cs.iloc[-1] ** (1 / n) - 1
    ann_m = cm.iloc[-1] ** (1 / n) - 1
    ann_g = cg.iloc[-1] ** (1 / n) - 1

    for cum, color in [(cs, p["red"]), (cg, p["accent"]), (cm, p["blue"])]:
        ax.text(last_y + 0.5, cum.iloc[-1], f"\\${cum.iloc[-1]:,.1f}",
                color=color, fontsize=9, va="center", fontweight="bold")

    ax.text(0, -0.16, s["ann"].format(s=ann_s, m=ann_m, g=ann_g),
            transform=ax.transAxes, fontsize=9, color=p["muted"])

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
