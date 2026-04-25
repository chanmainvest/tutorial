"""Generate the inflation purchasing-power assets for Week 1.

Outputs:
- week01_inflation_purchasing_power.png  : 50-year purchasing-power curve
  starting in DEFAULT_START. Matches the default state of the interactive
  demo so the static fallback and the live demo agree at first glance.
- stdout: the markdown table for embedding in the lesson, plus narrative
  summary stats (purchasing power lost since 1900, since 2000, since 2020).

Data: US CPI YoY % change, 1900-2025 (BLS-style annual averages). The
last few entries are estimates pending official annual prints.

Run:
    uv run python course/image/week01_inflation_purchasing_power.py
"""

from __future__ import annotations

import os
import matplotlib
import matplotlib.pyplot as plt

# Prefer CJK-capable fonts so the localised PNGs render Chinese cleanly.
matplotlib.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC", "PingFang SC",
    "Noto Sans CJK TC", "Noto Sans CJK SC", "SimHei", "Arial Unicode MS",
    "DejaVu Sans",
]
matplotlib.rcParams["axes.unicode_minus"] = False

LANGS = ("en", "hk", "tw", "cn")
LANG_LABELS = {
    "en": {
        "title_main": "Purchasing power of ${initial:.0f} held as cash from {start}",
        "title_sub":  "After {horizon} years of US inflation: ${end:.2f} ({pct:.0f}% of the original)",
        "xlabel":     "Year",
        "ylabel":     "Purchasing power (in {start} dollars)",
        "legend1":    "Real purchasing power of ${initial:.0f} held as cash",
        "legend2":    "Original ${initial:.0f} value (nominal)",
    },
    "hk": {
        "title_main": "由 {start} 年起以現金持有 ${initial:.0f} 的購買力",
        "title_sub":  "經過 {horizon} 年美國通脹後:${end:.2f}(只剩原值的 {pct:.0f}%)",
        "xlabel":     "年份",
        "ylabel":     "購買力(以 {start} 年美元計)",
        "legend1":    "以現金持有 ${initial:.0f} 的實質購買力",
        "legend2":    "原本 ${initial:.0f} 的名義價值",
    },
    "tw": {
        "title_main": "由 {start} 年起以現金持有 ${initial:.0f} 的購買力",
        "title_sub":  "經過 {horizon} 年美國通膨後:${end:.2f}(只剩原值的 {pct:.0f}%)",
        "xlabel":     "年份",
        "ylabel":     "購買力(以 {start} 年美元計)",
        "legend1":    "以現金持有 ${initial:.0f} 的實質購買力",
        "legend2":    "原本 ${initial:.0f} 的名目價值",
    },
    "cn": {
        "title_main": "从 {start} 年起以现金持有 ${initial:.0f} 的购买力",
        "title_sub":  "经过 {horizon} 年美国通胀后:${end:.2f}(只剩原值的 {pct:.0f}%)",
        "xlabel":     "年份",
        "ylabel":     "购买力(以 {start} 年美元计)",
        "legend1":    "以现金持有 ${initial:.0f} 的实质购买力",
        "legend2":    "原本 ${initial:.0f} 的名义价值",
    },
}

# US CPI YoY change (decimal), 1900-2025 (126 entries)
CPI = [
    # 1900s
    0.012, 0.012, 0.000, 0.012, 0.000, 0.000, 0.000, 0.048, -0.011, 0.000,
    # 1910s
    0.046, 0.000, 0.022, 0.011, 0.011, 0.011, 0.076, 0.178, 0.180, 0.146,
    # 1920s
    0.156, -0.105, -0.061, 0.018, 0.000, 0.024, 0.000, -0.012, -0.012, 0.000,
    # 1930s
    -0.023, -0.089, -0.103, -0.052, 0.035, 0.026, 0.010, 0.037, -0.020, -0.013,
    # 1940s
    0.007, 0.050, 0.109, 0.060, 0.016, 0.023, 0.085, 0.144, 0.081, -0.012,
    # 1950s
    0.013, 0.079, 0.019, 0.008, 0.007, -0.004, 0.015, 0.033, 0.027, 0.009,
    # 1960s
    0.015, 0.011, 0.012, 0.012, 0.013, 0.016, 0.029, 0.031, 0.042, 0.055,
    # 1970s
    0.057, 0.044, 0.032, 0.062, 0.110, 0.091, 0.057, 0.065, 0.076, 0.113,
    # 1980s
    0.135, 0.103, 0.062, 0.032, 0.043, 0.035, 0.019, 0.037, 0.041, 0.048,
    # 1990s
    0.054, 0.042, 0.030, 0.030, 0.026, 0.028, 0.030, 0.023, 0.016, 0.022,
    # 2000s
    0.034, 0.028, 0.016, 0.023, 0.027, 0.034, 0.032, 0.029, 0.038, -0.004,
    # 2010s
    0.016, 0.032, 0.021, 0.015, 0.016, 0.001, 0.013, 0.021, 0.024, 0.018,
    # 2020s
    0.012, 0.047, 0.080, 0.041, 0.029, 0.026,
]
YEARS = list(range(1900, 2026))
assert len(CPI) == len(YEARS), f"{len(CPI)} vs {len(YEARS)}"

