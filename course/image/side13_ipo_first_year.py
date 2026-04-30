"""Side 13, sec 2.1 -- average first-year price path of US IPOs, 2010-2024 cohort.

Stylised average path normalised to offer price = 1.00. Built from
Ritter pooled stats: ~ +18% first-day pop, ~ flat months 1-3, ~ -8%
drift through month 6 as 90 / 180-day lock-ups expire and first
quarterly earnings disappoint, finishing month 12 at ~ 0.90 of offer
(consistent with Ritter's pooled -10pp benchmark-relative number).

A reference market line at +10% over 12 months (typical broad-market
nominal return window) is overlaid for context.

Run:
    uv run python course/image/side13_ipo_first_year.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side13_ipo_first_year"


# Months 0..12. Month 0 = offer price (1.00). Month 0.05 (just after
# pricing) = first-day open at 1.18 -- the average first-day pop.
# Stylised drift mirroring Ritter pooled US 1980-2024 results, weighted
# toward the 2010-2024 vintage:
#   - month 1: 1.20 (small post-pop drift up)
#   - month 2: 1.16 (sell-side coverage initiation, mixed)
#   - month 3: 1.12 (90-day lock-up partial expiry for direct-listing names)
#   - month 4: 1.05 (first earnings cycle)
#   - month 5: 0.97 (180-day lock-up flood for traditional IPOs)
#   - month 6: 0.93
#   - month 9: 0.90
#   - month 12: 0.90 (== Ritter pooled -10% to broad market)
PATH_X = np.array(
    [0.0, 0.05, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
)
PATH_Y = np.array(
    [1.00, 1.18, 1.20, 1.16, 1.12, 1.05, 0.97, 0.93, 0.91, 0.90, 0.90, 0.90, 0.90, 0.90]
)

# Reference market path (broad index +10% over 12 months, linear).
MKT_X = np.array([0.0, 12.0])
MKT_Y = np.array([1.00, 1.10])


LANG_STRINGS = {
    "en": {
        "title":      "Average US IPO first-year price path, 2010 - 2024 cohort",
        "subtitle":   "Normalised to offer price = 1.00. Day-one pop +18% goes to allocated insiders. Retail buyer at the open is down ~24% by month 12.",
        "xlabel":     "Months since IPO",
        "ylabel":     "Price relative to offer",
        "lbl_ipo":    "Average IPO path",
        "lbl_mkt":    "Broad market (+10%/yr ref)",
        "lbl_offer":  "Offer price (allocated buyer entry)",
        "lbl_open":   "First-day open (retail entry)",
        "annot_pop":  "Day-one pop\n+18%",
        "annot_lock": "180-day lock-up\nflood, first 10-Q",
        "annot_end":  "Month 12: 0.90\n-10pp vs broad market",
        "footer":     "Sources: Jay Ritter IPO database (UF), Renaissance IPO ETF (IPO) vs VTI returns 2013-Apr2026, pooled stylisation. Weights skewed to 2010-2024 vintage. Real cohort dispersion is large -- this is the average curve only.",
    },
    "hk": {
        "title":      "美國 IPO 上市首年平均價格路徑,2010 - 2024 年群組",
        "subtitle":   "以發行價 = 1.00 標準化。首日 +18% 跳空只屬獲分配機構,散戶在開市買入,12 個月後仍然跌約 24%。",
        "xlabel":     "上市後月份",
        "ylabel":     "相對發行價",
        "lbl_ipo":    "IPO 平均路徑",
        "lbl_mkt":    "大市基準(+10%/年參考)",
        "lbl_offer":  "發行價(機構入場)",
        "lbl_open":   "首日開市價(散戶入場)",
        "annot_pop":  "首日跳空\n+18%",
        "annot_lock": "180 日鎖倉\n屆滿、首份 10-Q",
        "annot_end":  "第 12 個月:0.90\n比大市低約 10 點",
        "footer":     "資料:Jay Ritter IPO 資料庫(佛羅里達大學)、Renaissance IPO ETF(代號 IPO)對比 VTI 2013-2026年4月、合併樣本。權重偏向 2010-2024 年群組。實際個股分佈很闊,此為平均曲線。",
    },
    "tw": {
        "title":      "美國 IPO 上市首年平均價格路徑,2010 - 2024 年群組",
        "subtitle":   "以發行價 = 1.00 標準化。首日 +18% 跳空僅歸已配售機構,散戶在開盤買入,12 個月後仍下跌約 24%。",
        "xlabel":     "上市後月份",
        "ylabel":     "相對發行價",
        "lbl_ipo":    "IPO 平均路徑",
        "lbl_mkt":    "大盤基準(+10%/年參考)",
        "lbl_offer":  "發行價(機構入場)",
        "lbl_open":   "首日開盤價(散戶入場)",
        "annot_pop":  "首日跳空\n+18%",
        "annot_lock": "180 日鎖倉\n屆滿、首份 10-Q",
        "annot_end":  "第 12 個月:0.90\n較大盤低約 10 個百分點",
        "footer":     "資料:Jay Ritter IPO 資料庫(佛羅里達大學)、Renaissance IPO ETF(代號 IPO)對比 VTI 2013-2026年4月、合併樣本。權重偏向 2010-2024 年群組。實際個股分布很廣,此為平均曲線。",
    },
    "cn": {
        "title":      "美国 IPO 上市首年平均价格路径,2010 - 2024 年群组",
        "subtitle":   "以发行价 = 1.00 归一化。首日 +18% 跳空只归已配售机构,散户开盘买入,12 个月后仍下跌约 24%。",
        "xlabel":     "上市后月份",
        "ylabel":     "相对发行价",
        "lbl_ipo":    "IPO 平均路径",
        "lbl_mkt":    "大盘基准(+10%/年参考)",
        "lbl_offer":  "发行价(机构入场)",
        "lbl_open":   "首日开盘价(散户入场)",
        "annot_pop":  "首日跳空\n+18%",
        "annot_lock": "180 日锁仓\n届满、首份 10-Q",
        "annot_end":  "第 12 个月:0.90\n比大盘低约 10 个百分点",
        "footer":     "数据:Jay Ritter IPO 数据库(佛罗里达大学)、Renaissance IPO ETF(代号 IPO)对比 VTI 2013-2026年4月、合并样本。权重偏向 2010-2024 年群组。实际个股分布很广,此为平均曲线。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.0, 6.2), dpi=150)
    style_axes(ax, p)

    # IPO path: thick blue line.
    ax.plot(PATH_X, PATH_Y, color=p["blue"], linewidth=2.6,
            label=s["lbl_ipo"], zorder=5)
    # Reference market line.
    ax.plot(MKT_X, MKT_Y, color=p["green"], linewidth=1.6,
            linestyle="--", label=s["lbl_mkt"], zorder=4)

    # Offer-price horizontal reference (allocated entry).
    ax.axhline(1.00, color=p["muted"], linewidth=0.8, linestyle=":",
               zorder=2)
    # First-day open horizontal (retail entry).
    ax.axhline(1.18, color=p["red"], linewidth=0.8, linestyle=":",
               zorder=2)

    # Markers at offer (0,1.00) and open (0.05,1.18).
    ax.plot([0.0], [1.00], marker="o", color=p["green"], markersize=8,
            zorder=6)
    ax.plot([0.05], [1.18], marker="o", color=p["red"], markersize=8,
            zorder=6)

    ax.text(0.30, 1.00, s["lbl_offer"], color=p["green"],
            fontsize=9.2, fontweight="bold", va="center")
    ax.text(0.30, 1.215, s["lbl_open"], color=p["red"],
            fontsize=9.2, fontweight="bold", va="center")

    # Pop arrow annotation.
    ax.annotate(s["annot_pop"],
                xy=(0.05, 1.18), xytext=(1.6, 1.27),
                fontsize=10, fontweight="bold", color=p["red"],
                ha="center",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.9))

    # Lock-up drag annotation.
    ax.annotate(s["annot_lock"],
                xy=(5.0, 0.97), xytext=(7.0, 1.17),
                fontsize=9.5, color=p["fg"], ha="center",
                arrowprops=dict(arrowstyle="->", color=p["fg"], lw=0.7))

    # Endpoint annotation.
    ax.annotate(s["annot_end"],
                xy=(12.0, 0.90), xytext=(9.6, 0.78),
                fontsize=9.5, color=p["red"], ha="center", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.7))

    ax.set_xlim(-0.5, 13.0)
    ax.set_ylim(0.72, 1.32)
    ax.set_xticks([0, 1, 2, 3, 6, 9, 12])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.2f}"))
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.legend(loc="lower left", fontsize=9.5, frameon=False)

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.16, s["footer"], transform=ax.transAxes,
            fontsize=8.3, color=p["muted"])

    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
