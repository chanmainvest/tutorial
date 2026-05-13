"""Side 29, §2.4 -- Trade-Weighted U.S. Dollar Index 1990-Apr 2026.

Tries FRED DTWEXBGS first (Broad goods+services, 2006+) and falls back
to an embedded monthly approximation 1990-2026.  Five strong/weak-dollar
regimes shaded and labelled.

Run:
    uv run python course/image/side29_dxy_history.py
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
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import fred_series  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side29_dxy_history"


# Approximate quarterly trade-weighted USD index 1990-Apr 2026.
# Re-based to 100 = 2006-Jan to match FRED DTWEXBGS scale.
# Sources: ICE DXY rebased to broad-index + Fed DTWEXM/DTWEXBGS splice.
EMBED = [
    # (year, month, value)
    (1990, 1, 90), (1990, 7, 88), (1991, 1, 92), (1991, 7, 89),
    (1992, 1, 88), (1992, 7, 84), (1993, 1, 90), (1993, 7, 92),
    (1994, 1, 92), (1994, 7, 88), (1995, 1, 88), (1995, 7, 86),
    (1996, 1, 90), (1996, 7, 91), (1997, 1, 96), (1997, 7, 99),
    (1998, 1, 102), (1998, 7, 104), (1999, 1, 100), (1999, 7, 100),
    (2000, 1, 105), (2000, 7, 110), (2001, 1, 115), (2001, 7, 117),
    (2002, 1, 119), (2002, 7, 113), (2003, 1, 109), (2003, 7, 105),
    (2004, 1, 101), (2004, 7, 99), (2005, 1, 96), (2005, 7, 99),
    (2006, 1, 100), (2006, 7, 98), (2007, 1, 97), (2007, 7, 94),
    (2008, 1, 90), (2008, 7, 87), (2009, 1, 100), (2009, 7, 95),
    (2010, 1, 96), (2010, 7, 95), (2011, 1, 92), (2011, 7, 90),
    (2012, 1, 95), (2012, 7, 96), (2013, 1, 95), (2013, 7, 96),
    (2014, 1, 95), (2014, 7, 96), (2015, 1, 105), (2015, 7, 109),
    (2016, 1, 113), (2016, 7, 110), (2017, 1, 113), (2017, 7, 109),
    (2018, 1, 105), (2018, 7, 110), (2019, 1, 113), (2019, 7, 113),
    (2020, 1, 113), (2020, 7, 113), (2021, 1, 110), (2021, 7, 111),
    (2022, 1, 113), (2022, 7, 119), (2022, 10, 124),
    (2023, 1, 119), (2023, 7, 116), (2024, 1, 119), (2024, 7, 117),
    (2024, 12, 122), (2025, 4, 118), (2025, 8, 113),
    (2026, 1, 110), (2026, 4, 109),
]


def _series() -> pd.Series:
    """Try FRED DTWEXBGS first; if unavailable, return embedded series."""
    try:
        df = fred_series("DTWEXBGS", start="2006-01-01")
        s_fred = df["DTWEXBGS"].resample("ME").mean()
    except Exception:
        s_fred = None

    # Build embedded series.
    idx = [pd.Timestamp(y, m, 1) for (y, m, _) in EMBED]
    vals = [v for (_, _, v) in EMBED]
    s_emb = pd.Series(vals, index=pd.DatetimeIndex(idx)).resample("ME").interpolate()

    if s_fred is not None and len(s_fred) > 100:
        # Splice: embedded pre-2006, FRED 2006+
        cutoff = pd.Timestamp("2006-01-01")
        # Scale embedded to match FRED at the cutoff month
        first_fred = s_fred[s_fred.index >= cutoff].iloc[0]
        last_emb = s_emb[s_emb.index < cutoff].iloc[-1]
        if last_emb > 0:
            scale = first_fred / last_emb
            s_emb_scaled = s_emb[s_emb.index < cutoff] * scale
        else:
            s_emb_scaled = s_emb[s_emb.index < cutoff]
        s_full = pd.concat([s_emb_scaled, s_fred[s_fred.index >= cutoff]])
        return s_full.sort_index()
    return s_emb


REGIMES = [
    # (start, end, label_key, color_key)
    ("1995-01-01", "2002-02-01", "reg1", "red"),
    ("2002-02-01", "2008-04-01", "reg2", "blue"),
    ("2014-06-01", "2016-12-01", "reg3", "red"),
    ("2022-01-01", "2022-12-01", "reg4", "red"),
    ("2024-12-01", "2026-04-30", "reg5", "blue"),
]


LANG_STRINGS = {
    "en": {
        "title":    "Trade-Weighted U.S. Dollar Index, 1990-Apr 2026",
        "subtitle": "FRED DTWEXBGS spliced with pre-2006 embedded broad-USD approximation. Five labelled regimes.",
        "xlabel":   "Year",
        "ylabel":   "Index level (2006-Jan = 100)",
        "footer":   "Source: Federal Reserve H.10 (DTWEXBGS), pre-2006 reconstructed from Fed DTWEXM and ICE DXY. Monthly average.",
        "reg1":     "1995-2002\nstrong USD",
        "reg2":     "2002-2008\nweak USD",
        "reg3":     "2014-2016\nstrong USD 2.0",
        "reg4":     "2022\nspike to 124",
        "reg5":     "2025-2026\nretracement",
    },
    "hk": {
        "title":    "貿易加權美元指數,1990-2026 年 4 月",
        "subtitle": "FRED DTWEXBGS 與 2006 年前廣義美元估算拼接。五個標示體制。",
        "xlabel":   "年份",
        "ylabel":   "指數水平(2006 年 1 月 = 100)",
        "footer":   "來源:聯儲局 H.10(DTWEXBGS),2006 年前由 Fed DTWEXM 與 ICE DXY 重構。月度平均。",
        "reg1":     "1995-2002\n強美元",
        "reg2":     "2002-2008\n弱美元",
        "reg3":     "2014-2016\n強美元 2.0",
        "reg4":     "2022\n飆升至 124",
        "reg5":     "2025-2026\n回落",
    },
    "tw": {
        "title":    "貿易加權美元指數,1990-2026 年 4 月",
        "subtitle": "FRED DTWEXBGS 與 2006 年前廣義美元估算拼接。五個標示體制。",
        "xlabel":   "年份",
        "ylabel":   "指數水準(2006 年 1 月 = 100)",
        "footer":   "資料:Fed H.10(DTWEXBGS),2006 年前由 Fed DTWEXM 與 ICE DXY 重構。月度平均。",
        "reg1":     "1995-2002\n強美元",
        "reg2":     "2002-2008\n弱美元",
        "reg3":     "2014-2016\n強美元 2.0",
        "reg4":     "2022\n飆升至 124",
        "reg5":     "2025-2026\n回落",
    },
    "cn": {
        "title":    "贸易加权美元指数,1990-2026 年 4 月",
        "subtitle": "FRED DTWEXBGS 与 2006 年前广义美元估算拼接。五个标示体制。",
        "xlabel":   "年份",
        "ylabel":   "指数水平(2006 年 1 月 = 100)",
        "footer":   "来源:美联储 H.10(DTWEXBGS),2006 年前由 Fed DTWEXM 与 ICE DXY 重构。月度平均。",
        "reg1":     "1995-2002\n强美元",
        "reg2":     "2002-2008\n弱美元",
        "reg3":     "2014-2016\n强美元 2.0",
        "reg4":     "2022\n飙升至 124",
        "reg5":     "2025-2026\n回落",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    series = _series()
    fig, ax = plt.subplots(figsize=(11.0, 6.2))
    style_axes(ax, p)

    # Regime shading
    for start, end, key, col_key in REGIMES:
        ax.axvspan(pd.Timestamp(start), pd.Timestamp(end),
                   color=p[col_key], alpha=0.06, lw=0)

    ax.plot(series.index, series.values, color=p["blue"], linewidth=1.8)

    # Long-term reference: median
    median_val = float(series.median())
    ax.axhline(median_val, color=p["muted"], linestyle="--", linewidth=0.8, alpha=0.6)
    ax.text(series.index[5], median_val + 0.6,
            f"median = {median_val:.0f}",
            fontsize=8.5, color=p["muted"], style="italic")

    # Regime labels
    label_y = series.max() * 1.02
    label_positions = {
        "reg1": pd.Timestamp("1998-08-01"),
        "reg2": pd.Timestamp("2005-04-01"),
        "reg3": pd.Timestamp("2015-09-01"),
        "reg4": pd.Timestamp("2022-06-01"),
        "reg5": pd.Timestamp("2025-08-01"),
    }
    for key, x in label_positions.items():
        ax.text(x, label_y, s[key], fontsize=8.3, color=p["fg"],
                ha="center", va="bottom", fontweight="bold")

    # End-point marker
    last_x, last_y = series.index[-1], float(series.iloc[-1])
    ax.plot([last_x], [last_y], marker="o", color=p["red"], markersize=7)
    ax.annotate(f"Apr 2026: {last_y:.0f}",
                xy=(last_x, last_y),
                xytext=(-90, -22), textcoords="offset points",
                fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.8))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24, color=p["fg"])
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.text(0, -0.12, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"], style="italic")

    ymin = float(series.min()) * 0.95
    ymax = float(series.max()) * 1.10
    ax.set_ylim(ymin, ymax)

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
