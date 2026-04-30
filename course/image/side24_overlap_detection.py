"""Side 24, §2.2 — 5x5 stock-overlap heatmap (Morningstar X-Ray illustration).

Five popular ETFs - VTI, VOO, SPY, QQQ, SCHD - the kind of "diversified"
portfolio retail investors stack thinking they are buying five different
products. We hand-construct a representative top-30 holdings universe
weighted by published 2026-Q1 fund factsheets, then compute pairwise
top-10 overlap as min-weight sum across shared names. Average pairwise
overlap lands ~60%, with the VTI/VOO/SPY cluster at 99%+.

Run:
    uv run python course/image/side24_overlap_detection.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side24_overlap_detection"


# Top holdings by approximate Apr-2026 fund weight (%).
# Source: published factsheets / SEC N-PORT, hand-rounded to one decimal.
HOLDINGS = {
    "AAPL":   {"VTI": 6.4, "VOO": 7.0, "SPY": 7.0, "QQQ": 8.5, "SCHD": 0.0},
    "MSFT":   {"VTI": 6.0, "VOO": 6.5, "SPY": 6.5, "QQQ": 8.0, "SCHD": 0.0},
    "NVDA":   {"VTI": 5.4, "VOO": 5.9, "SPY": 5.9, "QQQ": 7.4, "SCHD": 0.0},
    "AMZN":   {"VTI": 3.5, "VOO": 3.8, "SPY": 3.8, "QQQ": 5.0, "SCHD": 0.0},
    "META":   {"VTI": 2.4, "VOO": 2.6, "SPY": 2.6, "QQQ": 4.4, "SCHD": 0.0},
    "GOOGL":  {"VTI": 2.0, "VOO": 2.2, "SPY": 2.2, "QQQ": 3.6, "SCHD": 0.0},
    "GOOG":   {"VTI": 1.7, "VOO": 1.9, "SPY": 1.9, "QQQ": 3.4, "SCHD": 0.0},
    "TSLA":   {"VTI": 1.5, "VOO": 1.7, "SPY": 1.7, "QQQ": 2.8, "SCHD": 0.0},
    "AVGO":   {"VTI": 1.6, "VOO": 1.8, "SPY": 1.8, "QQQ": 4.5, "SCHD": 0.0},
    "BRK.B":  {"VTI": 1.6, "VOO": 1.8, "SPY": 1.8, "QQQ": 0.0, "SCHD": 0.0},
    "JPM":    {"VTI": 1.4, "VOO": 1.5, "SPY": 1.5, "QQQ": 0.0, "SCHD": 0.0},
    "LLY":    {"VTI": 1.2, "VOO": 1.3, "SPY": 1.3, "QQQ": 0.0, "SCHD": 0.0},
    "V":      {"VTI": 1.0, "VOO": 1.1, "SPY": 1.1, "QQQ": 0.0, "SCHD": 0.0},
    "HD":     {"VTI": 0.8, "VOO": 0.8, "SPY": 0.8, "QQQ": 0.0, "SCHD": 4.4},
    "ABBV":   {"VTI": 0.7, "VOO": 0.8, "SPY": 0.8, "QQQ": 0.0, "SCHD": 4.5},
    "VZ":     {"VTI": 0.4, "VOO": 0.5, "SPY": 0.5, "QQQ": 0.0, "SCHD": 4.6},
    "MRK":    {"VTI": 0.5, "VOO": 0.6, "SPY": 0.6, "QQQ": 0.0, "SCHD": 4.5},
    "KO":     {"VTI": 0.5, "VOO": 0.5, "SPY": 0.5, "QQQ": 0.0, "SCHD": 4.4},
    "PEP":    {"VTI": 0.5, "VOO": 0.5, "SPY": 0.5, "QQQ": 1.6, "SCHD": 4.4},
    "CSCO":   {"VTI": 0.4, "VOO": 0.4, "SPY": 0.4, "QQQ": 1.5, "SCHD": 4.6},
    "TXN":    {"VTI": 0.3, "VOO": 0.3, "SPY": 0.3, "QQQ": 1.0, "SCHD": 4.4},
    "AMGN":   {"VTI": 0.3, "VOO": 0.4, "SPY": 0.4, "QQQ": 1.0, "SCHD": 4.5},
    "BMY":    {"VTI": 0.2, "VOO": 0.2, "SPY": 0.2, "QQQ": 0.0, "SCHD": 4.4},
    "PFE":    {"VTI": 0.3, "VOO": 0.3, "SPY": 0.3, "QQQ": 0.0, "SCHD": 4.5},
    "CVX":    {"VTI": 0.5, "VOO": 0.5, "SPY": 0.5, "QQQ": 0.0, "SCHD": 4.5},
    "XOM":    {"VTI": 0.9, "VOO": 1.0, "SPY": 1.0, "QQQ": 0.0, "SCHD": 0.0},
    "ADBE":   {"VTI": 0.5, "VOO": 0.5, "SPY": 0.5, "QQQ": 1.6, "SCHD": 0.0},
    "INTC":   {"VTI": 0.3, "VOO": 0.3, "SPY": 0.3, "QQQ": 0.7, "SCHD": 0.0},
    "AMD":    {"VTI": 0.5, "VOO": 0.6, "SPY": 0.6, "QQQ": 1.6, "SCHD": 0.0},
    "NFLX":   {"VTI": 0.5, "VOO": 0.5, "SPY": 0.5, "QQQ": 1.7, "SCHD": 0.0},
}

FUNDS = ["VTI", "VOO", "SPY", "QQQ", "SCHD"]


def _topN(fund: str, n: int = 10):
    rows = sorted(((t, w[fund]) for t, w in HOLDINGS.items()), key=lambda r: -r[1])
    return [(t, w) for t, w in rows if w > 0][:n]


def _norm(rows):
    s = sum(w for _, w in rows) or 1.0
    return {t: w / s for t, w in rows}


def _overlap(a_rows, b_rows) -> float:
    """min-weight sum across shared names, normalised so single fund = 1."""
    a = _norm(a_rows)
    b = _norm(b_rows)
    return sum(min(a.get(t, 0), b.get(t, 0)) for t in set(a) | set(b))


def _build_matrix() -> np.ndarray:
    M = np.zeros((len(FUNDS), len(FUNDS)))
    for i, fa in enumerate(FUNDS):
        for j, fb in enumerate(FUNDS):
            M[i, j] = _overlap(_topN(fa), _topN(fb))
    return M


def build_fig(s):
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    M = _build_matrix() * 100  # to %

    fig, ax = plt.subplots(figsize=(10.0, 7.6), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    ax.set_facecolor(p["bg"])

    cmap = mcolors.LinearSegmentedColormap.from_list(
        "overlap", ["#fdfbf5", "#fbe6cc", "#e89060", "#b71c1c"], N=256
    )
    im = ax.imshow(M, cmap=cmap, vmin=0, vmax=100, aspect="equal")

    # cell labels
    for i in range(len(FUNDS)):
        for j in range(len(FUNDS)):
            v = M[i, j]
            txt_color = "white" if v > 60 else p["fg"]
            ax.text(j, i, f"{v:.0f}%", ha="center", va="center",
                    color=txt_color, fontsize=12, weight="bold")

    ax.set_xticks(range(len(FUNDS)))
    ax.set_yticks(range(len(FUNDS)))
    ax.set_xticklabels(FUNDS, fontsize=11, color=p["fg"])
    ax.set_yticklabels(FUNDS, fontsize=11, color=p["fg"])
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.03)
    cb.outline.set_visible(False)
    cb.ax.tick_params(labelsize=8.5, colors=p["fg"])
    cb.set_label(s["cb_label"], fontsize=9.5, color=p["fg"])

    # average off-diagonal
    triu = np.triu_indices(len(FUNDS), k=1)
    avg = float(M[triu].mean())
    ax.text(0.02, -0.16, s["box_text"].format(avg=f"{avg:.0f}%"),
            transform=ax.transAxes, ha="left", va="top",
            fontsize=10.0, color=p["fg"],
            bbox=dict(boxstyle="round,pad=0.55", fc=p["bg"], ec=p["accent"], lw=1.0))

    fig.suptitle(s["title"], color=p["fg"], fontsize=14.5, weight="bold", y=0.97)
    fig.text(0.5, 0.915, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.2, color=p["muted"])
    fig.subplots_adjust(left=0.10, right=0.92, top=0.88, bottom=0.18)
    return fig


LANG_STRINGS = {
    "en": {
        "title": "Stock-overlap matrix: 5 popular ETFs",
        "subtitle": "Pairwise top-10 holdings overlap. VTI/VOO/SPY are the same fund three times. (Side 24)",
        "footer": "Cell value = sum of min-weight across each fund pair's top-10 names, normalised. Source: Apr-2026 fund factsheets.",
        "cb_label": "Top-10 overlap (%)",
        "box_text": "Average off-diagonal pairwise overlap: {avg}\nThis is one big mega-cap bet, paying four expense ratios.",
    },
    "hk": {
        "title": "持股重疊矩陣:5 隻熱門 ETF",
        "subtitle": "兩兩前十持股重疊。VTI/VOO/SPY 其實是同一隻基金三次。(Side 24)",
        "footer": "格內值 = 每對基金前十持股最小權重之和,經正規化。資料:2026 年 4 月基金概覽。",
        "cb_label": "前十重疊(%)",
        "box_text": "對角外平均兩兩重疊:{avg}\n其實是同一個大型科技股押注,卻付四份管理費。",
    },
    "tw": {
        "title": "持股重疊矩陣:5 檔熱門 ETF",
        "subtitle": "兩兩前十持股重疊。VTI/VOO/SPY 其實是同一檔基金三次。(Side 24)",
        "footer": "格內值 = 每對基金前十持股最小權重之和,經標準化。資料:2026 年 4 月基金概覽。",
        "cb_label": "前十重疊(%)",
        "box_text": "對角外平均兩兩重疊:{avg}\n其實是同一個大型科技股押注,卻付四份管理費。",
    },
    "cn": {
        "title": "持股重叠矩阵:5 只热门 ETF",
        "subtitle": "两两前十持股重叠。VTI/VOO/SPY 其实是同一只基金三次。(Side 24)",
        "footer": "格内值 = 每对基金前十持股最小权重之和,经归一化。资料:2026 年 4 月基金概览。",
        "cb_label": "前十重叠(%)",
        "box_text": "对角外平均两两重叠:{avg}\n其实是同一个大型科技股押注,却付四份管理费。",
    },
}


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
