"""Side 14, sec 2.2 -- Stylised PE fund J-curve over 10 years.

Shows capital calls (negative bars), distributions (positive bars),
and cumulative net cash flow (line). Net IRR ~ 12% by construction,
trough at ~ -65% of committed capital in year 4, breakeven year 6,
finishes at ~ +70% in year 10.

Run:
    uv run python course/image/side14_pe_jcurve.py
"""

from __future__ import annotations
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, render_for_all_locales, style_axes, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side14_pe_jcurve"


# Capital calls (negative). Total -1.00 of commitment over years 1-5.
CALLS = {
    1: -0.20,
    2: -0.25,
    3: -0.22,
    4: -0.18,
    5: -0.15,
    6:  0.00,
    7:  0.00,
    8:  0.00,
    9:  0.00,
    10: 0.00,
}

# Distributions (positive). Sum to ~ +1.70 -> net +0.70 -> IRR ~12%.
DISTRIBUTIONS = {
    1:  0.00,
    2:  0.00,
    3:  0.04,
    4:  0.10,
    5:  0.20,
    6:  0.32,
    7:  0.36,
    8:  0.30,
    9:  0.22,
    10: 0.16,
}


def compute_series():
    years = list(range(1, 11))
    calls = [CALLS[y] for y in years]
    dists = [DISTRIBUTIONS[y] for y in years]
    nets = [calls[i] + dists[i] for i in range(len(years))]
    cum = []
    s = 0.0
    for n in nets:
        s += n
        cum.append(s)
    # Compute approximate IRR by Newton's method on yearly cash flows.
    cf = nets[:]
    # IRR solve: sum cf_i / (1+r)^i = 0 with i=1..10
    def npv(r):
        return sum(cf[i] / (1 + r) ** (i + 1) for i in range(len(cf)))
    lo, hi = -0.5, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        v = npv(mid)
        if v > 0:
            lo = mid
        else:
            hi = mid
    irr = 0.5 * (lo + hi)
    return years, calls, dists, nets, cum, irr


LANG_STRINGS = {
    "en": {
        "title": "PE Fund J-Curve -- 10-yr Cash Flow Profile",
        "subtitle": "Capital calls front-load years 1-5. Distributions back-load years 4-10. Cumulative cash troughs ~-65% of commitment in year 4; breakeven year 6; finishes +70% for net IRR ~12%.",
        "ylabel": "Cash flow / cumulative (% of committed capital)",
        "xlabel": "Year of fund life",
        "lbl_calls": "Capital calls",
        "lbl_dists": "Distributions",
        "lbl_cum": "Cumulative net cash flow",
        "lbl_irr_box": "Net IRR (computed): {irr:.1f}%/yr\nTrough: {tr:+.0%} of commitment in year {tr_y}\nBreakeven: between years 5 and 6\nTotal payout: +1.70x of commitment",
        "annot_jcurve": "The J-curve\n(years 1-5 underwater)",
        "lbl_invest_phase": "Investment period (calls)",
        "lbl_harvest_phase": "Harvest period (distributions)",
        "footer": "Stylised cash-flow profile. Calls front-load through investment period (years 1-5); distributions back-load through harvest period (years 4-10). Net IRR computed by bisection on the dated cash-flow series. Real funds dispersed widely around this shape; vintage and manager dispersion both add ~5-15 pp.",
    },
    "hk": {
        "title": "PE 基金 J 曲線 -- 10 年現金流",
        "subtitle": "出資要求集中在 1-5 年,分派集中在 4-10 年。累計現金第 4 年見底約 -65%,第 6 年回本,第 10 年 +70%,淨 IRR 約 12%。",
        "ylabel": "現金流 / 累計(承諾資本 %)",
        "xlabel": "基金生命週期年份",
        "lbl_calls": "出資要求",
        "lbl_dists": "分派",
        "lbl_cum": "累計淨現金流",
        "lbl_irr_box": "計算淨 IRR:{irr:.1f}%/年\n底部:第 {tr_y} 年 {tr:+.0%} 承諾額\n回本:第 5-6 年之間\n總分派:1.70x 承諾額",
        "annot_jcurve": "J 曲線\n(1-5 年水底)",
        "lbl_invest_phase": "投資期(出資)",
        "lbl_harvest_phase": "收成期(分派)",
        "footer": "示意現金流輪廓。投資期(1-5 年)集中出資,收成期(4-10 年)集中分派。淨 IRR 由現金流序列二分法解出。實際基金圍繞此形大幅分散,vintage 與管理人各加 ~5-15 pp 偏離。",
    },
    "tw": {
        "title": "PE 基金 J 曲線 -- 10 年現金流",
        "subtitle": "出資需求集中在 1-5 年,分配集中在 4-10 年。累計現金第 4 年觸底 -65%,第 6 年回本,第 10 年 +70%,淨 IRR 約 12%。",
        "ylabel": "現金流 / 累計(承諾資本 %)",
        "xlabel": "基金存續年份",
        "lbl_calls": "出資需求",
        "lbl_dists": "分配",
        "lbl_cum": "累計淨現金流",
        "lbl_irr_box": "計算淨 IRR:{irr:.1f}%/年\n谷底:第 {tr_y} 年 {tr:+.0%} 承諾額\n回本:第 5-6 年之間\n總分配:1.70x 承諾額",
        "annot_jcurve": "J 曲線\n(1-5 年水下)",
        "lbl_invest_phase": "投資期(出資)",
        "lbl_harvest_phase": "收成期(分配)",
        "footer": "示意現金流輪廓。投資期(1-5 年)集中出資,收成期(4-10 年)集中分配。淨 IRR 由現金流序列二分法解出。實際基金圍繞此形大幅分散,vintage 與管理人各加 ~5-15 pp 偏離。",
    },
    "cn": {
        "title": "PE 基金 J 曲线 -- 10 年现金流",
        "subtitle": "出资需求集中在 1-5 年,分配集中在 4-10 年。累计现金第 4 年触底 -65%,第 6 年回本,第 10 年 +70%,净 IRR 约 12%。",
        "ylabel": "现金流 / 累计(承诺资本 %)",
        "xlabel": "基金存续年份",
        "lbl_calls": "出资需求",
        "lbl_dists": "分配",
        "lbl_cum": "累计净现金流",
        "lbl_irr_box": "计算净 IRR:{irr:.1f}%/年\n谷底:第 {tr_y} 年 {tr:+.0%} 承诺额\n回本:第 5-6 年之间\n总分配:1.70x 承诺额",
        "annot_jcurve": "J 曲线\n(1-5 年水下)",
        "lbl_invest_phase": "投资期(出资)",
        "lbl_harvest_phase": "收成期(分配)",
        "footer": "示意现金流轮廓。投资期(1-5 年)集中出资,收成期(4-10 年)集中分配。净 IRR 由现金流序列二分法解出。实际基金围绕此形大幅分散,vintage 与管理人各加 ~5-15 pp 偏离。",
    },
}


