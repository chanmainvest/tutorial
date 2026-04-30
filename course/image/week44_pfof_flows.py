"""Week 44, §2.4 — Payment-for-order-flow industry flow diagram.

Schematic Sankey-style flow: retail customers -> brokers (Robinhood,
Schwab, Webull, Public, Fidelity-options) -> wholesalers (Citadel, Virtu,
Susquehanna, Jane Street, G1X) -> exchange or internalisation.
Annotated dollar amounts reflect 2024 industry-wide PFOF revenue of
roughly $3.0-3.5B (equities ~$1.0B, options ~$2.2B). Numbers are
approximations based on public Rule 606 disclosures and SEC filings.

Run:
    uv run python course/image/week44_pfof_flows.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
BASE = "week44_pfof_flows"

LANG_STRINGS = {
    "en": {
        "title":     "Where the $3.2B/yr in retail PFOF comes from and where it goes",
        "subtitle":  "Schematic of US retail equity + options order flow, 2024 industry estimate",
        "col_retail":"Retail customers",
        "col_broker":"Retail brokers",
        "col_whole": "Wholesale market makers",
        "col_venue": "Execution venues",
        "retail_lbl":"~50M\nactive retail\naccounts",
        "venue_intern":"Internalised\n(~70%)\nwholesaler\ninventory",
        "venue_lit":  "Lit exchanges\n(~25%)\nNYSE / Nasdaq /\nCboe / IEX",
        "venue_dark": "Dark pools\n(~5%)\nGS SIGMA-X /\nUBS ATS / Liquidnet",
        "footer":    "Numbers approximate. Rule 606 disclosures + SEC PFOF filings, 2024 calendar year. Equities PFOF ~US 1.0B, options PFOF ~US 2.2B.",
        "ann_total": "Industry PFOF\n2024: US 3.2B",
        "ann_path":  "Customer click ->\nbroker route ->\nwholesaler fill ->\nspread captured",
    },
    "hk": {
        "title":     "每年 32 億美元零售 PFOF 從何而來、流向何處",
        "subtitle":  "美國零售股票 + 期權流量示意圖,2024 年行業估計",
        "col_retail":"零售客戶",
        "col_broker":"零售券商",
        "col_whole": "批發做市商",
        "col_venue": "執行場所",
        "retail_lbl":"~5,000 萬\n活躍零售\n帳戶",
        "venue_intern":"內部化\n(~70%)\n做市商自有\n存貨",
        "venue_lit":  "明盤交易所\n(~25%)\nNYSE / Nasdaq /\nCboe / IEX",
        "venue_dark": "暗池\n(~5%)\nGS SIGMA-X /\nUBS ATS / Liquidnet",
        "footer":    "數字為近似值。來源:Rule 606 披露 + SEC PFOF 文件,2024 年。股票 PFOF 約 10 億美元,期權 PFOF 約 22 億美元。",
        "ann_total": "行業 PFOF\n2024:32 億美元",
        "ann_path":  "客戶點擊 ->\n券商路由 ->\n批發商成交 ->\n拿走價差",
    },
    "tw": {
        "title":     "每年 32 億美元零售 PFOF 從何而來、流向何處",
        "subtitle":  "美國零售股票 + 選擇權流量示意圖,2024 年產業估計",
        "col_retail":"零售客戶",
        "col_broker":"零售券商",
        "col_whole": "批發造市商",
        "col_venue": "執行場所",
        "retail_lbl":"~5,000 萬\n活躍零售\n帳戶",
        "venue_intern":"內部成交\n(~70%)\n造市商自有\n部位",
        "venue_lit":  "明盤交易所\n(~25%)\nNYSE / Nasdaq /\nCboe / IEX",
        "venue_dark": "暗池\n(~5%)\nGS SIGMA-X /\nUBS ATS / Liquidnet",
        "footer":    "數字為近似值。來源:Rule 606 披露 + SEC PFOF 文件,2024 年。股票 PFOF 約 10 億美元,選擇權 PFOF 約 22 億美元。",
        "ann_total": "產業 PFOF\n2024:32 億美元",
        "ann_path":  "客戶點擊 ->\n券商路由 ->\n批發商成交 ->\n拿走價差",
    },
    "cn": {
        "title":     "每年 32 亿美元零售 PFOF 从何而来、流向何处",
        "subtitle":  "美国零售股票 + 期权流量示意图,2024 年行业估算",
        "col_retail":"零售客户",
        "col_broker":"零售券商",
        "col_whole": "批发做市商",
        "col_venue": "执行场所",
        "retail_lbl":"~5,000 万\n活跃零售\n账户",
        "venue_intern":"内部化\n(~70%)\n做市商自有\n库存",
        "venue_lit":  "明盘交易所\n(~25%)\nNYSE / Nasdaq /\nCboe / IEX",
        "venue_dark": "暗池\n(~5%)\nGS SIGMA-X /\nUBS ATS / Liquidnet",
        "footer":    "数字为近似值。来源:Rule 606 披露 + SEC PFOF 文件,2024 年。股票 PFOF 约 10 亿美元,期权 PFOF 约 22 亿美元。",
        "ann_total": "行业 PFOF\n2024:32 亿美元",
        "ann_path":  "客户点击 ->\n券商路由 ->\n批发商成交 ->\n拿走价差",
    },
}

# Rough 2024 PFOF revenue per broker, $M (industry estimates from public filings)
BROKERS = [
    ("Robinhood",  1100),
    ("Schwab/TDA", 750),
    ("Webull",     350),
    ("Fidelity*",  280),
    ("Public/Etc", 720),
]
# *Fidelity = options-only PFOF; equities are routed without payment
WHOLESALERS = [
    ("Citadel Securities", 1450),
    ("Virtu Financial",     720),
    ("Susquehanna",         460),
    ("Jane Street",         320),
    ("G1X / Wolverine",     250),
]


def build_fig(s_in):
    s = dict(s_in)
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(13.0, 7.2), dpi=150)
    style_axes(ax, p)

    # 4 columns at x = 0, 1, 2, 3
    col_x = [0.5, 3.0, 5.5, 8.5]
    col_w = 1.4
    n_b = len(BROKERS)
    n_w = len(WHOLESALERS)

    # ---- Column headers ----
    headers = [s["col_retail"], s["col_broker"], s["col_whole"], s["col_venue"]]
    for x, h in zip(col_x, headers):
        ax.text(x + col_w / 2, 9.20, h, ha="center", va="bottom",
                fontsize=11.5, weight="bold", color=p["fg"])

    # ---- Column 1: retail customers (single big block) ----
    ax.add_patch(mpatches.FancyBboxPatch(
        (col_x[0], 3.5), col_w, 3.5,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor=p["accent"], alpha=0.20,
        edgecolor=p["accent"], linewidth=1.5))
    ax.text(col_x[0] + col_w / 2, 5.25, s["retail_lbl"], ha="center", va="center",
            fontsize=10, color=p["fg"], weight="bold")

    # ---- Column 2: brokers ----
    total_b = sum(v for _, v in BROKERS)
    yb_top = 8.7
    yb_bot = 1.0
    span_b = yb_top - yb_bot
    broker_rects = []  # (y_center, height, label, value)
    cursor = yb_top
    for name, val in BROKERS:
        h = (val / total_b) * span_b * 0.95
        cursor -= h
        ax.add_patch(mpatches.FancyBboxPatch(
            (col_x[1], cursor), col_w, h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=p["blue"], alpha=0.78,
            edgecolor=p["blue"], linewidth=1.0))
        cy = cursor + h / 2
        ax.text(col_x[1] + col_w / 2, cy, f"{name}\nUS {val/1000:.2f}B",
                ha="center", va="center", fontsize=8.5, color="white",
                weight="bold")
        broker_rects.append((cy, h, name, val))
        cursor -= 0.06  # gap

    # ---- Column 3: wholesalers ----
    total_w = sum(v for _, v in WHOLESALERS)
    yw_top = 8.7
    yw_bot = 1.0
    span_w = yw_top - yw_bot
    whole_rects = []
    cursor = yw_top
    for name, val in WHOLESALERS:
        h = (val / total_w) * span_w * 0.95
        cursor -= h
        ax.add_patch(mpatches.FancyBboxPatch(
            (col_x[2], cursor), col_w, h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=p["red"], alpha=0.78,
            edgecolor=p["red"], linewidth=1.0))
        cy = cursor + h / 2
        ax.text(col_x[2] + col_w / 2, cy, f"{name}\nUS {val/1000:.2f}B",
                ha="center", va="center", fontsize=8.5, color="white",
                weight="bold")
        whole_rects.append((cy, h, name, val))
        cursor -= 0.06

    # ---- Column 4: venues (3 destinations) ----
    venues = [
        (s["venue_intern"], 0.70, p["red"]),     # 70% internalised
        (s["venue_lit"],    0.25, p["blue"]),    # 25% lit
        (s["venue_dark"],   0.05, p["purple"]),  # 5% dark pools
    ]
    yv_top = 8.7
    yv_bot = 1.0
    span_v = yv_top - yv_bot
    cursor = yv_top
    venue_rects = []
    for label, frac, col in venues:
        h = frac * span_v * 0.95
        cursor -= h
        ax.add_patch(mpatches.FancyBboxPatch(
            (col_x[3], cursor), col_w, h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=col, alpha=0.55,
            edgecolor=col, linewidth=1.0))
        cy = cursor + h / 2
        ax.text(col_x[3] + col_w / 2, cy, label,
                ha="center", va="center", fontsize=8.5, color=p["fg"],
                weight="bold")
        venue_rects.append((cy, h, col))
        cursor -= 0.06

    # ---- Flows: retail -> brokers (single fan) ----
    retail_cy = 5.25
    for cy, h, name, val in broker_rects:
        x0 = col_x[0] + col_w
        x1 = col_x[1]
        # Curve via cubic Bezier
        verts = [(x0, retail_cy), ((x0 + x1) / 2, retail_cy),
                 ((x0 + x1) / 2, cy), (x1, cy)]
        path = mpatches.Path(verts, [mpatches.Path.MOVETO, mpatches.Path.CURVE4,
                                      mpatches.Path.CURVE4, mpatches.Path.CURVE4])
        lw = max(0.6, 6 * val / total_b)
        ax.add_patch(mpatches.PathPatch(path, facecolor="none",
                                         edgecolor=p["accent"], alpha=0.45,
                                         linewidth=lw))

    # ---- Flows: brokers -> wholesalers (concentrated; assume each broker
    # routes proportionally to wholesaler size) ----
    for bcy, bh, bname, bval in broker_rects:
        for wcy, wh, wname, wval in whole_rects:
            share = wval / total_w
            x0 = col_x[1] + col_w
            x1 = col_x[2]
            verts = [(x0, bcy), ((x0 + x1) / 2, bcy),
                     ((x0 + x1) / 2, wcy), (x1, wcy)]
            path = mpatches.Path(verts, [mpatches.Path.MOVETO, mpatches.Path.CURVE4,
                                          mpatches.Path.CURVE4, mpatches.Path.CURVE4])
            lw = max(0.3, 4 * (bval / total_b) * share)
            ax.add_patch(mpatches.PathPatch(path, facecolor="none",
                                             edgecolor=p["muted"], alpha=0.30,
                                             linewidth=lw))

    # ---- Flows: wholesalers -> venues ----
    for wcy, wh, wname, wval in whole_rects:
        for vcy, vh, vcol in venue_rects:
            # use venue heights as flow weights
            x0 = col_x[2] + col_w
            x1 = col_x[3]
            verts = [(x0, wcy), ((x0 + x1) / 2, wcy),
                     ((x0 + x1) / 2, vcy), (x1, vcy)]
            path = mpatches.Path(verts, [mpatches.Path.MOVETO, mpatches.Path.CURVE4,
                                          mpatches.Path.CURVE4, mpatches.Path.CURVE4])
            lw = max(0.3, 5 * vh / span_v)
            ax.add_patch(mpatches.PathPatch(path, facecolor="none",
                                             edgecolor=vcol, alpha=0.30,
                                             linewidth=lw))

    # Total annotation removed; title already states $3.2B figure.

    # ---- Path note ----
    ax.text(0.1, 0.25, s["ann_path"], ha="left", va="bottom",
            fontsize=8.5, color=p["muted"], style="italic")

    # ---- Title and subtitle (suptitle on top, subtitle just below) ----
    fig.suptitle(s["title"], fontsize=14.5, fontweight="bold",
                 color=p["fg"], y=0.97)
    fig.text(0.5, 0.92, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.5, color=p["muted"])

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.0)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("left", "bottom", "top", "right"):
        ax.spines[spine].set_visible(False)
    ax.grid(False)

    fig.tight_layout(rect=[0, 0.04, 1, 0.89])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
