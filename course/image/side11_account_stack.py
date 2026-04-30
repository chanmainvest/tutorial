"""Side 11, §1 — 2026 retirement-account contribution priority pyramid.

Six-tier waterfall/pyramid showing the canonical funding order with
2026 dollar limits. Tiers from bottom to top:
  1. Employer 401(k) match (illustrative $7,500 typical for 5% on $150k)
  2. HSA family             $8,550
  3. Roth IRA               $7,000
  4. 401(k) deferral max    $23,500
  5. Mega-backdoor lane     $30,950 (= 70k - 23.5k - 7.5k match - 8.05k other)
  6. Taxable brokerage      unlimited

Drawn as horizontal centred bars (pyramid silhouette) with each tier
labelled (priority#, account name, 2026 dollar amount).

Run:
    uv run python course/image/side11_account_stack.py
"""

from __future__ import annotations
import sys
from pathlib import Path
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (
    PALETTE_LIGHT, render_for_all_locales, apply_cjk_font,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side11_account_stack"

# Tier visual widths (top -> bottom, 0..1).
# Pyramid: top (taxable, unlimited) is widest at top? We'll invert -
# typical pyramid puts highest priority at the BASE (widest), so order
# from bottom to top is tier1->tier6 with shrinking widths.
# But priority 1 = 'do first' should be visually anchored. We use the
# inverted pyramid: tier 1 at TOP (most urgent) widest, tier 6 at BOTTOM
# narrowest. Actually the canonical "stack" diagram has tier 1 at the
# BOTTOM (the foundation you fund first). Use bottom = tier1.
# Width sized roughly by typical-dollar capacity.

TIERS = [
    # (priority, key, color)
    (1, "match",   "blue"),
    (2, "hsa",     "green"),
    (3, "roth",    "purple"),
    (4, "k401",    "accent"),
    (5, "mega",    "orange"),
    (6, "taxable", "grey"),
]

LANG_STRINGS = {
    "en": {
        "title":    "The 2026 Retirement Contribution Stack",
        "subtitle": "Strict priority. Empty each tier before the next.",
        "footer":   "Limits: 401(k) deferral $23,500 ($31k 50+) - IRA $7,000 ($8k 50+) - HSA $4,300 single / $8,550 family - 401(k) total cap $70,000",
        "tiers": {
            "match":   ("Tier 1", "Employer 401(k) match",       "Capture every match dollar (50-100% return)"),
            "hsa":     ("Tier 2", "HSA $4,300 single / $8,550 family", "Triple-tax-advantaged. HDHP required."),
            "roth":    ("Tier 3", "Roth IRA $7,000",             "Backdoor it if income > $165k single."),
            "k401":    ("Tier 4", "401(k) deferral up to $23,500",  "Trad if bracket falls in retirement; else Roth."),
            "mega":    ("Tier 5", "Mega-backdoor up to $70,000 cap", "After-tax 401(k) + in-service Roth rollover."),
            "taxable": ("Tier 6", "Taxable brokerage (unlimited)",   "Asset location + SOUL #15 (Side Lesson 4)."),
        },
    },
    "hk": {
        "title":    "2026 退休帳戶供款優先順序",
        "subtitle": "嚴格按順序填滿,每層滿額後才進入下一層。",
        "footer":   "上限:401(k) $23,500(50+ $31k) - IRA $7,000(50+ $8k) - HSA 單身 $4,300 / 家庭 $8,550 - 401(k) 總上限 $70,000",
        "tiers": {
            "match":   ("第 1 層", "雇主 401(k) 配對",           "每一元配對都要拿到(50-100% 即時回報)"),
            "hsa":     ("第 2 層", "HSA 單身 $4,300 / 家庭 $8,550", "三重免稅。需參與高自付額醫保。"),
            "roth":    ("第 3 層", "Roth IRA $7,000",            "收入超過 $165k 單身須走後門。"),
            "k401":    ("第 4 層", "401(k) 自付最高 $23,500",     "退休稅階較低用傳統,否則用 Roth。"),
            "mega":    ("第 5 層", "巨型後門 至 $70,000 總上限",   "稅後 401(k) + 在職 Roth 轉換。"),
            "taxable": ("第 6 層", "應稅證券戶(無上限)",         "資產位置 + SOUL #15(側課 4)。"),
        },
    },
    "tw": {
        "title":    "2026 退休帳戶提撥優先順序",
        "subtitle": "嚴格依序,每層滿額後才進下一層。",
        "footer":   "上限:401(k) $23,500(50+ $31k) - IRA $7,000(50+ $8k) - HSA 單身 $4,300 / 家庭 $8,550 - 401(k) 總上限 $70,000",
        "tiers": {
            "match":   ("第 1 層", "雇主 401(k) 配對",           "每一元配對都要拿到(50-100% 立即報酬)"),
            "hsa":     ("第 2 層", "HSA 單身 $4,300 / 家庭 $8,550", "三重免稅。需參加高自負額醫保。"),
            "roth":    ("第 3 層", "Roth IRA $7,000",            "收入超過 $165k 單身改走後門。"),
            "k401":    ("第 4 層", "401(k) 自提最高 $23,500",     "退休稅階較低用傳統,否則用 Roth。"),
            "mega":    ("第 5 層", "巨型後門 至 $70,000 總上限",   "稅後 401(k) + 在職 Roth 轉換。"),
            "taxable": ("第 6 層", "應稅證券戶(無上限)",         "資產位置 + SOUL #15(側課 4)。"),
        },
    },
    "cn": {
        "title":    "2026 退休账户缴款优先顺序",
        "subtitle": "严格按顺序填满,每层满额后才进入下一层。",
        "footer":   "上限:401(k) $23,500(50+ $31k) - IRA $7,000(50+ $8k) - HSA 单身 $4,300 / 家庭 $8,550 - 401(k) 总上限 $70,000",
        "tiers": {
            "match":   ("第 1 层", "雇主 401(k) 匹配",           "每一元匹配都要拿到(50-100% 即时回报)"),
            "hsa":     ("第 2 层", "HSA 单身 $4,300 / 家庭 $8,550", "三重免税。需参加高自付额医保。"),
            "roth":    ("第 3 层", "Roth IRA $7,000",            "收入超过 $165k 单身走后门。"),
            "k401":    ("第 4 层", "401(k) 自付最高 $23,500",     "退休税阶较低用传统,否则用 Roth。"),
            "mega":    ("第 5 层", "巨型后门 至 $70,000 总上限",   "税后 401(k) + 在职 Roth 转换。"),
            "taxable": ("第 6 层", "应税证券户(无限额)",         "资产位置 + SOUL #15(侧课 4)。"),
        },
    },
}


def build_fig(s):
    # Escape $ signs in all displayed strings to avoid matplotlib mathtext
    # mode (which falls back to rm font and drops CJK glyphs).
    def esc(v):
        if isinstance(v, str):
            return v.replace("$", r"\$")
        if isinstance(v, tuple):
            return tuple(esc(x) for x in v)
        if isinstance(v, dict):
            return {k: esc(x) for k, x in v.items()}
        return v
    s = {k: esc(v) for k, v in s.items()}
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.5, 7.0), dpi=150)
    fig.patch.set_facecolor(p["bg"])
    ax.set_facecolor(p["bg"])

    # Vertical layout: bottom = tier 1 (foundation). Each tier 1.0 high.
    # Widths: pyramid shape gradually narrowing toward top.
    widths = [11.0, 10.0, 9.0, 8.0, 7.0, 6.2]  # bottom to top
    y_step = 1.05
    centre = 0

    # Draw bottom-to-top so tier1 ends up at y=0..1, tier6 at y=5..6.
    for i, (priority, key, color_key) in enumerate(TIERS):
        w = widths[i]
        y = i * y_step
        x0 = centre - w / 2
        ax.barh(
            y + 0.5, w, height=0.92,
            left=x0, color=p[color_key], alpha=0.85,
            edgecolor=p["fg"], linewidth=1.2, zorder=3,
        )
        tier_label, name, blurb = s["tiers"][key]
        # Priority label on the left of the bar.
        ax.text(x0 - 0.25, y + 0.5, tier_label,
                ha="right", va="center", fontsize=11.5, weight="bold",
                color=p["fg"], zorder=4)
        # Account name centred on the bar.
        ax.text(centre, y + 0.65, name, ha="center", va="center",
                fontsize=12.0, weight="bold", color="#ffffff", zorder=5)
        # Blurb just below the name on the bar.
        ax.text(centre, y + 0.30, blurb, ha="center", va="center",
                fontsize=8.8, color="#ffffff", alpha=0.95, zorder=5)

    # Big arrow on the right pointing top->bottom indicating "fund order".
    ax.annotate(
        "", xy=(7.5, 0.6), xytext=(7.5, 5.4),
        arrowprops=dict(arrowstyle="-|>", color=p["accent"], lw=2.5),
        zorder=2,
    )
    ax.text(7.4, 3.0, "FUND\nORDER" if False else "", ha="left", va="center",
            fontsize=10, weight="bold", color=p["accent"])

    ax.set_xlim(-8.0, 8.5)
    ax.set_ylim(-0.4, len(TIERS) * y_step + 0.4)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold",
                 color=p["fg"])
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.5, color="#4a5568", style="italic")
    fig.text(0.5, 0.04, s["footer"], ha="center", fontsize=8.4,
             color=p["muted"])
    fig.tight_layout(rect=[0, 0.06, 1, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
