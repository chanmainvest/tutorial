"""Side 18, §2.1 -- Global investable equity market cap by region.

Pie / donut chart of MSCI ACWI IMI weights as of April 2026:
US ~60%, EAFE ~25%, EM ~12%, Frontier ~3%.  The headline this chart
should leave: global cap is dominated by one country, and the gap
has widened since the 1989 Japan-peak when the US was only ~40%.

Run:
    uv run python course/image/side18_global_market_cap.py
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
BASE = "side18_global_market_cap"


# Approximate MSCI ACWI IMI weights as of April 2026.
WEIGHTS = [60.0, 25.0, 12.0, 3.0]


LANG_STRINGS = {
    "en": {
        "title":    "Global investable equity market cap, April 2026",
        "subtitle": "MSCI ACWI IMI weights. The US is ~60% of the global float -- five times the size of #2 (Japan).",
        "labels":   ["United States", "Developed ex-US (EAFE)",
                     "Emerging markets", "Frontier"],
        "footer":   "Source: MSCI ACWI IMI factsheet (Apr 2026 estimate). EAFE = Europe, Australasia, Far East ex-Canada. EM is dominated by China ~28%, India ~17%, Taiwan ~16%, Korea ~12%. Frontier (Vietnam, Nigeria, etc.) is ~3% but illiquid.",
        "centre":   "World\nequity\n$92T",
        "annotate_us": "Mag-7 alone\n= entire EAFE",
    },
    "hk": {
        "title":    "全球可投資股票市值,2026 年 4 月",
        "subtitle": "MSCI ACWI IMI 權重。美國佔全球市值約 60%——是第二名(日本)的五倍。",
        "labels":   ["美國", "已開發市場除美(EAFE)",
                     "新興市場", "前沿市場"],
        "footer":   "資料:MSCI ACWI IMI 概覽(2026 年 4 月估算)。EAFE = 歐洲、澳大利亞、遠東,不含加拿大。新興市場以中國約 28%、印度約 17%、台灣約 16%、韓國約 12% 為主。前沿市場(越南、尼日利亞等)約 3%,流動性差。",
        "centre":   "全球\n股票\n92 兆美元",
        "annotate_us": "光是 Mag-7\n= 整個 EAFE",
    },
    "tw": {
        "title":    "全球可投資股票市值,2026 年 4 月",
        "subtitle": "MSCI ACWI IMI 權重。美國佔全球市值約 60%——是第二名(日本)的五倍。",
        "labels":   ["美國", "已開發市場除美(EAFE)",
                     "新興市場", "前沿市場"],
        "footer":   "資料:MSCI ACWI IMI 概覽(2026 年 4 月估算)。EAFE = 歐洲、澳洲、遠東,不含加拿大。新興市場以中國約 28%、印度約 17%、台灣約 16%、韓國約 12% 為主。前沿市場(越南、奈及利亞等)約 3%,流動性差。",
        "centre":   "全球\n股票\n92 兆美元",
        "annotate_us": "光是 Mag-7\n= 整個 EAFE",
    },
    "cn": {
        "title":    "全球可投资股票市值,2026 年 4 月",
        "subtitle": "MSCI ACWI IMI 权重。美国占全球市值约 60%——是第二名(日本)的五倍。",
        "labels":   ["美国", "发达市场除美(EAFE)",
                     "新兴市场", "前沿市场"],
        "footer":   "资料:MSCI ACWI IMI 概览(2026 年 4 月估算)。EAFE = 欧洲、澳洲、远东,不含加拿大。新兴市场以中国约 28%、印度约 17%、台湾约 16%、韩国约 12% 为主。前沿市场(越南、尼日利亚等)约 3%,流动性差。",
        "centre":   "全球\n股票\n92 万亿美元",
        "annotate_us": "光是 Mag-7\n= 整个 EAFE",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    colors = [p["red"], p["blue"], p["accent"], p["muted"]]

    fig, ax = plt.subplots(figsize=(10.4, 6.4))
    fig.patch.set_facecolor(p["bg"])
    ax.set_facecolor(p["bg"])

    # Donut: explode US slightly.
    explode = [0.04, 0.0, 0.0, 0.0]

    def autopct(pct):
        return f"{pct:.1f}%"

    wedges, texts, autotexts = ax.pie(
        WEIGHTS,
        labels=s["labels"],
        colors=colors,
        autopct=autopct,
        startangle=90,
        counterclock=False,
        explode=explode,
        wedgeprops=dict(width=0.42, edgecolor=p["bg"], linewidth=2),
        pctdistance=0.78,
        labeldistance=1.08,
        textprops=dict(fontsize=10.5, color=p["fg"]),
    )

    for at in autotexts:
        at.set_color("#ffffff")
        at.set_fontweight("bold")
        at.set_fontsize(10.5)

    # Centre text
    ax.text(0, 0, s["centre"], ha="center", va="center",
            fontsize=12, color=p["fg"], fontweight="bold")

    # US callout - the Mag-7 = EAFE comparison
    ax.annotate(
        s["annotate_us"],
        xy=(0.55, 0.55), xytext=(1.25, 1.05),
        fontsize=9.5, color=p["red"], fontweight="bold",
        ha="left",
        arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0,
                        connectionstyle="arc3,rad=-0.2"),
    )

    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 color=p["fg"], y=0.97)
    fig.text(0.5, 0.91, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")

    fig.text(0.5, 0.04, s["footer"], ha="center",
             fontsize=8, color=p["muted"], style="italic", wrap=True)

    fig.subplots_adjust(top=0.84, bottom=0.10, left=0.04, right=0.96)
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
