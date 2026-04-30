"""Side 02, S2.2 - Visual diagram of a 10-K table of contents.

Four-part skeleton (Parts I-IV) with each numbered Item shown as a
labelled row. The 8 items that matter most for an investor are
highlighted in gold.

Run:
    uv run python course/image/side02_10k_anatomy.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side02_10k_anatomy"


# Items most worth reading -- highlighted gold.
GOLD_ITEMS = {"Item 1", "Item 1A", "Item 3", "Item 7", "Item 8a", "Item 8b", "Item 8c", "Item 8d"}


LANG_STRINGS = {
    "en": {
        "title":    "Anatomy of a 10-K",
        "subtitle": "Four parts, fifteen items. The eight items in gold are the only ones you need to read carefully.",
        "footer":   "8 of 15 items = 45-min read for a familiar company, 2 hours for a new one.",
        "parts": [
            ("PART I",   "The Business", [
                ("Item 1",  "Business -- segments, customers, competition"),
                ("Item 1A", "Risk Factors -- first three + what is new"),
                ("Item 1B", "Unresolved Staff Comments"),
                ("Item 2",  "Properties"),
                ("Item 3",  "Legal Proceedings -- read every numeric range"),
                ("Item 4",  "Mine Safety Disclosures"),
            ]),
            ("PART II",  "The Financials", [
                ("Item 5",  "Market for Common Equity, Buybacks"),
                ("Item 7",  "MD&A -- non-GAAP reconciliations"),
                ("Item 7A", "Quantitative Market Risk"),
                ("Item 8a", "Income Statement"),
                ("Item 8b", "Cash Flow Statement"),
                ("Item 8c", "Notes -- Debt"),
                ("Item 8d", "Notes -- Subsequent Events"),
                ("Item 9A", "Controls -- look for 'material weakness'"),
            ]),
            ("PART III", "Governance", [
                ("Item 10", "Directors and Executive Officers"),
                ("Item 11", "Executive Compensation"),
                ("Item 12", "Beneficial Ownership"),
                ("Item 13", "Related-Party Transactions"),
                ("Item 14", "Auditor Fees"),
            ]),
            ("PART IV",  "Exhibits", [
                ("Item 15", "Exhibits -- contracts, debt agreements, certifications"),
            ]),
        ],
        "legend_gold": "Read first",
        "legend_grey": "Skim or skip",
    },
    "hk": {
        "title":    "10-K 文件結構",
        "subtitle": "四部分、十五項。金色高亮的八項才是真正需要細讀的部分。",
        "footer":   "15 項中 8 項 = 熟悉公司 45 分鐘、新公司 2 小時。",
        "parts": [
            ("第一部分", "業務", [
                ("項目 1",  "業務 -- 分部、客戶、競爭"),
                ("項目 1A", "風險因素 -- 前三項 + 新增項"),
                ("項目 1B", "SEC 未解決意見"),
                ("項目 2",  "物業"),
                ("項目 3",  "法律訴訟 -- 留意金額區間"),
                ("項目 4",  "礦場安全披露"),
            ]),
            ("第二部分", "財務", [
                ("項目 5",  "股票市場、回購"),
                ("項目 7",  "MD&A -- 非 GAAP 對賬"),
                ("項目 7A", "市場風險量化披露"),
                ("項目 8a", "損益表"),
                ("項目 8b", "現金流量表"),
                ("項目 8c", "附註 -- 債務"),
                ("項目 8d", "附註 -- 後續事項"),
                ("項目 9A", "內控 -- 留意「重大缺陷」"),
            ]),
            ("第三部分", "公司治理", [
                ("項目 10", "董事及高管"),
                ("項目 11", "高管薪酬"),
                ("項目 12", "持股情況"),
                ("項目 13", "關聯交易"),
                ("項目 14", "核數師費用"),
            ]),
            ("第四部分", "附件", [
                ("項目 15", "附件 -- 合約、債務協議、簽署證明"),
            ]),
        ],
        "legend_gold": "優先閱讀",
        "legend_grey": "略讀或跳過",
    },
    "tw": {
        "title":    "10-K 文件結構",
        "subtitle": "四部分、十五項。金色標示的八項才是真正需要細讀的部分。",
        "footer":   "15 項中 8 項 = 熟悉公司 45 分鐘、新公司 2 小時。",
        "parts": [
            ("第一部分", "業務", [
                ("項目 1",  "業務 -- 分部、客戶、競爭"),
                ("項目 1A", "風險因素 -- 前三項 + 新增項"),
                ("項目 1B", "SEC 未解決意見"),
                ("項目 2",  "資產"),
                ("項目 3",  "法律訴訟 -- 留意金額區間"),
                ("項目 4",  "礦場安全披露"),
            ]),
            ("第二部分", "財務", [
                ("項目 5",  "股票市場、回購"),
                ("項目 7",  "MD&A -- 非 GAAP 對帳"),
                ("項目 7A", "市場風險量化披露"),
                ("項目 8a", "損益表"),
                ("項目 8b", "現金流量表"),
                ("項目 8c", "附註 -- 債務"),
                ("項目 8d", "附註 -- 後續事項"),
                ("項目 9A", "內控 -- 留意「重大缺陷」"),
            ]),
            ("第三部分", "公司治理", [
                ("項目 10", "董事及高階主管"),
                ("項目 11", "高階主管薪酬"),
                ("項目 12", "持股情況"),
                ("項目 13", "關係人交易"),
                ("項目 14", "簽證會計師費用"),
            ]),
            ("第四部分", "附件", [
                ("項目 15", "附件 -- 合約、債務協議、簽署證明"),
            ]),
        ],
        "legend_gold": "優先閱讀",
        "legend_grey": "略讀或跳過",
    },
    "cn": {
        "title":    "10-K 文件结构",
        "subtitle": "四部分、十五项。金色高亮的八项才是真正需要细读的部分。",
        "footer":   "15 项中 8 项 = 熟悉公司 45 分钟、新公司 2 小时。",
        "parts": [
            ("第一部分", "业务", [
                ("项目 1",  "业务 -- 分部、客户、竞争"),
                ("项目 1A", "风险因素 -- 前三项 + 新增项"),
                ("项目 1B", "SEC 未解决意见"),
                ("项目 2",  "资产"),
                ("项目 3",  "法律诉讼 -- 留意金额区间"),
                ("项目 4",  "矿场安全披露"),
            ]),
            ("第二部分", "财务", [
                ("项目 5",  "股票市场、回购"),
                ("项目 7",  "MD&A -- 非 GAAP 对账"),
                ("项目 7A", "市场风险量化披露"),
                ("项目 8a", "损益表"),
                ("项目 8b", "现金流量表"),
                ("项目 8c", "附注 -- 债务"),
                ("项目 8d", "附注 -- 后续事项"),
                ("项目 9A", "内控 -- 留意「重大缺陷」"),
            ]),
            ("第三部分", "公司治理", [
                ("项目 10", "董事及高管"),
                ("项目 11", "高管薪酬"),
                ("项目 12", "持股情况"),
                ("项目 13", "关联交易"),
                ("项目 14", "审计师费用"),
            ]),
            ("第四部分", "附件", [
                ("项目 15", "附件 -- 合同、债务协议、签署证明"),
            ]),
        ],
        "legend_gold": "优先阅读",
        "legend_grey": "略读或跳过",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.5, 8.0), dpi=150)
    style_axes(ax, p)

    # Two-column layout: Part I + Part II on the left, Parts III + IV on the right.
    layout = [(0, 0, 1), (1, 0, 1), (2, 1, 1), (3, 1, 1)]

    # We need to compute y positions per column independently.
    col_y = {0: 0.97, 1: 0.97}
    part_colors = [p["blue"], p["green"], p["purple"], p["accent"]]

    for idx, (part_idx, col, _) in enumerate(layout):
        part_label, part_name, items = s["parts"][part_idx]
        x_left = 0.03 if col == 0 else 0.53
        x_right = x_left + 0.44

        # Part header strip
        y_top = col_y[col]
        header = FancyBboxPatch(
            (x_left, y_top - 0.045), x_right - x_left, 0.045,
            boxstyle="round,pad=0.002,rounding_size=0.008",
            facecolor=part_colors[part_idx], edgecolor="none",
            transform=ax.transAxes, zorder=2,
        )
        ax.add_patch(header)
        ax.text(x_left + 0.01, y_top - 0.022, part_label,
                ha="left", va="center", fontsize=11, fontweight="bold",
                color="white", transform=ax.transAxes, zorder=3)
        ax.text(x_right - 0.01, y_top - 0.022, part_name,
                ha="right", va="center", fontsize=10.5, fontstyle="italic",
                color="white", transform=ax.transAxes, zorder=3)

        y = y_top - 0.045
        for item_id, item_desc in items:
            y -= 0.043
            is_gold = item_id.replace(" ", "") in {x.replace(" ", "") for x in GOLD_ITEMS}
            face = "#fff5cc" if is_gold else p["bg"]
            edge = p["accent"] if is_gold else p["grid"]
            box = Rectangle(
                (x_left, y), x_right - x_left, 0.040,
                facecolor=face, edgecolor=edge, linewidth=1.0 if is_gold else 0.6,
                transform=ax.transAxes, zorder=2,
            )
            ax.add_patch(box)
            ax.text(x_left + 0.012, y + 0.020, item_id,
                    ha="left", va="center",
                    fontsize=9.5, fontweight="bold",
                    color=p["accent"] if is_gold else p["fg"],
                    transform=ax.transAxes, zorder=3)
            ax.text(x_left + 0.085, y + 0.020, item_desc,
                    ha="left", va="center",
                    fontsize=8.8,
                    color=p["fg"] if is_gold else p["muted"],
                    transform=ax.transAxes, zorder=3)
        col_y[col] = y - 0.025

    # Legend
    leg_y = 0.06
    leg_x = 0.03
    swatch1 = Rectangle((leg_x, leg_y), 0.022, 0.022,
                        facecolor="#fff5cc", edgecolor=p["accent"], linewidth=1.0,
                        transform=ax.transAxes, zorder=3)
    ax.add_patch(swatch1)
    ax.text(leg_x + 0.030, leg_y + 0.011, s["legend_gold"],
            ha="left", va="center", fontsize=9.5, color=p["fg"],
            fontweight="bold", transform=ax.transAxes, zorder=3)

    swatch2 = Rectangle((leg_x + 0.18, leg_y), 0.022, 0.022,
                        facecolor=p["bg"], edgecolor=p["grid"], linewidth=0.6,
                        transform=ax.transAxes, zorder=3)
    ax.add_patch(swatch2)
    ax.text(leg_x + 0.18 + 0.030, leg_y + 0.011, s["legend_grey"],
            ha="left", va="center", fontsize=9.5, color=p["muted"],
            transform=ax.transAxes, zorder=3)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ("left", "right", "top", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.grid(False)

    fig.suptitle(s["title"], fontsize=15, fontweight="bold", y=0.985)
    fig.text(0.5, 0.945, s["subtitle"], ha="center",
             fontsize=10.5, color=p["muted"], style="italic")
    fig.text(0.5, 0.022, s["footer"], ha="center",
             fontsize=9.5, color=p["muted"], style="italic")
    fig.tight_layout(rect=[0, 0.04, 1, 0.93])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    print(f"Wrote {BASE}_*.png to {OUT_DIR}")
