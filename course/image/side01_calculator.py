"""Render a stylized BA II Plus financial calculator illustration.

Procedurally drawn (no copyrighted product photo). Mirrors the layout
of the real Texas Instruments BA II Plus (1991-2014 design):

- Silver-grey face plate, black keypad area
- 9 rows x 5 cols key grid with the "=" key spanning two rows
- Row 1: CPT, ENTER, up-arrow, down-arrow, ON/OFF
- Row 2: 2nd, CF, NPV, IRR, right-arrow (worksheet next)
- Row 3: lighter silver TVM keys N, I/Y, PV, PMT, FV
- Numeric pad in lighter silver, function keys in dark charcoal
- White secondary labels above each key (the 2ND functions)

Run:
    uv run python course/image/side01_calculator.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from scripts.chart_helpers import apply_cjk_font  # noqa: E402

apply_cjk_font()

OUT_DIR = Path(__file__).parent

# Colour palette (mirrors the real BA II Plus standard model) ---------------
SHELL_OUTER = "#1a1a1a"   # outer bezel / dark trim
SHELL_FACE  = "#9aa0a4"   # silver-grey face plate (LCD area)
SHELL_KEYP  = "#1f1f1f"   # black keypad surround
LCD_BG      = "#bfc4a6"   # LCD greenish-grey
LCD_FG      = "#0c1207"
KEY_DARK    = "#2c2c2c"   # function keys (dark charcoal)
KEY_LIGHT   = "#b6b8b1"   # TVM + numeric keys (silver-grey)
KEY_2ND     = "#caa645"   # 2nd key gold/tan accent
KEY_RED     = "#a02020"   # CE/C accent
SEC_LBL     = "#ffffff"   # secondary labels are white on the dark device


# Locale-specific labels ----------------------------------------------------
LANG = {
    "en": {
        "subtitle":     "Advanced Financial Calculator",
        "caption_main": "Industry standard for CFA, CMT and bond-desk seats.",
        "lbl_2nd":   "2ND",   "lbl_cpt":   "CPT",
        "lbl_enter": "ENTER", "lbl_clr":   "CE|C",
        "lbl_onoff": "ON/OFF","lbl_cf":    "CF",
        "lbl_sto":   "STO",   "lbl_rcl":   "RCL",
        "sec": {
            "CPT": "QUIT", "ENTER": "SET", "↑": "DEL", "↓": "INS",
            "CF": "RESET", "NPV": "MEM", "IRR": "BOND",
            "N": "xP/Y", "I/Y": "P/Y", "PV": "AMORT", "PMT": "BGN", "FV": "CLR TVM",
            "%": "K", "÷": "RAND",
            "(": "SIN", ")": "COS", "y^x": "TAN", "×": "x!",
            "HYP": "INV",
            "7": "DATA", "8": "STAT", "9": "BOND", "-": "nPr",
            "STO": "RND", "5": "Δ%", "6": "BRKEVN", "+": "nCr",
            "RCL": "CLR WORK", "1": "ICONV", "2": "PROFIT", "3": "DEPR",
            "=": "ANS",
            "CE|C": "OFF", "0": "MEM", ".": "FORMAT", "+/-": "RESET",
        },
    },
    "hk": {
        "subtitle":     "高階財務計算機",
        "caption_main": "CFA、CMT 與債券交易檯的業界標準。",
        "lbl_2nd":   "2ND",   "lbl_cpt":   "計算",
        "lbl_enter": "輸入",  "lbl_clr":   "清除",
        "lbl_onoff": "開關",  "lbl_cf":    "現金流",
        "lbl_sto":   "存",    "lbl_rcl":   "取",
        "sec": {
            "計算": "離開", "輸入": "設定", "↑": "刪除", "↓": "插入",
            "現金流": "重設", "NPV": "記憶", "IRR": "債券",
            "N": "期×P/Y", "I/Y": "期/年", "PV": "攤還", "PMT": "期初", "FV": "清TVM",
            "%": "K", "÷": "亂數",
            "(": "SIN", ")": "COS", "y^x": "TAN", "×": "x!",
            "HYP": "INV",
            "7": "數據", "8": "統計", "9": "債券", "-": "nPr",
            "存": "捨入", "5": "Δ%", "6": "盈虧", "+": "nCr",
            "取": "清表", "1": "利率換", "2": "損益", "3": "折舊",
            "=": "答案",
            "清除": "關機", "0": "記憶", ".": "格式", "+/-": "重設",
        },
    },
    "tw": {
        "subtitle":     "進階財務計算機",
        "caption_main": "CFA、CMT 與債券交易桌的業界標準。",
        "lbl_2nd":   "2ND",   "lbl_cpt":   "計算",
        "lbl_enter": "輸入",  "lbl_clr":   "清除",
        "lbl_onoff": "開關",  "lbl_cf":    "現金流",
        "lbl_sto":   "儲存",  "lbl_rcl":   "取回",
        "sec": {
            "計算": "離開", "輸入": "設定", "↑": "刪除", "↓": "插入",
            "現金流": "重設", "NPV": "記憶", "IRR": "公債",
            "N": "期×P/Y", "I/Y": "期/年", "PV": "攤還", "PMT": "期初", "FV": "清TVM",
            "%": "K", "÷": "亂數",
            "(": "SIN", ")": "COS", "y^x": "TAN", "×": "x!",
            "HYP": "INV",
            "7": "資料", "8": "統計", "9": "公債", "-": "nPr",
            "儲存": "捨入", "5": "Δ%", "6": "損平", "+": "nCr",
            "取回": "清表", "1": "利率換", "2": "損益", "3": "折舊",
            "=": "答案",
            "清除": "關機", "0": "記憶", ".": "格式", "+/-": "重設",
        },
    },
    "cn": {
        "subtitle":     "高级财务计算器",
        "caption_main": "CFA、CMT 与债券交易台的行业标准。",
        "lbl_2nd":   "2ND",   "lbl_cpt":   "计算",
        "lbl_enter": "输入",  "lbl_clr":   "清除",
        "lbl_onoff": "开关",  "lbl_cf":    "现金流",
        "lbl_sto":   "存储",  "lbl_rcl":   "调用",
        "sec": {
            "计算": "退出", "输入": "设定", "↑": "删除", "↓": "插入",
            "现金流": "重置", "NPV": "记忆", "IRR": "债券",
            "N": "期×P/Y", "I/Y": "期/年", "PV": "摊还", "PMT": "期初", "FV": "清TVM",
            "%": "K", "÷": "随机",
            "(": "SIN", ")": "COS", "y^x": "TAN", "×": "x!",
            "HYP": "INV",
            "7": "数据", "8": "统计", "9": "债券", "-": "nPr",
            "存储": "舍入", "5": "Δ%", "6": "盈亏", "+": "nCr",
            "调用": "清表", "1": "利率换", "2": "损益", "3": "折旧",
            "=": "答案",
            "清除": "关机", "0": "记忆", ".": "格式", "+/-": "重置",
        },
    },
}


def make_rows(L):
    """Return the 9-row, 5-col grid as (label, kind) per cell.

    kind: 'second', 'tvm', 'memory', 'num', 'op', 'clr', 'onoff', 'normal'.
    A cell with label '=TALL' marks the lower half of the tall '=' key.
    """
    return [
        # Row 1: workspace navigation + ON/OFF on the top right
        [(L["lbl_cpt"], "normal"),  (L["lbl_enter"], "normal"),
         ("↑", "normal"),           ("↓", "normal"),
         (L["lbl_onoff"], "onoff")],
        # Row 2: 2nd + cash-flow worksheets + arrow
        [(L["lbl_2nd"], "second"), (L["lbl_cf"], "normal"),
         ("NPV", "normal"),         ("IRR", "normal"),
         ("→", "normal")],
        # Row 3: TVM (lighter silver keys)
        [("N", "tvm"), ("I/Y", "tvm"), ("PV", "tvm"),
         ("PMT", "tvm"), ("FV", "tvm")],
        # Row 4: math row 1
        [("%", "normal"), ("√x", "normal"), ("x²", "normal"),
         ("1/x", "normal"), ("÷", "op")],
        # Row 5: trig + parens + power + multiply
        [("HYP", "normal"), ("(", "normal"), (")", "normal"),
         ("y^x", "normal"), ("×", "op")],
        # Row 6: LN + 7-8-9 + minus
        [("LN", "normal"), ("7", "num"), ("8", "num"),
         ("9", "num"), ("-", "op")],
        # Row 7: STO + 4-5-6 + plus
        [(L["lbl_sto"], "memory"), ("4", "num"), ("5", "num"),
         ("6", "num"), ("+", "op")],
        # Row 8: RCL + 1-2-3 + = (= spans rows 8-9)
        [(L["lbl_rcl"], "memory"), ("1", "num"), ("2", "num"),
         ("3", "num"), ("=", "op")],
        # Row 9: CE/C + 0 + . + +/-  (col 5 occupied by tall =)
        [(L["lbl_clr"], "clr"), ("0", "num"), (".", "num"),
         ("+/-", "num"), ("=TALL", None)],
    ]


def kind_colors(kind):
    if kind == "tvm":     return KEY_LIGHT, "#1a1a1a"
    if kind == "num":     return KEY_LIGHT, "#1a1a1a"
    if kind == "op":      return KEY_DARK,  "#f0f0f0"
    if kind == "memory":  return KEY_DARK,  "#f0f0f0"
    if kind == "second":  return KEY_2ND,   "#1a1207"
    if kind == "clr":     return KEY_RED,   "#ffffff"
    if kind == "onoff":   return KEY_DARK,  "#f0f0f0"
    return KEY_DARK, "#f0f0f0"


def draw(ax, L):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 175)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor("#1a1a1a")

    # Outer dark shell
    ax.add_patch(FancyBboxPatch(
        (3, 3), 94, 169, boxstyle="round,pad=0,rounding_size=4.5",
        linewidth=0, facecolor=SHELL_OUTER, zorder=1,
    ))
    # Silver-grey face plate (upper section: branding + LCD)
    ax.add_patch(FancyBboxPatch(
        (6, 119), 88, 50, boxstyle="round,pad=0,rounding_size=2.5",
        linewidth=0, facecolor=SHELL_FACE, zorder=2,
    ))
    # Black keypad surround (lower section)
    ax.add_patch(FancyBboxPatch(
        (6, 6), 88, 110, boxstyle="round,pad=0,rounding_size=2.5",
        linewidth=0, facecolor=SHELL_KEYP, zorder=2,
    ))

    # Top branding (BA II PLUS, then TI logo + Texas Instruments)
    ax.text(50, 162, "BA II PLUS", color="#ffffff",
            ha="center", fontsize=12.5, weight="bold", zorder=4,
            family="DejaVu Sans")
    ax.text(50, 154, "TEXAS INSTRUMENTS", color="#ffffff",
            ha="center", fontsize=7.4, weight="bold", zorder=4,
            family="DejaVu Sans")
    ax.text(50, 149, L["subtitle"], color="#202020",
            ha="center", fontsize=6.6, style="italic", zorder=4)

    # LCD
    lcd_x, lcd_y, lcd_w, lcd_h = 14, 126, 72, 16
    ax.add_patch(FancyBboxPatch(
        (lcd_x, lcd_y), lcd_w, lcd_h, boxstyle="round,pad=0,rounding_size=1.0",
        linewidth=1.0, edgecolor="#3a3a3a", facecolor=LCD_BG, zorder=3,
    ))
    ax.text(lcd_x + lcd_w - 3, lcd_y + lcd_h/2, "PMT= 10,000.00",
            color=LCD_FG, ha="right", va="center",
            fontsize=12.5, weight="bold",
            family="DejaVu Sans Mono", zorder=4)
    # "BUSINESS ANALYST" tagline below the LCD
    ax.text(50, 122, "BUSINESS ANALYST", color="#3a3a3a",
            ha="center", fontsize=5.6, weight="bold",
            family="DejaVu Sans", zorder=4)

    # Key grid: 5 cols x 9 rows (real BA II Plus footprint)
    rows = make_rows(L)
    n_cols, n_rows = 5, len(rows)
    grid_x, grid_y = 9, 9
    grid_w, grid_h = 82, 105
    gap_x, gap_y = 1.5, 1.4
    key_w = (grid_w - gap_x * (n_cols - 1)) / n_cols
    key_h = (grid_h - gap_y * (n_rows - 1)) / n_rows

    for ri, row in enumerate(rows):
        y = grid_y + (n_rows - 1 - ri) * (key_h + gap_y)
        for ci, (label, kind) in enumerate(row):
            if label == "=TALL":
                continue  # placeholder; the "=" key above renders tall
            x = grid_x + ci * (key_w + gap_x)
            tall = (label == "=" and ri == 7)  # "=" spans rows 8-9
            h = key_h * 2 + gap_y if tall else key_h
            y_draw = y - (key_h + gap_y) if tall else y
            fc, tc = kind_colors(kind)
            # Drop shadow
            ax.add_patch(FancyBboxPatch(
                (x, y_draw - 0.5), key_w, h,
                boxstyle="round,pad=0,rounding_size=0.9",
                linewidth=0, facecolor="#000000", alpha=0.55, zorder=3,
            ))
            ax.add_patch(FancyBboxPatch(
                (x, y_draw), key_w, h,
                boxstyle="round,pad=0,rounding_size=0.9",
                linewidth=0.5, edgecolor="#0a0a0a",
                facecolor=fc, zorder=4,
            ))
            sec = L["sec"].get(label)
            if sec:
                ax.text(x + key_w/2, y_draw + h - 0.4, sec, color=SEC_LBL,
                        ha="center", va="top",
                        fontsize=4.6, weight="bold", zorder=5)
            ax.text(x + key_w/2, y_draw + h * 0.36, label, color=tc,
                    ha="center", va="center",
                    fontsize=7.2 if len(label) <= 4 else 5.8,
                    weight="bold", zorder=5)


def build_one(lang: str) -> None:
    fig, ax = plt.subplots(figsize=(6.5, 11.4), dpi=170)
    fig.patch.set_facecolor("#1a1a1a")
    draw(ax, LANG[lang])
    out = OUT_DIR / f"side01_calculator_{lang}.png"
    fig.savefig(out, dpi=170, bbox_inches="tight", facecolor=fig.get_facecolor())
    if lang == "en":
        fig.savefig(OUT_DIR / "side01_calculator.png", dpi=170,
                    bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  wrote {out.name}")


if __name__ == "__main__":
    for lang in ("en", "hk", "tw", "cn"):
        build_one(lang)
    print("done.")
