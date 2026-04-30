"""Week 38, §2.3 - Poor man's covered call (PMCC) payoff at short-call expiry.

Long leg: a 24-month LEAPS call at K=80 priced at $25 (per share).
Short leg: a 30-day call at K=110 sold at $1.50 (per share).
Net debit: $23.50.

At the short call's expiration we mark the LEAPS using BSM with
T=(730-30)/365 days remaining, sigma=22%, r=4%. The short call is at
its terminal payoff: max(S - 110, 0). Net P&L = LEAPS_value(S, T_rem)
- max(S - 110, 0) - 23.50. We highlight max profit at S=110 and max
loss = -23.50 (LEAPS goes near zero on a deep collapse).

Run:
    uv run python course/image/week38_pmcc_payoff.py
"""

from __future__ import annotations

import math
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
BASE = "week38_pmcc_payoff"


def _Phi(x):
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2.0)))


def bsm_call_price(S, K, T, sigma, r, q=0.0):
    sqrtT = np.sqrt(T)
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    return S * np.exp(-q * T) * _Phi(d1) - K * np.exp(-r * T) * _Phi(d2)


# Position parameters.
LEAPS_K = 80.0
LEAPS_DTE_INIT = 730       # days at trade entry
LEAPS_PREM_PAID = 25.0     # paid up-front per share
SHORT_K = 110.0
SHORT_DTE = 30
SHORT_PREM_RECV = 1.50
SIGMA = 0.22
RFREE = 0.04
NET_DEBIT = LEAPS_PREM_PAID - SHORT_PREM_RECV  # 23.50


def compute_payoff():
    S = np.linspace(50.0, 140.0, 451)
    T_rem = (LEAPS_DTE_INIT - SHORT_DTE) / 365.0
    leaps_val = bsm_call_price(S, LEAPS_K, T_rem, SIGMA, RFREE)
    short_payoff = np.maximum(S - SHORT_K, 0.0)
    pnl = leaps_val - short_payoff - NET_DEBIT
    return S, leaps_val, short_payoff, pnl


