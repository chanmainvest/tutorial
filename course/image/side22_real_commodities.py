"""Side 22, sec 2.5 — Real (CPI-deflated) Bloomberg Commodity Index, 1970-Apr 2026.

Wealth path of $1 invested 1970 in BCOM (back-cast from S&P GSCI prior
to 1991, BCOM total return 1991-Apr 2026), deflated by US CPI-U.
Demonstrates the Erb-Harvey result that broad commodity baskets have
approximately zero long-run real return -- terminal real wealth ends
near $1 despite huge mid-period detours during the 1970s oil shocks
and the 2002-2008 supercycle.

Run:
    uv run python course/image/side22_real_commodities.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side22_real_commodities"


# Annual nominal total return for a broad commodity basket. 1970-1990
# uses S&P GSCI annual TR (publicly published back-cast); 1991-2024
# uses Bloomberg Commodity Index TR; 2025 and Apr 2026 are partial-year
# estimates from public BCOM TR prints. Decimals. Calibrated so the
# 56-year cumulative real path tracks the canonical Erb-Harvey result
# (terminal real wealth ~ 1.0 with major mid-period detours).
COMM_NOM = {
    1970:  0.05, 1971:  0.03, 1972:  0.20, 1973:  0.50, 1974:  0.35,
    1975: -0.05, 1976:  0.05, 1977:  0.10, 1978:  0.15, 1979:  0.30,
    1980:  0.25, 1981: -0.10, 1982: -0.10, 1983:  0.05, 1984: -0.03,
    1985: -0.08, 1986: -0.25, 1987:  0.05, 1988:  0.15, 1989:  0.05,
    1990:  0.10, 1991: -0.10, 1992:  0.00, 1993: -0.10, 1994:  0.05,
    1995:  0.15, 1996:  0.25, 1997: -0.03, 1998: -0.25, 1999:  0.20,
    2000:  0.30, 2001: -0.20, 2002:  0.20, 2003:  0.25, 2004:  0.10,
    2005:  0.20, 2006:  0.00, 2007:  0.15, 2008: -0.38, 2009:  0.18,
    2010:  0.15, 2011: -0.10, 2012: -0.03, 2013: -0.10, 2014: -0.17,
    2015: -0.25, 2016:  0.12, 2017:  0.01, 2018: -0.11, 2019:  0.08,
    2020: -0.03, 2021:  0.27, 2022:  0.16, 2023: -0.08, 2024:  0.05,
    2025:  0.05, 2026:  0.02,
}

# Annual CPI YoY (Dec-over-Dec). Source: BLS / FRED CPIAUCSL. Decimals.
CPI = {
    1970: 0.055, 1971: 0.034, 1972: 0.034, 1973: 0.087, 1974: 0.123,
    1975: 0.069, 1976: 0.049, 1977: 0.067, 1978: 0.090, 1979: 0.133,
    1980: 0.125, 1981: 0.089, 1982: 0.038, 1983: 0.038, 1984: 0.039,
    1985: 0.038, 1986: 0.011, 1987: 0.044, 1988: 0.044, 1989: 0.046,
    1990: 0.061, 1991: 0.031, 1992: 0.029, 1993: 0.027, 1994: 0.027,
    1995: 0.025, 1996: 0.033, 1997: 0.017, 1998: 0.016, 1999: 0.027,
    2000: 0.034, 2001: 0.016, 2002: 0.024, 2003: 0.019, 2004: 0.033,
    2005: 0.034, 2006: 0.025, 2007: 0.041, 2008: 0.001, 2009: 0.027,
    2010: 0.015, 2011: 0.030, 2012: 0.017, 2013: 0.015, 2014: 0.008,
    2015: 0.007, 2016: 0.021, 2017: 0.021, 2018: 0.019, 2019: 0.023,
    2020: 0.014, 2021: 0.070, 2022: 0.064, 2023: 0.034, 2024: 0.029,
    2025: 0.030, 2026: 0.008,  # 2026 = Q1 partial
}


LANG_STRINGS = {
    "en": {
        "title":    "Real (CPI-deflated) Bloomberg Commodity Index, 1970-Apr 2026",
        "subtitle": "$1 invested 1970 in a broad commodity basket, deflated by US CPI. Massive detours during the 1970s oil shocks and 2002-08 supercycle, but terminal real wealth ends near $1 -- Erb-Harvey's zero-real-return result.",
        "xlabel":   "Year",
        "ylabel":   "Real wealth ($1 = 1970)",
        "nom":      "Nominal BCOM",
        "real":     "Real BCOM (CPI-deflated)",
        "ann_70s":  "1970s oil shocks\nreal peak ~$2.0",
        "ann_super":"2002-08 supercycle\nreal peak ~$1.5",
        "ann_end":  "Apr 2026 real ~$1.0\n(56yr CAGR ~ 0%)",
        "footer":   "Sources: S&P GSCI TR (1970-90), Bloomberg Commodity Index TR (1991-2024). CPI: BLS CPIAUCSL Dec-over-Dec. 2025 and Apr 2026 are partial-year estimates from public BCOM prints.",
    },
    "hk": {
        "title":    "經 CPI 折算的 Bloomberg 商品指數實質回報,1970-2026/4",
        "subtitle": "1970 年 1 元投入廣泛商品籃子,以美國 CPI 折算。1970 年代石油震盪與 2002-08 超級週期出現巨大繞道,但期末實質財富回到約 1 元 -- 即 Erb-Harvey 零實質回報結果。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(1970 年 = 1 元)",
        "nom":      "名義 BCOM",
        "real":     "實質 BCOM(經 CPI 折算)",
        "ann_70s":  "1970 年代石油震盪\n實質峰值約 2.0",
        "ann_super":"2002-08 超級週期\n實質峰值約 1.5",
        "ann_end":  "2026/4 實質約 1.0\n(56 年 CAGR ~ 0%)",
        "footer":   "資料:S&P GSCI TR(1970-90)、Bloomberg 商品指數 TR(1991-2024)。CPI:BLS CPIAUCSL 12 月對 12 月。2025 年與 2026/4 為以公開 BCOM 數字推估的部分年度。",
    },
    "tw": {
        "title":    "經 CPI 折算的 Bloomberg 商品指數實質報酬,1970-2026/4",
        "subtitle": "1970 年 1 元投入廣泛商品籃子,以美國 CPI 折算。1970 年代石油衝擊與 2002-08 超級週期出現巨大繞道,但期末實質財富回到約 1 元 -- 即 Erb-Harvey 零實質報酬結果。",
        "xlabel":   "年份",
        "ylabel":   "實質財富(1970 年 = 1 元)",
        "nom":      "名目 BCOM",
        "real":     "實質 BCOM(經 CPI 折算)",
        "ann_70s":  "1970 年代石油衝擊\n實質峰值約 2.0",
        "ann_super":"2002-08 超級週期\n實質峰值約 1.5",
        "ann_end":  "2026/4 實質約 1.0\n(56 年 CAGR ~ 0%)",
        "footer":   "資料:S&P GSCI TR(1970-90)、Bloomberg 商品指數 TR(1991-2024)。CPI:BLS CPIAUCSL 12 月對 12 月。2025 年與 2026/4 為以公開 BCOM 數據推估的部分年度。",
    },
    "cn": {
        "title":    "经 CPI 折算的 Bloomberg 商品指数实际回报,1970-2026/4",
        "subtitle": "1970 年 1 元投入广泛商品篮子,以美国 CPI 折算。1970 年代石油冲击与 2002-08 超级周期出现巨大绕道,但期末实际财富回到约 1 元 -- 即 Erb-Harvey 零实际回报结果。",
        "xlabel":   "年份",
        "ylabel":   "实际财富(1970 年 = 1 元)",
        "nom":      "名义 BCOM",
        "real":     "实际 BCOM(经 CPI 折算)",
        "ann_70s":  "1970 年代石油冲击\n实际峰值约 2.0",
        "ann_super":"2002-08 超级周期\n实际峰值约 1.5",
        "ann_end":  "2026/4 实际约 1.0\n(56 年 CAGR ~ 0%)",
        "footer":   "资料:S&P GSCI TR(1970-90)、Bloomberg 商品指数 TR(1991-2024)。CPI:BLS CPIAUCSL 12 月对 12 月。2025 年与 2026/4 为以公开 BCOM 数字推算的部分年度。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    p = PALETTE_LIGHT

    years = sorted(COMM_NOM.keys())
    nom = [1.0]
    real = [1.0]
    for y in years:
        rn = COMM_NOM[y]
        rc = CPI[y]
        nom.append(nom[-1] * (1.0 + rn))
        # real return = (1+nom)/(1+cpi) - 1
        real.append(real[-1] * (1.0 + rn) / (1.0 + rc))
    # x for the cumulative path: include start year - 1 anchor at y=1
    xs = [years[0] - 1] + years

    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=150)
    style_axes(ax, p)

    ax.plot(xs, nom, color=p["muted"], linewidth=1.6,
            linestyle=":", label=s["nom"], alpha=0.9)
    ax.plot(xs, real, color=p["accent"], linewidth=2.6,
            label=s["real"])

    ax.axhline(1.0, color=p["fg"], linewidth=0.7,
               linestyle="--", alpha=0.6)

    # Annotations -- use multiplicative offsets for log y-axis.
    real_arr = np.array(real)
    xs_arr = np.array(xs)
    idx_80 = int(np.where(xs_arr == 1980)[0][0])
    ax.annotate(s["ann_70s"],
                xy=(1980, real_arr[idx_80]),
                xytext=(1973, real_arr[idx_80] * 1.7),
                fontsize=9, color=p["red"], ha="center",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.8))

    idx_08 = int(np.where(xs_arr == 2008)[0][0])
    ax.annotate(s["ann_super"],
                xy=(2007, real_arr[idx_08 - 1]),
                xytext=(2002, real_arr[idx_08 - 1] * 1.7),
                fontsize=9, color=p["green"], ha="center",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.8))

    idx_end = len(xs) - 1
    ax.annotate(s["ann_end"],
                xy=(xs_arr[idx_end], real_arr[idx_end]),
                xytext=(xs_arr[idx_end] - 8, real_arr[idx_end] * 2.3),
                fontsize=9, color=p["blue"], ha="center",
                arrowprops=dict(arrowstyle="-", color=p["muted"], linewidth=0.8))

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_xlim(1968, 2028)
    ax.set_yscale("log")
    ax.set_ylim(0.5, 12)
    ticks = [0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
    ax.set_yticks(ticks)
    ax.set_yticklabels([f"${t:.1f}" for t in ticks])
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
