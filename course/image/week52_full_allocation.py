"""Week 52, §2.2 — Pie chart of the model L4 allocation.

Seven sleeves, grouped under SOUL #13's four-tranche framework:
35% global equity (growth), 25% income, 15% gold + 5% BTC (store-of-value),
10% CTA + 5% tail-hedge (opportunistic), 5% cash. Rendered as a donut with
slice labels in the perimeter and a tranche-summary footer underneath.

Run:
    uv run python course/image/week52_full_allocation.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
    apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week52_full_allocation"

# Sleeve order: equity, income, gold, btc, cta, tail, cash
KEYS   = ["equity", "income", "gold", "btc", "cta", "tail", "cash"]
WEIGHT = [   35,       25,      15,     5,    10,    5,      5  ]


def _palette_for_keys():
    p = PALETTE_LIGHT
    return {
        "equity": p["blue"],
        "income": p["red"],
        "gold":   p["accent"],
        "btc":    p["purple"],
        "cta":    p["teal"],
        "tail":   p["orange"],
        "cash":   p["grey"],
    }


LANG_STRINGS = {
    "en": {
        "title":    "Model L4 allocation: seven sleeves, four tranches",
        "subtitle": "35/25/15/5/10/5/5 -- the four-tranche barbell as a working portfolio (SOUL #13, #14).",
        "centre":   "L4\nmodel",
        "labels": {
            "equity": "Global equity\n(VTI/AVUV/MTUM)\n35%",
            "income": "Income\n(BND/SCHD/JEPI)\n25%",
            "gold":   "Gold\n(GLDM)\n15%",
            "btc":    "BTC (IBIT)\n5%",
            "cta":    "CTA\n(DBMF)\n10%",
            "tail":   "Tail hedge\n(SPY puts)\n5%",
            "cash":   "Cash\n(SGOV)\n5%",
        },
        "footer": "Growth 35% | Income 25% | Store-of-value 20% (gold+BTC) | Opportunistic 15% (CTA+tail) | Cash 5%",
    },
    "hk": {
        "title":    "L4 模型配置:七板塊、四層級",
        "subtitle": "35/25/15/5/10/5/5 -- 四層級槓鈴變成可運作組合(SOUL #13、#14)。",
        "centre":   "L4\n模型",
        "labels": {
            "equity": "全球股票\n(VTI/AVUV/MTUM)\n35%",
            "income": "收益\n(BND/SCHD/JEPI)\n25%",
            "gold":   "黃金\n(GLDM)\n15%",
            "btc":    "比特幣 (IBIT)\n5%",
            "cta":    "CTA\n(DBMF)\n10%",
            "tail":   "尾部對沖\n(SPY 認沽)\n5%",
            "cash":   "現金\n(SGOV)\n5%",
        },
        "footer": "增長 35% | 收益 25% | 價值儲存 20%(金+BTC) | 機會 15%(CTA+尾部) | 現金 5%",
    },
    "tw": {
        "title":    "L4 模型配置:七板塊、四層級",
        "subtitle": "35/25/15/5/10/5/5 -- 四層級槓鈴變成可執行組合(SOUL #13、#14)。",
        "centre":   "L4\n模型",
        "labels": {
            "equity": "全球股票\n(VTI/AVUV/MTUM)\n35%",
            "income": "收益\n(BND/SCHD/JEPI)\n25%",
            "gold":   "黃金\n(GLDM)\n15%",
            "btc":    "比特幣 (IBIT)\n5%",
            "cta":    "CTA\n(DBMF)\n10%",
            "tail":   "尾部避險\n(SPY 賣權)\n5%",
            "cash":   "現金\n(SGOV)\n5%",
        },
        "footer": "增長 35% | 收益 25% | 價值儲存 20%(金+BTC) | 機會 15%(CTA+尾部) | 現金 5%",
    },
    "cn": {
        "title":    "L4 模型配置:七板块、四层级",
        "subtitle": "35/25/15/5/10/5/5 -- 四层级杠铃变成可运作组合(SOUL #13、#14)。",
        "centre":   "L4\n模型",
        "labels": {
            "equity": "全球股票\n(VTI/AVUV/MTUM)\n35%",
            "income": "收益\n(BND/SCHD/JEPI)\n25%",
            "gold":   "黄金\n(GLDM)\n15%",
            "btc":    "比特币 (IBIT)\n5%",
            "cta":    "CTA\n(DBMF)\n10%",
            "tail":   "尾部对冲\n(SPY 看跌)\n5%",
            "cash":   "现金\n(SGOV)\n5%",
        },
        "footer": "增长 35% | 收益 25% | 价值储存 20%(金+BTC) | 机会 15%(CTA+尾部) | 现金 5%",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    cols_map = _palette_for_keys()
    cols   = [cols_map[k] for k in KEYS]
    labels = [s["labels"][k] for k in KEYS]

    fig, ax = plt.subplots(figsize=(11.5, 7.4), dpi=150)
    ax.set_facecolor(p["bg"])
    fig.patch.set_facecolor(p["bg"])
    ax.set_aspect("equal")
    ax.axis("off")

    wedges, _ = ax.pie(
        WEIGHT, colors=cols, startangle=90, counterclock=False,
        wedgeprops=dict(width=0.40, edgecolor=p["bg"], linewidth=2.0),
    )

    # Annotate each wedge with a label outside the donut.
    for w, lab in zip(wedges, labels):
        ang = 0.5 * (w.theta1 + w.theta2)
        rad = np.deg2rad(ang)
        x = np.cos(rad)
        y = np.sin(rad)
        ha = "left" if x >= 0 else "right"
        ax.annotate(
            lab,
            xy=(x * 0.85, y * 0.85),
            xytext=(x * 1.18, y * 1.18),
            ha=ha, va="center",
            fontsize=10.5, color=p["fg"],
            arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7),
        )

    # Centre label.
    ax.text(0, 0, s["centre"], ha="center", va="center",
            fontsize=18, fontweight="bold", color=p["fg"])

    # Title + subtitle + footer.
    fig.suptitle(s["title"], fontsize=15, fontweight="bold",
                 color=p["fg"], y=0.97)
    fig.text(0.5, 0.915, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.04, s["footer"], ha="center",
             fontsize=10.0, color=p["fg"])

    fig.subplots_adjust(left=0.10, right=0.90, top=0.88, bottom=0.10)
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
