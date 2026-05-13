"""Side 03, sec 2.2 -- VTSAX vs VTI cumulative after-tax wealth, 2005-2025.

Embedded approximate annual data: SP500 total return, Vanguard
Total Stock Market price-only return, dividend yield, and the
mutual fund's special capital-gain distribution as a share of NAV
in years where one occurred. Both funds share the same portfolio
at the same 4 bp expense; the ETF (VTI) realises essentially zero
fund-level cap gains because of in-kind redemptions, while the
mutual fund (VTSAX) occasionally pushes a distribution that the
shareholder must pay tax on at the LTCG rate.

Run:
    uv run python course/image/side03_etf_vs_mf_tax.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side03_etf_vs_mf_tax"


# Approximate annual data 2005-2024 -----------------------------------------
# total_return: Vanguard Total Stock Market total return (proxy via VTI/VTSAX)
# div_yield: ordinary qualified dividend yield (already taxed each year for
#   both wrappers).  cap_gain_dist: VTSAX-only special capital-gain
#   distribution as a fraction of year-end NAV.  VTI distributions were
#   essentially zero across the entire history, so we set them to 0.
YEARS = list(range(2005, 2025))
TOTAL_RETURN = [
    0.0625, 0.1546, 0.0566, -0.3699, 0.2843, 0.1733, 0.0107, 0.1610,
    0.3349, 0.1271, 0.0042, 0.1267, 0.2114, -0.0518, 0.3068, 0.2087,
    0.2576, -0.1956, 0.2613, 0.2362,
]
DIV_YIELD = [
    0.0180, 0.0185, 0.0195, 0.0240, 0.0210, 0.0195, 0.0205, 0.0210,
    0.0195, 0.0190, 0.0205, 0.0200, 0.0185, 0.0205, 0.0185, 0.0150,
    0.0140, 0.0165, 0.0150, 0.0140,
]
# VTSAX-only year-end LT cap gain distributions (fraction of NAV).
# Source: Vanguard distribution history (approximate).  VTI's ETF wrapper
# has not distributed a meaningful capital gain in any of these years.
VTSAX_CG_DIST = {
    2005: 0.0000, 2006: 0.0000, 2007: 0.0000, 2008: 0.0010, 2009: 0.0000,
    2010: 0.0000, 2011: 0.0000, 2012: 0.0000, 2013: 0.0000, 2014: 0.0030,
    2015: 0.0080, 2016: 0.0000, 2017: 0.0000, 2018: 0.0070, 2019: 0.0000,
    2020: 0.0050, 2021: 0.0040, 2022: 0.0000, 2023: 0.0000, 2024: 0.0030,
}

# Tax model (24% federal + 5% state, qualified div / LT cap gain at 15%+5%)
INITIAL = 100_000.0
LTCG_RATE = 0.15 + 0.05      # federal + state
QDI_RATE  = 0.15 + 0.05      # qualified-dividend treated same as LTCG
# Note: terminal sale tax is the same for both wrappers (you sell when you
# choose), so we exclude it -- we are isolating the *fund-level distribution*
# tax drag that mutual funds suffer and ETFs avoid.


def simulate():
    """Return ((years, vti_path, vtsax_path), terminal_diff_pct)."""
    n = len(YEARS)
    vti = [INITIAL]
    vtsax = [INITIAL]
    for i in range(n):
        ret = TOTAL_RETURN[i]
        dy  = DIV_YIELD[i]
        cg  = VTSAX_CG_DIST[YEARS[i]]
        # Both wrappers pay annual qualified-dividend tax on the dividend
        # portion (assume div paid out and re-invested net of tax).
        div_drag = dy * QDI_RATE
        # ETF: only div drag.
        vti.append(vti[-1] * (1 + ret - div_drag))
        # Mutual fund: also loses cg * LTCG rate to fund-level distribution
        # (re-invested net of tax).
        cg_drag = cg * LTCG_RATE
        vtsax.append(vtsax[-1] * (1 + ret - div_drag - cg_drag))
    years_x = [YEARS[0] - 1] + YEARS
    return years_x, vti, vtsax


LANG_STRINGS = {
    "en": {
        "title": "VTI vs VTSAX -- 100k After-Tax Wealth, 2005-2024 (Taxable Account, 20% LTCG/QDI Rate)",
        "subtitle": "Same portfolio, same fee. ETF avoids the mutual fund's year-end capital-gain distributions via in-kind redemptions.",
        "ylabel": "After-tax wealth (USD)",
        "xlabel": "Year",
        "vti_lbl": "VTI (ETF)",
        "vtsax_lbl": "VTSAX (mutual fund)",
        "vti_end": "VTI: ${:,.0f}",
        "vtsax_end": "VTSAX: ${:,.0f}",
        "diff_lbl": "Wrapper edge after 20yr: +${:,.0f} ({:+.1f}%)",
        "footnote": "Approximate model. VTI capital-gain distributions have been essentially zero across this entire 20-year window (Section 852(b)(6) in-kind exemption). VTSAX has paid distributions in 2008/2014/2015/2018/2020/2021/2024.",
    },
    "hk": {
        "title": "VTI vs VTSAX -- 10 萬美元稅後財富,2005-2024(應稅戶口,20% LTCG/QDI 稅率)",
        "subtitle": "同一組合、同一費率。ETF 透過實物贖回避免共同基金的年終資本利得分派。",
        "ylabel": "稅後財富(美元)",
        "xlabel": "年份",
        "vti_lbl": "VTI(ETF)",
        "vtsax_lbl": "VTSAX(共同基金)",
        "vti_end": "VTI:US${:,.0f}",
        "vtsax_end": "VTSAX:US${:,.0f}",
        "diff_lbl": "20 年包裝結構優勢:+US${:,.0f}({:+.1f}%)",
        "footnote": "近似模型。VTI 在過去 20 年的資本利得分派基本為零(IRC 852(b)(6) 實物豁免)。VTSAX 於 2008/2014/2015/2018/2020/2021/2024 有分派。",
    },
    "tw": {
        "title": "VTI vs VTSAX -- 10 萬美元稅後財富,2005-2024(應稅帳戶,20% LTCG/QDI 稅率)",
        "subtitle": "同一投組、同一費率。ETF 透過實物贖回避免共同基金的年終資本利得配息。",
        "ylabel": "稅後財富(美元)",
        "xlabel": "年份",
        "vti_lbl": "VTI(ETF)",
        "vtsax_lbl": "VTSAX(共同基金)",
        "vti_end": "VTI:US${:,.0f}",
        "vtsax_end": "VTSAX:US${:,.0f}",
        "diff_lbl": "20 年包裝結構優勢:+US${:,.0f}({:+.1f}%)",
        "footnote": "近似模型。VTI 在過去 20 年的資本利得配息基本為零(IRC 852(b)(6) 實物豁免)。VTSAX 於 2008/2014/2015/2018/2020/2021/2024 有配息。",
    },
    "cn": {
        "title": "VTI vs VTSAX -- 10 万美元税后财富,2005-2024(应税账户,20% LTCG/QDI 税率)",
        "subtitle": "同一组合、同一费率。ETF 通过实物赎回避免共同基金的年终资本利得分配。",
        "ylabel": "税后财富(美元)",
        "xlabel": "年份",
        "vti_lbl": "VTI(ETF)",
        "vtsax_lbl": "VTSAX(共同基金)",
        "vti_end": "VTI:US${:,.0f}",
        "vtsax_end": "VTSAX:US${:,.0f}",
        "diff_lbl": "20 年包装结构优势:+US${:,.0f}({:+.1f}%)",
        "footnote": "近似模型。VTI 在过去 20 年的资本利得分配基本为零(IRC 852(b)(6) 实物豁免)。VTSAX 于 2008/2014/2015/2018/2020/2021/2024 有分配。",
    },
}


def build_fig(s):
    P = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}
    years_x, vti, vtsax = simulate()
    diff = vti[-1] - vtsax[-1]
    diff_pct = (vti[-1] / vtsax[-1] - 1.0) * 100.0

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax)

    ax.plot(years_x, vti, color=P["blue"], linewidth=2.6,
            label=s["vti_lbl"], marker="o", markersize=4.5,
            markerfacecolor=P["blue"], markeredgecolor="white")
    ax.plot(years_x, vtsax, color=P["red"], linewidth=2.4,
            linestyle=(0, (5, 3)), label=s["vtsax_lbl"],
            marker="s", markersize=4.0,
            markerfacecolor=P["red"], markeredgecolor="white")

    # Mark VTSAX distribution years on the path
    for yr, cg in VTSAX_CG_DIST.items():
        if cg > 0:
            idx = YEARS.index(yr) + 1
            ax.scatter([years_x[idx]], [vtsax[idx]],
                       s=80, facecolor="none", edgecolor=P["accent"],
                       linewidth=1.6, zorder=5)

    # End-of-period annotations
    ax.annotate(s["vti_end"].format(vti[-1]),
                xy=(years_x[-1], vti[-1]), xytext=(8, 14),
                textcoords="offset points",
                color=P["blue"], fontsize=10.5, weight="bold")
    ax.annotate(s["vtsax_end"].format(vtsax[-1]),
                xy=(years_x[-1], vtsax[-1]), xytext=(8, -18),
                textcoords="offset points",
                color=P["red"], fontsize=10.5, weight="bold")

    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_title(s["title"], pad=24, fontsize=13.5, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")

    # Edge box
    edge_text = s["diff_lbl"].format(diff, diff_pct)
    ax.text(0.02, 0.97, edge_text, transform=ax.transAxes,
            ha="left", va="top",
            fontsize=11, weight="bold", color=P["green"],
            bbox=dict(boxstyle="round,pad=0.45",
                      facecolor="#e8f5e9",
                      edgecolor=P["green"], linewidth=1.2))

    ax.legend(loc="lower right", frameon=True, fontsize=10.5,
              facecolor=P["bg"], edgecolor=P["grid"])
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"${v/1000:,.0f}k"))
    ax.set_xlim(years_x[0] - 0.3, years_x[-1] + 1.6)

    fig.text(0.5, 0.02, s["footnote"], ha="center",
             fontsize=8.8, color=P["muted"])
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    yrs, vti, vtsax = simulate()
    print(f"VTI  end: ${vti[-1]:,.0f}")
    print(f"VTSAX end: ${vtsax[-1]:,.0f}")
    print(f"Edge: ${vti[-1]-vtsax[-1]:,.0f}  ({(vti[-1]/vtsax[-1]-1)*100:+.2f}%)")
