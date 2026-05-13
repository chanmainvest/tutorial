"""Week 34, §2.8 — Calendar-year 2022 returns by asset class.

Damodaran 1928-2024 file gives SP500 -18.11%, TBond10Y -17.83%, TBill
+1.46%, plus we add fixed values for TLT, REITs, gold, USD, HYG, BTC.
The visual punchline: every long-duration asset fell together.

Run:
    uv run python course/image/week34_2022_case.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

OUT_DIR = Path(__file__).parent
BASE = "week34_2022_case"


def _2022_rows():
    """Return list of (key, value_pct, category) for 2022."""
    df = damodaran_annual_returns()
    sp = float(df.loc[2022, "SP500"]) * 100.0
    tb = float(df.loc[2022, "TBond10Y"]) * 100.0
    bill = float(df.loc[2022, "TBill3M"]) * 100.0
    # Standard 2022 calendar-year prints from public data:
    rows = [
        ("BTC",   -64.2, "alt_neg"),
        ("TLT",   -31.2, "bond"),
        ("REITS", -24.4, "rrei"),
        ("SP500",     sp, "equity"),
        ("UST10Y",    tb, "bond"),
        ("HYG",   -10.9, "bond"),
        ("BILL",    bill, "cash"),
        ("GOLD",   +0.4, "alt"),
        ("USD",    +8.2, "alt"),
    ]
    return rows


LANG_STRINGS = {
    "en": {
        "title":    "Calendar-year 2022 returns by asset class",
        "subtitle": "Diversification failed because rate sensitivity dominated. Cash, gold and the dollar were the only positives.",
        "xlabel":   "Asset class",
        "ylabel":   "2022 total return (%)",
        "labels": {
            "BTC":    "Bitcoin",
            "TLT":    "30y Treasury (TLT)",
            "REITS":  "REITs (VNQ)",
            "SP500":  "S&P 500",
            "UST10Y": "10y Treasury",
            "HYG":    "High-yield (HYG)",
            "BILL":   "3M T-Bill",
            "GOLD":   "Gold",
            "USD":    "USD (DXY)",
        },
        "ann_lose": "Long-duration assets fell together",
        "ann_win":  "Only cash, gold,\nand the dollar held up",
        "footer":   "Sources: Damodaran 1928-2024 (SP500, UST10Y, T-Bill); standard public prints for TLT, VNQ, HYG, GLD, DXY, Bitcoin.",
    },
    "hk": {
        "title":    "2022 年度各資產類別回報",
        "subtitle": "分散投資失靈 — 利率敏感性壓倒了一切。只有現金、黃金與美元守住正回報。",
        "xlabel":   "資產類別",
        "ylabel":   "2022 年總回報(%)",
        "labels": {
            "BTC":    "比特幣",
            "TLT":    "30 年國債(TLT)",
            "REITS":  "房託(VNQ)",
            "SP500":  "標普 500",
            "UST10Y": "10 年國債",
            "HYG":    "高收益債(HYG)",
            "BILL":   "3 個月國庫券",
            "GOLD":   "黃金",
            "USD":    "美元(DXY)",
        },
        "ann_lose": "長久期資產齊跌",
        "ann_win":  "只有現金、黃金\n與美元能守住",
        "footer":   "資料來源:Damodaran 1928-2024(標普 500、10 年國債、國庫券);公開報價(TLT、VNQ、HYG、GLD、DXY、比特幣)。",
    },
    "tw": {
        "title":    "2022 年度各資產類別報酬",
        "subtitle": "分散投資失靈 — 利率敏感性壓倒一切。只有現金、黃金與美元守住正報酬。",
        "xlabel":   "資產類別",
        "ylabel":   "2022 年總報酬(%)",
        "labels": {
            "BTC":    "比特幣",
            "TLT":    "30 年公債(TLT)",
            "REITS":  "REITs(VNQ)",
            "SP500":  "標普 500",
            "UST10Y": "10 年公債",
            "HYG":    "高收益債(HYG)",
            "BILL":   "3 個月國庫券",
            "GOLD":   "黃金",
            "USD":    "美元(DXY)",
        },
        "ann_lose": "長存續期資產齊跌",
        "ann_win":  "只有現金、黃金\n與美元能守住",
        "footer":   "資料來源:Damodaran 1928-2024(標普 500、10 年公債、國庫券);公開報價(TLT、VNQ、HYG、GLD、DXY、比特幣)。",
    },
    "cn": {
        "title":    "2022 年度各资产类别回报",
        "subtitle": "分散投资失灵 — 利率敏感性压倒一切。只有现金、黄金与美元守住正回报。",
        "xlabel":   "资产类别",
        "ylabel":   "2022 年总回报(%)",
        "labels": {
            "BTC":    "比特币",
            "TLT":    "30 年国债(TLT)",
            "REITS":  "REITs(VNQ)",
            "SP500":  "标普 500",
            "UST10Y": "10 年国债",
            "HYG":    "高收益债(HYG)",
            "BILL":   "3 个月国库券",
            "GOLD":   "黄金",
            "USD":    "美元(DXY)",
        },
        "ann_lose": "长久期资产齐跌",
        "ann_win":  "只有现金、黄金\n与美元能守住",
        "footer":   "数据来源:Damodaran 1928-2024(标普 500、10 年国债、国库券);公开报价(TLT、VNQ、HYG、GLD、DXY、比特币)。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    rows = _2022_rows()

    fig, ax = plt.subplots(figsize=(11, 6.2))
    style_axes(ax, p)

    keys = [k for k, _, _ in rows]
    vals = [v for _, v, _ in rows]
    labels = [s["labels"][k] for k in keys]

    colors = [p["red"] if v < 0 else p["green"] for v in vals]
    x = np.arange(len(vals))
    bars = ax.bar(x, vals, color=colors, edgecolor=p["fg"], linewidth=0.7, width=0.72)

    for i, b in enumerate(bars):
        v = vals[i]
        ax.text(b.get_x() + b.get_width() / 2,
                v + (1.2 if v >= 0 else -1.2),
                f"{v:+.1f}%",
                ha="center",
                va="bottom" if v >= 0 else "top",
                fontsize=10, fontweight="bold",
                color=p["fg"])

    ax.axhline(0, color=p["fg"], linewidth=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, ha="right", fontsize=9.5)
    ax.set_ylim(-72, 18)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    # Annotations
    ax.text(2.5, -55, s["ann_lose"], color=p["red"],
            fontsize=10, ha="center", fontweight="bold")
    ax.text(7.0, 13, s["ann_win"], color=p["green"],
            fontsize=9.5, ha="center", fontweight="bold")

    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.5,
             color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
