"""Week 44, §2.1 — Limit order book schematic with market-order price impact.

Synthetic 5-deep top-of-book around $50.04 midpoint. Left panel shows
bid/ask ladder with the NBBO spread highlighted. Right panel illustrates
a 1,000-share market buy walking through three ask levels, with the
volume-weighted fill price annotated and the temporary "hole" left in
the book.

Run:
    uv run python course/image/week44_order_book.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week44_order_book"

# 5 levels each side. Prices in USD, sizes in shares.
ASKS = [(50.05, 200), (50.08, 500), (50.10, 800), (50.12, 1500), (50.15, 3000)]
BIDS = [(50.03, 300), (50.01, 600), (49.98, 1200), (49.96, 2000), (49.94, 4000)]

LANG_STRINGS = {
    "en": {
        "title":      "Anatomy of a limit order book and a market-order fill",
        "subtitle":   "5-deep synthetic book at $50 mid. Right panel: a 1,000-share market buy walks three ask levels.",
        "left_title": "Resting limit orders (top of book)",
        "right_title":"Market buy 1,000 shares - book after fill",
        "ask_lbl":    "Asks (sellers)",
        "bid_lbl":    "Bids (buyers)",
        "x_size":     "Resting size (shares)",
        "y_price":    "Price ($)",
        "spread":     "NBBO spread $0.02 = 4.0 bps",
        "mid":        "Midpoint 50.04",
        "filled":     "FILLED",
        "fill_text":  "Volume-weighted fill: 50.087  ·  300 shares left at 50.10",
        "impact":     "Price impact: 9.4 bps vs midpoint",
    },
    "hk": {
        "title":      "限價委託簿剖析及市價單成交",
        "subtitle":   "$50 中價附近合成的 5 檔深度。右圖:1,000 股市價買單吞掉三檔賣出價。",
        "left_title": "靜態限價委託(盤口)",
        "right_title":"市價買 1,000 股 - 成交後盤口",
        "ask_lbl":    "賣出方",
        "bid_lbl":    "買入方",
        "x_size":     "掛單量(股)",
        "y_price":    "價格(美元)",
        "spread":     "NBBO 價差 $0.02 = 4.0 基點",
        "mid":        "中價 50.04",
        "filled":     "已成交",
        "fill_text":  "成交均價:50.087  ·  剩 300 股掛在 50.10",
        "impact":     "對中價衝擊:9.4 基點",
    },
    "tw": {
        "title":      "限價委託簿剖析與市價單成交",
        "subtitle":   "$50 中價附近合成的 5 檔深度。右圖:1,000 股市價買單吃掉三檔賣價。",
        "left_title": "靜態限價委託(盤口)",
        "right_title":"市價買 1,000 股 - 成交後盤口",
        "ask_lbl":    "賣方",
        "bid_lbl":    "買方",
        "x_size":     "掛單量(股)",
        "y_price":    "價格(美元)",
        "spread":     "NBBO 價差 $0.02 = 4.0 基點",
        "mid":        "中價 50.04",
        "filled":     "已成交",
        "fill_text":  "成交均價:50.087  ·  剩 300 股掛於 50.10",
        "impact":     "對中價衝擊:9.4 基點",
    },
    "cn": {
        "title":      "限价委托簿剖析及市价单成交",
        "subtitle":   "$50 中价附近合成的 5 档深度。右图:1,000 股市价买单吞掉三档卖价。",
        "left_title": "静态限价委托(盘口)",
        "right_title":"市价买 1,000 股 - 成交后盘口",
        "ask_lbl":    "卖方",
        "bid_lbl":    "买方",
        "x_size":     "挂单量(股)",
        "y_price":    "价格(美元)",
        "spread":     "NBBO 价差 $0.02 = 4.0 基点",
        "mid":        "中价 50.04",
        "filled":     "已成交",
        "fill_text":  "成交均价:50.087  ·  剩 300 股挂于 50.10",
        "impact":     "对中价冲击:9.4 基点",
    },
}


def _vwap_fill(asks, qty):
    remaining = qty
    cost = 0.0
    fills = []  # list of (price, size_filled)
    for price, size in asks:
        take = min(size, remaining)
        if take <= 0:
            break
        cost += price * take
        fills.append((price, take))
        remaining -= take
        if remaining == 0:
            break
    avg = cost / qty
    return avg, fills


def build_fig(s_in):
    s = dict(s_in)
    p = PALETTE_LIGHT
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 6.4), dpi=150)

    # ---------------- LEFT PANEL: book before ----------------
    ax = axes[0]
    style_axes(ax, p)
    ask_prices = [a[0] for a in ASKS]
    ask_sizes  = [a[1] for a in ASKS]
    bid_prices = [b[0] for b in BIDS]
    bid_sizes  = [b[1] for b in BIDS]

    bar_h = 0.018
    # Asks: positive x
    ax.barh(ask_prices, ask_sizes, height=bar_h, color=p["red"], alpha=0.85,
            edgecolor=p["red"], linewidth=0.6, label=s["ask_lbl"])
    # Bids: negative x
    ax.barh(bid_prices, [-x for x in bid_sizes], height=bar_h, color=p["blue"],
            alpha=0.85, edgecolor=p["blue"], linewidth=0.6, label=s["bid_lbl"])

    # Annotate sizes on each bar
    for pr, sz in zip(ask_prices, ask_sizes):
        ax.text(sz + 100, pr, f"{sz:,}", va="center", ha="left",
                fontsize=8.5, color=p["red"])
    for pr, sz in zip(bid_prices, bid_sizes):
        ax.text(-sz - 100, pr, f"{sz:,}", va="center", ha="right",
                fontsize=8.5, color=p["blue"])

    # Spread band
    best_ask = ask_prices[0]
    best_bid = bid_prices[0]
    mid = 0.5 * (best_ask + best_bid)
    ax.axhspan(best_bid, best_ask, color=p["accent"], alpha=0.18, zorder=0)
    ax.axhline(mid, color=p["accent"], linewidth=1.0, linestyle="--", alpha=0.85)
    ax.text(0, mid + 0.003, s["mid"], color=p["accent"], fontsize=9,
            ha="center", weight="bold")
    ax.text(0, best_bid - 0.012, s["spread"], color=p["accent"], fontsize=9,
            ha="center", style="italic")

    ax.axvline(0, color=p["muted"], linewidth=0.7)
    ax.set_xlim(-4500, 4500)
    ax.set_ylim(49.92, 50.17)
    ax.set_xlabel(s["x_size"])
    ax.set_ylabel(s["y_price"])
    ax.set_title(s["left_title"], pad=12, fontsize=11.5, weight="bold",
                 color=p["fg"])
    ax.legend(loc="lower right", frameon=False, fontsize=9)

    # ---------------- RIGHT PANEL: after 1000-share buy ----------------
    qty = 1000
    avg, fills = _vwap_fill(ASKS, qty)
    # Build remaining ask book
    consumed = {pr: take for pr, take in fills}
    new_asks = []
    for price, size in ASKS:
        rem = size - consumed.get(price, 0)
        new_asks.append((price, rem))

    ax2 = axes[1]
    style_axes(ax2, p)

    # Filled (lighter, hatched) + remaining (solid)
    for price, size in ASKS:
        taken = consumed.get(price, 0)
        rem = size - taken
        if taken > 0:
            ax2.barh(price, taken, height=bar_h, color=p["red"], alpha=0.25,
                     hatch="///", edgecolor=p["red"], linewidth=0.6)
        if rem > 0:
            ax2.barh(price, rem, height=bar_h, left=taken, color=p["red"],
                     alpha=0.85, edgecolor=p["red"], linewidth=0.6)
        # Label "FILLED" or remaining qty
        if taken == size:
            ax2.text(taken / 2, price, s["filled"], va="center", ha="center",
                     fontsize=8, color="white", weight="bold")
        elif taken > 0:
            ax2.text(size + 100, price, f"{rem:,}", va="center", ha="left",
                     fontsize=8.5, color=p["red"])
        else:
            ax2.text(size + 100, price, f"{size:,}", va="center", ha="left",
                     fontsize=8.5, color=p["red"])

    # Bids on right panel: unchanged
    ax2.barh(bid_prices, [-x for x in bid_sizes], height=bar_h, color=p["blue"],
             alpha=0.85, edgecolor=p["blue"], linewidth=0.6)
    for pr, sz in zip(bid_prices, bid_sizes):
        ax2.text(-sz - 100, pr, f"{sz:,}", va="center", ha="right",
                 fontsize=8.5, color=p["blue"])

    # Average fill marker
    ax2.axhline(avg, color=p["accent"], linewidth=1.6)
    ax2.text(2200, avg + 0.004, f"VWAP fill = {avg:.3f}",
             color=p["accent"], fontsize=9.5, weight="bold")

    # Original midpoint
    ax2.axhline(mid, color=p["muted"], linewidth=0.8, linestyle=":")
    ax2.text(2200, mid - 0.012, f"orig. mid {mid:.2f}",
             color=p["muted"], fontsize=8.5, style="italic")

    # Impact arrow
    ax2.annotate("", xy=(1700, avg), xytext=(1700, mid),
                 arrowprops=dict(arrowstyle="->", color=p["accent"], lw=1.6))
    ax2.text(1800, (avg + mid) / 2, s["impact"], color=p["accent"],
             fontsize=8.5, style="italic")

    ax2.axvline(0, color=p["muted"], linewidth=0.7)
    ax2.set_xlim(-4500, 4500)
    ax2.set_ylim(49.92, 50.17)
    ax2.set_xlabel(s["x_size"])
    ax2.set_title(s["right_title"], pad=12, fontsize=11.5, weight="bold",
                  color=p["fg"])

    # Suptitle and subtitle
    fig.suptitle(s["title"], fontsize=14.5, fontweight="bold",
                 color=p["fg"], y=0.995)
    fig.text(0.5, 0.945, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"], style="italic")
    # Footer
    fig.text(0.5, 0.02, s["fill_text"], ha="center",
             fontsize=9, color=p["muted"])

    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for p in paths:
        print(f"wrote {p}")
