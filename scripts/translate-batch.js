#!/usr/bin/env node
/**
 * Automated Translation for Investment Tutorial Course
 *
 * Translates English course markdown files to three Chinese variants
 * using the Anthropic Claude API.
 *
 * Usage:
 *   node scripts/translate-batch.js --locale hk          # Translate all to HK Chinese
 *   node scripts/translate-batch.js --locale all          # Translate all locales
 *   node scripts/translate-batch.js --locale tw --file week01  # Translate one file
 *   node scripts/translate-batch.js --locale cn --force   # Overwrite existing
 *   node scripts/translate-batch.js --locale hk --dry-run # Preview without writing
 *
 * Requires: ANTHROPIC_API_KEY environment variable
 * Install:  cd scripts && npm install
 */

const Anthropic = require('@anthropic-ai/sdk');
const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.resolve(__dirname, '..');

// ---------------------------------------------------------------------------
// Locale configuration
// ---------------------------------------------------------------------------
const LOCALE_CONFIG = {
    hk: {
        name: 'Hong Kong Traditional Chinese',
        script: '繁體中文',
        dir: 'course_hk',
        description: 'Hong Kong Traditional Chinese (繁體). Use Hong Kong financial terminology and conventions.'
    },
    tw: {
        name: 'Taiwan Traditional Chinese',
        script: '繁體中文',
        dir: 'course_tw',
        description: 'Taiwan Traditional Chinese (繁體). Use Taiwan financial terminology and conventions.'
    },
    cn: {
        name: 'Mainland Simplified Chinese',
        script: '簡體中文',
        dir: 'course_cn',
        description: 'Mainland Simplified Chinese (簡體). Use Mainland China financial terminology and conventions.'
    }
};

// ---------------------------------------------------------------------------
// Financial terminology — locale-specific translations
// ---------------------------------------------------------------------------
const TERMINOLOGY = {
    'stock':              { hk: '股票', tw: '股票', cn: '股票' },
    'bond':               { hk: '債券', tw: '債券', cn: '债券' },
    'portfolio':          { hk: '投資組合', tw: '投資組合', cn: '投资组合' },
    'dividend':           { hk: '股息', tw: '股利', cn: '股息' },
    'index fund':         { hk: '指數基金', tw: '指數基金', cn: '指数基金' },
    'ETF':                { hk: '交易所買賣基金', tw: '指數股票型基金', cn: '交易所交易基金' },
    'mutual fund':        { hk: '互惠基金', tw: '共同基金', cn: '共同基金' },
    'return':             { hk: '回報', tw: '報酬', cn: '收益' },
    'yield':              { hk: '收益率', tw: '殖利率', cn: '收益率' },
    'interest rate':      { hk: '利率', tw: '利率', cn: '利率' },
    'inflation':          { hk: '通脹', tw: '通膨', cn: '通胀' },
    'risk':               { hk: '風險', tw: '風險', cn: '风险' },
    'volatility':         { hk: '波動性', tw: '波動性', cn: '波动性' },
    'asset allocation':   { hk: '資產配置', tw: '資產配置', cn: '资产配置' },
    'rebalancing':        { hk: '再平衡', tw: '再平衡', cn: '再平衡' },
    'call option':        { hk: '認購期權', tw: '買權', cn: '看涨期权' },
    'put option':         { hk: '認沽期權', tw: '賣權', cn: '看跌期权' },
    'strike price':       { hk: '行使價', tw: '履約價', cn: '行权价' },
    'expiration':         { hk: '到期日', tw: '到期日', cn: '到期日' },
    'premium':            { hk: '期權金', tw: '權利金', cn: '期权费' },
    'covered call':       { hk: '備兌認購期權', tw: '掩護性買權', cn: '备兑看涨期权' },
    'warrant':            { hk: '窩輪', tw: '權證', cn: '权证' },
    'bull market':        { hk: '牛市', tw: '多頭市場', cn: '牛市' },
    'bear market':        { hk: '熊市', tw: '空頭市場', cn: '熊市' },
    'market cap':         { hk: '市值', tw: '市值', cn: '市值' },
    'P/E ratio':          { hk: '市盈率', tw: '本益比', cn: '市盈率' },
    'earnings':           { hk: '盈利', tw: '盈餘', cn: '盈利' },
    'coupon':             { hk: '票息', tw: '票面利率', cn: '票息' },
    'duration':           { hk: '存續期', tw: '存續期間', cn: '久期' },
    'credit spread':      { hk: '信用利差', tw: '信用利差', cn: '信用利差' },
    'yield curve':        { hk: '收益率曲線', tw: '殖利率曲線', cn: '收益率曲线' },
    'futures':            { hk: '期貨', tw: '期貨', cn: '期货' },
    'leverage':           { hk: '槓桿', tw: '槓桿', cn: '杠杆' },
    'hedge':              { hk: '對沖', tw: '避險', cn: '对冲' },
    'short selling':      { hk: '沽空', tw: '放空', cn: '做空' },
    'margin':             { hk: '保證金', tw: '保證金', cn: '保证金' },
    'drawdown':           { hk: '回撤', tw: '回撤', cn: '回撤' },
    'Sharpe ratio':       { hk: '夏普比率', tw: '夏普比率', cn: '夏普比率' },
};

