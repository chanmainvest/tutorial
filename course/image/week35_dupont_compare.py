"""Week 35, §2.1 — DuPont 3-factor decomposition for five firms (FY2024).

Bar chart with one cluster per firm (AAPL, MSFT, KO, JPM, F). Each
cluster shows three component bars (NPM, Asset Turnover, Equity
Multiplier) plus a fourth ROE bar. Values are FY2024 approximations
from public 10-K filings.

  AAPL: NPM 23.97%, AT 1.07, EM 6.40 -> ROE ~165%
  MSFT: NPM 35.94%, AT 0.48, EM 1.91 -> ROE ~33%
  KO:   NPM 22.74%, AT 0.47, EM 4.04 -> ROE ~43%
  JPM:  NPM 37.00%, AT 0.04, EM 11.6 -> ROE ~17%
  F:    NPM 3.18%,  AT 0.65, EM 6.63 -> ROE ~14%

Run:
    uv run python course/image/week35_dupont_compare.py
"""

from __future__ import annotations

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
BASE = "week35_dupont_compare"


# Firms in display order
FIRMS = ["AAPL", "MSFT", "KO", "JPM", "F"]

# (NPM_percent, Asset_Turnover, Equity_Multiplier)
DUPONT = {
    "AAPL": (23.97, 1.07, 6.40),
    "MSFT": (35.94, 0.48, 1.91),
    "KO":   (22.74, 0.47, 4.04),
    "JPM":  (37.00, 0.04, 11.60),
    "F":    (3.18, 0.65, 6.63),
}

def roe(firm: str) -> float:
    npm, at, em = DUPONT[firm]
    return (npm / 100.0) * at * em * 100.0


