"""Week 15, §2.2 — Growth × inflation 2x2 grid.

Bridgewater all-weather quadrants. Each cell shows:
- the macro signature (growth direction, inflation direction)
- the winning asset class
- a historical decade anchor

Run:
    uv run python course/image/week15_quadrants.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week15_quadrants"


LANG_STRINGS = {
    "en": {
        "title":    "The four all-weather quadrants",
        "subtitle": "Each cell has a winning asset class. A diversified book holds one position in every cell.",
        "axis_x":   "Inflation surprise",
        "axis_y":   "Growth surprise",
        "lo":       "lower",
        "hi":       "higher",
        "tl_h":     "Reflation",
        "tl_a":     "Commodities · EM equity\nGold (late cycle)",
        "tl_e":     "2003-2007 · 2021",
        "tr_h":     "Goldilocks",
        "tr_a":     "DM equity · growth\nstocks · credit",
        "tr_e":     "1991-1999 · 2013-2019",
        "bl_h":     "Stagflation",
        "bl_a":     "Gold · TIPS\nshort-duration cash",
        "bl_e":     "1973-74 · 1979-80 · 2022",
        "br_h":     "Deflationary recession",
        "br_a":     "Long-dur. Treasuries\ndefensive equity · USD",
        "br_e":     "2001-02 · 2008-09 · 2020",
        "footer":   "Growth surprise = realised growth minus expected growth. Inflation surprise = realised CPI minus expected CPI. Source: Bridgewater All-Weather framework (1996), historical anchoring by author.",
    },
    "hk": {
        "title":    "四個全天候象限",
        "subtitle": "每個象限都有對應贏家資產類別。多元化組合在每個象限都持有一份倉位。",
        "axis_x":   "通脹意外",
        "axis_y":   "增長意外",
        "lo":       "低於預期",
        "hi":       "高於預期",
        "tl_h":     "再通脹",
        "tl_a":     "商品 · 新興市場股票\n黃金(後期)",
        "tl_e":     "2003-2007 · 2021",
        "tr_h":     "金髮女孩",
        "tr_a":     "成熟市場股票 · 成長股\n信用債",
        "tr_e":     "1991-1999 · 2013-2019",
        "bl_h":     "停滯性通脹",
        "bl_a":     "黃金 · TIPS\n短久期現金",
        "bl_e":     "1973-74 · 1979-80 · 2022",
        "br_h":     "通縮型衰退",
        "br_a":     "長久期國債\n防守性股票 · 美元",
        "br_e":     "2001-02 · 2008-09 · 2020",
        "footer":   "增長意外 = 實際增長 - 預期增長;通脹意外 = 實際 CPI - 預期 CPI。來源:橋水全天候框架(1996),歷史對照由作者整理。",
    },
    "tw": {
        "title":    "四個全天候象限",
        "subtitle": "每個象限都有對應贏家資產類別。多元化組合在每個象限都持有一份部位。",
        "axis_x":   "通膨意外",
        "axis_y":   "成長意外",
        "lo":       "低於預期",
        "hi":       "高於預期",
        "tl_h":     "再通膨",
        "tl_a":     "商品 · 新興市場股票\n黃金(後期)",
        "tl_e":     "2003-2007 · 2021",
        "tr_h":     "金髮女孩",
        "tr_a":     "成熟市場股票 · 成長股\n信用債",
        "tr_e":     "1991-1999 · 2013-2019",
        "bl_h":     "停滯性通膨",
        "bl_a":     "黃金 · TIPS\n短存續期現金",
        "bl_e":     "1973-74 · 1979-80 · 2022",
        "br_h":     "通縮型衰退",
        "br_a":     "長存續期公債\n防禦性股票 · 美元",
        "br_e":     "2001-02 · 2008-09 · 2020",
        "footer":   "成長意外 = 實際成長 - 預期成長;通膨意外 = 實際 CPI - 預期 CPI。來源:橋水全天候框架(1996),歷史對照由作者整理。",
    },
    "cn": {
        "title":    "四个全天候象限",
        "subtitle": "每个象限都有对应赢家资产类别。多元化组合在每个象限都持有一份仓位。",
        "axis_x":   "通胀意外",
        "axis_y":   "增长意外",
        "lo":       "低于预期",
        "hi":       "高于预期",
        "tl_h":     "再通胀",
        "tl_a":     "商品 · 新兴市场股票\n黄金(后期)",
        "tl_e":     "2003-2007 · 2021",
        "tr_h":     "金发女孩",
        "tr_a":     "成熟市场股票 · 成长股\n信用债",
        "tr_e":     "1991-1999 · 2013-2019",
        "bl_h":     "停滞性通胀",
        "bl_a":     "黄金 · TIPS\n短久期现金",
        "bl_e":     "1973-74 · 1979-80 · 2022",
        "br_h":     "通缩型衰退",
        "br_a":     "长久期国债\n防御性股票 · 美元",
        "br_e":     "2001-02 · 2008-09 · 2020",
        "footer":   "增长意外 = 实际增长 - 预期增长;通胀意外 = 实际 CPI - 预期 CPI。来源:桥水全天候框架(1996),历史对照由作者整理。",
    },
}


def _cell(ax, x, y, w, h, color, header, asset, era, p):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        linewidth=2.0, edgecolor=color, facecolor=color + "18",
    )
    ax.add_patch(rect)
    cx = x + w / 2.0
    ax.text(cx, y + h - 0.10, header,
            ha="center", va="top", fontsize=14, fontweight="bold", color=color)
    ax.text(cx, y + h / 2.0 + 0.02, asset,
            ha="center", va="center", fontsize=11, color=p["fg"])
    ax.text(cx, y + 0.07, era,
            ha="center", va="bottom", fontsize=9.5,
            color=p["muted"], style="italic")


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.6), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    ax.set_facecolor(p["bg"])

    # Cells: top-left, top-right, bottom-left, bottom-right
    _cell(ax, 0.05, 1.05, 0.90, 0.90, p["orange"], s["tl_h"], s["tl_a"], s["tl_e"], p)
    _cell(ax, 1.05, 1.05, 0.90, 0.90, p["green"],  s["tr_h"], s["tr_a"], s["tr_e"], p)
    _cell(ax, 0.05, 0.05, 0.90, 0.90, p["red"],    s["bl_h"], s["bl_a"], s["bl_e"], p)
    _cell(ax, 1.05, 0.05, 0.90, 0.90, p["blue"],   s["br_h"], s["br_a"], s["br_e"], p)

    # Axis arrows + labels
    ax.annotate("", xy=(2.10, 1.0), xytext=(-0.05, 1.0),
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=1.2))
    ax.annotate("", xy=(1.0, 2.10), xytext=(1.0, -0.05),
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=1.2))

    ax.text(2.12, 1.0, s["axis_x"], va="center", ha="left",
            fontsize=10.5, color=p["muted"], fontweight="bold")
    ax.text(1.0, 2.12, s["axis_y"], va="bottom", ha="center",
            fontsize=10.5, color=p["muted"], fontweight="bold")

    # Inflation low/high markers (axis x)
    ax.text(0.50, 1.02, s["lo"], ha="center", va="bottom",
            fontsize=9, color=p["muted"])
    ax.text(1.50, 1.02, s["hi"], ha="center", va="bottom",
            fontsize=9, color=p["muted"])
    # Growth low/high markers (axis y)
    ax.text(0.98, 0.50, s["lo"], ha="right", va="center",
            fontsize=9, color=p["muted"])
    ax.text(0.98, 1.50, s["hi"], ha="right", va="center",
            fontsize=9, color=p["muted"])

    ax.set_xlim(-0.10, 2.30)
    ax.set_ylim(-0.10, 2.30)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.suptitle(s["title"], fontsize=15, fontweight="bold", y=0.98)
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.03, s["footer"], ha="center",
             fontsize=8.5, color=p["muted"])

    fig.tight_layout(rect=[0, 0.05, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
