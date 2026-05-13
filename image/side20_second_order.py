"""Side 20, §2.2-2.5 - Second-order Greeks (vanna, charm, color, volga).

4-panel chart showing vanna, charm, color, and volga as functions of
spot for a 30-day, K=100, sigma=20%, r=4% European call. All values
computed via Black-Scholes closed forms; per-day for charm/color, per
1 vol-pt for vanna/volga.

Run:
    uv run python course/image/side20_second_order.py
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
BASE = "side20_second_order"


SQRT_2PI = math.sqrt(2.0 * math.pi)


def _phi(x):
    return np.exp(-0.5 * x * x) / SQRT_2PI


def _Phi(x):
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2.0)))


def second_order_greeks(S, K, T, sigma, r):
    """Return (vanna, charm_per_day, color_per_day, volga) for a call.

    - vanna   = dDelta/dSigma per 1 vol-pt    (divide raw by 100)
    - charm   = dDelta/dt    per calendar day (divide year-rate by 365)
    - color   = dGamma/dt    per calendar day (divide year-rate by 365)
    - volga   = dVega/dSigma per 1 vol-pt     (raw vega already per 100)
    """
    sqrtT = math.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    pdf1 = _phi(d1)

    # Vanna: -phi(d1) * d2 / sigma -- the result is dDelta per unit sigma
    # change. Divide by 100 to express as "per 1 vol-pt".
    vanna = -pdf1 * d2 / sigma / 100.0

    # Charm (call, no dividend): d(Delta)/dt = -d(Delta)/dT.
    # dDelta/dT = phi(d1) * (2*r*T - d2 * sigma * sqrt(T)) / (2 * T * sigma * sqrt(T))
    charm_year = -pdf1 * (2.0 * r * T - d2 * sigma * sqrtT) / (2.0 * T * sigma * sqrtT)
    charm = charm_year / 365.0

    # Color: d(Gamma)/dt = -d(Gamma)/dT.
    # dGamma/dT = -gamma * (1/(2T) + (r*d1)/(sigma*sqrt(T)) - d1*d2/(2T))
    # We compute via direct closed form:
    color_year = -pdf1 / (2.0 * S * T * sigma * sqrtT) * (
        2.0 * r * T + 1.0
        + (2.0 * r * T - d2 * sigma * sqrtT) * d1 / (sigma * sqrtT)
    )
    color = color_year / 365.0

    # Volga (vomma): vega * d1 * d2 / sigma. Vega per 1 vol-pt = S*phi(d1)*sqrt(T)/100.
    vega_per_pt = S * pdf1 * sqrtT / 100.0
    volga = vega_per_pt * d1 * d2 / sigma / 100.0

    return vanna, charm, color, volga


LANG_STRINGS = {
    "en": {
        "title":    "Second-order Greeks vs spot - 30-day, K=$100, sigma=20%, r=4% call",
        "subtitle": "Closed-form Black-Scholes. Vanna and volga are per 1 vol-pt; charm and color are per calendar day.",
        "vanna_t":  "Vanna - dDelta / dSigma (per 1 vol-pt)",
        "charm_t":  "Charm - dDelta / dt (per day)",
        "color_t":  "Color - dGamma / dt (per day)",
        "volga_t":  "Volga (Vomma) - dVega / dSigma (per 1 vol-pt)",
        "xlabel":   "Spot price ($)",
        "atm":      "ATM (S=K)",
        "footer":   "Vanna and volga peak in the wings; charm peaks ITM/OTM and is near zero ATM; color is most negative ATM, where the gamma bell sharpens fastest.",
    },
    "hk": {
        "title":    "二階 Greek 對現價 - 30 日,K=100 美元,sigma=20%,r=4% 認購",
        "subtitle": "Black-Scholes 封閉解。Vanna 與 Volga 為每 1 vol 點;Charm 與 Color 為每曆日。",
        "vanna_t":  "Vanna - dDelta / dSigma(每 1 vol 點)",
        "charm_t":  "Charm - dDelta / dt(每日)",
        "color_t":  "Color - dGamma / dt(每日)",
        "volga_t":  "Volga(Vomma)- dVega / dSigma(每 1 vol 點)",
        "xlabel":   "現價(美元)",
        "atm":      "ATM(S=K)",
        "footer":   "Vanna 與 Volga 在價內價外兩翼最大;Charm 在 ITM/OTM 最大,ATM 接近零;Color 在 ATM 最負,該處 Gamma 鐘形收窄最快。",
    },
    "tw": {
        "title":    "二階 Greek 對現價 - 30 日,K=100 美元,sigma=20%,r=4% 買權",
        "subtitle": "Black-Scholes 封閉解。Vanna 與 Volga 為每 1 vol 點;Charm 與 Color 為每日曆日。",
        "vanna_t":  "Vanna - dDelta / dSigma(每 1 vol 點)",
        "charm_t":  "Charm - dDelta / dt(每日)",
        "color_t":  "Color - dGamma / dt(每日)",
        "volga_t":  "Volga(Vomma)- dVega / dSigma(每 1 vol 點)",
        "xlabel":   "現價(美元)",
        "atm":      "ATM(S=K)",
        "footer":   "Vanna 與 Volga 於兩翼最大;Charm 於價內外最大,ATM 近零;Color 於 ATM 最負,Gamma 鐘形收窄最快。",
    },
    "cn": {
        "title":    "二阶 Greek 对现价 - 30 日,K=100 美元,sigma=20%,r=4% 看涨",
        "subtitle": "Black-Scholes 闭式解。Vanna 与 Volga 为每 1 vol 点;Charm 与 Color 为每日历日。",
        "vanna_t":  "Vanna - dDelta / dSigma(每 1 vol 点)",
        "charm_t":  "Charm - dDelta / dt(每日)",
        "color_t":  "Color - dGamma / dt(每日)",
        "volga_t":  "Volga(Vomma)- dVega / dSigma(每 1 vol 点)",
        "xlabel":   "现价(美元)",
        "atm":      "ATM(S=K)",
        "footer":   "Vanna 与 Volga 在两翼最大;Charm 在 ITM/OTM 最大,ATM 接近零;Color 在 ATM 最负,Gamma 钟形收窄最快。",
    },
}


def build_fig(s):
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v)
         for k, v in s.items()}
    p = PALETTE_LIGHT

    K = 100.0
    T = 30.0 / 365.0
    sigma = 0.20
    r = 0.04
    S = np.linspace(70.0, 130.0, 401)

    vanna, charm, color, volga = second_order_greeks(S, K, T, sigma, r)

    fig, axs = plt.subplots(2, 2, figsize=(12.4, 7.6))
    for ax in axs.flat:
        style_axes(ax, p)

    panels = [
        (axs[0, 0], charm, s["charm_t"], p["red"],    "{:+.4f}"),
        (axs[0, 1], vanna, s["vanna_t"], p["blue"],   "{:+.4f}"),
        (axs[1, 0], color, s["color_t"], p["accent"], "{:+.5f}"),
        (axs[1, 1], volga, s["volga_t"], p["green"],  "{:+.4f}"),
    ]

    for ax, y, title, color_, fmt in panels:
        ax.plot(S, y, color=color_, linewidth=2.4)
        ax.fill_between(S, y, color=color_, alpha=0.10)
        ax.axvline(K, color=p["muted"], linewidth=0.9,
                   linestyle="--", alpha=0.7)
        ax.axhline(0.0, color=p["muted"], linewidth=0.7,
                   linestyle="-", alpha=0.5)
        ax.set_title(title, fontsize=11.3, fontweight="bold",
                     color=p["fg"], loc="left", pad=6)
        ax.set_xlabel(s["xlabel"], fontsize=9.5, color=p["muted"])
        ax.set_xlim(70, 130)

        idx_atm = int(np.argmin(np.abs(S - K)))
        ax.plot(K, y[idx_atm], "o", color=color_, markersize=6, zorder=5)
        ax.annotate(s["atm"] + " " + fmt.format(y[idx_atm]),
                    xy=(K, y[idx_atm]),
                    xytext=(8, 8 if y[idx_atm] >= 0 else -16),
                    textcoords="offset points",
                    fontsize=9, color=color_, fontweight="bold")

    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 color=p["fg"], x=0.02, ha="left", y=0.985)
    fig.text(0.02, 0.945, s["subtitle"], fontsize=10, color=p["muted"])
    fig.text(0.02, 0.01, s["footer"], fontsize=9.2,
             color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.03, 1, 0.93])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
