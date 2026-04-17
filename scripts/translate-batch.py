#!/usr/bin/env python3
"""
Automated Translation for Chanma Investment Tutorial

Translates English course markdown files to three Chinese variants
using the Anthropic Claude API.

Usage:
    python scripts/translate-batch.py --locale hk          # Translate all to HK Chinese
    python scripts/translate-batch.py --locale all          # Translate all locales
    python scripts/translate-batch.py --locale tw --file week01  # Translate one file
    python scripts/translate-batch.py --locale cn --force   # Overwrite existing
    python scripts/translate-batch.py --locale hk --dry-run # Preview without writing

Requires: ANTHROPIC_API_KEY environment variable
Install:  pip install anthropic
"""

import argparse
import os
import sys

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Locale configuration
# ---------------------------------------------------------------------------
LOCALE_CONFIG = {
    "hk": {
        "name": "Hong Kong Traditional Chinese",
        "script": "繁體中文",
        "dir": "course_hk",
        "description": "Hong Kong Traditional Chinese (繁體). Use Hong Kong financial terminology and conventions.",
    },
    "tw": {
        "name": "Taiwan Traditional Chinese",
        "script": "繁體中文",
        "dir": "course_tw",
        "description": "Taiwan Traditional Chinese (繁體). Use Taiwan financial terminology and conventions.",
    },
    "cn": {
        "name": "Mainland Simplified Chinese",
        "script": "簡體中文",
        "dir": "course_cn",
        "description": "Mainland Simplified Chinese (簡體). Use Mainland China financial terminology and conventions.",
    },
}

# ---------------------------------------------------------------------------
# Financial terminology — locale-specific translations
# ---------------------------------------------------------------------------
TERMINOLOGY = {
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
    "call option": {"hk": "認購期權", "tw": "買權", "cn": "看涨期权"},
    "put option": {"hk": "認沽期權", "tw": "賣權", "cn": "看跌期权"},
    "strike price": {"hk": "行使價", "tw": "履約價", "cn": "行权价"},
    "expiration": {"hk": "到期日", "tw": "到期日", "cn": "到期日"},
    "premium": {"hk": "期權金", "tw": "權利金", "cn": "期权费"},
    "covered call": {"hk": "備兌認購期權", "tw": "掩護性買權", "cn": "备兑看涨期权"},
    "warrant": {"hk": "窩輪", "tw": "權證", "cn": "权证"},
    "bull market": {"hk": "牛市", "tw": "多頭市場", "cn": "牛市"},
    "bear market": {"hk": "熊市", "tw": "空頭市場", "cn": "熊市"},
    "market cap": {"hk": "市值", "tw": "市值", "cn": "市值"},
    "P/E ratio": {"hk": "市盈率", "tw": "本益比", "cn": "市盈率"},
    "earnings": {"hk": "盈利", "tw": "盈餘", "cn": "盈利"},
    "coupon": {"hk": "票息", "tw": "票面利率", "cn": "票息"},
    "duration": {"hk": "存續期", "tw": "存續期間", "cn": "久期"},
    "credit spread": {"hk": "信用利差", "tw": "信用利差", "cn": "信用利差"},
    "yield curve": {"hk": "收益率曲線", "tw": "殖利率曲線", "cn": "收益率曲线"},
    "futures": {"hk": "期貨", "tw": "期貨", "cn": "期货"},
    "leverage": {"hk": "槓桿", "tw": "槓桿", "cn": "杠杆"},
    "hedge": {"hk": "對沖", "tw": "避險", "cn": "对冲"},
    "short selling": {"hk": "沽空", "tw": "放空", "cn": "做空"},
    "margin": {"hk": "保證金", "tw": "保證金", "cn": "保证金"},
    "drawdown": {"hk": "回撤", "tw": "回撤", "cn": "回撤"},
    "Sharpe ratio": {"hk": "夏普比率", "tw": "夏普比率", "cn": "夏普比率"},
    "cash-secured put": {"hk": "現金擔保認沽期權", "tw": "現金擔保賣權", "cn": "现金担保看跌期权"},
    "iron condor": {"hk": "鐵鷹式策略", "tw": "鐵禿鷹策略", "cn": "铁鹰策略"},
    "LEAPS": {"hk": "長期期權", "tw": "長期期權", "cn": "长期期权"},
    "VIX": {"hk": "波動率指數", "tw": "波動率指數", "cn": "波动率指数"},
    "Value at Risk": {"hk": "風險值", "tw": "風險值", "cn": "风险价值"},
    "alpha": {"hk": "阿爾法", "tw": "阿爾法", "cn": "阿尔法"},
    "beta": {"hk": "貝塔", "tw": "貝塔", "cn": "贝塔"},
    "factor investing": {"hk": "因子投資", "tw": "因子投資", "cn": "因子投资"},
    "momentum": {"hk": "動量", "tw": "動能", "cn": "动量"},
    "REIT": {"hk": "房地產信託基金", "tw": "不動產投資信託", "cn": "房地产投资信托"},
    "dollar cost averaging": {"hk": "平均成本法", "tw": "定期定額投資", "cn": "定投"},
    "financial statement": {"hk": "財務報表", "tw": "財務報表", "cn": "财务报表"},
    "income statement": {"hk": "損益表", "tw": "損益表", "cn": "利润表"},
    "balance sheet": {"hk": "資產負債表", "tw": "資產負債表", "cn": "资产负债表"},
    "cash flow statement": {"hk": "現金流量表", "tw": "現金流量表", "cn": "现金流量表"},
    "sector rotation": {"hk": "板塊輪動", "tw": "類股輪動", "cn": "板块轮动"},
    "backtesting": {"hk": "回測", "tw": "回測", "cn": "回测"},
    "tail risk": {"hk": "尾部風險", "tw": "尾部風險", "cn": "尾部风险"},
    "structured product": {"hk": "結構性產品", "tw": "結構型商品", "cn": "结构化产品"},
    "trend following": {"hk": "趨勢跟蹤", "tw": "趨勢跟隨", "cn": "趋势跟踪"},
}


