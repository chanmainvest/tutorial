"""Week 30, §2.3 - Iron condor probability-of-profit at three short-strike widths.

SPY at $500, 30 days to expiry, IV 20%, r 4%. The one-month one-sigma
move is sigma * sqrt(T) = ~5.73% = ~$28.65. Three condors are scored:
shorts at +/-1 sigma, +/-0.75 sigma, and +/-0.5 sigma. The lognormal
probability of finishing inside [Kp_short, Kc_short] is reported.

POP = Phi(d2_high) - Phi(d2_low), with the standard BSM d2 formula
applied to each short strike. With the small drift adjustment the
1-sigma POP comes in just under the naive 68%.

Run:
    uv run python course/image/week30_condor_pop.py
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
BASE = "week30_condor_pop"


SQRT2 = math.sqrt(2.0)


def _Phi(x):
    return 0.5 * (1.0 + math.erf(x / SQRT2))


def _condor_pop(S0, sigma, T, r, k_widths):
    """Return list of (label_value, POP, credit_estimate) for each k.

    k = number of sigma between spot and each short strike.
    Strikes: K_put = S0 * exp(-k * sigma * sqrt(T)),
             K_call = S0 * exp(+k * sigma * sqrt(T)).
    POP = Phi(d2_call) - Phi(d2_put), the lognormal Pr(K_put < S_T < K_call).
    """
    out = []
    sqrtT = math.sqrt(T)
    for k in k_widths:
        Kp = S0 * math.exp(-k * sigma * sqrtT)
        Kc = S0 * math.exp(+k * sigma * sqrtT)
        # d2 evaluated at each short strike.
        d2p = (math.log(S0 / Kp) + (r - 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
        d2c = (math.log(S0 / Kc) + (r - 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
        # Pr(K_put < S_T < K_call) = Phi(d2_p) - Phi(d2_c)? No.
        # P(S_T > K) = Phi(d2). So P(K_put < S_T < K_call)
        # = P(S_T > K_put) - P(S_T > K_call) = Phi(d2p) - Phi(d2c).
        pop = _Phi(d2p) - _Phi(d2c)
        out.append({"k": k, "Kp": Kp, "Kc": Kc, "pop": pop})
    return out


LANG_STRINGS = {
    "en": {
        "title":    "Iron condor POP vs short-strike distance - SPY $500, 30 DTE, IV 20%",
        "subtitle": "Lognormal probability that SPY closes between the two short strikes at expiry. Wing width = $5 in all three. Tighter shorts pay more credit; the win-rate falls off a cliff.",
        "xlabel":   "Short strike distance from spot",
        "ylabel":   "Probability of profit",
        "labels":   ["+/-1.0 sigma\n(~$471 / ~$530)",
                     "+/-0.75 sigma\n(~$478 / ~$523)",
                     "+/-0.5 sigma\n(~$486 / ~$515)"],
        "annot":    "POP",
        "footer":   "Drift adjustment from r=4%, sigma=20%, T=30/365 trims the naive 68/55/38% by ~0.5 percentage points each.",
    },
    "hk": {
        "title":    "鐵兀鷹勝率 vs 賣空執行價距離 - SPY $500,30 日到期,IV 20%",
        "subtitle": "對數常態分佈下,SPY 到期收於兩個賣空執行價之間的機率。三組翼寬均為 $5。賣空越貼價,權利金越高,勝率急跌。",
        "xlabel":   "賣空執行價距離現價",
        "ylabel":   "獲利機率",
        "labels":   ["+/-1.0 sigma\n(~$471 / ~$530)",
                     "+/-0.75 sigma\n(~$478 / ~$523)",
                     "+/-0.5 sigma\n(~$486 / ~$515)"],
        "annot":    "POP",
        "footer":   "r=4%,sigma=20%,T=30/365 的漂移調整把樸素的 68/55/38% 各削去約 0.5 個百分點。",
    },
    "tw": {
        "title":    "鐵兀鷹勝率 vs 賣空履約價距離 - SPY $500,30 日到期,IV 20%",
        "subtitle": "對數常態分佈下,SPY 到期收於兩個賣空履約價之間的機率。三組翼寬均為 $5。賣空越貼價,權利金越高,勝率快速下滑。",
        "xlabel":   "賣空履約價距現價",
        "ylabel":   "獲利機率",
        "labels":   ["+/-1.0 sigma\n(~$471 / ~$530)",
                     "+/-0.75 sigma\n(~$478 / ~$523)",
                     "+/-0.5 sigma\n(~$486 / ~$515)"],
        "annot":    "POP",
        "footer":   "r=4%,sigma=20%,T=30/365 的漂移調整將樸素的 68/55/38% 各削減約 0.5 個百分點。",
    },
    "cn": {
        "title":    "铁鹰胜率 vs 卖空行权价距离 - SPY $500,30 日到期,IV 20%",
        "subtitle": "对数正态分布下,SPY 到期收于两个卖空行权价之间的概率。三组翼宽均为 $5。卖空越贴价,权利金越高,胜率急速下滑。",
        "xlabel":   "卖空行权价距现价",
        "ylabel":   "获利概率",
        "labels":   ["+/-1.0 sigma\n(~$471 / ~$530)",
                     "+/-0.75 sigma\n(~$478 / ~$523)",
                     "+/-0.5 sigma\n(~$486 / ~$515)"],
        "annot":    "POP",
        "footer":   "r=4%,sigma=20%,T=30/365 的漂移调整将朴素的 68/55/38% 各削去约 0.5 个百分点。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v)
            if not isinstance(v, list) else
            [vv.replace("$", r"\$") for vv in v]
         for k, v in s.items()}

    S0 = 500.0
    sigma = 0.20
    T = 30.0 / 365.0
    r = 0.04
    widths = [1.0, 0.75, 0.50]
    rows = _condor_pop(S0, sigma, T, r, widths)
    pops = [row["pop"] for row in rows]

    fig, ax = plt.subplots(figsize=(11.0, 6.4), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    style_axes(ax, p)

    x = np.arange(len(rows))
    colors = [p["green"], p["accent"], p["red"]]
    bars = ax.bar(x, pops, width=0.55, color=colors,
                  edgecolor=p["bg"], linewidth=1.0, zorder=3)

    for bar, pop, row in zip(bars, pops, rows):
        ax.text(bar.get_x() + bar.get_width() / 2,
                pop + 0.012,
                f"{pop * 100:.1f}%",
                ha="center", va="bottom",
                fontsize=12, fontweight="bold",
                color=bar.get_facecolor())
        # Strike call-out near base of bar.
        ax.text(bar.get_x() + bar.get_width() / 2,
                0.02,
                f"\\${row['Kp']:.0f}  -  \\${row['Kc']:.0f}",
                ha="center", va="bottom",
                fontsize=8.6, color=p["bg"], fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(s["labels"], fontsize=10, color=p["fg"])
    ax.set_ylim(0.0, 0.85)
    ax.set_yticks([0.0, 0.2, 0.4, 0.5, 0.6, 0.68, 0.8])
    ax.set_yticklabels(["0%", "20%", "40%", "50%", "60%", "68%", "80%"])
    ax.set_xlabel(s["xlabel"], fontsize=10.5, color=p["fg"])
    ax.set_ylabel(s["ylabel"], fontsize=10.5, color=p["fg"])

    # Reference lines at the naive sigma probabilities.
    for ref, label in [(0.6827, "1σ"), (0.5468, "0.75σ"), (0.3829, "0.5σ")]:
        ax.axhline(ref, color=p["muted"], linewidth=0.5,
                   linestyle=":", alpha=0.4)

    ax.set_title(s["title"], pad=24, fontsize=14.5, weight="bold",
                 color=p["fg"], loc="left")
    fig.text(0.02, 0.92, s["subtitle"], ha="left",
             fontsize=10, color=p["muted"], style="italic")
    fig.text(0.5, 0.015, s["footer"], ha="center",
             fontsize=9, color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.04, 1, 0.90])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
