"""Side Lesson 07, §2.2 — VNQ sector composition (April 2026).

Horizontal bar chart of the sector weights inside Vanguard's REIT ETF
(VNQ), with bars coloured by category and the digital-infrastructure
theme (towers + data + logistics) called out as the modern majority.
Weights are MSCI US IM Real Estate 25/50 sector groupings rounded to
the nearest 0.5 per cent.

Run:
    uv run python course/image/side07_reit_sectors.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side07_reit_sectors"

# (key, weight_pct, category)
# category: 'digital' (towers/data), 'logistics', 'core' (resi/health/storage),
# 'legacy' (retail/office/hotel), 'specialty'
ROWS = [
    ("data",     15.0, "digital"),
    ("towers",   14.0, "digital"),
    ("indus",    10.0, "logistics"),
    ("resi",      9.0, "core"),
    ("health",    8.0, "core"),
    ("storage",   6.0, "core"),
    ("office",    5.0, "legacy"),
    ("retail",    4.0, "legacy"),
    ("hotel",     3.0, "legacy"),
    ("spec",     26.0, "specialty"),
]

LANG_STRINGS = {
    "en": {
        "title":    "VNQ sector composition — April 2026",
        "subtitle": "Modern public-REIT exposure is dominated by digital infrastructure and logistics. Malls and offices are minority slices.",
        "xlabel":   "Weight (%)",
        "footer":   "Source: Vanguard fact sheet, MSCI US IM Real Estate 25/50. Rounded to 0.5 per cent. 'Specialty' includes timber, gaming, prisons, and a small mortgage-REIT residual.",
        "labels": {
            "data":    "Data centres (EQIX, DLR)",
            "towers":  "Cell towers (AMT, CCI, SBAC)",
            "indus":   "Industrial logistics (PLD, EXR)",
            "resi":    "Residential apartments",
            "health":  "Healthcare (WELL, VTR)",
            "storage": "Self storage",
            "office":  "Office (BXP)",
            "retail":  "Retail and malls (SPG)",
            "hotel":   "Hotels and lodging",
            "spec":    "Specialty / other",
        },
        "legend": {
            "digital":   "Digital infrastructure",
            "logistics": "E-commerce logistics",
            "core":      "Resi / health / storage",
            "legacy":    "Office / retail / hotel",
            "specialty": "Specialty and other",
        },
        "callout": "Digital + logistics = 39%\nLegacy retail+office+hotel = 12%",
    },
    "hk": {
        "title":    "VNQ 行業構成 — 2026 年 4 月",
        "subtitle": "現代公開房託 ETF 主要由數碼基建及物流主導。商場和辦公樓只佔少數。",
        "xlabel":   "權重(%)",
        "footer":   "來源:Vanguard 概況、MSCI US IM Real Estate 25/50。四捨五入至 0.5%。「特殊」包括林業、博彩、監獄,以及小量按揭房託殘餘。",
        "labels": {
            "data":    "數據中心(EQIX、DLR)",
            "towers":  "電訊塔(AMT、CCI、SBAC)",
            "indus":   "工業物流(PLD、EXR)",
            "resi":    "住宅公寓",
            "health":  "醫療(WELL、VTR)",
            "storage": "迷你倉",
            "office":  "辦公室(BXP)",
            "retail":  "零售商場(SPG)",
            "hotel":   "酒店住宿",
            "spec":    "特殊 / 其他",
        },
        "legend": {
            "digital":   "數碼基建",
            "logistics": "電商物流",
            "core":      "住宅 / 醫療 / 倉儲",
            "legacy":    "辦公 / 零售 / 酒店",
            "specialty": "特殊及其他",
        },
        "callout": "數碼 + 物流 = 39%\n傳統零售+辦公+酒店 = 12%",
    },
    "tw": {
        "title":    "VNQ 產業組成 — 2026 年 4 月",
        "subtitle": "現代公開 REIT ETF 由數位基礎建設與物流主導。商場與辦公室只佔少數。",
        "xlabel":   "權重(%)",
        "footer":   "資料來源:Vanguard 概況、MSCI US IM Real Estate 25/50。四捨五入至 0.5%。「特殊」包括林業、博弈、監獄,及少量抵押 REIT 殘餘。",
        "labels": {
            "data":    "資料中心(EQIX、DLR)",
            "towers":  "通訊塔(AMT、CCI、SBAC)",
            "indus":   "工業物流(PLD、EXR)",
            "resi":    "住宅公寓",
            "health":  "醫療(WELL、VTR)",
            "storage": "自助倉儲",
            "office":  "辦公室(BXP)",
            "retail":  "零售商場(SPG)",
            "hotel":   "飯店住宿",
            "spec":    "特殊 / 其他",
        },
        "legend": {
            "digital":   "數位基礎建設",
            "logistics": "電商物流",
            "core":      "住宅 / 醫療 / 倉儲",
            "legacy":    "辦公 / 零售 / 飯店",
            "specialty": "特殊與其他",
        },
        "callout": "數位 + 物流 = 39%\n傳統零售+辦公+飯店 = 12%",
    },
    "cn": {
        "title":    "VNQ 行业构成 — 2026 年 4 月",
        "subtitle": "现代公开房托 ETF 主要由数字基建及物流主导。商场和办公楼只占少数。",
        "xlabel":   "权重(%)",
        "footer":   "来源:Vanguard 概况、MSCI US IM Real Estate 25/50。四舍五入至 0.5%。「特殊」包括林业、博彩、监狱,以及少量按揭房托残余。",
        "labels": {
            "data":    "数据中心(EQIX、DLR)",
            "towers":  "电信塔(AMT、CCI、SBAC)",
            "indus":   "工业物流(PLD、EXR)",
            "resi":    "住宅公寓",
            "health":  "医疗(WELL、VTR)",
            "storage": "迷你仓",
            "office":  "办公室(BXP)",
            "retail":  "零售商场(SPG)",
            "hotel":   "酒店住宿",
            "spec":    "特殊 / 其他",
        },
        "legend": {
            "digital":   "数字基建",
            "logistics": "电商物流",
            "core":      "住宅 / 医疗 / 仓储",
            "legacy":    "办公 / 零售 / 酒店",
            "specialty": "特殊及其他",
        },
        "callout": "数字 + 物流 = 39%\n传统零售+办公+酒店 = 12%",
    },
}


def _category_colors(p):
    return {
        "digital":   p["blue"],
        "logistics": p["accent"],
        "core":      p["green"],
        "legacy":    p["red"],
        "specialty": p["grey"],
    }


def build_fig(s):
    p = PALETTE_LIGHT
    cats = _category_colors(p)
    keys = [r[0] for r in ROWS]
    weights = [r[1] for r in ROWS]
    cat_keys = [r[2] for r in ROWS]
    labels = [s["labels"][k] for k in keys]
    colors = [cats[c] for c in cat_keys]

    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=150)
    style_axes(ax)

    y = np.arange(len(ROWS))[::-1]  # top to bottom
    bars = ax.barh(y, weights, color=colors, edgecolor="white",
                   linewidth=0.8, zorder=3, height=0.72)
    for bar, w in zip(bars, weights):
        ax.text(w + 0.4, bar.get_y() + bar.get_height() / 2,
                f"{w:.1f}%", va="center", ha="left",
                fontsize=10, fontweight="bold", color=p["fg"])

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_xlim(0, max(weights) * 1.18)

    # Category legend (top-right)
    handles = [plt.Rectangle((0, 0), 1, 1, color=cats[k])
               for k in ("digital", "logistics", "core", "legacy", "specialty")]
    leg_labels = [s["legend"][k]
                  for k in ("digital", "logistics", "core", "legacy", "specialty")]
    ax.legend(handles, leg_labels, loc="lower right", frameon=False,
              fontsize=9.0, ncol=1)

    # Callout box on the right
    ax.text(0.99, 0.62, s["callout"],
            transform=ax.transAxes, ha="right", va="top",
            fontsize=10, color=p["fg"], fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5",
                      facecolor=p["bg"], edgecolor=p["accent"], linewidth=1.2))

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.6, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
