"""Week 36, §2.2 — After-tax yield hierarchy at 32% federal + 5% state.

Same nine income lines as week36_yield_hierarchy.py, but each yield is
multiplied by (1 - effective tax rate) for its category. Highlights how
qualified dividends keep ~80% of their yield while corporate coupons
and option premium lose ~37%, flipping the visual ranking.

Run:
    uv run python course/image/week36_tax_adjusted.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week36_tax_adjusted"


# Effective tax rates at 32% federal + 5% state.
#   Treasuries:        32% federal,  0% state  -> 32% effective
#   Corporate coupons: 32% + 5%               -> 37%
#   Qualified divs:    15% federal LTCG + 5%   -> 20%
#   REITs:             37% on 80% of distrib.  -> 29.6%
#   Option premium:    37% (short-term)        -> 37%
TAX = {
    "tre":  0.32,
    "corp": 0.37,
    "qd":   0.20,
    "reit": 0.296,
    "opt":  0.37,
}

ROWS = [
    ("2yr Treasury",  3.9, "tre"),
    ("10yr Treasury", 4.2, "tre"),
    ("LQD (IG corp)", 5.0, "corp"),
    ("HYG (HY corp)", 7.5, "corp"),
    ("S&P 500 div",   1.4, "qd"),
    ("VYM",           2.9, "qd"),
    ("SCHD",          3.6, "qd"),
    ("VNQ (REIT)",    3.8, "reit"),
    ("JEPI",          7.8, "opt"),
]


LANG_STRINGS = {
    "en": {
        "title":    "After-tax yield at 32% federal + 5% state — April 2026",
        "subtitle": "Same nine income lines, taxed in a taxable account. Qualified dividends keep ~80% of yield; corporate coupons and option premium keep ~63%.",
        "xlabel":   "Income source",
        "ylabel":   "After-tax yield (%)",
        "pre_label": "pre-tax",
        "footer":   "Tax categories: Treasuries lose 32% (federal-only), corporates 37%, qualified dividends 20% (LTCG + state), REITs ~30% (199A on 80%), option premium 37% (short-term cap gain).",
        "legend": {
            "tre":  "Treasuries (state-exempt)",
            "corp": "Corporate coupons",
            "qd":   "Qualified dividends",
            "reit": "REIT distributions",
            "opt":  "Option premium",
        },
        "labels": {r[0]: r[0] for r in ROWS},
    },
    "hk": {
        "title":    "32% 聯邦 + 5% 州稅後收益率 — 2026 年 4 月",
        "subtitle": "同樣九個收入項目,在應稅帳戶中扣稅。合格股息保留約 80%;公司債券利息和期權權利金只保留約 63%。",
        "xlabel":   "收入來源",
        "ylabel":   "稅後收益率 (%)",
        "pre_label": "稅前",
        "footer":   "稅務類別:國債失去 32%(僅聯邦),公司債券 37%,合格股息 20%(LTCG + 州稅),REIT ~30%(199A 對 80%),期權權利金 37%(短期資本利得)。",
        "legend": {
            "tre":  "國債(免州稅)",
            "corp": "公司債券利息",
            "qd":   "合格股息",
            "reit": "REIT 派息",
            "opt":  "期權權利金",
        },
        "labels": {
            "2yr Treasury":  "2 年國債",
            "10yr Treasury": "10 年國債",
            "LQD (IG corp)": "LQD(投資級公司)",
            "HYG (HY corp)": "HYG(高息公司)",
            "S&P 500 div":   "標普 500 股息",
            "VYM":           "VYM",
            "SCHD":          "SCHD",
            "VNQ (REIT)":    "VNQ(REIT)",
            "JEPI":          "JEPI",
        },
    },
    "tw": {
        "title":    "32% 聯邦 + 5% 州稅後殖利率 — 2026 年 4 月",
        "subtitle": "同樣九個收入項目,在應稅帳戶中扣稅。合格股息保留約 80%;公司債券利息和選擇權權利金只保留約 63%。",
        "xlabel":   "收入來源",
        "ylabel":   "稅後殖利率 (%)",
        "pre_label": "稅前",
        "footer":   "稅務類別:公債失去 32%(僅聯邦),公司債券 37%,合格股息 20%(LTCG + 州稅),REIT ~30%(199A 對 80%),選擇權權利金 37%(短期資本利得)。",
        "legend": {
            "tre":  "公債(免州稅)",
            "corp": "公司債券利息",
            "qd":   "合格股息",
            "reit": "REIT 配息",
            "opt":  "選擇權權利金",
        },
        "labels": {
            "2yr Treasury":  "2 年公債",
            "10yr Treasury": "10 年公債",
            "LQD (IG corp)": "LQD(投資級公司)",
            "HYG (HY corp)": "HYG(高息公司)",
            "S&P 500 div":   "標普 500 股息",
            "VYM":           "VYM",
            "SCHD":          "SCHD",
            "VNQ (REIT)":    "VNQ(REIT)",
            "JEPI":          "JEPI",
        },
    },
    "cn": {
        "title":    "32% 联邦 + 5% 州税后收益率 — 2026 年 4 月",
        "subtitle": "同样九项收入,在应税账户中扣税。合格股息保留约 80%;公司债券利息和期权权利金只保留约 63%。",
        "xlabel":   "收入来源",
        "ylabel":   "税后收益率 (%)",
        "pre_label": "税前",
        "footer":   "税务类别:国债失去 32%(仅联邦),公司债券 37%,合格股息 20%(LTCG + 州税),REIT ~30%(199A 对 80%),期权权利金 37%(短期资本利得)。",
        "legend": {
            "tre":  "国债(免州税)",
            "corp": "公司债券利息",
            "qd":   "合格股息",
            "reit": "REIT 派息",
            "opt":  "期权权利金",
        },
        "labels": {
            "2yr Treasury":  "2 年国债",
            "10yr Treasury": "10 年国债",
            "LQD (IG corp)": "LQD(投资级公司)",
            "HYG (HY corp)": "HYG(高息公司)",
            "S&P 500 div":   "标普 500 股息",
            "VYM":           "VYM",
            "SCHD":          "SCHD",
            "VNQ (REIT)":    "VNQ(REIT)",
            "JEPI":          "JEPI",
        },
    },
}


def _category_colors(p):
    return {
        "tre":  p["blue"],
        "corp": p["red"],
        "qd":   p["green"],
        "reit": p["purple"],
        "opt":  p["accent"],
    }


def build_fig(s):
    p = PALETTE_LIGHT
    cats = _category_colors(p)
    labels = [s["labels"][r[0]] for r in ROWS]
    pre = np.array([r[1] for r in ROWS])
    post = np.array([r[1] * (1 - TAX[r[2]]) for r in ROWS])
    colors = [cats[r[2]] for r in ROWS]

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax)
    x = np.arange(len(ROWS))

    # Ghosted pre-tax bars in the background, real after-tax bars in front.
    ax.bar(x, pre, color=colors, alpha=0.20, edgecolor="white",
           linewidth=0.6, zorder=2, label=None)
    bars = ax.bar(x, post, color=colors, edgecolor="white",
                  linewidth=0.8, zorder=3)
    for bar, y_post, y_pre in zip(bars, post, pre):
        ax.text(bar.get_x() + bar.get_width() / 2, y_post + 0.10,
                f"{y_post:.1f}%", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["fg"])
        ax.text(bar.get_x() + bar.get_width() / 2, y_pre + 0.10,
                f"{s['pre_label']}: {y_pre:.1f}%", ha="center", va="bottom",
                fontsize=8.5, color=p["muted"])

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9.5, rotation=20, ha="right")
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.set_ylim(0, max(pre) * 1.22)

    handles = [plt.Rectangle((0, 0), 1, 1, color=cats[k]) for k in ("tre", "corp", "qd", "reit", "opt")]
    leg_labels = [s["legend"][k] for k in ("tre", "corp", "qd", "reit", "opt")]
    ax.legend(handles, leg_labels, loc="upper left", frameon=False, fontsize=9.5, ncol=2)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.6, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
