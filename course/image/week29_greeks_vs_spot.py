"""Week 29, §2.5 — The four primary Greeks plotted vs spot.

Black-Scholes closed-form delta, gamma, theta (per day), and vega (per 1
vol-point) for a 30-day, K=100, sigma=20%, r=4% European call across
spot 60..140. Shows the personalities: delta is a smooth S-curve
between 0 and 1, gamma is a bell centred at the strike, theta is most
negative at-the-money, vega has the same bell shape as gamma but in
units of dollars-per-vol-point.

Run:
    uv run python course/image/week29_greeks_vs_spot.py
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
BASE = "week29_greeks_vs_spot"


# ---- Black-Scholes ---------------------------------------------------
SQRT_2PI = math.sqrt(2.0 * math.pi)


def _phi(x):
    return np.exp(-0.5 * x * x) / SQRT_2PI


def _Phi(x):
    # Vectorised standard-normal CDF via erf.
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2.0)))


def bsm_greeks(S, K, T, sigma, r, kind="call"):
    sqrtT = math.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    pdf1 = _phi(d1)
    if kind == "call":
        delta = _Phi(d1)
        theta_year = (-S * pdf1 * sigma / (2.0 * sqrtT)
                      - r * K * np.exp(-r * T) * _Phi(d2))
    else:
        delta = _Phi(d1) - 1.0
        theta_year = (-S * pdf1 * sigma / (2.0 * sqrtT)
                      + r * K * np.exp(-r * T) * _Phi(-d2))
    gamma = pdf1 / (S * sigma * sqrtT)
    vega = S * pdf1 * sqrtT / 100.0     # per 1 vol-point
    theta = theta_year / 365.0          # per calendar day
    return delta, gamma, theta, vega


# ---- Strings ---------------------------------------------------------
LANG_STRINGS = {
    "en": {
        "title":    "The four primary Greeks vs spot - 30-day, K=$100, sigma=20%, r=4% call",
        "subtitle": "Closed-form Black-Scholes. Delta is the slope of the premium curve, gamma its curvature, theta the daily time-decay, vega the sensitivity to a one-point move in implied vol.",
        "delta_t":  "Delta (probability-of-finishing-ITM proxy)",
        "gamma_t":  "Gamma (acceleration of delta)",
        "theta_t":  "Theta per day (time-decay, ATM is worst)",
        "vega_t":   "Vega per 1 vol-pt (peaks at-the-money)",
        "xlabel":   "Spot price ($)",
        "atm":      "ATM (S=K)",
        "footer":   "All four Greeks are mirror-images either side of the strike. Gamma and vega are bell curves; theta is a negative bell; delta is the integral of gamma.",
    },
    "hk": {
        "title":    "四大主要 Greek 對現價 - 30 日,K=100 美元,sigma=20%,r=4% 認購",
        "subtitle": "Black-Scholes 封閉解。Delta 是權利金曲線的斜率,Gamma 是曲率,Theta 是每日時間衰減,Vega 對應隱含波幅變動 1 點的敏感度。",
        "delta_t":  "Delta(到期 ITM 機率近似)",
        "gamma_t":  "Gamma(Delta 的加速度)",
        "theta_t":  "每日 Theta(時間衰減,ATM 最差)",
        "vega_t":   "每 1 vol 點的 Vega(在價內價外間最大)",
        "xlabel":   "現價(美元)",
        "atm":      "ATM(S=K)",
        "footer":   "四個 Greek 在執行價兩側互為鏡像。Gamma 與 Vega 是鐘形;Theta 是負鐘形;Delta 是 Gamma 的積分。",
    },
    "tw": {
        "title":    "四大主要 Greek 對現價 - 30 日,K=100 美元,sigma=20%,r=4% 買權",
        "subtitle": "Black-Scholes 封閉解。Delta 是權利金曲線的斜率,Gamma 是曲率,Theta 是每日時間衰減,Vega 對應隱含波動率變動 1 點的敏感度。",
        "delta_t":  "Delta(到期 ITM 機率近似)",
        "gamma_t":  "Gamma(Delta 的加速度)",
        "theta_t":  "每日 Theta(時間衰減,ATM 最差)",
        "vega_t":   "每 1 vol 點的 Vega(履約價附近最大)",
        "xlabel":   "現價(美元)",
        "atm":      "ATM(S=K)",
        "footer":   "四個 Greek 在履約價兩側為鏡像對稱。Gamma 與 Vega 為鐘形;Theta 為負鐘形;Delta 為 Gamma 的積分。",
    },
    "cn": {
        "title":    "四大主要 Greek 对现价 - 30 日,K=100 美元,sigma=20%,r=4% 看涨",
        "subtitle": "Black-Scholes 闭式解。Delta 是权利金曲线的斜率,Gamma 是曲率,Theta 是每日时间衰减,Vega 对应隐含波动率变动 1 点的敏感度。",
        "delta_t":  "Delta(到期 ITM 概率近似)",
        "gamma_t":  "Gamma(Delta 的加速度)",
        "theta_t":  "每日 Theta(时间衰减,ATM 最严重)",
        "vega_t":   "每 1 vol 点的 Vega(行权价附近最大)",
        "xlabel":   "现价(美元)",
        "atm":      "ATM(S=K)",
        "footer":   "四个 Greek 在行权价两侧呈镜像对称。Gamma 与 Vega 为钟形;Theta 为负钟形;Delta 是 Gamma 的积分。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT

    K = 100.0
    T = 30.0 / 365.0
    sigma = 0.20
    r = 0.04
    S = np.linspace(60.0, 140.0, 401)

    delta, gamma, theta, vega = bsm_greeks(S, K, T, sigma, r, "call")

    fig, axs = plt.subplots(2, 2, figsize=(12.4, 7.6))
    for ax in axs.flat:
        style_axes(ax, p)

    panels = [
        (axs[0, 0], delta, s["delta_t"], p["blue"],   None,    "{:.2f}"),
        (axs[0, 1], gamma, s["gamma_t"], p["accent"], None,    "{:.3f}"),
        (axs[1, 0], theta, s["theta_t"], p["red"],    None,    "{:.3f}"),
        (axs[1, 1], vega,  s["vega_t"],  p["green"],  None,    "{:.3f}"),
    ]

    for ax, y, title, color, _, fmt in panels:
        ax.plot(S, y, color=color, linewidth=2.4)
        ax.fill_between(S, y, color=color, alpha=0.10)
        ax.axvline(K, color=p["muted"], linewidth=0.9,
                   linestyle="--", alpha=0.7)
        ax.set_title(title, fontsize=11.3, fontweight="bold",
                     color=p["fg"], loc="left", pad=6)
        ax.set_xlabel(s["xlabel"], fontsize=9.5, color=p["muted"])
        ax.set_xlim(60, 140)

        # Mark ATM value.
        idx_atm = int(np.argmin(np.abs(S - K)))
        ax.plot(K, y[idx_atm], "o", color=color, markersize=6, zorder=5)
        ax.annotate(s["atm"] + " " + fmt.format(y[idx_atm]),
                    xy=(K, y[idx_atm]),
                    xytext=(8, 8 if y[idx_atm] >= 0 else -16),
                    textcoords="offset points",
                    fontsize=9, color=color, fontweight="bold")

    # Y-axis bands per panel (let matplotlib auto-fit but pad).
    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 color=p["fg"], x=0.02, ha="left", y=0.985)
    fig.text(0.02, 0.945, s["subtitle"], fontsize=10,
             color=p["muted"])
    fig.text(0.02, 0.01, s["footer"], fontsize=9.2,
             color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.03, 1, 0.93])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
