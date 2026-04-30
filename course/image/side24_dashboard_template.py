"""Side 24, §2.5 — Mock 4-panel monitoring dashboard.

Single-figure layout matching the spreadsheet workflow described in the
markdown: top-left wealth path vs 60/40 reference, top-right peak drawdown
band, bottom-left asset-class breakdown bars (target vs actual with drift
arrows), bottom-right monthly fee accrual line. All data is illustrative —
hand-built monthly synthesis seeded by deterministic LCG so the four-locale
PNGs render byte-stable.

Run:
    uv run python course/image/side24_dashboard_template.py
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
    apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side24_dashboard_template"


# ---------- deterministic monthly synthetic 60-month wealth path ----------
def _lcg(seed: int):
    state = [seed & 0xFFFFFFFF]
    def nxt():
        state[0] = (1664525 * state[0] + 1013904223) & 0xFFFFFFFF
        return state[0] / 0xFFFFFFFF
    return nxt


def _box_muller(rng):
    while True:
        u1 = max(rng(), 1e-9)
        u2 = rng()
        yield (-2.0 * np.log(u1)) ** 0.5 * np.cos(2 * np.pi * u2)


def _wealth_paths(months=60, seed=20260429):
    rng = _lcg(seed)
    bm = _box_muller(rng)
    # Portfolio: 7%/yr, 11% vol monthly. 60/40: 6%/yr, 9% vol.
    mu_p, sig_p = 0.07 / 12, 0.11 / np.sqrt(12)
    mu_b, sig_b = 0.06 / 12, 0.09 / np.sqrt(12)
    p = [1.0]
    b = [1.0]
    for _ in range(months):
        z1 = next(bm)
        z2 = 0.85 * z1 + (1 - 0.85**2) ** 0.5 * next(bm)
        p.append(p[-1] * (1 + mu_p + sig_p * z1))
        b.append(b[-1] * (1 + mu_b + sig_b * z2))
    return np.array(p), np.array(b)


def build_fig(s):
    p = PALETTE_LIGHT
    # Escape literal $ so matplotlib mathtext doesn't eat substrings.
    s = {k: (v.replace("$", r"\$") if isinstance(v, str) else v) for k, v in s.items()}

    fig = plt.figure(figsize=(13.0, 8.2), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    gs = fig.add_gridspec(2, 2, hspace=0.42, wspace=0.26,
                          left=0.07, right=0.97, top=0.88, bottom=0.09)

    months = np.arange(0, 61)
    port, ref = _wealth_paths(60)

    # --- Panel 1: wealth path -------------------------------------------------
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(months, port, color=p["blue"], lw=2.2, label=s["lab_yours"])
    ax1.plot(months, ref, color=p["grey"], lw=1.3, ls="--", label=s["lab_ref"])
    ax1.fill_between(months, port, ref, where=(port >= ref),
                     color=p["green"], alpha=0.10)
    ax1.fill_between(months, port, ref, where=(port < ref),
                     color=p["red"], alpha=0.10)
    ax1.set_title(s["p1_title"], color=p["fg"], fontsize=11.5, weight="bold", pad=8)
    ax1.set_xlabel(s["xlabel_months"], fontsize=9, color=p["muted"])
    ax1.set_ylabel(s["ylabel_value"], fontsize=9, color=p["muted"])
    ax1.legend(loc="upper left", fontsize=8.5, frameon=False)
    style_axes(ax1)
    ax1.text(0.98, 0.05,
             f"{s['lab_terminal']}: {port[-1]:.2f}x", transform=ax1.transAxes,
             ha="right", va="bottom", fontsize=9.2, color=p["fg"],
             bbox=dict(boxstyle="round,pad=0.3", fc=p["bg"], ec=p["grid"], lw=0.7))

    # --- Panel 2: drawdown ----------------------------------------------------
    ax2 = fig.add_subplot(gs[0, 1])
    peak = np.maximum.accumulate(port)
    dd = port / peak - 1.0
    ax2.fill_between(months, dd * 100, 0, color=p["red"], alpha=0.35, lw=0)
    ax2.plot(months, dd * 100, color=p["red"], lw=1.4)
    ax2.axhline(-15, color=p["accent"], lw=1.0, ls="--")
    ax2.text(months[-1], -15, f"  {s['lab_ips_band']} -15%",
             ha="left", va="center", fontsize=8.6, color=p["accent"])
    ax2.set_title(s["p2_title"], color=p["fg"], fontsize=11.5, weight="bold", pad=8)
    ax2.set_xlabel(s["xlabel_months"], fontsize=9, color=p["muted"])
    ax2.set_ylabel(s["ylabel_dd"], fontsize=9, color=p["muted"])
    ax2.set_ylim(-25, 2)
    style_axes(ax2)
    worst = float(dd.min()) * 100
    ax2.text(0.98, 0.05, f"{s['lab_worst']}: {worst:.1f}%",
             transform=ax2.transAxes, ha="right", va="bottom",
             fontsize=9.2, color=p["fg"],
             bbox=dict(boxstyle="round,pad=0.3", fc=p["bg"], ec=p["grid"], lw=0.7))

    # --- Panel 3: asset-class breakdown ---------------------------------------
    ax3 = fig.add_subplot(gs[1, 0])
    sleeves = ["equity", "income", "gold", "btc", "cta", "tail", "cash"]
    target = np.array([35, 25, 15, 5, 10, 5, 5])
    actual = np.array([42, 22, 14, 7, 8, 4, 3])
    drift = actual - target
    colors = [p["blue"], p["red"], p["accent"], p["purple"],
              p["teal"], p["orange"], p["grey"]]
    y = np.arange(len(sleeves))
    width = 0.36
    ax3.barh(y - width / 2, target, height=width, color=colors,
             alpha=0.45, edgecolor=p["grid"], lw=0.5, label=s["lab_target"])
    ax3.barh(y + width / 2, actual, height=width, color=colors,
             edgecolor=p["fg"], lw=0.5, label=s["lab_actual"])
    for i, d in enumerate(drift):
        clr = p["red"] if abs(d) > 5 else p["fg"]
        sign = "+" if d > 0 else ""
        ax3.text(max(target[i], actual[i]) + 1.2, i, f"{sign}{d}pp",
                 va="center", fontsize=8.5, color=clr, weight="bold")
    ax3.set_yticks(y)
    ax3.set_yticklabels([s[f"sleeve_{k}"] for k in sleeves], fontsize=9)
    ax3.invert_yaxis()
    ax3.set_xlim(0, 52)
    ax3.set_xlabel(s["xlabel_pct"], fontsize=9, color=p["muted"])
    ax3.set_title(s["p3_title"], color=p["fg"], fontsize=11.5, weight="bold", pad=8)
    ax3.legend(loc="lower right", fontsize=8.5, frameon=False)
    style_axes(ax3)
    ax3.axvline(0, color=p["grid"], lw=0.6)

    # --- Panel 4: fees paid ---------------------------------------------------
    ax4 = fig.add_subplot(gs[1, 1])
    # Hypothetical $500k portfolio, weighted ER = 0.18% -> $900/yr -> $75/mo,
    # plus a one-time advisory bill of $1500 in month 6, plus a 12b-1 drag
    # rising 5% across the window. Cumulative line.
    base_monthly = 75.0
    monthly = np.array([base_monthly * (1 + 0.05 * (m / 60)) for m in range(61)])
    monthly[6] += 1500
    cum_fees = np.cumsum(monthly)
    ax4.plot(months, cum_fees, color=p["accent"], lw=2.2)
    ax4.fill_between(months, cum_fees, 0, color=p["accent"], alpha=0.12)
    ax4.set_title(s["p4_title"], color=p["fg"], fontsize=11.5, weight="bold", pad=8)
    ax4.set_xlabel(s["xlabel_months"], fontsize=9, color=p["muted"])
    ax4.set_ylabel(s["ylabel_dollar"], fontsize=9, color=p["muted"])
    style_axes(ax4)
    ax4.text(months[-1], cum_fees[-1],
             f"  {s['lab_total_fees']}: \\${cum_fees[-1]/1000:.1f}k",
             ha="left", va="center", fontsize=9.2, color=p["fg"], weight="bold")
    ax4.set_xlim(0, 70)

    # --- suptitle / subtitle / footer ----------------------------------------
    fig.suptitle(s["title"], color=p["fg"], fontsize=15, weight="bold", y=0.965)
    fig.text(0.5, 0.918, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.015, s["footer"], ha="center",
             fontsize=9.2, color=p["muted"])
    return fig


LANG_STRINGS = {
    "en": {
        "title": "Monthly portfolio dashboard -- 4 panels, one page",
        "subtitle": "What the spreadsheet view should show: wealth, drawdown, drift, fees. (Side 24)",
        "footer": "Illustrative model L4 portfolio, 5-year monthly synthesis. Bands: -15% IPS DD limit. Drift > 5pp triggers rebalance.",
        "p1_title": "Wealth path vs. 60/40 reference",
        "p2_title": "Peak drawdown",
        "p3_title": "Asset-class breakdown vs. target",
        "p4_title": "Fees paid (cumulative, $)",
        "xlabel_months": "Months",
        "xlabel_pct": "Weight (%)",
        "ylabel_value": "Wealth ($1 base)",
        "ylabel_dd": "Drawdown (%)",
        "ylabel_dollar": "Cumulative fees ($)",
        "lab_yours": "Your portfolio", "lab_ref": "60/40 reference",
        "lab_target": "Target", "lab_actual": "Actual",
        "lab_terminal": "Terminal", "lab_worst": "Worst",
        "lab_ips_band": "IPS band",
        "lab_total_fees": "Total",
        "sleeve_equity": "Equity", "sleeve_income": "Income",
        "sleeve_gold": "Gold", "sleeve_btc": "BTC",
        "sleeve_cta": "CTA", "sleeve_tail": "Tail hedge", "sleeve_cash": "Cash",
    },
    "hk": {
        "title": "每月組合儀表板 -- 4 板塊、單頁",
        "subtitle": "試算表該顯示的內容:財富、回撤、偏離、費用。(Side 24)",
        "footer": "示意 L4 組合,5 年月度合成。邊界:IPS 回撤上限 -15%。偏離 > 5pp 觸發再平衡。",
        "p1_title": "財富路徑 vs 60/40 基準",
        "p2_title": "峰值回撤",
        "p3_title": "資產類別配置 vs 目標",
        "p4_title": "已付費用(累計,美元)",
        "xlabel_months": "月份",
        "xlabel_pct": "權重(%)",
        "ylabel_value": "財富(\\$1 起點)",
        "ylabel_dd": "回撤(%)",
        "ylabel_dollar": "累計費用(\\$)",
        "lab_yours": "你的組合", "lab_ref": "60/40 基準",
        "lab_target": "目標", "lab_actual": "實際",
        "lab_terminal": "終值", "lab_worst": "最差",
        "lab_ips_band": "IPS 帶",
        "lab_total_fees": "合共",
        "sleeve_equity": "股票", "sleeve_income": "收益",
        "sleeve_gold": "黃金", "sleeve_btc": "比特幣",
        "sleeve_cta": "CTA", "sleeve_tail": "尾部對沖", "sleeve_cash": "現金",
    },
    "tw": {
        "title": "每月組合儀表板 -- 4 區塊、單頁",
        "subtitle": "試算表該顯示的內容:財富、回檔、偏離、費用。(Side 24)",
        "footer": "示意 L4 組合,5 年月度合成。邊界:IPS 回檔上限 -15%。偏離 > 5pp 觸發再平衡。",
        "p1_title": "財富路徑 vs 60/40 基準",
        "p2_title": "峰值回檔",
        "p3_title": "資產類別配置 vs 目標",
        "p4_title": "已付費用(累計,美元)",
        "xlabel_months": "月份",
        "xlabel_pct": "權重(%)",
        "ylabel_value": "財富(\\$1 起點)",
        "ylabel_dd": "回檔(%)",
        "ylabel_dollar": "累計費用(\\$)",
        "lab_yours": "你的組合", "lab_ref": "60/40 基準",
        "lab_target": "目標", "lab_actual": "實際",
        "lab_terminal": "終值", "lab_worst": "最差",
        "lab_ips_band": "IPS 帶",
        "lab_total_fees": "合計",
        "sleeve_equity": "股票", "sleeve_income": "收益",
        "sleeve_gold": "黃金", "sleeve_btc": "比特幣",
        "sleeve_cta": "CTA", "sleeve_tail": "尾部避險", "sleeve_cash": "現金",
    },
    "cn": {
        "title": "每月组合仪表板 -- 4 板块、单页",
        "subtitle": "电子表格该显示的内容:财富、回撤、偏离、费用。(Side 24)",
        "footer": "示意 L4 组合,5 年月度合成。边界:IPS 回撤上限 -15%。偏离 > 5pp 触发再平衡。",
        "p1_title": "财富路径 vs 60/40 基准",
        "p2_title": "峰值回撤",
        "p3_title": "资产类别配置 vs 目标",
        "p4_title": "已付费用(累计,美元)",
        "xlabel_months": "月份",
        "xlabel_pct": "权重(%)",
        "ylabel_value": "财富(\\$1 起点)",
        "ylabel_dd": "回撤(%)",
        "ylabel_dollar": "累计费用(\\$)",
        "lab_yours": "你的组合", "lab_ref": "60/40 基准",
        "lab_target": "目标", "lab_actual": "实际",
        "lab_terminal": "终值", "lab_worst": "最差",
        "lab_ips_band": "IPS 带",
        "lab_total_fees": "合计",
        "sleeve_equity": "股票", "sleeve_income": "收益",
        "sleeve_gold": "黄金", "sleeve_btc": "比特币",
        "sleeve_cta": "CTA", "sleeve_tail": "尾部对冲", "sleeve_cash": "现金",
    },
}


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pp in paths:
        print(f"wrote {pp}")
