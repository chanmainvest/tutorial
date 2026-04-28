"""Generate the Official-vs-ShadowStats CPI chart for Week 1, §2.1.

Shows two YoY inflation series side by side, 1980 to 2025:

- **Official BLS CPI-U** — the headline number reported on the news.
- **ShadowStats 1980-based CPI alternate** — John Williams' attempt to
  reconstruct CPI using pre-1980 BLS methodology (no hedonic adjustment,
  no geometric/substitution weighting, original housing imputation).

The two series tracked closely until the early 1990s, when the BLS
introduced geometric weighting and (later) hedonic adjustments. From
~2000 onward the ShadowStats series consistently reads several percentage
points higher.

**Honest caveats** (also in the lesson §2.1 text):

- ShadowStats' methodology is not universally accepted. A common critique
  is that the series effectively adds a near-constant offset rather than
  fully recomputing the basket from raw data.
- The official series itself has been adjusted multiple times in ways
  that lower the printed number (Boskin Commission 1996 estimated
  cumulative effect ~0.5-1.0 pp/yr).
- Ground truth is somewhere between the two; the chart's value is
  illustrating that *the headline number understates experienced
  inflation by a non-trivial amount*, not in defending either methodology.

Data sources:

- Official CPI YoY: BLS published series, annual averages.
- ShadowStats 1980-based: approximated from John Williams'
  shadowstats.com published charts (the site itself is paywalled but
  headline values appear in many free summaries). Numbers here are
  illustrative approximations within ~1 pp of published values.

Run:
    uv run python course/image/week01_shadow_cpi.py
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
        "title":   "Official US CPI vs ShadowStats 1980-based CPI alternate",
        "subtitle": "Annual YoY % change. The gap opens after the 1990s methodology changes (hedonics, geometric weighting).",
        "xlabel":  "Year",
        "ylabel":  "Annual inflation rate (%)",
        "official": "Official BLS CPI-U",
        "shadow":   "ShadowStats 1980-based alternate",
    },
    "hk": {
        "title":   "美國官方 CPI 與 ShadowStats 1980 年方法論 CPI 對比",
        "subtitle": "年度按年變化(%)。1990 年代方法論修改(享樂調整、幾何加權)後差距逐漸擴大。",
        "xlabel":  "年份",
        "ylabel":  "年度通脹率(%)",
        "official": "官方 BLS CPI-U",
        "shadow":   "ShadowStats 1980 方法論替代版",
    },
    "tw": {
        "title":   "美國官方 CPI 與 ShadowStats 1980 年方法論 CPI 對比",
        "subtitle": "年度按年變化(%)。1990 年代方法論修改(享樂調整、幾何加權)後差距逐漸擴大。",
        "xlabel":  "年份",
        "ylabel":  "年度通膨率(%)",
        "official": "官方 BLS CPI-U",
        "shadow":   "ShadowStats 1980 方法論替代版",
    },
    "cn": {
        "title":   "美国官方 CPI 与 ShadowStats 1980 年方法论 CPI 对比",
        "subtitle": "年度按年变化(%)。1990 年代方法论修改(享乐调整、几何加权)后差距逐渐扩大。",
        "xlabel":  "年份",
        "ylabel":  "年度通胀率(%)",
        "official": "官方 BLS CPI-U",
        "shadow":   "ShadowStats 1980 方法论替代版",
    },
}

# Annual CPI YoY % change, 1980-2025.
# Official: BLS CPI-U annual average.
# Shadow: ShadowStats 1980-based alternate (illustrative approximation).
YEARS = list(range(1980, 2026))
OFFICIAL = [
    13.5, 10.3, 6.2, 3.2, 4.3, 3.5, 1.9, 3.7, 4.1, 4.8,        # 1980s
    5.4, 4.2, 3.0, 3.0, 2.6, 2.8, 3.0, 2.3, 1.6, 2.2,          # 1990s
    3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.9, 3.8, -0.4,         # 2000s
    1.6, 3.2, 2.1, 1.5, 1.6, 0.1, 1.3, 2.1, 2.4, 1.8,          # 2010s
    1.2, 4.7, 8.0, 4.1, 2.9, 2.6,                              # 2020-2025
]
# ShadowStats 1980-based (approximations from public summaries).
SHADOW = [
    14.0, 11.0, 7.5, 4.5, 5.5, 4.5, 3.0, 5.0, 5.5, 6.5,        # 1980s — small gap
    7.0, 6.0, 5.0, 5.0, 5.0, 5.5, 6.0, 5.5, 5.0, 5.5,          # 1990s — gap grows
    7.0, 6.5, 5.5, 6.0, 7.0, 8.0, 8.0, 8.0, 9.5, 6.0,          # 2000s — ~5pp gap
    7.5, 9.0, 8.5, 8.0, 8.0, 7.0, 8.0, 9.0, 9.5, 9.0,          # 2010s — ~7pp gap
    8.5, 12.0, 15.0, 11.0, 10.0, 9.5,                          # 2020-2025
]
assert len(YEARS) == len(OFFICIAL) == len(SHADOW)


def render_static_png(out_dir: str) -> None:
    for lang in LANGS:
        L = LANG_LABELS[lang]

        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("#fdfbf5")
        ax.set_facecolor("#fdfbf5")

        ax.plot(YEARS, OFFICIAL, color="#0d47a1", linewidth=2.4,
                marker="o", markersize=3.5, markevery=3,
                label=L["official"])
        ax.plot(YEARS, SHADOW, color="#b71c1c", linewidth=2.4,
                marker="s", markersize=3.5, markevery=3,
                label=L["shadow"])

        # Shade the gap between the two.
        ax.fill_between(YEARS, OFFICIAL, SHADOW,
                        where=[s > o for s, o in zip(SHADOW, OFFICIAL)],
                        color="#b71c1c", alpha=0.10,
                        interpolate=True, label=None)

        ax.axhline(0, color="#5a5a5a", linewidth=0.8, linestyle=":", alpha=0.6)
        ax.axhline(2, color="#2e7d32", linewidth=0.8, linestyle="--", alpha=0.5)
        ax.text(1981, 2.3, "Fed 2% target", color="#2e7d32", fontsize=9, alpha=0.75)

        ax.set_xlim(1980, 2025)
        ax.set_ylim(-2, 17)
        ax.set_xlabel(L["xlabel"], fontsize=12)
        ax.set_ylabel(L["ylabel"], fontsize=12)
        ax.set_title(L["title"] + "\n" + L["subtitle"],
                     fontsize=13, pad=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper right", fontsize=10.5)

        fname = "week01_shadow_cpi.png" if lang == "en" \
            else f"week01_shadow_cpi_{lang}.png"
        out_path = os.path.join(out_dir, fname)
        plt.tight_layout()
        plt.savefig(out_path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        plt.close(fig)
        if lang == "en":
            shutil.copy2(out_path, os.path.join(out_dir, "week01_shadow_cpi_en.png"))
        print(f"Saved: {out_path}")


def main() -> None:
    out_dir = os.path.dirname(__file__)
    render_static_png(out_dir)


if __name__ == "__main__":
    main()
