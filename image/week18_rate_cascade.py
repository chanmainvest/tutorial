"""Week 18, §2.1 — The interest-rate cascade, 1990 through April 2026.

Four FRED series on one chart: Fed funds (FEDFUNDS), 10-year Treasury
(DGS10), 30-year mortgage (MORTGAGE30US), and BAA corporate yield (BAA).
The Fed sets the bottom; the market sets the top three. Spreads widen in
2008-09 and 2020 stress and during the 2022-2024 hiking cycle.

Run:
    uv run python course/image/week18_rate_cascade.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import fred_series  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week18_rate_cascade"

LANG_STRINGS = {
    "en": {
        "title":    "The interest-rate cascade, 1990-2026",
        "subtitle": "The Fed sets the floor (FEDFUNDS). The market sets everything above it. Stress widens the spread between BAA corporates and Treasuries.",
        "xlabel":   "Year",
        "ylabel":   "Yield (% annual)",
        "fed":      "Fed funds (FEDFUNDS)",
        "ust":      "10-year Treasury (DGS10)",
        "mort":     "30-year mortgage (MORTGAGE30US)",
        "baa":      "BAA corporate (BAA)",
        "ann_2008": "2008-09\ncredit shock",
        "ann_2020": "2020\nCOVID",
        "ann_2022": "2022-24\nhiking cycle",
        "ann_zlb":  "Zero-bound\n2009-15, 2020-22",
    },
    "hk": {
        "title":    "利率瀑布,1990-2026",
        "subtitle": "聯儲訂下底線(FEDFUNDS),市場訂下其餘。壓力時期 BAA 公司債與國債的息差擴闊。",
        "xlabel":   "年份",
        "ylabel":   "孳息率(年化 %)",
        "fed":      "聯邦基金利率(FEDFUNDS)",
        "ust":      "十年期美國國債(DGS10)",
        "mort":     "三十年按揭(MORTGAGE30US)",
        "baa":      "BAA 公司債(BAA)",
        "ann_2008": "2008-09\n信貸震盪",
        "ann_2020": "2020\nCOVID",
        "ann_2022": "2022-24\n加息周期",
        "ann_zlb":  "零利率下限\n2009-15、2020-22",
    },
    "tw": {
        "title":    "利率瀑布,1990-2026",
        "subtitle": "聯準會訂下底線(FEDFUNDS),市場訂下其餘。壓力時期 BAA 公司債與公債的利差擴大。",
        "xlabel":   "年份",
        "ylabel":   "殖利率(年化 %)",
        "fed":      "聯邦資金利率(FEDFUNDS)",
        "ust":      "十年期美國公債(DGS10)",
        "mort":     "三十年房貸(MORTGAGE30US)",
        "baa":      "BAA 公司債(BAA)",
        "ann_2008": "2008-09\n信用震盪",
        "ann_2020": "2020\nCOVID",
        "ann_2022": "2022-24\n升息循環",
        "ann_zlb":  "零利率下限\n2009-15、2020-22",
    },
    "cn": {
        "title":    "利率瀑布,1990-2026",
        "subtitle": "美联储设定底线(FEDFUNDS),市场设定其余。压力时期 BAA 公司债与国债的息差扩大。",
        "xlabel":   "年份",
        "ylabel":   "收益率(年化 %)",
        "fed":      "联邦基金利率(FEDFUNDS)",
        "ust":      "十年期美国国债(DGS10)",
        "mort":     "三十年按揭(MORTGAGE30US)",
        "baa":      "BAA 公司债(BAA)",
        "ann_2008": "2008-09\n信贷冲击",
        "ann_2020": "2020\nCOVID",
        "ann_2022": "2022-24\n加息周期",
        "ann_zlb":  "零利率下限\n2009-15、2020-22",
    },
}


def _load() -> dict[str, pd.Series]:
    out: dict[str, pd.Series] = {}
    for sid in ("FEDFUNDS", "DGS10", "MORTGAGE30US", "BAA"):
        df = fred_series(sid, start="1990-01-01")
        s = df.iloc[:, 0].dropna().astype(float)
        s.index = pd.to_datetime(s.index)
        s = s.resample("ME").last().dropna()
        s = s[s.index >= "1990-01-01"]
        s = s[s.index <= "2026-04-30"]
        out[sid] = s
    return out


def build_fig(s):
    series = _load()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.2))
    style_axes(ax, p)

    ax.plot(series["BAA"].index, series["BAA"].values,
            color=p["red"], linewidth=1.8, label=s["baa"])
    ax.plot(series["MORTGAGE30US"].index, series["MORTGAGE30US"].values,
            color=p["orange"], linewidth=1.6, label=s["mort"])
    ax.plot(series["DGS10"].index, series["DGS10"].values,
            color=p["blue"], linewidth=1.6, label=s["ust"])
    ax.plot(series["FEDFUNDS"].index, series["FEDFUNDS"].values,
            color=p["green"], linewidth=1.6, label=s["fed"])

    # Stress shading
    for d0, d1 in (("2008-09-01", "2009-06-01"), ("2020-02-01", "2020-06-01")):
        ax.axvspan(pd.Timestamp(d0), pd.Timestamp(d1),
                   color=p["muted"], alpha=0.10)

    # Hiking-cycle shading
    ax.axvspan(pd.Timestamp("2022-03-01"), pd.Timestamp("2024-09-01"),
               color=p["accent"], alpha=0.07)

    ax.text(pd.Timestamp("2008-12-01"), 1.05, s["ann_2008"],
            ha="center", fontsize=8.5, color=p["muted"])
    ax.text(pd.Timestamp("2020-04-01"), 1.05, s["ann_2020"],
            ha="center", fontsize=8.5, color=p["muted"])
    ax.text(pd.Timestamp("2023-06-01"), 1.05, s["ann_2022"],
            ha="center", fontsize=8.5, color=p["muted"])

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, 12.5)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
