"""Generate the US M2 + US National Debt parallel-growth chart for Week 1, §2.2.

Both series in trillions USD on the same axis, 1990-2025. The story is
the parallel: US Treasury debt outstanding and US M2 money supply have
climbed together with the same inflection points (2008 GFC, 2020 COVID),
because fiscal deficits are now overwhelmingly financed by central-bank
money creation rather than by existing private savings.

Data sources:

- US M2:    FRED M2SL (Federal Reserve), year-end values.
- US Debt:  US Treasury TreasuryDirect 'Debt to the Penny', year-end
            total public debt outstanding (intragovernmental + held by
            the public).

Approximations to one decimal place; minor revisions don't change the
qualitative story.

Run:
    uv run python course/image/week01_us_debt_m2.py
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
        "title":    "US Treasury debt and US M2 money supply",
        "subtitle": "Both in trillions of USD, 1990-2025. They climb together — fiscal deficits financed by money creation are not separate phenomena.",
        "xlabel":   "Year",
        "ylabel":   "Trillions USD",
        "debt":     "US Treasury debt outstanding",
        "m2":       "US M2 money supply",
        "ann_gfc":  "2008 GFC",
        "ann_covid": "2020 COVID",
    },
    "hk": {
        "title":    "美國國債與美國 M2 貨幣供應",
        "subtitle": "皆以萬億美元計,1990-2025。兩者同步上升 — 由貨幣創造融資的財政赤字不是兩件獨立的事。",
        "xlabel":   "年份",
        "ylabel":   "萬億美元",
        "debt":     "美國國債未償餘額",
        "m2":       "美國 M2 貨幣供應",
        "ann_gfc":  "2008 金融海嘯",
        "ann_covid": "2020 新冠",
    },
    "tw": {
        "title":    "美國國債與美國 M2 貨幣供給",
        "subtitle": "皆以兆美元計,1990-2025。兩者同步上升 — 由貨幣創造融資的財政赤字不是兩件獨立的事。",
        "xlabel":   "年份",
        "ylabel":   "兆美元",
        "debt":     "美國國債未償餘額",
        "m2":       "美國 M2 貨幣供給",
        "ann_gfc":  "2008 金融海嘯",
        "ann_covid": "2020 新冠",
    },
    "cn": {
        "title":    "美国国债与美国 M2 货币供应",
        "subtitle": "皆以万亿美元计,1990-2025。两者同步上升 — 由货币创造融资的财政赤字不是两件独立的事。",
        "xlabel":   "年份",
        "ylabel":   "万亿美元",
        "debt":     "美国国债未偿余额",
        "m2":       "美国 M2 货币供应",
        "ann_gfc":  "2008 金融危机",
        "ann_covid": "2020 新冠",
    },
}

YEARS = list(range(1990, 2026))

# US National debt outstanding ($T, year-end totals)
US_DEBT = [
    3.2, 3.6, 4.0, 4.4, 4.7, 4.9, 5.2, 5.4, 5.5, 5.7,           # 1990s
    5.6, 5.8, 6.2, 6.8, 7.4, 7.9, 8.5, 9.0, 10.0, 12.3,         # 2000s
    14.0, 15.2, 16.4, 17.4, 18.0, 18.9, 19.9, 20.5, 22.0, 23.2, # 2010s
    27.7, 29.6, 31.4, 34.0, 35.5, 36.4,                          # 2020-2025
]

# US M2 money supply ($T, year-end)
US_M2 = [
    3.30, 3.43, 3.51, 3.50, 3.50, 3.65, 3.85, 4.04, 4.40, 4.62, # 1990s
    4.93, 5.43, 5.77, 6.05, 6.40, 6.66, 7.07, 7.46, 8.15, 8.49, # 2000s
    8.78, 9.66, 10.49, 11.06, 11.69, 12.34, 13.21, 13.85, 14.36, 15.32, # 2010s
    19.09, 21.49, 21.46, 20.83, 21.45, 22.20,                    # 2020-2025
]

assert len(YEARS) == len(US_DEBT) == len(US_M2)


def render_static_png(out_dir: str) -> None:
    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        ax.plot(YEARS, US_DEBT, color="#b71c1c", linewidth=2.6,
                marker="o", markersize=3.5, markevery=3,
                label=L["debt"])
        ax.plot(YEARS, US_M2, color="#0d47a1", linewidth=2.6,
                marker="s", markersize=3.5, markevery=3,
                label=L["m2"])

        # Inflection-point annotations
        ax.axvline(2008, color="#5a5a5a", linewidth=0.8, linestyle=":", alpha=0.6)
        ax.axvline(2020, color="#5a5a5a", linewidth=0.8, linestyle=":", alpha=0.6)
        ax.text(2008.3, 33, L["ann_gfc"], fontsize=9.5,
                color="#5a5a5a", alpha=0.85, rotation=0)
        ax.text(2020.3, 33, L["ann_covid"], fontsize=9.5,
                color="#5a5a5a", alpha=0.85, rotation=0)

        # End-point labels
        ax.annotate(f"${US_DEBT[-1]:.1f}T", xy=(2025, US_DEBT[-1]),
                    xytext=(2025.3, US_DEBT[-1]),
                    fontsize=11, color="#b71c1c", fontweight="bold",
                    va="center")
        ax.annotate(f"${US_M2[-1]:.1f}T", xy=(2025, US_M2[-1]),
                    xytext=(2025.3, US_M2[-1]),
                    fontsize=11, color="#0d47a1", fontweight="bold",
                    va="center")

        ax.set_xlim(1990, 2027)
        ax.set_ylim(0, 40)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(L["title"] + "\n" + L["subtitle"], fontsize=13, pad=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper left", fontsize=10.5)

        fname = "week01_us_debt_m2.png" if lang == "en" \
            else f"week01_us_debt_m2_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            shutil.copy2(out_path, os.path.join(out_dir, "week01_us_debt_m2_en.png"))
        print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)
    render_static_png(out_dir)


if __name__ == "__main__":
    main()
