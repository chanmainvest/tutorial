"""Side 16, sec 1 -- S&P 500 drawdown chart 1928-Apr 2026.

Combines Damodaran annual SP500 total returns (1928-1984) with monthly
Yahoo ^GSPC adjusted closes (1985-Apr 2026) to produce a continuous
wealth index, then plots the percentage below running peak (drawdown).
Each major bear is annotated with its depth and duration.

Run:
    uv run python course/image/side16_century_drawdowns.py
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
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)
from scripts.market_data import damodaran_annual_returns, yahoo_history  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side16_century_drawdowns"


# Curated bear-market annotations. (date_at_trough, depth_pct, label).
BEARS = [
    ("1932-06-01", -86, "1929-32\n-86%, 34mo"),
    ("1942-04-01", -49, "1937-42\n-49%, 60mo"),
    ("1974-10-01", -48, "1973-74\n-48%, 21mo"),
    ("1987-12-01", -34, "1987\n-34%, 20mo"),
    ("2002-10-01", -49, "2000-02\n-49%, 85mo"),
    ("2009-03-01", -57, "2007-09\n-57%, 49mo"),
    ("2020-03-01", -34, "2020\n-34%, 5mo"),
    ("2022-10-01", -25, "2022\n-25%, 21mo"),
]


LANG_STRINGS = {
    "en": {
        "title":    "S&P 500 drawdown, 1928 - April 2026",
        "subtitle": "Percentage below running peak. Annual returns pre-1985 (Damodaran), monthly closes 1985+. Eight bears of -20% or worse.",
        "xlabel":   "Year",
        "ylabel":   "Drawdown from peak (%)",
        "footer":   "Sources: Damodaran annual SP500 total returns 1928-1984; Yahoo Finance ^GSPC monthly adjusted close 1985-Apr 2026. Pre-1985 drawdowns at annual resolution -- intra-year troughs may be deeper than shown.",
        "bears":    [b[2] for b in BEARS],
    },
    "hk": {
        "title":    "標普 500 跌幅,1928 - 2026 年 4 月",
        "subtitle": "較高位回落百分比。1985 年前年度數據(Damodaran),1985 年起月度收市。八次 -20% 或以上熊市。",
        "xlabel":   "年份",
        "ylabel":   "由高位跌幅 (%)",
        "footer":   "資料:Damodaran 年度標普 500 總回報 1928-1984;Yahoo Finance ^GSPC 月度調整收市 1985-2026 年 4 月。1985 年前為年度解像度,年內谷底可能較圖中更深。",
        "bears":    ["1929-32\n-86%、34月", "1937-42\n-49%、60月", "1973-74\n-48%、21月",
                     "1987\n-34%、20月", "2000-02\n-49%、85月", "2007-09\n-57%、49月",
                     "2020\n-34%、5月", "2022\n-25%、21月"],
    },
    "tw": {
        "title":    "標普 500 跌幅,1928 - 2026 年 4 月",
        "subtitle": "較高點回落百分比。1985 年前年度數據(Damodaran),1985 年起月度收盤。八次 -20% 以上空頭。",
        "xlabel":   "年份",
        "ylabel":   "自高點跌幅 (%)",
        "footer":   "資料:Damodaran 年度標普 500 總報酬 1928-1984;Yahoo Finance ^GSPC 月度調整收盤 1985-2026 年 4 月。1985 年前為年度解析度,年內谷底可能較圖中更深。",
        "bears":    ["1929-32\n-86%、34月", "1937-42\n-49%、60月", "1973-74\n-48%、21月",
                     "1987\n-34%、20月", "2000-02\n-49%、85月", "2007-09\n-57%、49月",
                     "2020\n-34%、5月", "2022\n-25%、21月"],
    },
    "cn": {
        "title":    "标普 500 回撤,1928 - 2026 年 4 月",
        "subtitle": "较高点回落百分比。1985 年前年度数据(Damodaran),1985 年起月度收盘。八次 -20% 或更深熊市。",
        "xlabel":   "年份",
        "ylabel":   "自高点回撤 (%)",
        "footer":   "数据:Damodaran 年度标普 500 总回报 1928-1984;Yahoo Finance ^GSPC 月度调整收盘 1985-2026 年 4 月。1985 年前为年度精度,年内谷底可能比图中更深。",
        "bears":    ["1929-32\n-86%、34月", "1937-42\n-49%、60月", "1973-74\n-48%、21月",
                     "1987\n-34%、20月", "2000-02\n-49%、85月", "2007-09\n-57%、49月",
                     "2020\n-34%、5月", "2022\n-25%、21月"],
    },
}


def _wealth_index() -> pd.Series:
    # Pre-1985 from Damodaran annual returns.
    dam = damodaran_annual_returns()
    early_idx = []
    early_val = []
    w = 1.0
    early_idx.append(pd.Timestamp("1927-12-31"))
    early_val.append(w)
    for year in range(1928, 1985):
        if year not in dam.index:
            continue
        r = float(dam.loc[year, "SP500"])
        w = w * (1.0 + r)
        early_idx.append(pd.Timestamp(year=year, month=12, day=31))
        early_val.append(w)
    early = pd.Series(early_val, index=pd.DatetimeIndex(early_idx))

    # Monthly Yahoo from 1985.
    df = yahoo_history("^GSPC", start="1984-12-01", interval="1mo")
    px = df["AdjClose"].dropna()
    px.index = pd.to_datetime(px.index).to_period("M").to_timestamp("M")
    px = px[~px.index.duplicated(keep="last")].sort_index()
    px = px[px.index >= pd.Timestamp("1985-01-01")]

    # Splice: scale Yahoo so first point matches the 1984 year-end Damodaran.
    if len(px) > 0:
        scale = early.iloc[-1] / px.iloc[0]
        late = px * scale
    else:
        late = px

    return pd.concat([early, late]).sort_index()


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT
    w = _wealth_index()
    peak = w.cummax()
    dd = (w / peak - 1.0) * 100.0  # in percent

    fig, ax = plt.subplots(figsize=(12.0, 6.4), dpi=150)
    style_axes(ax, p)

    x = dd.index.values
    y = dd.values
    ax.fill_between(x, y, 0, color=p["red"], alpha=0.35, linewidth=0)
    ax.plot(x, y, color=p["red"], linewidth=1.0)

    # Reference horizontal lines.
    for thr, lbl in [(-10, "-10%"), (-20, "-20%"), (-40, "-40%")]:
        ax.axhline(thr, color=p["muted"], linewidth=0.6, linestyle=":", alpha=0.7)
        ax.text(pd.Timestamp("1928-01-01"), thr + 1.0, lbl, color=p["muted"],
                fontsize=8, ha="left")

    # Bear annotations.
    bears = list(zip([pd.Timestamp(b[0]) for b in BEARS],
                     [b[1] for b in BEARS],
                     s["bears"]))
    # Stagger annotation y positions to avoid overlap.
    y_offsets = [-95, -65, -78, -55, -78, -78, -50, -42]
    for (xt, depth, label), yoff in zip(bears, y_offsets):
        ax.annotate(
            label,
            xy=(xt, depth),
            xytext=(xt, yoff),
            ha="center", va="top",
            fontsize=8.4, color=p["fg"], fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.6),
            bbox=dict(boxstyle="round,pad=0.25", facecolor=p["bg"],
                      edgecolor=p["muted"], linewidth=0.5, alpha=0.92),
        )

    ax.set_xlim(pd.Timestamp("1928-01-01"), pd.Timestamp("2026-06-01"))
    ax.set_ylim(-100, 5)
    ax.xaxis.set_major_locator(mdates.YearLocator(10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{int(v)}%"))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold", loc="left")
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
