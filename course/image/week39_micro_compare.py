"""Week 39, §2.2 -- Capital required for $50,000 of S&P 500 exposure.

Five vehicles compared: SPY shares (full $50k), 2x /MES contracts
($4k margin), 1x /ES (oversized -- $14k margin controls $260k notional),
1x deep-ITM LEAPS at 0.92 delta (~$10k premium for $52k exposure), and
1x SSO 2x ETF ($25k for $50k effective). Bars are coloured by category;
notional controlled is annotated above.

Run:
    uv run python course/image/week39_micro_compare.py
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
BASE = "week39_micro_compare"


# Capital required (dollars) and notional controlled (dollars).
VEHICLES = [
    # name_key, capital, notional, leverage, color_key
    ("spy",   50_000, 50_000,  1.0,  "blue"),
    ("mes",    4_000, 52_000, 13.0,  "green"),
    ("es",    14_000, 260_000, 18.6, "red"),     # oversized
    ("leaps", 10_000, 52_000,  5.2,  "accent"),
    ("sso",   25_000, 50_000,  2.0,  "purple"),
]


LANG_STRINGS = {
    "en": {
        "title":    "Capital required for $50,000 of S&P 500 exposure",
        "subtitle": "Five vehicles, same target exposure. Notional controlled is shown above each bar; the leverage ratio is in parentheses. April 2026 anchors: SPY $520, sigma 19%, T-bill 4.3%.",
        "xlabel":   "Vehicle",
        "ylabel":   "Capital required ($)",
        "labels":   {
            "spy":   "SPY shares",
            "mes":   "2 x /MES",
            "es":    "1 x /ES (oversized)",
            "leaps": "1 x LEAPS 0.92D",
            "sso":   "1 x SSO (2x ETF)",
        },
        "lev_fmt":  "{lev:.1f}x leverage",
        "not_fmt":  "controls ${not:,.0f}",
        "footer":   "/MES = Micro E-mini, $5/pt, ~$2k margin. /ES = full E-mini, $50/pt, ~$14k margin. LEAPS = Black-Scholes 12-mo, K=0.80*S, sigma=19%, r=4.3%, q=1.3%.",
    },
    "hk": {
        "title":    "取得 $50,000 標普 500 敞口所需資金",
        "subtitle": "五種工具,同一敞口目標。每個柱頂標示控制的名義金額,括號內為槓桿倍數。2026/4 基準:SPY $520、波幅 19%、國庫券 4.3%。",
        "xlabel":   "工具",
        "ylabel":   "所需資金(美元)",
        "labels":   {
            "spy":   "SPY 股票",
            "mes":   "2 張 /MES",
            "es":    "1 張 /ES(過大)",
            "leaps": "1 張 LEAPS 0.92D",
            "sso":   "1 張 SSO(2 倍 ETF)",
        },
        "lev_fmt":  "槓桿 {lev:.1f} 倍",
        "not_fmt":  "控制 ${not:,.0f}",
        "footer":   "/MES = 微型 E-mini,每點 $5,保證金約 $2k。/ES = 標準 E-mini,每點 $50,保證金約 $14k。LEAPS = BS 12 月、K=0.80*S、sigma=19%、r=4.3%、q=1.3%。",
    },
    "tw": {
        "title":    "取得 $50,000 標普 500 部位所需資金",
        "subtitle": "五種工具,同一目標部位。柱頂為控制的名目金額,括號內為槓桿倍數。2026/4 基準:SPY $520、波動 19%、國庫券 4.3%。",
        "xlabel":   "工具",
        "ylabel":   "所需資金(美元)",
        "labels":   {
            "spy":   "SPY 股票",
            "mes":   "2 口 /MES",
            "es":    "1 口 /ES(過大)",
            "leaps": "1 張 LEAPS 0.92D",
            "sso":   "1 張 SSO(2 倍 ETF)",
        },
        "lev_fmt":  "槓桿 {lev:.1f} 倍",
        "not_fmt":  "控制 ${not:,.0f}",
        "footer":   "/MES = 微型 E-mini,每點 $5,保證金約 $2k。/ES = 標準 E-mini,每點 $50,保證金約 $14k。LEAPS = BS 12 月、K=0.80*S、sigma=19%、r=4.3%、q=1.3%。",
    },
    "cn": {
        "title":    "获得 $50,000 标普 500 敞口所需资金",
        "subtitle": "五种工具,同一目标敞口。柱顶为控制的名义金额,括号内为杠杆倍数。2026/4 基准:SPY $520、波动 19%、国库券 4.3%。",
        "xlabel":   "工具",
        "ylabel":   "所需资金(美元)",
        "labels":   {
            "spy":   "SPY 股票",
            "mes":   "2 张 /MES",
            "es":    "1 张 /ES(过大)",
            "leaps": "1 张 LEAPS 0.92D",
            "sso":   "1 张 SSO(2 倍 ETF)",
        },
        "lev_fmt":  "杠杆 {lev:.1f} 倍",
        "not_fmt":  "控制 ${not:,.0f}",
        "footer":   "/MES = 微型 E-mini,每点 $5,保证金约 $2k。/ES = 标准 E-mini,每点 $50,保证金约 $14k。LEAPS = BS 12 月、K=0.80*S、sigma=19%、r=4.3%、q=1.3%。",
    },
}


def build_fig(s):
    s = {**s, "title": s["title"].replace("$", r"\$"),
         "subtitle": s["subtitle"].replace("$", r"\$"),
         "footer": s["footer"].replace("$", r"\$")}
    p = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    style_axes(ax, p)

    n = len(VEHICLES)
    x = np.arange(n)
    caps = [v[1] for v in VEHICLES]
    nots = [v[2] for v in VEHICLES]
    levs = [v[3] for v in VEHICLES]
    colors = [p[v[4]] for v in VEHICLES]
    keys = [v[0] for v in VEHICLES]
    labels = [s["labels"][k] for k in keys]

    bars = ax.bar(x, caps, color=colors, width=0.62, edgecolor="none")

    for i, b in enumerate(bars):
        cap = caps[i]
        nv = nots[i]
        lv = levs[i]
        # Top notional + leverage label
        top_y = cap + 1500
        ax.text(b.get_x() + b.get_width()/2, top_y,
                s["not_fmt"].format(**{"not": nv}).replace("$", "\\$"),
                ha="center", va="bottom", fontsize=10,
                fontweight="bold", color=colors[i])
        ax.text(b.get_x() + b.get_width()/2, top_y + 2700,
                "(" + s["lev_fmt"].format(lev=lv) + ")",
                ha="center", va="bottom", fontsize=9,
                color=p["muted"])
        # Inside bar capital number
        ax.text(b.get_x() + b.get_width()/2, cap/2,
                "\\$" + f"{cap:,.0f}",
                ha="center", va="center", fontsize=11,
                fontweight="bold", color="white")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_ylim(0, max(caps) * 1.55)

    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold", loc="left")
    fig.text(0.5, 0.94, s["subtitle"], ha="center",
             fontsize=10.0, color=p["muted"], style="italic")

    fig.text(0.5, 0.02, s["footer"], ha="center", fontsize=8.0,
             color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_*.png and {BASE}.png to {OUT_DIR}")
