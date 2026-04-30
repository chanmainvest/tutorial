"""Side 25, sec 2.4 -- HFRI Composite vs 60/40 vs S&P 500 wealth path.

Three-line wealth path of $1 invested Jan 2000 through Apr 2026 in:
  - HFRI Fund Weighted Composite Index (industry average)
  - 60/40 SPY/AGG annually rebalanced
  - S&P 500 total return

Annual returns embedded inline. HFRI from HFR public composite tables;
SPY total return from Damodaran histretSP; AGG from Vanguard VBMFX
proxy + Aggregate index post-2003. Apr 2026 is partial-year YTD.

Run:
    uv run python course/image/side25_hfri_vs_60_40.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side25_hfri_vs_60_40"

# Annual total returns (decimal). 2026 is partial YTD through April.
# HFRI: HFR public Fund Weighted Composite (HFRX/HFRI consensus).
# SPX: S&P 500 total return (Damodaran).
# AGG: Bloomberg US Aggregate (VBMFX/VBTLX/AGG composite).
DATA = {
#   year   HFRI    SPX     AGG
    2000: ( 0.050, -0.091,  0.118),
    2001: ( 0.046, -0.119,  0.084),
    2002: (-0.014, -0.221,  0.103),
    2003: ( 0.197,  0.286,  0.041),
    2004: ( 0.090,  0.108,  0.043),
    2005: ( 0.092,  0.049,  0.024),
    2006: ( 0.128,  0.158,  0.043),
    2007: ( 0.100,  0.055,  0.070),
    2008: (-0.190, -0.370,  0.052),
    2009: ( 0.200,  0.265,  0.059),
    2010: ( 0.105,  0.151,  0.065),
    2011: (-0.051,  0.021,  0.078),
    2012: ( 0.063,  0.160,  0.042),
    2013: ( 0.094,  0.323,  -0.020),
    2014: ( 0.030,  0.137,  0.060),
    2015: (-0.011,  0.014,  0.005),
    2016: ( 0.055,  0.120,  0.027),
    2017: ( 0.087,  0.218,  0.035),
    2018: (-0.046, -0.044, -0.000),
    2019: ( 0.103,  0.315,  0.087),
    2020: ( 0.117,  0.184,  0.075),
    2021: ( 0.103,  0.288, -0.015),
    2022: (-0.004, -0.181, -0.130),
    2023: ( 0.080,  0.262,  0.054),
    2024: ( 0.097,  0.250,  0.013),
    2025: ( 0.072,  0.110,  0.038),
    2026: ( 0.018,  0.034,  0.012),  # YTD through Apr 2026
}

LANG_STRINGS = {
    "en": {
        "title":    "HFRI Composite vs 60/40 vs S&P 500: $1 -> ?, Jan 2000 - Apr 2026",
        "subtitle": "Hedge fund category average roughly tied 60/40 over 26 years. Both lost badly to plain S&P 500.",
        "xlabel":   "Year",
        "ylabel":   "Wealth from $1 invested Jan 2000",
        "lbl_hfri": "HFRI Composite",
        "lbl_6040": "60/40 (SPY + AGG, annual rebal)",
        "lbl_spx":  "S&P 500 total return",
        "ann_2008": "2008: HFRI -19%, 60/40 -22%, SPX -37%",
        "ann_regime": "Pre-2009: HFRI alpha was real. Post-2009: 60/40-with-fees.",
        "footer":   "HFRI from HFR public Fund Weighted Composite. SPX from Damodaran histretSP. AGG = Bloomberg US Aggregate proxy. 2026 YTD through April.",
    },
    "hk": {
        "title":    "HFRI 綜合指數 vs 60/40 vs 標普 500:$1 變多少?2000 年 1 月 - 2026 年 4 月",
        "subtitle": "對沖基金平均回報 26 年來大致與 60/40 打平,兩者都遠遠輸給單純標普 500。",
        "xlabel":   "年份",
        "ylabel":   "2000 年 1 月起投入 1 美元的累積財富",
        "lbl_hfri": "HFRI 綜合指數",
        "lbl_6040": "60/40(SPY + AGG,年度再平衡)",
        "lbl_spx":  "標普 500 總回報",
        "ann_2008": "2008 年:HFRI -19%、60/40 -22%、標普 500 -37%",
        "ann_regime": "2009 年前:對沖基金有真 alpha。2009 年後:60/40 加費用。",
        "footer":   "HFRI 源自 HFR 公開綜合指數;標普 500 源自 Damodaran;AGG 為彭博美國綜合指數代理。2026 年為 4 月底前 YTD。",
    },
    "tw": {
        "title":    "HFRI 綜合指數 vs 60/40 vs 標普 500:$1 變多少?2000 年 1 月 - 2026 年 4 月",
        "subtitle": "避險基金平均報酬 26 年來大致與 60/40 打平,兩者都遠遠輸給單純標普 500。",
        "xlabel":   "年份",
        "ylabel":   "2000 年 1 月起投入 1 美元的累積財富",
        "lbl_hfri": "HFRI 綜合指數",
        "lbl_6040": "60/40(SPY + AGG,年度再平衡)",
        "lbl_spx":  "標普 500 總報酬",
        "ann_2008": "2008 年:HFRI -19%、60/40 -22%、標普 -37%",
        "ann_regime": "2009 年前:避險基金有真 alpha。2009 年後:60/40 加費用。",
        "footer":   "HFRI 源自 HFR 公開綜合指數;標普 500 源自 Damodaran;AGG 為彭博美國綜合指數代理。2026 年為 4 月底前 YTD。",
    },
    "cn": {
        "title":    "HFRI 综合指数 vs 60/40 vs 标普 500:$1 变多少?2000 年 1 月 - 2026 年 4 月",
        "subtitle": "对冲基金平均回报 26 年来大致与 60/40 打平,两者都远远输给单纯标普 500。",
        "xlabel":   "年份",
        "ylabel":   "2000 年 1 月起投入 1 美元的累计财富",
        "lbl_hfri": "HFRI 综合指数",
        "lbl_6040": "60/40(SPY + AGG,年度再平衡)",
        "lbl_spx":  "标普 500 总回报",
        "ann_2008": "2008 年:HFRI -19%、60/40 -22%、标普 -37%",
        "ann_regime": "2009 年前:对冲基金有真 alpha。2009 年后:60/40 加费用。",
        "footer":   "HFRI 源自 HFR 公开综合指数;标普 500 源自 Damodaran;AGG 为彭博美国综合指数代理。2026 年为 4 月底前 YTD。",
    },
}


def _build_paths():
    years = sorted(DATA.keys())
    hfri = [1.0]
    sxty = [1.0]
    spx  = [1.0]
    for y in years:
        h, s, a = DATA[y]
        hfri.append(hfri[-1] * (1 + h))
        # 60/40 annually rebalanced: weighted return on each year
        sxty.append(sxty[-1] * (1 + 0.60 * s + 0.40 * a))
        spx.append(spx[-1] * (1 + s))
    x_years = [years[0] - 1] + years  # year 0 = start of 2000 = end of 1999
    return np.array(x_years), np.array(hfri), np.array(sxty), np.array(spx)


def build_fig(s):
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    x, hfri, sxty, spx = _build_paths()

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax, p)

    ax.plot(x, hfri, color=p["blue"], linewidth=2.6, label=s["lbl_hfri"])
    ax.plot(x, sxty, color=p["green"], linewidth=2.4, label=s["lbl_6040"])
    ax.plot(x, spx,  color=p["accent"], linewidth=2.6, label=s["lbl_spx"])

    # Endpoint labels
    end_x = x[-1]
    ax.scatter([end_x] * 3, [hfri[-1], sxty[-1], spx[-1]],
               color=[p["blue"], p["green"], p["accent"]],
               s=42, zorder=5, edgecolors="white", linewidths=1.2)
    ax.text(end_x + 0.3, hfri[-1], r"\$" + f"{hfri[-1]:.2f}",
            fontsize=10, fontweight="bold", color=p["blue"], va="center")
    ax.text(end_x + 0.3, sxty[-1], r"\$" + f"{sxty[-1]:.2f}",
            fontsize=10, fontweight="bold", color=p["green"], va="center")
    ax.text(end_x + 0.3, spx[-1], r"\$" + f"{spx[-1]:.2f}",
            fontsize=10, fontweight="bold", color=p["accent"], va="center")

    # 2008 annotation
    ax.annotate(s["ann_2008"],
                xy=(2008, hfri[list(x).index(2008)]),
                xytext=(2003, 5.6),
                fontsize=9.0, color=p["red"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.8))

    # Regime divide
    ax.axvline(2008, color=p["muted"], linestyle=":", linewidth=1.0, alpha=0.7)
    ax.text(2008.2, 7.4, s["ann_regime"],
            fontsize=8.8, color=p["muted"], style="italic")

    ax.set_xlim(1999, end_x + 1.6)
    ax.set_ylim(0.5, 8.5)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], pad=24, fontsize=13.5, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10, color=p["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=p["muted"], style="italic")

    ax.legend(loc="upper left", frameon=True, fontsize=10,
              facecolor=p["bg"], edgecolor=p["grid"])
    ax.grid(True, color=p["grid"], linewidth=0.6, alpha=0.7)

    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
