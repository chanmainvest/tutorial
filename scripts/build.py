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
    pattern = r"\n---\s*\n\s*## Part 2: YouTube Script.*"
    return re.sub(pattern, "", md, flags=re.DOTALL)


def extract_title(md):
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1) if m else "Untitled"


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
def build_nav_menu(pages):
    """Multilevel accordion menu opened by the hamburger button."""
    parts = ['<a href="index.html" class="menu-link menu-top">Home</a>']

    for level_idx, level in enumerate(LEVELS):
        level_num = level_idx + 1
        level_pages = [p for p in pages if p.get("level") == level_num]
        if not level_pages:
            continue

        parts.append('<div class="menu-group">')
        parts.append(
            f'<button class="menu-trigger" type="button" aria-expanded="false">'
            f'<span>{level["name"]}</span>'
            f'<span class="caret">&#9656;</span>'
            f'</button>'
        )
        parts.append('<div class="menu-sub">')
        for p in level_pages:
            parts.append(f'<a href="{p["slug"]}.html" class="menu-sublink">{p["nav_title"]}</a>')
        parts.append('</div>')
        parts.append('</div>')

    side_pages = [p for p in pages if p["type"] == "side"]
    if side_pages:
        parts.append('<div class="menu-group">')
        parts.append(
            '<button class="menu-trigger" type="button" aria-expanded="false">'
            '<span>Side Lessons</span><span class="caret">&#9656;</span></button>'
        )
        parts.append('<div class="menu-sub">')
        for p in side_pages:
            parts.append(f'<a href="{p["slug"]}.html" class="menu-sublink">{p["nav_title"]}</a>')
        parts.append('</div></div>')

    info_pages = [p for p in pages if p["type"] == "info"]
    for p in info_pages:
        parts.append(f'<a href="{p["slug"]}.html" class="menu-link">{p["nav_title"]}</a>')

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Breadcrumb
# ---------------------------------------------------------------------------
def build_breadcrumb(page, pages):
    crumbs = ['<a href="index.html">Chanma Investment Tutorial</a>']

    if page["type"] == "level_overview":
        level_num = page["level"]
        crumbs.append(f'<span>{LEVELS[level_num - 1]["name"]}</span>')
    elif page["type"] == "week":
        level_num = page["level"]
        crumbs.append(f'<a href="level{level_num}.html">{LEVELS[level_num - 1]["name"]}</a>')
        crumbs.append(f'<span>{page["title"]}</span>')
    elif page["type"] == "side":
        crumbs.append('<span>Side Lessons</span>')
        crumbs.append(f'<span>{page["title"]}</span>')
    elif page["type"] == "info":
        crumbs.append(f'<span>{page["title"]}</span>')
    elif page["slug"] == "index":
        crumbs = ['<span>Chanma Investment Tutorial</span>']

    return ' <span class="bc-sep">&#8250;</span> '.join(crumbs)


