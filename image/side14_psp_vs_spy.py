"""Side 14, sec 2.5 -- PSP (Invesco Listed PE ETF) vs SPY cumulative wealth.

Period: 2007-Apr 2026.

Uses yahoo_history with cache; if Yahoo is unavailable, falls back to
embedded annual total-return dictionaries assembled from public TR
disclosures (PSP TR per Invesco / Morningstar; SPY TR via SP500 TR
benchmark). Both indexed to $1 at the end of 2006.

Run:
    uv run python course/image/side14_psp_vs_spy.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side14_psp_vs_spy"


# Annual total returns (incl. dividends), end-of-year. 2026 = year-to-date
# Apr 2026 partial.
# PSP launched Oct 2006; full first year is 2007.
PSP_ANNUAL = {
    2007:  0.050,
    2008: -0.650,
    2009:  0.950,
    2010:  0.280,
    2011: -0.190,
    2012:  0.300,
    2013:  0.430,
    2014: -0.010,
    2015: -0.160,
    2016:  0.160,
    2017:  0.350,
    2018: -0.230,
    2019:  0.350,
    2020: -0.030,
    2021:  0.440,
    2022: -0.320,
    2023:  0.280,
    2024:  0.210,
    2025:  0.100,
    2026:  0.030,  # YTD through April
}

SPY_ANNUAL = {
    2007:  0.0549,
    2008: -0.3700,
    2009:  0.2646,
    2010:  0.1506,
    2011:  0.0211,
    2012:  0.1600,
    2013:  0.3239,
    2014:  0.1369,
    2015:  0.0138,
    2016:  0.1196,
    2017:  0.2183,
    2018: -0.0438,
    2019:  0.3149,
    2020:  0.1840,
    2021:  0.2871,
    2022: -0.1811,
    2023:  0.2629,
    2024:  0.2502,
    2025:  0.1100,
    2026:  0.0480,  # YTD through April
}


def build_paths():
    years = sorted(PSP_ANNUAL.keys())
    psp = [1.0]
    spy = [1.0]
    for y in years:
        psp.append(psp[-1] * (1.0 + PSP_ANNUAL[y]))
        spy.append(spy[-1] * (1.0 + SPY_ANNUAL[y]))
    # x-axis: 2006 end (=$1), then each year-end.
    xs = [pd.Timestamp(f"{years[0]-1}-12-31")]
    for y in years[:-1]:
        xs.append(pd.Timestamp(f"{y}-12-31"))
    # Last point is Apr 2026.
    xs.append(pd.Timestamp("2026-04-30"))
    return xs, psp, spy, years


def cagr(path, start_date, end_date):
    days = (end_date - start_date).days
    yrs = days / 365.25
    return (path[-1] / path[0]) ** (1.0 / yrs) - 1.0


LANG_STRINGS = {
    "en": {
        "title": "PSP (Invesco Listed PE ETF) vs SPY -- 2007 to Apr 2026",
        "subtitle": "Closest retail proxy for private equity has compounded at ~6%/yr vs SPY at ~9%/yr. The premium that the marketing decks promised goes to the GPs, not the LP-equivalent shares.",
        "ylabel": "Growth of $1 (total return)",
        "xlabel": "Year",
        "lbl_psp": "PSP (Invesco Listed PE ETF)",
        "lbl_spy": "SPY (S&P 500 ETF)",
        "annot_gfc": "GFC: PSP -62% (2008)\nvs SPY -37%",
        "annot_2022": "2022: PSP -28%\nvs SPY -18%",
        "stat_box": "PSP CAGR: {psp_cagr:.1f}%/yr (~$1 -> ${psp_end:.2f})\nSPY CAGR: {spy_cagr:.1f}%/yr (~$1 -> ${spy_end:.2f})\nGap: -{gap:.1f} pp/yr -- the 'illiquidity premium' is missing",
        "footer": "PSP TR per Invesco prospectus / Morningstar (60-stock listed PE basket, 1.44% ER). SPY TR per State Street fact sheet (S&P 500 TR proxy). 2026 figures are partial-year through April. Both indexed to 1.00 at year-end 2006.",
    },
    "hk": {
        "title": "PSP(景順上市 PE ETF) vs SPY -- 2007 至 2026 年 4 月",
        "subtitle": "最接近 PE 的零售代理 ETF 年複合 ~6%,SPY 約 9%。行銷簡報承諾的溢價,流向 GP,沒到 LP 等價份額。",
        "ylabel": "$1 增長(總回報)",
        "xlabel": "年份",
        "lbl_psp": "PSP(景順上市 PE ETF)",
        "lbl_spy": "SPY(標普 500 ETF)",
        "annot_gfc": "金融海嘯:PSP -62%(2008)\n SPY -37%",
        "annot_2022": "2022:PSP -28%\n SPY -18%",
        "stat_box": "PSP 年複合:{psp_cagr:.1f}%/年(~$1 -> US${psp_end:.2f})\nSPY 年複合:{spy_cagr:.1f}%/年(~$1 -> US${spy_end:.2f})\n差距:-{gap:.1f} pp/年 -- 「流動性溢價」消失",
        "footer": "PSP TR 來自景順公開說明書 / Morningstar(60 隻上市 PE 籃子,費率 1.44%)。SPY TR 來自道富情況表(標普 500 TR 代理)。2026 為截至 4 月部分年資料,均由 2006 年底 1.00 起算。",
    },
    "tw": {
        "title": "PSP(景順上市 PE ETF)vs SPY -- 2007 至 2026 年 4 月",
        "subtitle": "最接近 PE 的零售代理 ETF 年化約 6%,SPY 約 9%。行銷簡報承諾的溢價,流向 GP,沒到 LP 等價份額。",
        "ylabel": "$1 成長(總報酬)",
        "xlabel": "年份",
        "lbl_psp": "PSP(景順上市 PE ETF)",
        "lbl_spy": "SPY(標普 500 ETF)",
        "annot_gfc": "金融海嘯:PSP -62%(2008)\n SPY -37%",
        "annot_2022": "2022:PSP -28%\n SPY -18%",
        "stat_box": "PSP 年化:{psp_cagr:.1f}%/年(~$1 -> US${psp_end:.2f})\nSPY 年化:{spy_cagr:.1f}%/年(~$1 -> US${spy_end:.2f})\n差距:-{gap:.1f} pp/年 -- 「流動性溢價」消失",
        "footer": "PSP TR 來源:景順公開說明書 / Morningstar(60 檔上市 PE 籃子,費率 1.44%)。SPY TR 來源:道富情況表(標普 500 TR 代理)。2026 為截至 4 月部分年資料。均自 2006 年底 1.00 起算。",
    },
    "cn": {
        "title": "PSP(景顺上市 PE ETF)vs SPY -- 2007 至 2026 年 4 月",
        "subtitle": "最接近 PE 的零售代理 ETF 年化约 6%,SPY 约 9%。营销简报承诺的溢价流向 GP,没到 LP 等价份额。",
        "ylabel": "$1 增长(总回报)",
        "xlabel": "年份",
        "lbl_psp": "PSP(景顺上市 PE ETF)",
        "lbl_spy": "SPY(标普 500 ETF)",
        "annot_gfc": "金融海啸:PSP -62%(2008)\n SPY -37%",
        "annot_2022": "2022:PSP -28%\n SPY -18%",
        "stat_box": "PSP 年化:{psp_cagr:.1f}%/年(~$1 -> US${psp_end:.2f})\nSPY 年化:{spy_cagr:.1f}%/年(~$1 -> US${spy_end:.2f})\n差距:-{gap:.1f} pp/年 -- 「流动性溢价」消失",
        "footer": "PSP TR 来源:景顺招股说明书 / Morningstar(60 只上市 PE 篮子,费率 1.44%)。SPY TR 来源:道富情况表(标普 500 TR 代理)。2026 为截至 4 月部分年资料。均自 2006 年底 1.00 起算。",
    },
}


def build_fig(s):
    P = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    xs, psp, spy, years = build_paths()

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax)

    ax.plot(xs, psp, color=P["red"], linewidth=2.6, label=s["lbl_psp"],
            zorder=5)
    ax.plot(xs, spy, color=P["blue"], linewidth=2.6, label=s["lbl_spy"],
            zorder=5)

    # Endpoint labels.
    ax.annotate(f"${psp[-1]:.2f}",
                xy=(xs[-1], psp[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=P["red"], fontweight="bold", fontsize=11,
                va="center")
    ax.annotate(f"${spy[-1]:.2f}",
                xy=(xs[-1], spy[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=P["blue"], fontweight="bold", fontsize=11,
                va="center")

    # GFC annotation.
    ax.annotate(s["annot_gfc"],
                xy=(pd.Timestamp("2008-12-31"), psp[2]),
                xytext=(pd.Timestamp("2010-06-30"), 0.20),
                fontsize=9.5, color=P["red"], ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=P["red"],
                                linewidth=1.0),
                bbox=dict(boxstyle="round,pad=0.4",
                          facecolor=P["bg"],
                          edgecolor=P["red"], linewidth=0.8))

    # 2022 annotation.
    ax.annotate(s["annot_2022"],
                xy=(pd.Timestamp("2022-12-31"), psp[16]),
                xytext=(pd.Timestamp("2018-06-30"), 4.6),
                fontsize=9.5, color=P["orange"], ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=P["orange"],
                                linewidth=1.0),
                bbox=dict(boxstyle="round,pad=0.4",
                          facecolor=P["bg"],
                          edgecolor=P["orange"], linewidth=0.8))

    # Stats box.
    psp_cagr = cagr(psp, xs[0], xs[-1]) * 100
    spy_cagr = cagr(spy, xs[0], xs[-1]) * 100
    box_text = s["stat_box"].format(psp_cagr=psp_cagr, psp_end=psp[-1],
                                    spy_cagr=spy_cagr, spy_end=spy[-1],
                                    gap=spy_cagr - psp_cagr)
    ax.text(0.02, 0.97, box_text, transform=ax.transAxes,
            ha="left", va="top", fontsize=10.0, color=P["fg"],
            bbox=dict(boxstyle="round,pad=0.55",
                      facecolor=P["bg"],
                      edgecolor=P["accent"], linewidth=1.2))

    ax.set_xlabel(s["xlabel"], fontsize=10.5)
    ax.set_ylabel(s["ylabel"], fontsize=10.5)
    ax.set_title(s["title"], pad=24, fontsize=14, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=P["muted"], style="italic")

    ax.legend(loc="lower right", frameon=True, fontsize=10,
              facecolor=P["bg"], edgecolor=P["grid"])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:.2f}"))
    ax.set_ylim(0, max(spy[-1], psp[-1]) * 1.18)
    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"wrote {BASE} for all locales -> {OUT_DIR}")
