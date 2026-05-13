"""Week 7, §2.3 — Corporate capital stack diagram.

Vertical stacked-bar diagram showing the six tiers of claims on a
corporation's assets, from senior (top) to residual (bottom):
suppliers, employees, lenders/bondholders, tax authority, preferred
shareholders, common equity. The common-equity tier is shaded as a
wedge to indicate its residual, variable nature.

Run:
    uv run python course/image/week07_capital_stack.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week07_capital_stack"

LANG_STRINGS = {
    "en": {
        "title":    "The corporate capital stack — who gets paid first",
        "subtitle": "Senior claims at top; equity is the residual at the bottom.",
        "tiers":    ["Suppliers &\ntrade creditors", "Employees &\nwages", "Lenders &\nbondholders", "Tax authority\n(government)", "Preferred\nshareholders", "Common\nequity"],
        "senior":   "Fixed contractual claims\n(paid first in bankruptcy)",
        "residual": "Residual claim\n(variable — last paid,\nfirst to absorb losses,\nbut unlimited upside)",
        "profit_big":   "Large profit →\nwide equity slice",
        "profit_small": "Small profit →\nnarrow equity slice",
        "profit_zero":  "Business fails →\nequity = zero",
        "footer":   "Schematic. Relative tier sizes are illustrative, not to scale.",
    },
    "hk": {
        "title":    "企業資本結構 — 誰先獲賠",
        "subtitle": "優先債權在上;股東權益是最底層的剩餘索償。",
        "tiers":    ["供應商及\n商業債權人", "僱員及\n薪酬", "貸款人及\n債券持有人", "稅務機關\n(政府)", "優先股\n股東", "普通股\n股東權益"],
        "senior":   "固定合約索償\n(破產時優先支付)",
        "residual": "剩餘索償\n(可變 — 最遲支付,\n最先承受虧損,\n但上行空間不設限)",
        "profit_big":   "豐厚利潤 →\n股權比例大",
        "profit_small": "微利 →\n股權比例小",
        "profit_zero":  "企業倒閉 →\n股權歸零",
        "footer":   "示意圖。各層相對大小僅供說明,並非按比例繪製。",
    },
    "tw": {
        "title":    "企業資本結構 — 誰先獲償",
        "subtitle": "優先債權在上;股東權益是最底層的剩餘請求權。",
        "tiers":    ["供應商及\n交易債權人", "員工及\n薪資", "貸款人及\n債券持有人", "稅務機關\n(政府)", "特別股\n股東", "普通股\n股東權益"],
        "senior":   "固定合約債權\n(破產時優先清償)",
        "residual": "剩餘請求權\n(可變 — 最晚清償,\n最先承受虧損,\n但上漲空間無上限)",
        "profit_big":   "獲利豐厚 →\n股權份額大",
        "profit_small": "獲利微薄 →\n股權份額小",
        "profit_zero":  "企業倒閉 →\n股權歸零",
        "footer":   "示意圖。各層相對大小僅供說明,並非按比例繪製。",
    },
    "cn": {
        "title":    "企业资本结构 — 谁先获偿",
        "subtitle": "优先债权在上;股东权益是最底层的剩余索偿。",
        "tiers":    ["供应商及\n贸易债权人", "员工及\n工资", "贷款人及\n债券持有人", "税务机关\n(政府)", "优先股\n股东", "普通股\n股东权益"],
        "senior":   "固定合约索偿\n(破产时优先支付)",
        "residual": "剩余索偿\n(可变 — 最迟支付,\n最先承受亏损,\n但上行空间无上限)",
        "profit_big":   "丰厚利润 →\n股权比例大",
        "profit_small": "微利 →\n股权比例小",
        "profit_zero":  "企业倒闭 →\n股权归零",
        "footer":   "示意图。各层相对大小仅供说明,并非按比例绘制。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(10, 7.0))
    style_axes(ax, p)
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 7.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.grid(False)

    # Tier colours — senior tiers in cool blues/greys, equity in gold
    tier_colors = [
        "#5c6bc0",  # suppliers - indigo
        "#7986cb",  # employees - light indigo
        "#42a5f5",  # lenders - blue
        "#78909c",  # tax - blue-grey
        "#a1887f",  # preferred - brown
        p["accent"],  # common equity - gold
    ]
    tier_heights = [0.9, 0.9, 1.1, 0.8, 0.7, 1.5]
    bar_left = 2.5
    bar_width = 3.0

    y = 0.0
    tier_ys = []
    for i in range(6):
        h = tier_heights[i]
        alpha = 0.75 if i < 5 else 0.85
        rect = mpatches.FancyBboxPatch(
            (bar_left, y), bar_width, h,
            boxstyle="round,pad=0.05",
            facecolor=tier_colors[i], alpha=alpha,
            edgecolor=p["fg"], linewidth=1.2,
        )
        ax.add_patch(rect)
        # Label inside the tier
        ax.text(bar_left + bar_width / 2, y + h / 2, s["tiers"][5 - i],
                ha="center", va="center", fontsize=10, color="white",
                fontweight="bold")
        tier_ys.append(y)
        y += h + 0.1

    # Bracket annotation on the left for "fixed contractual claims"
    senior_bottom = tier_ys[1]
    senior_top = tier_ys[-1] + tier_heights[-1]
    ax.annotate("", xy=(bar_left - 0.3, senior_bottom),
                xytext=(bar_left - 0.3, senior_top),
                arrowprops=dict(arrowstyle="-", color=p["blue"], lw=1.5))
    ax.plot([bar_left - 0.45, bar_left - 0.15],
            [senior_bottom, senior_bottom], color=p["blue"], lw=1.5)
    ax.plot([bar_left - 0.45, bar_left - 0.15],
            [senior_top, senior_top], color=p["blue"], lw=1.5)
    ax.text(bar_left - 0.6, (senior_bottom + senior_top) / 2, s["senior"],
            ha="right", va="center", fontsize=9, color=p["blue"])

    # Bracket annotation on the right for equity residual
    eq_bottom = tier_ys[0]
    eq_top = tier_ys[0] + tier_heights[0]
    ax.annotate("", xy=(bar_left + bar_width + 0.3, eq_bottom),
                xytext=(bar_left + bar_width + 0.3, eq_top),
                arrowprops=dict(arrowstyle="-", color=p["accent"], lw=1.5))
    ax.plot([bar_left + bar_width + 0.15, bar_left + bar_width + 0.45],
            [eq_bottom, eq_bottom], color=p["accent"], lw=1.5)
    ax.plot([bar_left + bar_width + 0.15, bar_left + bar_width + 0.45],
            [eq_top, eq_top], color=p["accent"], lw=1.5)
    ax.text(bar_left + bar_width + 0.6, (eq_bottom + eq_top) / 2,
            s["residual"],
            ha="left", va="center", fontsize=9, color=p["accent"])

    # Three small scenario arrows on the far right showing equity variability
    scenarios = [
        (s["profit_big"], 0.25, p["green"]),
        (s["profit_small"], -0.6, p["orange"]),
        (s["profit_zero"], -1.4, p["red"]),
    ]
    x_scen = 8.5
    for label, y_off, clr in scenarios:
        y_pos = (eq_bottom + eq_top) / 2 + y_off
        ax.text(x_scen, y_pos, label, ha="center", va="center",
                fontsize=8.5, color=clr, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=p["bg"],
                          edgecolor=clr, alpha=0.8))

    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0.0, -0.06, s["footer"], transform=ax.transAxes,
            fontsize=8, color=p["muted"])
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for path in paths:
        print(f"wrote {path}")
