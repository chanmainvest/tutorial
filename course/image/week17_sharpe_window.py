"""Week 17, §2.8 — Rolling 10-year Sharpe of the S&P 500.

Computes the rolling 10-year Sharpe ratio of the S&P 500 (total
return) over the 3-month T-Bill, on Damodaran's 1928-2024 annual
dataset. Highlights the regime swings between the 1970s
near-zero and the 2010s ~1.5.

Run:
    uv run python course/image/week17_sharpe_window.py
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
BASE = "week17_sharpe_window"

LANG_STRINGS = {
    "en": {
        "title":    "Rolling 10-year Sharpe ratio of the S&P 500",
        "subtitle": "Annual excess returns over 3-month T-Bills, Damodaran 1928-2024. The same asset reads anywhere from ~0 to ~1.5 depending on the window.",
        "xlabel":   "End year of 10-year window",
        "ylabel":   "Annualised Sharpe ratio",
        "label":    "10-year rolling Sharpe",
        "ann":      "Mean Sharpe across all windows: {m:.2f}  ·  range: {lo:.2f} to {hi:.2f}",
        "epoch_70s":  "1970s\nstagflation",
        "epoch_00s":  "2000s\ntwo crashes",
        "epoch_10s":  "2010s\nQE tailwind",
    },
    "hk": {
        "title":    "標普 500 滾動 10 年夏普比率",
        "subtitle": "對 3 個月國庫券的年度超額回報,Damodaran 1928-2024。同一資產隨窗口不同,讀數可由 ~0 到 ~1.5。",
        "xlabel":   "10 年窗口結束年份",
        "ylabel":   "年化夏普比率",
        "label":    "10 年滾動夏普",
        "ann":      "全部窗口平均夏普:{m:.2f}  ·  區間:{lo:.2f} 至 {hi:.2f}",
        "epoch_70s":  "1970 年代\n滯脹",
        "epoch_00s":  "2000 年代\n兩次崩盤",
        "epoch_10s":  "2010 年代\nQE 順風",
    },
    "tw": {
        "title":    "標普 500 滾動 10 年夏普比率",
        "subtitle": "對 3 個月國庫券的年度超額報酬,Damodaran 1928-2024。同一資產隨窗口不同,讀數可由 ~0 到 ~1.5。",
        "xlabel":   "10 年窗口結束年份",
        "ylabel":   "年化夏普比率",
        "label":    "10 年滾動夏普",
        "ann":      "全部窗口平均夏普:{m:.2f}  ·  區間:{lo:.2f} 至 {hi:.2f}",
        "epoch_70s":  "1970 年代\n停滯性通膨",
        "epoch_00s":  "2000 年代\n兩次崩盤",
        "epoch_10s":  "2010 年代\nQE 順風",
    },
    "cn": {
        "title":    "标普 500 滚动 10 年夏普比率",
        "subtitle": "对 3 个月国库券的年度超额回报,Damodaran 1928-2024。同一资产随窗口不同,读数可由 ~0 到 ~1.5。",
        "xlabel":   "10 年窗口结束年份",
        "ylabel":   "年化夏普比率",
        "label":    "10 年滚动夏普",
        "ann":      "全部窗口平均夏普:{m:.2f}  ·  区间:{lo:.2f} 至 {hi:.2f}",
        "epoch_70s":  "1970 年代\n滞胀",
        "epoch_00s":  "2000 年代\n两次崩盘",
        "epoch_10s":  "2010 年代\nQE 顺风",
    },
}


def _rolling_sharpe(window: int = 10) -> pd.Series:
    df = damodaran_annual_returns()
    excess = df["SP500"] - df["TBill3M"]
    out = {}
    arr = excess.values
    yrs = excess.index.values
    for i in range(window - 1, len(arr)):
        seg = arr[i - window + 1 : i + 1]
        m = seg.mean()
        s = seg.std(ddof=1)
        if s > 0:
            out[int(yrs[i])] = m / s
    return pd.Series(out)


def build_fig(s):
    sr = _rolling_sharpe(10)
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 5.6))
    style_axes(ax, p)

    ax.axhline(0, color=p["fg"], linewidth=0.8)
    ax.fill_between(sr.index, sr.values, 0,
                    where=(sr.values >= 0), color=p["accent"], alpha=0.18, linewidth=0)
    ax.fill_between(sr.index, sr.values, 0,
                    where=(sr.values < 0), color=p["red"], alpha=0.20, linewidth=0)
    ax.plot(sr.index, sr.values, color=p["accent"], linewidth=2.2, label=s["label"])

    # Highlight three regimes
    epoch_data = [
        (1979, sr.loc[1979] if 1979 in sr.index else 0.0, s["epoch_70s"], "down"),
        (2009, sr.loc[2009] if 2009 in sr.index else 0.0, s["epoch_00s"], "up"),
        (2019, sr.loc[2019] if 2019 in sr.index else 0.0, s["epoch_10s"], "up"),
    ]
    for yr, y, label, dirn in epoch_data:
        dy = -0.45 if dirn == "down" else 0.40
        va = "top" if dirn == "down" else "bottom"
        ax.annotate(
            label, xy=(yr, y), xytext=(yr, y + dy),
            fontsize=8.8, color=p["fg"], ha="center", va=va,
            arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.6),
        )

    mean_s = float(sr.mean())
    lo_s = float(sr.min())
    hi_s = float(sr.max())

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["ann"].format(m=mean_s, lo=lo_s, hi=hi_s),
            transform=ax.transAxes, fontsize=9, color=p["muted"])
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.set_ylim(min(-0.4, lo_s - 0.1), max(2.0, hi_s + 0.3))
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