LANG_STRINGS = {
    "en": {
        "title": "Poor man's covered call - net P&L at short-call expiry",
        "subtitle": "Long Jan-2028 \\$80 LEAPS @ \\$25 + short 30-day \\$110 call @ \\$1.50. Net debit \\$23.50/share, \\$2,350/contract. Underlying \\$100, sigma=22%, r=4%.",
        "xlabel": "Underlying price at short-call expiry (\\$)",
        "ylabel": "Net P&L per share (\\$)",
        "footer": "Same risk profile as a covered call, ~25% of the capital. Roll the short leg every 30 days; roll the LEAPS at 90 DTE remaining.",
        "leaps_lbl": "Long LEAPS value (700 DTE remaining)",
        "short_lbl": "Short call payoff (terminal)",
        "pnl_lbl": "Net P&L (LEAPS - short - debit)",
        "max_profit": "Max profit ~\\${pp:.2f}/share at S=\\$110",
        "max_loss": "Max loss = -\\${nd:.2f} (net debit)",
        "be_lbl": "Breakeven ~\\${be:.2f}",
        "below_band": "LEAPS retreats - mark-to-market loss",
        "between_band": "Sweet spot - LEAPS gains, short decays",
        "above_band": "Short call caps upside above \\$110",
    },
    "hk": {
        "title": "窮人版備兌認購 - 短期認購到期日的淨損益",
        "subtitle": "買入 2028 年 1 月、80 美元 LEAPS @25 美元 + 賣出 30 日、110 美元認購 @1.5 美元。淨支出 23.5 美元/股,2,350 美元/合約。標的 100 美元、sigma=22%、r=4%。",
        "xlabel": "短期認購到期時標的價格(美元)",
        "ylabel": "每股淨損益(美元)",
        "footer": "與備兌認購相同的風險,僅約 25% 資金。短腿每 30 天滾動;LEAPS 於剩餘 90 DTE 滾動。",
        "leaps_lbl": "持有 LEAPS 價值(尚餘 700 DTE)",
        "short_lbl": "短期認購到期內在值",
        "pnl_lbl": "淨損益(LEAPS - 短腿 - 淨支出)",
        "max_profit": "最大利潤 約 {pp:.2f} 美元/股,在 S=110 美元",
        "max_loss": "最大虧損 = -{nd:.2f} 美元(淨支出)",
        "be_lbl": "盈虧平衡 約 {be:.2f} 美元",
        "below_band": "LEAPS 回落 - 帳面虧損",
        "between_band": "甜蜜區 - LEAPS 上漲、短腿衰減",
        "above_band": "短腿封頂 110 美元以上的上行",
    },
    "tw": {
        "title": "窮人版掩護性買權 - 短期買權到期日的淨損益",
        "subtitle": "買進 2028 年 1 月、80 美元 LEAPS @25 美元 + 賣出 30 日、110 美元買權 @1.5 美元。淨支出 23.5 美元/股,2,350 美元/口。標的 100 美元、sigma=22%、r=4%。",
        "xlabel": "短期買權到期時標的價(美元)",
        "ylabel": "每股淨損益(美元)",
        "footer": "與掩護性買權相同的風險,僅約 25% 資金。短腿每 30 天轉倉;LEAPS 於剩餘 90 DTE 轉倉。",
        "leaps_lbl": "持有 LEAPS 價值(尚餘 700 DTE)",
        "short_lbl": "短期買權到期內在值",
        "pnl_lbl": "淨損益(LEAPS - 短腿 - 淨支出)",
        "max_profit": "最大獲利 約 {pp:.2f} 美元/股,於 S=110 美元",
        "max_loss": "最大虧損 = -{nd:.2f} 美元(淨支出)",
        "be_lbl": "損益平衡 約 {be:.2f} 美元",
        "below_band": "LEAPS 回落 - 帳面虧損",
        "between_band": "甜蜜區 - LEAPS 上行、短腿衰減",
        "above_band": "短腿封頂 110 美元以上的上行",
    },
    "cn": {
        "title": "穷人版备兑看涨 - 短期看涨到期时的净盈亏",
        "subtitle": "买入 2028 年 1 月、80 美元 LEAPS @25 美元 + 卖出 30 日、110 美元看涨 @1.5 美元。净支出 23.5 美元/股,2,350 美元/合约。标的 100 美元、sigma=22%、r=4%。",
        "xlabel": "短期看涨到期时标的价格(美元)",
        "ylabel": "每股净盈亏(美元)",
        "footer": "与备兑看涨相同的风险,仅约 25% 资金。短腿每 30 天滚动;LEAPS 在剩余 90 DTE 滚动。",
        "leaps_lbl": "持有 LEAPS 价值(剩余 700 DTE)",
        "short_lbl": "短期看涨到期内在值",
        "pnl_lbl": "净盈亏(LEAPS - 短腿 - 净支出)",
        "max_profit": "最大利润 约 {pp:.2f} 美元/股,在 S=110 美元",
        "max_loss": "最大亏损 = -{nd:.2f} 美元(净支出)",
        "be_lbl": "盈亏平衡 约 {be:.2f} 美元",
        "below_band": "LEAPS 回落 - 账面亏损",
        "between_band": "甜蜜区 - LEAPS 上行、短腿衰减",
        "above_band": "短腿封顶 110 美元以上的上行",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    S, leaps_val, short_payoff, pnl = compute_payoff()

    # Find max profit S* (numerical), breakeven (where pnl crosses 0).
    i_peak = int(np.argmax(pnl))
    s_peak = S[i_peak]
    pnl_peak = pnl[i_peak]
    # breakeven: leftmost S where pnl >= 0.
    sign = np.sign(pnl)
    cross = np.where(np.diff(sign) > 0)[0]
    be = S[cross[0]] if len(cross) else float("nan")

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax, p)

    # Region shading.
    ax.axvspan(50, LEAPS_K, color=p["red"], alpha=0.06, zorder=0)
    ax.axvspan(LEAPS_K, SHORT_K, color=p["green"], alpha=0.07, zorder=0)
    ax.axvspan(SHORT_K, 140, color=p["accent"], alpha=0.07, zorder=0)

    ax.text(65, -19, s["below_band"], fontsize=8.8, color=p["red"],
            fontweight="bold", ha="center")
    ax.text(95, -19, s["between_band"], fontsize=8.8, color=p["green"],
            fontweight="bold", ha="center")
    ax.text(125, -19, s["above_band"], fontsize=8.8, color=p["accent"],
            fontweight="bold", ha="center")

    # Reference lines.
    ax.plot(S, leaps_val - LEAPS_PREM_PAID, color=p["green"], linewidth=1.4,
            linestyle="--", alpha=0.7, label=s["leaps_lbl"])
    ax.plot(S, -short_payoff + SHORT_PREM_RECV, color=p["red"], linewidth=1.4,
            linestyle="--", alpha=0.7, label=s["short_lbl"])
    # Combined P&L.
    ax.plot(S, pnl, color=p["blue"], linewidth=2.6, label=s["pnl_lbl"])
    ax.fill_between(S, pnl, 0, where=(pnl >= 0), color=p["green"], alpha=0.16)
    ax.fill_between(S, pnl, 0, where=(pnl < 0), color=p["red"], alpha=0.12)

    # Zero line.
    ax.axhline(0, color=p["muted"], linewidth=0.8, alpha=0.7)

    # Strike markers.
    for k, lab in [(LEAPS_K, "LEAPS K=\\$80"), (SHORT_K, "Short K=\\$110")]:
        ax.axvline(k, color=p["muted"], linestyle=":", linewidth=0.9, alpha=0.6)
        ax.text(k, 14.5, lab, ha="center", fontsize=9, color=p["muted"])

    # Max profit marker.
    ax.plot(s_peak, pnl_peak, "o", color=p["green"], markersize=9, zorder=6)
    ax.annotate(
        s["max_profit"].format(pp=pnl_peak),
        xy=(s_peak, pnl_peak), xytext=(-180, 30), textcoords="offset points",
        fontsize=10, color=p["green"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["green"], lw=1.0),
    )

    # Max loss marker (left edge).
    ax.plot(S[0], pnl[0], "o", color=p["red"], markersize=9, zorder=6)
    ax.annotate(
        s["max_loss"].format(nd=NET_DEBIT),
        xy=(S[0], pnl[0]), xytext=(20, 25), textcoords="offset points",
        fontsize=10, color=p["red"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["red"], lw=1.0),
    )

    # Breakeven marker.
    if not np.isnan(be):
        ax.plot(be, 0, "o", color=p["accent"], markersize=8, zorder=6)
        ax.annotate(
            s["be_lbl"].format(be=be),
            xy=(be, 0), xytext=(-50, -45), textcoords="offset points",
            fontsize=9.5, color=p["accent"], fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=p["accent"], lw=0.9),
        )

    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_xlim(50, 140)
    ax.set_ylim(-26, 18)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"\\${v:.0f}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"\\${v:.0f}"))

    ax.set_title(s["title"], pad=24, fontsize=15, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.2, color=p["muted"], style="italic")

    ax.legend(loc="lower right", framealpha=0.92, fontsize=9.3)
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print("Wrote:")
    for q in paths:
        print(" ", q)
