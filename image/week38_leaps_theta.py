"""Week 38, §2.2 - Daily theta vs DTE for 5 delta bands.

For each target delta in {0.10, 0.30, 0.50, 0.70, 0.90} we sweep DTE from
30 to 1095 days. At each DTE we solve for the strike that yields the
target delta on a $100 stock with sigma=22%, r=4%, q=0%, then evaluate
the Black-Scholes daily theta. The plot illustrates the 1/sqrt(T)
scaling: a 730-DTE option has roughly one-fifth the per-day dollar theta
of a 30-DTE option at the same delta.

Run:
    uv run python course/image/week38_leaps_theta.py
"""

from __future__ import annotations

import math
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
BASE = "week38_leaps_theta"

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _phi(x):
    return math.exp(-0.5 * x * x) / SQRT_2PI


def bsm_call_delta(S, K, T, sigma, r, q=0.0):
    sqrtT = math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    return math.exp(-q * T) * _Phi(d1)


def bsm_call_theta_per_day(S, K, T, sigma, r, q=0.0):
    sqrtT = math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    theta_year = (
        -S * math.exp(-q * T) * _phi(d1) * sigma / (2.0 * sqrtT)
        - r * K * math.exp(-r * T) * _Phi(d2)
        + q * S * math.exp(-q * T) * _Phi(d1)
    )
    return theta_year / 365.0


def strike_for_delta(target_delta, S, T, sigma, r, q=0.0):
    """Bisection: find K such that BSM call delta equals target_delta."""
    # Higher K -> lower delta. Bracket K in [0.01*S, 5*S].
    lo, hi = 0.01 * S, 5.0 * S
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        d = bsm_call_delta(S, mid, T, sigma, r, q)
        if d > target_delta:
            lo = mid  # need smaller delta -> larger K
        else:
            hi = mid
        if hi - lo < 1e-6:
            break
    return 0.5 * (lo + hi)


# Anchors.
S = 100.0
SIGMA = 0.22
RFREE = 0.04


def compute_curves():
    deltas = [0.90, 0.70, 0.50, 0.30, 0.10]
    dtes = np.arange(30, 1096, 5)  # 30..1095 days
    out = {}
    for d in deltas:
        thetas = []
        for dte in dtes:
            T = dte / 365.0
            K = strike_for_delta(d, S, T, SIGMA, RFREE)
            th = bsm_call_theta_per_day(S, K, T, SIGMA, RFREE)
            thetas.append(-th)  # absolute (positive) theta cost per day
        out[d] = (dtes, np.array(thetas))
    return out


