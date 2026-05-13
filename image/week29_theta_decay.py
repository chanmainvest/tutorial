"""Week 29, §2.4 — Theta acceleration as expiration approaches.

For a sequence of ATM calls (S=K=100, sigma=20%, r=4%) we compute the
absolute one-day theta at every DTE from 90 down to 1, and the
cumulative premium loss from a 90-day starting point. The point of the
chart is that time-decay is non-linear: roughly two-thirds of the
extrinsic premium of a 90-day ATM option burns in the final 30 days.

Run:
    uv run python course/image/week29_theta_decay.py
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
BASE = "week29_theta_decay"


SQRT_2PI = math.sqrt(2.0 * math.pi)


def _Phi(x):
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2.0)))


def _phi(x):
    return np.exp(-0.5 * x * x) / SQRT_2PI


def bsm_call_price(S, K, T, sigma, r):
    sqrtT = np.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    return S * _Phi(d1) - K * np.exp(-r * T) * _Phi(d2)


def bsm_call_theta_per_day(S, K, T, sigma, r):
    sqrtT = np.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    theta_year = (-S * _phi(d1) * sigma / (2.0 * sqrtT)
                  - r * K * np.exp(-r * T) * _Phi(d2))
    return theta_year / 365.0


LANG_STRINGS = {
    "en": {
        "title":    "Theta accelerates as expiry approaches - ATM call, S=K=$100, sigma=20%",
        "subtitle": "Left panel: |theta| per calendar day rises from ~$0.013 at 90 DTE to ~$0.20 at 3 DTE. Right panel: option premium itself, with the last-30-day cliff highlighted.",
        "x_left":   "Days to expiration (DTE)",
        "y_left":   "|Theta| per day ($ per share)",
        "x_right":  "Days to expiration (DTE)",
        "y_right":  "Call premium ($ per share)",
        "left_t":   "Daily theta cost",
        "right_t":  "Premium decay path",
        "band":     "Last 30 days = ~63% of 90-day premium gone",
        "footer":   "Sellers love this curve, buyers hate it. The 30-45 DTE window is the sweet spot for theta-collectors: enough remaining premium to be worth selling, decay starting to bite.",
        "anno30":   "30 DTE: theta ~ $0.05/day",
        "anno7":    "7 DTE: theta ~ $0.10/day",
        "anno1":    "1 DTE: theta ~ $0.20/day",
    },
    "hk": {
        "title":    "Theta 隨到期日加速 - ATM 認購,S=K=100 美元,sigma=20%",
        "subtitle": "左圖:每曆日 |theta| 由 90 DTE 約 0.013 美元升至 3 DTE 約 0.20 美元。右圖:期權價格本身,最後 30 日的懸崖突出顯示。",
        "x_left":   "距到期日(DTE)",
        "y_left":   "每日 |Theta|(每股美元)",
        "x_right":  "距到期日(DTE)",
        "y_right":  "認購權利金(每股美元)",
        "left_t":   "每日 Theta 成本",
        "right_t":  "權利金衰減路徑",
        "band":     "最後 30 日 = 90 日權利金的約 63% 消失",
        "footer":   "賣方喜歡這條曲線,買方討厭。30-45 DTE 是 Theta 收集者的甜點區:剩餘權利金值得賣,衰減又開始啃噬。",
        "anno30":   "30 DTE:theta 約 0.05/日",
        "anno7":    "7 DTE:theta 約 0.10/日",
        "anno1":    "1 DTE:theta 約 0.20/日",
    },
    "tw": {
        "title":    "Theta 隨到期日加速 - ATM 買權,S=K=100 美元,sigma=20%",
        "subtitle": "左圖:每日曆 |theta| 由 90 DTE 約 0.013 美元升至 3 DTE 約 0.20 美元。右圖:選擇權價格本身,最後 30 日的懸崖凸顯。",
        "x_left":   "距到期日(DTE)",
        "y_left":   "每日 |Theta|(每股美元)",
        "x_right":  "距到期日(DTE)",
        "y_right":  "買權權利金(每股美元)",
        "left_t":   "每日 Theta 成本",
        "right_t":  "權利金衰減路徑",
        "band":     "最後 30 日 = 90 日權利金的約 63% 蒸發",
        "footer":   "賣方愛這條曲線,買方恨它。30-45 DTE 是 Theta 收集者的甜蜜點:剩餘權利金夠賣,衰減開始發威。",
        "anno30":   "30 DTE:theta 約 0.05/日",
        "anno7":    "7 DTE:theta 約 0.10/日",
        "anno1":    "1 DTE:theta 約 0.20/日",
    },
    "cn": {
        "title":    "Theta 随到期日加速 - ATM 看涨,S=K=100 美元,sigma=20%",
        "subtitle": "左图:每日历日 |theta| 由 90 DTE 约 0.013 美元升至 3 DTE 约 0.20 美元。右图:期权价格本身,最后 30 日的悬崖凸显。",
        "x_left":   "距到期日(DTE)",
        "y_left":   "每日 |Theta|(每股美元)",
        "x_right":  "距到期日(DTE)",
        "y_right":  "看涨权利金(每股美元)",
        "left_t":   "每日 Theta 成本",
        "right_t":  "权利金衰减路径",
        "band":     "最后 30 日 = 90 日权利金的约 63% 蒸发",
        "footer":   "卖方喜欢这条曲线,买方讨厌。30-45 DTE 是 Theta 收割者的甜蜜区:剩余权利金值得卖,衰减刚开始啃食。",
        "anno30":   "30 DTE:theta 约 0.05/日",
        "anno7":    "7 DTE:theta 约 0.10/日",
        "anno1":    "1 DTE:theta 约 0.20/日",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT

    K = 100.0
    S = 100.0
    sigma = 0.20
    r = 0.04

    dte = np.arange(90, 0, -1)            # 90, 89, ..., 1
    T = dte / 365.0
    theta = bsm_call_theta_per_day(S, K, T, sigma, r)
    abs_theta = -theta                    # positive numbers
    prem = bsm_call_price(S, K, T, sigma, r)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.4, 5.4))
    style_axes(axL, p)
    style_axes(axR, p)

    # --- Left: |theta| per day vs DTE. X-axis decreases left to right.
    axL.plot(dte, abs_theta, color=p["red"], linewidth=2.4)
    axL.fill_between(dte, abs_theta, color=p["red"], alpha=0.12)
    axL.invert_xaxis()
    axL.set_xlabel(s["x_left"], fontsize=10, color=p["muted"])
    axL.set_ylabel(s["y_left"], fontsize=10, color=p["muted"])
    axL.set_title(s["left_t"], fontsize=11.5, fontweight="bold",
                  color=p["fg"], loc="left", pad=6)

    # Highlight the last 30 days.
    axL.axvspan(30, 0, color=p["accent"], alpha=0.10)

    def _idx(d):
        return int(np.where(dte == d)[0][0])

    for d, key, dy in ((30, "anno30", -22), (7, "anno7", -22), (1, "anno1", -22)):
        i = _idx(d)
        axL.plot(d, abs_theta[i], "o", color=p["red"], markersize=6, zorder=5)
        axL.annotate(s[key], xy=(d, abs_theta[i]),
                     xytext=(-60, dy), textcoords="offset points",
                     fontsize=9, color=p["red"], fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=p["red"]))

    # --- Right: premium decay path.
    axR.plot(dte, prem, color=p["blue"], linewidth=2.4)
    axR.fill_between(dte, prem, color=p["blue"], alpha=0.12)
    axR.invert_xaxis()
    axR.set_xlabel(s["x_right"], fontsize=10, color=p["muted"])
    axR.set_ylabel(s["y_right"], fontsize=10, color=p["muted"])
    axR.set_title(s["right_t"], fontsize=11.5, fontweight="bold",
                  color=p["fg"], loc="left", pad=6)
    axR.axvspan(30, 0, color=p["accent"], alpha=0.10)

    p90 = prem[_idx(90)]
    p30 = prem[_idx(30)]
    p1 = prem[_idx(1)]
    axR.plot(90, p90, "o", color=p["blue"], markersize=6, zorder=5)
    axR.plot(30, p30, "o", color=p["blue"], markersize=6, zorder=5)
    axR.plot(1, p1, "o", color=p["blue"], markersize=6, zorder=5)
    axR.annotate(rf"\${p90:.2f}", xy=(90, p90), xytext=(8, 6),
                 textcoords="offset points", fontsize=9.5,
                 color=p["blue"], fontweight="bold")
    axR.annotate(rf"\${p30:.2f}", xy=(30, p30), xytext=(8, 6),
                 textcoords="offset points", fontsize=9.5,
                 color=p["blue"], fontweight="bold")
    axR.annotate(rf"\${p1:.2f}", xy=(1, p1), xytext=(-44, 10),
                 textcoords="offset points", fontsize=9.5,
                 color=p["blue"], fontweight="bold")
    axR.text(15, p90 * 0.55, s["band"], fontsize=9.5,
             color=p["accent"], fontweight="bold", ha="center")

    fig.suptitle(s["title"], fontsize=14, fontweight="bold",
                 color=p["fg"], x=0.02, ha="left", y=0.99)
    fig.text(0.02, 0.94, s["subtitle"], fontsize=10, color=p["muted"])
    fig.text(0.02, 0.01, s["footer"], fontsize=9.2,
             color=p["accent"], fontweight="bold")

    fig.tight_layout(rect=[0, 0.04, 1, 0.91])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
