"""Week 24, §2.4 — Layered expected-return decomposition by archetype.

For four archetypes (conservative, moderate, aggressive, institutional),
stack the contribution to expected return from each sleeve plus the
fee drag, with the net result marked.

Assumed inputs (4-locale labels keep them readable):
  beta  return  =  7.0%
  factor return =  9.0% (= 7% beta + 2% factor premium)
  alpha return  =  4.0% (market-neutral, uncorrelated)
  cash  return  =  4.0%
  fees: beta 0.04% / factor 0.20% / alpha 1.50% / cash 0.10%
        applied to each sleeve weight.

Run:
    uv run python course/image/week24_layered_returns.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    render_for_all_locales,
    style_axes,
)

OUT_DIR = Path(__file__).parent
BASE = "week24_layered_returns"

# weights (beta, factor, alpha, cash) per archetype
ARCHETYPES = [
    ("conservative",  [0.90, 0.00, 0.00, 0.10]),
    ("moderate",      [0.80, 0.10, 0.05, 0.05]),
    ("aggressive",    [0.65, 0.15, 0.15, 0.05]),
    ("institutional", [0.70, 0.15, 0.13, 0.02]),
]

R_BETA, R_FACTOR, R_ALPHA, R_CASH = 0.07, 0.09, 0.04, 0.04
F_BETA, F_FACTOR, F_ALPHA, F_CASH = 0.0004, 0.0020, 0.0150, 0.0010

LANG_STRINGS = {
    "en": {
        "title":         "Expected return decomposition — four archetype portfolios",
        "subtitle":      "Each bar stacks the gross contribution from beta, factor, alpha, cash sleeves; fee drag is plotted to the left of zero. Net return is the black tick. SOUL #1: most of the return comes from the beta sleeve — the rest is buying vol reduction.",
        "xlabel":        "Contribution to expected annual return (%)",
        "conservative":  "Conservative\n(90/0/0/10)",
        "moderate":      "Moderate\n(80/10/5/5)",
        "aggressive":    "Aggressive\n(65/15/15/5)",
        "institutional": "Institutional\n(70/15/13/2)",
        "beta":          "Beta sleeve",
        "factor":        "Factor sleeve",
        "alpha":         "Alpha sleeve",
        "cash":          "Cash sleeve",
        "fees":          "Fee drag",
        "net":           "Net return",
        "footer":        "Inputs: beta 7%, factor 9% (7% + 2% premium), alpha 4% market-neutral, cash 4%; fees: beta 4 bps / factor 20 bps / alpha 150 bps / cash 10 bps applied to each sleeve weight.",
    },
    "hk": {
        "title":         "預期回報拆解 — 四個原型組合",
        "subtitle":      "每條柱堆疊 beta / 因子 / alpha / 現金板塊的毛貢獻;費用拖累畫在零的左側。淨回報以黑色刻度標示。SOUL #1:多數回報來自 beta 板塊,其餘是在買波動下降。",
        "xlabel":        "對年化預期回報的貢獻 (%)",
        "conservative":  "保守型\n(90/0/0/10)",
        "moderate":      "中庸型\n(80/10/5/5)",
        "aggressive":    "進取型\n(65/15/15/5)",
        "institutional": "機構型\n(70/15/13/2)",
        "beta":          "Beta 板塊",
        "factor":        "因子板塊",
        "alpha":         "Alpha 板塊",
        "cash":          "現金板塊",
        "fees":          "費用拖累",
        "net":           "淨回報",
        "footer":        "假設:beta 7%、因子 9%(7% + 2% 溢價)、alpha 4% 市場中性、現金 4%;費用 beta 4 bps / 因子 20 bps / alpha 150 bps / 現金 10 bps 按板塊權重計。",
    },
    "tw": {
        "title":         "預期報酬拆解 — 四個原型組合",
        "subtitle":      "每條柱堆疊 beta / 因子 / alpha / 現金板塊的毛貢獻;費用拖累畫在零的左側。淨報酬以黑色刻度標示。SOUL #1:多數報酬來自 beta 板塊,其餘是在買波動下降。",
        "xlabel":        "對年化預期報酬的貢獻 (%)",
        "conservative":  "保守型\n(90/0/0/10)",
        "moderate":      "中庸型\n(80/10/5/5)",
        "aggressive":    "積極型\n(65/15/15/5)",
        "institutional": "機構型\n(70/15/13/2)",
        "beta":          "Beta 板塊",
        "factor":        "因子板塊",
        "alpha":         "Alpha 板塊",
        "cash":          "現金板塊",
        "fees":          "費用拖累",
        "net":           "淨報酬",
        "footer":        "假設:beta 7%、因子 9%(7% + 2% 溢價)、alpha 4% 市場中性、現金 4%;費用 beta 4 bps / 因子 20 bps / alpha 150 bps / 現金 10 bps 按板塊權重計。",
    },
    "cn": {
        "title":         "预期回报拆解 — 四个原型组合",
        "subtitle":      "每条柱堆叠 beta / 因子 / alpha / 现金板块的毛贡献;费用拖累画在零的左侧。净回报以黑色刻度标示。SOUL #1:多数回报来自 beta 板块,其余是在买波动下降。",
        "xlabel":        "对年化预期回报的贡献 (%)",
        "conservative":  "保守型\n(90/0/0/10)",
        "moderate":      "中庸型\n(80/10/5/5)",
        "aggressive":    "进取型\n(65/15/15/5)",
        "institutional": "机构型\n(70/15/13/2)",
        "beta":          "Beta 板块",
        "factor":        "因子板块",
        "alpha":         "Alpha 板块",
        "cash":          "现金板块",
        "fees":          "费用拖累",
        "net":           "净回报",
        "footer":        "假设:beta 7%、因子 9%(7% + 2% 溢价)、alpha 4% 市场中性、现金 4%;费用 beta 4 bps / 因子 20 bps / alpha 150 bps / 现金 10 bps 按板块权重计。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    sleeve_colors = {
        "beta":   p["blue"],
        "factor": p["accent"],
        "alpha":  p["green"],
        "cash":   p["grey"],
        "fees":   p["red"],
    }

    fig, ax = plt.subplots(figsize=(11, 6.0))
    style_axes(ax, p)

    rows = list(reversed(ARCHETYPES))   # top-to-bottom
    y = np.arange(len(rows))
    labels = [s[k] for k, _ in rows]

    for i, (_, w) in enumerate(rows):
        wb, wf, wa, wc = w
        contrib_b = wb * R_BETA   * 100
        contrib_f = wf * R_FACTOR * 100
        contrib_a = wa * R_ALPHA  * 100
        contrib_c = wc * R_CASH   * 100
        fee_total = -(wb * F_BETA + wf * F_FACTOR + wa * F_ALPHA + wc * F_CASH) * 100
        net = contrib_b + contrib_f + contrib_a + contrib_c + fee_total

        # Positive stack starting at 0
        left = 0.0
        for key, c in [("beta", contrib_b), ("factor", contrib_f),
                       ("alpha", contrib_a), ("cash", contrib_c)]:
            if c <= 0:
                continue
            ax.barh(i, c, left=left, color=sleeve_colors[key],
                    edgecolor=p["bg"], linewidth=1.0,
                    label=s[key] if i == 0 else None)
            if c >= 0.4:
                ax.text(left + c / 2, i, f"{c:.2f}",
                        ha="center", va="center",
                        color="white", fontsize=9, fontweight="bold")
            left += c

        # Fee drag negative bar (to the left of zero)
        ax.barh(i, fee_total, left=0, color=sleeve_colors["fees"],
                edgecolor=p["bg"], linewidth=1.0,
                label=s["fees"] if i == 0 else None)
        if abs(fee_total) >= 0.05:
            ax.text(fee_total / 2, i, f"{fee_total:.2f}",
                    ha="center", va="center",
                    color="white", fontsize=8.5, fontweight="bold")

        # Net tick
        ax.plot([net, net], [i - 0.36, i + 0.36],
                color=p["fg"], linewidth=2.4,
                label=s["net"] if i == 0 else None)
        ax.text(net + 0.1, i, f"{net:.2f}%",
                va="center", color=p["fg"], fontsize=10, fontweight="bold")

    ax.axvline(0, color=p["muted"], linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel(s["xlabel"])
    ax.set_xlim(-1.0, 8.5)

    ax.set_title(s["title"], fontsize=14, fontweight="bold",
                 loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=10, color=p["muted"], wrap=True)

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.26),
              ncol=6, frameon=False, fontsize=9.5)

    ax.text(0, -0.34, s["footer"], transform=ax.transAxes,
            fontsize=8.5, color=p["muted"], style="italic")

    fig.tight_layout(rect=[0, 0.06, 1, 0.94])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
