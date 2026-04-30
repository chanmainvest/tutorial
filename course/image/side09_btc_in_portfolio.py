"""Side 09, sec 2.3 -- 60/40 vs 60/40 + 1/3/5% Bitcoin, Jan 2014 - Apr 2026.

$10,000 starting balance. Annual rebalance to target weights. SP500
proxy from Damodaran annual returns; bond proxy from Damodaran
TBond10Y. Bitcoin proxy from embedded annual returns built off the
side09_btc_history price anchors. The 2025 and 2026 rows are
projections (Damodaran ends at 2024) and are flagged in the footer.

Run:
    uv run python course/image/side09_btc_in_portfolio.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales, style_axes,
)
from scripts.market_data import damodaran_annual_returns  # noqa: E402

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side09_btc_in_portfolio"

# Embedded annual BTC USD returns (calendar year, decimal). Derived
# from end-of-year price anchors used in side09_btc_history.py.
BTC_ANNUAL = {
    2014: -0.585,
    2015:  0.365,
    2016:  1.230,
    2017: 13.580,
    2018: -0.740,
    2019:  0.950,
    2020:  3.030,
    2021:  0.600,
    2022: -0.640,
    2023:  1.550,
    2024:  1.215,
    2025:  0.420,   # ~$93k -> ~$132k EOY 2025
    2026: -0.152,   # YTD Apr: ~$132k -> ~$112k
}

# 2025 / 2026 SP500 + Bond projections (Damodaran ends 2024).
SPX_PROJ = {2025: 0.180, 2026: -0.020}    # 2026 = 4-month YTD
BND_PROJ = {2025: 0.050, 2026:  0.012}    # treas 10Y proxy

START_VAL = 10_000.0
W_STOCK_BASE = 0.60
W_BOND_BASE  = 0.40
BTC_WEIGHTS = [0.00, 0.01, 0.03, 0.05]

LANG_STRINGS = {
    "en": {
        "title":    "60/40 vs 60/40 + 1/3/5% Bitcoin, $10,000, Jan 2014 - Apr 2026",
        "subtitle": "Annual rebalance back to target. Small BTC sleeves add ~1-3 pp/yr CAGR; the cost is modestly deeper drawdowns. SOUL #14 (barbell).",
        "xlabel":   "Year",
        "ylabel":   "Cumulative wealth (USD)",
        "labels":   ["60/40 (no BTC)", "60/40 + 1% BTC",
                     "60/40 + 3% BTC", "60/40 + 5% BTC"],
        "footer":   "Stocks: Damodaran SP500 annual TR. Bonds: Damodaran 10Y Treasury. BTC: end-of-year price anchors. 2025-2026 = projection (Damodaran ends 2024). Annual rebalance.",
        "_lang":    "en",
    },
    "hk": {
        "title":    "60/40 vs 60/40 加 1/3/5% 比特幣,1 萬美元,2014 年 1 月 - 2026 年 4 月",
        "subtitle": "每年重新平衡至目標權重。細小 BTC 倉位每年加 1-3 個百分點複合回報;代價是回撤略深。SOUL #14(槓鈴)。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(美元)",
        "labels":   ["60/40(無 BTC)", "60/40 加 1% BTC",
                     "60/40 加 3% BTC", "60/40 加 5% BTC"],
        "footer":   "股票:Damodaran SP500 全回報。債券:Damodaran 10 年國債。BTC:年末價錨點。2025-2026 為預測(Damodaran 至 2024)。每年再平衡。",
        "_lang":    "hk",
    },
    "tw": {
        "title":    "60/40 vs 60/40 加 1/3/5% 比特幣,1 萬美元,2014 年 1 月 - 2026 年 4 月",
        "subtitle": "每年再平衡至目標權重。小幅 BTC 部位每年加 1-3 個百分點 CAGR;代價是回撤略深。SOUL #14(槓鈴)。",
        "xlabel":   "年份",
        "ylabel":   "累計財富(美元)",
        "labels":   ["60/40(無 BTC)", "60/40 加 1% BTC",
                     "60/40 加 3% BTC", "60/40 加 5% BTC"],
        "footer":   "股票:Damodaran SP500 全報酬。債券:Damodaran 10 年公債。BTC:年末價錨點。2025-2026 為預測(Damodaran 至 2024)。每年再平衡。",
        "_lang":    "tw",
    },
    "cn": {
        "title":    "60/40 vs 60/40 加 1/3/5% 比特币,1 万美元,2014 年 1 月 - 2026 年 4 月",
        "subtitle": "每年再平衡至目标权重。小幅 BTC 仓位每年加 1-3 个百分点 CAGR;代价是回撤略深。SOUL #14(杠铃)。",
        "xlabel":   "年份",
        "ylabel":   "累计财富(美元)",
        "labels":   ["60/40(无 BTC)", "60/40 加 1% BTC",
                     "60/40 加 3% BTC", "60/40 加 5% BTC"],
        "footer":   "股票:Damodaran SP500 总回报。债券:Damodaran 10 年国债。BTC:年末价锚点。2025-2026 为预测(Damodaran 至 2024)。每年再平衡。",
        "_lang":    "cn",
    },
}


def _annual_returns():
    """Return dict year -> (spx, bnd, btc) for 2014..2026."""
    dam = damodaran_annual_returns()
    out = {}
    for y in range(2014, 2027):
        if y in dam.index:
            spx = float(dam.loc[y, "SP500"])
            bnd = float(dam.loc[y, "TBond10Y"])
        else:
            spx = SPX_PROJ.get(y, 0.0)
            bnd = BND_PROJ.get(y, 0.0)
        btc = BTC_ANNUAL[y]
        out[y] = (spx, bnd, btc)
    return out


def _path(rets, w_btc):
    """Compute year-end wealth path with annual rebalance."""
    w_s = (1.0 - w_btc) * 0.6
    w_b = (1.0 - w_btc) * 0.4
    val = START_VAL
    path = [(2014, START_VAL)]
    for y, (spx, bnd, btc) in sorted(rets.items()):
        port_ret = w_s * spx + w_b * bnd + w_btc * btc
        val = val * (1.0 + port_ret)
        path.append((y + 1, val))   # year-end
    # Last entry is end of 2026 (= April 2026 for the partial year)
    return path


def build_fig(s):
    p = PALETTE_LIGHT
    rets = _annual_returns()
    paths = {w: _path(rets, w) for w in BTC_WEIGHTS}

    fig, ax = plt.subplots(figsize=(11.4, 6.2), dpi=150)
    style_axes(ax, p)

    colors = [p["grey"], p["blue"], p["accent"], p["red"]]

    for (w, color, label) in zip(BTC_WEIGHTS, colors, s["labels"]):
        path = paths[w]
        x = [pd.Timestamp(f"{yr}-01-01") if yr <= 2026
             else pd.Timestamp("2026-04-30") for yr, _ in path]
        # Last anchor is end-of-2026; treat as April 2026 for label
        x[-1] = pd.Timestamp("2026-04-30")
        y = [v for _, v in path]
        lw = 2.4 if w in (0.0, 0.05) else 1.8
        alpha = 1.0 if w in (0.0, 0.05) else 0.9
        ax.plot(x, y, color=color, linewidth=lw, alpha=alpha,
                label=label, zorder=4 if w == 0.05 else 3)
        # Endpoint label
        end = y[-1]
        ax.annotate(
            f"\\${end:,.0f}",
            xy=(x[-1], end),
            xytext=(8, 0),
            textcoords="offset points",
            ha="left", va="center",
            color=color,
            fontsize=9.0,
            fontweight="bold",
        )

    ax.set_xlabel(s["xlabel"])
    ax.set_ylabel(s["ylabel"])
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.set_title(s["title"], fontsize=13.2, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"])
    ax.text(0, -0.13, s["footer"], transform=ax.transAxes,
            fontsize=8.0, color=p["muted"])

    fig.tight_layout(rect=[0, 0.02, 0.94, 0.96])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Saved {BASE}*.png to {OUT_DIR}")
