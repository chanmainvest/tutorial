"""Generate the 'buy term and invest the difference' vs whole-life chart for Week 2, §2.7.

Two wealth trajectories over 20 years for a healthy 30-year-old buying
$1M of life-insurance coverage:

- **Whole-life policy**: $8,000 / year premium, all of which goes into
  the policy. Cash value grows at a net 3% / year (a typical figure
  after agent commission, surrender drag, and stacked policy fees).
- **Buy term + invest the difference**: $500 / year premium for a
  20-year level-term policy with the same $1M death benefit, plus
  $7,500 / year invested into a broad index ETF compounding at 8% / year
  net of fees.

Both strategies provide the same death benefit during the 20-year
window. The difference is what they leave you sitting on at the end.

Defaults reflect roughly real-world quotes for a healthy 30-year-old
non-smoker; numbers are illustrative, not a quote.

Run:
    uv run --with matplotlib python course/image/week02_buy_term_invest_difference.py
"""

from __future__ import annotations

import os
import shutil

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC", "PingFang SC",
    "Noto Sans CJK TC", "Noto Sans CJK SC", "SimHei", "Arial Unicode MS",
    "DejaVu Sans",
]
matplotlib.rcParams["axes.unicode_minus"] = False

LANGS = ("en", "hk", "tw", "cn")

LANG_LABELS = {
    "en": {
        "title":    "Buy term and invest the difference — beats whole-life cash value by 5x over 20 years",
        "subtitle": "$1M coverage, age 30 healthy: $8K/yr whole-life premium vs $500/yr term + $7,500/yr in an index ETF at 8%",
        "xlabel":   "Year",
        "ylabel":   "Account value (USD)",
        "whole":    "Whole-life cash value (3% net)",
        "term":     "Term + ETF investment (8% net)",
        "end_whole": "Whole-life ends:",
        "end_term":  "Term + ETF ends:",
        "gap":       "Gap:",
    },
    "hk": {
        "title":    "買定期保險 + 投資差額 — 20 年下來比終身保險現金價值多 5 倍",
        "subtitle": "100 萬美元保額,健康 30 歲:每年 8,000 美元終身保費 vs 每年 500 美元定期保險 + 7,500 美元投資指數 ETF(年回報 8%)",
        "xlabel":   "年份",
        "ylabel":   "戶口價值(美元)",
        "whole":    "終身保險現金價值(淨 3%)",
        "term":     "定期保險 + ETF 投資(淨 8%)",
        "end_whole": "終身保險結餘:",
        "end_term":  "定期 + ETF 結餘:",
        "gap":       "差距:",
    },
    "tw": {
        "title":    "買定期保險 + 投資差額 — 20 年下來比終身保險現金價值多 5 倍",
        "subtitle": "100 萬美元保額,健康 30 歲:每年 8,000 美元終身保費 vs 每年 500 美元定期保險 + 7,500 美元投資指數 ETF(年報酬 8%)",
        "xlabel":   "年份",
        "ylabel":   "帳戶價值(美元)",
        "whole":    "終身保險現金價值(淨 3%)",
        "term":     "定期保險 + ETF 投資(淨 8%)",
        "end_whole": "終身保險結餘:",
        "end_term":  "定期 + ETF 結餘:",
        "gap":       "差距:",
    },
    "cn": {
        "title":    "买定期保险 + 投资差额 — 20 年下来比终身保险现金价值多 5 倍",
        "subtitle": "100 万美元保额,健康 30 岁:每年 8,000 美元终身保费 vs 每年 500 美元定期保险 + 7,500 美元投资指数 ETF(年回报 8%)",
        "xlabel":   "年份",
        "ylabel":   "账户价值(美元)",
        "whole":    "终身保险现金价值(净 3%)",
        "term":     "定期保险 + ETF 投资(净 8%)",
        "end_whole": "终身保险结余:",
        "end_term":  "定期 + ETF 结余:",
        "gap":       "差距:",
    },
}

YEARS = list(range(0, 21))  # year 0 = before any premium
WHOLE_PREMIUM = 8_000.0     # USD/yr — typical $1M whole-life for healthy 30 yr old
TERM_PREMIUM  = 500.0       # USD/yr — typical $1M 20-yr level term, healthy 30 yr old
INVEST_DIFF   = WHOLE_PREMIUM - TERM_PREMIUM  # 7,500/yr into ETF

WHOLE_GROWTH = 0.03         # 3% net cash-value growth (after agent commission + drag)
ETF_GROWTH   = 0.08         # 8% net long-term equity return after expense ratio


def whole_life_trajectory() -> list[float]:
    """Year-by-year whole-life cash value: deposit at start of year, then grow."""
    values = [0.0]
    cv = 0.0
    for _ in YEARS[1:]:
        cv = (cv + WHOLE_PREMIUM) * (1.0 + WHOLE_GROWTH)
        values.append(cv)
    return values


def term_invest_trajectory() -> list[float]:
    """Year-by-year invested portfolio value (term premium is expensed, not invested)."""
    values = [0.0]
    pv = 0.0
    for _ in YEARS[1:]:
        pv = (pv + INVEST_DIFF) * (1.0 + ETF_GROWTH)
        values.append(pv)
    return values


def render_static_png(out_dir: str) -> None:
    whole = whole_life_trajectory()
    term  = term_invest_trajectory()

    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        ax.plot(YEARS, whole, color="#b71c1c", linewidth=2.6,
                marker="o", markersize=4, markevery=2,
                label=L["whole"])
        ax.plot(YEARS, term, color="#0d47a1", linewidth=2.6,
                marker="s", markersize=4, markevery=2,
                label=L["term"])

        # End-point dollar labels
        ax.annotate(f"${whole[-1]:,.0f}", xy=(YEARS[-1], whole[-1]),
                    xytext=(YEARS[-1] + 0.3, whole[-1]),
                    fontsize=11, color="#b71c1c", fontweight="bold",
                    va="center")
        ax.annotate(f"${term[-1]:,.0f}", xy=(YEARS[-1], term[-1]),
                    xytext=(YEARS[-1] + 0.3, term[-1]),
                    fontsize=11, color="#0d47a1", fontweight="bold",
                    va="center")

        gap = term[-1] - whole[-1]
        ratio = term[-1] / whole[-1] if whole[-1] > 0 else float("inf")

        ax.set_xlim(0, YEARS[-1] + 3)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(L["title"] + "\n" + L["subtitle"], fontsize=12.5, pad=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper left", fontsize=10.5)

        # Caption box with end values
        caption = (f"{L['end_whole']} ${whole[-1]:,.0f}    "
                   f"{L['end_term']} ${term[-1]:,.0f}    "
                   f"{L['gap']} ${gap:,.0f}  ({ratio:.1f}x)")
        fig.text(0.5, 0.005, caption, ha="center", fontsize=10.5,
                 color="#333", family="sans-serif")

        fname = "week02_buy_term_invest_difference.png" if lang == "en" \
            else f"week02_buy_term_invest_difference_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout(rect=(0, 0.03, 1, 1))
        plt.savefig(out_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            shutil.copy2(out_path, os.path.join(out_dir, "week02_buy_term_invest_difference_en.png"))
        print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)
    render_static_png(out_dir)


if __name__ == "__main__":
    main()
