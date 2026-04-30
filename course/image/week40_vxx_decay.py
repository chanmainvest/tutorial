"""Week 40, sec 2.2 — Cumulative return $1 in VXX vs SPY since Jan 2009.

VXX has lost ~99.99% of its value since 2009 inception, after eight
reverse splits, total-return adjusted. Log scale required to see the
decay. SPY shown for reference. Constructed from embedded annual return
prints derived from the actual VXX/VXX-B series and Damodaran SP500
totals.

Run:
    uv run python course/image/week40_vxx_decay.py
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
BASE = "week40_vxx_decay"


# Annual total returns. VXX series spliced (original VXX 2009-2017,
# VXX series-B 2018-2026 YTD), reverse-split adjusted from public data.
# SPY total returns from Damodaran SP500 row + 2025 estimate + 2026 YTD.
# 2009 is partial (Jan 30 - Dec 31).
ANNUAL = [
    # (year, vxx_ret, spy_ret)
    (2009, -0.560,  0.265),   # VXX inception 2009-01-30
    (2010, -0.715,  0.151),
    (2011, -0.034,  0.021),
    (2012, -0.781,  0.160),
    (2013, -0.654,  0.323),
    (2014, -0.270,  0.137),
    (2015, -0.357,  0.014),
    (2016, -0.682,  0.120),
    (2017, -0.730,  0.218),
    (2018, -0.493, -0.044),
    (2019, -0.453,  0.314),
    (2020,  0.110,  0.184),   # COVID year, rare positive
    (2021, -0.708,  0.287),
    (2022, -0.118, -0.181),
    (2023, -0.450,  0.263),
    (2024, -0.490,  0.250),
    (2025, -0.555,  0.120),
    (2026, -0.150,  0.045),   # YTD through April
]


def _series():
    yrs = [r[0] for r in ANNUAL]
    vxx_r = np.array([r[1] for r in ANNUAL])
    spy_r = np.array([r[2] for r in ANNUAL])
    cum_v = np.cumprod(1.0 + vxx_r)
    cum_s = np.cumprod(1.0 + spy_r)
    # Anchor end-of-year dates for x-axis.
    dates = pd.to_datetime([f"{y}-12-31" if y < 2026 else "2026-04-30"
                            for y in yrs])
    # Prepend $1 starting point (Jan-30-2009).
    dates = pd.DatetimeIndex(["2009-01-30"]).append(dates)
    cum_v = np.concatenate([[1.0], cum_v])
    cum_s = np.concatenate([[1.0], cum_s])
    return dates, cum_v, cum_s


LANG_STRINGS = {
    "en": {
        "title":    "$1 in VXX vs $1 in SPY since Jan 2009 inception (log scale)",
        "subtitle": "VXX is a constant-maturity 30-day VIX-futures product. Contango roll cost compounds to ~99.99% loss across 17 years.",
        "xlabel":   "Year",
        "ylabel":   "Wealth ($, log scale)",
        "vxx":      "VXX (long 1x VIX futures)",
        "spy":      "SPY (S&P 500 ETF)",
        "vxx_end":  "VXX end value",
        "spy_end":  "SPY end value",
        "footer":   "Eight reverse splits required to keep share price > $1. Source: VXX/VXX-B + Damodaran SP500 totals.",
    },
    "hk": {
        "title":    "VXX 與 SPY 自 2009 年 1 月起 1 美元的累計表現(對數軸)",
        "subtitle": "VXX 為持續維持 30 日到期的 VIX 期貨產品。Contango 滾倉成本累計 17 年虧損約 99.99%。",
        "xlabel":   "年份",
        "ylabel":   "財富(美元,對數軸)",
        "vxx":      "VXX(1x 多 VIX 期貨)",
        "spy":      "SPY(標普 500 ETF)",
        "vxx_end":  "VXX 期末值",
        "spy_end":  "SPY 期末值",
        "footer":   "已進行 8 次合股以維持股價 > 1 美元。資料來源:VXX/VXX-B + Damodaran SP500 全收益。",
    },
    "tw": {
        "title":    "VXX 與 SPY 自 2009 年 1 月起 1 美元的累計表現(對數軸)",
        "subtitle": "VXX 為持續維持 30 日到期的 VIX 期貨商品。Contango 換倉成本累計 17 年虧損約 99.99%。",
        "xlabel":   "年份",
        "ylabel":   "財富(美元,對數軸)",
        "vxx":      "VXX(1x 多 VIX 期貨)",
        "spy":      "SPY(標普 500 ETF)",
        "vxx_end":  "VXX 期末值",
        "spy_end":  "SPY 期末值",
        "footer":   "已進行 8 次反向分割以維持股價 > 1 美元。資料來源:VXX/VXX-B + Damodaran SP500 總報酬。",
    },
    "cn": {
        "title":    "VXX 与 SPY 自 2009 年 1 月起 1 美元的累计表现(对数轴)",
        "subtitle": "VXX 是持续维持 30 日到期的 VIX 期货产品。Contango 滚仓成本累计 17 年亏损约 99.99%。",
        "xlabel":   "年份",
        "ylabel":   "财富(美元,对数轴)",
        "vxx":      "VXX(1x 多 VIX 期货)",
        "spy":      "SPY(标普 500 ETF)",
        "vxx_end":  "VXX 期末值",
        "spy_end":  "SPY 期末值",
        "footer":   "已进行 8 次合股以维持股价 > 1 美元。数据来源:VXX/VXX-B + Damodaran SP500 全收益。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    dates, cv, cs = _series()

    fig, ax = plt.subplots(figsize=(11.4, 6.2), dpi=150)
    style_axes(ax, p)

    ax.plot(dates, cs, color=p["blue"], linewidth=2.4, label=s["spy"])
    ax.plot(dates, cv, color=p["red"], linewidth=2.4, label=s["vxx"])
    ax.fill_between(dates, cv, 1e-7, color=p["red"], alpha=0.07)

    ax.set_yscale("log")
    ax.set_ylim(1e-6, 20)

    # End annotations.
    end_v = cv[-1]
    end_s = cs[-1]
    ax.plot([dates[-1]], [end_v], "o", color=p["red"], markersize=7, zorder=5)
    ax.plot([dates[-1]], [end_s], "o", color=p["blue"], markersize=7, zorder=5)
    ax.annotate(
        s["vxx_end"] + f"\n${end_v:.6f}\n({(end_v - 1) * 100:.2f}%)",
        xy=(dates[-1], end_v),
        xytext=(-110, 22),
        textcoords="offset points",
        fontsize=9, color=p["red"], fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=p["red"], alpha=0.6, linewidth=0.7),
    )
    ax.annotate(
        s["spy_end"] + f"\n${end_s:,.2f}\n(+{(end_s - 1) * 100:.0f}%)",
        xy=(dates[-1], end_s),
        xytext=(-90, -38),
        textcoords="offset points",
        fontsize=9, color=p["blue"], fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=p["blue"], alpha=0.6, linewidth=0.7),
    )

    # 1.0 reference line.
    ax.axhline(1.0, color=p["muted"], linewidth=0.9, linestyle="--", alpha=0.6)

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.set_title(s["title"], fontsize=13.5, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"])
    ax.legend(loc="lower left", frameon=False, fontsize=10)

    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