# ---------------------------------------------------------------------------
# Glossary page generation
# ---------------------------------------------------------------------------
def build_glossary_html():
    with open(TERMINOLOGY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    parts = ['<h1>Glossary &mdash; Investment Terminology</h1>']
    parts.append(
        '<p>Cross-reference table for investment terms across English, '
        'Hong Kong (繁體), Taiwan (繁體), and Mainland China (簡體). '
        'These translations are the canonical vocabulary used throughout the course.</p>'
    )
    intro_lang = {
        "hk": "詞彙表 — 投資術語對照表（英文 / 香港 / 台灣 / 中國大陸）",
        "tw": "詞彙表 — 投資術語對照表（英文 / 香港 / 台灣 / 中國大陸）",
        "cn": "词汇表 — 投资术语对照表（英文 / 香港 / 台湾 / 中国大陆）",
    }

    def render_table(locale_for_intro=None):
        out = []
        if locale_for_intro:
            out.append(f'<h1>{intro_lang[locale_for_intro]}</h1>')
        for category, terms in data["categories"].items():
            out.append(f'<h2>{category}</h2>')
            out.append('<table class="glossary-table">')
            out.append('<thead><tr><th>English</th><th>HK 🇭🇰</th><th>TW 🇹🇼</th><th>CN 🇨🇳</th></tr></thead>')
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

    en_html = "\n".join(parts) + "\n" + render_table()
    lang_contents = {loc: render_table(loc) for loc in ("hk", "tw", "cn")}
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
    font-size: 1.1rem;
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
.theme-toggle .icon-light { display: none; }
.theme-toggle .icon-dark { display: inline; }
html[data-theme="dark"] .theme-toggle .icon-light { display: inline; }
html[data-theme="dark"] .theme-toggle .icon-dark { display: none; }

/* Hamburger button (always visible) */
.hamburger {
    background: none;
    border: 2px solid transparent;
    border-radius: 4px;
    color: var(--nav-text);
    font-size: 1.4rem;
    line-height: 1;
    cursor: pointer;
    padding: 6px 10px;
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
    right: 0;
    width: 340px;
    max-width: 88vw;
    height: 100vh;
    background: var(--menu-bg);
    border-left: 1px solid var(--menu-border);
    box-shadow: var(--shadow-lg);
    transform: translateX(100%);
    transition: transform 0.25s ease;
    z-index: 200;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
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
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.lang === lang) btn.classList.add('active');
    });
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
def page_template(title, content, lang_contents, nav_menu, breadcrumb, prev_page, next_page):
    # Country flags: emoji + ISO letters fallback. Twemoji JS replaces emoji
    # with SVG images at runtime; if that fails we still see the letters.
    lang_buttons = [
        ("en", "\U0001F1EC\U0001F1E7", "EN", "English"),
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

    prev_html = ""
    next_html = ""
    if prev_page:
        prev_html = (
            f'<a href="{prev_page["slug"]}.html" class="nav-btn prev">'
            f'<span style="font-size:1.2rem">&#8592;</span>'
            f'<span class="nav-btn-text">'
            f'<span class="btn-label">Previous</span>'
            f'<span>{prev_page["nav_title"]}</span>'
            f'</span></a>'
        )
    else:
        prev_html = '<span class="nav-placeholder"></span>'

    if next_page:
        next_html = (
            f'<a href="{next_page["slug"]}.html" class="nav-btn next">'
            f'<span class="nav-btn-text">'
            f'<span class="btn-label">Next</span>'
            f'<span>{next_page["nav_title"]}</span>'
            f'</span>'
            f'<span style="font-size:1.2rem">&#8594;</span>'
            f'</a>'
        )
    else:
        next_html = '<span class="nav-placeholder"></span>'

    hk_content = lang_contents.get("hk", "<p><em>Translation coming soon...</em></p>")
    tw_content = lang_contents.get("tw", "<p><em>Translation coming soon...</em></p>")
    cn_content = lang_contents.get("cn", "<p><em>Translation coming soon...</em></p>")

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
            <a href="index.html" class="nav-brand">
                <span class="brand-icon">&#9670;</span>
                <span class="brand-text-long">Chanma Investment</span>
            </a>
            <div class="nav-controls">
                <div class="lang-selector">{lang_selector}</div>
                <button class="theme-toggle" onclick="toggleTheme()" title="Toggle dark / light theme" aria-label="Toggle theme">
                    <span class="icon-dark">&#9789;</span>
                    <span class="icon-light">&#9728;</span>
                </button>
                <button class="hamburger" onclick="toggleMenu()" aria-label="Open menu" aria-controls="site-menu">&#9776;</button>
            </div>
        </div>
    </nav>

    <div class="menu-overlay" aria-hidden="true"></div>
    <aside id="site-menu" class="menu-panel" aria-label="Site navigation">
        <div class="menu-header">
            <span class="menu-title">Course Navigation</span>
            <button class="menu-close" onclick="toggleMenu(false)" aria-label="Close menu">&#10005;</button>
        </div>
        <div class="menu-body">
            {nav_menu}
        </div>
    </aside>

    <div class="breadcrumb-bar">
        <div class="breadcrumb-inner">{breadcrumb}</div>
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
        <div class="nav-buttons">
            {prev_html}
            {next_html}
        </div>
    </footer>

    <footer class="site-footer">
        <p>Chanma Investment Tutorial &copy; 2025 &middot; <a href="glossary.html">Glossary</a> &middot; <a href="disclaimer.html">Disclaimer</a> &middot; <a href="faq.html">FAQ</a> &middot; <a href="https://www.patreon.com/c/hevangel">Patreon</a></p>
        <p style="margin-top:4px;opacity:0.7;">Released under the MIT License. Educational content only &mdash; not financial advice.</p>
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
    nav_menu = build_nav_menu(pages)

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

        breadcrumb = build_breadcrumb(page, pages)
        prev_page = pages[i - 1] if i > 0 else None
        next_page = pages[i + 1] if i < len(pages) - 1 else None

        html = page_template(
            title, html_content, lang_contents, nav_menu, breadcrumb,
            prev_page, next_page,
        )

        out_name = f"{page['slug']}.html"
        out_path = os.path.join(docs_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"  Built: {out_name}")

    print(f"\nDone! Built {len(pages)} pages in docs/")


if __name__ == "__main__":
    build()
