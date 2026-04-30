"""Side 03, sec 2.1 -- ETF creation and redemption schematic.

A non-data flow diagram. Three column stations -- Authorized
Participant, ETF Sponsor, Open Exchange -- with the underlying
basket of stocks at far left. Solid blue arrows depict the
creation cycle (basket -> sponsor -> ETF shares -> exchange);
dashed red arrows depict redemption (the reverse). An iNAV
ticker box sits above the sponsor with the 15-second cadence.

Run:
    uv run python course/image/side03_creation_redemption.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side03_creation_redemption"


LANG_STRINGS = {
    "en": {
        "title": "How an ETF Is Created and Redeemed",
        "subtitle": "Authorized Participants arbitrage premiums and discounts via in-kind transfers; iNAV publishes every 15 seconds.",
        "basket": "Basket of\nUnderlying\nStocks",
        "ap": "Authorized\nParticipant\n(Goldman, Citadel,\nVirtu, Jane St)",
        "sponsor": "ETF Sponsor\n(Vanguard,\nBlackRock,\nState St)",
        "exchange": "Open Exchange\n(NYSE Arca,\nNasdaq, Cboe)",
        "creation_lbl": "CREATION (price > NAV)",
        "redemption_lbl": "REDEMPTION (price < NAV)",
        "step_basket": "1. Buy basket on\nopen market",
        "step_deliver": "2. Deliver basket\nin kind",
        "step_issue": "3. Issue creation\nunit (25k-100k\nETF shares)",
        "step_sell": "4. Sell ETF shares\nat the premium",
        "rstep_buy": "1. Buy ETF cheap\non exchange",
        "rstep_return": "2. Return ETF shares",
        "rstep_basket": "3. Receive basket\nin kind",
        "rstep_sell": "4. Sell basket at\nfair value",
        "inav": "iNAV\nticker\n(every 15s)",
        "footnote": "In-kind transfers are not taxable sales (IRC sec 852(b)(6)) -- gains leave the fund without triggering distributions.",
    },
    "hk": {
        "title": "ETF 創設與贖回流程",
        "subtitle": "授權參與者透過實物交收套利溢價/折讓;iNAV 每 15 秒發佈。",
        "basket": "底層\n股票籃",
        "ap": "授權參與者\n(高盛、Citadel\nVirtu、Jane St)",
        "sponsor": "ETF 發行商\n(Vanguard、\nBlackRock、\nState St)",
        "exchange": "公開交易所\n(NYSE Arca、\nNasdaq、Cboe)",
        "creation_lbl": "創設(價格 > NAV)",
        "redemption_lbl": "贖回(價格 < NAV)",
        "step_basket": "1. 在公開市場\n買入股票籃",
        "step_deliver": "2. 實物交付\n股票籃",
        "step_issue": "3. 發行創設單位\n(2.5 萬-10 萬\nETF 股)",
        "step_sell": "4. 在溢價水平\n賣出 ETF 股",
        "rstep_buy": "1. 在交易所\n低價買入 ETF",
        "rstep_return": "2. 退回 ETF 股",
        "rstep_basket": "3. 實物收回\n股票籃",
        "rstep_sell": "4. 按公允價值\n賣出股票籃",
        "inav": "iNAV\n報價\n(每 15 秒)",
        "footnote": "實物交收非應課稅出售(美國稅法 852(b)(6))-- 資本利得無聲離開基金,不觸發分派。",
    },
    "tw": {
        "title": "ETF 申購與贖回流程",
        "subtitle": "授權參與者透過實物交收套利溢價/折價;iNAV 每 15 秒發佈。",
        "basket": "底層\n股票籃",
        "ap": "授權參與者\n(高盛、Citadel\nVirtu、Jane St)",
        "sponsor": "ETF 發行商\n(Vanguard、\nBlackRock、\nState St)",
        "exchange": "公開交易所\n(NYSE Arca、\nNasdaq、Cboe)",
        "creation_lbl": "申購(價格 > NAV)",
        "redemption_lbl": "贖回(價格 < NAV)",
        "step_basket": "1. 在公開市場\n買入股票籃",
        "step_deliver": "2. 實物交付\n股票籃",
        "step_issue": "3. 發行申購單位\n(2.5 萬-10 萬\nETF 股)",
        "step_sell": "4. 在溢價水平\n賣出 ETF 股",
        "rstep_buy": "1. 在交易所\n低價買入 ETF",
        "rstep_return": "2. 退回 ETF 股",
        "rstep_basket": "3. 實物收回\n股票籃",
        "rstep_sell": "4. 按公允價值\n賣出股票籃",
        "inav": "iNAV\n報價\n(每 15 秒)",
        "footnote": "實物交收非應稅出售(美國稅法 852(b)(6))-- 資本利得無聲離開基金,不觸發配息。",
    },
    "cn": {
        "title": "ETF 申购与赎回流程",
        "subtitle": "授权参与者通过实物交收套利溢价/折价;iNAV 每 15 秒发布。",
        "basket": "底层\n股票篮",
        "ap": "授权参与者\n(高盛、Citadel\nVirtu、Jane St)",
        "sponsor": "ETF 发行商\n(Vanguard、\nBlackRock、\nState St)",
        "exchange": "公开交易所\n(NYSE Arca、\nNasdaq、Cboe)",
        "creation_lbl": "申购(价格 > NAV)",
        "redemption_lbl": "赎回(价格 < NAV)",
        "step_basket": "1. 在公开市场\n买入股票篮",
        "step_deliver": "2. 实物交付\n股票篮",
        "step_issue": "3. 发行申购单位\n(2.5 万-10 万\nETF 股)",
        "step_sell": "4. 在溢价水平\n卖出 ETF 股",
        "rstep_buy": "1. 在交易所\n低价买入 ETF",
        "rstep_return": "2. 退回 ETF 股",
        "rstep_basket": "3. 实物收回\n股票篮",
        "rstep_sell": "4. 按公允价值\n卖出股票篮",
        "inav": "iNAV\n报价\n(每 15 秒)",
        "footnote": "实物交收非应税出售(美国税法 852(b)(6))-- 资本利得无声离开基金,不触发分配。",
    },
}


def _box(ax, x, y, w, h, label, face, edge, text_color="#1a2332", fontsize=10.5, weight="bold"):
    p = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=face, edgecolor=edge, linewidth=1.5,
    )
    ax.add_patch(p)
    ax.text(x, y, label, ha="center", va="center",
            fontsize=fontsize, color=text_color, weight=weight)


def build_fig(s):
    P = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(12.4, 7.0), dpi=150)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.set_facecolor(P["bg"])
    fig.patch.set_facecolor(P["bg"])
    ax.set_axis_off()

    # Stations -- 4 columns: basket, AP, sponsor, exchange
    cx_basket   = 1.4
    cx_ap       = 4.2
    cx_sponsor  = 7.6
    cx_exchange = 10.8
    y_top    = 5.2   # creation row
    y_bot    = 2.4   # redemption row
    y_centre = 3.8
    box_w    = 2.2
    box_h    = 1.55

    # Boxes (centre-row tall stations)
    _box(ax, cx_basket,   y_centre, box_w, 1.9, s["basket"],   "#fff8e1", P["accent"], fontsize=10.5)
    _box(ax, cx_ap,       y_centre, box_w, 1.9, s["ap"],       "#e3f2fd", P["blue"],   fontsize=10)
    _box(ax, cx_sponsor,  y_centre, box_w, 1.9, s["sponsor"],  "#e8f5e9", P["green"],  fontsize=10)
    _box(ax, cx_exchange, y_centre, box_w, 1.9, s["exchange"], "#fce4ec", P["purple"], fontsize=10)

    # iNAV ticker box above sponsor
    _box(ax, cx_sponsor, 6.45, 1.7, 0.9, s["inav"], "#fff", P["red"],
         text_color=P["red"], fontsize=9.5, weight="bold")
    ax.annotate("", xy=(cx_sponsor, 4.8), xytext=(cx_sponsor, 6.0),
                arrowprops=dict(arrowstyle="->", color=P["red"], lw=1.0,
                                linestyle=(0, (2, 2))))

    # Creation arrows (top, blue, solid) -- left to right then back to exchange
    def arrow(x0, y0, x1, y1, color, ls="-", rad=0.0, lw=2.2):
        a = FancyArrowPatch((x0, y0), (x1, y1),
                            arrowstyle="-|>", mutation_scale=18,
                            color=color, lw=lw, linestyle=ls,
                            connectionstyle=f"arc3,rad={rad}")
        ax.add_patch(a)

    # Creation flow (solid blue, slightly above centre)
    yC = y_centre + 0.15
    arrow(cx_basket + 1.1,   yC + 0.55, cx_ap - 1.1,       yC + 0.55, P["blue"], "-", 0.18)
    arrow(cx_ap + 1.1,       yC + 0.55, cx_sponsor - 1.1,  yC + 0.55, P["blue"], "-", 0.18)
    arrow(cx_sponsor + 1.1,  yC + 0.55, cx_exchange - 1.1, yC + 0.55, P["blue"], "-", 0.18)

    # Redemption flow (dashed red, slightly below centre, right -> left)
    yR = y_centre - 0.15
    arrow(cx_exchange - 1.1, yR - 0.55, cx_sponsor + 1.1,  yR - 0.55, P["red"], (0, (4, 3)), -0.18)
    arrow(cx_sponsor - 1.1,  yR - 0.55, cx_ap + 1.1,       yR - 0.55, P["red"], (0, (4, 3)), -0.18)
    arrow(cx_ap - 1.1,       yR - 0.55, cx_basket + 1.1,   yR - 0.55, P["red"], (0, (4, 3)), -0.18)

    # Step labels
    def step(xa, xb, y, txt, color):
        ax.text((xa + xb) / 2, y, txt, ha="center", va="center",
                fontsize=8.5, color=color, weight="bold",
                bbox=dict(boxstyle="round,pad=0.25", facecolor=P["bg"],
                          edgecolor="none", alpha=0.85))

    step(cx_basket, cx_ap,       yC + 1.1, s["step_basket"],   P["blue"])
    step(cx_ap, cx_sponsor,      yC + 1.1, s["step_deliver"],  P["blue"])
    step(cx_sponsor, cx_exchange,yC + 1.1, s["step_issue"],    P["blue"])
    ax.text(cx_exchange, yC + 1.55, s["step_sell"], ha="center", va="center",
            fontsize=8.5, color=P["blue"], weight="bold",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=P["bg"],
                      edgecolor="none", alpha=0.85))

    step(cx_exchange, cx_sponsor, yR - 1.1, s["rstep_buy"],    P["red"])
    step(cx_sponsor, cx_ap,       yR - 1.1, s["rstep_return"], P["red"])
    step(cx_ap, cx_basket,        yR - 1.1, s["rstep_basket"], P["red"])
    ax.text(cx_basket, yR - 1.55, s["rstep_sell"], ha="center", va="center",
            fontsize=8.5, color=P["red"], weight="bold",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=P["bg"],
                      edgecolor="none", alpha=0.85))

    # Cycle labels
    ax.text(0.4, 6.4, s["creation_lbl"], ha="left", va="center",
            fontsize=11, color=P["blue"], weight="bold")
    ax.text(0.4, 1.2, s["redemption_lbl"], ha="left", va="center",
            fontsize=11, color=P["red"], weight="bold")

    # Title + subtitle + footnote
    fig.suptitle(s["title"], fontsize=15.5, weight="bold",
                 color=P["fg"], y=0.97)
    fig.text(0.5, 0.915, s["subtitle"], ha="center",
             fontsize=10.2, color=P["muted"], style="italic")
    fig.text(0.5, 0.04, s["footnote"], ha="center",
             fontsize=9.0, color=P["muted"])

    fig.tight_layout(rect=[0.0, 0.06, 1.0, 0.90])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_(en|hk|tw|cn).png and {BASE}.png")
