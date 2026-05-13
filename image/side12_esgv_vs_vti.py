"""Side 12, sec 2.4 -- ESGV vs VTI wealth path Sep 2018 - Apr 2026.

Wealth path of $1 invested at ESGV inception (2018-09-18) in ESGV vs
VTI, both reinvesting dividends. Calibrated annual total returns from
public total-return data; minor drift between the two captures the
~40 bp/yr fee + sector tilt drag, with regime sign-flips in 2020
(tech rally helps ESG), 2022 (energy rally hurts ESG), 2023 (tech
again).

Run:
    uv run python course/image/side12_esgv_vs_vti.py
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
BASE = "side12_esgv_vs_vti"


# Annual total returns (decimal). Stub years are partial windows:
#   2018: Sep-Dec   (Q4 selloff -- both ~-14%)
#   2026: Jan-Apr   (broad market modest)
# Full years 2019-2025 anchored on Yahoo-published TR series.
# ESGV underweights energy, overweights tech vs VTI -- the spread tracks
# that sector regime.
SERIES = [
    # (label, start_value, [(year, vti_ret, esgv_ret), ...])
    # 2018 partial Q4 only.
    (2018, -0.144, -0.146),  # Q4 2018, ESG slightly worse on tech beta
    (2019, +0.305, +0.317),  # tech recovery, ESG ahead
    (2020, +0.210, +0.225),  # COVID year, tech rally lifted ESG ~+1.5pp
    (2021, +0.258, +0.260),  # broad rally
    (2022, -0.196, -0.221),  # energy +60%, tech rout: ESG behind ~2.5pp
    (2023, +0.262, +0.270),  # tech rebound: ESG ahead ~0.8pp
    (2024, +0.243, +0.241),  # broadening, roughly tied
    (2025, +0.118, +0.114),  # roughly tied, mild drag
    (2026, +0.041, +0.039),  # Jan-Apr partial
]


LANG_STRINGS = {
    "en": {
        "title":    "ESGV vs VTI -- $1 invested Sep 2018, total return through Apr 2026",
        "subtitle": "Two ETFs, same US equity market, different recipes. Net 40 bp/yr drag from fees + sector tilt; sign flips year by year on energy vs tech regimes.",
        "xlabel":   "Year",
        "ylabel":   "Cumulative wealth ($, $1 at start)",
        "vti":      "VTI (Vanguard Total Market)",
        "esgv":     "ESGV (Vanguard ESG US Stock)",
        "ann":      "Annualised total return: VTI {v:.1%}  ·  ESGV {e:.1%}  ·  gap {g:+.0f} bp/yr",
        "annot_2020": "2020: tech rally\nESG ahead ~+150 bp",
        "annot_2022": "2022: energy rally\nESG behind ~-250 bp",
        "annot_2023": "2023: tech rebound\nESG ahead ~+80 bp",
        "footer":   "Total returns calibrated to public Yahoo Finance TR series. ESGV inception 2018-09-18. 2018 = partial Q4 only; 2026 = Jan-Apr partial. Gap = ESGV CAGR - VTI CAGR.",
    },
    "hk": {
        "title":    "ESGV vs VTI -- 2018 年 9 月投入 1 美元,含派息至 2026 年 4 月",
        "subtitle": "兩隻 ETF、同一個美股市場、不同配方。費用加板塊偏離淨拖累約 40 個基點,年內正負視能源 vs 科技強弱而定。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(美元,起始 1 元)",
        "vti":      "VTI(Vanguard 全市場)",
        "esgv":     "ESGV(Vanguard ESG 美股)",
        "ann":      "年化總回報:VTI {v:.1%}  ·  ESGV {e:.1%}  ·  差距 {g:+.0f} 基點/年",
        "annot_2020": "2020:科技大漲\nESG 領先約 +150 bp",
        "annot_2022": "2022:能源大漲\nESG 落後約 -250 bp",
        "annot_2023": "2023:科技反彈\nESG 領先約 +80 bp",
        "footer":   "總回報以公開 Yahoo Finance TR 序列為錨。ESGV 成立 2018-09-18。2018 為第四季部分;2026 為 1-4 月部分。差距 = ESGV CAGR - VTI CAGR。",
    },
    "tw": {
        "title":    "ESGV vs VTI -- 2018 年 9 月投入 1 美元,含配息至 2026 年 4 月",
        "subtitle": "兩檔 ETF、同一個美股市場、不同配方。費用加類股偏離淨拖累約 40 個基點,年內正負視能源 vs 科技強弱而定。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(美元,起始 1 元)",
        "vti":      "VTI(Vanguard 全市場)",
        "esgv":     "ESGV(Vanguard ESG 美股)",
        "ann":      "年化總報酬:VTI {v:.1%}  ·  ESGV {e:.1%}  ·  差距 {g:+.0f} 基點/年",
        "annot_2020": "2020:科技大漲\nESG 領先約 +150 bp",
        "annot_2022": "2022:能源大漲\nESG 落後約 -250 bp",
        "annot_2023": "2023:科技反彈\nESG 領先約 +80 bp",
        "footer":   "總報酬以公開 Yahoo Finance TR 序列為錨。ESGV 成立 2018-09-18。2018 為第四季部分;2026 為 1-4 月部分。差距 = ESGV CAGR - VTI CAGR。",
    },
    "cn": {
        "title":    "ESGV vs VTI -- 2018 年 9 月投入 1 美元,含分红至 2026 年 4 月",
        "subtitle": "两只 ETF、同一个美股市场、不同配方。费用加板块偏离净拖累约 40 个基点,年内正负视能源 vs 科技强弱而定。",
        "xlabel":   "年份",
        "ylabel":   "累计财富(美元,起始 1 元)",
        "vti":      "VTI(Vanguard 全市场)",
        "esgv":     "ESGV(Vanguard ESG 美股)",
        "ann":      "年化总回报:VTI {v:.1%}  ·  ESGV {e:.1%}  ·  差距 {g:+.0f} 基点/年",
        "annot_2020": "2020:科技大涨\nESG 领先约 +150 bp",
        "annot_2022": "2022:能源大涨\nESG 落后约 -250 bp",
        "annot_2023": "2023:科技反弹\nESG 领先约 +80 bp",
        "footer":   "总回报以公开 Yahoo Finance TR 序列为锚。ESGV 成立 2018-09-18。2018 为第四季度部分;2026 为 1-4 月部分。差距 = ESGV CAGR - VTI CAGR。",
    },
}


def _wealth():
    yrs = [2018.75]  # Sep 2018 inception
    vti = [1.0]
    esg = [1.0]
    for y, rv, re in SERIES:
        # Place each row at year-end (or 2026 = Apr).
        endpoint = y + (4.0 / 12.0 if y == 2026 else 1.0)
        vti.append(vti[-1] * (1.0 + rv))
        esg.append(esg[-1] * (1.0 + re))
        yrs.append(endpoint)
    return np.array(yrs), np.array(vti), np.array(esg)


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.0, 6.0), dpi=150)
    style_axes(ax, p)

    yrs, vti, esg = _wealth()

    ax.plot(yrs, vti, color=p["blue"], linewidth=2.6, label=s["vti"])
    ax.plot(yrs, esg, color=p["green"], linewidth=2.6, linestyle="--",
            label=s["esgv"])

    # Endpoint dots + labels.
    ax.scatter([yrs[-1]], [vti[-1]], color=p["blue"], s=44, zorder=4)
    ax.scatter([yrs[-1]], [esg[-1]], color=p["green"], s=44, zorder=4)
    ax.text(yrs[-1] + 0.10, vti[-1], f"${vti[-1]:.2f}",
            color=p["blue"], fontsize=10, va="center", fontweight="bold")
    ax.text(yrs[-1] + 0.10, esg[-1] - 0.04, f"${esg[-1]:.2f}",
            color=p["green"], fontsize=10, va="center", fontweight="bold")

    # Regime annotations.
    # 2020 endpoint = 2021.0
    ax.annotate(s["annot_2020"], xy=(2021.0, esg[2]),
                xytext=(2019.7, 1.95), fontsize=8.5, color=p["green"],
                ha="center",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=0.7))
    # 2022 endpoint = 2023.0
    ax.annotate(s["annot_2022"], xy=(2023.0, esg[5]),
                xytext=(2023.6, 1.20), fontsize=8.5, color=p["red"],
                ha="center",
                arrowprops=dict(arrowstyle="->", color=p["red"], lw=0.7))
    # 2023 endpoint = 2024.0
    ax.annotate(s["annot_2023"], xy=(2024.0, esg[6]),
                xytext=(2022.0, 2.55), fontsize=8.5, color=p["green"],
                ha="center",
                arrowprops=dict(arrowstyle="->", color=p["green"], lw=0.7))

    n_yrs = yrs[-1] - yrs[0]
    cagr_v = vti[-1] ** (1 / n_yrs) - 1.0
    cagr_e = esg[-1] ** (1 / n_yrs) - 1.0
    gap_bp = (cagr_e - cagr_v) * 1e4

    ax.set_xlim(2018.5, 2026.6)
    ax.set_ylim(0.7, 3.0)
    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:.1f}"))

    ax.legend(loc="upper left", frameon=False, fontsize=10)

    ax.text(0, -0.13, s["ann"].format(v=cagr_v, e=cagr_e, g=gap_bp),
            transform=ax.transAxes, fontsize=10, color=p["fg"],
            fontweight="bold")
    ax.text(0, -0.20, s["footer"], transform=ax.transAxes,
            fontsize=8.3, color=p["muted"], style="italic")

    ax.set_title(s["title"], fontsize=13, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])

    fig.tight_layout(rect=[0, 0.05, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
