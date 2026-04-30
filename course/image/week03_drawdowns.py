"""Week 3, §2.5 — S&P 500 drawdown chart, 1950 onward.

Uses monthly S&P 500 Total Return (^SP500TR) where available; falls
back to ^GSPC price index when not. Computes peak-to-trough drawdown
on the running maximum and plots the underwater curve.

Run:
    uv run python course/image/week03_drawdowns.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import yahoo_history  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week03_drawdowns"

LANG_STRINGS = {
    "en": {
        "title":    "S&P 500 drawdown from prior peak, 1985-2026",
        "subtitle": "Monthly close on Yahoo Finance ^GSPC. Each shaded trough is a major bear market; recovery times vary by an order of magnitude.",
        "xlabel":   "Year",
        "ylabel":   "Drawdown from prior all-time high",
        "annot":    {
            "1987-10-01": "1987\nBlack Monday\n-34%",
            "2002-09-01": "2000-02\ndot-com\n-49%",
            "2009-02-01": "2007-09\nGFC\n-55%",
            "2020-03-01": "2020\nCOVID\n-34%",
            "2022-09-01": "2022\nselloff\n-25%",
        },
    },
    "hk": {
        "title":    "標普 500 自前高回撚，1985-2026",
        "subtitle": "Yahoo Finance ^GSPC 月度收盤。每個陰影低谷是一次主要熊市，復元時間相差一個量級。",
        "xlabel":   "年份",
        "ylabel":   "自歷史新高的回撚",
        "annot":    {
            "1987-10-01": "1987\n黑色星期一\n-34%",
            "2002-09-01": "2000-02\n科網泡沫\n-49%",
            "2009-02-01": "2007-09\n金融海嘯\n-55%",
            "2020-03-01": "2020\n新冠\n-34%",
            "2022-09-01": "2022\n回調\n-25%",
        },
    },
    "tw": {
        "title":    "標普 500 自前高回檔，1985-2026",
        "subtitle": "Yahoo Finance ^GSPC 月度收盤。每個陰影低谷是一次主要熊市，復原時間相差一個量級。",
        "xlabel":   "年份",
        "ylabel":   "自歷史新高的回檔",
        "annot":    {
            "1987-10-01": "1987\n黑色星期一\n-34%",
            "2002-09-01": "2000-02\n網路泡沫\n-49%",
            "2009-02-01": "2007-09\n金融海嘯\n-55%",
            "2020-03-01": "2020\n新冠\n-34%",
            "2022-09-01": "2022\n回檔\n-25%",
        },
    },
    "cn": {
        "title":    "标普 500 自前高回撚，1985-2026",
        "subtitle": "Yahoo Finance ^GSPC 月度收盘。每个阴影低谷是一次主要熊市，复元时间相差一个量级。",
        "xlabel":   "年份",
        "ylabel":   "自历史新高的回撚",
        "annot":    {
            "1987-10-01": "1987\n黑色星期一\n-34%",
            "2002-09-01": "2000-02\n互联网泡沫\n-49%",
            "2009-02-01": "2007-09\n金融海啸\n-55%",
            "2020-03-01": "2020\n新冠\n-34%",
            "2022-09-01": "2022\n回调\n-25%",
        },
    },
}


def _drawdown_series() -> pd.Series:
    df = yahoo_history("^GSPC", start="1950-01-01", interval="1mo")
    px = df["AdjClose"].dropna()
    peak = px.cummax()
    dd = px / peak - 1.0
    return dd


def build_fig(s):
    dd = _drawdown_series()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 5.6))
    style_axes(ax, p)

    ax.fill_between(dd.index, dd.values, 0, where=(dd.values < 0),
                    color=p["red"], alpha=0.35, linewidth=0)
    ax.plot(dd.index, dd.values, color=p["red"], linewidth=1.0)
    ax.axhline(0, color=p["fg"], linewidth=0.8)

    # Annotations at major troughs
    for date_str, label in s["annot"].items():
        d = pd.Timestamp(date_str)
        if d in dd.index:
            y = float(dd.loc[d])
        else:
            # nearest within ±90 days
            nearest = dd.index[dd.index.get_indexer([d], method="nearest")[0]]
            y = float(dd.loc[nearest])
            d = nearest
        ax.annotate(
            label, xy=(d, y), xytext=(d, y - 0.10),
            fontsize=8.5, color=p["fg"], ha="center", va="top",
            arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.6),
        )

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_ylim(-0.75, 0.05)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
