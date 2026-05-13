"""Week 14, §2.2 - KO/PEP normalised prices and log-spread Z-score (2015-2024).

Top panel: Coca-Cola (KO) and PepsiCo (PEP) total-return prices, both
normalised to 100 at the start of 2015. Bottom panel: rolling-Z-score
of the log-price spread log(KO) - log(PEP) using a 60-day lookback,
with +/-2 sigma bands. The aim is to show students that two ostensibly
similar names spend most of their lives within +/-2 sigma of each
other, but periodically dislocate; those dislocations are the entry
candidates a pair trader looks for.

Data source: Yahoo Finance daily AdjClose via scripts/market_data.py.
Falls back to monthly if daily fails. If both fail, raises so the
caller sees the issue rather than silently producing a fake chart.

Run:
    uv run python course/image/week14_kopep_spread.py
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
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import yahoo_history  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week14_kopep_spread"

START = "2015-01-01"
END = "2024-12-31"
LOOKBACK = 60  # trading-day rolling window for Z-score


def _load_pair() -> pd.DataFrame:
    """Return a DataFrame with daily AdjClose columns KO and PEP, aligned."""
    try:
        ko = yahoo_history("KO", start=START, end=END, interval="1d")["AdjClose"]
        pep = yahoo_history("PEP", start=START, end=END, interval="1d")["AdjClose"]
    except Exception:
        ko = yahoo_history("KO", start=START, end=END, interval="1mo")["AdjClose"]
        pep = yahoo_history("PEP", start=START, end=END, interval="1mo")["AdjClose"]
    df = pd.concat([ko.rename("KO"), pep.rename("PEP")], axis=1).dropna()
    return df


LANG_STRINGS = {
    "en": {
        "title":     "KO vs PEP — normalised price and log-spread Z-score, 2015-2024",
        "subtitle":  "Two world-class beverage incumbents. Most of the time the spread sits inside +/-2 sigma; the dislocations are the trade.",
        "top_ylabel":  "Price (rebased to 100)",
        "bot_ylabel":  "Z-score of log(KO) - log(PEP), 60-day rolling",
        "xlabel":      "Date",
        "ko":          "Coca-Cola (KO)",
        "pep":         "PepsiCo (PEP)",
        "z_label":     "Z-score",
        "band2":       "+/-2 sigma",
        "band0":       "mean",
        "footer":      "Data: Yahoo Finance daily AdjClose. Z-score uses a 60-trading-day rolling mean and stdev of log(KO)-log(PEP).",
    },
    "hk": {
        "title":     "KO 對 PEP — 標準化股價與對數價差 Z-score,2015-2024",
        "subtitle":  "兩家世界級飲料龍頭。價差大部分時間落在 +/-2 標準差之內,偏離才是交易機會。",
        "top_ylabel":  "股價(標準化至 100)",
        "bot_ylabel":  "log(KO) - log(PEP) 之 Z-score(60 日滾動)",
        "xlabel":      "日期",
        "ko":          "可口可樂(KO)",
        "pep":         "百事公司(PEP)",
        "z_label":     "Z-score",
        "band2":       "+/-2 標準差",
        "band0":       "均值",
        "footer":      "數據:Yahoo Finance 日線 AdjClose。Z-score 採用 60 個交易日滾動均值與標準差,作用於 log(KO)-log(PEP)。",
    },
    "tw": {
        "title":     "KO 對 PEP — 標準化股價與對數價差 Z-score,2015-2024",
        "subtitle":  "兩家世界級飲料巨頭。價差大部分時間落在 +/-2 個標準差以內,偏離才是交易機會。",
        "top_ylabel":  "股價(基準化至 100)",
        "bot_ylabel":  "log(KO) - log(PEP) 之 Z-score(60 日滾動)",
        "xlabel":      "日期",
        "ko":          "可口可樂(KO)",
        "pep":         "百事公司(PEP)",
        "z_label":     "Z-score",
        "band2":       "+/-2 個標準差",
        "band0":       "均值",
        "footer":      "數據:Yahoo Finance 日線 AdjClose。Z-score 採用 60 個交易日滾動均值與標準差,作用於 log(KO)-log(PEP)。",
    },
    "cn": {
        "title":     "KO 对 PEP — 标准化股价与对数价差 Z-score,2015-2024",
        "subtitle":  "两家世界级饮料龙头。价差大部分时间落在 +/-2 标准差之内,偏离才是交易机会。",
        "top_ylabel":  "股价(基准化至 100)",
        "bot_ylabel":  "log(KO) - log(PEP) 的 Z-score(60 日滚动)",
        "xlabel":      "日期",
        "ko":          "可口可乐(KO)",
        "pep":         "百事公司(PEP)",
        "z_label":     "Z-score",
        "band2":       "+/-2 标准差",
        "band0":       "均值",
        "footer":      "数据:Yahoo Finance 日线 AdjClose。Z-score 采用 60 个交易日滚动均值与标准差,作用于 log(KO)-log(PEP)。",
    },
}


def build_fig(s):
    apply_cjk_font()
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    df = _load_pair()
    ko_norm = df["KO"] / df["KO"].iloc[0] * 100.0
    pep_norm = df["PEP"] / df["PEP"].iloc[0] * 100.0

    log_spread = np.log(df["KO"]) - np.log(df["PEP"])
    mu = log_spread.rolling(LOOKBACK).mean()
    sd = log_spread.rolling(LOOKBACK).std()
    z = (log_spread - mu) / sd

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(11.5, 7.4), dpi=160,
        gridspec_kw={"height_ratios": [1.15, 1.0], "hspace": 0.32},
        sharex=True,
    )
    fig.patch.set_facecolor(p["bg"])

    # ---- Top panel: normalised prices ----
    style_axes(ax_top, p)
    ax_top.plot(df.index, ko_norm.values, color=p["red"], linewidth=1.7, label=s["ko"])
    ax_top.plot(df.index, pep_norm.values, color=p["blue"], linewidth=1.7, label=s["pep"])
    ax_top.axhline(100, color=p["muted"], linewidth=0.7, linestyle=":", alpha=0.6)
    ax_top.set_ylabel(s["top_ylabel"], fontsize=10)
    ax_top.legend(loc="upper left", frameon=False, fontsize=10)

    # ---- Bottom panel: Z-score ----
    style_axes(ax_bot, p)
    ax_bot.plot(df.index, z.values, color=p["accent"], linewidth=1.4, label=s["z_label"])
    ax_bot.axhline(0, color=p["muted"], linewidth=0.8)
    for level, lbl_use in ((2, True), (-2, False)):
        ax_bot.axhline(level, color=p["red"], linewidth=0.9, linestyle="--", alpha=0.7,
                       label=s["band2"] if lbl_use else None)
    ax_bot.fill_between(df.index, -2, 2, color=p["green"], alpha=0.06, linewidth=0)
    ax_bot.set_ylim(-4, 4)
    ax_bot.set_ylabel(s["bot_ylabel"], fontsize=10)
    ax_bot.set_xlabel(s["xlabel"], fontsize=10)
    ax_bot.legend(loc="upper left", frameon=False, fontsize=9)

    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 color=p["fg"], y=0.985)
    fig.text(0.5, 0.945, s["subtitle"], ha="center", fontsize=10,
             color=p["muted"], style="italic")
    fig.text(0.5, 0.015, s["footer"], ha="center", fontsize=8.5,
             color=p["muted"])

    fig.tight_layout(rect=[0, 0.035, 1, 0.93])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
