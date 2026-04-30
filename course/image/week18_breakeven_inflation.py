"""Week 18, §2.3 — 10-year breakeven inflation, 2003 through April 2026.

The breakeven is the 10-year nominal Treasury yield minus the 10-year
TIPS yield (FRED publishes the difference directly as T10YIE). It is
the market's daily, mark-to-market forecast of average CPI over the
next ten years. Annotates the 2008 deflation scare, the 2022 inflation
peak, and the most recent print.

Run:
    uv run python course/image/week18_breakeven_inflation.py
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
from scripts.market_data import fred_series  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week18_breakeven_inflation"

LANG_STRINGS = {
    "en": {
        "title":    "10-year breakeven inflation, 2003-2026",
        "subtitle": "FRED T10YIE = nominal 10y Treasury minus 10y TIPS yield. The market's mark-to-market guess at average CPI for the next decade.",
        "xlabel":   "Year",
        "ylabel":   "Breakeven (% annual)",
        "label":    "10y breakeven",
        "fed_target": "Fed 2% target",
        "ann_2008": "2008 deflation scare\n{v:.2f}%",
        "ann_2022": "2022 inflation peak\n{v:.2f}%",
        "ann_now":  "Apr 2026\n{v:.2f}%",
    },
    "hk": {
        "title":    "十年期通脹預期(盈虧平衡通脹率),2003-2026",
        "subtitle": "FRED T10YIE = 名義十年期國債息率減去十年期 TIPS 息率。市場每日重估的未來十年平均 CPI 預期。",
        "xlabel":   "年份",
        "ylabel":   "通脹預期(年化 %)",
        "label":    "十年期通脹預期",
        "fed_target": "聯儲 2% 目標",
        "ann_2008": "2008 通縮恐慌\n{v:.2f}%",
        "ann_2022": "2022 通脹高峰\n{v:.2f}%",
        "ann_now":  "2026 年 4 月\n{v:.2f}%",
    },
    "tw": {
        "title":    "十年期通膨預期(平衡通膨率),2003-2026",
        "subtitle": "FRED T10YIE = 名目十年期公債殖利率減去十年期 TIPS 殖利率。市場每日重估的未來十年平均 CPI 預期。",
        "xlabel":   "年份",
        "ylabel":   "通膨預期(年化 %)",
        "label":    "十年期通膨預期",
        "fed_target": "聯準會 2% 目標",
        "ann_2008": "2008 通縮恐慌\n{v:.2f}%",
        "ann_2022": "2022 通膨高峰\n{v:.2f}%",
        "ann_now":  "2026 年 4 月\n{v:.2f}%",
    },
    "cn": {
        "title":    "十年期通胀预期(盈亏平衡通胀率),2003-2026",
        "subtitle": "FRED T10YIE = 名义十年期国债收益率减去十年期 TIPS 收益率。市场每日重估的未来十年平均 CPI 预期。",
        "xlabel":   "年份",
        "ylabel":   "通胀预期(年化 %)",
        "label":    "十年期通胀预期",
        "fed_target": "美联储 2% 目标",
        "ann_2008": "2008 通缩恐慌\n{v:.2f}%",
        "ann_2022": "2022 通胀高峰\n{v:.2f}%",
        "ann_now":  "2026 年 4 月\n{v:.2f}%",
    },
}


def _load() -> pd.Series:
    df = fred_series("T10YIE", start="2003-01-01")
    s = df.iloc[:, 0].dropna().astype(float)
    s.index = pd.to_datetime(s.index)
    s = s.resample("W").last().dropna()
    s = s[s.index <= "2026-04-30"]
    return s


def build_fig(s):
    series = _load()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.6, 5.8))
    style_axes(ax, p)

    ax.plot(series.index, series.values,
            color=p["blue"], linewidth=1.6, label=s["label"])
    ax.fill_between(series.index, 2.0, series.values,
                    where=(series.values >= 2.0),
                    color=p["red"], alpha=0.10, interpolate=True)
    ax.fill_between(series.index, 2.0, series.values,
                    where=(series.values < 2.0),
                    color=p["green"], alpha=0.10, interpolate=True)

    # Fed 2% target
    ax.axhline(2.0, color=p["accent"], linewidth=1.0, linestyle="--", alpha=0.8)
    ax.text(series.index[5], 2.05, s["fed_target"],
            fontsize=9, color=p["accent"])

    # 2008 deflation trough (Nov 2008)
    win = series["2008-09":"2009-02"]
    t08 = win.idxmin()
    v08 = float(win.min())
    ax.annotate(s["ann_2008"].format(v=v08),
                xy=(t08, v08), xytext=(pd.Timestamp("2010-06-01"), -0.4),
                ha="left", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.2))

    # 2022 inflation peak
    win22 = series["2022-01":"2022-12"]
    t22 = win22.idxmax()
    v22 = float(win22.max())
    ax.annotate(s["ann_2022"].format(v=v22),
                xy=(t22, v22), xytext=(pd.Timestamp("2018-06-01"), 3.4),
                ha="left", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.2))

    # Now
    last_t = series.index[-1]
    last_v = float(series.iloc[-1])
    ax.annotate(s["ann_now"].format(v=last_v),
                xy=(last_t, last_v),
                xytext=(last_t - pd.Timedelta(days=900), last_v + 1.0),
                ha="left", fontsize=9, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.2))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(-1.0, 4.2)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
