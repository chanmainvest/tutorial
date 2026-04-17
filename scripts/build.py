#!/usr/bin/env python3
"""
Static Site Generator for Chanma Investment Tutorial

Reads markdown files from course/, course_hk/, course_tw/, course_cn/
and generates a static website in docs/ with:
- Single-panel layout with top navigation bar
- Multilevel hamburger menu in the top-right corner
- Breadcrumb navigation
- Country flag language selector (rendered via Twemoji for cross-platform display)
- Dark/light theme toggle with localStorage persistence
- Prev/next page buttons in footer
- YouTube script sections filtered out (article content only)
- A Glossary page generated from scripts/terminology.json
- Professional, trust-building visual theme (light + dark variants)

Usage: uv run python scripts/build.py
"""

import json
import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
TERMINOLOGY_PATH = os.path.join(SCRIPTS_DIR, "terminology.json")

# ---------------------------------------------------------------------------
# Course structure definition
# ---------------------------------------------------------------------------
LEVELS = [
    {"name": "Level 1: Foundation", "subtitle": "Beginner", "range": (1, 12), "overview": "level1_overview"},
    {"name": "Level 2: Intermediate", "subtitle": "Intermediate", "range": (13, 24), "overview": "level2_overview"},
    {"name": "Level 3: Advanced", "subtitle": "Options & Fixed Income", "range": (25, 36), "overview": "level3_overview"},
    {"name": "Level 4: Sophisticated", "subtitle": "Professional Tools", "range": (37, 46), "overview": "level4_overview"},
    {"name": "Level 5: Expert", "subtitle": "Portfolio Integration", "range": (47, 52), "overview": "level5_overview"},
]

LOCALES = ("en", "hk", "tw", "cn")

# UI strings translated per locale. Used for the hamburger menu, breadcrumb,
# brand text, footer, prev/next buttons, and "translation pending" placeholder.
LOCALE_LABELS = {
    "en": {
        "brand":            "Chanma Investment",
        "menu_title":       "Course Navigation",
        "home":             "Home",
        "side_lessons":     "Side Lessons",
        "glossary":         "Glossary",
        "disclaimer":       "Disclaimer",
        "faq":              "FAQ",
        "course_root":      "Chanma Investment Tutorial",
        "previous":         "Previous",
        "next":             "Next",
        "overview_suffix":  " Overview",
        "translation_pending": "Translation coming soon...",
        "level_names": [
            "Level 1: Foundation",
            "Level 2: Intermediate",
            "Level 3: Advanced",
            "Level 4: Sophisticated",
            "Level 5: Expert",
        ],
        "footer_tagline": "Released under the MIT License. Educational content only \u2014 not financial advice.",
    },
    "hk": {
        "brand":            "陳馬投資",
        "menu_title":       "課程導覽",
        "home":             "首頁",
        "side_lessons":     "補充課程",
        "glossary":         "詞彙表",
        "disclaimer":       "免責聲明",
        "faq":              "常見問題",
        "course_root":      "陳馬投資教學",
        "previous":         "上一頁",
        "next":             "下一頁",
        "overview_suffix":  "總覽",
        "translation_pending": "翻譯稍後推出……",
        "level_names": [
            "第一級：入門",
            "第二級：中階",
            "第三級：進階",
            "第四級：精通",
            "第五級：專家",
        ],
        "footer_tagline": "以 MIT 授權釋出。內容僅作教學用途，並非投資建議。",
    },
    "tw": {
        "brand":            "陳馬投資",
        "menu_title":       "課程導覽",
        "home":             "首頁",
        "side_lessons":     "補充單元",
        "glossary":         "詞彙表",
        "disclaimer":       "免責聲明",
        "faq":              "常見問題",
        "course_root":      "陳馬投資教學",
        "previous":         "上一頁",
        "next":             "下一頁",
        "overview_suffix":  "總覽",
        "translation_pending": "翻譯即將推出……",
        "level_names": [
            "第一級：入門",
            "第二級：中階",
            "第三級：進階",
            "第四級：專業",
            "第五級：專家",
        ],
        "footer_tagline": "以 MIT 授權釋出。內容僅供教學使用，非投資建議。",
    },
    "cn": {
        "brand":            "陈马投资",
        "menu_title":       "课程导览",
        "home":             "首页",
        "side_lessons":     "补充课程",
        "glossary":         "词汇表",
        "disclaimer":       "免责声明",
        "faq":              "常见问题",
        "course_root":      "陈马投资教程",
        "previous":         "上一页",
        "next":             "下一页",
        "overview_suffix":  "总览",
        "translation_pending": "翻译即将推出……",
        "level_names": [
            "第一级：入门",
            "第二级：中阶",
            "第三级：进阶",
            "第四级：专业",
            "第五级:  专家",
        ],
        "footer_tagline": "以 MIT 协议发布。内容仅供教学，并非投资建议。",
    },
}


