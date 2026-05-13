"""Side Lesson 04, §2.2 — Asset location grid.

Three account columns (Taxable / Traditional IRA / Roth IRA) by eight
common asset sleeves. Each cell is colour-coded for whether that
sleeve belongs in that account: green = best, amber = acceptable,
red = wrong. A short reason fragment sits inside each cell.

Run:
    uv run python course/image/side04_asset_location_grid.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.chart_helpers import (  # noqa: E402
    PALETTE_LIGHT,
    apply_cjk_font,
    render_for_all_locales,
)

apply_cjk_font()
OUT_DIR = Path(__file__).parent
BASE = "side04_asset_location_grid"


# Score: 2 = best, 1 = acceptable, 0 = worst.
# Order columns: taxable, trad, roth.
ASSETS = [
    ("us_stock",  [2, 1, 2]),
    ("intl",      [2, 0, 1]),
    ("ig_bond",   [0, 2, 1]),
    ("hy_bond",   [0, 2, 2]),
    ("reit",      [0, 2, 2]),
    ("tips",      [0, 2, 1]),
    ("mlp",       [2, 0, 0]),
    ("growth",    [1, 1, 2]),
]

REASON_KEYS = {
    ("us_stock",  0): "lo_div_ltcg",
    ("us_stock",  1): "wastes_def",
    ("us_stock",  2): "ok_growth",
    ("intl",      0): "ftc_only",
    ("intl",      1): "loses_ftc",
    ("intl",      2): "loses_ftc_ok",
    ("ig_bond",   0): "ord_drag",
    ("ig_bond",   1): "defer_int",
    ("ig_bond",   2): "wastes_growth",
    ("hy_bond",   0): "huge_ord",
    ("hy_bond",   1): "shelter_ord",
    ("hy_bond",   2): "shelter_ord_alt",
    ("reit",      0): "non_qual",
    ("reit",      1): "shelter_reit",
    ("reit",      2): "shelter_reit_alt",
    ("tips",      0): "phantom",
    ("tips",      1): "no_phantom",
    ("tips",      2): "ok_no_phantom",
    ("mlp",       0): "k1_ok",
    ("mlp",       1): "ubti",
    ("mlp",       2): "ubti2",
    ("growth",    0): "defer_gain",
    ("growth",    1): "ord_at_with",
    ("growth",    2): "tax_free_compound",
}


LANG_STRINGS = {
    "en": {
        "title":    "Asset location grid - where each sleeve belongs",
        "subtitle": "Green: best location.  Amber: acceptable.  Red: avoid.  Bracket assumed 32% federal + 5% state.",
        "footer":   "Rules: tax-inefficient income (bonds, REITs, TIPS) sheltered in IRA.  LTCG-eligible stocks stay in taxable.  Highest-expected-return assets go to Roth.  MLPs trigger UBIT inside any IRA.",
        "col_tax":  "Taxable brokerage",
        "col_trad": "Traditional IRA / 401(k)",
        "col_roth": "Roth IRA",
        "asset_labels": {
            "us_stock": "US stocks (VTI / SPY)",
            "intl":     "Intl stocks (VXUS / IEFA)",
            "ig_bond":  "IG bonds (BND / AGG)",
            "hy_bond":  "HY bonds (HYG / JNK)",
            "reit":     "REITs (VNQ / SCHH)",
            "tips":     "TIPS (SCHP / VTIP)",
            "mlp":      "MLPs / energy K-1",
            "growth":   "High-growth / crypto",
        },
        "reasons": {
            "lo_div_ltcg":      "Low yield, LTCG efficient",
            "wastes_def":       "Wastes deferral",
            "ok_growth":        "OK; growth tax-free",
            "ftc_only":         "Foreign tax credit",
            "loses_ftc":        "Loses FTC",
            "loses_ftc_ok":     "Loses FTC; OK growth",
            "ord_drag":         "Ordinary income drag 1.6%",
            "defer_int":        "Defers ordinary income",
            "wastes_growth":    "Wastes Roth on bonds",
            "huge_ord":         "Ord. drag 3%/yr",
            "shelter_ord":      "Best - shelter HY income",
            "shelter_ord_alt":  "Strong - sheltered HY",
            "non_qual":         "Non-qualified div = ord.",
            "shelter_reit":     "Shelters REIT ord. income",
            "shelter_reit_alt": "Strong - sheltered REIT",
            "phantom":          "Phantom-income tax bill",
            "no_phantom":       "No phantom-income issue",
            "ok_no_phantom":    "OK; phantom OK in Roth",
            "k1_ok":            "K-1 ok; basis benefits",
            "ubti":             "UBIT > 1k -> 990-T",
            "ubti2":            "UBIT > 1k -> 990-T",
            "defer_gain":       "Cap-gain deferral",
            "ord_at_with":      "Gains -> ord. on draw",
            "tax_free_compound":"Tax-free compounding",
        },
    },
    "hk": {
        "title":    "資產定位格 - 每個板塊應放哪個帳戶",
        "subtitle": "綠:最佳。橙:可接受。紅:避免。假設 32% 聯邦 + 5% 州稅階。",
        "footer":   "規則:稅務低效收入(債券、REITs、TIPS)放 IRA;符合 LTCG 的股票留在應稅;最高預期回報資產進 Roth;MLPs 在任何 IRA 內觸發 UBIT。",
        "col_tax":  "應稅帳戶",
        "col_trad": "Traditional IRA / 401(k)",
        "col_roth": "Roth IRA",
        "asset_labels": {
            "us_stock": "美股(VTI / SPY)",
            "intl":     "國際股(VXUS / IEFA)",
            "ig_bond":  "投資級債(BND / AGG)",
            "hy_bond":  "高息債(HYG / JNK)",
            "reit":     "REITs(VNQ / SCHH)",
            "tips":     "TIPS(SCHP / VTIP)",
            "mlp":      "MLPs / 能源 K-1",
            "growth":   "高增長 / 加密",
        },
        "reasons": {
            "lo_div_ltcg":      "低殖利率,LTCG 高效",
            "wastes_def":       "浪費遞延",
            "ok_growth":        "可;增長免稅",
            "ftc_only":         "外國稅收抵免",
            "loses_ftc":        "失去 FTC",
            "loses_ftc_ok":     "失 FTC;增長可",
            "ord_drag":         "普通稅拖累 1.6%",
            "defer_int":        "遞延普通收入",
            "wastes_growth":    "Roth 浪費於債",
            "huge_ord":         "普通稅拖累 3%/年",
            "shelter_ord":      "最佳 - 庇護高息",
            "shelter_ord_alt":  "強 - 高息庇護",
            "non_qual":         "非合格 = 普通稅",
            "shelter_reit":     "庇護 REIT 普通收入",
            "shelter_reit_alt": "強 - REIT 庇護",
            "phantom":          "幻影所得稅",
            "no_phantom":       "無幻影問題",
            "ok_no_phantom":    "可;Roth 內 OK",
            "k1_ok":            "K-1 OK;成本回收",
            "ubti":             "UBIT > 1千 -> 990-T",
            "ubti2":            "UBIT > 1千 -> 990-T",
            "defer_gain":       "資本利得遞延",
            "ord_at_with":      "提領變普通稅",
            "tax_free_compound":"免稅複利",
        },
    },
    "tw": {
        "title":    "資產定位格 - 每個部位應放哪個帳戶",
        "subtitle": "綠:最佳。橙:可接受。紅:避免。假設 32% 聯邦 + 5% 州稅階。",
        "footer":   "規則:稅務低效收入(債券、REITs、TIPS)放 IRA;符合 LTCG 的股票留在應稅;最高預期報酬資產進 Roth;MLPs 在任何 IRA 內觸發 UBIT。",
        "col_tax":  "應稅帳戶",
        "col_trad": "Traditional IRA / 401(k)",
        "col_roth": "Roth IRA",
        "asset_labels": {
            "us_stock": "美股(VTI / SPY)",
            "intl":     "國際股(VXUS / IEFA)",
            "ig_bond":  "投資級債(BND / AGG)",
            "hy_bond":  "高息債(HYG / JNK)",
            "reit":     "REITs(VNQ / SCHH)",
            "tips":     "TIPS(SCHP / VTIP)",
            "mlp":      "MLPs / 能源 K-1",
            "growth":   "高成長 / 加密",
        },
        "reasons": {
            "lo_div_ltcg":      "低殖利率,LTCG 高效",
            "wastes_def":       "浪費遞延",
            "ok_growth":        "可;成長免稅",
            "ftc_only":         "外國稅收抵免",
            "loses_ftc":        "失去 FTC",
            "loses_ftc_ok":     "失 FTC;成長可",
            "ord_drag":         "普通稅拖累 1.6%",
            "defer_int":        "遞延普通收入",
            "wastes_growth":    "Roth 浪費於債",
            "huge_ord":         "普通稅拖累 3%/年",
            "shelter_ord":      "最佳 - 庇護高息",
            "shelter_ord_alt":  "強 - 高息庇護",
            "non_qual":         "非合格 = 普通稅",
            "shelter_reit":     "庇護 REIT 普通收入",
            "shelter_reit_alt": "強 - REIT 庇護",
            "phantom":          "幻影所得稅",
            "no_phantom":       "無幻影問題",
            "ok_no_phantom":    "可;Roth 內 OK",
            "k1_ok":            "K-1 OK;成本回收",
            "ubti":             "UBIT > 1千 -> 990-T",
            "ubti2":            "UBIT > 1千 -> 990-T",
            "defer_gain":       "資本利得遞延",
            "ord_at_with":      "提領變普通稅",
            "tax_free_compound":"免稅複利",
        },
    },
    "cn": {
        "title":    "资产定位格 - 每个板块应放哪个账户",
        "subtitle": "绿:最佳。橙:可接受。红:避免。假设 32% 联邦 + 5% 州税阶。",
        "footer":   "规则:税务低效收入(债券、REITs、TIPS)放 IRA;符合 LTCG 的股票留在应税;最高预期回报资产进 Roth;MLPs 在任何 IRA 内触发 UBIT。",
        "col_tax":  "应税账户",
        "col_trad": "Traditional IRA / 401(k)",
        "col_roth": "Roth IRA",
        "asset_labels": {
            "us_stock": "美股(VTI / SPY)",
            "intl":     "国际股(VXUS / IEFA)",
            "ig_bond":  "投资级债(BND / AGG)",
            "hy_bond":  "高息债(HYG / JNK)",
            "reit":     "REITs(VNQ / SCHH)",
            "tips":     "TIPS(SCHP / VTIP)",
            "mlp":      "MLPs / 能源 K-1",
            "growth":   "高增长 / 加密",
        },
        "reasons": {
            "lo_div_ltcg":      "低收益率,LTCG 高效",
            "wastes_def":       "浪费递延",
            "ok_growth":        "可;增长免税",
            "ftc_only":         "外国税收抵免",
            "loses_ftc":        "失去 FTC",
            "loses_ftc_ok":     "失 FTC;增长可",
            "ord_drag":         "普通税拖累 1.6%",
            "defer_int":        "递延普通收入",
            "wastes_growth":    "Roth 浪费于债",
            "huge_ord":         "普通税拖累 3%/年",
            "shelter_ord":      "最佳 - 庇护高息",
            "shelter_ord_alt":  "强 - 高息庇护",
            "non_qual":         "非合格 = 普通税",
            "shelter_reit":     "庇护 REIT 普通收入",
            "shelter_reit_alt": "强 - REIT 庇护",
            "phantom":          "幻影所得税",
            "no_phantom":       "无幻影问题",
            "ok_no_phantom":    "可;Roth 内 OK",
            "k1_ok":            "K-1 OK;成本回收",
            "ubti":             "UBIT > 1千 -> 990-T",
            "ubti2":            "UBIT > 1千 -> 990-T",
            "defer_gain":       "资本利得递延",
            "ord_at_with":      "提领变普通税",
            "tax_free_compound":"免税复利",
        },
    },
}


def _color_for_score(score: int, p: dict) -> tuple[str, str]:
    if score == 2:
        return ("#9fcfa3", p["green"])    # green tint
    if score == 1:
        return ("#f3d99a", p["accent"])   # amber tint
    return ("#e8a8a8", p["red"])          # red tint


def build_fig(s):
    p = PALETTE_LIGHT
    fig, ax = plt.subplots(figsize=(11.5, 7.6), dpi=150)
    ax.set_facecolor(p["bg"])
    fig.set_facecolor(p["bg"])

    n_rows = len(ASSETS)
    col_x = [0.0, 1.0, 2.0]
    cell_w = 0.95
    cell_h = 0.86

    headers = [s["col_tax"], s["col_trad"], s["col_roth"]]
    for j, h in enumerate(headers):
        ax.text(col_x[j] + cell_w / 2, n_rows + 0.10, h,
                ha="center", va="center",
                fontsize=11, fontweight="bold", color=p["fg"])

    for i, (key, scores) in enumerate(ASSETS):
        y = n_rows - 1 - i
        ax.text(-0.08, y + cell_h / 2,
                s["asset_labels"][key],
                ha="right", va="center",
                fontsize=10, fontweight="bold", color=p["fg"])
        for j, score in enumerate(scores):
            fill, edge = _color_for_score(score, p)
            rect = mpatches.FancyBboxPatch(
                (col_x[j], y), cell_w, cell_h,
                boxstyle="round,pad=0.005,rounding_size=0.04",
                facecolor=fill, edgecolor=edge, linewidth=1.4)
            ax.add_patch(rect)
            reason = s["reasons"][REASON_KEYS[(key, j)]]
            ax.text(col_x[j] + cell_w / 2, y + cell_h / 2,
                    reason, ha="center", va="center",
                    fontsize=8.6, color="#1a2332")

    ax.set_xlim(-1.7, 3.05)
    ax.set_ylim(-0.6, n_rows + 0.6)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_title(s["title"], pad=24, fontsize=15, weight="bold",
                 color=p["fg"])
    fig.text(0.5, 0.93, s["subtitle"], ha="center",
             fontsize=10.0, color="#4a5568", style="italic")
    fig.text(0.5, 0.03, s["footer"], ha="center",
             fontsize=8.5, color=p["muted"], wrap=True)

    fig.tight_layout(rect=[0.02, 0.06, 0.98, 0.92])
    return fig


if __name__ == "__main__":
    render_for_all_locales(BASE, OUT_DIR, build_fig, LANG_STRINGS)
