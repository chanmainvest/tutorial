"""Side 30, §2.1 — The Wheel cycle flow diagram.

A schematic three-state diagram of the wheel: cash + short put -> long
shares + short call -> back to cash. Each transition is annotated with a
typical premium magnitude on a 30-delta, 30-DTE setup on AAPL @ $215.

Run:
    uv run python course/image/side30_wheel_flow.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT, apply_cjk_font, render_for_all_locales,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side30_wheel_flow"


LANG_STRINGS = {
    "en": {
        "title":    "The wheel — three states, two transitions",
        "subtitle": "Typical numbers: AAPL @ \\$215, 30-delta, 30 DTE.  Premium per contract.",
        "state_a_h":  "STATE A",
        "state_a":    "Cash + short PUT",
        "state_a_d":  "$21,500 collateral\nShort 30-delta put @ \\$210\nCollect ~\\$430 / contract",
        "state_b_h":  "STATE B",
        "state_b":    "Long 100 shares + short CALL",
        "state_b_d":  "Cost basis ~\\$205.70\nShort 30-delta call @ \\$220\nCollect ~\\$380 / contract",
        "arrow_ab":   "Put assigned\n(stock < \\$210 at expiry)\n~3x / year on AAPL",
        "arrow_ba":   "Call assigned\n(stock > \\$220 at expiry)\nshares called away",
        "loop":       "If put expires worthless,\nwrite another put.\n~9 of 12 months.",
        "footer":     "On a normal-vol underlying you spend most of the year in state A. State B is the recovery loop after assignment, not the goal.",
    },
    "hk": {
        "title":    "輪轉策略 — 三個狀態,兩個轉換",
        "subtitle": "AAPL @ \\$215,30-delta,30 天到期。每張合約權利金。",
        "state_a_h":  "狀態 A",
        "state_a":    "現金 + 賣出 PUT",
        "state_a_d":  "佔用 \\$21,500 抵押\n賣出 30-delta 賣權 @ \\$210\n收取約 \\$430 / 張",
        "state_b_h":  "狀態 B",
        "state_b":    "持有 100 股 + 賣出 CALL",
        "state_b_d":  "成本約 \\$205.70\n賣出 30-delta 買權 @ \\$220\n收取約 \\$380 / 張",
        "arrow_ab":   "賣權被指派\n(到期時股價 < \\$210)\nAAPL 每年約 3 次",
        "arrow_ba":   "買權被指派\n(到期時股價 > \\$220)\n股票被買走",
        "loop":       "若賣權到期作廢,\n再寫一張新的賣權。\n約 12 個月中 9 個月。",
        "footer":     "正常波動率的標的,大部分時間都在狀態 A。狀態 B 是被指派後的修復過程,不是目的。",
    },
    "tw": {
        "title":    "輪轉策略 — 三個狀態,兩個轉換",
        "subtitle": "AAPL @ \\$215,30-delta,30 天到期。每張合約權利金。",
        "state_a_h":  "狀態 A",
        "state_a":    "現金 + 賣出 PUT",
        "state_a_d":  "佔用 \\$21,500 擔保\n賣出 30-delta 賣權 @ \\$210\n收取約 \\$430 / 張",
        "state_b_h":  "狀態 B",
        "state_b":    "持有 100 股 + 賣出 CALL",
        "state_b_d":  "成本約 \\$205.70\n賣出 30-delta 買權 @ \\$220\n收取約 \\$380 / 張",
        "arrow_ab":   "賣權被指派\n(到期時股價 < \\$210)\nAAPL 每年約 3 次",
        "arrow_ba":   "買權被指派\n(到期時股價 > \\$220)\n股票被買走",
        "loop":       "若賣權到期作廢,\n再寫一張新的賣權。\n約 12 個月中 9 個月。",
        "footer":     "正常波動率的標的,大部分時間都在狀態 A。狀態 B 是被指派後的修復過程,不是目的。",
    },
    "cn": {
        "title":    "轮转策略 — 三个状态,两个转换",
        "subtitle": "AAPL @ \\$215,30-delta,30 天到期。每张合约权利金。",
        "state_a_h":  "状态 A",
        "state_a":    "现金 + 卖出 PUT",
        "state_a_d":  "占用 \\$21,500 抵押\n卖出 30-delta 卖权 @ \\$210\n收取约 \\$430 / 张",
        "state_b_h":  "状态 B",
        "state_b":    "持有 100 股 + 卖出 CALL",
        "state_b_d":  "成本约 \\$205.70\n卖出 30-delta 买权 @ \\$220\n收取约 \\$380 / 张",
        "arrow_ab":   "卖权被指派\n(到期时股价 < \\$210)\nAAPL 每年约 3 次",
        "arrow_ba":   "买权被指派\n(到期时股价 > \\$220)\n股票被买走",
        "loop":       "若卖权到期作废,\n再写一张新的卖权。\n约 12 个月中 9 个月。",
        "footer":     "正常波动率的标的,大部分时间都在状态 A。状态 B 是被指派后的修复过程,不是目的。",
    },
}


def _box(ax, x, y, w, h, color, fc, header, body, body_detail):
    """Draw a labelled rounded box."""
    patch = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=2.0, edgecolor=color, facecolor=fc, zorder=3,
    )
    ax.add_patch(patch)
    ax.text(x, y + h / 2 - 0.18, header, ha="center", va="center",
            fontsize=10, weight="bold", color=color, zorder=4)
    ax.text(x, y + h / 2 - 0.42, body, ha="center", va="center",
            fontsize=12, weight="bold", color="#1a2332", zorder=4)
    ax.text(x, y - 0.05, body_detail, ha="center", va="center",
            fontsize=9.0, color="#4a5568", zorder=4,
            linespacing=1.45)


def build_fig(s):
    p = PALETTE_LIGHT

    fig, ax = plt.subplots(figsize=(12.6, 6.6), dpi=150)
    ax.set_facecolor(p["bg"])
    fig.set_facecolor(p["bg"])

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.set_aspect("auto")
    ax.axis("off")

    # State A box (left)
    _box(ax, 2.6, 3.5, 4.2, 3.1, p["blue"], "#eef3fb",
         s["state_a_h"], s["state_a"], s["state_a_d"])

    # State B box (right)
    _box(ax, 9.4, 3.5, 4.2, 3.1, p["accent"], "#faf3e0",
         s["state_b_h"], s["state_b"], s["state_b_d"])

    # Arrow A -> B (top): put assigned
    arrow_ab = FancyArrowPatch(
        (4.7, 4.1), (7.3, 4.1),
        arrowstyle="-|>", mutation_scale=24,
        linewidth=2.4, color=p["red"], zorder=2,
    )
    ax.add_patch(arrow_ab)
    ax.text(6.0, 5.05, s["arrow_ab"], ha="center", va="center",
            fontsize=9.5, color=p["red"], weight="bold",
            linespacing=1.3,
            bbox=dict(boxstyle="round,pad=0.35", facecolor=p["bg"],
                      edgecolor=p["red"], linewidth=0.8))

    # Arrow B -> A (bottom): call assigned
    arrow_ba = FancyArrowPatch(
        (7.3, 2.9), (4.7, 2.9),
        arrowstyle="-|>", mutation_scale=24,
        linewidth=2.4, color=p["green"], zorder=2,
    )
    ax.add_patch(arrow_ba)
    ax.text(6.0, 1.95, s["arrow_ba"], ha="center", va="center",
            fontsize=9.5, color=p["green"], weight="bold",
            linespacing=1.3,
            bbox=dict(boxstyle="round,pad=0.35", facecolor=p["bg"],
                      edgecolor=p["green"], linewidth=0.8))

    # Self-loop on State A
    loop_arrow = FancyArrowPatch(
        (1.0, 4.7), (1.0, 2.3),
        connectionstyle="arc3,rad=-0.6",
        arrowstyle="-|>", mutation_scale=20,
        linewidth=1.8, color=p["muted"], zorder=2,
    )
    ax.add_patch(loop_arrow)
    ax.text(0.15, 3.5, s["loop"], ha="center", va="center",
            fontsize=8.5, color=p["muted"], style="italic",
            linespacing=1.3, rotation=90)

    # Title & subtitle
    fig.text(0.5, 0.95, s["title"], ha="center", fontsize=15,
             weight="bold", color="#1a2332")
    fig.text(0.5, 0.905, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.025, s["footer"], ha="center",
             fontsize=9.0, color="#4a5568", style="italic")

    fig.tight_layout(rect=[0, 0.05, 1, 0.88])
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
