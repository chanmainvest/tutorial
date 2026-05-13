"""Side 22, sec 2.3 — Wealth path of $1 in physical gold vs USO, 2000-Apr 2026.

Two lines on a log axis: $1 in physical gold (GLDM-equivalent, vault-
held bullion) and $1 in USO (front-month WTI futures rolled monthly).
The chart isolates the wrapper-mechanics divergence: same asset class
(commodity), identical starting capital, opposite long-run outcomes.
Gold compounds because GLDM holds spot. USO bleeds because the fund
holds futures and rolls them through chronic contango.

Run:
    uv run python course/image/side22_gold_vs_oil.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side22_gold_vs_oil"


# Annual nominal total return for each instrument. Decimals.
# GOLD = LBMA AM gold-price total return (no yield, just spot). 2000-2024
# from public LBMA / kitco end-of-year prints. 2025 and Apr 2026 are
# partial-year estimates anchored on the de-dollarisation rally.
GOLD = {
    2000: -0.057, 2001:  0.024, 2002:  0.247, 2003:  0.197, 2004:  0.052,
    2005:  0.181, 2006:  0.226, 2007:  0.310, 2008:  0.057, 2009:  0.245,
    2010:  0.296, 2011:  0.101, 2012:  0.070, 2013: -0.281, 2014: -0.018,
    2015: -0.105, 2016:  0.085, 2017:  0.137, 2018: -0.011, 2019:  0.184,
    2020:  0.249, 2021: -0.039, 2022: -0.003, 2023:  0.131, 2024:  0.270,
    2025:  0.220, 2026:  0.080,  # 2026 = Q1 partial
}

# USO total return. 2006-2024 from publicly reported USO NAV TR.
# Pre-2006 (2000-2005) estimated as front-month WTI %change minus an
# 8% annual contango drag, since USO inception was April 2006. The
# point of the chart is qualitative: the long-run wedge is dominated
# by the 2009-2020 contango era.
USO = {
    2000:  0.044, 2001: -0.342, 2002:  0.428, 2003:  0.029, 2004:  0.235,
    2005:  0.317, 2006: -0.150, 2007:  0.398, 2008: -0.541, 2009: -0.140,
    2010:  0.022, 2011: -0.026, 2012: -0.110, 2013:  0.064, 2014: -0.420,
    2015: -0.460, 2016:  0.066, 2017: -0.029, 2018: -0.205, 2019:  0.282,
    2020: -0.679, 2021:  0.561, 2022:  0.319, 2023: -0.093, 2024:  0.075,
    2025:  0.050, 2026:  0.030,  # 2026 = Q1 partial
}


LANG_STRINGS = {
    "en": {
        "title":    "$1 in physical gold (GLDM proxy) vs USO, 2000-Apr 2026",
        "subtitle": "Same asset class, opposite mechanics. Gold ETFs hold vault bullion (no roll). USO holds front-month WTI futures and rolls them monthly through chronic contango. The gap is pure wrapper drag, not a price view on oil.",
        "xlabel":   "Year",
        "ylabel":   "Wealth ($1 invested Jan 2000, log scale)",
        "gold":     "Physical gold (GLDM-equivalent)",
        "uso":      "USO (front-month WTI futures, rolled)",
        "ann_2008": "2008: oil to $147\nthen -54% USO crash",
        "ann_2020": "Apr-2020 super-contango\nUSO -68% in one year",
        "ann_gold": "Gold ~$3500 / $1 -> ~$12",
        "ann_uso":  "USO < $0.50 (-50%+)",
        "footer":   "Gold: LBMA AM end-of-year prints converted to TR. USO: publicly reported NAV TR for 2006-2024; 2000-2005 estimated as WTI front-month %chg minus 8%/yr contango drag. 2025/Apr 2026 partial-year prints. Log y-axis.",
    },
    "hk": {
        "title":    "1 元投入實物黃金(GLDM 代理)vs USO,2000-2026/4",
        "subtitle": "相同資產類別,相反機制。黃金 ETF 持有金庫實金(無展期)。USO 持有 WTI 近月期貨並每月在長期 contango 中展期。差距純粹來自包裝層的損耗,並非對油價的看法。",
        "xlabel":   "年份",
        "ylabel":   "財富(2000/1 投入 1 元,對數軸)",
        "gold":     "實物黃金(GLDM 等價)",
        "uso":      "USO(WTI 近月期貨展期)",
        "ann_2008": "2008:油價達 147\n隨後 USO 大跌 54%",
        "ann_2020": "2020/4 超級 contango\nUSO 一年內 -68%",
        "ann_gold": "黃金約 $3500 / 1 元 -> 約 12 元",
        "ann_uso":  "USO 不到 0.5 元(-50% 以上)",
        "footer":   "黃金:LBMA AM 年末價轉為 TR。USO:2006-2024 為公開 NAV TR;2000-2005 估為 WTI 近月百分比減 8%/年 contango 損耗。2025 與 2026/4 為部分年度。對數 y 軸。",
    },
    "tw": {
        "title":    "1 元投入實體黃金(GLDM 代理)vs USO,2000-2026/4",
        "subtitle": "相同資產類別,相反機制。黃金 ETF 持有金庫實金(無展期)。USO 持有 WTI 近月期貨並每月在長期 contango 中展期。差距純粹來自包裝層的耗損,並非對油價的看法。",
        "xlabel":   "年份",
        "ylabel":   "財富(2000/1 投入 1 元,對數軸)",
        "gold":     "實體黃金(GLDM 等價)",
        "uso":      "USO(WTI 近月期貨展期)",
        "ann_2008": "2008:油價達 147\n隨後 USO 大跌 54%",
        "ann_2020": "2020/4 超級 contango\nUSO 一年內 -68%",
        "ann_gold": "黃金約 $3500 / 1 元 -> 約 12 元",
        "ann_uso":  "USO 不到 0.5 元(-50% 以上)",
        "footer":   "黃金:LBMA AM 年末價轉為 TR。USO:2006-2024 為公開 NAV TR;2000-2005 估為 WTI 近月百分比減 8%/年 contango 耗損。2025 與 2026/4 為部分年度。對數 y 軸。",
    },
    "cn": {
        "title":    "1 元投入实物黄金(GLDM 代理)vs USO,2000-2026/4",
        "subtitle": "相同资产类别,相反机制。黄金 ETF 持有金库实金(无展期)。USO 持有 WTI 近月期货并每月在长期 contango 中展期。差距纯粹来自包装层的损耗,并非对油价的看法。",
        "xlabel":   "年份",
        "ylabel":   "财富(2000/1 投入 1 元,对数轴)",
        "gold":     "实物黄金(GLDM 等价)",
        "uso":      "USO(WTI 近月期货展期)",
        "ann_2008": "2008:油价达 147\n随后 USO 暴跌 54%",
        "ann_2020": "2020/4 超级 contango\nUSO 一年内 -68%",
        "ann_gold": "黄金约 $3500 / 1 元 -> 约 12 元",
        "ann_uso":  "USO 不到 0.5 元(-50% 以上)",
        "footer":   "黄金:LBMA AM 年末价转为 TR。USO:2006-2024 为公开 NAV TR;2000-2005 估为 WTI 近月百分比减 8%/年 contango 损耗。2025 与 2026/4 为部分年度。对数 y 轴。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    years = sorted(GOLD.keys())
    g = [1.0]
    u = [1.0]
    for y in years:
        g.append(g[-1] * (1.0 + GOLD[y]))
        u.append(u[-1] * (1.0 + USO[y]))
    xs = [years[0] - 1] + years

    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=150)
    style_axes(ax, p)

    ax.plot(xs, g, color=p["accent"], linewidth=2.8, label=s["gold"])
    ax.plot(xs, u, color=p["red"], linewidth=2.4, label=s["uso"], linestyle="-")

    ax.axhline(1.0, color=p["muted"], linewidth=0.7,
               linestyle="--", alpha=0.6)

    ax.set_yscale("log")
    ax.set_xlim(1998, 2028)
    ax.set_ylim(0.05, 30)
    ticks = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
    ax.set_yticks(ticks)
    ax.set_yticklabels([f"${t:.2f}" if t < 1 else f"${t:.0f}" for t in ticks])

    # Annotations
    g_arr = np.array(g)
    u_arr = np.array(u)
    xs_arr = np.array(xs)

    idx_08 = int(np.where(xs_arr == 2008)[0][0])
    ax.annotate(s["ann_2008"],
                xy=(2008, u_arr[idx_08]),
                xytext=(2004, 0.18),
                fontsize=8.5, color=p["red"], ha="center",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.7))

    idx_20 = int(np.where(xs_arr == 2020)[0][0])
    ax.annotate(s["ann_2020"],
                xy=(2020, u_arr[idx_20]),
                xytext=(2017, 0.10),
                fontsize=8.5, color=p["red"], ha="center",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.7))

    # End markers
    ax.scatter([xs_arr[-1]], [g_arr[-1]], color=p["accent"], s=60, zorder=5)
    ax.scatter([xs_arr[-1]], [u_arr[-1]], color=p["red"], s=60, zorder=5)
    ax.annotate(s["ann_gold"],
                xy=(xs_arr[-1], g_arr[-1]),
                xytext=(xs_arr[-1] - 9, g_arr[-1] * 1.6),
                fontsize=9, color=p["accent"], ha="center", weight="bold",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.7))
    ax.annotate(s["ann_uso"],
                xy=(xs_arr[-1], u_arr[-1]),
                xytext=(xs_arr[-1] - 9, u_arr[-1] * 0.45),
                fontsize=9, color=p["red"], ha="center", weight="bold",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.7))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold", loc="left")
    fig.text(0.5, 0.94, s["subtitle"], ha="center",
             fontsize=10.0, color=p["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.0, color=p["muted"])

    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
