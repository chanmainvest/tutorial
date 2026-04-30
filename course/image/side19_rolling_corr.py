"""Side 19, Sec 2.4 — SPY-TLT 90-day rolling correlation, 2002 to Apr 2026.

Pulls daily AdjClose for SPY and TLT from Yahoo, computes daily simple
returns, then a 90-trading-day rolling correlation. Annotates the 2008
spike toward zero, the March 2020 COVID briefly-positive print, and the
2022 regime flip from -0.4 to roughly +0.3.

Falls back to an embedded monthly series of approximate rolling-90D
correlation values if Yahoo fails or returns truncated data.

Run:
    uv run python course/image/side19_rolling_corr.py
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
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import yahoo_history  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side19_rolling_corr"

START = "2002-07-01"   # TLT inception ~2002-07
END = "2026-04-30"
WINDOW = 90

# Monthly fallback: approx end-of-month 90D rolling SPY/TLT correlation.
# Sourced from published SPY/TLT correlation studies (S&P, BlackRock,
# Morningstar) plus author estimates for in-between months. Smooth
# interpolation; not for trading. Used only when Yahoo is unavailable.
_FALLBACK_MONTHLY = {
    # 2002
    "2002-12": -0.20,
    # 2003
    "2003-06": -0.30, "2003-12": -0.45,
    # 2004
    "2004-06": -0.50, "2004-12": -0.40,
    # 2005
    "2005-06": -0.30, "2005-12": -0.25,
    # 2006
    "2006-06": -0.20, "2006-12": -0.15,
    # 2007
    "2007-06": -0.30, "2007-12": -0.40,
    # 2008
    "2008-03": -0.45, "2008-06": -0.40,
    "2008-09": -0.10, "2008-12": -0.30,   # Lehman regime
    # 2009
    "2009-06": -0.50, "2009-12": -0.55,
    # 2010
    "2010-06": -0.60, "2010-12": -0.50,
    # 2011
    "2011-06": -0.40, "2011-12": -0.55,
    # 2012
    "2012-06": -0.40, "2012-12": -0.30,
    # 2013 taper tantrum
    "2013-06": -0.10, "2013-12": -0.25,
    # 2014
    "2014-06": -0.35, "2014-12": -0.40,
    # 2015
    "2015-06": -0.30, "2015-12": -0.35,
    # 2016
    "2016-06": -0.40, "2016-12": -0.45,
    # 2017
    "2017-06": -0.50, "2017-12": -0.40,
    # 2018 Q4 hike scare
    "2018-06": -0.30, "2018-12": -0.10,
    # 2019
    "2019-06": -0.45, "2019-12": -0.55,
    # 2020 COVID
    "2020-03": -0.05, "2020-06": -0.50, "2020-12": -0.45,
    # 2021
    "2021-06": -0.40, "2021-12": -0.30,
    # 2022 inflation regime flip
    "2022-03": +0.05, "2022-06": +0.45, "2022-09": +0.55, "2022-12": +0.40,
    # 2023
    "2023-03": +0.30, "2023-06": +0.10, "2023-09": +0.20, "2023-12": +0.05,
    # 2024
    "2024-03": +0.10, "2024-06": +0.00, "2024-09": -0.05, "2024-12": +0.10,
    # 2025
    "2025-03": +0.15, "2025-06": +0.20, "2025-09": +0.10, "2025-12": +0.05,
    # 2026
    "2026-03": +0.10,
}


def _load_real_corr() -> pd.Series | None:
    """Try to fetch SPY+TLT from Yahoo and compute rolling corr."""
    try:
        spy = yahoo_history("SPY", start=START, end=END)["AdjClose"]
        tlt = yahoo_history("TLT", start=START, end=END)["AdjClose"]
        df = pd.concat([spy.rename("SPY"), tlt.rename("TLT")], axis=1).dropna()
        if len(df) < WINDOW * 4:
            return None
        rets = df.pct_change().dropna()
        # rolling pearson
        rho = rets["SPY"].rolling(WINDOW).corr(rets["TLT"]).dropna()
        return rho
    except Exception as exc:
        print(f"[side19_rolling_corr] Yahoo fetch failed ({exc}); using fallback.")
        return None


def _fallback_corr() -> pd.Series:
    items = sorted(_FALLBACK_MONTHLY.items())
    idx = pd.to_datetime([k + "-15" for k, _ in items])
    vals = np.array([v for _, v in items], dtype=float)
    s = pd.Series(vals, index=idx)
    # Reindex daily (business days) and interpolate for a smooth line.
    daily_idx = pd.date_range(start=START, end=END, freq="B")
    return s.reindex(s.index.union(daily_idx)).interpolate("time").reindex(daily_idx)


def _series() -> pd.Series:
    real = _load_real_corr()
    if real is not None and len(real) > 100:
        return real
    return _fallback_corr()


LANG_STRINGS = {
    "en": {
        "title":    "SPY vs TLT: 90-day rolling correlation, 2002-2026",
        "subtitle": "Two decades of negative equity-bond correlation made 60/40 work. The 2022 inflation regime flipped the sign.",
        "xlabel":   "Date",
        "ylabel":   "90-day rolling correlation",
        "label":    "SPY-TLT 90D corr",
        "ann_2008": "Oct 2008\nLehman: rho ~ -0.1",
        "ann_2020": "Mar 2020\nCOVID: rho ~ 0",
        "ann_2022": "2022\nregime flip: rho > +0.5",
        "ann_baseline": "2010s baseline\n~ -0.4",
        "footer":   "SPY+TLT daily AdjClose, Yahoo Finance. Monthly fallback used if fetch fails. Reference lines at 0 (no diversification benefit) and -0.4 (2010s typical).",
    },
    "hk": {
        "title":    "SPY vs TLT:90 日滾動相關性,2002-2026",
        "subtitle": "20 年股債負相關支撐了 60/40。2022 通脹體制翻轉了符號。",
        "xlabel":   "日期",
        "ylabel":   "90 日滾動相關性",
        "label":    "SPY-TLT 90D 相關",
        "ann_2008": "2008 年 10 月\n雷曼:rho ~ -0.1",
        "ann_2020": "2020 年 3 月\n新冠:rho ~ 0",
        "ann_2022": "2022 年\n體制翻轉:rho > +0.5",
        "ann_baseline": "2010 年代基準線\n~ -0.4",
        "footer":   "SPY+TLT 日度復權收盤,Yahoo Finance。如取數失敗使用月度 fallback。參考線:0(無分散收益)及 -0.4(2010 年代典型值)。",
    },
    "tw": {
        "title":    "SPY vs TLT:90 日滾動相關性,2002-2026",
        "subtitle": "20 年股債負相關支撐了 60/40。2022 通膨情境翻轉了符號。",
        "xlabel":   "日期",
        "ylabel":   "90 日滾動相關性",
        "label":    "SPY-TLT 90D 相關",
        "ann_2008": "2008 年 10 月\n雷曼:rho ~ -0.1",
        "ann_2020": "2020 年 3 月\n新冠:rho ~ 0",
        "ann_2022": "2022 年\n情境翻轉:rho > +0.5",
        "ann_baseline": "2010 年代基準\n~ -0.4",
        "footer":   "SPY+TLT 日度復權收盤,Yahoo Finance。若取數失敗使用月度 fallback。參考線:0(無分散收益)及 -0.4(2010 年代典型值)。",
    },
    "cn": {
        "title":    "SPY vs TLT:90 日滚动相关性,2002-2026",
        "subtitle": "20 年股债负相关支撑了 60/40。2022 通胀环境翻转了符号。",
        "xlabel":   "日期",
        "ylabel":   "90 日滚动相关性",
        "label":    "SPY-TLT 90D 相关",
        "ann_2008": "2008 年 10 月\n雷曼:rho ~ -0.1",
        "ann_2020": "2020 年 3 月\n新冠:rho ~ 0",
        "ann_2022": "2022 年\n环境翻转:rho > +0.5",
        "ann_baseline": "2010 年代基准\n~ -0.4",
        "footer":   "SPY+TLT 日度复权收盘,Yahoo Finance。若取数失败使用月度 fallback。参考线:0(无分散收益)及 -0.4(2010 年代典型值)。",
    },
}


_RHO = _series()


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)

    rho = _RHO
    # Color fill: green where negative (good diversification), red where positive.
    ax.fill_between(rho.index, rho.values, 0,
                    where=(rho.values < 0), color=PALETTE_LIGHT["green"],
                    alpha=0.18, interpolate=True)
    ax.fill_between(rho.index, rho.values, 0,
                    where=(rho.values >= 0), color=PALETTE_LIGHT["red"],
                    alpha=0.20, interpolate=True)
    ax.plot(rho.index, rho.values, color=PALETTE_LIGHT["blue"],
            linewidth=1.2, alpha=0.85, label=s["label"], zorder=3)

    ax.axhline(0, color=PALETTE_LIGHT["fg"], linewidth=0.9,
               linestyle="-", alpha=0.55, zorder=2)
    ax.axhline(-0.4, color=PALETTE_LIGHT["green"], linewidth=0.9,
               linestyle="--", alpha=0.55, zorder=2)

    # Annotations.
    def _annot(date_str, label, xy_off, color):
        ts = pd.Timestamp(date_str)
        if ts not in rho.index:
            ts = rho.index[rho.index.get_indexer([ts], method="nearest")[0]]
        y = float(rho.loc[ts])
        ax.annotate(
            label, xy=(ts, y),
            xytext=(ts + pd.Timedelta(days=xy_off[0]), y + xy_off[1]),
            fontsize=9, color=color, ha="center", va="center",
            arrowprops=dict(arrowstyle="->", color=color, lw=0.9, alpha=0.75),
        )

    _annot("2008-10-15", s["ann_2008"], (-700, +0.30), PALETTE_LIGHT["red"])
    _annot("2020-03-23", s["ann_2020"], (-600, +0.40), PALETTE_LIGHT["accent"])
    _annot("2022-09-15", s["ann_2022"], (-300, +0.25), PALETTE_LIGHT["red"])
    # Baseline label as plain text (no arrow).
    ax.text(pd.Timestamp("2015-01-01"), -0.62, s["ann_baseline"],
            fontsize=9, color=PALETTE_LIGHT["green"], ha="center", va="center")

    ax.set_ylim(-0.85, 0.85)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.legend(loc="lower left", framealpha=0.9, fontsize=9.5)

    style_axes(ax)
    ax.set_title(s["title"], pad=24, fontsize=14.5, weight="bold")
    fig.text(0.5, 0.935, s["subtitle"], ha="center",
             fontsize=10, color=PALETTE_LIGHT["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=PALETTE_LIGHT["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
