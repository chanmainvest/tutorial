"""Generate the SPIVA active-fund underperformance chart for Week 2, §2.4.

Grouped bar chart showing the percentage of actively managed funds that
underperformed their benchmark across 5/10/20-year horizons, broken out
by 6 categories (US Large/Mid/Small Cap, International, Emerging Markets,
US Investment-Grade Bond). The headline number — 90% of US large-cap
managers losing to the S&P 500 over a 20-year window — is annotated in
bold.

Data source: SPIVA scorecard from S&P Dow Jones Indices, approximate
figures from recent reports. The exact numbers wobble year to year; the
qualitative pattern (longer horizon → worse for active) does not.

Run:
    uv run --with matplotlib python course/image/week02_spiva.py
"""

from __future__ import annotations

import os
import shutil

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC", "PingFang SC",
    "Noto Sans CJK TC", "Noto Sans CJK SC", "SimHei", "Arial Unicode MS",
    "DejaVu Sans",
]
matplotlib.rcParams["axes.unicode_minus"] = False

LANGS = ("en", "hk", "tw", "cn")
LANG_LABELS = {
    "en": {
        "title":    "SPIVA: % of active funds underperforming the index",
        "subtitle": "Across six categories and three time horizons. The longer the window, the worse for active management.",
        "ylabel":   "% of active funds underperforming",
        "h5":       "5-year",
        "h10":      "10-year",
        "h20":      "20-year",
        "ann":      "90%",
        "cats": [
            "US Large-Cap", "US Mid-Cap", "US Small-Cap",
            "International", "Emerging Markets", "US IG Bond",
        ],
    },
    "hk": {
        "title":    "SPIVA:跑輸指數的主動型基金比例",
        "subtitle": "六個類別、三個時間窗口。窗口越長,主動管理越糟糕。",
        "ylabel":   "跑輸指數的主動型基金 %",
        "h5":       "5 年",
        "h10":      "10 年",
        "h20":      "20 年",
        "ann":      "90%",
        "cats": [
            "美國大型股", "美國中型股", "美國小型股",
            "國際股票", "新興市場", "美國投資級債券",
        ],
    },
    "tw": {
        "title":    "SPIVA:落後指數的主動型基金比例",
        "subtitle": "六個類別、三個時間窗口。窗口越長,主動管理越慘。",
        "ylabel":   "落後指數的主動型基金 %",
        "h5":       "5 年",
        "h10":      "10 年",
        "h20":      "20 年",
        "ann":      "90%",
        "cats": [
            "美國大型股", "美國中型股", "美國小型股",
            "國際股票", "新興市場", "美國投資級債券",
        ],
    },
    "cn": {
        "title":    "SPIVA:跑输指数的主动型基金比例",
        "subtitle": "六个类别、三个时间窗口。窗口越长,主动管理越糟糕。",
        "ylabel":   "跑输指数的主动型基金 %",
        "h5":       "5 年",
        "h10":      "10 年",
        "h20":      "20 年",
        "ann":      "90%",
        "cats": [
            "美国大型股", "美国中型股", "美国小型股",
            "国际股票", "新兴市场", "美国投资级债券",
        ],
    },
}

# SPIVA underperformance % — see §2.4 of week02_index_funds_etfs.md
DATA_5Y  = [78, 74, 68, 71, 69, 72]
DATA_10Y = [85, 83, 79, 82, 80, 81]
DATA_20Y = [90, 89, 88, 87, 85, 86]

# Red-orange-dark-red gradient (longer horizon = darker)
COLOR_5Y  = "#f4a261"   # warm orange
COLOR_10Y = "#e63946"   # red
COLOR_20Y = "#7f0000"   # dark red


def render_static_png(out_dir: str) -> None:
    n_cats = len(DATA_5Y)
    x = np.arange(n_cats)
    bar_w = 0.26

    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        b1 = ax.bar(x - bar_w, DATA_5Y,  bar_w, label=L["h5"],
                    color=COLOR_5Y,  edgecolor="white", linewidth=0.6)
        b2 = ax.bar(x,         DATA_10Y, bar_w, label=L["h10"],
                    color=COLOR_10Y, edgecolor="white", linewidth=0.6)
        b3 = ax.bar(x + bar_w, DATA_20Y, bar_w, label=L["h20"],
                    color=COLOR_20Y, edgecolor="white", linewidth=0.6)

        # Value labels on top of every bar
        for bars, vals in [(b1, DATA_5Y), (b2, DATA_10Y), (b3, DATA_20Y)]:
            for rect, v in zip(bars, vals):
                ax.text(rect.get_x() + rect.get_width() / 2,
                        v + 1.0,
                        f"{v}%",
                        ha="center", va="bottom",
                        fontsize=8.5, color="#3a3a3a")

        # Headline annotation: US Large-Cap 20Y bar — bold "90%"
        head_x = x[0] + bar_w
        head_y = DATA_20Y[0]
        ax.annotate(L["ann"],
                    xy=(head_x, head_y),
                    xytext=(head_x + 0.55, head_y + 7),
                    fontsize=18, fontweight="bold", color="#7f0000",
                    arrowprops=dict(arrowstyle="->", color="#7f0000",
                                    lw=1.6, shrinkA=4, shrinkB=4))

        ax.set_ylim(0, 105)
        ax.set_xticks(x)
        ax.set_xticklabels(L["cats"], fontsize=10, rotation=15, ha="right")
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(L["title"] + "\n" + L["subtitle"], fontsize=13, pad=10)
        ax.yaxis.set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda v, _: f"{int(v)}%")
        )
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.legend(loc="lower right", fontsize=10.5, framealpha=0.95)

        # Reference 50% line
        ax.axhline(50, color="#5a5a5a", linewidth=0.8,
                   linestyle=":", alpha=0.6)

        fname = "week02_spiva.png" if lang == "en" \
            else f"week02_spiva_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            shutil.copy2(out_path, os.path.join(out_dir, "week02_spiva_en.png"))
        print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)
    render_static_png(out_dir)


if __name__ == "__main__":
    main()
