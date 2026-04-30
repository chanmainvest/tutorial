"""Week 3, §2.7 — Range of annualised real returns by holding period.

Uses the embedded Damodaran annual dataset. For each holding length
in {1, 5, 10, 20, 30} years, computes every rolling-window annualised
*real* return (S&P 500 total return less CPI), then plots min, max,
median, and 10/90th percentiles.

Run:
    uv run python course/image/week03_holding_periods.py
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
BASE = "week03_holding_periods"

LANG_STRINGS = {
    "en": {
        "title":    "Range of rolling annualised real returns by holding period",
        "subtitle": "S&P 500 total return less CPI, 1928-2024 (Damodaran). Time crushes the range, not the cumulative dollar consequence.",
        "xlabel":   "Holding period (years)",
        "ylabel":   "Annualised real return",
        "lbl_max":  "Best window",
        "lbl_min":  "Worst window",
        "lbl_band": "10th-90th percentile",
        "lbl_med":  "Median",
    },
    "hk": {
        "title":    "按持有期分組的滾動年化實質回報區間",
        "subtitle": "標普 500 總回報減 CPI,1928-2024(Damodaran)。時間壓縮的是區間,不是累積金額的差距。",
        "xlabel":   "持有期(年)",
        "ylabel":   "年化實質回報",
        "lbl_max":  "最佳窗口",
        "lbl_min":  "最差窗口",
        "lbl_band": "10-90 百分位區間",
        "lbl_med":  "中位數",
    },
    "tw": {
        "title":    "依持有期分組的滾動年化實質報酬區間",
        "subtitle": "標普 500 總報酬減 CPI,1928-2024(Damodaran)。時間壓縮的是區間,不是累積金額的差距。",
        "xlabel":   "持有期(年)",
        "ylabel":   "年化實質報酬",
        "lbl_max":  "最佳窗口",
        "lbl_min":  "最差窗口",
        "lbl_band": "10-90 百分位區間",
        "lbl_med":  "中位數",
    },
    "cn": {
        "title":    "按持有期分组的滚动年化实质回报区间",
        "subtitle": "标普 500 总回报减 CPI,1928-2024(Damodaran)。时间压缩的是区间,不是累积金额的差距。",
        "xlabel":   "持有期(年)",
        "ylabel":   "年化实质回报",
        "lbl_max":  "最佳窗口",
        "lbl_min":  "最差窗口",
        "lbl_band": "10-90 百分位区间",
        "lbl_med":  "中位数",
    },
}

HORIZONS = [1, 3, 5, 10, 15, 20, 25, 30]


def _stats():
    df = damodaran_annual_returns()
    sp = df["SP500"].dropna()
    cpi = df["CPI"].dropna()
    real = (1 + sp) / (1 + cpi) - 1
    real = real.dropna()

    rows = []
    for h in HORIZONS:
        # geometric annualised over rolling h-year windows
        gross = (1 + real).rolling(h).apply(np.prod, raw=True)
        ann = gross ** (1 / h) - 1
        ann = ann.dropna()
        rows.append({
            "h":   h,
            "min": float(ann.min()),
            "p10": float(ann.quantile(0.10)),
            "med": float(ann.median()),
            "p90": float(ann.quantile(0.90)),
            "max": float(ann.max()),
        })
    return pd.DataFrame(rows)


def build_fig(s):
    df = _stats()
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10, 5.6))
    style_axes(ax, p)

    x = df["h"].values
    ax.fill_between(x, df["min"].values, df["max"].values,
                    color=p["blue"], alpha=0.12, label=s["lbl_max"])
    ax.fill_between(x, df["p10"].values, df["p90"].values,
                    color=p["blue"], alpha=0.30, label=s["lbl_band"])

    ax.plot(x, df["max"].values, color=p["green"], linewidth=2.0,
            marker="o", markersize=5, label=s["lbl_max"])
    ax.plot(x, df["min"].values, color=p["red"], linewidth=2.0,
            marker="o", markersize=5, label=s["lbl_min"])
    ax.plot(x, df["med"].values, color=p["fg"], linewidth=2.0,
            marker="o", markersize=5, linestyle="--", label=s["lbl_med"])

    ax.axhline(0, color=p["fg"], linewidth=0.8, linestyle=":")

    # Label endpoints
    for _, row in df.iterrows():
        ax.text(row["h"], row["max"] + 0.015, f"+{row['max']:.0%}",
                ha="center", fontsize=8, color=p["green"])
        ax.text(row["h"], row["min"] - 0.025, f"{row['min']:.0%}",
                ha="center", fontsize=8, color=p["red"])

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.set_xticks(HORIZONS)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