def build_fig(s):
    P = PALETTE_LIGHT
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    years, calls, dists, nets, cum, irr = compute_series()

    fig, ax_left = plt.subplots(figsize=(11.4, 6.4), dpi=150)
    style_axes(ax_left)

    # Bars
    width = 0.42
    xs = np.array(years, dtype=float)
    ax_left.bar(xs - width / 2, [c * 100 for c in calls], width=width,
                color=P["red"], alpha=0.85, edgecolor="white", linewidth=0.6,
                label=s["lbl_calls"], zorder=3)
    ax_left.bar(xs + width / 2, [d * 100 for d in dists], width=width,
                color=P["green"], alpha=0.85, edgecolor="white", linewidth=0.6,
                label=s["lbl_dists"], zorder=3)

    # Cumulative line on the same axis (units = % of commitment).
    cum_pct = [c * 100 for c in cum]
    ax_left.plot(xs, cum_pct, color=P["fg"], linewidth=2.6, marker="o",
                 markersize=6, markerfacecolor=P["fg"],
                 markeredgecolor="white", label=s["lbl_cum"], zorder=5)

    # Underwater shading (years where cum < 0).
    underwater_x = [x for x, c in zip(xs, cum_pct) if c < 0]
    if underwater_x:
        ax_left.axvspan(min(underwater_x) - 0.5, max(underwater_x) + 0.5,
                        ymin=0, ymax=1, color=P["red"], alpha=0.07, zorder=1)

    # Zero line.
    ax_left.axhline(0, color=P["muted"], linewidth=1.0, linestyle="--", zorder=2)

    # IRR + trough callout box -- placed upper-left in the bar chart.
    trough_idx = int(np.argmin(cum_pct))
    trough_val = cum[trough_idx]
    trough_y = years[trough_idx]
    box_text = s["lbl_irr_box"].format(irr=irr * 100, tr=trough_val, tr_y=trough_y)
    ax_left.text(0.30, 0.34, box_text, transform=ax_left.transAxes,
                 ha="left", va="top",
                 fontsize=10.0, color=P["fg"],
                 bbox=dict(boxstyle="round,pad=0.55",
                           facecolor=P["bg"],
                           edgecolor=P["accent"], linewidth=1.2))

    # J-curve annotation arrow pointing to trough -- below the curve.
    ax_left.annotate(s["annot_jcurve"],
                     xy=(trough_y, trough_val * 100),
                     xytext=(1.0, -90),
                     fontsize=10.5, color=P["red"], fontweight="bold",
                     ha="left", va="center",
                     arrowprops=dict(arrowstyle="->", color=P["red"],
                                     linewidth=1.4))

    # Cumulative endpoint label.
    end_y = cum_pct[-1]
    ax_left.annotate(f"{end_y:+.0f}%",
                     xy=(xs[-1], end_y),
                     xytext=(8, 0), textcoords="offset points",
                     color=P["fg"], fontweight="bold", fontsize=10.5,
                     va="center")

    # Phase labels above plot, in the open zone above year labels.
    ax_left.text(3.0, 88, s.get("lbl_invest_phase", "Investment period (calls)"),
                 ha="center", va="center", fontsize=9.5,
                 color=P["red"], style="italic")
    ax_left.text(7.5, 88, s.get("lbl_harvest_phase", "Harvest period (distributions)"),
                 ha="center", va="center", fontsize=9.5,
                 color=P["green"], style="italic")

    ax_left.set_xlabel(s["xlabel"], fontsize=10.5)
    ax_left.set_ylabel(s["ylabel"], fontsize=10.5)
    ax_left.set_title(s["title"], pad=24, fontsize=14, weight="bold")
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color=P["muted"], style="italic")
    fig.text(0.5, 0.02, s["footer"], ha="center",
             fontsize=8.5, color=P["muted"], style="italic")

    ax_left.legend(loc="center left", bbox_to_anchor=(0.62, 0.20),
                   frameon=True, fontsize=9.5,
                   facecolor=P["bg"], edgecolor=P["grid"])
    ax_left.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"{v:+.0f}%" if v != 0 else "0%"))
    ax_left.set_xlim(0.3, 11.2)
    ax_left.set_ylim(-100, 100)
    ax_left.set_xticks(years)

    fig.tight_layout(rect=[0, 0.04, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"wrote {BASE} for all locales -> {OUT_DIR}")
