"""Generate the "Three Portfolios" chart for Week 1.

Three savers each put $10,000 into a different vehicle every year from
1971 through 2025. The chart shows the year-by-year nominal value of
each portfolio (log scale), and the script also prints the inflation-
adjusted ("real") values in 1971 dollars at the end of the period.

Data sources (annual averages, decimal):
- 3-month T-bill rates: FRED series TB3MS, annual mean
- CPI YoY change: FRED series CPIAUCSL, December YoY
- S&P 500 total return (dividends reinvested): NYU Stern Damodaran
  historical returns dataset (Total Annual Return on S&P 500)

The most recent 1-2 entries are estimated where official annual prints
were not yet finalised at the time this script was written.

Run:
    uv run python course/image/week01_three_portfolios.py
Output:
    course/image/week01_three_portfolios.png
"""

from __future__ import annotations

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Prefer CJK-capable fonts so the localised PNGs render Chinese cleanly.
matplotlib.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC", "PingFang SC",
    "Noto Sans CJK TC", "Noto Sans CJK SC", "SimHei", "Arial Unicode MS",
    "DejaVu Sans",
]
matplotlib.rcParams["axes.unicode_minus"] = False

DEPOSIT = 10_000

YEARS = list(range(1971, 2026))  # 1971..2025 inclusive (55 years)

LANGS = ("en", "hk", "tw", "cn")

# Per-locale strings for the chart. Dollar signs are kept literal because
# the underlying currency is USD across all locales of this lesson.
LANG_LABELS = {
    "en": {
        "title_main":   "Three Portfolios, Same $10,000/year Deposit, 1971-2025",
        "title_sub":    "Where you put your savings matters more than how much you save",
        "xlabel":       "Year",
        "ylabel":       "Portfolio value (USD, log scale)",
        "legend_c":     "Person C — S&P 500 (dividends reinvested)",
        "legend_b":     "Person B — Short-term US T-bills",
        "legend_a":     "Person A — Cash (= total deposits)",
    },
    "hk": {
        "title_main":   "三個投資組合,每年同樣存入 $10,000(1971-2025)",
        "title_sub":    "把錢放在哪裡,比你存了多少更重要",
        "xlabel":       "年份",
        "ylabel":       "投資組合價值(美元,對數刻度)",
        "legend_c":     "C — S&P 500(股息再投資)",
        "legend_b":     "B — 短期美國國庫券",
        "legend_a":     "A — 現金(=累計存款)",
    },
    "tw": {
        "title_main":   "三個投資組合,每年同樣存入 $10,000(1971-2025)",
        "title_sub":    "把錢放在哪裡,比你存了多少更重要",
        "xlabel":       "年份",
        "ylabel":       "投資組合價值(美元,對數刻度)",
        "legend_c":     "C — 標普 500(股息再投入)",
        "legend_b":     "B — 短期美國國庫券",
        "legend_a":     "A — 現金(=累計存款)",
    },
    "cn": {
        "title_main":   "三个投资组合,每年同样存入 $10,000(1971-2025)",
        "title_sub":    "把钱放在哪里,比你存了多少更重要",
        "xlabel":       "年份",
        "ylabel":       "投资组合价值(美元,对数刻度)",
        "legend_c":     "C — 标普 500(股息再投资)",
        "legend_b":     "B — 短期美国国债",
        "legend_a":     "A — 现金(= 累计存款)",
    },
}

# Annual average 3-month US Treasury bill yield (decimal)
TBILL = [
    0.0434, 0.0407, 0.0704, 0.0789, 0.0584, 0.0499, 0.0527, 0.0722, 0.1004, 0.1151,
    0.1403, 0.1069, 0.0863, 0.0958, 0.0749, 0.0597, 0.0583, 0.0667, 0.0811, 0.0751,
    0.0542, 0.0345, 0.0302, 0.0429, 0.0551, 0.0502, 0.0507, 0.0481, 0.0466, 0.0585,
    0.0345, 0.0162, 0.0102, 0.0138, 0.0316, 0.0473, 0.0436, 0.0137, 0.0015, 0.0014,
    0.0005, 0.0009, 0.0006, 0.0003, 0.0005, 0.0032, 0.0093, 0.0194, 0.0206, 0.0036,
    0.0004, 0.0202, 0.0511, 0.0495, 0.0430,
]

