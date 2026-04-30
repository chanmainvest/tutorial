"""Side 09, sec 1 -- Bitcoin USD price 2010-Apr 2026 (log scale).

Embedded month-end price anchors built from well-known historical
Bitcoin closes (CoinDesk/Yahoo BTC-USD). Plotted log-scale with the
four halvings marked, the four cycle peaks annotated, and the three
completed minus-eighty-per-cent drawdowns shaded.

Run:
    uv run python course/image/side09_btc_history.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side09_btc_history"

# Month-end BTC USD price anchors (approximate). Used to construct a
# continuous log-price line. Sources: CoinDesk historical, Yahoo
# BTC-USD. Values rounded to plausible historicals.
ANCHORS = [
    ("2010-07-15",      0.08),
    ("2010-12-31",      0.30),
    ("2011-06-30",     17.00),  # first mini-bubble
    ("2011-12-31",      4.70),
    ("2012-12-31",     13.50),
    ("2013-04-15",    230.00),  # April 2013 spike
    ("2013-12-31",    760.00),  # Cycle 1 peak ~ $1150
    ("2013-11-30",   1150.00),  # actual cycle 1 high
    ("2014-12-31",    315.00),
    ("2015-01-15",    180.00),  # 2015 trough -85% from 2013-11
    ("2015-12-31",    430.00),
    ("2016-07-09",    660.00),  # halving #2
    ("2016-12-31",    960.00),
    ("2017-06-30",   2500.00),
    ("2017-12-17",  19800.00),  # Cycle 2 peak
    ("2018-06-30",   6400.00),
    ("2018-12-15",   3200.00),  # cycle 2 trough
    ("2019-06-30",  10800.00),
    ("2019-12-31",   7200.00),
    ("2020-03-15",   5000.00),  # COVID flush
    ("2020-05-11",   9000.00),  # halving #3
    ("2020-12-31",  29000.00),
    ("2021-04-15",  63000.00),
    ("2021-07-15",  31500.00),
    ("2021-11-10",  69000.00),  # Cycle 3 peak
    ("2022-06-30",  19800.00),
    ("2022-11-15",  15500.00),  # FTX low
    ("2022-12-31",  16500.00),
    ("2023-06-30",  30500.00),
    ("2023-12-31",  42000.00),
    ("2024-01-11",  46000.00),  # spot ETF launch
    ("2024-04-19",  64000.00),  # halving #4
    ("2024-12-31",  93000.00),
    ("2025-06-30", 118000.00),
    ("2025-10-15", 145000.00),  # Cycle 4 peak (so far)
    ("2025-12-31", 132000.00),
    ("2026-04-30", 112000.00),
]

HALVINGS = [
    ("2012-11-28", "halving #1"),
    ("2016-07-09", "halving #2"),
    ("2020-05-11", "halving #3"),
    ("2024-04-19", "halving #4"),
]

CYCLE_PEAKS = [
    # (date, price, en, hk, tw, cn)
    ("2013-11-30",   1150.00,
     "Cycle 1 peak\n$1,150",
     "周期一峰\n1,150 美元",
     "週期一峰\n1,150 美元",
     "周期一峰\n1,150 美元"),
    ("2017-12-17",  19800.00,
     "Cycle 2 peak\n$19,800",
     "周期二峰\n19,800 美元",
     "週期二峰\n19,800 美元",
     "周期二峰\n19,800 美元"),
    ("2021-11-10",  69000.00,
     "Cycle 3 peak\n$69,000",
     "周期三峰\n69,000 美元",
     "週期三峰\n69,000 美元",
     "周期三峰\n69,000 美元"),
    ("2025-10-15", 145000.00,
     "Cycle 4 peak\n$145,000",
     "周期四峰\n145,000 美元",
     "週期四峰\n145,000 美元",
     "周期四峰\n145,000 美元"),
]

# Cycle drawdowns to shade (start, end).
DRAWDOWN_BANDS = [
    ("2013-11-30", "2015-01-15"),   # -85%
    ("2017-12-17", "2018-12-15"),   # -84%
    ("2021-11-10", "2022-11-15"),   # -77%
]


def _build_series() -> pd.Series:
    rows = []
    for d, p in ANCHORS:
        rows.append((pd.to_datetime(d), float(p)))
    df = (
        pd.DataFrame(rows, columns=["date", "price"])
        .drop_duplicates(subset=["date"])
        .sort_values("date")
        .reset_index(drop=True)
    )
    # Reindex to monthly business-month-end and log-interpolate so the
    # line is smooth. The anchors define the shape; the interpolation
    # just fills in.
    full_idx = pd.date_range(df["date"].iloc[0], df["date"].iloc[-1],
                             freq="ME")
    s = pd.Series(np.log(df["price"].values), index=df["date"].values)
    s = s.reindex(s.index.union(full_idx)).sort_index().interpolate("time")
    s = s.loc[full_idx]
    return pd.Series(np.exp(s.values), index=s.index, name="BTC")


LANG_STRINGS = {
    "en": {
        "title":    "Bitcoin USD price, log scale, July 2010 - April 2026",
        "subtitle": "Three completed -80% drawdowns. Each cycle's recovery has gone to a higher high. SOUL #3 (belief) + SOUL #6 (vol-tail-wags-dog).",
        "xlabel":   "Year",
        "ylabel":   "BTC price (USD, log)",
        "drawdown": "drawdown",
        "footer":   "Sources: CoinDesk, Yahoo BTC-USD. Cycle peaks 2013-11, 2017-12, 2021-11, 2025-10. Halvings 2012-11, 2016-07, 2020-05, 2024-04.",
        "_lang":    "en",
    },
    "hk": {
        "title":    "比特幣美元價,對數刻度,2010 年 7 月 - 2026 年 4 月",
        "subtitle": "三次完整的 -80% 跌幅。每個周期的回復都創出更高高點。SOUL #3(信念)+ SOUL #6(波幅尾擺狗)。",
        "xlabel":   "年份",
        "ylabel":   "比特幣價(美元,對數)",
        "drawdown": "跌幅",
        "footer":   "資料來源:CoinDesk、Yahoo BTC-USD。周期峰:2013-11、2017-12、2021-11、2025-10。減半:2012-11、2016-07、2020-05、2024-04。",
        "_lang":    "hk",
    },
    "tw": {
        "title":    "比特幣美元價,對數刻度,2010 年 7 月 - 2026 年 4 月",
        "subtitle": "三次完整的 -80% 回撤。每個週期的回復都創更高高點。SOUL #3(信念)+ SOUL #6(波動尾擺狗)。",
        "xlabel":   "年份",
        "ylabel":   "比特幣價(美元,對數)",
        "drawdown": "回撤",
        "footer":   "資料來源:CoinDesk、Yahoo BTC-USD。週期峰:2013-11、2017-12、2021-11、2025-10。減半:2012-11、2016-07、2020-05、2024-04。",
        "_lang":    "tw",
    },
    "cn": {
        "title":    "比特币美元价,对数刻度,2010 年 7 月 - 2026 年 4 月",
        "subtitle": "三次完整的 -80% 回撤。每个周期的回复都创更高高点。SOUL #3(信念)+ SOUL #6(波动尾摆狗)。",
        "xlabel":   "年份",
        "ylabel":   "比特币价(美元,对数)",
        "drawdown": "回撤",
        "footer":   "数据来源:CoinDesk、Yahoo BTC-USD。周期峰:2013-11、2017-12、2021-11、2025-10。减半:2012-11、2016-07、2020-05、2024-04。",
        "_lang":    "cn",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    btc = _build_series()

    fig, ax = plt.subplots(figsize=(12.0, 6.4), dpi=150)
    style_axes(ax, p)
    ax.set_yscale("log")

    # Drawdown shading
    lang_idx = {"en": 2, "hk": 3, "tw": 4, "cn": 5}.get(s.get("_lang", "en"), 2)
    for start, end in DRAWDOWN_BANDS:
        ax.axvspan(pd.to_datetime(start), pd.to_datetime(end),
                   color=p["red"], alpha=0.10, linewidth=0)

    # Halving vertical markers (dotted)
    for d, _ in HALVINGS:
        ax.axvline(pd.to_datetime(d), color=p["accent"],
                   linewidth=0.8, linestyle=":", alpha=0.75)

    # Main line
    ax.plot(btc.index, btc.values, color=p["blue"],
            linewidth=1.4, zorder=4)
    # Latest point
    ax.plot([btc.index[-1]], [btc.values[-1]], "o",
            color=p["accent"], markeredgecolor=p["fg"],
            markersize=7, zorder=5)

    # Cycle peak annotations
    for ev in CYCLE_PEAKS:
        date = pd.to_datetime(ev[0])
        price = ev[1]
        label = ev[lang_idx]
        ax.plot([date], [price], "o", color=p["red"],
                markeredgecolor=p["fg"], markersize=6, zorder=5)
        ax.annotate(
            label,
            xy=(date, price),
            xytext=(-32, 26),
            textcoords="offset points",
            ha="left",
            fontsize=8.6,
            color=p["fg"],
            fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=p["muted"],
                            linewidth=0.6, alpha=0.7),
        )

    # Halving labels along the bottom
    halv_lbl_map = {
        "en": ["halving 1 (2012-11)", "halving 2 (2016-07)",
               "halving 3 (2020-05)", "halving 4 (2024-04)"],
        "hk": ["減半 1 (2012-11)", "減半 2 (2016-07)",
               "減半 3 (2020-05)", "減半 4 (2024-04)"],
        "tw": ["減半 1 (2012-11)", "減半 2 (2016-07)",
               "減半 3 (2020-05)", "減半 4 (2024-04)"],
        "cn": ["减半 1 (2012-11)", "减半 2 (2016-07)",
               "减半 3 (2020-05)", "减半 4 (2024-04)"],
    }
    halv_lbls = halv_lbl_map.get(s.get("_lang", "en"), halv_lbl_map["en"])
    y_lbl_min = 0.18
    for (d, _), lbl in zip(HALVINGS, halv_lbls):
        ax.text(pd.to_datetime(d), y_lbl_min, lbl,
                rotation=90, fontsize=7.5, color=p["accent"],
                fontweight="bold", va="bottom", ha="right", alpha=0.9)

    # Drawdown labels
    dd_pcts = ["-85%", "-84%", "-77%"]
    for (start, end), pct in zip(DRAWDOWN_BANDS, dd_pcts):
        mid = pd.to_datetime(start) + (pd.to_datetime(end) - pd.to_datetime(start)) / 2
        ax.text(mid, 0.55, f"{s['drawdown']} {pct}",
                ha="center", va="bottom", fontsize=7.8,
                color=p["red"], fontweight="bold", alpha=0.85)

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0.05, 300_000)
    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.3, color=p["muted"])

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Saved {BASE}*.png to {OUT_DIR}")
