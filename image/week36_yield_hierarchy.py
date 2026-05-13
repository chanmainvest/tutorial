"""Week 36, §2.1 — Pre-tax yield hierarchy by income source (April 2026).

Bar chart of headline (pre-tax) yields for the canonical income menu:
2-year and 10-year Treasuries, LQD (IG corporate), HYG (high-yield
corporate), S&P 500 dividend yield, VYM, SCHD, VNQ (REITs), JEPI
(option-premium ETF). Bars are coloured by tax category to preview the
after-tax sort. Yields are approximate April-2026 snapshots from
fund-issuer fact sheets and FRED.

Run:
    uv run python course/image/week36_yield_hierarchy.py
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
BASE = "week36_yield_hierarchy"


# Tax categories: tre = Treasury (federal-only ordinary, state exempt),
# corp = corporate coupon (full ordinary), qd = qualified dividend (LTCG),
# reit = REIT (ordinary with 199A 20% reduction), opt = option premium
# (short-term cap gain).
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
        "title":    "Pre-tax yield by income source — April 2026",
        "subtitle": "The headline menu. Bars coloured by tax category; the after-tax chart in the next figure flips the order.",
        "xlabel":   "Income source",
        "ylabel":   "Pre-tax yield (%)",
        "footer":   "Sources: fund issuer fact sheets (SCHD/VYM/VNQ/JEPI/LQD/HYG), FRED (Treasury yields), S&P (index dividend yield). Rounded to nearest 0.1%.",
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
        "title":    "按收入來源分類的稅前收益率 — 2026 年 4 月",
        "subtitle": "這是頭條菜單。柱顏色按稅務類別劃分;下一張稅後圖會把次序翻轉。",
        "xlabel":   "收入來源",
        "ylabel":   "稅前收益率 (%)",
        "footer":   "來源:基金發行商概況(SCHD/VYM/VNQ/JEPI/LQD/HYG)、FRED(國債收益率)、S&P(指數股息率)。四捨五入至 0.1%。",
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
        "title":    "依收入來源分類的稅前殖利率 — 2026 年 4 月",
        "subtitle": "這是頭版菜單。柱依稅務類別著色;下一張稅後圖會翻轉次序。",
        "xlabel":   "收入來源",
        "ylabel":   "稅前殖利率 (%)",
        "footer":   "來源:基金公司概況(SCHD/VYM/VNQ/JEPI/LQD/HYG)、FRED(公債殖利率)、S&P(指數股息率)。四捨五入至 0.1%。",
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
        "title":    "按收入来源分类的税前收益率 — 2026 年 4 月",
        "subtitle": "这是头条菜单。柱按税务类别着色;下一张税后图会把次序翻转。",
        "xlabel":   "收入来源",
        "ylabel":   "税前收益率 (%)",
        "footer":   "来源:基金发行商概况(SCHD/VYM/VNQ/JEPI/LQD/HYG)、FRED(国债收益率)、S&P(指数股息率)。四舍五入至 0.1%。",
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
    yields = [r[1] for r in ROWS]
    colors = [cats[r[2]] for r in ROWS]

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax)
    x = np.arange(len(ROWS))
    bars = ax.bar(x, yields, color=colors, edgecolor="white", linewidth=0.8, zorder=3)
    for bar, y in zip(bars, yields):
        ax.text(bar.get_x() + bar.get_width() / 2, y + 0.12,
                f"{y:.1f}%", ha="center", va="bottom",
                fontsize=10, fontweight="bold", color=p["fg"])

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9.5, rotation=20, ha="right")
    ax.set_xlabel(s["xlabel"], fontsize=10)
    ax.set_ylabel(s["ylabel"], fontsize=10)
    ax.set_ylim(0, max(yields) * 1.18)

    # Legend by category
    handles = [plt.Rectangle((0, 0), 1, 1, color=cats[k]) for k in ("tre", "corp", "qd", "reit", "opt")]
    leg_labels = [s["legend"][k] for k in ("tre", "corp", "qd", "reit", "opt")]
    ax.legend(handles, leg_labels, loc="upper left", frameon=False, fontsize=9.5, ncol=2)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=8.8, color="#4a5568", style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