def build_system_prompt(locale):
    config = LOCALE_CONFIG[locale]
    term_table = "\n".join(
        f"  {en} → {t[locale]}" for en, t in TERMINOLOGY.items()
    )

    return f"""You are an expert financial content translator specializing in {config['name']}.

TARGET: {config['description']}

FINANCIAL TERMINOLOGY — always use these exact translations:
{term_table}

RULES:
1. Translate ALL text content including section headers.
2. Preserve ALL markdown formatting exactly (headers, lists, tables, code blocks, links, bold, italic).
3. Preserve [VISUAL], [ANIMATION], and [CUT TO] tags in English — do NOT translate them.
4. Preserve host names "Horace" and "Stella" without translating. Translate their Chinese names: Horace is 陳馬, Stella is 小魚.
5. Preserve animation file paths (e.g., animation/week01_compound_growth.py) without translating.
6. Preserve ASCII art diagrams — translate only the text labels within them.
7. Output ONLY the translated markdown. No preamble, no commentary, no wrapping.
8. The YouTube script dialogue must sound natural and conversational in {config['script']}."""


def is_placeholder(file_path):
    if not os.path.exists(file_path):
        return True
    with open(file_path, "r", encoding="utf-8") as f:
        head = f.read(200)
    return "This file needs translation" in head


