"""Week 6, §2.4 — Gold vs S&P 500 vs 60/40 vs 60/25/15, regime by regime.

Six small multiples (5 regime panels + full-period summary). Each panel
starts every line at $1 at the start of that regime so you can see the
*shape* of returns inside the window. The fourth line is a 60/25/15
portfolio (60% S&P, 25% intermediate Treasuries, 15% gold) rebalanced
annually — the case for a small permanent gold sleeve.

Equity / bond / CPI from Damodaran annual dataset.
Gold from FRED GOLDAMGBD228NLBM annual averages, with offline fallback.

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

# Regimes: (start_year, end_year_inclusive, label_key)
REGIMES = [
    (1971, 1980, "r_70s"),
    (1981, 1999, "r_disinf"),
    (2000, 2011, "r_lostdec"),
    (2012, 2019, "r_disinf2"),
    (2020, 2024, "r_covid"),
    (1971, 2024, "r_full"),
]

LANG_STRINGS = {
    "en": {
        "title":    "Gold vs S&P 500 vs 60/40 vs 60/25/15 — regime by regime",
        "subtitle": "Each panel starts every line at $1 at the start of the regime. Real (CPI-adjusted) returns. The 60/25/15 sleeve adds 15% gold to a 60/25 stock/Treasury core.",
        "stocks":   "100% S&P 500",
        "gold":     "100% gold",
        "sixty":    "60/40",
        "blend":    "60/25/15 (with gold)",
        "r_70s":      "1971-1980 — Stagflation, end of Bretton Woods",
        "r_disinf":   "1981-1999 — Volcker disinflation, equity bull",
        "r_lostdec":  "2000-2011 — Dot-com bust + GFC",
        "r_disinf2":  "2012-2019 — Post-GFC disinflation",
        "r_covid":    "2020-2024 — COVID + reflation",
        "r_full":     "1971-2024 — Full period",
        "ann":      "Geom. ann. real return ({n}y): S&P {s:+.1%}  ·  60/40 {m:+.1%}  ·  60/25/15 {b:+.1%}  ·  gold {g:+.1%}",
        "footer":   "Sources: Damodaran annual data (S&P 500, 10y T-bond), FRED GOLDAMGBD228NLBM (gold). Real returns deflated by CPI.",
    },
    "hk": {
        "title":    "黃金 vs 標普 500 vs 60/40 vs 60/25/15 — 分時期比較",
        "subtitle": "每張小圖每條線都由該時期起點 $1 開始。CPI 調整後實質回報。60/25/15 組合在 60/25 股債核心上加入 15% 黃金。",
        "stocks":   "100% 標普 500",
        "gold":     "100% 黃金",
        "sixty":    "60/40",
        "blend":    "60/25/15(含黃金)",
        "r_70s":      "1971-1980 — 滯脹、布雷頓森林結束",
        "r_disinf":   "1981-1999 — Volcker 反通脹、股市大牛",
        "r_lostdec":  "2000-2011 — 科網爆破 + 金融海嘯",
        "r_disinf2":  "2012-2019 — 金融海嘯後低通脹",
        "r_covid":    "2020-2024 — 新冠 + 再通脹",
        "r_full":     "1971-2024 — 全期",
        "ann":      "幾何年化實質回報({n}年):標普 {s:+.1%}  ·  60/40 {m:+.1%}  ·  60/25/15 {b:+.1%}  ·  黃金 {g:+.1%}",
        "footer":   "資料來源:Damodaran 年度資料(標普 500、10 年國債)、FRED GOLDAMGBD228NLBM(黃金)。實質回報以 CPI 調整。",
    },
    "tw": {
        "title":    "黃金 vs 標普 500 vs 60/40 vs 60/25/15 — 各時期比較",
        "subtitle": "每張小圖每條線從該時期起點 $1 開始。CPI 調整後實質報酬。60/25/15 組合在 60/25 股債核心上加 15% 黃金。",
        "stocks":   "100% 標普 500",
        "gold":     "100% 黃金",
        "sixty":    "60/40",
        "blend":    "60/25/15(含黃金)",
        "r_70s":      "1971-1980 — 停滯性通膨、布列敦森林結束",
        "r_disinf":   "1981-1999 — Volcker 抗通膨、股市大牛",
        "r_lostdec":  "2000-2011 — 科技泡沫 + 金融海嘯",
        "r_disinf2":  "2012-2019 — 金融海嘯後低通膨",
        "r_covid":    "2020-2024 — 新冠 + 再通膨",
        "r_full":     "1971-2024 — 全期",
        "ann":      "幾何年化實質報酬({n}年):標普 {s:+.1%}  ·  60/40 {m:+.1%}  ·  60/25/15 {b:+.1%}  ·  黃金 {g:+.1%}",
        "footer":   "資料來源:Damodaran 年度資料(標普 500、10 年公債)、FRED GOLDAMGBD228NLBM(黃金)。實質報酬以 CPI 調整。",
    },
    "cn": {
        "title":    "黄金 vs 标普 500 vs 60/40 vs 60/25/15 — 分时期比较",
        "subtitle": "每张小图每条线从该时期起点 $1 开始。CPI 调整后实质回报。60/25/15 组合在 60/25 股债核心上加入 15% 黄金。",
        "stocks":   "100% 标普 500",
        "gold":     "100% 黄金",
        "sixty":    "60/40",
        "blend":    "60/25/15(含黄金)",
        "r_70s":      "1971-1980 — 滞胀、布雷顿森林体系终结",
        "r_disinf":   "1981-1999 — Volcker 反通胀、股市大牛",
        "r_lostdec":  "2000-2011 — 互联网泡沫 + 金融危机",
        "r_disinf2":  "2012-2019 — 金融危机后低通胀",
        "r_covid":    "2020-2024 — 新冠 + 再通胀",
        "r_full":     "1971-2024 — 全期",
        "ann":      "几何年化实质回报({n}年):标普 {s:+.1%}  ·  60/40 {m:+.1%}  ·  60/25/15 {b:+.1%}  ·  黄金 {g:+.1%}",
        "footer":   "数据来源:Damodaran 年度数据(标普 500、10 年国债)、FRED GOLDAMGBD228NLBM(黄金)。实质回报以 CPI 调整。",
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


def _annual_real_returns() -> pd.DataFrame:
    """Return DataFrame with annual real returns for stocks, bonds, gold + 60/40 + 60/25/15."""
    dam = damodaran_annual_returns()
    dam = dam.loc[1971:2024]
    sp = dam["SP500"]
    bd = dam["TBond10Y"]
    cpi = dam["CPI"]

    rs = (1 + sp) / (1 + cpi) - 1
    rb = (1 + bd) / (1 + cpi) - 1

    gold = _gold_annual()
    nom_g = gold.pct_change().fillna(0.0)
    real_g = (1 + nom_g) / (1 + cpi.reindex(gold.index)) - 1
    real_g.iloc[0] = 0.0

    rm = 0.6 * rs + 0.4 * rb
    rblend = 0.6 * rs + 0.25 * rb + 0.15 * real_g.reindex(rs.index)

    return pd.DataFrame({
        "stocks": rs, "bonds": rb, "gold": real_g.reindex(rs.index),
        "sixty": rm, "blend": rblend,
    }).dropna()


def _cum(returns: pd.Series, y0: int, y1: int) -> pd.Series:
    """Cumulative wealth from $1 at start of y0 through end of y1."""
    sub = returns.loc[y0:y1]
    cum = (1 + sub).cumprod()
    cum = pd.concat([pd.Series([1.0], index=[y0 - 1]), cum])
    return cum


def _ann(returns: pd.Series, y0: int, y1: int) -> float:
    sub = returns.loc[y0:y1]
    n = len(sub)
    if n == 0:
        return 0.0
    return float((1 + sub).prod() ** (1.0 / n) - 1)


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    df = _annual_real_returns()
    p = PALETTE_LIGHT

    fig, axes = plt.subplots(2, 3, figsize=(14.0, 8.6))
    axes = axes.flatten()

    for ax, (y0, y1, key) in zip(axes, REGIMES):
        style_axes(ax, p)
        cs = _cum(df["stocks"], y0, y1)
        cg = _cum(df["gold"], y0, y1)
        cm = _cum(df["sixty"], y0, y1)
        cb = _cum(df["blend"], y0, y1)

        ax.plot(cs.index, cs.values, color=p["red"], linewidth=1.6, label=s["stocks"])
        ax.plot(cg.index, cg.values, color=p["accent"], linewidth=1.6, label=s["gold"])
        ax.plot(cm.index, cm.values, color=p["blue"], linewidth=1.6, label=s["sixty"])
        ax.plot(cb.index, cb.values, color=p["green"], linewidth=2.0, label=s["blend"])

        ax.axhline(1.0, color=p["muted"], linewidth=0.5, linestyle=":")
        ax.set_title(s[key], fontsize=10.5, fontweight="bold", loc="left")
        ax.set_xlim(y0 - 1, y1 + 1)
        ax.tick_params(labelsize=8)

        n = y1 - y0 + 1
        ann_s = _ann(df["stocks"], y0, y1)
        ann_g = _ann(df["gold"], y0, y1)
        ann_m = _ann(df["sixty"], y0, y1)
        ann_b = _ann(df["blend"], y0, y1)
        ax.text(0.02, -0.22,
                s["ann"].format(n=n, s=ann_s, m=ann_m, b=ann_b, g=ann_g),
                transform=ax.transAxes, fontsize=8, color=p["muted"])

    # Legend on first axis
    axes[0].legend(loc="upper left", frameon=False, fontsize=8)

    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 x=0.04, ha="left", y=0.995)
    fig.text(0.04, 0.96, s["subtitle"], fontsize=10, color=p["muted"], ha="left")
    fig.text(0.04, 0.005, s["footer"], fontsize=8.5, color=p["muted"], ha="left")

    fig.tight_layout(rect=[0, 0.02, 1, 0.94])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
