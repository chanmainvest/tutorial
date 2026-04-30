"""Side 26, Sec 2.3 -- Typical bid-ask spreads by market-cap bucket.

Bar chart of representative bid-ask spreads (basis points) across the
five canonical US-listed market-cap buckets, with ADV annotations and
cap-range labels. The 100x gap between mega-caps and micro-caps is the
chart's punchline.

Run:
    uv run python course/image/side26_liquidity_by_size.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side26_liquidity_by_size"

# bucket: (typical spread bps, typical ADV $M, midpoint cap $B label idx)
BUCKETS = [
    ("mega",  1.0,    8000.0),
    ("large", 4.0,    700.0),
    ("mid",   10.0,   80.0),
    ("small", 45.0,   12.0),
    ("micro", 200.0,  1.5),
]


LANG_STRINGS = {
    "en": {
        "title": "Typical Bid-Ask Spread by Market-Cap Bucket (Apr 2026)",
        "subtitle": "Liquidity scales roughly with the inverse square root of market cap. Micro-caps cost ~200x more to trade than mega-caps.",
        "ylabel": "Quoted bid-ask spread (basis points, log scale)",
        "xlabel": "Market-cap bucket",
        "buckets": {
            "mega":  "Mega\n> $500B\n(AAPL, MSFT)",
            "large": "Large\n$10B-$500B\n(median S&P 500)",
            "mid":   "Mid\n$2B-$10B",
            "small": "Small\n$300M-$2B\n(median R2000)",
            "micro": "Micro\n< $300M",
        },
        "spread_lbl": "{:.0f} bps",
        "spread_lbl_sub": "{:.1f} bps",
        "adv_lbl": "ADV ~ ${adv}",
        "footer": "Round-trip cost on a 1%-of-ADV order = quoted spread + ~10 bps square-root impact in normal vol. Crisis vol multiplies the spread component 5-10x.",
        "note": "Dashed line: 50 bp threshold. Above = small/micro territory where rebalancing drag becomes material.",
    },
    "hk": {
        "title": "各市值區間的典型買賣價差(2026年4月)",
        "subtitle": "流動性大致與市值的平方根反比。微型股的交易成本約為大型股的 200 倍。",
        "ylabel": "報價買賣價差(基點,對數刻度)",
        "xlabel": "市值區間",
        "buckets": {
            "mega":  "超大型\n> 5,000億美元\n(AAPL, MSFT)",
            "large": "大型\n100億-5,000億\n(S&P 500 中位數)",
            "mid":   "中型\n20億-100億",
            "small": "小型\n3億-20億\n(R2000 中位數)",
            "micro": "微型\n< 3億美元",
        },
        "spread_lbl": "{:.0f} bps",
        "spread_lbl_sub": "{:.1f} bps",
        "adv_lbl": "ADV ~ ${adv}",
        "footer": "1% ADV 訂單的雙向成本 = 報價價差 + 約 10 bps 平方根衝擊(正常波動率)。危機波動率將價差部分放大 5-10 倍。",
        "note": "虛線:50 bp 門檻。以上為小型/微型股範圍,再平衡拖累變得顯著。",
    },
    "tw": {
        "title": "各市值區間的典型買賣價差(2026年4月)",
        "subtitle": "流動性大致與市值的平方根反比。微型股的交易成本約為大型股的 200 倍。",
        "ylabel": "報價買賣價差(基點,對數刻度)",
        "xlabel": "市值區間",
        "buckets": {
            "mega":  "超大型\n> 5,000億美元\n(AAPL, MSFT)",
            "large": "大型\n100億-5,000億\n(S&P 500 中位數)",
            "mid":   "中型\n20億-100億",
            "small": "小型\n3億-20億\n(R2000 中位數)",
            "micro": "微型\n< 3億美元",
        },
        "spread_lbl": "{:.0f} bps",
        "spread_lbl_sub": "{:.1f} bps",
        "adv_lbl": "ADV ~ ${adv}",
        "footer": "1% ADV 訂單的雙向成本 = 報價價差 + 約 10 bps 平方根衝擊(正常波動率)。危機波動率將價差部分放大 5-10 倍。",
        "note": "虛線:50 bp 門檻。以上為小型/微型股範圍,再平衡拖累變得顯著。",
    },
    "cn": {
        "title": "各市值区间的典型买卖价差(2026年4月)",
        "subtitle": "流动性大致与市值的平方根反比。微型股的交易成本约为大型股的 200 倍。",
        "ylabel": "报价买卖价差(基点,对数刻度)",
        "xlabel": "市值区间",
        "buckets": {
            "mega":  "超大型\n> 5,000亿美元\n(AAPL, MSFT)",
            "large": "大型\n100亿-5,000亿\n(S&P 500 中位数)",
            "mid":   "中型\n20亿-100亿",
            "small": "小型\n3亿-20亿\n(R2000 中位数)",
            "micro": "微型\n< 3亿美元",
        },
        "spread_lbl": "{:.0f} bps",
        "spread_lbl_sub": "{:.1f} bps",
        "adv_lbl": "ADV ~ ${adv}",
        "footer": "1% ADV 订单的双向成本 = 报价价差 + 约 10 bps 平方根冲击(正常波动率)。危机波动率将价差部分放大 5-10 倍。",
        "note": "虚线:50 bp 阈值。以上为小型/微型股范围,再平衡拖累变得显著。",
    },
}


def _fmt_adv(adv_m: float) -> str:
    """Format ADV $M as a human label, e.g. 8000 -> '$8B/d', 1.5 -> '$1.5M/d'."""
    if adv_m >= 1000:
        return f"\\${adv_m/1000:.0f}B/d"
    if adv_m >= 100:
        return f"\\${adv_m:.0f}M/d"
    if adv_m >= 10:
        return f"\\${adv_m:.0f}M/d"
    return f"\\${adv_m:.1f}M/d"


def build_fig(s_in):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s_in.items()}
    P = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(11.0, 6.4), dpi=150)
    style_axes(ax)

    keys = [b[0] for b in BUCKETS]
    spreads = [b[1] for b in BUCKETS]
    advs = [b[2] for b in BUCKETS]

    # Color gradient: mega = teal/blue, large = blue, mid = grey, small = orange, micro = red
    colors = [P["teal"], P["blue"], P["grey"], P["orange"], P["red"]]

    x = np.arange(len(keys))
    bars = ax.bar(x, spreads, color=colors, edgecolor="white", linewidth=1.5,
                  width=0.7, zorder=3)

    # Value labels on top of each bar
    for xi, sp in zip(x, spreads):
        if sp >= 5:
            lbl = s["spread_lbl"].format(sp)
        else:
            lbl = s["spread_lbl_sub"].format(sp)
        ax.text(xi, sp * 1.18, lbl, ha="center", va="bottom",
                fontsize=11, weight="bold", color=P["fg"])

    # ADV annotation below bar (inside the bar at top for the small ones)
    for xi, sp, adv in zip(x, spreads, advs):
        adv_lbl_template = s_in["adv_lbl"]  # use raw template for {adv}
        adv_lbl = adv_lbl_template.format(adv=_fmt_adv(adv))
        ax.text(xi, sp * 0.55 if sp >= 8 else sp * 1.7,
                adv_lbl, ha="center", va="center",
                fontsize=9, color="white" if sp >= 8 else P["muted"],
                weight="bold" if sp >= 8 else "normal", style="italic")

    # 50 bp dashed reference line
    ax.axhline(50, color=P["accent"], linewidth=1.2, linestyle="--", alpha=0.85, zorder=2)
    ax.text(len(keys) - 0.4, 56, "50 bp", color=P["accent"], fontsize=9,
            ha="right", style="italic", weight="bold")

    bucket_labels = [s["buckets"][k] for k in keys]
    ax.set_xticks(x)
    ax.set_xticklabels(bucket_labels, fontsize=9.5)
    ax.set_xlabel(s["xlabel"], fontsize=10.5, labelpad=8)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_yscale("log")
    ax.set_ylim(0.5, 600)
    ax.set_xlim(-0.6, len(keys) - 0.4)

    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")
    fig.text(0.5, 0.06, s["note"], ha="center",
             fontsize=8.8, color=P["accent"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=P["muted"], style="italic")

    ax.grid(True, axis="y", color=P["grid"], linewidth=0.6, alpha=0.6, which="both")
    ax.grid(False, axis="x")

    fig.tight_layout(rect=[0, 0.08, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
