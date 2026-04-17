#!/usr/bin/env python3
"""
Static Site Generator for Chanma Investment Tutorial

Reads markdown files from course/, course_hk/, course_tw/, course_cn/
and generates a static website in docs/ with:
- Single-panel layout with top navigation bar
- Breadcrumb navigation
- Country flag language selector
- Prev/next page buttons in footer
- YouTube script sections filtered out (article content only)
- Professional, trust-building visual theme

Usage: python scripts/build.py
"""

import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

    # Code blocks (fenced)
    def replace_code_block(m):
        lang = m.group(1)
        code = m.group(2)
        code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    html = re.sub(r"```(\w*)\n([\s\S]*?)```", replace_code_block, html)

    # Inline code
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)

    # Headers
    html = re.sub(r"^######\s+(.+)$", r"<h6>\1</h6>", html, flags=re.MULTILINE)
    html = re.sub(r"^#####\s+(.+)$", r"<h5>\1</h5>", html, flags=re.MULTILINE)
    html = re.sub(r"^####\s+(.+)$", r"<h4>\1</h4>", html, flags=re.MULTILINE)
    html = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", html)
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)

    # Images (before links so ![...](...) is not matched as link)
    html = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', html)

    # Links
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)

    # Horizontal rules
    html = re.sub(r"^---$", "<hr>", html, flags=re.MULTILINE)

    # Tables
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

    # Blockquotes
    html = re.sub(r"^>\s+(.+)$", r"<blockquote>\1</blockquote>", html, flags=re.MULTILINE)

    # Unordered lists
    html = re.sub(r"^[\s]*[-*]\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"(<li>.*</li>\n?)+", r"<ul>\g<0></ul>", html)

    # Ordered lists
    html = re.sub(r"^\d+\.\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)

    # Paragraphs
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
    """Remove Part 2: YouTube Script section from markdown content."""
    # Match "## Part 2: YouTube Script" and everything after it
    pattern = r"\n---\s*\n\s*## Part 2: YouTube Script.*"
    result = re.sub(pattern, "", md, flags=re.DOTALL)
    return result


# ---------------------------------------------------------------------------
# Extract title from markdown
# ---------------------------------------------------------------------------
def extract_title(md):
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1) if m else "Untitled"


# ---------------------------------------------------------------------------
# Build ordered page list for navigation
# ---------------------------------------------------------------------------
def build_page_list(course_files):
    """Build ordered list of all pages with metadata for navigation."""
    pages = []

    # Course overview (index)
    pages.append({
        "slug": "index",
        "file": "overview.md",
        "title": "Course Overview",
        "level": None,
        "type": "overview",
        "nav_title": "Course Overview",
    })

    # Level overviews and weekly lessons
    for level_idx, level in enumerate(LEVELS):
        level_num = level_idx + 1
        overview_file = f"{level['overview']}.md"
        if overview_file in course_files:
            pages.append({
                "slug": f"level{level_num}",
                "file": overview_file,
                "title": level["name"],
                "level": level_num,
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
                    "slug": f"week{week_str}",
                    "file": file,
                    "title": f"Week {week_num}: {topic}",
                    "level": level_num,
                    "type": "week",
                    "week_num": week_num,
                    "nav_title": f"Week {week_num}: {topic}",
                })

    # Side lessons
    side_files = sorted([f for f in course_files if f.startswith("side")])
    for file in side_files:
        m = re.match(r"side(\d+)_(.+)\.md", file)
        if m:
            num = int(m.group(1))
            topic = m.group(2).replace("_", " ")
            topic = topic[0].upper() + topic[1:]
            pages.append({
                "slug": f"side{m.group(1)}",
                "file": file,
                "title": f"Side {num}: {topic}",
                "level": None,
                "type": "side",
                "nav_title": f"Side {num}: {topic}",
            })

    # Disclaimer
    if "disclaimer.md" in course_files:
        pages.append({
            "slug": "disclaimer",
            "file": "disclaimer.md",
            "title": "Disclaimer",
            "level": None,
            "type": "info",
            "nav_title": "Disclaimer",
        })

    # FAQ (at the end)
    if "faq.md" in course_files:
        pages.append({
            "slug": "faq",
            "file": "faq.md",
            "title": "FAQ",
            "level": None,
            "type": "info",
            "nav_title": "FAQ",
        })

    return pages


# ---------------------------------------------------------------------------
# Build navigation menu HTML
# ---------------------------------------------------------------------------
def build_nav_menu(pages):
    """Build dropdown navigation menu HTML."""
    menu = ""

    # Course overview
    menu += '<div class="nav-dropdown">'
    menu += '<a href="index.html" class="nav-link">Home</a>'
    menu += "</div>"

    # Levels with dropdowns
    for level_idx, level in enumerate(LEVELS):
        level_num = level_idx + 1
        level_pages = [p for p in pages if p.get("level") == level_num]
        if not level_pages:
            continue

        menu += '<div class="nav-dropdown">'
        menu += f'<button class="nav-link dropdown-trigger">Level {level_num} <span class="arrow">&#9662;</span></button>'
        menu += '<div class="dropdown-content">'

        for p in level_pages:
            menu += f'<a href="{p["slug"]}.html">{p["nav_title"]}</a>'

        menu += "</div></div>"

    # Side lessons dropdown
    side_pages = [p for p in pages if p["type"] == "side"]
    if side_pages:
        menu += '<div class="nav-dropdown">'
        menu += '<button class="nav-link dropdown-trigger">Side Lessons <span class="arrow">&#9662;</span></button>'
        menu += '<div class="dropdown-content">'
        for p in side_pages:
            menu += f'<a href="{p["slug"]}.html">{p["nav_title"]}</a>'
        menu += "</div></div>"

    # Info pages
    info_pages = [p for p in pages if p["type"] == "info"]
    if info_pages:
        for p in info_pages:
            menu += f'<div class="nav-dropdown"><a href="{p["slug"]}.html" class="nav-link">{p["nav_title"]}</a></div>'

    return menu


# ---------------------------------------------------------------------------
# Build breadcrumb HTML
# ---------------------------------------------------------------------------
def build_breadcrumb(page, pages):
    """Build breadcrumb navigation HTML."""
    crumbs = [('<a href="index.html">Chanma Investment Tutorial</a>')]

    if page["type"] == "level_overview":
        level_num = page["level"]
        crumbs.append(f'<span>{LEVELS[level_num - 1]["name"]}</span>')
    elif page["type"] == "week":
        level_num = page["level"]
        crumbs.append(f'<a href="level{level_num}.html">{LEVELS[level_num - 1]["name"]}</a>')
        # Show topic only (week number is in breadcrumb context already)
        topic = page["title"]
        crumbs.append(f"<span>{topic}</span>")
    elif page["type"] == "side":
        crumbs.append('<span>Side Lessons</span>')
        crumbs.append(f'<span>{page["title"]}</span>')
    elif page["type"] == "info":
        crumbs.append(f'<span>{page["title"]}</span>')
    elif page["slug"] == "index":
        crumbs = ['<span>Chanma Investment Tutorial</span>']

    return ' <span class="bc-sep">&#8250;</span> '.join(crumbs)


# ---------------------------------------------------------------------------
# CSS for the professional theme
# ---------------------------------------------------------------------------
SITE_CSS = """
:root {
    --bg: #fafbfc;
    --text: #2d3748;
    --heading: #1a202c;
    --accent: #1e3a5f;
    --accent-hover: #2c5282;
    --accent-light: #e8f0fe;
    --border: #e2e8f0;
    --card-bg: #ffffff;
    --code-bg: #f7fafc;
    --nav-bg: #1e3a5f;
    --nav-text: #ffffff;
    --nav-hover: #2c5282;
    --breadcrumb-bg: #f1f5f9;
    --footer-bg: #1e3a5f;
    --footer-text: #e2e8f0;
    --success: #38a169;
    --warning: #d69e2e;
    --gold: #c5a44e;
    --shadow: 0 1px 3px rgba(0,0,0,0.08);
    --shadow-lg: 0 4px 12px rgba(0,0,0,0.1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    line-height: 1.8;
    color: var(--text);
    background: var(--bg);
    font-size: 17px;
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
    gap: 0;
}

.nav-brand {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-weight: 700;
    font-size: 1.15rem;
    color: var(--nav-text);
    text-decoration: none;
    letter-spacing: -0.3px;
    margin-right: 32px;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 8px;
}

.nav-brand .brand-icon {
    font-size: 1.4rem;
}

.nav-menu {
    display: flex;
    align-items: center;
    gap: 0;
    flex: 1;
}

.nav-dropdown {
    position: relative;
}

.nav-link, .dropdown-trigger {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: var(--nav-text);
    text-decoration: none;
    padding: 16px 14px;
    font-size: 0.88rem;
    font-weight: 500;
    background: none;
    border: none;
    cursor: pointer;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: background 0.15s;
}

.nav-link:hover, .dropdown-trigger:hover {
    background: var(--nav-hover);
}

.arrow { font-size: 0.7rem; }

.dropdown-content {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    background: var(--card-bg);
    min-width: 320px;
    box-shadow: var(--shadow-lg);
    border: 1px solid var(--border);
    border-radius: 0 0 6px 6px;
    z-index: 200;
    max-height: 480px;
    overflow-y: auto;
}

.nav-dropdown:hover .dropdown-content {
    display: block;
}

.dropdown-content a {
    display: block;
    padding: 10px 16px;
    color: var(--text);
    text-decoration: none;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 0.85rem;
    border-bottom: 1px solid #f0f0f0;
    transition: background 0.1s;
}

.dropdown-content a:hover {
    background: var(--accent-light);
    color: var(--accent);
}

.dropdown-content a:last-child { border-bottom: none; }

/* Language selector in nav */
.lang-selector {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 6px;
}

.lang-btn {
    background: none;
    border: 2px solid transparent;
    border-radius: 4px;
    cursor: pointer;
    padding: 4px 6px;
    font-size: 1.3rem;
    line-height: 1;
    transition: all 0.15s;
    opacity: 0.7;
}

.lang-btn:hover { opacity: 1; }

.lang-btn.active {
    border-color: var(--gold);
    opacity: 1;
    background: rgba(255,255,255,0.15);
}

/* Mobile hamburger */
.hamburger {
    display: none;
    background: none;
    border: none;
    color: var(--nav-text);
    font-size: 1.5rem;
    cursor: pointer;
    padding: 8px;
    margin-left: auto;
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
    color: #718096;
}

.breadcrumb-inner a {
    color: var(--accent);
    text-decoration: none;
}

.breadcrumb-inner a:hover { text-decoration: underline; }

.bc-sep { color: #a0aec0; margin: 0 4px; }

/* --- Main Content --- */
.main-wrap {
    max-width: 820px;
    margin: 0 auto;
    padding: 36px 24px 60px;
}

.content-area { }

.lang-content { display: none; }
.lang-content.active { display: block; }

/* Typography */
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

tr:nth-child(even) { background: #f8fafc; }

pre {
    background: var(--code-bg);
    padding: 16px 20px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 16px 0;
    border: 1px solid var(--border);
    font-size: 0.88rem;
}

code {
    font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
    font-size: 0.9em;
}

p code {
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
    color: white;
    border-color: var(--accent);
    box-shadow: var(--shadow-lg);
}

.nav-btn .btn-label {
    font-size: 0.75rem;
    color: #a0aec0;
    display: block;
    font-weight: 400;
}

.nav-btn:hover .btn-label { color: rgba(255,255,255,0.7); }

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
@media (max-width: 768px) {
    .nav-menu { display: none; }
    .nav-menu.open {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 56px;
        left: 0;
        right: 0;
        background: var(--nav-bg);
        box-shadow: var(--shadow-lg);
        padding-bottom: 8px;
    }
    .nav-menu.open .nav-dropdown { width: 100%; }
    .nav-menu.open .dropdown-content {
        position: static;
        box-shadow: none;
        border: none;
        background: rgba(0,0,0,0.1);
        border-radius: 0;
        max-height: 300px;
    }
    .nav-menu.open .dropdown-content a {
        color: var(--nav-text);
        border-bottom-color: rgba(255,255,255,0.1);
        padding-left: 32px;
    }
    .hamburger { display: block; }
    .lang-selector { margin-left: 0; padding: 8px 14px; }
    .main-wrap { padding: 20px 16px 40px; }
    h1 { font-size: 1.5rem; }
    .nav-btn { padding: 10px 14px; font-size: 0.8rem; }
}
"""


# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------
SITE_JS = """
function switchLang(lang) {
    document.querySelectorAll('.lang-content').forEach(el => el.classList.remove('active'));
    var el = document.getElementById('content-' + lang);
    if (el) el.classList.add('active');
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.lang === lang) btn.classList.add('active');
    });
    localStorage.setItem('preferred-lang', lang);
}

// Restore language preference
(function() {
    var saved = localStorage.getItem('preferred-lang');
    if (saved && saved !== 'en') switchLang(saved);
})();

// Mobile menu toggle
function toggleMenu() {
    document.querySelector('.nav-menu').classList.toggle('open');
}

// Close menu when clicking outside
document.addEventListener('click', function(e) {
    var menu = document.querySelector('.nav-menu');
    var hamburger = document.querySelector('.hamburger');
    if (menu && hamburger && !menu.contains(e.target) && !hamburger.contains(e.target)) {
        menu.classList.remove('open');
    }
});
"""


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
def page_template(title, content, lang_contents, nav_menu, breadcrumb, prev_page, next_page):
    # Flag emojis for language selector
    lang_flags = {
        "en": "\U0001F1EC\U0001F1E7",  # GB flag
        "hk": "\U0001F1ED\U0001F1F0",  # HK flag
        "tw": "\U0001F1F9\U0001F1FC",  # TW flag
        "cn": "\U0001F1E8\U0001F1F3",  # CN flag
    }

    lang_selector = ""
    for lang, flag in lang_flags.items():
        active = " active" if lang == "en" else ""
        lang_selector += f'<button class="lang-btn{active}" data-lang="{lang}" onclick="switchLang(\'{lang}\')" title="{lang.upper()}">{flag}</button>'

    # Prev/next buttons
    prev_html = ""
    next_html = ""
    if prev_page:
        prev_html = f'''<a href="{prev_page['slug']}.html" class="nav-btn prev">
            <span style="font-size:1.2rem">&#8592;</span>
            <span class="nav-btn-text">
                <span class="btn-label">Previous</span>
                <span>{prev_page['nav_title']}</span>
            </span>
        </a>'''
    else:
        prev_html = '<span class="nav-placeholder"></span>'

    if next_page:
        next_html = f'''<a href="{next_page['slug']}.html" class="nav-btn next">
            <span class="nav-btn-text">
                <span class="btn-label">Next</span>
                <span>{next_page['nav_title']}</span>
            </span>
            <span style="font-size:1.2rem">&#8594;</span>
        </a>'''
    else:
        next_html = '<span class="nav-placeholder"></span>'

    # Build language content divs
    hk_content = lang_contents.get("hk", "<p><em>Translation coming soon...</em></p>")
    tw_content = lang_contents.get("tw", "<p><em>Translation coming soon...</em></p>")
    cn_content = lang_contents.get("cn", "<p><em>Translation coming soon...</em></p>")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Chanma Investment Tutorial</title>
    <style>{SITE_CSS}</style>
</head>
<body>
    <nav class="top-nav">
        <div class="nav-inner">
            <a href="index.html" class="nav-brand">
                <span class="brand-icon">&#9670;</span>
                Chanma Investment
            </a>
            <button class="hamburger" onclick="toggleMenu()">&#9776;</button>
            <div class="nav-menu">
                {nav_menu}
                <div class="lang-selector">
                    {lang_selector}
                </div>
            </div>
        </div>
    </nav>

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
        <p>Chanma Investment Tutorial &copy; 2025 &middot; <a href="disclaimer.html">Disclaimer</a> &middot; <a href="faq.html">FAQ</a> &middot; <a href="https://www.patreon.com/c/hevangel">Patreon</a></p>
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

    # Get all markdown files
    try:
        course_files = sorted(f for f in os.listdir(course_dir) if f.endswith(".md"))
    except OSError as e:
        print(f"Error reading course directory: {e}")
        return

    if not course_files:
        print("No markdown files found in course/. Nothing to build.")
        return

    print(f"Found {len(course_files)} markdown files in course/")

    # Build page list and navigation
    pages = build_page_list(course_files)
    nav_menu = build_nav_menu(pages)

    # Build each page
    for i, page in enumerate(pages):
        source_file = page["file"]
        source_path = os.path.join(course_dir, source_file)

        if not os.path.exists(source_path):
            print(f"  Skipping {source_file} (not found)")
            continue

        md_content = open(source_path, "r", encoding="utf-8").read()

        # Strip YouTube scripts from web output
        article_content = strip_youtube_section(md_content)
        html_content = markdown_to_html(article_content)

        # Load translations (also strip YouTube scripts)
        lang_contents = {}
        for lang, lang_dir in [("hk", hk_dir), ("tw", tw_dir), ("cn", cn_dir)]:
            lang_path = os.path.join(lang_dir, source_file)
            if os.path.exists(lang_path):
                lang_md = open(lang_path, "r", encoding="utf-8").read()
                lang_article = strip_youtube_section(lang_md)
                lang_contents[lang] = markdown_to_html(lang_article)

        # Build breadcrumb
        breadcrumb = build_breadcrumb(page, pages)

        # Prev/next navigation
        prev_page = pages[i - 1] if i > 0 else None
        next_page = pages[i + 1] if i < len(pages) - 1 else None

        # Use page title (but strip week/side number from h1 since breadcrumb has it)
        title = extract_title(article_content)

        # Generate HTML
        html = page_template(
            title, html_content, lang_contents, nav_menu, breadcrumb,
            prev_page, next_page
        )

        out_name = f"{page['slug']}.html"
        out_path = os.path.join(docs_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"  Built: {out_name}")

    print(f"\nDone! Built {len(pages)} pages in docs/")


if __name__ == "__main__":
    build()
