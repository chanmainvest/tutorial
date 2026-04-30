"""Side 27, S2.5 - P/E vs ROE quadrant scatter for 30 US-listed names.

Lower-right (low P/E, high ROE) is the GARP zone, shaded green.
Upper-right is "quality at a premium". Upper-left is the glamour-stock
trap. Lower-left is value-trap territory. April 2026 figures.

Run:
    uv run python course/image/side27_garp_quadrant.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side27_garp_quadrant"


# 30 US-listed names, approximate trailing P/E and ROE (%), April 2026.
# Magnitudes are illustrative for the quadrant frame, not buy/sell signals.
STOCKS = [
    # (ticker, P/E, ROE%)
    ("AAPL",  28, 145),
    ("MSFT",  32,  38),
    ("GOOGL", 22,  28),
    ("AMZN",  38,  22),
    ("META",  24,  32),
    ("NVDA",  36,  90),
    ("TSLA",  60,  18),
    ("BRK.B", 22,  12),
    ("JPM",   12,  16),
    ("V",     28,  50),
    ("JNJ",   16,  24),
    ("UNH",   18,  26),
    ("PG",    24,  35),
    ("KO",    24,  42),
    ("PEP",   22,  50),
    ("WMT",   28,  22),
    ("COST",  48,  30),
    ("NEE",   20,  12),
    ("XOM",   13,  18),
    ("CVX",   14,  14),
    ("BAC",   11,  10),
    ("WFC",   12,  11),
    ("AVGO",  30,  32),
    ("CRM",   34,  12),
    ("ADBE",  28,  36),
    ("NFLX",  30,  30),
    ("TXN",   24,  38),
    ("LIN",   30,  17),
    ("TMO",   26,  16),
    ("ABBV",  14,  60),
]

PE_CUT  = 20.0   # cheap if PE <= 20
ROE_CUT = 20.0   # high quality if ROE >= 20


LANG_STRINGS = {
    "en": {
        "title":    "P/E vs ROE quadrant - 30 US large-caps, April 2026",
        "subtitle": "Lower-right is the GARP zone: low price, high return on equity. Most large-caps live in the upper-right (quality at a premium).",
        "xlabel":   "Trailing P/E",
        "ylabel":   "Return on equity (%)",
        "q_garp":   "GARP zone\n(cheap + high quality)",
        "q_glam":   "Glamour-stock trap\n(expensive + high quality)",
        "q_trap":   "Value trap\n(cheap + low quality)",
        "q_avoid":  "Avoid\n(expensive + low quality)",
        "footer":   "Cuts at P/E = 20 and ROE = 20%. Stocks migrating into the lower-right are the GARP screen's natural targets.",
    },
    "hk": {
        "title":    "P/E 對 ROE 四象限 - 30 隻美股大型股,2026 年 4 月",
        "subtitle": "右下角為 GARP 區:低估值 + 高股本回報。大部分大型股位於右上角(優質但溢價)。",
        "xlabel":   "市盈率(TTM)",
        "ylabel":   "股本回報率 ROE(%)",
        "q_garp":   "GARP 區\n(便宜 + 高品質)",
        "q_glam":   "明星股陷阱\n(昂貴 + 高品質)",
        "q_trap":   "價值陷阱\n(便宜 + 低品質)",
        "q_avoid":  "避免\n(昂貴 + 低品質)",
        "footer":   "以 P/E = 20、ROE = 20% 切分。正在向右下角遷移的股票就是 GARP 篩選的天然目標。",
    },
    "tw": {
        "title":    "P/E 對 ROE 四象限 - 30 檔美股大型股,2026 年 4 月",
        "subtitle": "右下為 GARP 區:低估值 + 高股東權益報酬。大多數大型股位於右上(優質但溢價)。",
        "xlabel":   "本益比(TTM)",
        "ylabel":   "股東權益報酬率 ROE(%)",
        "q_garp":   "GARP 區\n(便宜 + 高品質)",
        "q_glam":   "明星股陷阱\n(昂貴 + 高品質)",
        "q_trap":   "價值陷阱\n(便宜 + 低品質)",
        "q_avoid":  "避免\n(昂貴 + 低品質)",
        "footer":   "以 P/E = 20、ROE = 20% 切分。正在向右下角遷移的股票就是 GARP 篩選的天然目標。",
    },
    "cn": {
        "title":    "P/E 对 ROE 四象限 - 30 只美股大盘股,2026 年 4 月",
        "subtitle": "右下为 GARP 区:低估值 + 高净资产收益率。大多数大盘股位于右上(优质但溢价)。",
        "xlabel":   "市盈率(TTM)",
        "ylabel":   "净资产收益率 ROE(%)",
        "q_garp":   "GARP 区\n(便宜 + 高品质)",
        "q_glam":   "明星股陷阱\n(昂贵 + 高品质)",
        "q_trap":   "价值陷阱\n(便宜 + 低品质)",
        "q_avoid":  "避免\n(昂贵 + 低品质)",
        "footer":   "以 P/E = 20、ROE = 20% 切分。正在向右下角迁移的股票就是 GARP 筛选的天然目标。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax, p)

    x_lo, x_hi = 5, 70
    y_lo, y_hi = 0, 160

    # Quadrant fills.
    # Lower-right (GARP) — green tint
    ax.add_patch(Rectangle((x_lo, ROE_CUT), PE_CUT - x_lo, y_hi - ROE_CUT,
                           facecolor=p["green"], alpha=0.13, edgecolor="none", zorder=0))
    # Upper-right (glamour) — orange tint
    ax.add_patch(Rectangle((PE_CUT, ROE_CUT), x_hi - PE_CUT, y_hi - ROE_CUT,
                           facecolor=p["orange"], alpha=0.07, edgecolor="none", zorder=0))
    # Lower-left (trap) — red tint
    ax.add_patch(Rectangle((x_lo, y_lo), PE_CUT - x_lo, ROE_CUT - y_lo,
                           facecolor=p["red"], alpha=0.10, edgecolor="none", zorder=0))
    # Upper-left (avoid) — grey tint
    ax.add_patch(Rectangle((PE_CUT, y_lo), x_hi - PE_CUT, ROE_CUT - y_lo,
                           facecolor=p["grey"], alpha=0.07, edgecolor="none", zorder=0))

    # Cut lines.
    ax.axvline(PE_CUT, color=p["muted"], linewidth=0.8, linestyle="--", alpha=0.7)
    ax.axhline(ROE_CUT, color=p["muted"], linewidth=0.8, linestyle="--", alpha=0.7)

    # Quadrant labels (corners).
    ax.text(x_lo + 1, y_hi - 5, s["q_garp"],
            fontsize=10, color=p["green"], fontweight="bold",
            ha="left", va="top", alpha=0.95)
    ax.text(x_hi - 1, y_hi - 5, s["q_glam"],
            fontsize=10, color=p["orange"], fontweight="bold",
            ha="right", va="top", alpha=0.95)
    ax.text(x_lo + 1, y_lo + 5, s["q_trap"],
            fontsize=10, color=p["red"], fontweight="bold",
            ha="left", va="bottom", alpha=0.95)
    ax.text(x_hi - 1, y_lo + 5, s["q_avoid"],
            fontsize=10, color=p["grey"], fontweight="bold",
            ha="right", va="bottom", alpha=0.95)

    # Scatter points.
    for ticker, pe, roe in STOCKS:
        if pe > x_hi:
            pe = x_hi - 1  # clip TSLA-style outliers visually
        in_garp = (pe <= PE_CUT) and (roe >= ROE_CUT)
        color = p["green"] if in_garp else p["blue"]
        size = 90 if in_garp else 55
        ax.scatter(pe, min(roe, y_hi - 3), s=size, color=color,
                   edgecolor=p["fg"], linewidth=0.7, alpha=0.92, zorder=3)
        # Label offset to avoid overlap; small clusters tweaked manually.
        dx, dy = 0.7, 3.5
        if ticker in ("AAPL",):  # off-chart ROE clipped, label below
            dy = -7
        if ticker in ("MA",):
            dy = -7
        ax.text(pe + dx, min(roe, y_hi - 3) + dy, ticker,
                fontsize=8.5, color=p["fg"], ha="left", va="bottom",
                zorder=4)

    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(y_lo, y_hi)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)

    ax.set_title(s["title"], pad=24, fontsize=14, fontweight="bold", loc="left")
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"], style="italic", ha="left", va="bottom")

    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.5, color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.93])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_*.png to {OUT_DIR}")
