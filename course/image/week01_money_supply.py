"""Generate the global M2 money-supply chart for Week 1, §2.2.

Shows broad money supply (M2) for five major currencies over 2000-2025,
each indexed to 100 at year 2000, on a log scale. The story:

- Every major currency has been debased over the period (every line
  rises).
- China stands out — CNY M2 is up roughly 25× over 25 years, driven by
  state-directed credit expansion.
- The post-2020 vertical move is visible across all currencies — the
  COVID-era response was a globally synchronised expansion of money,
  the largest in modern history outside of wartime.

Data sources (year-end M2, approximate, headline values):

- US M2:   FRED M2SL (Federal Reserve)
- EU M3:   ECB Statistical Data Warehouse (using M3 as the EU's broad
           money measure since the ECB doesn't publish M2 the way the
           Fed does — closest equivalent)
- JP M2:   Bank of Japan
- CN M2:   People's Bank of China
- TW M2:   Central Bank of the Republic of China (Taiwan)

Numbers below are illustrative year-end approximations; small revisions
to source data won't change the chart's qualitative story.

Run:
    uv run python course/image/week01_money_supply.py
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
        "title":    "Broad money supply (M2) of major currencies",
        "subtitle": "Indexed to 100 at year 2000, log scale. Every line is a story of currency debasement.",
        "xlabel":   "Year",
        "ylabel":   "M2 indexed (year 2000 = 100, log scale)",
        "us":       "USD M2 (US Federal Reserve)",
        "eu":       "EUR M3 (ECB — broad money)",
        "jp":       "JPY M2 (Bank of Japan)",
        "cn":       "CNY M2 (People's Bank of China)",
        "tw":       "TWD M2 (CBC Taiwan)",
        "annot_cn": "China: ~25× in 25 years",
        "annot_us": "US: ~4.4×",
        "annot_covid": "COVID response\n(global, 2020+)",
    },
    "hk": {
        "title":    "主要貨幣的廣義貨幣供應(M2)",
        "subtitle": "以 2000 年為 100 作指數化,對數軸。每條線都是貨幣貶值的故事。",
        "xlabel":   "年份",
        "ylabel":   "M2 指數(2000 年 = 100,對數軸)",
        "us":       "美元 M2(美聯儲)",
        "eu":       "歐元 M3(歐洲央行 — 廣義貨幣)",
        "jp":       "日圓 M2(日本央行)",
        "cn":       "人民幣 M2(中國人民銀行)",
        "tw":       "新台幣 M2(台灣中央銀行)",
        "annot_cn": "中國:25 年增長約 25 倍",
        "annot_us": "美國:約 4.4 倍",
        "annot_covid": "新冠應對\n(2020 年起全球同步)",
    },
    "tw": {
        "title":    "主要貨幣的廣義貨幣供給(M2)",
        "subtitle": "以 2000 年為 100 作指數化,對數軸。每條線都是貨幣貶值的故事。",
        "xlabel":   "年份",
        "ylabel":   "M2 指數(2000 年 = 100,對數軸)",
        "us":       "美元 M2(美聯儲)",
        "eu":       "歐元 M3(歐洲央行 — 廣義貨幣)",
        "jp":       "日圓 M2(日本央行)",
        "cn":       "人民幣 M2(中國人民銀行)",
        "tw":       "新台幣 M2(中央銀行)",
        "annot_cn": "中國:25 年增長約 25 倍",
        "annot_us": "美國:約 4.4 倍",
        "annot_covid": "新冠應對\n(2020 年起全球同步)",
    },
    "cn": {
        "title":    "主要货币的广义货币供应(M2)",
        "subtitle": "以 2000 年为 100 作指数化,对数轴。每条线都是货币贬值的故事。",
        "xlabel":   "年份",
        "ylabel":   "M2 指数(2000 年 = 100,对数轴)",
        "us":       "美元 M2(美联储)",
        "eu":       "欧元 M3(欧洲央行 — 广义货币)",
        "jp":       "日元 M2(日本央行)",
        "cn":       "人民币 M2(中国人民银行)",
        "tw":       "新台币 M2(台湾央行)",
        "annot_cn": "中国:25 年增长约 25 倍",
        "annot_us": "美国:约 4.4 倍",
        "annot_covid": "新冠应对\n(2020 年起全球同步)",
    },
}

# Year-end M2 (broad money) headline values, in local currency units.
# Approximations. 2000-2025 (26 entries each).
YEARS = list(range(2000, 2026))

# US M2 in trillions USD
US_M2 = [4.93, 5.43, 5.77, 6.05, 6.40, 6.66, 7.07, 7.46, 8.15, 8.49,
         8.78, 9.66, 10.49, 11.06, 11.69, 12.34, 13.21, 13.85, 14.36, 15.32,
         19.09, 21.49, 21.46, 20.83, 21.45, 22.20]

# EU M3 in trillions EUR  (ECB's broad money — closest to M2)
EU_M3 = [4.99, 5.41, 5.81, 6.27, 6.85, 7.46, 8.20, 9.05, 9.60, 9.36,
         9.45, 9.62, 9.83, 9.85, 10.35, 10.85, 11.40, 11.93, 12.39, 13.04,
         14.20, 15.20, 16.04, 16.50, 16.85, 17.20]

# Japan M2 in trillions JPY
JP_M2 = [620, 650, 680, 700, 715, 730, 740, 745, 740, 770,
         800, 820, 840, 870, 905, 935, 970, 1010, 1040, 1075,
         1170, 1230, 1240, 1235, 1240, 1255]

# China M2 in trillions CNY
CN_M2 = [13.5, 16.0, 18.5, 22.0, 25.5, 30.0, 34.5, 40.0, 47.5, 60.0,
         72.5, 85.0, 97.5, 110.0, 122.5, 139.2, 155.0, 167.7, 182.7, 198.7,
         218.7, 238.0, 266.4, 292.3, 313.5, 322.0]

# Taiwan M2 in trillions TWD
TW_M2 = [20.5, 21.5, 22.5, 23.7, 24.9, 26.0, 27.0, 28.5, 30.5, 32.5,
         34.0, 35.7, 37.4, 39.5, 41.7, 43.5, 45.0, 46.6, 48.0, 49.5,
         52.7, 55.7, 57.6, 58.5, 59.5, 60.5]

assert all(len(s) == len(YEARS) for s in [US_M2, EU_M3, JP_M2, CN_M2, TW_M2])


def index_to_100(series):
    base = series[0]
    return [v / base * 100 for v in series]


def render_static_png(out_dir: str) -> None:
    series_idx = {
        "us": index_to_100(US_M2),
        "eu": index_to_100(EU_M3),
        "jp": index_to_100(JP_M2),
        "cn": index_to_100(CN_M2),
        "tw": index_to_100(TW_M2),
    }
    colors = {
        "us": "#0d47a1",
        "eu": "#5d4037",
        "jp": "#b71c1c",
        "cn": "#c62828",
        "tw": "#2e7d32",
    }
    line_styles = {
        "us": "-",
        "eu": "-",
        "jp": "-",
        "cn": "-",
        "tw": "--",
    }

    for lang in LANGS:
        L = LANG_LABELS[lang]
        fig, ax = plt.subplots(figsize=(11, 6.5))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        for key in ("us", "eu", "jp", "cn", "tw"):
            ax.plot(YEARS, series_idx[key], color=colors[key],
                    linewidth=2.4, linestyle=line_styles[key],
                    marker="o", markersize=3, markevery=3,
                    label=L[key])

        # COVID shading
        ax.axvspan(2020, 2022, color="#b71c1c", alpha=0.07)
        ax.text(2020.2, 1500, L["annot_covid"], fontsize=9.5,
                color="#b71c1c", alpha=0.85)

        # End-point annotations for the most extreme lines
        ax.annotate(L["annot_cn"],
                    xy=(2025, series_idx["cn"][-1]),
                    xytext=(2018, series_idx["cn"][-1] * 1.1),
                    fontsize=10, color=colors["cn"], fontweight="bold")
        ax.annotate(L["annot_us"],
                    xy=(2025, series_idx["us"][-1]),
                    xytext=(2018, series_idx["us"][-1] * 0.65),
                    fontsize=10, color=colors["us"], fontweight="bold")

        ax.set_yscale("log")
        ax.set_xlim(2000, 2025)
        ax.set_ylim(80, 3500)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(L["title"] + "\n" + L["subtitle"], fontsize=13, pad=10)
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(loc="upper left", fontsize=10)

        fname = "week01_money_supply.png" if lang == "en" \
            else f"week01_money_supply_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            shutil.copy2(out_path, os.path.join(out_dir, "week01_money_supply_en.png"))
        print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)
    render_static_png(out_dir)


if __name__ == "__main__":
    main()
