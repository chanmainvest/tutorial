"""Week 5, §2.7 — 10-year US Treasury yield, 1962 through 2026.

Long-run history of the 10-year constant-maturity yield via FRED's
DGS10 daily series, resampled to month-end. Annotates the 1981
Volcker peak, the 2020 COVID trough, and the most recent reading.

Run:
    uv run python course/image/week05_yield_history.py
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
BASE = "week05_yield_history"

LANG_STRINGS = {
    "en": {
        "title":    "10-year US Treasury yield, 1962-2026",
        "subtitle": "FRED DGS10, month-end. The 1981 peak under Volcker, the 40-year decline through 2020, and the post-COVID rise.",
        "xlabel":   "Year",
        "ylabel":   "Yield (% annual)",
        "peak":     "1981 peak\n{v:.1f}% (Volcker)",
        "trough":   "2020 trough\n{v:.1f}% (COVID)",
        "now":      "Apr 2026\n{v:.1f}%",
        "regime1":  "Inflation rising\n1962-1981",
        "regime2":  "40-year bond bull\n1981-2020",
        "regime3":  "2022+ break",
    },
    "hk": {
        "title":    "十年期美國國債孳息率,1962-2026",
        "subtitle": "FRED DGS10 月底數據。1981 年沃爾克高峰,40 年下行至 2020 年,COVID 後反彈。",
        "xlabel":   "年份",
        "ylabel":   "孳息率(年化 %)",
        "peak":     "1981 年高峰\n{v:.1f}%(沃爾克)",
        "trough":   "2020 年低谷\n{v:.1f}%(COVID)",
        "now":      "2026 年 4 月\n{v:.1f}%",
        "regime1":  "通脹上行\n1962-1981",
        "regime2":  "四十年債券大牛\n1981-2020",
        "regime3":  "2022 後斷裂",
    },
    "tw": {
        "title":    "十年期美國公債殖利率,1962-2026",
        "subtitle": "FRED DGS10 月底資料。1981 年伏克爾高峰、40 年下行至 2020 年、COVID 後反彈。",
        "xlabel":   "年份",
        "ylabel":   "殖利率(年化 %)",
        "peak":     "1981 年高峰\n{v:.1f}%(伏克爾)",
        "trough":   "2020 年低谷\n{v:.1f}%(COVID)",
        "now":      "2026 年 4 月\n{v:.1f}%",
        "regime1":  "通膨上行\n1962-1981",
        "regime2":  "四十年公債大多頭\n1981-2020",
        "regime3":  "2022 後斷裂",
    },
    "cn": {
        "title":    "十年期美国国债收益率,1962-2026",
        "subtitle": "FRED DGS10 月末数据。1981 年沃尔克高峰、40 年下行至 2020 年、COVID 后反弹。",
        "xlabel":   "年份",
        "ylabel":   "收益率(年化 %)",
        "peak":     "1981 年高峰\n{v:.1f}%(沃尔克)",
        "trough":   "2020 年低谷\n{v:.1f}%(COVID)",
        "now":      "2026 年 4 月\n{v:.1f}%",
        "regime1":  "通胀上行\n1962-1981",
        "regime2":  "四十年债券大牛\n1981-2020",
        "regime3":  "2022 后断裂",
    },
}


def _load() -> pd.Series:
    df = fred_series("DGS10", start="1962-01-01")
    s = df.iloc[:, 0].dropna().astype(float)
    s.index = pd.to_datetime(s.index)
    s = s.resample("ME").last().dropna()
    return s


def build_fig(s):
    series = _load()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.4, 5.8))
    style_axes(ax, p)

    ax.plot(series.index, series.values, color=p["blue"], linewidth=1.6)
    ax.fill_between(series.index, 0, series.values, color=p["blue"], alpha=0.08)

    # Find peak (around 1981) and trough (around 2020)
    peak_idx = series["1980":"1982"].idxmax()
    peak_v = series.loc[peak_idx]
    trough_idx = series["2020":"2020"].idxmin()
    trough_v = series.loc[trough_idx]
    last_idx = series.index[-1]
    last_v = float(series.iloc[-1])

    # Annotate peak
    ax.annotate(s["peak"].format(v=peak_v),
                xy=(peak_idx, peak_v), xytext=(peak_idx, peak_v + 2.5),
                ha="center", fontsize=9, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.2))
    # Annotate trough
    ax.annotate(s["trough"].format(v=trough_v),
                xy=(trough_idx, trough_v), xytext=(trough_idx, trough_v - 2.6),
                ha="center", fontsize=9, color=p["green"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=1.2))
    # Annotate current
    ax.annotate(s["now"].format(v=last_v),
                xy=(last_idx, last_v), xytext=(last_idx, last_v + 2.0),
                ha="right", fontsize=9, color=p["accent"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.2))

    # Regime band labels at top
    ax.text(pd.Timestamp("1971-06-01"), 17.2, s["regime1"],
            ha="center", fontsize=8.5, color=p["muted"])
    ax.text(pd.Timestamp("2000-06-01"), 17.2, s["regime2"],
            ha="center", fontsize=8.5, color=p["muted"])
    ax.text(pd.Timestamp("2023-06-01"), 17.2, s["regime3"],
            ha="center", fontsize=8.5, color=p["muted"])
    # Regime divider lines
    for d in (pd.Timestamp("1981-09-01"), pd.Timestamp("2020-08-01")):
        ax.axvline(d, color=p["muted"], linestyle=":", linewidth=0.8, alpha=0.7)

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, 18.5)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
