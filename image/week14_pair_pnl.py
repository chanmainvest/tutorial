"""Week 14, §2.5 - Backtest of a +/-2 sigma entry / 0 sigma exit pair-trading
rule on the KO/PEP log spread, 2015-2024.

Rule (long the spread = long KO, short PEP at equal dollar):
    enter long  when Z <= -2,
    enter short when Z >= +2,
    exit         when Z crosses 0,
    flat otherwise.
Daily P&L is `position * d(log_spread)` where position is in {-1, 0, +1}
and dollar-neutral. The chart has two panels: top is the Z-score with
up/down arrows on entries; bottom is the cumulative P&L line in
percent, no compounding.

Costs: 5 bps round-trip per trade (each side leg). This is not a
production backtest; the point is the *shape* of the equity curve --
many small wins, occasional regime breaks where the spread does not
revert and you cut.

Run:
    uv run python course/image/week14_pair_pnl.py
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
BASE = "week14_pair_pnl"

START = "2015-01-01"
END = "2024-12-31"
LOOKBACK = 60
ENTRY_Z = 2.0
EXIT_Z = 0.0
COST_BPS_PER_TRADE = 5.0  # round-trip, applied at each side change


def _load_pair() -> pd.DataFrame:
    try:
        ko = yahoo_history("KO", start=START, end=END, interval="1d")["AdjClose"]
        pep = yahoo_history("PEP", start=START, end=END, interval="1d")["AdjClose"]
    except Exception:
        ko = yahoo_history("KO", start=START, end=END, interval="1mo")["AdjClose"]
        pep = yahoo_history("PEP", start=START, end=END, interval="1mo")["AdjClose"]
    return pd.concat([ko.rename("KO"), pep.rename("PEP")], axis=1).dropna()


def _backtest(df: pd.DataFrame):
    log_spread = np.log(df["KO"]) - np.log(df["PEP"])
    mu = log_spread.rolling(LOOKBACK).mean()
    sd = log_spread.rolling(LOOKBACK).std()
    z = (log_spread - mu) / sd

    # Generate position series. Long spread when Z <= -ENTRY (expect KO to rise
    # vs PEP), short spread when Z >= +ENTRY. Exit on cross of zero.
    pos = np.zeros(len(df))
    cur = 0
    for i in range(len(df)):
        zi = z.iloc[i]
        if np.isnan(zi):
            pos[i] = 0
            continue
        if cur == 0:
            if zi <= -ENTRY_Z:
                cur = 1
            elif zi >= ENTRY_Z:
                cur = -1
        elif cur == 1 and zi >= EXIT_Z:
            cur = 0
        elif cur == -1 and zi <= EXIT_Z:
            cur = 0
        pos[i] = cur

    pos_s = pd.Series(pos, index=df.index)
    # Daily P&L in spread-log-units. Position applied to *next-day* return.
    d_spread = log_spread.diff().fillna(0.0)
    daily = pos_s.shift(1).fillna(0.0) * d_spread

    # Costs at each position change.
    pos_chg = pos_s.diff().abs().fillna(0.0)
    cost = pos_chg * (COST_BPS_PER_TRADE / 1e4)
    daily = daily - cost

    cum = daily.cumsum()  # additive: log P&L approximates pct return for small moves

    # Trade markers: position transitions away from 0
    entries_long = (pos_s.shift(1).fillna(0) == 0) & (pos_s == 1)
    entries_short = (pos_s.shift(1).fillna(0) == 0) & (pos_s == -1)
    return z, pos_s, cum, entries_long, entries_short


LANG_STRINGS = {
    "en": {
        "title":     "Pair-trading P&L on KO/PEP — +/-2 sigma entry, 0 sigma exit, 2015-2024",
        "subtitle":  "Long the spread on cheap (Z <= -2), short on rich (Z >= +2), flat across mean. 5 bps round-trip cost per trade.",
        "top_ylabel":  "Z-score",
        "bot_ylabel":  "Cumulative P&L (log-spread units)",
        "xlabel":      "Date",
        "z_label":     "Z-score of log(KO) - log(PEP)",
        "pnl_label":   "Cumulative P&L",
        "long_label":  "Enter long spread",
        "short_label": "Enter short spread",
        "footer":      "Data: Yahoo Finance daily AdjClose. Z = (log_spread - 60d mean) / 60d stdev.  This is a teaching backtest, not an out-of-sample validated strategy.",
    },
    "hk": {
        "title":     "KO/PEP 配對交易損益 — +/-2 標準差入場、0 線出場,2015-2024",
        "subtitle":  "便宜時(Z <= -2)做多價差,昂貴時(Z >= +2)做空價差,回到均值清倉。每次交易單邊成本 5 bp。",
        "top_ylabel":  "Z-score",
        "bot_ylabel":  "累計損益(log-spread 單位)",
        "xlabel":      "日期",
        "z_label":     "log(KO) - log(PEP) 的 Z-score",
        "pnl_label":   "累計損益",
        "long_label":  "做多價差入場",
        "short_label": "做空價差入場",
        "footer":      "數據:Yahoo Finance 日線 AdjClose。Z =(log_spread - 60 日均值)/ 60 日標準差。教學示意回測,並未經過樣本外驗證。",
    },
    "tw": {
        "title":     "KO/PEP 配對交易損益 — +/-2 個標準差進場、0 線出場,2015-2024",
        "subtitle":  "便宜時(Z <= -2)做多價差,昂貴時(Z >= +2)做空價差,回到均值平倉。每次交易單邊成本 5 bp。",
        "top_ylabel":  "Z-score",
        "bot_ylabel":  "累計損益(log-spread 單位)",
        "xlabel":      "日期",
        "z_label":     "log(KO) - log(PEP) 的 Z-score",
        "pnl_label":   "累計損益",
        "long_label":  "做多價差進場",
        "short_label": "做空價差進場",
        "footer":      "數據:Yahoo Finance 日線 AdjClose。Z =(log_spread - 60 日均值)/ 60 日標準差。教學示意回測,未經樣本外驗證。",
    },
    "cn": {
        "title":     "KO/PEP 配对交易损益 — +/-2 标准差入场、0 线出场,2015-2024",
        "subtitle":  "便宜时(Z <= -2)做多价差,昂贵时(Z >= +2)做空价差,回到均值平仓。每次交易单边成本 5 bp。",
        "top_ylabel":  "Z-score",
        "bot_ylabel":  "累计损益(log-spread 单位)",
        "xlabel":      "日期",
        "z_label":     "log(KO) - log(PEP) 的 Z-score",
        "pnl_label":   "累计损益",
        "long_label":  "做多价差入场",
        "short_label": "做空价差入场",
        "footer":      "数据:Yahoo Finance 日线 AdjClose。Z =(log_spread - 60 日均值)/ 60 日标准差。教学示意回测,未经样本外验证。",
    },
}


def build_fig(s):
    apply_cjk_font()
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    df = _load_pair()
    z, pos, cum, ent_long, ent_short = _backtest(df)

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(11.5, 7.4), dpi=160,
        gridspec_kw={"height_ratios": [1.0, 1.0], "hspace": 0.32},
        sharex=True,
    )
    fig.patch.set_facecolor(p["bg"])

    # ---- Top: Z-score with arrows on entries ----
    style_axes(ax_top, p)
    ax_top.plot(df.index, z.values, color=p["accent"], linewidth=1.2,
                label=s["z_label"])
    ax_top.axhline(0, color=p["muted"], linewidth=0.7)
    ax_top.axhline(2, color=p["red"], linewidth=0.9, linestyle="--", alpha=0.7)
    ax_top.axhline(-2, color=p["red"], linewidth=0.9, linestyle="--", alpha=0.7)
    ax_top.fill_between(df.index, -2, 2, color=p["green"], alpha=0.05, linewidth=0)

    long_idx = df.index[ent_long.values]
    short_idx = df.index[ent_short.values]
    if len(long_idx) > 0:
        ax_top.scatter(long_idx, z.loc[long_idx].values,
                       marker="^", s=70, color=p["green"], zorder=5,
                       label=s["long_label"], edgecolors=p["bg"], linewidths=0.8)
    if len(short_idx) > 0:
        ax_top.scatter(short_idx, z.loc[short_idx].values,
                       marker="v", s=70, color=p["red"], zorder=5,
                       label=s["short_label"], edgecolors=p["bg"], linewidths=0.8)
    ax_top.set_ylim(-4, 4)
    ax_top.set_ylabel(s["top_ylabel"], fontsize=10)
    ax_top.legend(loc="upper left", frameon=False, fontsize=9)

    # ---- Bottom: cumulative P&L ----
    style_axes(ax_bot, p)
    ax_bot.plot(df.index, cum.values, color=p["blue"], linewidth=1.8,
                label=s["pnl_label"])
    ax_bot.fill_between(df.index, 0, cum.values, where=(cum.values >= 0),
                        color=p["green"], alpha=0.10, linewidth=0)
    ax_bot.fill_between(df.index, 0, cum.values, where=(cum.values < 0),
                        color=p["red"], alpha=0.10, linewidth=0)
    ax_bot.axhline(0, color=p["muted"], linewidth=0.7)
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
