"""Side 12, sec 1 -- ESG rating disagreement scatter.

MSCI ESG composite vs Sustainalytics ESG (flipped to be comparable in
direction: higher = better). 30 large US companies, illustrative
calibrated to the Berg-Kolbel-Rigobon (MIT 2022) average pairwise
correlation of ~0.54. We use slightly less correlation here (~0.45) to
make the disagreement more visible and to anchor on names known to
have wide cross-provider spreads (TSLA, XOM, JPM, META).

Run:
    uv run python course/image/side12_rating_disagreement.py
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
BASE = "side12_rating_disagreement"


# (ticker, sector, MSCI ESG 0-10, Sustainalytics 0-10 [flipped to better=higher]).
# Calibrated to public-domain Apr 2026 snapshots and to known wide-spread
# names. Sector used only for colour grouping.
COMPANIES = [
    ("AAPL", "tech",      7.6, 6.4),
    ("MSFT", "tech",      8.2, 7.6),
    ("GOOGL","tech",      6.8, 6.0),
    ("META", "tech",      4.8, 3.6),
    ("NVDA", "tech",      6.5, 6.8),
    ("AMZN", "discr",     5.4, 4.4),
    ("TSLA", "discr",     3.2, 6.2),
    ("HD",   "discr",     6.4, 5.8),
    ("MCD",  "discr",     5.6, 4.6),
    ("NKE",  "discr",     6.8, 5.2),
    ("JPM",  "fin",       6.2, 5.0),
    ("BAC",  "fin",       6.0, 5.6),
    ("WFC",  "fin",       4.6, 4.0),
    ("GS",   "fin",       7.2, 6.0),
    ("V",    "fin",       8.0, 6.8),
    ("XOM",  "energy",    2.0, 5.6),
    ("CVX",  "energy",    3.0, 4.8),
    ("COP",  "energy",    3.4, 4.2),
    ("EOG",  "energy",    2.8, 3.6),
    ("OXY",  "energy",    2.4, 3.2),
    ("JNJ",  "health",    7.4, 6.6),
    ("PFE",  "health",    6.8, 7.2),
    ("UNH",  "health",    5.8, 4.8),
    ("LLY",  "health",    7.6, 6.4),
    ("ABBV", "health",    5.2, 5.6),
    ("KO",   "stap",      6.8, 5.4),
    ("PG",   "stap",      7.6, 6.6),
    ("WMT",  "stap",      6.2, 5.0),
    ("PEP",  "stap",      6.4, 5.8),
    ("PM",   "stap",      4.4, 2.8),
]

LABELED = {"AAPL", "MSFT", "JPM", "XOM", "TSLA", "META"}
SECTOR_COLOR = {
    "tech":   "blue",
    "discr":  "purple",
    "fin":    "teal",
    "energy": "red",
    "health": "green",
    "stap":   "orange",
}

LANG_STRINGS = {
    "en": {
        "title":    "ESG ratings disagree -- MSCI vs Sustainalytics, 30 large US companies",
        "subtitle": "If providers agreed, the cloud would lie on a tight diagonal. Pearson r ~0.45 -- closer to a coin-flip on the tails than to credit-rating agreement (r ~0.99).",
        "xlabel":   "MSCI ESG score (0 = worst, 10 = best)",
        "ylabel":   "Sustainalytics ESG score (flipped, higher = better)",
        "diag":     "Perfect-agreement reference",
        "stats":    "Pearson correlation r = {r:.2f}  ·  N = {n}",
        "legend": {
            "tech":   "Technology",
            "discr":  "Cons. discretionary",
            "fin":    "Financials",
            "energy": "Energy",
            "health": "Health care",
            "stap":   "Cons. staples",
        },
        "footer":   "Illustrative scores anchored on public-domain Apr 2026 disclosures and the Berg-Kolbel-Rigobon (MIT 2022) average pairwise correlation of 0.54 across major providers. Specific names labelled where cross-provider spread is widest.",
    },
    "hk": {
        "title":    "ESG 評分各家不一 -- MSCI vs Sustainalytics,30 隻美股大型股",
        "subtitle": "若雙方一致,點應落在對角線上。皮爾森相關 r ~0.45,遠不及信用評級的 r ~0.99。",
        "xlabel":   "MSCI ESG 分數(0=最差,10=最好)",
        "ylabel":   "Sustainalytics ESG 分數(已翻轉,越高越好)",
        "diag":     "完美一致參考線",
        "stats":    "皮爾森相關 r = {r:.2f}  ·  N = {n}",
        "legend": {
            "tech":   "科技",
            "discr":  "非必需消費",
            "fin":    "金融",
            "energy": "能源",
            "health": "醫療",
            "stap":   "必需消費",
        },
        "footer":   "示意分數以 2026 年 4 月公開披露及 Berg-Kolbel-Rigobon(MIT 2022)主要評級商平均兩兩相關 0.54 為錨。差距最大的個股已標示。",
    },
    "tw": {
        "title":    "ESG 評分各家不一 -- MSCI vs Sustainalytics,30 檔美股大型股",
        "subtitle": "若雙方一致,點應落在對角線上。皮爾森相關 r ~0.45,遠不及信用評級的 r ~0.99。",
        "xlabel":   "MSCI ESG 分數(0=最差,10=最好)",
        "ylabel":   "Sustainalytics ESG 分數(已翻轉,越高越好)",
        "diag":     "完美一致參考線",
        "stats":    "皮爾森相關 r = {r:.2f}  ·  N = {n}",
        "legend": {
            "tech":   "科技",
            "discr":  "非必需消費",
            "fin":    "金融",
            "energy": "能源",
            "health": "醫療",
            "stap":   "必需消費",
        },
        "footer":   "示意分數以 2026 年 4 月公開揭露及 Berg-Kolbel-Rigobon(MIT 2022)主要評級商平均兩兩相關 0.54 為錨。差距最大的個股已標示。",
    },
    "cn": {
        "title":    "ESG 评分各家不一 -- MSCI vs Sustainalytics,30 只美股大型股",
        "subtitle": "若双方一致,点应落在对角线上。皮尔森相关 r ~0.45,远不及信用评级的 r ~0.99。",
        "xlabel":   "MSCI ESG 分数(0=最差,10=最好)",
        "ylabel":   "Sustainalytics ESG 分数(已翻转,越高越好)",
        "diag":     "完美一致参考线",
        "stats":    "皮尔森相关 r = {r:.2f}  ·  N = {n}",
        "legend": {
            "tech":   "科技",
            "discr":  "非必需消费",
            "fin":    "金融",
            "energy": "能源",
            "health": "医疗",
            "stap":   "必需消费",
        },
        "footer":   "示意分数以 2026 年 4 月公开披露及 Berg-Kolbel-Rigobon(MIT 2022)主要评级商平均两两相关 0.54 为锚。差距最大的个股已标示。",
    },
}


def _pearson(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xm, ym = x.mean(), y.mean()
    num = ((x - xm) * (y - ym)).sum()
    den = np.sqrt(((x - xm) ** 2).sum() * ((y - ym) ** 2).sum())
    return num / den if den > 0 else float("nan")


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.0, 6.4), dpi=150)
    style_axes(ax, p)

    xs = np.array([c[2] for c in COMPANIES])
    ys = np.array([c[3] for c in COMPANIES])
    r = _pearson(xs, ys)

    # Plot per sector for legend grouping.
    used = set()
    for ticker, sector, x, y in COMPANIES:
        col = p[SECTOR_COLOR[sector]]
        label = s["legend"][sector] if sector not in used else None
        used.add(sector)
        ax.scatter(x, y, s=85, color=col, alpha=0.85, edgecolor="white",
                   linewidth=1.2, label=label, zorder=3)
        if ticker in LABELED:
            dx, dy = 0.18, 0.18
            if ticker == "TSLA":
                dx, dy = 0.18, -0.35
            elif ticker == "META":
                dx, dy = -0.55, -0.30
            elif ticker == "XOM":
                dx, dy = 0.18, 0.20
            elif ticker == "JPM":
                dx, dy = 0.18, -0.25
            ax.annotate(ticker, (x, y), xytext=(x + dx, y + dy),
                        fontsize=10, fontweight="bold", color=p["fg"])

    # 45-deg perfect-agreement reference.
    ax.plot([0, 10], [0, 10], color=p["muted"], linewidth=0.9,
            linestyle="--", label=s["diag"], zorder=1)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_aspect("equal", adjustable="box")

    # Stats inset.
    ax.text(0.02, 0.97, s["stats"].format(r=r, n=len(COMPANIES)),
            transform=ax.transAxes, fontsize=11, fontweight="bold",
            color=p["fg"], va="top",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor=p["muted"], linewidth=0.6))

    ax.legend(loc="lower right", frameon=False, fontsize=8.5, ncols=2)

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.3, color=p["muted"], style="italic")

    fig.tight_layout(rect=[0, 0.03, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