# CPI year-on-year change (decimal). Negative in 2009 reflects the GFC deflation.
CPI = [
    0.044, 0.032, 0.062, 0.110, 0.091, 0.057, 0.065, 0.076, 0.113, 0.135,
    0.103, 0.062, 0.032, 0.043, 0.035, 0.019, 0.037, 0.041, 0.048, 0.054,
    0.042, 0.030, 0.030, 0.026, 0.028, 0.030, 0.023, 0.016, 0.022, 0.034,
    0.028, 0.016, 0.023, 0.027, 0.034, 0.032, 0.029, 0.038, -0.004, 0.016,
    0.032, 0.021, 0.015, 0.016, 0.001, 0.013, 0.021, 0.024, 0.018, 0.012,
    0.047, 0.080, 0.041, 0.029, 0.026,
]

# S&P 500 total return with dividends reinvested (decimal)
SPX_TR = [
    0.1431, 0.1898, -0.1466, -0.2647, 0.3720, 0.2384, -0.0718, 0.0656, 0.1844, 0.3242,
    -0.0491, 0.2155, 0.2256, 0.0627, 0.3173, 0.1867, 0.0525, 0.1661, 0.3169, -0.0310,
    0.3047, 0.0762, 0.1008, 0.0132, 0.3758, 0.2296, 0.3336, 0.2858, 0.2104, -0.0910,
    -0.1189, -0.2210, 0.2868, 0.1088, 0.0491, 0.1579, 0.0549, -0.3700, 0.2646, 0.1506,
    0.0211, 0.1600, 0.3239, 0.1369, 0.0138, 0.1196, 0.2183, -0.0438, 0.3149, 0.1840,
    0.2871, -0.1811, 0.2629, 0.2502, 0.2000,
]

assert len(YEARS) == len(TBILL) == len(CPI) == len(SPX_TR) == 55, "length mismatch"


def compound_with_deposit(returns: list[float], deposit: int = DEPOSIT) -> list[float]:
    """End-of-year balance when `deposit` is added at the start of each year
    and earns the annual return for that year."""
    val = 0.0
    out: list[float] = []
    for r in returns:
        val = (val + deposit) * (1 + r)
        out.append(val)
    return out


def cash_running(n: int, deposit: int = DEPOSIT) -> list[float]:
    """Pure cash, no return — just the running sum of deposits."""
    return [float(deposit * (i + 1)) for i in range(n)]


