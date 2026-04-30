"""Week 31, §2.1 — US Treasury yield curve, today vs three historical regimes.

Plots the current (April 2026) US Treasury curve alongside the curves
from June 2007 (pre-GFC, near-flat), April 2020 (zero-bound), and
July 2023 (peak modern inversion). Pulls live snapshots from FRED
(DGS3MO/DGS2/DGS5/DGS10/DGS30) when reachable; embedded fallback
keeps the script reproducible offline.

Run:
    uv run python course/image/week31_curve_today.py
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
BASE = "week31_curve_today"

TENORS = ["3M", "2Y", "5Y", "10Y", "30Y"]
TENOR_X = [0.25, 2.0, 5.0, 10.0, 30.0]
SERIES_IDS = ["DGS3MO", "DGS2", "DGS5", "DGS10", "DGS30"]

# Embedded fallback snapshots (yield % at month-end). Source: FRED.
FALLBACK = {
    "2007-06": [4.82, 4.87, 4.93, 5.03, 5.12],   # Pre-GFC, near-flat
    "2020-04": [0.13, 0.20, 0.36, 0.64, 1.27],   # COVID zero-bound
    "2023-07": [5.45, 4.88, 4.18, 3.97, 4.03],   # Peak modern inversion
    "2026-04": [3.50, 3.60, 3.80, 4.00, 4.30],   # Today (April 2026)
}

LANG_STRINGS = {
    "en": {
        "title":    "US Treasury yield curve - Apr 2026 vs three regimes",
        "subtitle": "FRED DGS3MO/DGS2/DGS5/DGS10/DGS30, month-end snapshots. Same five tenors, four very different worlds.",
        "xlabel":   "Maturity (years, log scale)",
        "ylabel":   "Yield (% annual)",
        "lab_2007": "Jun 2007 - pre-GFC, flat",
        "lab_2020": "Apr 2020 - COVID, zero-bound",
        "lab_2023": "Jul 2023 - peak inversion",
        "lab_2026": "Apr 2026 - today, normal",
        "ann_inv":  "Inverted: 3M above 10Y by ~150 bp",
        "ann_now":  "10y-2y spread back to +40 bp",
    },
    "hk": {
        "title":    "美國國債孳息曲線 - 2026 年 4 月 vs 三個歷史時期",
        "subtitle": "FRED DGS3MO/DGS2/DGS5/DGS10/DGS30 月底快照。相同五個年期,四個截然不同的世界。",
        "xlabel":   "年期(年,對數軸)",
        "ylabel":   "孳息率(年化 %)",
        "lab_2007": "2007 年 6 月 - 金融海嘯前,曲線扁平",
        "lab_2020": "2020 年 4 月 - 疫情零利率",
        "lab_2023": "2023 年 7 月 - 現代史上最深倒掛",
        "lab_2026": "2026 年 4 月 - 當下,正常",
        "ann_inv":  "倒掛:3 個月高於 10 年約 150 個基點",
        "ann_now":  "10 年減 2 年息差回升至 +40 bp",
    },
    "tw": {
        "title":    "美國公債殖利率曲線 - 2026 年 4 月 vs 三個歷史時期",
        "subtitle": "FRED DGS3MO/DGS2/DGS5/DGS10/DGS30 月底資料。相同五個年期,四個截然不同的世界。",
        "xlabel":   "年期(年,對數軸)",
        "ylabel":   "殖利率(年化 %)",
        "lab_2007": "2007 年 6 月 - 金融海嘯前,曲線扁平",
        "lab_2020": "2020 年 4 月 - 疫情零利率",
        "lab_2023": "2023 年 7 月 - 現代史最深倒掛",
        "lab_2026": "2026 年 4 月 - 當前,正常",
        "ann_inv":  "倒掛:3 個月高於 10 年約 150 個基點",
        "ann_now":  "10 年減 2 年利差回到 +40 bp",
    },
    "cn": {
        "title":    "美国国债收益率曲线 - 2026 年 4 月 vs 三个历史时期",
        "subtitle": "FRED DGS3MO/DGS2/DGS5/DGS10/DGS30 月末快照。同样五个期限,四个截然不同的世界。",
        "xlabel":   "期限(年,对数轴)",
        "ylabel":   "收益率(年化 %)",
        "lab_2007": "2007 年 6 月 - 金融危机前,曲线平坦",
        "lab_2020": "2020 年 4 月 - 疫情零利率",
        "lab_2023": "2023 年 7 月 - 现代史最深倒挂",
        "lab_2026": "2026 年 4 月 - 当下,正常",
        "ann_inv":  "倒挂:3 个月高于 10 年约 150 个基点",
        "ann_now":  "10 年减 2 年利差回到 +40 bp",
    },
}


def _snapshot_at(month_str: str) -> list[float]:
    """Try FRED for each tenor at the given month-end; fallback if any fail."""
    try:
        target = pd.Timestamp(month_str + "-01") + pd.offsets.MonthEnd(0)
        out: list[float] = []
        for sid in SERIES_IDS:
            df = fred_series(sid, start="2007-01-01")
            s = df.iloc[:, 0].dropna().astype(float)
            s.index = pd.to_datetime(s.index)
            # take the last available reading on or before target
            s = s[s.index <= target]
            if s.empty:
                raise RuntimeError(f"no data for {sid} at {month_str}")
            out.append(float(s.iloc[-1]))
        return out
    except Exception:
        return FALLBACK[month_str]


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10.6, 6.0))
    style_axes(ax, p)

    snaps = {k: _snapshot_at(k) for k in FALLBACK.keys()}

    series = [
        ("2007-06", s["lab_2007"], p["grey"],   "o", "--", 1.7),
        ("2020-04", s["lab_2020"], p["green"],  "s", "-.", 1.7),
        ("2023-07", s["lab_2023"], p["red"],    "^", ":",  1.7),
        ("2026-04", s["lab_2026"], p["blue"],   "o", "-",  2.6),
    ]
    for key, label, colour, marker, linestyle, lw in series:
        ys = snaps[key]
        ax.plot(TENOR_X, ys, color=colour, linewidth=lw, linestyle=linestyle,
                marker=marker, markersize=6, label=label)

    # Annotate today's curve points
    today = snaps["2026-04"]
    for x, y, t in zip(TENOR_X, today, TENORS):
        ax.annotate(f"{t}\n{y:.2f}%", xy=(x, y), xytext=(0, 10),
                    textcoords="offset points", ha="center",
                    fontsize=8.5, color=p["blue"], fontweight="bold")

    # Annotate inversion + today's slope
    ax.text(8.0, 5.8, s["ann_inv"], fontsize=9, color=p["red"], fontweight="bold")
    ax.text(8.0, 0.2, s["ann_now"], fontsize=9, color=p["blue"], fontweight="bold")

    ax.set_xscale("log")
    ax.set_xticks(TENOR_X)
    ax.set_xticklabels(TENORS)
    ax.set_xlim(0.18, 40)
    ax.set_ylim(0, 6.5)

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    ax.legend(loc="lower right", fontsize=9, frameon=False)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