// ---------------------------------------------------------------------------
// Build the translation prompt
// ---------------------------------------------------------------------------
function buildSystemPrompt(locale) {
    const config = LOCALE_CONFIG[locale];
    const termTable = Object.entries(TERMINOLOGY)
        .map(([en, t]) => `  ${en} → ${t[locale]}`)
        .join('\n');

    return `You are an expert financial content translator specializing in ${config.name}.

TARGET: ${config.description}

FINANCIAL TERMINOLOGY — always use these exact translations:
${termTable}

RULES:
1. Translate ALL text content including section headers.
2. Preserve ALL markdown formatting exactly (headers, lists, tables, code blocks, links, bold, italic).
3. Preserve [VISUAL], [ANIMATION], and [CUT TO] tags in English — do NOT translate them.
4. Preserve host names "Alex" and "Sam" without translating.
5. Preserve animation file paths (e.g., animation/week01_compound_growth.py) without translating.
6. Preserve ASCII art diagrams — translate only the text labels within them.
7. Output ONLY the translated markdown. No preamble, no commentary, no wrapping.
8. The YouTube script dialogue must sound natural and conversational in ${config.script}.`;
}

// ---------------------------------------------------------------------------
// Check if a file is a placeholder (contains the marker comment)
// ---------------------------------------------------------------------------
function isPlaceholder(filePath) {
    if (!fs.existsSync(filePath)) return true;
    const head = fs.readFileSync(filePath, 'utf8').slice(0, 200);
    return head.includes('This file needs translation');
}

// ---------------------------------------------------------------------------
// Translate a single file
// ---------------------------------------------------------------------------
async function translateFile(client, sourceFile, locale, options) {
    const sourceDir = path.join(PROJECT_ROOT, 'course');
    const targetDir = path.join(PROJECT_ROOT, LOCALE_CONFIG[locale].dir);
    const sourcePath = path.join(sourceDir, sourceFile);
    const targetPath = path.join(targetDir, sourceFile);

    // Skip if already translated (unless --force)
    if (!options.force && fs.existsSync(targetPath) && !isPlaceholder(targetPath)) {
        return { status: 'skipped', file: sourceFile, locale };
    }

    if (options.dryRun) {
        return { status: 'dry-run', file: sourceFile, locale };
    }

    const content = fs.readFileSync(sourcePath, 'utf8');

    try {
        const response = await client.messages.create({
            model: 'claude-sonnet-4-20250514',
            max_tokens: 16384,
            system: buildSystemPrompt(locale),
            messages: [{ role: 'user', content }]
        });

        let translated = response.content[0].text;

        // Strip any accidental preamble (e.g., "Here is the translation:")
        const firstHeader = translated.indexOf('#');
        if (firstHeader > 0 && firstHeader < 100) {
            translated = translated.slice(firstHeader);
        }

        fs.mkdirSync(targetDir, { recursive: true });
        fs.writeFileSync(targetPath, translated, 'utf8');

        return {
            status: 'translated',
            file: sourceFile,
            locale,
            inputTokens: response.usage.input_tokens,
            outputTokens: response.usage.output_tokens
        };
    } catch (err) {
        return { status: 'error', file: sourceFile, locale, error: err.message };
    }
}

