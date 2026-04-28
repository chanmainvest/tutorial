"""Generate the expense-ratio compounding-drag chart for Week 2, §2.5.

Five wealth trajectories of a $100,000 stake compounded over 30 years
at the same 10% gross return, but with five different expense ratios:
0.03% (index ETF), 0.50%, 1.00%, 1.50%, 2.00% (insurance wrapper).

The point is brutal: a 2% wrapper costs roughly $700,000 of terminal
wealth on a $100,000 stake over 30 years, even when the underlying
gross return is identical to the index. Fees compound — and the
compounded fee is the only line on a fund prospectus that is
guaranteed.

Run:
    uv run --with matplotlib python course/image/week02_expense_drag.py
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
        "title":    "Expense ratios compound — over 30 years a 2% fee costs $700K",
        "subtitle": "$100,000 invested for 30 years at a 10% gross return, with five different expense ratios",
        "xlabel":   "Year",
        "ylabel":   "Portfolio value (USD)",
        "fund":     {
            "0.03": "Index ETF (0.03%)",
            "0.50": "Cheap active (0.50%)",
            "1.00": "Average active (1.00%)",
            "1.50": "Expensive active (1.50%)",
            "2.00": "Insurance wrapper (2.00%)",
        },
    },
    "hk": {
        "title":    "費用率會複利累積 — 30 年下來 2% 費用蝕掉約 70 萬美元",
        "subtitle": "10 萬美元投資 30 年,毛回報同為 10%,五種不同費用率",
        "xlabel":   "年份",
        "ylabel":   "組合價值(美元)",
        "fund":     {
            "0.03": "指數 ETF(0.03%)",
            "0.50": "低費主動(0.50%)",
            "1.00": "平均主動(1.00%)",
            "1.50": "高費主動(1.50%)",
            "2.00": "保險包裝(2.00%)",
        },
    },
    "tw": {
        "title":    "費用率會複利累積 — 30 年下來 2% 費用蝕掉約 70 萬美元",
        "subtitle": "10 萬美元投資 30 年,毛報酬同為 10%,五種不同費用率",
        "xlabel":   "年份",
        "ylabel":   "投組價值(美元)",
        "fund":     {
            "0.03": "指數 ETF(0.03%)",
            "0.50": "低費主動(0.50%)",
            "1.00": "平均主動(1.00%)",
            "1.50": "高費主動(1.50%)",
            "2.00": "保險包裝(2.00%)",
        },
    },
    "cn": {
        "title":    "费用率会复利累积 — 30 年下来 2% 费用蚕食约 70 万美元",
        "subtitle": "10 万美元投资 30 年,毛回报同为 10%,五种不同费用率",
        "xlabel":   "年份",
        "ylabel":   "组合价值(美元)",
        "fund":     {
            "0.03": "指数 ETF(0.03%)",
            "0.50": "低费主动(0.50%)",
            "1.00": "平均主动(1.00%)",
            "1.50": "高费主动(1.50%)",
            "2.00": "保险包装(2.00%)",
        },
    },
}

PRINCIPAL = 100_000.0
YEARS_HORIZON = 30
GROSS_RETURN = 0.10
YEARS = list(range(0, YEARS_HORIZON + 1))

# Five expense ratios, displayed as "E.E%" strings for keying.
EXPENSE_RATIOS = [
    ("0.03", 0.0003, "#1f5e2d"),  # index ETF — green (good)
    ("0.50", 0.0050, "#0d47a1"),  # cheap active — navy
    ("1.00", 0.0100, "#a37500"),  # average active — gold
    ("1.50", 0.0150, "#c62828"),  # expensive — red
    ("2.00", 0.0200, "#6a1b9a"),  # insurance wrapper — purple
]


def trajectory(principal: float, gross: float, expense: float, years: int) -> list[float]:
    """Wealth trajectory year-by-year. Net return = gross - expense."""
    net = gross - expense
    return [principal * ((1.0 + net) ** y) for y in range(0, years + 1)]


def fmt_dollars(v: float) -> str:
    """Compact USD label for the end-point annotation, e.g. $1.72M."""
    if v >= 1_000_000:
        return f"${v / 1_000_000:.2f}M"
    if v >= 1_000:
        return f"${v / 1_000:.0f}K"
    return f"${v:,.0f}"


def render_static_png(out_dir: str) -> None:
    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6.2))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        end_values: dict[str, float] = {}
        for key, exp, color in EXPENSE_RATIOS:
            ys = trajectory(PRINCIPAL, GROSS_RETURN, exp, YEARS_HORIZON)
            end_values[key] = ys[-1]
            ax.plot(
                YEARS, ys,
                color=color, linewidth=2.4,
                label=L["fund"][key],
            )

        # End-point dollar labels — right of x = 30, vertically aligned to each line's last point.
        for key, exp, color in EXPENSE_RATIOS:
            v = end_values[key]
            ax.annotate(
                fmt_dollars(v),
                xy=(YEARS_HORIZON, v),
                xytext=(YEARS_HORIZON + 0.4, v),
                fontsize=10.5, color=color, fontweight="bold",
                va="center",
            )

        # Annotate the gap between the best and the worst line — the headline number.
        best = end_values["0.03"]
        worst = end_values["2.00"]
        gap = best - worst
        # Vertical bracket between the two end points
        x_b = YEARS_HORIZON - 0.4
        ax.annotate(
            "",
            xy=(x_b, best), xytext=(x_b, worst),
            arrowprops=dict(arrowstyle="<->", color="#5a5a5a", lw=1.2),
        )
        ax.text(
            x_b - 0.5, (best + worst) / 2,
            f"-{fmt_dollars(gap)}",
            fontsize=11, color="#5a5a5a", fontweight="bold",
            va="center", ha="right",
        )

        ax.set_xlim(0, YEARS_HORIZON + 4.5)
        ax.set_ylim(0, max(end_values.values()) * 1.10)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(L["title"] + "\n" + L["subtitle"], fontsize=13, pad=10)
        ax.grid(True, alpha=0.3)
        # y-axis as $K with thousands separator
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda v, _pos: f"${v / 1000:,.0f}K")
        )
        ax.legend(loc="upper left", fontsize=10)

        plt.tight_layout()
        if lang == "en":
            base_path = os.path.join(out_dir, "week02_expense_drag.png")
            plt.savefig(base_path, dpi=150, bbox_inches="tight",
                        facecolor=fig.get_facecolor())
            plt.close(fig)
            shutil.copy2(base_path, os.path.join(out_dir, "week02_expense_drag_en.png"))
            print(f"Saved: {base_path}")
            print(f"Saved: {os.path.join(out_dir, 'week02_expense_drag_en.png')}")
        else:
            out_path = os.path.join(out_dir, f"week02_expense_drag_{lang}.png")
            plt.savefig(out_path, dpi=150, bbox_inches="tight",
                        facecolor=fig.get_facecolor())
            plt.close(fig)
            print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)
    render_static_png(out_dir)


if __name__ == "__main__":
    main()