# ---------------------------------------------------------------------------
# Simple markdown to HTML converter
# ---------------------------------------------------------------------------
def markdown_to_html(md):
    html = md

    def replace_code_block(m):
        lang = m.group(1)
        code = m.group(2)
        code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    html = re.sub(r"```(\w*)\n([\s\S]*?)```", replace_code_block, html)
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)

    html = re.sub(r"^######\s+(.+)$", r"<h6>\1</h6>", html, flags=re.MULTILINE)
    html = re.sub(r"^#####\s+(.+)$", r"<h5>\1</h5>", html, flags=re.MULTILINE)
    html = re.sub(r"^####\s+(.+)$", r"<h4>\1</h4>", html, flags=re.MULTILINE)
    html = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    html = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", html)
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)

    html = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', html)
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)
    html = re.sub(r"^---$", "<hr>", html, flags=re.MULTILINE)

    def replace_table(m):
        header = m.group(1)
        body = m.group(3)
        header_cells = "".join(
            f"<th>{c.strip()}</th>" for c in header.split("|") if c.strip()
        )
        rows = []
        for row in body.strip().split("\n"):
            cells = "".join(
                f"<td>{c.strip()}</td>" for c in row.split("|") if c.strip()
            )
            rows.append(f"<tr>{cells}</tr>")
        return f"<table><thead><tr>{header_cells}</tr></thead><tbody>{''.join(rows)}</tbody></table>"

    html = re.sub(
        r"^(\|.+\|)\n(\|[-:\s|]+\|)\n((?:\|.+\|\n?)+)",
        replace_table,
        html,
        flags=re.MULTILINE,
    )

    html = re.sub(r"^>\s+(.+)$", r"<blockquote>\1</blockquote>", html, flags=re.MULTILINE)

    html = re.sub(r"^[\s]*[-*]\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"(<li>.*</li>\n?)+", r"<ul>\g<0></ul>", html)
    html = re.sub(r"^\d+\.\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)

    lines = html.split("\n")
    result = []
    in_paragraph = False

    for line in lines:
        stripped = line.strip()
        is_tag = bool(
            re.match(
                r"^<(h[1-6]|ul|ol|li|table|thead|tbody|tr|th|td|pre|code|blockquote|hr|div|img)",
                stripped,
            )
        )
        is_empty = stripped == ""

        if is_empty:
            if in_paragraph:
                result.append("</p>")
                in_paragraph = False
            continue

        if is_tag:
            if in_paragraph:
                result.append("</p>")
                in_paragraph = False
            result.append(stripped)
        else:
            if not in_paragraph:
                result.append("<p>")
                in_paragraph = True
            result.append(stripped)

    if in_paragraph:
        result.append("</p>")

    return "\n".join(result)


# ---------------------------------------------------------------------------
# Strip YouTube script section from markdown
# ---------------------------------------------------------------------------
def strip_youtube_section(md):
    """Strip Part 2 (YouTube Script) regardless of locale.

    English uses `## Part 2: YouTube Script`; Chinese translations use the
    locale-translated equivalent (e.g. `## 第二部分：YouTube 腳本`,
    `## 第二部分：YouTube脚本`). All variants contain "YouTube" in the
    `## ` heading, which we use as the anchor.
    """
    pattern = r"\n---\s*\n\s*##[^\n]*[Yy]ou[Tt]ube[^\n]*\n.*"
    return re.sub(pattern, "", md, flags=re.DOTALL)


def extract_title(md):
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1) if m else "Untitled"


# ---------------------------------------------------------------------------
# Post-processing: turn level / week references into hyperlinks
# ---------------------------------------------------------------------------
def linkify_overview_levels(html):
    """On the course overview page, wrap `<h3>Level N: ...</h3>` in a link
    to the corresponding level overview page. Works across all locales as
    long as the heading still starts with the digit 1-5 after "Level " or
    its translated equivalent — we anchor on the digit since the word for
    "Level" varies (Level / 級別 / 等級 / 级别).
    """
    pattern = re.compile(r'<h3>([^<]*?\b([1-5])\b[^<]*?)</h3>')

    def repl(m):
        text = m.group(1)
        n = m.group(2)
        return f'<h3><a href="level{n}.html" class="level-link">{text}</a></h3>'

    return pattern.sub(repl, html)


def linkify_level_weeks(html, level_num):
    """On a level overview page, wrap each `<tr>` in the weekly-lessons
    table with a link to the corresponding week page. The first <td> is
    the week number; we use it to compute the slug.
    """
    if not (1 <= level_num <= 5):
        return html

    row_pattern = re.compile(
        r'<tr>\s*<td>(\d{1,2})</td>\s*<td>([^<]+)</td>\s*</tr>'
    )

    def repl(m):
        week_num = int(m.group(1))
        topic = m.group(2).strip()
        slug = f"week{week_num:02d}"
        return (
            f'<tr class="week-row" onclick="window.location=\'{slug}.html\'">'
            f'<td><a href="{slug}.html">{week_num}</a></td>'
            f'<td><a href="{slug}.html">{topic}</a></td>'
            f'</tr>'
        )

    return row_pattern.sub(repl, html)


# ---------------------------------------------------------------------------
# Page list
# ---------------------------------------------------------------------------
def build_page_list(course_files):
    pages = []

    pages.append({
        "slug": "index", "file": "overview.md", "title": "Course Overview",
        "level": None, "type": "overview", "nav_title": "Course Overview",
    })

    for level_idx, level in enumerate(LEVELS):
        level_num = level_idx + 1
        overview_file = f"{level['overview']}.md"
        if overview_file in course_files:
            pages.append({
                "slug": f"level{level_num}", "file": overview_file,
                "title": level["name"], "level": level_num,
                "type": "level_overview",
                "nav_title": f"{level['name']} Overview",
            })

        for week_num in range(level["range"][0], level["range"][1] + 1):
            week_str = str(week_num).zfill(2)
            matching = [f for f in course_files if f.startswith(f"week{week_str}_")]
            if matching:
                file = matching[0]
                topic = file.replace(f"week{week_str}_", "").replace(".md", "").replace("_", " ")
                topic = topic[0].upper() + topic[1:]
                pages.append({
                    "slug": f"week{week_str}", "file": file,
                    "title": f"Week {week_num}: {topic}",
                    "level": level_num, "type": "week",
                    "week_num": week_num,
                    "nav_title": f"Week {week_num}: {topic}",
                })

    side_files = sorted([f for f in course_files if f.startswith("side")])
    for file in side_files:
        m = re.match(r"side(\d+)_(.+)\.md", file)
        if m:
            num = int(m.group(1))
            topic = m.group(2).replace("_", " ")
            topic = topic[0].upper() + topic[1:]
            pages.append({
                "slug": f"side{m.group(1)}", "file": file,
                "title": f"Side {num}: {topic}", "level": None,
                "type": "side", "nav_title": f"Side {num}: {topic}",
            })

    # Glossary (generated, not from a markdown file)
    pages.append({
        "slug": "glossary", "file": None, "title": "Glossary",
        "level": None, "type": "info", "nav_title": "Glossary",
    })

    if "disclaimer.md" in course_files:
        pages.append({
            "slug": "disclaimer", "file": "disclaimer.md", "title": "Disclaimer",
            "level": None, "type": "info", "nav_title": "Disclaimer",
        })

    if "faq.md" in course_files:
        pages.append({
            "slug": "faq", "file": "faq.md", "title": "FAQ",
            "level": None, "type": "info", "nav_title": "FAQ",
        })

    return pages


# ---------------------------------------------------------------------------
# Multilevel hamburger menu HTML
# ---------------------------------------------------------------------------
def get_translated_nav_title(page, locale, lang_dirs):
    """Return the page's translated nav title (or English fallback).

    Handles three cases:
      - level_overview: synthesised from LOCALE_LABELS[locale]["level_names"]
      - info pages with no source file (e.g. glossary): use info_label
      - lesson markdown files: read the translated H1 from the locale's file
    """
    L = LOCALE_LABELS[locale]
    if page.get("type") == "level_overview" and page.get("level"):
        return L["level_names"][page["level"] - 1] + L["overview_suffix"]
    if page.get("file") is None:
        info_label = {
            "glossary":   L["glossary"],
            "disclaimer": L["disclaimer"],
            "faq":        L["faq"],
        }
        return info_label.get(page.get("slug"), page.get("nav_title", ""))
    if locale == "en":
        return page.get("nav_title", "")
    lang_dir = lang_dirs.get(locale)
    if not lang_dir:
        return page.get("nav_title", "")
    path = os.path.join(lang_dir, page["file"])
    if not os.path.exists(path):
        # Disclaimer/faq might also be info-typed but live under course/.
        info_label = {
            "disclaimer": L["disclaimer"],
            "faq":        L["faq"],
        }
        return info_label.get(page.get("slug"), page.get("nav_title", ""))
    md = open(path, encoding="utf-8").read()
    return extract_title(strip_youtube_section(md))


def build_nav_menu(pages, locale, lang_dirs):
    """Multilevel accordion menu opened by the hamburger button."""
    L = LOCALE_LABELS[locale]
    parts = [f'<a href="index.html" class="menu-link menu-top">{L["home"]}</a>']

    for level_idx, level in enumerate(LEVELS):
        level_num = level_idx + 1
        level_pages = [p for p in pages if p.get("level") == level_num]
        if not level_pages:
            continue

        level_label = L["level_names"][level_idx]
        parts.append('<div class="menu-group">')
        parts.append(
            f'<button class="menu-trigger" type="button" aria-expanded="false">'
            f'<span>{level_label}</span>'
            f'<span class="caret">&#9656;</span>'
            f'</button>'
        )
        parts.append('<div class="menu-sub">')
        for p in level_pages:
            if p["type"] == "level_overview":
                title = level_label + L["overview_suffix"]
            else:
                title = get_translated_nav_title(p, locale, lang_dirs)
            parts.append(f'<a href="{p["slug"]}.html" class="menu-sublink">{title}</a>')
        parts.append('</div>')
        parts.append('</div>')

    side_pages = [p for p in pages if p["type"] == "side"]
    if side_pages:
        parts.append('<div class="menu-group">')
        parts.append(
            f'<button class="menu-trigger" type="button" aria-expanded="false">'
            f'<span>{L["side_lessons"]}</span><span class="caret">&#9656;</span></button>'
        )
        parts.append('<div class="menu-sub">')
        for p in side_pages:
            title = get_translated_nav_title(p, locale, lang_dirs)
            parts.append(f'<a href="{p["slug"]}.html" class="menu-sublink">{title}</a>')
        parts.append('</div></div>')

    # Info / generated pages: use locale-translated label by slug.
    info_label = {
        "glossary":   L["glossary"],
        "disclaimer": L["disclaimer"],
        "faq":        L["faq"],
    }
    for p in [p for p in pages if p["type"] == "info"]:
        label = info_label.get(p["slug"], p["nav_title"])
        parts.append(f'<a href="{p["slug"]}.html" class="menu-link">{label}</a>')

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Breadcrumb
# ---------------------------------------------------------------------------
def build_breadcrumb(page, locale, lang_dirs):
    L = LOCALE_LABELS[locale]
    root = f'<a href="index.html">{L["course_root"]}</a>'
    crumbs = [root]

    if page["type"] == "level_overview":
        level_num = page["level"]
        crumbs.append(f'<span>{L["level_names"][level_num - 1]}</span>')
    elif page["type"] == "week":
        level_num = page["level"]
        crumbs.append(
            f'<a href="level{level_num}.html">{L["level_names"][level_num - 1]}</a>'
        )
        title = get_translated_nav_title(page, locale, lang_dirs)
        crumbs.append(f'<span>{title}</span>')
    elif page["type"] == "side":
        crumbs.append(f'<span>{L["side_lessons"]}</span>')
        title = get_translated_nav_title(page, locale, lang_dirs)
        crumbs.append(f'<span>{title}</span>')
    elif page["type"] == "info":
        info_label = {
            "glossary":   L["glossary"],
            "disclaimer": L["disclaimer"],
            "faq":        L["faq"],
        }
        crumbs.append(f'<span>{info_label.get(page["slug"], page["nav_title"])}</span>')
    elif page["slug"] == "index":
        crumbs = [f'<span>{L["course_root"]}</span>']

    return ' <span class="bc-sep">&#8250;</span> '.join(crumbs)


# ---------------------------------------------------------------------------
# Glossary page generation
# ---------------------------------------------------------------------------
CATEGORY_TRANSLATIONS = {
    "Equities & Indices":   {"hk": "股票與指數",       "tw": "股票與指數",       "cn": "股票与指数"},
    "Funds & ETFs":         {"hk": "基金與ETF",        "tw": "基金與ETF",        "cn": "基金与ETF"},
    "Bonds & Fixed Income": {"hk": "債券與固定收益",   "tw": "債券與固定收益",   "cn": "债券与固定收益"},
    "Derivatives & Options":{"hk": "衍生工具與期權",   "tw": "衍生性商品與選擇權","cn": "衍生品与期权"},
    "Portfolio & Strategy": {"hk": "投資組合與策略",   "tw": "投資組合與策略",   "cn": "投资组合与策略"},
    "Risk & Performance":   {"hk": "風險與績效",       "tw": "風險與績效",       "cn": "风险与业绩"},
    "Macroeconomics":       {"hk": "宏觀經濟",         "tw": "總體經濟",         "cn": "宏观经济"},
    "Trading & Markets":    {"hk": "交易與市場",       "tw": "交易與市場",       "cn": "交易与市场"},
    "Valuation & Analysis": {"hk": "估值與分析",       "tw": "估值與分析",       "cn": "估值与分析"},
    "Other":                {"hk": "其他",             "tw": "其他",             "cn": "其他"},
}

GLOSSARY_TITLE = {
    "en": "Glossary — Investment Terminology",
    "hk": "詞彙表 — 投資術語",
    "tw": "詞彙表 — 投資術語",
    "cn": "词汇表 — 投资术语",
}

GLOSSARY_INTRO = {
    "en": "Cross-reference table for investment terms used throughout the course. These are the canonical translations the auto-translator and the lessons use.",
    "hk": "本課程所用投資術語的對照表。下表為自動翻譯與各課堂統一採用的標準譯名。",
    "tw": "本課程所用投資術語的對照表。下表為自動翻譯與各課程統一採用的標準譯名。",
    "cn": "本课程所用投资术语的对照表。下表为自动翻译与各课程统一采用的标准译名。",
}

GLOSSARY_HEADERS = ["English", "香港", "台灣", "中國"]


def build_glossary_html():
    with open(TERMINOLOGY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    def render(locale):
        out = [
            f'<h1>{GLOSSARY_TITLE[locale]}</h1>',
            f'<p>{GLOSSARY_INTRO[locale]}</p>',
        ]
        header_row = "".join(f"<th>{h}</th>" for h in GLOSSARY_HEADERS)
        for category, terms in data["categories"].items():
            if locale == "en":
                heading = category
            else:
                heading = CATEGORY_TRANSLATIONS.get(category, {}).get(locale, category)
            out.append(f'<h2>{heading}</h2>')
            out.append('<table class="glossary-table">')
            out.append(f'<thead><tr>{header_row}</tr></thead>')
            out.append('<tbody>')
            for en, mapping in terms.items():
                out.append(
                    f'<tr><td><strong>{en}</strong></td>'
                    f'<td>{mapping.get("hk", "")}</td>'
                    f'<td>{mapping.get("tw", "")}</td>'
                    f'<td>{mapping.get("cn", "")}</td></tr>'
                )
            out.append('</tbody></table>')
        return "\n".join(out)

    en_html = render("en")
    lang_contents = {loc: render(loc) for loc in ("hk", "tw", "cn")}
    return en_html, lang_contents


# ---------------------------------------------------------------------------
# CSS — light + dark themes
# ---------------------------------------------------------------------------
SITE_CSS = """
:root, html[data-theme="light"] {
    --bg: #faf7f2;
    --text: #2d3748;
    --muted: #718096;
    --heading: #1a202c;
    --accent: #1e3a5f;
    --accent-hover: #2c5282;
    --accent-light: #e8f0fe;
    --border: #e2e8f0;
    --card-bg: #ffffff;
    --code-bg: #f3efe7;
    --nav-bg: #1e3a5f;
    --nav-text: #ffffff;
    --nav-hover: #2c5282;
    --breadcrumb-bg: #f1ece2;
    --footer-bg: #1e3a5f;
    --footer-text: #e2e8f0;
    --gold: #c5a44e;
    --row-stripe: #f8f4eb;
    --shadow: 0 1px 3px rgba(0,0,0,0.08);
    --shadow-lg: 0 4px 12px rgba(0,0,0,0.1);
    --menu-bg: #ffffff;
    --menu-border: #e2e8f0;
    --menu-text: #2d3748;
    --menu-hover: #f1ece2;
    --menu-sub-bg: #f8f4eb;
}

html[data-theme="dark"] {
    --bg: #0f1724;
    --text: #d6dee8;
    --muted: #8a98a8;
    --heading: #f1f5f9;
    --accent: #c5a44e;
    --accent-hover: #d8bb6c;
    --accent-light: rgba(197,164,78,0.12);
    --border: #1f2a3a;
    --card-bg: #16202f;
    --code-bg: #0b121d;
    --nav-bg: #0a0f1a;
    --nav-text: #f5e9c8;
    --nav-hover: rgba(197,164,78,0.18);
    --breadcrumb-bg: #131b29;
    --footer-bg: #0a0f1a;
    --footer-text: #c8cfdb;
    --gold: #c5a44e;
    --row-stripe: #131b29;
    --shadow: 0 1px 3px rgba(0,0,0,0.45);
    --shadow-lg: 0 6px 20px rgba(0,0,0,0.6);
    --menu-bg: #131b29;
    --menu-border: #1f2a3a;
    --menu-text: #d6dee8;
    --menu-hover: rgba(197,164,78,0.12);
    --menu-sub-bg: #0f1724;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { color-scheme: light dark; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    line-height: 1.8;
    color: var(--text);
    background: var(--bg);
    font-size: 17px;
    transition: background 0.2s ease, color 0.2s ease;
}

/* --- Top Navigation Bar --- */
.top-nav {
    background: var(--nav-bg);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: var(--shadow-lg);
}

.nav-inner {
    max-width: 1100px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    padding: 0 24px;
    min-height: 56px;
    gap: 12px;
}

.nav-brand {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-weight: 700;
    font-size: 1.15rem;
    color: var(--nav-text);
    text-decoration: none;
    letter-spacing: -0.3px;
    margin-right: auto;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 8px;
}

.nav-brand .brand-icon {
    color: var(--gold);
    font-size: 1.4rem;
}

/* Right-side controls cluster */
.nav-controls {
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Country flag selector — uses Twemoji for cross-platform rendering */
.lang-selector { display: flex; align-items: center; gap: 4px; }

.lang-btn {
    background: none;
    border: 2px solid transparent;
    border-radius: 4px;
    cursor: pointer;
    padding: 4px 6px;
    line-height: 1;
    transition: all 0.15s;
    opacity: 0.7;
    display: inline-flex;
    align-items: center;
    color: var(--nav-text);
}
.lang-btn img.emoji,
.lang-btn .flag-text {
    width: 22px; height: 22px;
    vertical-align: middle;
    font-size: 1.05rem;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-weight: 700;
    letter-spacing: 0;
}
.lang-btn .flag-text {
    width: auto; height: auto;
    padding: 0 4px;
    border-radius: 3px;
    background: rgba(255,255,255,0.08);
}
.lang-btn:hover { opacity: 1; }
.lang-btn.active {
    border-color: var(--gold);
    opacity: 1;
    background: rgba(197,164,78,0.18);
}

/* Theme toggle */
.theme-toggle {
    background: none;
    border: 2px solid transparent;
    border-radius: 4px;
    cursor: pointer;
    padding: 6px 8px;
    color: var(--nav-text);
    line-height: 1;
    transition: all 0.15s;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
.theme-toggle:hover {
    background: rgba(255,255,255,0.08);
    border-color: rgba(197,164,78,0.4);
}
.theme-toggle svg {
    width: 20px;
    height: 20px;
    fill: none;
    stroke: currentColor;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    display: block;
}
.theme-toggle .icon-light { display: none; }
.theme-toggle .icon-dark  { display: inline-flex; }
html[data-theme="dark"] .theme-toggle .icon-light { display: inline-flex; }
html[data-theme="dark"] .theme-toggle .icon-dark  { display: none; }

/* Hamburger button — anchored to the top-left, before the brand */
.hamburger {
    background: none;
    border: 2px solid transparent;
    border-radius: 4px;
    color: var(--nav-text);
    font-size: 1.5rem;
    line-height: 1;
    cursor: pointer;
    padding: 6px 12px;
    margin-right: 12px;
    transition: all 0.15s;
}
.hamburger:hover {
    background: rgba(255,255,255,0.08);
    border-color: rgba(197,164,78,0.4);
}
.hamburger.open { background: rgba(197,164,78,0.18); border-color: var(--gold); }

/* --- Slide-out menu panel --- */
.menu-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.4);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease;
    z-index: 199;
}
.menu-overlay.open { opacity: 1; pointer-events: auto; }

.menu-panel {
    position: fixed;
    top: 0;
    width: 340px;
    max-width: 88vw;
    height: 100vh;
    background: var(--menu-bg);
    box-shadow: var(--shadow-lg);
    transition: transform 0.25s ease;
    z-index: 200;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
}
/* Right-side variant (legacy) */
.menu-panel:not(.menu-panel-left) {
    right: 0;
    border-left: 1px solid var(--menu-border);
    transform: translateX(100%);
}
/* Left-side variant (current default) */
.menu-panel-left {
    left: 0;
    border-right: 1px solid var(--menu-border);
    transform: translateX(-100%);
}
.menu-panel.open { transform: translateX(0); }

.menu-header {
    padding: 18px 20px;
    border-bottom: 1px solid var(--menu-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--menu-sub-bg);
}
.menu-title {
    font-weight: 700;
    color: var(--heading);
    letter-spacing: 0.4px;
    text-transform: uppercase;
    font-size: 0.78rem;
}
.menu-close {
    background: none;
    border: none;
    cursor: pointer;
    color: var(--menu-text);
    font-size: 1.4rem;
    padding: 0 6px;
    line-height: 1;
}

.menu-body { padding: 8px 0 20px; }

.menu-link, .menu-sublink, .menu-trigger {
    display: flex;
    align-items: center;
    width: 100%;
    padding: 12px 20px;
    color: var(--menu-text);
    text-decoration: none;
    background: none;
    border: none;
    text-align: left;
    font: inherit;
    font-size: 0.92rem;
    cursor: pointer;
    border-bottom: 1px solid var(--menu-border);
    transition: background 0.12s;
}
.menu-link:hover, .menu-sublink:hover, .menu-trigger:hover {
    background: var(--menu-hover);
    color: var(--accent);
}
.menu-link.menu-top { font-weight: 700; }

.menu-trigger { justify-content: space-between; font-weight: 600; }
.menu-trigger .caret { transition: transform 0.2s ease; color: var(--muted); }
.menu-trigger[aria-expanded="true"] .caret { transform: rotate(90deg); color: var(--accent); }

.menu-sub {
    background: var(--menu-sub-bg);
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.25s ease;
}
.menu-group.open .menu-sub { max-height: 1200px; }

.menu-sublink {
    padding-left: 38px;
    font-size: 0.86rem;
    color: var(--text);
    border-bottom: 1px solid var(--menu-border);
}

/* --- Breadcrumb --- */
.breadcrumb-bar {
    background: var(--breadcrumb-bg);
    border-bottom: 1px solid var(--border);
    padding: 10px 24px;
}
.breadcrumb-inner {
    max-width: 1100px;
    margin: 0 auto;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 0.85rem;
    color: var(--muted);
}
.breadcrumb-inner a { color: var(--accent); text-decoration: none; }
.breadcrumb-inner a:hover { text-decoration: underline; }
.bc-sep { color: var(--muted); margin: 0 4px; opacity: 0.6; }

/* --- Main Content --- */
.main-wrap {
    max-width: 820px;
    margin: 0 auto;
    padding: 36px 24px 60px;
}

.lang-content { display: none; }
.lang-content.active { display: block; }

/* Language-swappable UI fragments (menu, breadcrumb, brand, footer, prev/next).
   Block versions hide via display:none; inline versions (spans) use the same
   default. The `.active-lang` class is toggled by switchLang() in JS. */
.lang-swap { display: none; }
.lang-swap.active-lang { display: block; }
span.lang-swap.active-lang { display: inline; }

h1 {
    font-size: 2rem;
    color: var(--heading);
    margin: 8px 0 20px;
    font-weight: 700;
    letter-spacing: -0.5px;
    line-height: 1.3;
}
h2 {
    font-size: 1.45rem;
    color: var(--heading);
    margin: 32px 0 14px;
    padding-bottom: 8px;
    border-bottom: 2px solid var(--accent-light);
    font-weight: 700;
}
h3 {
    font-size: 1.2rem;
    color: var(--heading);
    margin: 24px 0 10px;
    font-weight: 700;
}
h4 {
    font-size: 1.05rem;
    color: var(--heading);
    margin: 18px 0 8px;
    font-weight: 700;
}

p { margin-bottom: 14px; }
ul, ol { margin: 10px 0 18px 28px; }
li { margin-bottom: 6px; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 0.92rem;
    box-shadow: var(--shadow);
    border-radius: 6px;
    overflow: hidden;
    background: var(--card-bg);
}
th, td {
    padding: 10px 14px;
    border: 1px solid var(--border);
    text-align: left;
}
th {
    background: var(--accent);
    color: white;
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
html[data-theme="dark"] th { color: #0f1724; }
tr:nth-child(even) td { background: var(--row-stripe); }

.glossary-table th:first-child { width: 28%; }

/* Linked level headers on the overview page */
.level-link {
    color: inherit;
    text-decoration: none;
    border-bottom: 2px solid var(--accent-light);
    transition: color 0.15s, border-color 0.15s;
}
.level-link:hover {
    color: var(--accent);
    border-bottom-color: var(--accent);
}

/* Clickable week rows on level overview pages */
.week-row { cursor: pointer; transition: background 0.12s; }
.week-row:hover td { background: var(--accent-light); }
.week-row td a { color: var(--accent); text-decoration: none; }
.week-row:hover td a { text-decoration: underline; }
.week-row td:first-child { width: 4em; text-align: center; font-weight: 700; }

pre {
    background: var(--code-bg);
    padding: 16px 20px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 16px 0;
    border: 1px solid var(--border);
    font-size: 0.88rem;
    color: var(--text);
}
code {
    font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
    font-size: 0.9em;
}
p code, li code {
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 3px;
    border: 1px solid var(--border);
}

blockquote {
    border-left: 4px solid var(--accent);
    padding: 12px 20px;
    margin: 16px 0;
    background: var(--accent-light);
    border-radius: 0 6px 6px 0;
    font-style: italic;
}

hr { border: none; border-top: 1px solid var(--border); margin: 32px 0; }

a { color: var(--accent); }
a:hover { color: var(--accent-hover); }

img { max-width: 100%; height: auto; border-radius: 6px; margin: 12px 0; }

/* --- Footer Navigation --- */
.page-footer {
    max-width: 820px;
    margin: 0 auto;
    padding: 0 24px 40px;
}

.nav-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 24px;
    border-top: 2px solid var(--border);
    gap: 16px;
}

.nav-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    text-decoration: none;
    color: var(--accent);
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    transition: all 0.15s;
    box-shadow: var(--shadow);
    max-width: 45%;
}
.nav-btn:hover {
    background: var(--accent);
    color: var(--bg);
    border-color: var(--accent);
    box-shadow: var(--shadow-lg);
}
.nav-btn .btn-label {
    font-size: 0.75rem;
    color: var(--muted);
    display: block;
    font-weight: 400;
}
.nav-btn:hover .btn-label { color: rgba(255,255,255,0.7); }
html[data-theme="dark"] .nav-btn:hover .btn-label { color: rgba(15,23,36,0.7); }
.nav-btn-text { display: flex; flex-direction: column; }
.nav-btn.next { text-align: right; margin-left: auto; }
.nav-btn.next .nav-btn-text { align-items: flex-end; }
.nav-placeholder { flex: 1; }

/* --- Site Footer --- */
.site-footer {
    background: var(--footer-bg);
    color: var(--footer-text);
    padding: 24px;
    text-align: center;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 0.82rem;
    margin-top: 40px;
}
.site-footer a { color: var(--gold); }

/* --- Mobile --- */
@media (max-width: 640px) {
    .nav-inner { padding: 0 14px; gap: 6px; }
    .nav-brand { font-size: 0.95rem; }
    .nav-brand .brand-text-long { display: none; }
    .lang-btn { padding: 3px 4px; }
    .lang-btn img.emoji, .lang-btn .flag-text { width: 18px; height: 18px; font-size: 0.85rem; }
    .main-wrap { padding: 20px 16px 40px; }
    h1 { font-size: 1.5rem; }
    .nav-btn { padding: 10px 14px; font-size: 0.8rem; }
    .menu-panel { width: 86vw; }
}
"""


# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------
SITE_JS = r"""
// --- Theme handling (must run before paint to avoid flash) ---
function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem('preferred-theme', theme); } catch(e) {}
}
function toggleTheme() {
    var current = document.documentElement.getAttribute('data-theme') || 'light';
    applyTheme(current === 'dark' ? 'light' : 'dark');
}

// --- Language switching ---
function switchLang(lang) {
    document.querySelectorAll('.lang-content').forEach(el => el.classList.remove('active'));
    var el = document.getElementById('content-' + lang);
    if (el) el.classList.add('active');
    // Per-locale UI fragments (menu, breadcrumb, brand, footer, nav buttons)
    document.querySelectorAll('.lang-swap').forEach(el => {
        el.classList.toggle('active-lang', el.dataset.langSection === lang);
    });
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.lang === lang) btn.classList.add('active');
    });
    document.documentElement.setAttribute('lang', lang === 'en' ? 'en' : 'zh-' + lang.toUpperCase());
    try { localStorage.setItem('preferred-lang', lang); } catch(e) {}
}

// --- Hamburger menu ---
function toggleMenu(force) {
    var panel = document.querySelector('.menu-panel');
    var overlay = document.querySelector('.menu-overlay');
    var btn = document.querySelector('.hamburger');
    if (!panel || !overlay || !btn) return;
    var open = (typeof force === 'boolean') ? force : !panel.classList.contains('open');
    panel.classList.toggle('open', open);
    overlay.classList.toggle('open', open);
    btn.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
}

function setupMenuTriggers() {
    document.querySelectorAll('.menu-trigger').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var group = btn.parentElement;
            var open = !group.classList.contains('open');
            group.classList.toggle('open', open);
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    });
}

// --- Init on DOMContentLoaded ---
document.addEventListener('DOMContentLoaded', function() {
    setupMenuTriggers();

    var saved = null;
    try { saved = localStorage.getItem('preferred-lang'); } catch(e) {}
    if (saved && saved !== 'en') switchLang(saved);

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') toggleMenu(false);
    });

    var overlay = document.querySelector('.menu-overlay');
    if (overlay) overlay.addEventListener('click', function() { toggleMenu(false); });

    // Twemoji upgrade — replaces emoji with high-quality SVGs so flags render
    // consistently on Windows / Linux where the system font may show letters.
    if (typeof twemoji !== 'undefined') {
        twemoji.parse(document.body, { folder: 'svg', ext: '.svg' });
    }
});

// Apply saved theme as early as possible (script in <head>)
(function() {
    try {
        var t = localStorage.getItem('preferred-theme');
        if (!t) {
            t = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
                ? 'dark' : 'light';
        }
        document.documentElement.setAttribute('data-theme', t);
    } catch(e) {
        document.documentElement.setAttribute('data-theme', 'light');
    }
})();
"""

# Inline early-theme script (to avoid flash of wrong theme)
EARLY_THEME_SCRIPT = """(function(){try{var t=localStorage.getItem('preferred-theme');if(!t){t=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}document.documentElement.setAttribute('data-theme',t);}catch(e){document.documentElement.setAttribute('data-theme','light');}})();"""


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
def _wrap_lang_swap(by_locale, default="en", inline=False):
    """Wrap per-locale strings in <span data-lang-section> elements; only the
    one matching the active language is shown via JS. `inline=True` uses
    <span> with display:inline; otherwise uses <div>."""
    tag = "span" if inline else "div"
    parts = []
    for loc in LOCALES:
        active = " active-lang" if loc == default else ""
        parts.append(
            f'<{tag} class="lang-swap{active}" data-lang-section="{loc}">'
            f'{by_locale[loc]}</{tag}>'
        )
    return "".join(parts)


def page_template(title, content, lang_contents, menus, breadcrumbs, prev_page, next_page, prev_titles, next_titles):
    # Country flags: emoji + ISO letters fallback. Twemoji JS replaces emoji
    # with SVG images at runtime; if that fails we still see the letters.
    lang_buttons = [
        ("en", "\U0001F1FA\U0001F1F8", "EN", "English"),
        ("hk", "\U0001F1ED\U0001F1F0", "HK", "香港繁體"),
        ("tw", "\U0001F1F9\U0001F1FC", "TW", "台灣繁體"),
        ("cn", "\U0001F1E8\U0001F1F3", "CN", "中国简体"),
    ]

    lang_selector = ""
    for code, flag, letters, name in lang_buttons:
        active = " active" if code == "en" else ""
        lang_selector += (
            f'<button class="lang-btn{active}" data-lang="{code}" '
            f'onclick="switchLang(\'{code}\')" title="{name}" aria-label="{name}">'
            f'<span class="emoji-wrap">{flag}</span>'
            f'<span class="flag-text" hidden>{letters}</span>'
            f'</button>'
        )

    # Per-locale prev/next buttons (label + page title both translated)
    def render_nav_buttons(loc):
        L = LOCALE_LABELS[loc]
        if prev_page:
            prev_t = prev_titles.get(loc, prev_page["nav_title"])
            prev_h = (
                f'<a href="{prev_page["slug"]}.html" class="nav-btn prev">'
                f'<span style="font-size:1.2rem">&#8592;</span>'
                f'<span class="nav-btn-text">'
                f'<span class="btn-label">{L["previous"]}</span>'
                f'<span>{prev_t}</span></span></a>'
            )
        else:
            prev_h = '<span class="nav-placeholder"></span>'
        if next_page:
            next_t = next_titles.get(loc, next_page["nav_title"])
            next_h = (
                f'<a href="{next_page["slug"]}.html" class="nav-btn next">'
                f'<span class="nav-btn-text">'
                f'<span class="btn-label">{L["next"]}</span>'
                f'<span>{next_t}</span></span>'
                f'<span style="font-size:1.2rem">&#8594;</span></a>'
            )
        else:
            next_h = '<span class="nav-placeholder"></span>'
        return f'<div class="nav-buttons">{prev_h}{next_h}</div>'

    nav_buttons_html = _wrap_lang_swap({l: render_nav_buttons(l) for l in LOCALES})
    menu_body_html = _wrap_lang_swap({l: menus[l] for l in LOCALES})
    breadcrumb_html = _wrap_lang_swap({l: breadcrumbs[l] for l in LOCALES}, inline=True)

    brand_html = _wrap_lang_swap(
        {l: LOCALE_LABELS[l]["brand"] for l in LOCALES}, inline=True
    )
    menu_title_html = _wrap_lang_swap(
        {l: LOCALE_LABELS[l]["menu_title"] for l in LOCALES}, inline=True
    )
    footer_tagline_html = _wrap_lang_swap(
        {l: LOCALE_LABELS[l]["footer_tagline"] for l in LOCALES}, inline=True
    )
    footer_links_html = _wrap_lang_swap(
        {
            l: (
                f'{LOCALE_LABELS[l]["course_root"]} &copy; 2025 &middot; '
                f'<a href="glossary.html">{LOCALE_LABELS[l]["glossary"]}</a> &middot; '
                f'<a href="disclaimer.html">{LOCALE_LABELS[l]["disclaimer"]}</a> &middot; '
                f'<a href="faq.html">{LOCALE_LABELS[l]["faq"]}</a> &middot; '
                f'<a href="https://www.patreon.com/c/hevangel">Patreon</a>'
            )
            for l in LOCALES
        },
        inline=True,
    )

    pending_hk = f'<p><em>{LOCALE_LABELS["hk"]["translation_pending"]}</em></p>'
    pending_tw = f'<p><em>{LOCALE_LABELS["tw"]["translation_pending"]}</em></p>'
    pending_cn = f'<p><em>{LOCALE_LABELS["cn"]["translation_pending"]}</em></p>'
    hk_content = lang_contents.get("hk", pending_hk)
    tw_content = lang_contents.get("tw", pending_tw)
    cn_content = lang_contents.get("cn", pending_cn)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Chanma Investment Tutorial</title>
    <script>{EARLY_THEME_SCRIPT}</script>
    <style>{SITE_CSS}</style>
    <script src="https://cdn.jsdelivr.net/npm/@twemoji/api@latest/dist/twemoji.min.js" crossorigin="anonymous" defer></script>
</head>
<body>
    <nav class="top-nav">
        <div class="nav-inner">
            <button class="hamburger" onclick="toggleMenu()" aria-label="Open menu" aria-controls="site-menu">&#9776;</button>
            <a href="index.html" class="nav-brand">
                <span class="brand-icon">&#9670;</span>
                <span class="brand-text-long">{brand_html}</span>
            </a>
            <div class="nav-controls">
                <div class="lang-selector">{lang_selector}</div>
                <button class="theme-toggle" onclick="toggleTheme()" title="Toggle dark / light theme" aria-label="Toggle theme">
                    <span class="icon-dark" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg></span>
                    <span class="icon-light" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg></span>
                </button>
            </div>
        </div>
    </nav>

    <div class="menu-overlay" aria-hidden="true"></div>
    <aside id="site-menu" class="menu-panel menu-panel-left" aria-label="Site navigation">
        <div class="menu-header">
            <span class="menu-title">{menu_title_html}</span>
            <button class="menu-close" onclick="toggleMenu(false)" aria-label="Close menu">&#10005;</button>
        </div>
        <div class="menu-body">
            {menu_body_html}
        </div>
    </aside>

    <div class="breadcrumb-bar">
        <div class="breadcrumb-inner">{breadcrumb_html}</div>
    </div>

    <main class="main-wrap">
        <div class="content-area">
            <div id="content-en" class="lang-content active">
                {content}
            </div>
            <div id="content-hk" class="lang-content">
                {hk_content}
            </div>
            <div id="content-tw" class="lang-content">
                {tw_content}
            </div>
            <div id="content-cn" class="lang-content">
                {cn_content}
            </div>
        </div>
    </main>

    <footer class="page-footer">
        {nav_buttons_html}
    </footer>

    <footer class="site-footer">
        <p>{footer_links_html}</p>
        <p style="margin-top:4px;opacity:0.7;">{footer_tagline_html}</p>
    </footer>

    <script>{SITE_JS}</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Main build function
# ---------------------------------------------------------------------------
def build():
    course_dir = os.path.join(PROJECT_ROOT, "course")
    hk_dir = os.path.join(PROJECT_ROOT, "course_hk")
    tw_dir = os.path.join(PROJECT_ROOT, "course_tw")
    cn_dir = os.path.join(PROJECT_ROOT, "course_cn")
    docs_dir = os.path.join(PROJECT_ROOT, "docs")

    os.makedirs(docs_dir, exist_ok=True)

    try:
        course_files = sorted(f for f in os.listdir(course_dir) if f.endswith(".md"))
    except OSError as e:
        print(f"Error reading course directory: {e}")
        return

    if not course_files:
        print("No markdown files found in course/. Nothing to build.")
        return

    print(f"Found {len(course_files)} markdown files in course/")

    pages = build_page_list(course_files)
    lang_dirs = {"en": course_dir, "hk": hk_dir, "tw": tw_dir, "cn": cn_dir}
    menus = {loc: build_nav_menu(pages, loc, lang_dirs) for loc in LOCALES}

    glossary_en, glossary_lang = build_glossary_html()

    for i, page in enumerate(pages):
        if page["slug"] == "glossary":
            html_content = glossary_en
            lang_contents = glossary_lang
            title = "Glossary"
        else:
            source_file = page["file"]
            source_path = os.path.join(course_dir, source_file)

            if not os.path.exists(source_path):
                print(f"  Skipping {source_file} (not found)")
                continue

            md_content = open(source_path, "r", encoding="utf-8").read()
            article_content = strip_youtube_section(md_content)
            html_content = markdown_to_html(article_content)

            lang_contents = {}
            for lang, lang_dir in [("hk", hk_dir), ("tw", tw_dir), ("cn", cn_dir)]:
                lang_path = os.path.join(lang_dir, source_file)
                if os.path.exists(lang_path):
                    lang_md = open(lang_path, "r", encoding="utf-8").read()
                    lang_article = strip_youtube_section(lang_md)
                    lang_contents[lang] = markdown_to_html(lang_article)

            title = extract_title(article_content)

            # Cross-page hyperlink upgrades
            if page["slug"] == "index":
                html_content = linkify_overview_levels(html_content)
                lang_contents = {k: linkify_overview_levels(v) for k, v in lang_contents.items()}
            elif page["type"] == "level_overview":
                level_num = page["level"]
                html_content = linkify_level_weeks(html_content, level_num)
                lang_contents = {k: linkify_level_weeks(v, level_num) for k, v in lang_contents.items()}

        breadcrumbs = {loc: build_breadcrumb(page, loc, lang_dirs) for loc in LOCALES}
        prev_page = pages[i - 1] if i > 0 else None
        next_page = pages[i + 1] if i < len(pages) - 1 else None

        prev_titles = {loc: get_translated_nav_title(prev_page, loc, lang_dirs)
                       for loc in LOCALES} if prev_page else {}
        next_titles = {loc: get_translated_nav_title(next_page, loc, lang_dirs)
                       for loc in LOCALES} if next_page else {}

        html = page_template(
            title, html_content, lang_contents, menus, breadcrumbs,
            prev_page, next_page, prev_titles, next_titles,
        )

        out_name = f"{page['slug']}.html"
        out_path = os.path.join(docs_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"  Built: {out_name}")

    print(f"\nDone! Built {len(pages)} pages in docs/")


if __name__ == "__main__":
    build()
