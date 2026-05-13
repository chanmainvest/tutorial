"""Side 08, sec 2.2 -- Cumulative wealth over 30 years at 5 fee levels.

$100,000 starting balance, 8% gross return, 30-year horizon.
Five fee levels: 0.05% index ETF / 0.50% passive blend /
1.00% active mutual fund / 1.50% advisor-wrapped /
2.00% fund-of-funds or hedge-fund management.

Run:
    uv run python course/image/side08_fee_drag.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side08_fee_drag"

INITIAL = 100_000.0
GROSS = 0.08
YEARS = 30
FEES = [0.0005, 0.005, 0.010, 0.015, 0.020]
FEE_LABELS_EN = [
    "0.05% (index ETF)",
    "0.50% (passive blend)",
    "1.00% (active MF)",
    "1.50% (advisor)",
    "2.00% (FoF / hedge fund)",
]
FEE_LABELS_HK = [
    "0.05%(指數 ETF)",
    "0.50%(被動混合)",
    "1.00%(主動共同基金)",
    "1.50%(顧問加碼)",
    "2.00%(基金中基金/對沖基金)",
]
FEE_LABELS_TW = [
    "0.05%(指數 ETF)",
    "0.50%(被動混合)",
    "1.00%(主動共同基金)",
    "1.50%(顧問加碼)",
    "2.00%(基金中基金/避險基金)",
]
FEE_LABELS_CN = [
    "0.05%(指数 ETF)",
    "0.50%(被动混合)",
    "1.00%(主动共同基金)",
    "1.50%(顾问加码)",
    "2.00%(基金中基金/对冲基金)",
]


def simulate():
    """Return list of (fee, [path of length YEARS+1])."""
    out = []
    for fee in FEES:
        net = GROSS - fee
        path = [INITIAL]
        for _ in range(YEARS):
            path.append(path[-1] * (1.0 + net))
        out.append((fee, path))
    return out


LANG_STRINGS = {
    "en": {
        "title": "The 1% Fee Costs You $400k -- 30-yr Wealth at 8% Gross, 100k Starting",
        "subtitle": "Same gross return, different fee. The gap to the 5 bp index ETF is the 'silent compounding killer'.",
        "ylabel": "Cumulative wealth (USD)",
        "xlabel": "Year",
        "fee_labels": FEE_LABELS_EN,
        "gap_lbl": "Gap to 5 bp ETF\n@ 1.00% fee: -${:,.0f}\n@ 2.00% fee: -${:,.0f}",
        "footnote": "Constant 8% gross compounded annually. Fee deducted at year-end. 30-year horizon. Excludes loads, transaction cost, and tax drag (which widen the gaps further).",
    },
    "hk": {
        "title": "1% 費用代價 40 萬美元 -- 30 年複利,8% 毛回報,10 萬美元起始",
        "subtitle": "同樣毛回報,不同費率。對 5 基點指數 ETF 的差距,就是「無聲複利殺手」。",
        "ylabel": "累計財富(美元)",
        "xlabel": "年份",
        "fee_labels": FEE_LABELS_HK,
        "gap_lbl": "對 5 基點 ETF 的缺口\n@ 1.00% 費率:-US${:,.0f}\n@ 2.00% 費率:-US${:,.0f}",
        "footnote": "假設恆定 8% 毛回報年度複利,年末扣費,30 年期。未計銷售費、交易成本及稅務拖累(實際差距更大)。",
    },
    "tw": {
        "title": "1% 費用代價 40 萬美元 -- 30 年複利,8% 毛報酬,10 萬美元起始",
        "subtitle": "同樣毛報酬,不同費率。對 5 基點指數 ETF 的差距,就是「無聲複利殺手」。",
        "ylabel": "累計財富(美元)",
        "xlabel": "年份",
        "fee_labels": FEE_LABELS_TW,
        "gap_lbl": "對 5 基點 ETF 的缺口\n@ 1.00% 費率:-US${:,.0f}\n@ 2.00% 費率:-US${:,.0f}",
        "footnote": "假設恆定 8% 毛報酬年度複利,年末扣費,30 年期。未計銷售費、交易成本及稅務拖累(實際差距更大)。",
    },
    "cn": {
        "title": "1% 费用代价 40 万美元 -- 30 年复利,8% 毛回报,10 万美元起始",
        "subtitle": "同样毛回报,不同费率。对 5 基点指数 ETF 的差距,就是「无声复利杀手」。",
        "ylabel": "累计财富(美元)",
        "xlabel": "年份",
        "fee_labels": FEE_LABELS_CN,
        "gap_lbl": "对 5 基点 ETF 的缺口\n@ 1.00% 费率:-US${:,.0f}\n@ 2.00% 费率:-US${:,.0f}",
        "footnote": "假设恒定 8% 毛回报年度复利,年末扣费,30 年期。未计销售费、交易成本及税务拖累(实际差距更大)。",
    },
}


COLORS = [
    PALETTE_LIGHT["blue"],
    PALETTE_LIGHT["green"],
    PALETTE_LIGHT["orange"],
    "#c2410c",
    PALETTE_LIGHT["red"],
]


def build_fig(s):
    P = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    paths = simulate()
    years_x = list(range(YEARS + 1))

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax)

    for (fee, path), color, label in zip(paths, COLORS, s["fee_labels"]):
        lw = 2.6 if fee in (0.0005, 0.010, 0.020) else 2.0
        ls = "-" if fee in (0.0005, 0.010, 0.020) else (0, (5, 3))
        ax.plot(years_x, path, color=color, linewidth=lw, linestyle=ls,
                label=label, marker="o" if fee == 0.010 else None,
                markersize=4.5, markevery=[YEARS],
                markerfacecolor=color, markeredgecolor="white")
        # End-of-period dollar amount
        ax.annotate(f"${path[-1]/1000:,.0f}k",
                    xy=(YEARS, path[-1]), xytext=(8, 0),
                    textcoords="offset points",
                    color=color, fontsize=10, weight="bold",
                    va="center")

    # Gap callout
    base_path = paths[0][1]
    one_path = paths[2][1]
    two_path = paths[4][1]
    gap_1 = base_path[-1] - one_path[-1]
    gap_2 = base_path[-1] - two_path[-1]
    gap_text = s["gap_lbl"].replace("$", r"\$").format(gap_1, gap_2)
    ax.text(0.02, 0.97, gap_text, transform=ax.transAxes,
            ha="left", va="top",
            fontsize=10.5, weight="bold", color=P["red"],
            bbox=dict(boxstyle="round,pad=0.5",
                      facecolor="#fdecea",
                      edgecolor=P["red"], linewidth=1.2))

    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_title(s["title"], pad=24, fontsize=13.5, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")
    fig.text(0.5, 0.02, s["footnote"], ha="center",
             fontsize=8.5, color=P["muted"], style="italic")

    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.84),
              frameon=True, fontsize=9.5,
              facecolor=P["bg"], edgecolor=P["grid"])
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"${v/1000:,.0f}k"))
    ax.set_xlim(0, YEARS + 4.0)
    ax.set_ylim(50_000, max(path[-1] for _, path in paths) * 1.10)

    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"wrote {BASE} for all locales -> {OUT_DIR}")
