"""Week 13, §2.2 - Payoff diagrams (long stock, short stock, long call, long put).

A 2x2 grid showing the four canonical payoff shapes a retail investor
encounters. The two top panels are linear (stock); the bottom two are
the option-based "constructive" versions with capped loss. This is the
visual companion to SOUL #14 (the barbell): options reshape the linear
stock payoff into asymmetric, capped-loss structures.

Run:
    uv run python course/image/week13_payoff_diagrams.py
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

OUT_DIR = Path(__file__).parent
BASE = "week13_payoff_diagrams"

# Reference: entry / strike at $100, premium = $5.
ENTRY = 100.0
PREMIUM = 5.0


LANG_STRINGS = {
    "en": {
        "title":      "Four payoff shapes — long, short, long call, long put",
        "subtitle":   "Stock payoffs are linear and unbounded; options cap the loss at the premium and reshape the payoff into a barbell.",
        "xlabel":     "Stock price at exit ($)",
        "ylabel":     "P&L per share ($)",
        "long_stock":  "Long stock (entry $100)",
        "short_stock": "Short stock (entry $100)",
        "long_call":   "Long $100 call (premium $5)",
        "long_put":    "Long $100 put (premium $5)",
        "lbl_loss_cap":  "loss capped at $100",
        "lbl_loss_inf":  "loss unbounded above",
        "lbl_prem":      "loss capped at $5 premium",
        "lbl_gain_inf":  "upside unlimited",
        "lbl_gain_cap":  "upside capped (strike → 0)",
        "footer":      "Entry / strike $100, option premium $5. Stock can't fall below 0; can in principle rise indefinitely.",
    },
    "hk": {
        "title":      "四種損益形態 — 做多、做空、買權、賣權",
        "subtitle":   "股票損益線性且無上限;期權把損失封頂在權利金,重塑為槓鈴形態。",
        "xlabel":     "出場時股價(美元)",
        "ylabel":     "每股損益(美元)",
        "long_stock":  "做多股票(入場 $100)",
        "short_stock": "做空股票(入場 $100)",
        "long_call":   "買入 $100 認購期權(權利金 $5)",
        "long_put":    "買入 $100 認沽期權(權利金 $5)",
        "lbl_loss_cap":  "最大虧損 $100",
        "lbl_loss_inf":  "虧損無上限",
        "lbl_prem":      "最大虧損 = 權利金 $5",
        "lbl_gain_inf":  "升幅無上限",
        "lbl_gain_cap":  "升幅有頂(行使價→0)",
        "footer":      "入場 / 行使價 $100、權利金 $5。股價不能跌穿 0,理論上可無限上升。",
    },
    "tw": {
        "title":      "四種損益形態 — 做多、做空、買權、賣權",
        "subtitle":   "股票損益線性且無上限;選擇權把損失封頂於權利金,重塑為槓鈴形態。",
        "xlabel":     "出場時股價(美元)",
        "ylabel":     "每股損益(美元)",
        "long_stock":  "做多股票(進場 $100)",
        "short_stock": "做空股票(進場 $100)",
        "long_call":   "買入 $100 買權(權利金 $5)",
        "long_put":    "買入 $100 賣權(權利金 $5)",
        "lbl_loss_cap":  "最大虧損 $100",
        "lbl_loss_inf":  "虧損無上限",
        "lbl_prem":      "最大虧損 = 權利金 $5",
        "lbl_gain_inf":  "上漲無上限",
        "lbl_gain_cap":  "上漲有頂(履約價→0)",
        "footer":      "進場 / 履約價 $100、權利金 $5。股價不能跌破 0,理論上可無限上漲。",
    },
    "cn": {
        "title":      "四种损益形态 — 做多、做空、买权、卖权",
        "subtitle":   "股票损益线性且无上限;期权把损失封顶在权利金,重塑为杠铃形态。",
        "xlabel":     "出场时股价(美元)",
        "ylabel":     "每股损益(美元)",
        "long_stock":  "做多股票(入场 $100)",
        "short_stock": "做空股票(入场 $100)",
        "long_call":   "买入 $100 看涨期权(权利金 $5)",
        "long_put":    "买入 $100 看跌期权(权利金 $5)",
        "lbl_loss_cap":  "最大亏损 $100",
        "lbl_loss_inf":  "亏损无上限",
        "lbl_prem":      "最大亏损 = 权利金 $5",
        "lbl_gain_inf":  "升幅无上限",
        "lbl_gain_cap":  "升幅有顶(行权价→0)",
        "footer":      "入场 / 行权价 $100、权利金 $5。股价不能跌破 0,理论上可无限上涨。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    apply_cjk_font()

    # Escape '$' so matplotlib does not enter mathtext mode (breaks CJK glyphs).
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    x = np.linspace(0, 220, 401)

    # P&L curves (per share)
    long_stock  = x - ENTRY
    short_stock = ENTRY - x
    long_call   = np.maximum(x - ENTRY, 0.0) - PREMIUM
    long_put    = np.maximum(ENTRY - x, 0.0) - PREMIUM

    fig, axes = plt.subplots(2, 2, figsize=(11.5, 7.6), dpi=160)
    fig.patch.set_facecolor(p["bg"])

    panels = [
        (axes[0, 0], long_stock,  s["long_stock"],  p["green"],  "long"),
        (axes[0, 1], short_stock, s["short_stock"], p["red"],    "short"),
        (axes[1, 0], long_call,   s["long_call"],   p["accent"], "call"),
        (axes[1, 1], long_put,    s["long_put"],    p["blue"],   "put"),
    ]

    for ax, pnl, title, color, kind in panels:
        style_axes(ax, p)
        # Shade gain / loss regions lightly
        ax.fill_between(x, pnl, 0, where=(pnl >= 0),
                        color=p["green"], alpha=0.10, linewidth=0)
        ax.fill_between(x, pnl, 0, where=(pnl < 0),
                        color=p["red"], alpha=0.10, linewidth=0)
        ax.plot(x, pnl, color=color, linewidth=2.4)
        ax.axhline(0, color=p["muted"], linewidth=0.8, linestyle="-", alpha=0.6)
        ax.axvline(ENTRY, color=p["muted"], linewidth=0.7, linestyle=":",
                   alpha=0.6)

        ax.set_xlim(0, 220)
        ax.set_ylim(-130, 130)
        ax.set_xlabel(s["xlabel"], fontsize=9)
        ax.set_ylabel(s["ylabel"], fontsize=9)
        ax.set_title(title, fontsize=11, fontweight="bold", loc="left",
                     color=p["fg"], pad=8)

        # Annotations specific to each panel.
        if kind == "long":
            ax.annotate(s["lbl_loss_cap"], xy=(2, -100), xytext=(15, -110),
                        fontsize=8.5, color=p["red"])
            ax.annotate(s["lbl_gain_inf"], xy=(215, 115), xytext=(115, 95),
                        fontsize=8.5, color=p["green"], ha="left")
        elif kind == "short":
            ax.annotate(s["lbl_loss_inf"], xy=(215, -115), xytext=(115, -100),
                        fontsize=8.5, color=p["red"], ha="left")
            ax.annotate(s["lbl_gain_cap"], xy=(2, 100), xytext=(8, 110),
                        fontsize=8.5, color=p["green"])
        elif kind == "call":
            ax.annotate(s["lbl_prem"], xy=(50, -PREMIUM),
                        xytext=(15, -35), fontsize=8.5, color=p["red"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"],
                                        lw=0.7))
            ax.annotate(s["lbl_gain_inf"], xy=(210, 105), xytext=(115, 90),
                        fontsize=8.5, color=p["green"], ha="left")
        elif kind == "put":
            ax.annotate(s["lbl_prem"], xy=(150, -PREMIUM),
                        xytext=(115, -35), fontsize=8.5, color=p["red"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"],
                                        lw=0.7))
            ax.annotate(s["lbl_gain_cap"], xy=(5, 90), xytext=(8, 105),
                        fontsize=8.5, color=p["green"])

        ax.set_xticks([0, 50, 100, 150, 200])

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
