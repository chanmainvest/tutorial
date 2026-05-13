"""Week 25, §2.6 - The four basic option positions at expiry.

A 2x2 grid of payoff diagrams (per share, at expiration) for the four
single-contract retail positions: long call, short call, long put,
short put. Each panel labels breakeven, max profit, and max loss so
the symmetry between buyer and seller, and between calls and puts,
reads at a glance. Reference strike K=$100, call premium c=$4,
put premium p=$4.

Run:
    uv run python course/image/week25_four_positions.py
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
BASE = "week25_four_positions"

K = 100.0
C = 4.0  # call premium
P = 4.0  # put premium


LANG_STRINGS = {
    "en": {
        "title":      "Four basic positions — long/short, call/put",
        "subtitle":   "Per-share payoff at expiry. Strike K=$100, call premium $4, put premium $4. Buyer and seller are exact mirrors.",
        "xlabel":     "Spot at expiry ($)",
        "ylabel":     "P&L per share ($)",
        "long_call":  "Long call (buy K=$100 call for $4)",
        "short_call": "Short call (sell K=$100 call for $4)",
        "long_put":   "Long put (buy K=$100 put for $4)",
        "short_put":  "Short put (sell K=$100 put for $4)",
        "lbl_be":         "breakeven",
        "lbl_maxp":       "max profit",
        "lbl_maxl":       "max loss",
        "lbl_unbounded":  "unbounded",
        "footer":     "P&L per share at expiry. Long positions cap loss at premium paid; short positions cap profit at premium received. Naked short call has unbounded loss.",
    },
    "hk": {
        "title":      "四種基本期權持倉 — 買/賣、認購/認沽",
        "subtitle":   "到期每股損益。行使價 K=$100、認購權利金 $4、認沽權利金 $4。買方和賣方完全對稱。",
        "xlabel":     "到期時現貨價(美元)",
        "ylabel":     "每股損益(美元)",
        "long_call":  "買認購(買 K=$100 認購,付 $4)",
        "short_call": "沽認購(沽 K=$100 認購,收 $4)",
        "long_put":   "買認沽(買 K=$100 認沽,付 $4)",
        "short_put":  "沽認沽(沽 K=$100 認沽,收 $4)",
        "lbl_be":         "打和點",
        "lbl_maxp":       "最大利潤",
        "lbl_maxl":       "最大虧損",
        "lbl_unbounded":  "無上限",
        "footer":     "到期每股損益。買方虧損封頂於所付權利金,賣方利潤封頂於所收權利金。裸沽認購虧損無上限。",
    },
    "tw": {
        "title":      "四種基本選擇權部位 — 買/賣、買權/賣權",
        "subtitle":   "到期每股損益。履約價 K=$100、買權權利金 $4、賣權權利金 $4。買方與賣方完全對稱。",
        "xlabel":     "到期時現貨價(美元)",
        "ylabel":     "每股損益(美元)",
        "long_call":  "買進買權(買 K=$100 買權,付 $4)",
        "short_call": "賣出買權(賣 K=$100 買權,收 $4)",
        "long_put":   "買進賣權(買 K=$100 賣權,付 $4)",
        "short_put":  "賣出賣權(賣 K=$100 賣權,收 $4)",
        "lbl_be":         "損益兩平",
        "lbl_maxp":       "最大利潤",
        "lbl_maxl":       "最大虧損",
        "lbl_unbounded":  "無上限",
        "footer":     "到期每股損益。買方虧損封頂於所付權利金,賣方利潤封頂於所收權利金。裸賣買權虧損無上限。",
    },
    "cn": {
        "title":      "四种基本期权持仓 — 买/卖、看涨/看跌",
        "subtitle":   "到期每股损益。行权价 K=$100、看涨权利金 $4、看跌权利金 $4。买方和卖方完全对称。",
        "xlabel":     "到期时现货价(美元)",
        "ylabel":     "每股损益(美元)",
        "long_call":  "买入看涨(买 K=$100 看涨,付 $4)",
        "short_call": "卖出看涨(卖 K=$100 看涨,收 $4)",
        "long_put":   "买入看跌(买 K=$100 看跌,付 $4)",
        "short_put":  "卖出看跌(卖 K=$100 看跌,收 $4)",
        "lbl_be":         "盈亏平衡",
        "lbl_maxp":       "最大利润",
        "lbl_maxl":       "最大亏损",
        "lbl_unbounded":  "无上限",
        "footer":     "到期每股损益。买方亏损封顶于所付权利金,卖方利润封顶于所收权利金。裸卖看涨亏损无上限。",
    },
}


def _annotate_band(ax, text, x, y, color, p):
    ax.annotate(text, xy=(x, y), xytext=(x, y),
                fontsize=8.6, color=color, ha="center", va="center")


def build_fig(s):
    p = PALETTE_LIGHT
    apply_cjk_font()

    # Escape '$' for matplotlib mathtext (breaks CJK).
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    S = np.linspace(50.0, 150.0, 401)

    long_call_pnl  = np.maximum(S - K, 0.0) - C
    short_call_pnl = -long_call_pnl
    long_put_pnl   = np.maximum(K - S, 0.0) - P
    short_put_pnl  = -long_put_pnl

    fig, axes = plt.subplots(2, 2, figsize=(12.0, 7.6), dpi=160)
    fig.patch.set_facecolor(p["bg"])

    panels = [
        # (ax, pnl, title, kind)
        (axes[0, 0], long_call_pnl,  s["long_call"],  "long_call"),
        (axes[0, 1], short_call_pnl, s["short_call"], "short_call"),
        (axes[1, 0], long_put_pnl,   s["long_put"],   "long_put"),
        (axes[1, 1], short_put_pnl,  s["short_put"],  "short_put"),
    ]

    for ax, pnl, title, kind in panels:
        style_axes(ax, p)
        ax.fill_between(S, pnl, 0, where=(pnl >= 0),
                        color=p["green"], alpha=0.10, linewidth=0)
        ax.fill_between(S, pnl, 0, where=(pnl < 0),
                        color=p["red"], alpha=0.10, linewidth=0)

        line_color = p["green"] if "long" in kind else p["red"]
        ax.plot(S, pnl, color=line_color, linewidth=2.4)

        ax.axhline(0, color=p["muted"], linewidth=0.8, alpha=0.6)
        ax.axvline(K, color=p["muted"], linewidth=0.7, linestyle=":", alpha=0.6)

        ax.set_xlim(50, 150)
        ax.set_ylim(-22, 22)
        ax.set_xlabel(s["xlabel"], fontsize=9)
        ax.set_ylabel(s["ylabel"], fontsize=9)
        ax.set_title(title, fontsize=10.5, fontweight="bold", loc="left",
                     color=p["fg"], pad=8)
        ax.set_xticks([50, 75, 100, 125, 150])
        ax.set_yticks([-20, -10, 0, 10, 20])

        # Per-panel annotations.
        if kind == "long_call":
            be = K + C
            ax.scatter([be], [0], color=p["accent"], s=28, zorder=5)
            ax.annotate(f"{s['lbl_be']} = \\$104",
                        xy=(be, 0), xytext=(be + 4, -7),
                        fontsize=8.5, color=p["accent"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxl']} = -\\$4", xy=(70, -C), xytext=(55, -16),
                        fontsize=8.5, color=p["red"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxp']} ({s['lbl_unbounded']})",
                        xy=(140, 36), xytext=(108, 16),
                        fontsize=8.5, color=p["green"], ha="left")
        elif kind == "short_call":
            be = K + C
            ax.scatter([be], [0], color=p["accent"], s=28, zorder=5)
            ax.annotate(f"{s['lbl_be']} = \\$104",
                        xy=(be, 0), xytext=(be + 4, 7),
                        fontsize=8.5, color=p["accent"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxp']} = +\\$4", xy=(70, C), xytext=(55, 16),
                        fontsize=8.5, color=p["green"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxl']} ({s['lbl_unbounded']})",
                        xy=(140, -36), xytext=(108, -16),
                        fontsize=8.5, color=p["red"], ha="left")
        elif kind == "long_put":
            be = K - P
            ax.scatter([be], [0], color=p["accent"], s=28, zorder=5)
            ax.annotate(f"{s['lbl_be']} = \\$96",
                        xy=(be, 0), xytext=(be - 18, -7),
                        fontsize=8.5, color=p["accent"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxl']} = -\\$4", xy=(130, -P), xytext=(115, -16),
                        fontsize=8.5, color=p["red"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxp']} = +\\$96 (S->0)",
                        xy=(50, 96 - P), xytext=(55, 16),
                        fontsize=8.5, color=p["green"], ha="left")
        elif kind == "short_put":
            be = K - P
            ax.scatter([be], [0], color=p["accent"], s=28, zorder=5)
            ax.annotate(f"{s['lbl_be']} = \\$96",
                        xy=(be, 0), xytext=(be - 18, 7),
                        fontsize=8.5, color=p["accent"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxp']} = +\\$4", xy=(130, P), xytext=(115, 16),
                        fontsize=8.5, color=p["green"],
                        arrowprops=dict(arrowstyle="-", color=p["muted"], lw=0.7))
            ax.annotate(f"{s['lbl_maxl']} = -\\$96 (S->0)",
                        xy=(50, -(96 - P)), xytext=(55, -16),
                        fontsize=8.5, color=p["red"], ha="left")

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
