"""Week 10, §2.5 — Average annual return by asset class across 4 regimes.

Each year 1929-2024 is tagged with one of {early, mid, late, recession}.
Bars: simple average of nominal annual returns inside each regime, for
4 asset classes: S&P 500 total return, 10y Treasuries, 3m T-bills, gold.

The S&P / Treasury / T-bill series come from the embedded Damodaran
table (scripts.market_data). Gold annual returns are embedded inline
below from London PM-fix year-end prices (1929-2024).

The regime tag per year is a simplified business-cycle label based on
NBER peaks/troughs and yoy real GDP direction:
    recession  -- year overlapping an NBER recession >= 4 months
    early      -- the 1-2 years immediately following a recession trough
    late       -- the 1-2 years immediately preceding a recession peak
    mid        -- everything else (steady expansion)

Run:
    uv run python course/image/week10_asset_class_by_regime.py
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
BASE = "week10_asset_class_by_regime"

# ---------------------------------------------------------------------------
# Regime tag per year (1929-2024). Hand-built from NBER recession dating +
# proximity to peak/trough. Categories: recession, early, mid, late.
# ---------------------------------------------------------------------------
REGIME = {
    # Great Depression contractions
    1929: "late", 1930: "recession", 1931: "recession", 1932: "recession",
    1933: "recession", 1934: "early", 1935: "early", 1936: "mid",
    1937: "late", 1938: "recession", 1939: "early", 1940: "early",
    # WWII expansion / 1945 recession
    1941: "mid", 1942: "mid", 1943: "mid", 1944: "late",
    1945: "recession", 1946: "early", 1947: "early",
    # 1948-49 recession
    1948: "late", 1949: "recession", 1950: "early", 1951: "early", 1952: "mid",
    # 1953-54 recession
    1953: "recession", 1954: "recession", 1955: "early", 1956: "mid",
    # 1957-58 recession
    1957: "recession", 1958: "recession", 1959: "early",
    # 1960-61 recession
    1960: "recession", 1961: "early", 1962: "early", 1963: "mid",
    1964: "mid", 1965: "mid", 1966: "late", 1967: "late", 1968: "late",
    # 1969-70 recession
    1969: "recession", 1970: "recession", 1971: "early", 1972: "mid",
    # 1973-75 recession (stagflation)
    1973: "recession", 1974: "recession", 1975: "recession",
    1976: "early", 1977: "mid", 1978: "late", 1979: "late",
    # 1980 + 1981-82 recessions
    1980: "recession", 1981: "recession", 1982: "recession",
    1983: "early", 1984: "early", 1985: "mid", 1986: "mid", 1987: "mid",
    1988: "mid", 1989: "late",
    # 1990-91 recession
    1990: "recession", 1991: "recession", 1992: "early", 1993: "early",
    1994: "mid", 1995: "mid", 1996: "mid", 1997: "mid", 1998: "mid",
    1999: "late", 2000: "late",
    # 2001 recession
    2001: "recession", 2002: "early", 2003: "early", 2004: "mid", 2005: "mid",
    2006: "late", 2007: "late",
    # 2008-09 recession
    2008: "recession", 2009: "recession", 2010: "early", 2011: "early",
    2012: "mid", 2013: "mid", 2014: "mid", 2015: "mid", 2016: "mid",
    2017: "mid", 2018: "mid", 2019: "late",
    # 2020 recession
    2020: "recession", 2021: "early", 2022: "late", 2023: "late",
    2024: "late",
}

# ---------------------------------------------------------------------------
# Gold annual returns (decimals), USD year-end London PM fix.
# Pre-1934 = $20.67/oz fixed; 1934 dollar devaluation lifted to $35
# (treated as a single ~+69% nominal step in 1934). $35 fixed
# 1934-1971; freely floating from 1971. Numbers below are conventional
# year-end-to-year-end returns.
# ---------------------------------------------------------------------------
GOLD = {
    1929: 0.000, 1930: 0.000, 1931: 0.000, 1932: 0.000, 1933: 0.000,
    1934: 0.6929,
    1935: 0.000, 1936: 0.000, 1937: 0.000, 1938: 0.000, 1939: 0.000,
    1940: 0.000, 1941: 0.000, 1942: 0.000, 1943: 0.000, 1944: 0.000,
    1945: 0.000, 1946: 0.000, 1947: 0.000, 1948: 0.000, 1949: 0.000,
    1950: 0.000, 1951: 0.000, 1952: 0.000, 1953: 0.000, 1954: 0.000,
    1955: 0.000, 1956: 0.000, 1957: 0.000, 1958: 0.000, 1959: 0.000,
    1960: 0.000, 1961: 0.000, 1962: 0.000, 1963: 0.000, 1964: 0.000,
    1965: 0.000, 1966: 0.000, 1967: 0.000, 1968: 0.000, 1969: 0.000,
    1970: 0.000,
    1971: 0.143, 1972: 0.434, 1973: 0.731, 1974: 0.660, 1975: -0.246,
    1976: -0.040, 1977: 0.213, 1978: 0.371, 1979: 1.268, 1980: 0.150,
    1981: -0.328, 1982: 0.144, 1983: -0.157, 1984: -0.190, 1985: 0.058,
    1986: 0.211, 1987: 0.241, 1988: -0.155, 1989: -0.025, 1990: -0.026,
    1991: -0.103, 1992: -0.058, 1993: 0.171, 1994: -0.022, 1995: 0.010,
    1996: -0.046, 1997: -0.215, 1998: -0.007, 1999: 0.012, 2000: -0.057,
    2001: 0.024, 2002: 0.243, 2003: 0.193, 2004: 0.052, 2005: 0.182,
    2006: 0.231, 2007: 0.310, 2008: 0.054, 2009: 0.244, 2010: 0.295,
    2011: 0.103, 2012: 0.071, 2013: -0.281, 2014: -0.019, 2015: -0.104,
    2016: 0.085, 2017: 0.135, 2018: -0.019, 2019: 0.184, 2020: 0.245,
    2021: -0.036, 2022: -0.005, 2023: 0.131, 2024: 0.270,
}


REGIME_ORDER = ["early", "mid", "late", "recession"]

LANG_STRINGS = {
    "en": {
        "title":    "Average annual return by asset class across business-cycle regimes, 1929-2024",
        "subtitle": "Each year tagged early / mid / late / recession from NBER dating. Simple average of nominal annual returns within each regime.",
        "xlabel":   "Cycle regime",
        "ylabel":   "Average nominal annual return",
        "stocks":   "S&P 500 total return",
        "tbond":    "10y US Treasury",
        "tbill":    "3m US T-bill",
        "gold":     "Gold (London PM fix)",
        "regimes":  ["Early-cycle", "Mid-cycle", "Late-cycle", "Recession"],
        "ann":      "Stocks dominate early. Commodities/gold dominate late. Long bonds dominate recession. Cash never strictly wins.",
    },
    "hk": {
        "title":    "各資產類別在景氣循環四階段的平均年回報,1929-2024",
        "subtitle": "依 NBER 日期將每年標為 早期/中期/晚期/衰退,計算每階段的名義年回報簡單平均。",
        "xlabel":   "景氣循環階段",
        "ylabel":   "平均名義年回報",
        "stocks":   "標普 500 總回報",
        "tbond":    "10 年期美國國債",
        "tbill":    "3 個月美國國庫券",
        "gold":     "黃金(倫敦下午定盤)",
        "regimes":  ["早期", "中期", "晚期", "衰退"],
        "ann":      "早期股票領先;晚期商品/黃金領先;衰退長債領先;現金從不長期勝出。",
    },
    "tw": {
        "title":    "各資產類別在景氣循環四階段的平均年報酬,1929-2024",
        "subtitle": "依 NBER 日期將每年標為 早期/中期/晚期/衰退,計算每階段的名義年報酬簡單平均。",
        "xlabel":   "景氣循環階段",
        "ylabel":   "平均名義年報酬",
        "stocks":   "標普 500 總報酬",
        "tbond":    "10 年期美國公債",
        "tbill":    "3 個月美國國庫券",
        "gold":     "黃金(倫敦下午定盤)",
        "regimes":  ["早期", "中期", "晚期", "衰退"],
        "ann":      "早期股票領先;晚期商品/黃金領先;衰退長債領先;現金從不長期勝出。",
    },
    "cn": {
        "title":    "各资产类别在经济周期四阶段的平均年回报,1929-2024",
        "subtitle": "按 NBER 日期将每年标为 早期/中期/晚期/衰退,计算各阶段的名义年回报简单平均。",
        "xlabel":   "周期阶段",
        "ylabel":   "平均名义年回报",
        "stocks":   "标普 500 总回报",
        "tbond":    "10 年期美国国债",
        "tbill":    "3 个月美国国库券",
        "gold":     "黄金(伦敦下午定盘)",
        "regimes":  ["早期", "中期", "晚期", "衰退"],
        "ann":      "早期股票领先;晚期商品/黄金领先;衰退长债领先;现金从不长期胜出。",
    },
}


def _avg_by_regime() -> pd.DataFrame:
    """Return a 4x4 frame: rows = regimes, columns = asset classes."""
    df = damodaran_annual_returns().copy()
    df["Gold"] = pd.Series(GOLD)
    df["regime"] = pd.Series(REGIME)
    df = df.dropna(subset=["regime"])

    out = (
        df.groupby("regime")[["SP500", "TBond10Y", "TBill3M", "Gold"]]
          .mean()
          .reindex(REGIME_ORDER)
    )
    return out


def build_fig(s):
    avg = _avg_by_regime()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 5.8))
    style_axes(ax, p)

    asset_cols = ["SP500", "TBond10Y", "TBill3M", "Gold"]
    asset_lbls = [s["stocks"], s["tbond"], s["tbill"], s["gold"]]
    asset_colors = [p["red"], p["blue"], p["grey"], p["accent"]]

    n_reg = len(REGIME_ORDER)
    n_ass = len(asset_cols)
    width = 0.9 / n_ass
    x_base = np.arange(n_reg)

    for i, (col, lbl, c) in enumerate(zip(asset_cols, asset_lbls, asset_colors)):
        vals = avg[col].values
        xs = x_base + (i - (n_ass - 1) / 2) * width
        ax.bar(xs, vals, width=width * 0.95, color=c, label=lbl,
               edgecolor="white", linewidth=0.5)
        for xi, v in zip(xs, vals):
            va = "bottom" if v >= 0 else "top"
            offset = 0.005 if v >= 0 else -0.005
            ax.text(xi, v + offset, f"{v*100:+.1f}%",
                    ha="center", va=va, fontsize=8, color=p["fg"])

    ax.axhline(0, color=p["muted"], linewidth=0.7)
    ax.set_xticks(x_base)
    ax.set_xticklabels(s["regimes"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.legend(loc="upper right", frameon=False, fontsize=9, ncol=2)

    ax.text(0, -0.16, s["ann"], transform=ax.transAxes,
            fontsize=9, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