INITIAL = 100.0
DEFAULT_START = 1975
HORIZON = 50


def cum_inflation(start_year: int, end_year: int) -> float:
    """Cumulative inflation factor from start of `start_year` to start of
    `end_year`. Equals 1.0 when start_year == end_year (no inflation yet)."""
    s = start_year - 1900
    e = end_year - 1900
    f = 1.0
    for i in range(s, e):
        f *= (1 + CPI[i])
    return f


def purchasing_power(initial: float, start_year: int, end_year: int) -> float:
    """Purchasing power of `initial` (held as cash) at the start of
    `end_year`, expressed in `start_year` dollars."""
    return initial / cum_inflation(start_year, end_year)


TABLE_START = 1970


def print_markdown_table() -> None:
    rows = [1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015,
            2020, 2025]
    print("| Year | Years elapsed | Purchasing power | % of original |")
    print("|------|--------------:|-----------------:|--------------:|")
    for y in rows:
        elapsed = y - TABLE_START
        pp = purchasing_power(INITIAL, TABLE_START, y)
        pct = pp / INITIAL * 100
        print(f"| {y} | {elapsed} | ${pp:.2f} | {pct:.1f}% |")


def render_static_png(out_dir: str) -> None:
    start = DEFAULT_START
    end = start + HORIZON
    years_axis = list(range(start, end + 1))
    pp_series = [purchasing_power(INITIAL, start, y) for y in years_axis]
    end_pp = pp_series[-1]
    end_pct = end_pp / INITIAL * 100

    fmt_args = {
        "initial": INITIAL,
        "start":   start,
        "horizon": HORIZON,
        "end":     end_pp,
        "pct":     end_pct,
    }

    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        ax.plot(years_axis, pp_series, color="#b71c1c", linewidth=2.8,
                marker="o", markersize=4, markevery=5,
                label=L["legend1"].format(**fmt_args))
        ax.axhline(INITIAL, color="#5a5a5a", linewidth=1.2, linestyle=":",
                   alpha=0.7, label=L["legend2"].format(**fmt_args))

        ax.set_xlim(start, end)
        ax.set_ylim(0, INITIAL * 1.08)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"].format(**fmt_args), fontsize=12)
        ax.set_title(
            L["title_main"].format(**fmt_args) + "\n"
            + L["title_sub"].format(**fmt_args),
            fontsize=13, pad=10,
        )
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper right", fontsize=10.5)

        ax.annotate(f"${end_pp:.2f}", xy=(end, end_pp),
                    xytext=(end - 1.5, end_pp - 6),
                    fontsize=12, fontweight="bold", color="#b71c1c", ha="right")

        fname = "week01_inflation_purchasing_power.png" if lang == "en" \
            else f"week01_inflation_purchasing_power_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            import shutil
            shutil.copy2(out_path, os.path.join(out_dir, "week01_inflation_purchasing_power_en.png"))
        print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)

    print("=" * 64)
    print("Inflation purchasing-power table (for direct paste into markdown):")
    print("=" * 64)
    print()
    print_markdown_table()
    print()

    pp_25_from_1900 = purchasing_power(INITIAL, 1900, 2025)
    loss_1900 = (1 - pp_25_from_1900 / INITIAL) * 100
    pp_25_from_2000 = purchasing_power(INITIAL, 2000, 2025)
    loss_2000 = (1 - pp_25_from_2000 / INITIAL) * 100
    pp_25_from_2020 = purchasing_power(INITIAL, 2020, 2025)
    loss_2020 = (1 - pp_25_from_2020 / INITIAL) * 100

    print("Summary stats for the markdown narrative:")
    print(f"  $100 held from 1900 -> 2025 (125 yrs): ${pp_25_from_1900:>6.2f} "
          f"({loss_1900:.1f}% lost)")
    print(f"  $100 held from 2000 -> 2025 ( 25 yrs): ${pp_25_from_2000:>6.2f} "
          f"({loss_2000:.1f}% lost)")
    print(f"  $100 held from 2020 -> 2025 (  5 yrs): ${pp_25_from_2020:>6.2f} "
          f"({loss_2020:.1f}% lost)")
    print()

    render_static_png(out_dir)


if __name__ == "__main__":
    main()