LANG_STRINGS = {
    "en": {
        "title": "Daily theta scales as 1 / sqrt(T) - cheap leverage at long DTE",
        "subtitle": "Black-Scholes call theta on \\$100 stock, sigma=22%, r=4%. At each DTE, strike is the one that yields the labeled delta. A 730-DTE option has ~5x less daily dollar theta than a 30-DTE option at the same delta.",
        "xlabel": "Days to expiration (DTE)",
        "ylabel": "|Theta| per day (\\$ per share)",
        "footer": "LEAPS land starts at DTE > 365. The 0.90D 730-DTE point is the canonical stock-replacement carry: roughly half a cent per day per share on \\$100 of underlying notional.",
        "leaps_band": "LEAPS zone (DTE > 1 year)",
        "lbl_90": "0.90D (deep ITM)",
        "lbl_70": "0.70D (ITM)",
        "lbl_50": "0.50D (ATM)",
        "lbl_30": "0.30D (OTM)",
        "lbl_10": "0.10D (far OTM)",
    },
    "hk": {
        "title": "每日 theta 按 1 / sqrt(T) 縮放 - 長 DTE 是廉價槓桿",
        "subtitle": "Black-Scholes 認購 theta:股價 100 美元、sigma=22%、r=4%。每個 DTE 取對應目標 delta 的行使價。730 DTE 的每日美元 theta 約為 30 DTE 的五分之一(同 delta)。",
        "xlabel": "距到期日(DTE)",
        "ylabel": "每日 |Theta|(每股美元)",
        "footer": "LEAPS 區從 DTE > 365 開始。0.90D、730 DTE 點正是股票替代策略的成本:每天每股約半美分,對應 100 美元名義敞口。",
        "leaps_band": "LEAPS 區(DTE > 1 年)",
        "lbl_90": "0.90D(深度價內)",
        "lbl_70": "0.70D(價內)",
        "lbl_50": "0.50D(價平)",
        "lbl_30": "0.30D(價外)",
        "lbl_10": "0.10D(深度價外)",
    },
    "tw": {
        "title": "每日 theta 以 1 / sqrt(T) 縮放 - 長 DTE 即廉價槓桿",
        "subtitle": "Black-Scholes 買權 theta:股價 100 美元、sigma=22%、r=4%。每個 DTE 取對應目標 delta 的履約價。730 DTE 每日美元 theta 約為 30 DTE 的五分之一(同 delta)。",
        "xlabel": "距到期日(DTE)",
        "ylabel": "每日 |Theta|(每股美元)",
        "footer": "LEAPS 區由 DTE > 365 起。0.90D、730 DTE 點即股票替代策略的成本:每日每股約半美分,對應 100 美元名義部位。",
        "leaps_band": "LEAPS 區(DTE > 1 年)",
        "lbl_90": "0.90D(深價內)",
        "lbl_70": "0.70D(價內)",
        "lbl_50": "0.50D(價平)",
        "lbl_30": "0.30D(價外)",
        "lbl_10": "0.10D(深價外)",
    },
    "cn": {
        "title": "每日 theta 按 1 / sqrt(T) 缩放 - 长 DTE 即廉价杠杆",
        "subtitle": "Black-Scholes 看涨 theta:股价 100 美元、sigma=22%、r=4%。各 DTE 取符合目标 delta 的行权价。730 DTE 每日美元 theta 约为 30 DTE 的五分之一(同 delta)。",
        "xlabel": "距到期日(DTE)",
        "ylabel": "每日 |Theta|(每股美元)",
        "footer": "LEAPS 区由 DTE > 365 起。0.90D、730 DTE 点即股票替代的成本:每天每股约半美分,对应 100 美元名义敞口。",
        "leaps_band": "LEAPS 区(DTE > 1 年)",
        "lbl_90": "0.90D(深度价内)",
        "lbl_70": "0.70D(价内)",
        "lbl_50": "0.50D(价平)",
        "lbl_30": "0.30D(价外)",
        "lbl_10": "0.10D(深度价外)",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    curves = compute_curves()

    fig, ax = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax, p)

    color_map = {
        0.90: p["green"],
        0.70: p["teal"],
        0.50: p["blue"],
        0.30: p["accent"],
        0.10: p["red"],
    }
    label_map = {
        0.90: s["lbl_90"], 0.70: s["lbl_70"], 0.50: s["lbl_50"],
        0.30: s["lbl_30"], 0.10: s["lbl_10"],
    }

    # Shade LEAPS zone (DTE > 365).
    ax.axvspan(365, 1095, color=p["accent"], alpha=0.07, zorder=0)
    ax.text(
        720, 0.205, s["leaps_band"], ha="center", va="top",
        fontsize=10, color=p["accent"], fontweight="bold",
    )

    for d in [0.90, 0.70, 0.50, 0.30, 0.10]:
        x, y = curves[d]
        ax.plot(x, y, color=color_map[d], linewidth=2.2, label=label_map[d])

    # Annotate ratio markers at DTE=30 and DTE=730 for ATM line.
    x50, y50 = curves[0.50]
    i30 = int(np.where(x50 == 30)[0][0])
    i730 = int(np.where(x50 == 730)[0][0])
    ax.plot([30, 730], [y50[i30], y50[i730]], "o", color=p["blue"],
            markersize=7, zorder=5)
    ax.annotate(
        f"30 DTE: \\${y50[i30]:.3f}/day",
        xy=(30, y50[i30]), xytext=(40, 30), textcoords="offset points",
        fontsize=9.5, color=p["blue"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["blue"], lw=0.9),
    )
    ax.annotate(
        f"730 DTE: \\${y50[i730]:.3f}/day  (~{y50[i30]/y50[i730]:.1f}x cheaper)",
        xy=(730, y50[i730]), xytext=(-50, 35), textcoords="offset points",
        fontsize=9.5, color=p["blue"], fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=p["blue"], lw=0.9),
    )

    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])
    ax.set_xlim(0, 1100)
    ax.set_ylim(0, 0.22)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"\\${v:.2f}"))

    ax.set_title(s["title"], pad=24, fontsize=15, fontweight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.2, color=p["muted"], style="italic")

    ax.legend(loc="upper right", framealpha=0.92, fontsize=9.5)
    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print("Wrote:")
    for q in paths:
        print(" ", q)