// ---------------------------------------------------------------------------
// Parse CLI arguments
// ---------------------------------------------------------------------------
function parseArgs() {
    const args = process.argv.slice(2);
    const options = {
        locale: null,
        filePattern: null,
        force: false,
        dryRun: false
    };

    for (let i = 0; i < args.length; i++) {
        switch (args[i]) {
            case '--locale':
                options.locale = args[++i];
                break;
            case '--file':
                options.filePattern = args[++i];
                break;
            case '--force':
                options.force = true;
                break;
            case '--dry-run':
                options.dryRun = true;
                break;
            case '--help':
                console.log(`Usage: node translate-batch.js --locale <hk|tw|cn|all> [options]

Options:
  --locale <locale>   Target locale: hk, tw, cn, or all (required)
  --file <pattern>    Only translate files matching pattern (e.g., week01, side)
  --force             Overwrite existing translations
  --dry-run           Show what would be translated without making API calls
  --help              Show this help`);
                process.exit(0);
        }
    }

    if (!options.locale) {
        console.error('Error: --locale is required. Use --help for usage.');
        process.exit(1);
    }

    return options;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
async function main() {
    const options = parseArgs();

    // Determine which locales to process
    const locales = options.locale === 'all'
        ? ['hk', 'tw', 'cn']
        : [options.locale];

    // Validate locales
    for (const loc of locales) {
        if (!LOCALE_CONFIG[loc]) {
            console.error(`Error: Unknown locale "${loc}". Use hk, tw, cn, or all.`);
            process.exit(1);
        }
    }

    // Get source files
    const courseDir = path.join(PROJECT_ROOT, 'course');
    let files = fs.readdirSync(courseDir)
        .filter(f => f.endsWith('.md'))
        .sort();

    if (options.filePattern) {
        files = files.filter(f => f.includes(options.filePattern));
    }

    if (files.length === 0) {
        console.log('No files match the criteria.');
        return;
    }

    console.log(`Translation batch: ${files.length} files x ${locales.length} locale(s) = ${files.length * locales.length} translations`);
    if (options.dryRun) console.log('(DRY RUN - no files will be written)\n');
    else console.log('');

    const client = new Anthropic();
    const results = { translated: 0, skipped: 0, errors: 0, dryRun: 0 };
    let totalInputTokens = 0;
    let totalOutputTokens = 0;

    for (const locale of locales) {
        console.log(`--- ${LOCALE_CONFIG[locale].name} ---`);

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const progress = `[${i + 1}/${files.length}]`;

            const result = await translateFile(client, file, locale, options);

            switch (result.status) {
                case 'translated':
                    console.log(`  ${progress} ${file} -> ${locale.toUpperCase()} (${result.inputTokens}+${result.outputTokens} tokens)`);
                    results.translated++;
                    totalInputTokens += result.inputTokens;
                    totalOutputTokens += result.outputTokens;
                    break;
                case 'skipped':
                    console.log(`  ${progress} ${file} -> ${locale.toUpperCase()} [skipped - already translated]`);
                    results.skipped++;
                    break;
                case 'dry-run':
                    console.log(`  ${progress} ${file} -> ${locale.toUpperCase()} [would translate]`);
                    results.dryRun++;
                    break;
                case 'error':
                    console.error(`  ${progress} ${file} -> ${locale.toUpperCase()} [ERROR: ${result.error}]`);
                    results.errors++;
                    break;
            }
        }
        console.log('');
    }

    // Summary
    console.log('=== Summary ===');
    console.log(`  Translated: ${results.translated}`);
    console.log(`  Skipped:    ${results.skipped}`);
    if (results.dryRun) console.log(`  Would do:   ${results.dryRun}`);
    if (results.errors) console.log(`  Errors:     ${results.errors}`);
    if (totalInputTokens) {
        const costInput = (totalInputTokens / 1_000_000) * 3;
        const costOutput = (totalOutputTokens / 1_000_000) * 15;
        console.log(`  Tokens:     ${totalInputTokens.toLocaleString()} in + ${totalOutputTokens.toLocaleString()} out`);
        console.log(`  Est. cost:  $${(costInput + costOutput).toFixed(2)}`);
    }
}

main().catch(err => {
    console.error('Fatal error:', err.message);
    process.exit(1);
});