LANG_STRINGS = {
    "en": {
        "title":    "DuPont decomposition: ROE = NPM x Asset Turnover x Equity Multiplier (FY2024)",
        "subtitle": "Five firms, three different paths to a similar headline ROE. AAPL's >150% ROE is buyback-driven; JPM's is leverage-driven; F's is turnover-with-thin-margin.",
        "xlabel":   "",
        "ylabel_left":  "Net Profit Margin (%)   |   Asset Turnover (x)   |   Equity Multiplier (x)",
        "ylabel_right": "Resulting ROE (%)",
        "npm":      "Net Profit Margin (%)",
        "at":       "Asset Turnover (x)",
        "em":       "Equity Multiplier (x)",
        "roe":      "ROE (%)",
        "footer":   "Source: company FY2024 10-Ks. Same headline ROE can come from very different machines.",
    },
    "hk": {
        "title":    "杜邦分解:ROE = 淨利率 x 資產周轉 x 權益乘數(FY2024)",
        "subtitle": "五家公司,三條通往相近 ROE 的不同路徑。AAPL 超過 150% 由回購驅動;JPM 由槓桿驅動;F 是高周轉低利潤。",
        "xlabel":   "",
        "ylabel_left":  "淨利率(%)|資產周轉(倍)|權益乘數(倍)",
        "ylabel_right": "由此得出之 ROE(%)",
        "npm":      "淨利率(%)",
        "at":       "資產周轉(倍)",
        "em":       "權益乘數(倍)",
        "roe":      "ROE(%)",
        "footer":   "資料:各公司 FY2024 10-K。同樣的 ROE 可能來自完全不同的機器。",
    },
    "tw": {
        "title":    "杜邦分解:ROE = 淨利率 x 資產周轉 x 權益乘數(FY2024)",
        "subtitle": "五家公司,三條通往相近 ROE 的不同路徑。AAPL 超過 150% 由買回驅動;JPM 由槓桿驅動;F 是高周轉低利潤。",
        "xlabel":   "",
        "ylabel_left":  "淨利率(%)|資產周轉(倍)|權益乘數(倍)",
        "ylabel_right": "由此得出之 ROE(%)",
        "npm":      "淨利率(%)",
        "at":       "資產周轉(倍)",
        "em":       "權益乘數(倍)",
        "roe":      "ROE(%)",
        "footer":   "資料:各公司 FY2024 10-K。同樣的 ROE 可能來自完全不同的機器。",
    },
    "cn": {
        "title":    "杜邦分解:ROE = 净利率 x 资产周转 x 权益乘数(FY2024)",
        "subtitle": "五家公司,三条通往相近 ROE 的不同路径。AAPL 超过 150% 由回购驱动;JPM 由杠杆驱动;F 是高周转低利润。",
        "xlabel":   "",
        "ylabel_left":  "净利率(%)|资产周转(倍)|权益乘数(倍)",
        "ylabel_right": "由此得出之 ROE(%)",
        "npm":      "净利率(%)",
        "at":       "资产周转(倍)",
        "em":       "权益乘数(倍)",
        "roe":      "ROE(%)",
        "footer":   "资料:各公司 FY2024 10-K。同样的 ROE 可能来自完全不同的机器。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax_left = plt.subplots(figsize=(12, 6.4))
    style_axes(ax_left, p)

    n = len(FIRMS)
    x = np.arange(n)
    bw = 0.20

    npm_vals = [DUPONT[f][0] for f in FIRMS]
    at_vals  = [DUPONT[f][1] for f in FIRMS]
    em_vals  = [DUPONT[f][2] for f in FIRMS]
    roe_vals = [roe(f) for f in FIRMS]

    # Three component bars on left axis
    b1 = ax_left.bar(x - 1.5 * bw, npm_vals, bw,
                     color=p["blue"], edgecolor=p["blue"],
                     alpha=0.92, label=s["npm"])
    b2 = ax_left.bar(x - 0.5 * bw, at_vals, bw,
                     color=p["green"], edgecolor=p["green"],
                     alpha=0.92, label=s["at"])
    b3 = ax_left.bar(x + 0.5 * bw, em_vals, bw,
                     color=p["purple"], edgecolor=p["purple"],
                     alpha=0.92, label=s["em"])

    # Right axis for ROE
    ax_right = ax_left.twinx()
    ax_right.spines["top"].set_visible(False)
    ax_right.tick_params(colors=p["fg"], labelsize=9)
    ax_right.yaxis.label.set_color(p["fg"])
    b4 = ax_right.bar(x + 1.5 * bw, roe_vals, bw,
                      color=p["accent"], edgecolor=p["accent"],
                      alpha=0.95, label=s["roe"])

    # Value labels
    for bar, val, fmt_str in zip(b1, npm_vals, ["%.1f%%"] * n):
        ax_left.text(bar.get_x() + bar.get_width() / 2, val + 0.4,
                     fmt_str % val, ha="center", va="bottom",
                     fontsize=8.5, color=p["blue"], fontweight="bold")
    for bar, val in zip(b2, at_vals):
        ax_left.text(bar.get_x() + bar.get_width() / 2, val + 0.05,
                     f"{val:.2f}", ha="center", va="bottom",
                     fontsize=8.5, color=p["green"], fontweight="bold")
    for bar, val in zip(b3, em_vals):
        ax_left.text(bar.get_x() + bar.get_width() / 2, val + 0.15,
                     f"{val:.2f}", ha="center", va="bottom",
                     fontsize=8.5, color=p["purple"], fontweight="bold")
    for bar, val in zip(b4, roe_vals):
        ax_right.text(bar.get_x() + bar.get_width() / 2, val + 2.0,
                      f"{val:.0f}%", ha="center", va="bottom",
                      fontsize=9, color=p["accent"], fontweight="bold")

    ax_left.set_xticks(x)
    ax_left.set_xticklabels(FIRMS, fontsize=11, fontweight="bold")
    ax_left.set_ylabel(s["ylabel_left"], fontsize=10, color=p["muted"])
    ax_right.set_ylabel(s["ylabel_right"], fontsize=10, color=p["accent"])

    # Set sane axis limits
    ax_left.set_ylim(0, max(max(npm_vals), max(em_vals)) * 1.20)
    ax_right.set_ylim(0, max(roe_vals) * 1.20)

    # Legend combining both axes
    handles = [b1, b2, b3, b4]
    labels = [s["npm"], s["at"], s["em"], s["roe"]]
    ax_left.legend(handles, labels, loc="upper right",
                   fontsize=9, framealpha=0.92, ncol=2)

    ax_left.set_title(s["title"], fontsize=13, fontweight="bold",
                      loc="left", pad=24)
    ax_left.text(0, 1.02, s["subtitle"], transform=ax_left.transAxes,
                 fontsize=10, color=p["muted"])
    ax_left.text(0, -0.13, s["footer"], transform=ax_left.transAxes,
                 fontsize=9.5, color=p["accent"], fontstyle="italic")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
