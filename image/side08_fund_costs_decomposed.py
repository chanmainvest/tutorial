"""Side 08, sec 2.1 -- Total cost of ownership decomposed by fund type.

Stacked horizontal bar showing expense ratio + transaction cost +
bid-ask + (hedge fund) performance fee for four fund types:

- Index ETF (e.g. VTI): 3 + 1 + 1 = 5 bp
- Passive mutual fund (VTSAX): 4 + 2 + 0 = 6 bp (drawn as 15 to
  show the average passive MF including older institutional MFs)
- Active mutual fund (typical retail): 75 + 25 + 0 = 100 bp
- Hedge fund (2/20 on a 10% gross year): 200 + 40 + 10 + 120 = 370 bp

Run:
    uv run python course/image/side08_fund_costs_decomposed.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side08_fund_costs_decomposed"


# Cost components in basis points
# Each row: (er, txn, bidask, perf)
DATA = {
    "etf":    (3,   1,   1,   0),
    "passive":(12,  3,   0,   0),
    "active": (75,  25,  0,   0),
    "hedge":  (200, 40,  10,  120),
}
ORDER = ["etf", "passive", "active", "hedge"]


LANG_STRINGS = {
    "en": {
        "title": "Total Cost of Ownership by Fund Type (bp/yr, on a 10% gross year)",
        "subtitle": "The headline expense ratio is rarely the whole fee. Stacked bars show ER + transaction cost + bid-ask + (hedge fund) performance fee.",
        "xlabel": "Total cost of ownership (basis points per year)",
        "fund_labels": {
            "etf":     "Index ETF\n(VTI / IVV / SPLG)",
            "passive": "Passive MF\n(VTSAX / VFIAX)",
            "active":  "Active MF\n(typical retail)",
            "hedge":   "Hedge fund\n(2/20 on 10% gross)",
        },
        "comp_labels": ["Expense ratio", "Transaction cost", "Bid-ask spread", "Performance fee"],
        "total_lbl": "{:.0f} bp",
        "footnote": "Approximate component breakdown per Morningstar 2024 fee study + ICI/CEM transaction-cost estimates. ETF bid-ask is the spread retail crosses on a single round-trip; mutual-fund bid-ask is paid indirectly through cash-flow management.",
    },
    "hk": {
        "title": "各類基金的總持有成本(年化基點,10% 毛回報情境)",
        "subtitle": "標明的管理費極少等於全部費用。堆疊條顯示管理費 + 交易成本 + 買賣價差 +(對沖基金)表現費。",
        "xlabel": "總持有成本(年化基點)",
        "fund_labels": {
            "etf":     "指數 ETF\n(VTI / IVV / SPLG)",
            "passive": "被動共同基金\n(VTSAX / VFIAX)",
            "active":  "主動共同基金\n(典型零售)",
            "hedge":   "對沖基金\n(2/20 於 10% 毛回報)",
        },
        "comp_labels": ["管理費", "交易成本", "買賣價差", "表現費"],
        "total_lbl": "{:.0f} 基點",
        "footnote": "近似拆解,參考 Morningstar 2024 費用研究與 ICI / CEM 交易成本估算。ETF 買賣價差為散戶單次往返支付;共同基金買賣價差透過現金流管理間接承擔。",
    },
    "tw": {
        "title": "各類基金的總持有成本(年化基點,10% 毛報酬情境)",
        "subtitle": "標明的管理費極少等於全部費用。堆疊條顯示管理費 + 交易成本 + 買賣價差 +(避險基金)績效費。",
        "xlabel": "總持有成本(年化基點)",
        "fund_labels": {
            "etf":     "指數 ETF\n(VTI / IVV / SPLG)",
            "passive": "被動共同基金\n(VTSAX / VFIAX)",
            "active":  "主動共同基金\n(典型零售)",
            "hedge":   "避險基金\n(2/20 於 10% 毛報酬)",
        },
        "comp_labels": ["管理費", "交易成本", "買賣價差", "績效費"],
        "total_lbl": "{:.0f} 基點",
        "footnote": "近似拆解,參考 Morningstar 2024 費用研究與 ICI / CEM 交易成本估算。ETF 買賣價差為散戶單次往返支付;共同基金買賣價差透過現金流管理間接承擔。",
    },
    "cn": {
        "title": "各类基金的总持有成本(年化基点,10% 毛回报情境)",
        "subtitle": "标明的管理费极少等于全部费用。堆叠条显示管理费 + 交易成本 + 买卖价差 +(对冲基金)业绩费。",
        "xlabel": "总持有成本(年化基点)",
        "fund_labels": {
            "etf":     "指数 ETF\n(VTI / IVV / SPLG)",
            "passive": "被动共同基金\n(VTSAX / VFIAX)",
            "active":  "主动共同基金\n(典型零售)",
            "hedge":   "对冲基金\n(2/20 于 10% 毛回报)",
        },
        "comp_labels": ["管理费", "交易成本", "买卖价差", "业绩费"],
        "total_lbl": "{:.0f} 基点",
        "footnote": "近似拆解,参考 Morningstar 2024 费用研究与 ICI / CEM 交易成本估算。ETF 买卖价差为散户单次往返支付;共同基金买卖价差通过现金流管理间接承担。",
    },
}

COMP_COLORS = [
    PALETTE_LIGHT["blue"],     # ER
    PALETTE_LIGHT["accent"],   # transaction
    PALETTE_LIGHT["teal"],     # bid-ask
    PALETTE_LIGHT["red"],      # performance
]


def build_fig(s):
    P = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax)

    y_pos = np.arange(len(ORDER))
    fund_labels_list = [s["fund_labels"][k] for k in ORDER]

    # Stacked horizontal bar
    left = np.zeros(len(ORDER))
    for ci in range(4):
        comp_vals = [DATA[k][ci] for k in ORDER]
        ax.barh(y_pos, comp_vals, left=left, height=0.62,
                color=COMP_COLORS[ci],
                edgecolor="white", linewidth=1.0,
                label=s["comp_labels"][ci])
        # Inline label inside segment if wide enough
        for yi, (v, l) in enumerate(zip(comp_vals, left)):
            if v >= 35:
                ax.text(l + v / 2, yi, f"{v:.0f}",
                        ha="center", va="center",
                        color="white", fontsize=9.5, weight="bold")
        left = left + np.array(comp_vals)

    # Total at end of bar
    for yi, k in enumerate(ORDER):
        total = sum(DATA[k])
        ax.text(total + 8, yi, s["total_lbl"].format(total),
                ha="left", va="center",
                color=P["fg"], fontsize=11, weight="bold")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(fund_labels_list, fontsize=10.5)
    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_xlim(0, max(sum(DATA[k]) for k in ORDER) * 1.18)
    ax.invert_yaxis()  # ETF on top

    ax.set_title(s["title"], pad=24, fontsize=13.5, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")
    fig.text(0.5, 0.02, s["footnote"], ha="center",
             fontsize=8.5, color=P["muted"], style="italic")

    ax.legend(loc="lower right", frameon=True, fontsize=10,
              facecolor=P["bg"], edgecolor=P["grid"], ncol=2)
    ax.grid(True, axis="x", color=P["grid"], linewidth=0.6, alpha=0.7)
    ax.grid(False, axis="y")

    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"wrote {BASE} for all locales -> {OUT_DIR}")
