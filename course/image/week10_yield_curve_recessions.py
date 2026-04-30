"""Week 10, §2.4 — 10y minus 2y Treasury spread with NBER recession shading.

FRED series T10Y2Y from 1976. NBER recession peaks/troughs are
hard-coded as constants per the post-1976 NBER Business Cycle
Dating Committee record.

Run:
    uv run python course/image/week10_yield_curve_recessions.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import fred_series  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week10_yield_curve_recessions"

# NBER recession dates, post-1976 (peak month, trough month).
NBER = [
    ("1980-01-01", "1980-07-01"),
    ("1981-07-01", "1982-11-01"),
    ("1990-07-01", "1991-03-01"),
    ("2001-03-01", "2001-11-01"),
    ("2007-12-01", "2009-06-01"),
    ("2020-02-01", "2020-04-01"),
]

LANG_STRINGS = {
    "en": {
        "title":    "10-year minus 2-year US Treasury spread, 1976 - April 2026",
        "subtitle": "Every NBER recession since 1980 was preceded by a yield-curve inversion. Shaded bands = NBER recessions.",
        "xlabel":   "Year",
        "ylabel":   "10y - 2y spread (percentage points)",
        "zeroline": "Zero (inversion threshold)",
        "spread":   "10y - 2y spread (FRED T10Y2Y)",
        "rec":      "NBER recession",
        "ann":      "Lead time from first inversion to NBER peak: typically 6-24 months",
    },
    "hk": {
        "title":    "美國 10 年期減 2 年期國債利差,1976 - 2026 年 4 月",
        "subtitle": "1980 年以來,每次 NBER 衰退之前都出現殖利率曲線倒掛。陰影=NBER 衰退期。",
        "xlabel":   "年份",
        "ylabel":   "10 年減 2 年利差(個百分點)",
        "zeroline": "零(倒掛門檻)",
        "spread":   "10 年減 2 年利差(FRED T10Y2Y)",
        "rec":      "NBER 衰退",
        "ann":      "從首次倒掛到 NBER 高峰的領先時間:通常 6-24 個月",
    },
    "tw": {
        "title":    "美國 10 年期減 2 年期公債利差,1976 - 2026 年 4 月",
        "subtitle": "1980 年以來,每次 NBER 衰退之前都出現殖利率曲線倒掛。陰影=NBER 衰退期。",
        "xlabel":   "年份",
        "ylabel":   "10 年減 2 年利差(個百分點)",
        "zeroline": "零(倒掛門檻)",
        "spread":   "10 年減 2 年利差(FRED T10Y2Y)",
        "rec":      "NBER 衰退",
        "ann":      "從首次倒掛到 NBER 高峰的領先時間:通常 6-24 個月",
    },
    "cn": {
        "title":    "美国 10 年期减 2 年期国债利差,1976 - 2026 年 4 月",
        "subtitle": "1980 年以来,每次 NBER 衰退之前都出现收益率曲线倒挂。阴影=NBER 衰退期。",
        "xlabel":   "年份",
        "ylabel":   "10 年减 2 年利差(个百分点)",
        "zeroline": "零(倒挂阈值)",
        "spread":   "10 年减 2 年利差(FRED T10Y2Y)",
        "rec":      "NBER 衰退",
        "ann":      "从首次倒挂到 NBER 高峰的领先时间:通常 6-24 个月",
    },
}


def _spread() -> pd.DataFrame:
    """Compose 10y-2y spread from FRED, falling back across series ids."""
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
    fig, ax = plt.subplots(figsize=(11, 5.6))
    style_axes(ax, p)

    # Recession bands first, behind the line
    for peak, trough in NBER:
        ax.axvspan(pd.Timestamp(peak), pd.Timestamp(trough),
                   color=p["grey"], alpha=0.18, linewidth=0)

    # Inversion threshold
    ax.axhline(0, color=p["muted"], linewidth=0.9, linestyle="--")

    # Spread line — colour positive vs negative segments differently
    x = df.index.values
    y = df["spread"].values
    ax.fill_between(x, y, 0, where=(y < 0), color=p["red"], alpha=0.35,
                    interpolate=True, linewidth=0)
    ax.fill_between(x, y, 0, where=(y >= 0), color=p["blue"], alpha=0.10,
                    interpolate=True, linewidth=0)
    ax.plot(x, y, color=p["blue"], linewidth=1.2, label=s["spread"])

    ax.set_xlim(pd.Timestamp("1976-01-01"), pd.Timestamp("2026-05-01"))
    ax.set_ylim(-3.0, 3.5)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Custom legend including recession band patch
    from matplotlib.patches import Patch
    handles = [
        plt.Line2D([0], [0], color=p["blue"], linewidth=1.6, label=s["spread"]),
        Patch(facecolor=p["grey"], alpha=0.25, label=s["rec"]),
        plt.Line2D([0], [0], color=p["muted"], linestyle="--",
                   linewidth=1.0, label=s["zeroline"]),
    ]
    ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=9)

    ax.text(0, -0.18, s["ann"], transform=ax.transAxes,
            fontsize=9, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
