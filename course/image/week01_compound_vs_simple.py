"""Generate the "Compound vs Simple Interest" chart for Week 1.

Shows how a $1,000 starting balance grows at the same nominal rate under
simple interest (interest only on principal) vs compound interest
(interest on the running balance). The static defaults match the
in-lesson example: $1,000, 8% annual, 40 years. The matching interactive
demo lets the website reader change the rate and the horizon.

Run:
    uv run python course/image/week01_compound_vs_simple.py
"""

from __future__ import annotations

import os
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
        "title_main":   "Compound vs. Simple Interest on ${p:,.0f}, {rate}% annual, over {y} years",
        "title_sub":    "Compound ends at ${ec:,.0f}, simple ends at ${es:,.0f} — a ${gap:,.0f} gap",
        "xlabel":       "Years",
        "ylabel":       "Account value (USD)",
        "legend_compound": "Compound interest at {rate}%",
        "legend_simple":   "Simple interest at {rate}%",
        "legend_bonus":    "Bonus from compounding",
    },
    "hk": {
        "title_main":   "${p:,.0f} 在 {rate}% 年利率下的複利 vs 單利({y} 年)",
        "title_sub":    "複利終值 ${ec:,.0f},單利終值 ${es:,.0f} — 相差 ${gap:,.0f}",
        "xlabel":       "年數",
        "ylabel":       "帳戶價值(美元)",
        "legend_compound": "複利({rate}%)",
        "legend_simple":   "單利({rate}%)",
        "legend_bonus":    "複利帶來的額外增長",
    },
    "tw": {
        "title_main":   "${p:,.0f} 在 {rate}% 年利率下的複利 vs 單利({y} 年)",
        "title_sub":    "複利終值 ${ec:,.0f},單利終值 ${es:,.0f} — 相差 ${gap:,.0f}",
        "xlabel":       "年數",
        "ylabel":       "帳戶價值(美元)",
        "legend_compound": "複利({rate}%)",
        "legend_simple":   "單利({rate}%)",
        "legend_bonus":    "複利帶來的額外增長",
    },
    "cn": {
        "title_main":   "${p:,.0f} 在 {rate}% 年利率下的复利 vs 单利({y} 年)",
        "title_sub":    "复利终值 ${ec:,.0f},单利终值 ${es:,.0f} — 相差 ${gap:,.0f}",
        "xlabel":       "年数",
        "ylabel":       "账户价值(美元)",
        "legend_compound": "复利({rate}%)",
        "legend_simple":   "单利({rate}%)",
        "legend_bonus":    "复利带来的额外增长",
    },
}

PRINCIPAL = 1000.0
RATE = 0.08
YEARS = 40


def simple_series(p: float, r: float, n: int) -> list[float]:
    return [p * (1 + r * t) for t in range(n + 1)]


def compound_series(p: float, r: float, n: int) -> list[float]:
    return [p * (1 + r) ** t for t in range(n + 1)]


def main() -> None:
    out_dir = os.path.dirname(__file__)
    xs = list(range(YEARS + 1))
    simple = simple_series(PRINCIPAL, RATE, YEARS)
    compound = compound_series(PRINCIPAL, RATE, YEARS)

    fmt_args = {
        "p": PRINCIPAL,
        "rate": int(RATE * 100),
        "y": YEARS,
        "ec": compound[-1],
        "es": simple[-1],
        "gap": compound[-1] - simple[-1],
    }

    def fmt(v: float) -> str:
        if v >= 1e6:
            return f"${v / 1e6:.2f}M"
        if v >= 1e3:
            return f"${v / 1e3:.1f}K"
        return f"${v:,.0f}"

    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        ax.plot(xs, compound, color="#b71c1c", linewidth=2.8,
                label=L["legend_compound"].format(**fmt_args))
        ax.plot(xs, simple, color="#0d47a1", linewidth=2.4, linestyle="--",
                label=L["legend_simple"].format(**fmt_args))
        ax.fill_between(xs, simple, compound,
                        where=[c >= s for s, c in zip(simple, compound)],
                        interpolate=True, color="#b71c1c", alpha=0.08,
                        label=L["legend_bonus"].format(**fmt_args))

        ax.set_xlim(0, YEARS)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(
            L["title_main"].format(**fmt_args) + "\n"
            + L["title_sub"].format(**fmt_args),
            fontsize=13, pad=10,
        )
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper left", fontsize=11)

        ax.annotate(fmt(compound[-1]), xy=(YEARS, compound[-1]),
                    xytext=(YEARS - 0.5, compound[-1] - 1400),
                    fontsize=12, fontweight="bold", color="#b71c1c", ha="right")
        ax.annotate(fmt(simple[-1]), xy=(YEARS, simple[-1]),
                    xytext=(YEARS - 0.5, simple[-1] + 600),
                    fontsize=12, fontweight="bold", color="#0d47a1", ha="right")

        fname = "week01_compound_vs_simple.png" if lang == "en" \
            else f"week01_compound_vs_simple_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            import shutil
            shutil.copy2(out_path, os.path.join(out_dir, "week01_compound_vs_simple_en.png"))
        print(f"Saved: {out_path}")
    print()
    print(f"Principal:    ${PRINCIPAL:,.2f}")
    print(f"Rate:         {RATE*100:.1f}% per year")
    print(f"Horizon:      {YEARS} years")
    print(f"Simple end:   ${simple[-1]:,.2f}  (interest = ${simple[-1] - PRINCIPAL:,.2f})")
    print(f"Compound end: ${compound[-1]:,.2f}  (interest = ${compound[-1] - PRINCIPAL:,.2f})")
    print(f"Compound bonus over simple: ${compound[-1] - simple[-1]:,.2f}")


if __name__ == "__main__":
    main()