def render_one(lang: str, a_nom, b_nom, c_nom) -> str:
    """Render the chart for a single locale. Returns the output path."""
    L = LANG_LABELS[lang]

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor("#fdfbf5")
    ax.set_facecolor("#fdfbf5")

    ax.plot(YEARS, c_nom, label=L["legend_c"], color="#b71c1c", linewidth=2.8)
    ax.plot(YEARS, b_nom, label=L["legend_b"], color="#0d47a1", linewidth=2.4)
    ax.plot(YEARS, a_nom, label=L["legend_a"], color="#5a5a5a", linewidth=2.2,
            linestyle="--")

    ax.set_yscale("log")
    ax.set_xlim(1971, 2027)
    ax.set_xlabel(L["xlabel"], fontsize=12)
    ax.set_ylabel(L["ylabel"], fontsize=12)
    ax.set_title(L["title_main"] + "\n" + L["title_sub"], fontsize=13.5, pad=12)
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(loc="upper left", fontsize=10.5, framealpha=0.95)

    def fmt_money(v: float) -> str:
        if v >= 1e6:
            return f"${v / 1e6:.2f}M"
        if v >= 1e3:
            return f"${v / 1e3:.0f}K"
        return f"${v:.0f}"

    label_kwargs = {"fontsize": 11.5, "fontweight": "bold", "ha": "left",
                    "va": "center"}
    ax.annotate(fmt_money(c_nom[-1]), xy=(2025.5, c_nom[-1]),
                color="#b71c1c", **label_kwargs)
    ax.annotate(fmt_money(b_nom[-1]), xy=(2025.5, b_nom[-1]),
                color="#0d47a1", **label_kwargs)
    ax.annotate(fmt_money(a_nom[-1]), xy=(2025.5, a_nom[-1]),
                color="#5a5a5a", **label_kwargs)

    plt.tight_layout()

    fname = "week01_three_portfolios.png" if lang == "en" \
        else f"week01_three_portfolios_{lang}.png"
    out_path = os.path.join(os.path.dirname(__file__), fname)
    plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    # Also write the EN copy as the locale-suffixed file so build.py's
    # localised_image_src() can find it without falling back.
    if lang == "en":
        copy_path = os.path.join(os.path.dirname(__file__),
                                 "week01_three_portfolios_en.png")
        import shutil
        shutil.copy2(out_path, copy_path)
    return out_path


def main() -> None:
    a_nom = cash_running(len(YEARS))             # cash, no interest
    b_nom = compound_with_deposit(TBILL)         # short-term T-bills
    c_nom = compound_with_deposit(SPX_TR)        # S&P 500 total return

    # Inflation-adjusted (in 1971 dollars), for the printed summary
    cum_cpi = np.cumprod([1 + r for r in CPI])
    a_real_1971 = a_nom[-1] / cum_cpi[-1]
    b_real_1971 = b_nom[-1] / cum_cpi[-1]
    c_real_1971 = c_nom[-1] / cum_cpi[-1]

    for lang in LANGS:
        out_path = render_one(lang, a_nom, b_nom, c_nom)
        print(f"Saved: {out_path}")

    total_deposited = DEPOSIT * len(YEARS)
    print()
    print(f"Each person deposited ${total_deposited:,} over {len(YEARS)} years (1971-2025).")
    print()
    print(f"  Person A (cash):     ${a_nom[-1]:>14,.0f} nominal | "
          f"${a_real_1971:>10,.0f} in 1971 dollars")
    print(f"  Person B (T-bills):  ${b_nom[-1]:>14,.0f} nominal | "
          f"${b_real_1971:>10,.0f} in 1971 dollars")
    print(f"  Person C (S&P 500):  ${c_nom[-1]:>14,.0f} nominal | "
          f"${c_real_1971:>10,.0f} in 1971 dollars")
    print()
    print(f"Cumulative CPI 1971-2025: {(cum_cpi[-1] - 1) * 100:.0f}% "
          f"(it now takes ${cum_cpi[-1]:.2f} to buy what $1 bought in 1971).")

    # Geometric mean (CAGR) of the annual return series itself — the right
    # number to quote as the "average annualised return" of the strategy,
    # because it's the constant rate that, compounded over the same number
    # of years, produces the same growth factor as the actual variable
    # path. (Arithmetic mean overstates compound performance.)
    n = len(YEARS)
    tbill_cagr = float(np.prod([1 + r for r in TBILL]) ** (1 / n) - 1)
    spx_cagr = float(np.prod([1 + r for r in SPX_TR]) ** (1 / n) - 1)
    cpi_cagr = float(cum_cpi[-1] ** (1 / n) - 1)
    print()
    print(f"Geometric-mean (CAGR) annual returns over {n} years (1971-2025):")
    print(f"  Cash:    0.00%")
    print(f"  T-bills: {tbill_cagr * 100:.2f}%")
    print(f"  S&P 500: {spx_cagr * 100:.2f}%")
    print(f"  (CPI for reference: {cpi_cagr * 100:.2f}% / yr — anything below this is a real loss.)")


if __name__ == "__main__":
    main()
