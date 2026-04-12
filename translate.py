#!/usr/bin/env python3
"""
Translation helper for Investment Tutorial Course.

This script provides a framework for translating course materials
from English to three Chinese variants:
- HK (Hong Kong Traditional Chinese)
- TW (Taiwan Traditional Chinese)
- CN (Mainland Simplified Chinese)

Usage:
    python translate.py              # Translate all files
    python translate.py week01       # Translate specific file
    python translate.py --check      # Check which files need translation

The translations preserve markdown formatting and adapt financial
terminology to each locale's conventions.
"""

import os
import re
import sys

# Financial terminology mapping for each locale
# Key: English term -> {hk: HK term, tw: TW term, cn: CN term}
FINANCIAL_TERMS = {
    # Basic terms
    "stock": {"hk": "股票", "tw": "股票", "cn": "股票"},
    "bond": {"hk": "債券", "tw": "債券", "cn": "债券"},
    "portfolio": {"hk": "投資組合", "tw": "投資組合", "cn": "投资组合"},
    "dividend": {"hk": "股息", "tw": "股利", "cn": "股息"},
    "index fund": {"hk": "指數基金", "tw": "指數基金", "cn": "指数基金"},
    "ETF": {"hk": "交易所買賣基金", "tw": "指數股票型基金", "cn": "交易所交易基金"},
    "mutual fund": {"hk": "互惠基金", "tw": "共同基金", "cn": "共同基金"},
    "return": {"hk": "回報", "tw": "報酬", "cn": "收益"},
    "yield": {"hk": "收益率", "tw": "殖利率", "cn": "收益率"},
    "interest rate": {"hk": "利率", "tw": "利率", "cn": "利率"},
    "inflation": {"hk": "通脹", "tw": "通膨", "cn": "通胀"},
    "risk": {"hk": "風險", "tw": "風險", "cn": "风险"},
    "volatility": {"hk": "波動性", "tw": "波動性", "cn": "波动性"},
    "asset allocation": {"hk": "資產配置", "tw": "資產配置", "cn": "资产配置"},
    "rebalancing": {"hk": "再平衡", "tw": "再平衡", "cn": "再平衡"},

    # Options terms
    "call option": {"hk": "認購期權", "tw": "買權", "cn": "看涨期权"},
    "put option": {"hk": "認沽期權", "tw": "賣權", "cn": "看跌期权"},
    "strike price": {"hk": "行使價", "tw": "履約價", "cn": "行权价"},
    "expiration": {"hk": "到期日", "tw": "到期日", "cn": "到期日"},
    "premium": {"hk": "期權金", "tw": "權利金", "cn": "期权费"},
    "covered call": {"hk": "備兌認購期權", "tw": "掩護性買權", "cn": "备兑看涨期权"},
    "warrant": {"hk": "窩輪", "tw": "權證", "cn": "权证"},

    # Market terms
    "bull market": {"hk": "牛市", "tw": "多頭市場", "cn": "牛市"},
    "bear market": {"hk": "熊市", "tw": "空頭市場", "cn": "熊市"},
    "market cap": {"hk": "市值", "tw": "市值", "cn": "市值"},
    "P/E ratio": {"hk": "市盈率", "tw": "本益比", "cn": "市盈率"},
    "earnings": {"hk": "盈利", "tw": "盈餘", "cn": "盈利"},

    # Fixed income
    "coupon": {"hk": "票息", "tw": "票面利率", "cn": "票息"},
    "duration": {"hk": "存續期", "tw": "存續期間", "cn": "久期"},
    "credit spread": {"hk": "信用利差", "tw": "信用利差", "cn": "信用利差"},
    "yield curve": {"hk": "收益率曲線", "tw": "殖利率曲線", "cn": "收益率曲线"},

    # Advanced terms
    "futures": {"hk": "期貨", "tw": "期貨", "cn": "期货"},
    "leverage": {"hk": "槓桿", "tw": "槓桿", "cn": "杠杆"},
    "hedge": {"hk": "對沖", "tw": "避險", "cn": "对冲"},
    "short selling": {"hk": "沽空", "tw": "放空", "cn": "做空"},
    "margin": {"hk": "保證金", "tw": "保證金", "cn": "保证金"},
    "drawdown": {"hk": "回撤", "tw": "回撤", "cn": "回撤"},
    "Sharpe ratio": {"hk": "夏普比率", "tw": "夏普比率", "cn": "夏普比率"},
}


def get_source_files(course_dir="course", pattern=None):
    """Get list of markdown files to translate."""
    files = []
    for f in sorted(os.listdir(course_dir)):
        if f.endswith('.md'):
            if pattern is None or pattern in f:
                files.append(f)
    return files


def check_translations():
    """Check which files need translation."""
    source_files = get_source_files()
    missing = {"hk": [], "tw": [], "cn": []}

    for f in source_files:
        for lang in ["hk", "tw", "cn"]:
            lang_dir = f"course_{lang}"
            if not os.path.exists(os.path.join(lang_dir, f)):
                missing[lang].append(f)

    print("Translation Status:")
    print(f"  Source files: {len(source_files)}")
    for lang in ["hk", "tw", "cn"]:
        translated = len(source_files) - len(missing[lang])
        print(f"  {lang.upper()}: {translated}/{len(source_files)} translated ({len(missing[lang])} missing)")
        if missing[lang]:
            for f in missing[lang][:5]:
                print(f"    - {f}")
            if len(missing[lang]) > 5:
                print(f"    ... and {len(missing[lang]) - 5} more")


def create_placeholder_translations(source_file, source_dir="course"):
    """Create placeholder translation files for a source file."""
    source_path = os.path.join(source_dir, source_file)
    if not os.path.exists(source_path):
        print(f"Source file not found: {source_path}")
        return

    content = open(source_path, 'r', encoding='utf-8').read()

    for lang in ["hk", "tw", "cn"]:
        lang_dir = f"course_{lang}"
        os.makedirs(lang_dir, exist_ok=True)
        target_path = os.path.join(lang_dir, source_file)

        if os.path.exists(target_path):
            print(f"  {lang.upper()}: Already exists, skipping")
            continue

        # Create a placeholder with the original content
        # In production, this would call a translation API
        header = {
            "hk": "<!-- 此檔案需要翻譯為香港繁體中文 -->\n<!-- This file needs translation to HK Traditional Chinese -->\n\n",
            "tw": "<!-- 此檔案需要翻譯為台灣繁體中文 -->\n<!-- This file needs translation to TW Traditional Chinese -->\n\n",
            "cn": "<!-- 此文件需要翻译为简体中文 -->\n<!-- This file needs translation to Simplified Chinese -->\n\n",
        }

        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(header[lang] + content)

        print(f"  {lang.upper()}: Created placeholder at {target_path}")


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--check':
            check_translations()
        else:
            pattern = sys.argv[1]
            files = get_source_files(pattern=pattern)
            for f in files:
                print(f"\nProcessing: {f}")
                create_placeholder_translations(f)
    else:
        files = get_source_files()
        print(f"Creating placeholder translations for {len(files)} files...\n")
        for f in files:
            print(f"Processing: {f}")
            create_placeholder_translations(f)
        print(f"\nDone! Created placeholders for {len(files)} files in course_hk/, course_tw/, course_cn/")
        print("These placeholders contain the English content and need manual or AI translation.")


if __name__ == '__main__':
    main()
