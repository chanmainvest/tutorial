"""Week 8, §2.4 — Apple FY2014–FY2024 EPS vs Free Cash Flow per share.

Split-adjusted (post 7:1 in 2014 and 4:1 in 2020) annual diluted EPS
vs FCF per share, USD. Constants from Apple's published 10-Ks. The
two lines mostly track each other; FY2020 (COVID, working-capital
release) and FY2024 (one-time ~$10B EU State-aid tax charge) are the
notable divergence years where FCF/share runs above EPS.

Sources cross-checked against Apple 10-K filings and Macrotrends.

Run:
    uv run python course/image/week08_eps_vs_fcf.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week08_eps_vs_fcf"

# Apple fiscal years end late September.
YEARS = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Diluted EPS, split-adjusted (post 7:1 Jun-2014 and 4:1 Aug-2020).
EPS = [1.61, 2.31, 2.08, 2.30, 2.98, 2.97, 3.28, 5.61, 6.11, 6.13, 6.08]

# FCF per share = (OCF - Capex) / diluted weighted-avg shares (post-split).
# Approximate from public 10-Ks.
FCF_PER_SHARE = [1.94, 2.41, 2.40, 2.42, 3.21, 3.13, 4.31, 5.62, 6.50, 6.16, 7.08]


LANG_STRINGS = {
    "en": {
        "title":    "Apple: EPS vs Free Cash Flow per share, FY2014-FY2024",
        "subtitle": "Split-adjusted diluted EPS and FCF/share. The two lines diverge in FY2020 (COVID working-capital release) and FY2024 (one-time ~$10B EU tax charge depressed reported earnings).",
        "xlabel":   "Fiscal year",
        "ylabel":   "USD per share (split-adjusted)",
        "eps":      "Diluted EPS",
        "fcf":      "FCF per share",
        "anno_fy20":"FY2020: WC release",
        "anno_fy24":"FY2024: $10B EU tax charge",
        "footer":   "Cash is the fact, earnings are the opinion. When the two diverge, trust the cash line.",
    },
    "hk": {
        "title":    "蘋果:每股盈利與每股自由現金流,FY2014-FY2024",
        "subtitle": "經拆股調整的攤薄 EPS 與每股 FCF。兩線在 FY2020(疫情期間營運資金釋放)及 FY2024(歐盟一次性約 100 億美元稅項)出現背離。",
        "xlabel":   "財政年度",
        "ylabel":   "每股美元(拆股調整後)",
        "eps":      "攤薄每股盈利",
        "fcf":      "每股自由現金流",
        "anno_fy20":"FY2020:營運資金釋放",
        "anno_fy24":"FY2024:歐盟 100 億稅項",
        "footer":   "現金是事實,盈利是觀點;兩者背離時,相信現金那條線。",
    },
    "tw": {
        "title":    "蘋果:每股盈餘與每股自由現金流,FY2014-FY2024",
        "subtitle": "經拆股調整的稀釋 EPS 與每股 FCF。兩線在 FY2020(疫情期間營運資金釋出)及 FY2024(歐盟一次性約 100 億美元稅費)出現背離。",
        "xlabel":   "會計年度",
        "ylabel":   "每股美元(拆股調整)",
        "eps":      "稀釋每股盈餘",
        "fcf":      "每股自由現金流",
        "anno_fy20":"FY2020:營運資金釋出",
        "anno_fy24":"FY2024:歐盟 100 億稅費",
        "footer":   "現金是事實,盈餘是觀點;兩者背離時,相信現金那條線。",
    },
    "cn": {
        "title":    "苹果:每股盈利与每股自由现金流,FY2014-FY2024",
        "subtitle": "经拆股调整的摊薄 EPS 与每股 FCF。两线在 FY2020(疫情期间营运资金释放)及 FY2024(欧盟一次性约 100 亿美元税项)出现背离。",
        "xlabel":   "财政年度",
        "ylabel":   "每股美元(拆股调整后)",
        "eps":      "摊薄每股盈利",
        "fcf":      "每股自由现金流",
        "anno_fy20":"FY2020:营运资金释放",
        "anno_fy24":"FY2024:欧盟 100 亿税项",
        "footer":   "现金是事实,盈利是观点;两者背离时,相信现金那条线。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11, 6.0))
    style_axes(ax, p)

    ax.plot(YEARS, EPS, color=p["blue"], linewidth=2.4, marker="o",
            markersize=6, label=s["eps"])
    ax.plot(YEARS, FCF_PER_SHARE, color=p["accent"], linewidth=2.4,
            marker="s", markersize=6, label=s["fcf"])

    # Shade divergence regions
    ax.fill_between(YEARS, EPS, FCF_PER_SHARE,
                    where=[f > e for f, e in zip(FCF_PER_SHARE, EPS)],
                    color=p["accent"], alpha=0.10, interpolate=True)

    # Annotations on FY2020 and FY2024
    i20 = YEARS.index(2020)
    i24 = YEARS.index(2024)
    ax.annotate(s["anno_fy20"],
                xy=(2020, FCF_PER_SHARE[i20]),
                xytext=(2017.4, 5.4),
                fontsize=9.5, color=p["fg"],
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))
    ax.annotate(s["anno_fy24"],
                xy=(2024, EPS[i24]),
                xytext=(2021.0, 3.3),
                fontsize=9.5, color=p["fg"],
                arrowprops=dict(arrowstyle="->", color=p["muted"], lw=0.8))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xticks(YEARS)
    ax.set_xticklabels([str(y) for y in YEARS])
    ax.set_ylim(0, max(FCF_PER_SHARE + EPS) * 1.18)

    ax.set_title(s["title"], fontsize=13, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontstyle="italic")

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
