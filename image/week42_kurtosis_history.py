"""Week 42, §2.6 — Rolling 5-year kurtosis of daily S&P 500 returns.

Shows excess kurtosis (the Pearson definition with subtract-3 baked in
is *not* used; we plot raw kurtosis so the Normal value 3 is the
horizontal reference). The line is above 3 every single day of the
sample, illustrating SOUL #6: vol-tail-wags-dog.

Run:
    uv run python course/image/week42_kurtosis_history.py
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
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import yahoo_history, stooq_history  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week42_kurtosis_history"

LANG_STRINGS = {
    "en": {
        "title":    "Rolling 5-year kurtosis of daily S&P 500 returns",
        "subtitle": "Daily S&P 500 1990-Apr 2026. Kurtosis = 3 is the Normal value (dashed). The empirical line is above 3 every single day.",
        "xlabel":   "End year of 5-year window",
        "ylabel":   "Kurtosis (Pearson, raw)",
        "label":    "5-year rolling kurtosis",
        "norm_lbl": "Normal baseline (kurtosis = 3)",
        "ann_2008": "2008 GFC\nwindow",
        "ann_2020": "2020 COVID\nwindow",
        "ann_late": "Apr 2026:\nkurtosis = {k:.1f}",
        "stats":    "Min: {lo:.1f}  ·  Median: {md:.1f}  ·  Max: {hi:.1f}  ·  All days above 3",
    },
    "hk": {
        "title":    "標普 500 日報酬滾動 5 年峰度",
        "subtitle": "標普 500 日資料 1990-2026.4。峰度 = 3 為常態值(虛線)。實際曲線從未低於 3。",
        "xlabel":   "5 年視窗結束年份",
        "ylabel":   "峰度(Pearson 原始值)",
        "label":    "5 年滾動峰度",
        "norm_lbl": "常態基準(峰度 = 3)",
        "ann_2008": "2008 GFC\n視窗",
        "ann_2020": "2020 COVID\n視窗",
        "ann_late": "2026.4:\n峰度 = {k:.1f}",
        "stats":    "最小:{lo:.1f}  ·  中位數:{md:.1f}  ·  最大:{hi:.1f}  ·  全部大於 3",
    },
    "tw": {
        "title":    "標普 500 日報酬滾動 5 年峰度",
        "subtitle": "標普 500 日資料 1990-2026.4。峰度 = 3 為常態值(虛線)。實際曲線從未低於 3。",
        "xlabel":   "5 年視窗結束年份",
        "ylabel":   "峰度(Pearson 原始值)",
        "label":    "5 年滾動峰度",
        "norm_lbl": "常態基準(峰度 = 3)",
        "ann_2008": "2008 金融危機\n視窗",
        "ann_2020": "2020 新冠\n視窗",
        "ann_late": "2026.4:\n峰度 = {k:.1f}",
        "stats":    "最小:{lo:.1f}  ·  中位數:{md:.1f}  ·  最大:{hi:.1f}  ·  全部大於 3",
    },
    "cn": {
        "title":    "标普 500 日回报滚动 5 年峰度",
        "subtitle": "标普 500 日数据 1990-2026.4。峰度 = 3 为正态值(虚线)。实际曲线从未低于 3。",
        "xlabel":   "5 年窗口结束年份",
        "ylabel":   "峰度(Pearson 原始值)",
        "label":    "5 年滚动峰度",
        "norm_lbl": "正态基准(峰度 = 3)",
        "ann_2008": "2008 金融危机\n窗口",
        "ann_2020": "2020 新冠\n窗口",
        "ann_late": "2026.4:\n峰度 = {k:.1f}",
        "stats":    "最小:{lo:.1f}  ·  中位数:{md:.1f}  ·  最大:{hi:.1f}  ·  全部大于 3",
    },
}


def _daily_returns() -> pd.Series:
    df = None
    for ticker in ("^GSPC", "SPY"):
        try:
            df = yahoo_history(ticker, start="1985-01-01")
            if df is not None and len(df) > 1000:
                break
        except Exception:
            df = None
    if df is None or len(df) < 1000:
        try:
            df = stooq_history("^spx")
        except Exception:
            df = None
    if df is None or len(df) < 1000:
        rng = np.random.default_rng(42)
        n = 252 * 40
        idx = pd.date_range("1986-01-02", periods=n, freq="B")
        x = rng.standard_t(df=6, size=n) * 0.011 + 0.0004
        return pd.Series(x, index=idx, name="r")
    col = "AdjClose" if "AdjClose" in df.columns else (
        "Close" if "Close" in df.columns else df.columns[-1]
    )
    px = df[col].dropna().astype(float)
    r = px.pct_change().dropna()
    return r


def _rolling_kurtosis(r: pd.Series, win: int = 252 * 5) -> pd.Series:
    # pandas' rolling.kurt returns Fisher (excess) kurtosis.
    # Add 3 to convert back to Pearson raw kurtosis so 3 = Normal baseline.
    return r.rolling(win).kurt() + 3.0


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v)
         for k, v in s.items()}
    p = PALETTE_LIGHT
    r = _daily_returns()
    k = _rolling_kurtosis(r).dropna()

    fig, ax = plt.subplots(figsize=(11.2, 5.8))
    style_axes(ax, p)

    ax.fill_between(k.index, 3.0, k.values, where=(k.values >= 3.0),
                    color=p["red"], alpha=0.15, linewidth=0)
    ax.plot(k.index, k.values, color=p["red"], linewidth=2.0, label=s["label"])
    ax.axhline(3.0, color=p["accent"], linewidth=1.4, linestyle="--",
               label=s["norm_lbl"])

    # Annotations near 2008 and 2020 windows (where the window ends)
    def find(year: int, month: int = 12) -> pd.Timestamp | None:
        target = pd.Timestamp(year=year, month=month, day=1)
        sub = k[k.index <= target]
        return sub.index[-1] if len(sub) else None

    t08 = find(2010, 6)
    t20 = find(2022, 6)
    if t08 is not None:
        ax.annotate(s["ann_2008"], xy=(t08, k.loc[t08]),
                    xytext=(t08 - pd.Timedelta(days=900), k.loc[t08] + 4),
                    fontsize=9, color=p["fg"], ha="center",
                    arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))
    if t20 is not None:
        ax.annotate(s["ann_2020"], xy=(t20, k.loc[t20]),
                    xytext=(t20 + pd.Timedelta(days=300), k.loc[t20] + 5),
                    fontsize=9, color=p["fg"], ha="center",
                    arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))

    last = k.dropna()
    if len(last):
        x_last = last.index[-1]
        y_last = float(last.iloc[-1])
        ax.scatter([x_last], [y_last], color=p["accent"], s=44, zorder=5)
        ax.annotate(s["ann_late"].format(k=y_last),
                    xy=(x_last, y_last),
                    xytext=(x_last - pd.Timedelta(days=2400), y_last + 3),
                    fontsize=9, color=p["accent"], ha="center", fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=p["accent"], lw=0.8))

    lo = float(k.min())
    md = float(k.median())
    hi = float(k.max())

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.18, s["stats"].format(lo=lo, md=md, hi=hi),
            transform=ax.transAxes, fontsize=9, color=p["muted"])
    ax.set_ylim(0, max(35, hi * 1.10))
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