def translate_file(client, source_file, locale, force=False, dry_run=False):
    source_dir = os.path.join(PROJECT_ROOT, "course")
    target_dir = os.path.join(PROJECT_ROOT, LOCALE_CONFIG[locale]["dir"])
    source_path = os.path.join(source_dir, source_file)
    target_path = os.path.join(target_dir, source_file)

    # Skip if already translated (unless --force)
    if not force and os.path.exists(target_path) and not is_placeholder(target_path):
        return {"status": "skipped", "file": source_file, "locale": locale}

    if dry_run:
        return {"status": "dry-run", "file": source_file, "locale": locale}

    content = open(source_path, "r", encoding="utf-8").read()

    try:
        # Use streaming to handle large files that take >10 minutes
        translated = ""
        input_tokens = 0
        output_tokens = 0
        with client.messages.stream(
            model="claude-sonnet-4-6-20250514",
            max_tokens=65536,
            thinking={
                "type": "enabled",
                "budget_tokens": 8000,
            },
            system=build_system_prompt(locale),
            messages=[{"role": "user", "content": content}],
        ) as stream:
            response = stream.get_final_message()

        # Extract text from response (skip thinking blocks)
        for block in response.content:
            if block.type == "text":
                translated += block.text
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

        # Strip any accidental preamble
        first_header = translated.find("#")
        if 0 < first_header < 100:
            translated = translated[first_header:]

        os.makedirs(target_dir, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(translated)

        return {
            "status": "translated",
            "file": source_file,
            "locale": locale,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        }
    except Exception as e:
        return {"status": "error", "file": source_file, "locale": locale, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Translate investment tutorial course files")
    parser.add_argument("--locale", required=True, help="Target locale: hk, tw, cn, or all")
    parser.add_argument("--file", dest="file_pattern", help="Only translate files matching pattern")
    parser.add_argument("--force", action="store_true", help="Overwrite existing translations")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    locales = ["hk", "tw", "cn"] if args.locale == "all" else [args.locale]

    for loc in locales:
        if loc not in LOCALE_CONFIG:
            print(f'Error: Unknown locale "{loc}". Use hk, tw, cn, or all.')
            sys.exit(1)

    course_dir = os.path.join(PROJECT_ROOT, "course")
    files = sorted(f for f in os.listdir(course_dir) if f.endswith(".md"))

    if args.file_pattern:
        files = [f for f in files if args.file_pattern in f]

    if not files:
        print("No files match the criteria.")
        return

    total = len(files) * len(locales)
    print(f"Translation batch: {len(files)} files x {len(locales)} locale(s) = {total} translations")
    if args.dry_run:
        print("(DRY RUN - no files will be written)\n")
    else:
        print()

    client = anthropic.Anthropic()
    results = {"translated": 0, "skipped": 0, "errors": 0, "dry_run": 0}
    total_input = 0
    total_output = 0

    for locale in locales:
        print(f"--- {LOCALE_CONFIG[locale]['name']} ---")

        for i, source_file in enumerate(files):
            progress = f"[{i + 1}/{len(files)}]"
            result = translate_file(client, source_file, locale, args.force, args.dry_run)

            if result["status"] == "translated":
                it = result["input_tokens"]
                ot = result["output_tokens"]
                print(f"  {progress} {source_file} -> {locale.upper()} ({it}+{ot} tokens)")
                results["translated"] += 1
                total_input += it
                total_output += ot
            elif result["status"] == "skipped":
                print(f"  {progress} {source_file} -> {locale.upper()} [skipped - already translated]")
                results["skipped"] += 1
            elif result["status"] == "dry-run":
                print(f"  {progress} {source_file} -> {locale.upper()} [would translate]")
                results["dry_run"] += 1
            elif result["status"] == "error":
                print(f"  {progress} {source_file} -> {locale.upper()} [ERROR: {result['error']}]")
                results["errors"] += 1

        print()

    print("=== Summary ===")
    print(f"  Translated: {results['translated']}")
    print(f"  Skipped:    {results['skipped']}")
    if results["dry_run"]:
        print(f"  Would do:   {results['dry_run']}")
    if results["errors"]:
        print(f"  Errors:     {results['errors']}")
    if total_input:
        cost_input = (total_input / 1_000_000) * 3
        cost_output = (total_output / 1_000_000) * 15
        print(f"  Tokens:     {total_input:,} in + {total_output:,} out")
        print(f"  Est. cost:  ${cost_input + cost_output:.2f}")


if __name__ == "__main__":
    main()
