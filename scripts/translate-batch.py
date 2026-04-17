#!/usr/bin/env python3
"""
Automated Translation for Chanma Investment Tutorial

Translates English course markdown files to three Chinese variants
using a configurable LLM provider (Anthropic Claude, OpenAI, or Google Gemini).

Defaults are read from scripts/configs.json. CLI flags override individual
config values.

Usage:
    uv run python scripts/translate-batch.py                    # use configs.json defaults
    uv run python scripts/translate-batch.py --locale hk        # only HK
    uv run python scripts/translate-batch.py --locale all       # HK+TW+CN
    uv run python scripts/translate-batch.py --file week01      # only files matching
    uv run python scripts/translate-batch.py --provider gemini  # override provider
    uv run python scripts/translate-batch.py --force            # overwrite existing
    uv run python scripts/translate-batch.py --dry-run          # preview only

Per-provider API keys are read from environment variables (configurable in
configs.json -> providers.<name>.api_key_env):
    ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY

Install (only the providers you actually use):
    uv pip install anthropic openai google-generativeai
"""

import argparse
import json
import os
import sys
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_PATH = os.path.join(SCRIPTS_DIR, "configs.json")
TERMINOLOGY_PATH = os.path.join(SCRIPTS_DIR, "terminology.json")

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
# Config + terminology loading
# ---------------------------------------------------------------------------
def load_configs():
    with open(CONFIGS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_terminology():
    with open(TERMINOLOGY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    flat = {}
    for category, terms in data.get("categories", {}).items():
        for en, mapping in terms.items():
            flat[en] = mapping
    return flat


# ---------------------------------------------------------------------------
# System prompt builder
# ---------------------------------------------------------------------------
def build_system_prompt(locale, terminology):
    config = LOCALE_CONFIG[locale]
    term_table = "\n".join(
        f"  {en} → {t[locale]}" for en, t in terminology.items() if locale in t
    )

    return f"""You are an expert financial content translator specializing in {config['name']}.

TARGET: {config['description']}

FINANCIAL TERMINOLOGY — always use these exact translations:
{term_table}

RULES:
1. Translate ALL text content including section headers.
2. Preserve ALL markdown formatting exactly (headers, lists, tables, code blocks, links, bold, italic).
3. Preserve [VISUAL], [ANIMATION], and [CUT TO] tags in English — do NOT translate them.
4. Use ONLY the Chinese host names: Horace -> 陳馬, Stella -> 小魚. Do NOT keep the English names in the translated output.
5. Preserve animation/image file paths (e.g., animation/week01_compound_growth.py) without translating.
6. Preserve ASCII art diagrams — translate only the text labels within them.
7. Output ONLY the translated markdown. No preamble, no commentary, no wrapping.
8. The YouTube script dialogue must sound natural and conversational in {config['script']}."""


# ---------------------------------------------------------------------------
# Provider adapters — each returns (translated_text, input_tokens, output_tokens)
# ---------------------------------------------------------------------------
def call_anthropic(provider_cfg, system, user):
    import anthropic
    client = anthropic.Anthropic()
    kwargs = {
        "model": provider_cfg["model"],
        "max_tokens": provider_cfg.get("max_tokens", 65536),
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    budget = provider_cfg.get("thinking_budget_tokens")
    if budget:
        kwargs["thinking"] = {"type": "enabled", "budget_tokens": budget}

    with client.messages.stream(**kwargs) as stream:
        response = stream.get_final_message()

    text = "".join(b.text for b in response.content if b.type == "text")
    return text, response.usage.input_tokens, response.usage.output_tokens


def call_openai(provider_cfg, system, user):
    from openai import OpenAI
    client = OpenAI()
    effort = provider_cfg.get("thinking_effort", "medium")
    response = client.responses.create(
        model=provider_cfg["model"],
        input=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_output_tokens=provider_cfg.get("max_output_tokens", 65536),
        reasoning={"effort": effort},
    )
    text = response.output_text
    usage = getattr(response, "usage", None)
    in_tok = getattr(usage, "input_tokens", 0) if usage else 0
    out_tok = getattr(usage, "output_tokens", 0) if usage else 0
    return text, in_tok, out_tok


def call_gemini(provider_cfg, system, user):
    import google.generativeai as genai
    genai.configure(api_key=os.environ.get(provider_cfg.get("api_key_env", "GEMINI_API_KEY")))
    model = genai.GenerativeModel(
        provider_cfg["model"],
        system_instruction=system,
    )
    response = model.generate_content(
        user,
        generation_config={
            "max_output_tokens": provider_cfg.get("max_output_tokens", 65536),
        },
    )
    text = response.text or ""
    usage = getattr(response, "usage_metadata", None)
    in_tok = getattr(usage, "prompt_token_count", 0) if usage else 0
    out_tok = getattr(usage, "candidates_token_count", 0) if usage else 0
    return text, in_tok, out_tok


PROVIDER_DISPATCH = {
    "anthropic": call_anthropic,
    "openai": call_openai,
    "gemini": call_gemini,
}


def check_provider_key(provider_name, provider_cfg):
    env_var = provider_cfg.get("api_key_env")
    if env_var and not os.environ.get(env_var):
        print(f'Error: provider "{provider_name}" requires environment variable {env_var}')
        sys.exit(1)


# ---------------------------------------------------------------------------
# Translation
# ---------------------------------------------------------------------------
def is_placeholder(file_path):
    if not os.path.exists(file_path):
        return True
    with open(file_path, "r", encoding="utf-8") as f:
        head = f.read(200)
    return "This file needs translation" in head


def strip_preamble(translated):
    first_header = translated.find("#")
    if 0 < first_header < 100:
        translated = translated[first_header:]
    return translated


def translate_file(provider_name, provider_cfg, source_path, target_path,
                   locale, terminology, force=False, dry_run=False):
    if not force and os.path.exists(target_path) and not is_placeholder(target_path):
        return {"status": "skipped"}
    if dry_run:
        return {"status": "dry-run"}

    content = open(source_path, "r", encoding="utf-8").read()
    system = build_system_prompt(locale, terminology)

    try:
        text, in_tok, out_tok = PROVIDER_DISPATCH[provider_name](provider_cfg, system, content)
    except Exception as e:
        return {"status": "error", "error": str(e)}

    text = strip_preamble(text)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(text)

    return {
        "status": "translated",
        "input_tokens": in_tok,
        "output_tokens": out_tok,
    }


# ---------------------------------------------------------------------------
# Progress bar
# ---------------------------------------------------------------------------
def render_progress(current, total, width=24):
    filled = int(width * current / total) if total else width
    return "[" + "#" * filled + "-" * (width - filled) + f"] {current}/{total}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    configs = load_configs()
    terminology = load_terminology()

    parser = argparse.ArgumentParser(description="Translate investment tutorial course files")
    parser.add_argument("--provider", help="LLM provider override: anthropic | openai | gemini")
    parser.add_argument("--model", help="Model override for the chosen provider")
    parser.add_argument("--locale", help="Target locale: hk, tw, cn, or all")
    parser.add_argument("--file", dest="file_pattern", help="Only translate files matching this substring")
    parser.add_argument("--source-dir", help="Source directory (default from configs.json)")
    parser.add_argument("--output-dir", help="Override output base directory; subdirectories course_<locale> still apply")
    parser.add_argument("--force", action="store_true", help="Overwrite existing translations")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    provider_name = args.provider or configs["provider"]
    if provider_name not in PROVIDER_DISPATCH:
        print(f'Error: unknown provider "{provider_name}". Choose from {list(PROVIDER_DISPATCH)}.')
        sys.exit(1)
    provider_cfg = dict(configs["providers"][provider_name])
    if args.model:
        provider_cfg["model"] = args.model

    check_provider_key(provider_name, provider_cfg)

    if args.locale:
        locales = ["hk", "tw", "cn"] if args.locale == "all" else [args.locale]
    else:
        locales = configs.get("locales", ["hk", "tw", "cn"])

    for loc in locales:
        if loc not in LOCALE_CONFIG:
            print(f'Error: Unknown locale "{loc}". Use hk, tw, cn, or all.')
            sys.exit(1)

    source_rel = args.source_dir or configs.get("source_dir", "course")
    source_dir = os.path.join(PROJECT_ROOT, source_rel)
    output_root = args.output_dir or configs.get("output_dir") or PROJECT_ROOT
    output_root = os.path.join(PROJECT_ROOT, output_root) if not os.path.isabs(output_root) else output_root

    file_pattern = args.file_pattern if args.file_pattern is not None else configs.get("file_pattern")
    force = args.force or configs.get("force", False)
    dry_run = args.dry_run or configs.get("dry_run", False)

    files = sorted(f for f in os.listdir(source_dir) if f.endswith(".md"))
    if file_pattern:
        files = [f for f in files if file_pattern in f]
    if not files:
        print("No files match the criteria.")
        return

    total = len(files) * len(locales)
    print(f"Provider:        {provider_name} ({provider_cfg['model']})")
    print(f"Source dir:      {source_rel}")
    print(f"Output root:     {output_root}")
    print(f"Locales:         {', '.join(locales)}")
    print(f"Files to do:     {len(files)} x {len(locales)} = {total} translations")
    if dry_run:
        print("(DRY RUN - no files will be written)")
    print()

    results = {"translated": 0, "skipped": 0, "errors": 0, "dry_run": 0}
    total_input = 0
    total_output = 0
    done = 0
    start = time.time()

    for locale in locales:
        print(f"--- {LOCALE_CONFIG[locale]['name']} ---")
        target_dir = os.path.join(output_root, LOCALE_CONFIG[locale]["dir"])

        for source_file in files:
            done += 1
            source_path = os.path.join(source_dir, source_file)
            target_path = os.path.join(target_dir, source_file)
            elapsed = time.time() - start
            bar = render_progress(done, total)
            sys.stdout.write(f"  {bar} {locale.upper()} {source_file:40s} ... ")
            sys.stdout.flush()

            t0 = time.time()
            result = translate_file(
                provider_name, provider_cfg, source_path, target_path,
                locale, terminology, force=force, dry_run=dry_run,
            )
            dt = time.time() - t0

            status = result["status"]
            if status == "translated":
                it = result["input_tokens"]
                ot = result["output_tokens"]
                total_input += it
                total_output += ot
                results["translated"] += 1
                print(f"OK ({it}+{ot} tok, {dt:.1f}s)")
            elif status == "skipped":
                results["skipped"] += 1
                print("skipped")
            elif status == "dry-run":
                results["dry_run"] += 1
                print("would translate")
            elif status == "error":
                results["errors"] += 1
                print(f"ERROR: {result['error']}")

        print(f"  elapsed: {elapsed:.1f}s\n")

    print("=== Summary ===")
    print(f"  Translated: {results['translated']}")
    print(f"  Skipped:    {results['skipped']}")
    if results["dry_run"]:
        print(f"  Would do:   {results['dry_run']}")
    if results["errors"]:
        print(f"  Errors:     {results['errors']}")
    if total_input:
        in_cost = (total_input / 1_000_000) * provider_cfg.get("input_cost_per_mtok", 0)
        out_cost = (total_output / 1_000_000) * provider_cfg.get("output_cost_per_mtok", 0)
        print(f"  Tokens:     {total_input:,} in + {total_output:,} out")
        print(f"  Est. cost:  ${in_cost + out_cost:.2f}")


if __name__ == "__main__":
    main()
