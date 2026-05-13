"""Week 31, §2.4 — 10y-2y Treasury spread with bull/bear regime annotations.

FRED series T10Y2Y from 1976. Highlights bull-steepener (Fed-cut)
and bear-flattener (Fed-hike) episodes by colouring the slope-
change segments. NBER recessions shown as light grey bands for
context.

Run:
    uv run python course/image/week31_slope_history.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import fred_series  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week31_slope_history"

# NBER recession dates (post-1976).
NBER = [
    ("1980-01-01", "1980-07-01"),
    ("1981-07-01", "1982-11-01"),
    ("1990-07-01", "1991-03-01"),
    ("2001-03-01", "2001-11-01"),
    ("2007-12-01", "2009-06-01"),
    ("2020-02-01", "2020-04-01"),
]

# Major regime annotations. (date, label_en, label_hk, label_tw, label_cn, regime).
REGIMES = [
    ("1981-09-01", "Volcker bear-flattener",   "沃爾克熊平", "伏克爾熊平", "沃尔克熊平", "bf"),
    ("2000-04-01", "Dotcom inversion",         "互聯網泡沫倒掛", "網路泡沫倒掛", "互联网泡沫倒挂", "bf"),
    ("2007-02-01", "Pre-GFC inversion",        "金融海嘯前倒掛", "金融海嘯前倒掛", "金融危机前倒挂", "bf"),
    ("2009-06-01", "Bull-steepener (cuts)",    "牛陡(降息)", "牛陡(降息)", "牛陡(降息)", "bs"),
    ("2019-08-01", "Brief 2019 inversion",     "2019 短暫倒掛", "2019 短暫倒掛", "2019 短暂倒挂", "bf"),
    ("2022-07-01", "2022-24 bear-flattener",   "2022-24 熊平", "2022-24 熊平", "2022-24 熊平", "bf"),
    ("2024-12-01", "Uninversion (cuts begin)", "倒掛結束", "倒掛結束", "倒挂结束", "bs"),
]

LANG_STRINGS = {
    "en": {
        "title":    "10-year minus 2-year US Treasury spread, 1976 - April 2026",
        "subtitle": "FRED T10Y2Y. Below zero = inversion. Bear-flatteners precede recessions; bull-steepeners follow them. Grey = NBER recessions.",
        "xlabel":   "Year",
        "ylabel":   "10y - 2y spread (percentage points)",
        "spread":   "10y - 2y spread",
        "rec":      "NBER recession",
        "zeroline": "Zero (inversion threshold)",
        "bf":       "Bear-flattener",
        "bs":       "Bull-steepener",
        "label_idx": 1,
    },
    "hk": {
        "title":    "10 年期減 2 年期美國國債息差,1976 - 2026 年 4 月",
        "subtitle": "FRED T10Y2Y。零以下=倒掛。熊平多領先衰退;牛陡多隨後出現。灰色=NBER 衰退。",
        "xlabel":   "年份",
        "ylabel":   "10 年減 2 年息差(百分點)",
        "spread":   "10 年減 2 年息差",
        "rec":      "NBER 衰退",
        "zeroline": "零(倒掛門檻)",
        "bf":       "熊平",
        "bs":       "牛陡",
        "label_idx": 2,
    },
    "tw": {
        "title":    "10 年期減 2 年期美國公債利差,1976 - 2026 年 4 月",
        "subtitle": "FRED T10Y2Y。零以下=倒掛。熊平多領先衰退;牛陡多隨後出現。灰色=NBER 衰退。",
        "xlabel":   "年份",
        "ylabel":   "10 年減 2 年利差(百分點)",
        "spread":   "10 年減 2 年利差",
        "rec":      "NBER 衰退",
        "zeroline": "零(倒掛門檻)",
        "bf":       "熊平",
        "bs":       "牛陡",
        "label_idx": 3,
    },
    "cn": {
        "title":    "10 年期减 2 年期美国国债利差,1976 - 2026 年 4 月",
        "subtitle": "FRED T10Y2Y。零以下=倒挂。熊平常领先衰退;牛陡常随后出现。灰色=NBER 衰退。",
        "xlabel":   "年份",
        "ylabel":   "10 年减 2 年利差(百分点)",
        "spread":   "10 年减 2 年利差",
        "rec":      "NBER 衰退",
        "zeroline": "零(倒挂阈值)",
        "bf":       "熊平",
        "bs":       "牛陡",
        "label_idx": 4,
    },
}


def _spread() -> pd.DataFrame:
    end = "2026-04-30"
    try:
        df = fred_series("T10Y2Y", start="1976-06-01", end=end)
        df.columns = ["spread"]
        return df
    except Exception:
        ten = fred_series("DGS10", start="1976-06-01", end=end)
        two = fred_series("DGS2", start="1976-06-01", end=end)
        ten.columns = ["ten"]
        two.columns = ["two"]
        df = ten.join(two, how="inner")
        df["spread"] = df["ten"] - df["two"]
        return df[["spread"]]


def build_fig(s):
    df = _spread().dropna()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.4, 6.2))
    style_axes(ax, p)

    # Recession bands behind everything
    for peak, trough in NBER:
        ax.axvspan(pd.Timestamp(peak), pd.Timestamp(trough),
                   color=p["grey"], alpha=0.15, linewidth=0)

    ax.axhline(0, color=p["muted"], linewidth=0.9, linestyle="--")

    x = df.index.values
    y = df["spread"].values
    ax.fill_between(x, y, 0, where=(y < 0), color=p["red"], alpha=0.35,
                    interpolate=True, linewidth=0)
    ax.fill_between(x, y, 0, where=(y >= 0), color=p["blue"], alpha=0.10,
                    interpolate=True, linewidth=0)
    ax.plot(x, y, color=p["blue"], linewidth=1.2)

    # Regime annotations
    idx = s["label_idx"]
    label_y_top = 3.05
    label_y_bot = -2.55
    for entry in REGIMES:
        date_s, lab_en, lab_hk, lab_tw, lab_cn, regime = entry
        d = pd.Timestamp(date_s)
        # find the value at that date for the arrow target
        nearest = df.index[df.index.searchsorted(d) - 1] if d > df.index[0] else df.index[0]
        spr = float(df.loc[nearest, "spread"])
        labels = (lab_en, lab_hk, lab_tw, lab_cn)
        text = labels[idx - 1]
        colour = p["red"] if regime == "bf" else p["green"]
        # alternate top/bottom by sign of spread to keep readable
        ytxt = label_y_top if spr <= 0 else label_y_bot
        ax.annotate(text, xy=(d, spr), xytext=(d, ytxt),
                    ha="center", fontsize=8.5, color=colour, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=colour, lw=0.9, alpha=0.7))

    ax.set_xlim(pd.Timestamp("1976-01-01"), pd.Timestamp("2026-05-01"))
    ax.set_ylim(-3.2, 3.6)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    from matplotlib.patches import Patch
    handles = [
        plt.Line2D([0], [0], color=p["blue"], linewidth=1.6, label=s["spread"]),
        Patch(facecolor=p["grey"], alpha=0.25, label=s["rec"]),
        plt.Line2D([0], [0], color=p["muted"], linestyle="--",
                   linewidth=1.0, label=s["zeroline"]),
        plt.Line2D([0], [0], color=p["red"], linewidth=0,
                   marker="s", markersize=8, label=s["bf"]),
        plt.Line2D([0], [0], color=p["green"], linewidth=0,
                   marker="s", markersize=8, label=s["bs"]),
    ]
    ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=9, ncol=2)

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
