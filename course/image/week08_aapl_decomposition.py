"""Week 8, §2.2 — Apple FY2024 horizontal waterfall: Revenue → FCF.

Walk Apple's FY2024 income statement and cash-flow statement as a single
left-to-right waterfall. Constants from Apple's published 10-K (FY2024,
year ended September 28, 2024):
    Revenue                  $391.0B
    Cost of revenue          $210.4B
    Gross profit             $180.7B
    Operating expenses        $57.5B (R&D 31.4 + SG&A 26.1)
    Operating income         $123.2B
    Income tax + other       $29.5B  (incl. $10B EU State-aid charge)
    Net income                $93.7B
    Non-cash + WC bridge     +$24.6B  (D&A, SBC, working-capital, deferred tax)
    Operating cash flow     $118.3B
    Capex                     $9.5B
    Free cash flow          $108.8B

Run:
    uv run python course/image/week08_aapl_decomposition.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
    style_axes,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "week08_aapl_decomposition"


# (label_key, delta_billions, kind)
# kind: "total" (anchor bar from 0), "neg" (subtraction), "pos" (addition)
STEPS = [
    ("revenue",   391.0, "total"),
    ("cogs",     -210.4, "neg"),
    ("gross",     180.7, "total"),
    ("opex",      -57.5, "neg"),
    ("opinc",     123.2, "total"),
    ("tax",       -29.5, "neg"),
    ("ni",         93.7, "total"),
    ("noncash",   +24.6, "pos"),
    ("ocf",       118.3, "total"),
    ("capex",      -9.5, "neg"),
    ("fcf",       108.8, "total"),
]


LANG_STRINGS = {
    "en": {
        "title":    "Apple FY2024: revenue to free cash flow",
        "subtitle": "Horizontal waterfall in $ billions. Source: Apple 10-K FY2024 (year ended Sep 28, 2024). FCF exceeds net income because non-cash charges and working-capital movements release cash.",
        "xlabel":   "$ billions",
        "labels":   {
            "revenue":  "Revenue",
            "cogs":     "Cost of revenue",
            "gross":    "Gross profit",
            "opex":     "Operating expenses",
            "opinc":    "Operating income",
            "tax":      "Tax + other",
            "ni":       "Net income",
            "noncash":  "D&A + SBC + WC",
            "ocf":      "Operating cash flow",
            "capex":    "Capex",
            "fcf":      "Free cash flow",
        },
        "footer":   "FCF $109B exceeds net income $94B by $15B — the cash signature of a capital-light business.",
    },
    "hk": {
        "title":    "蘋果 2024 財年:由營收走到自由現金流",
        "subtitle": "橫向瀑布圖,單位十億美元。資料:Apple FY2024 10-K(年度結束於 2024 年 9 月 28 日)。自由現金流高於淨利,因非現金費用與營運資金變動釋放現金。",
        "xlabel":   "十億美元",
        "labels":   {
            "revenue":  "營業收入",
            "cogs":     "營業成本",
            "gross":    "毛利",
            "opex":     "營業費用",
            "opinc":    "營業利益",
            "tax":      "稅項及其他",
            "ni":       "淨利",
            "noncash":  "折舊+股酬+營運資金",
            "ocf":      "經營現金流",
            "capex":    "資本開支",
            "fcf":      "自由現金流",
        },
        "footer":   "自由現金流 1090 億美元高於淨利 940 億約 150 億 — 輕資產業務的現金特徵。",
    },
    "tw": {
        "title":    "蘋果 2024 會計年度:由營收走到自由現金流",
        "subtitle": "水平瀑布圖,單位十億美元。資料:Apple FY2024 10-K(年度結束於 2024 年 9 月 28 日)。自由現金流高於淨利,因非現金費用與營運資金變動釋出現金。",
        "xlabel":   "十億美元",
        "labels":   {
            "revenue":  "營業收入",
            "cogs":     "營業成本",
            "gross":    "毛利",
            "opex":     "營業費用",
            "opinc":    "營業利益",
            "tax":      "稅費及其他",
            "ni":       "淨利",
            "noncash":  "折舊+股酬+營運資金",
            "ocf":      "營運現金流",
            "capex":    "資本支出",
            "fcf":      "自由現金流",
        },
        "footer":   "自由現金流 1090 億美元高於淨利 940 億約 150 億 — 輕資產企業的現金特徵。",
    },
    "cn": {
        "title":    "苹果 2024 财年:从营收走到自由现金流",
        "subtitle": "横向瀑布图,单位十亿美元。资料:Apple FY2024 10-K(年度结束于 2024 年 9 月 28 日)。自由现金流高于净利,因非现金费用与营运资金变动释放现金。",
        "xlabel":   "十亿美元",
        "labels":   {
            "revenue":  "营业收入",
            "cogs":     "营业成本",
            "gross":    "毛利",
            "opex":     "营业费用",
            "opinc":    "营业利益",
            "tax":      "税项及其他",
            "ni":       "净利",
            "noncash":  "折旧+股酬+营运资金",
            "ocf":      "经营现金流",
            "capex":    "资本开支",
            "fcf":      "自由现金流",
        },
        "footer":   "自由现金流 1090 亿美元高于净利 940 亿约 150 亿 — 轻资产业务的现金特征。",
    },
}


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(12, 6.6))
    style_axes(ax, p)

    labels = [s["labels"][k] for k, _, _ in STEPS]
    n = len(STEPS)
    y_positions = list(range(n, 0, -1))  # top-to-bottom waterfall

    running = 0.0
    for i, (key, delta, kind) in enumerate(STEPS):
        y = y_positions[i]
        if kind == "total":
            left = 0.0
            width = delta
            color = p["accent"] if key in ("revenue", "fcf") else p["blue"]
            running = delta
        elif kind == "neg":
            width = abs(delta)
            left = running - width
            running = running + delta  # delta negative
            color = p["red"]
        else:  # pos
            left = running
            width = delta
            running = running + delta
            color = p["green"]

        ax.barh(y, width, left=left, color=color, edgecolor=color,
                height=0.62, alpha=0.92)

        # Value label at end of bar
        if kind == "total":
            txt = f"${delta:,.1f}B"
            ax.text(delta + 5, y, txt, va="center", ha="left",
                    color=p["fg"], fontsize=10, fontweight="bold")
        else:
            sign = "-" if kind == "neg" else "+"
            txt = f"{sign}${abs(delta):,.1f}B"
            xpos = (left + width / 2)
            ax.text(xpos, y, txt, va="center", ha="center",
                    color="white", fontsize=9.5, fontweight="bold")

    # Connector lines between consecutive total bars
    last_total_x = None
    last_total_y = None
    cur = 0.0
    for i, (key, delta, kind) in enumerate(STEPS):
        y = y_positions[i]
        if kind == "total":
            cur = delta
            if last_total_x is not None:
                ax.plot([last_total_x, last_total_x], [last_total_y, y],
                        color=p["muted"], linewidth=0.7, linestyle=":")
            last_total_x = delta
            last_total_y = y
        elif kind == "neg":
            cur += delta
        else:
            cur += delta

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel(s["xlabel"])
    ax.set_xlim(0, 430)
    ax.set_title(s["title"], fontsize=14, fontweight="bold", loc="left", pad=24)
    ax.text(0, 1.02, s["subtitle"], transform=ax.transAxes,
            fontsize=9.5, color=p["muted"], wrap=True)
    ax.text(0, -0.10, s["footer"], transform=ax.transAxes,
            fontsize=9.5, color=p["accent"], fontweight="bold")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    paths = render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
    for pth in paths:
        print(f"wrote {pth}")
