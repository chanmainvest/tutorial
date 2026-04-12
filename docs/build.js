#!/usr/bin/env node
/**
 * Static Site Generator for Investment Tutorial Course
 *
 * Reads markdown files from course/, course_hk/, course_tw/, course_cn/
 * and generates a static website in docs/ with language toggle.
 *
 * Usage: node docs/build.js
 *
 * Dependencies: npm install marked (or use the bundled simple markdown parser)
 */

const fs = require('fs');
const path = require('path');

// Simple markdown to HTML converter (no dependencies needed)
function markdownToHtml(md) {
    let html = md;

    // Escape HTML entities first (but preserve markdown)
    // We'll handle this more carefully

    // Code blocks (fenced)
    html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (match, lang, code) => {
        const escaped = code.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return `<pre><code class="language-${lang}">${escaped}</code></pre>`;
    });

    // Inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Headers
    html = html.replace(/^######\s+(.+)$/gm, '<h6>$1</h6>');
    html = html.replace(/^#####\s+(.+)$/gm, '<h5>$1</h5>');
    html = html.replace(/^####\s+(.+)$/gm, '<h4>$1</h4>');
    html = html.replace(/^###\s+(.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^##\s+(.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^#\s+(.+)$/gm, '<h1>$1</h1>');

    // Bold and italic
    html = html.replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>');
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

    // Images
    html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1">');

    // Horizontal rules
    html = html.replace(/^---$/gm, '<hr>');

    // Tables
    html = html.replace(/^(\|.+\|)\n(\|[-:\s|]+\|)\n((?:\|.+\|\n?)+)/gm, (match, header, separator, body) => {
        const headerCells = header.split('|').filter(c => c.trim()).map(c => `<th>${c.trim()}</th>`).join('');
        const rows = body.trim().split('\n').map(row => {
            const cells = row.split('|').filter(c => c.trim()).map(c => `<td>${c.trim()}</td>`).join('');
            return `<tr>${cells}</tr>`;
        }).join('\n');
        return `<table><thead><tr>${headerCells}</tr></thead><tbody>${rows}</tbody></table>`;
    });

    // Blockquotes
    html = html.replace(/^>\s+(.+)$/gm, '<blockquote>$1</blockquote>');

    // Unordered lists
    html = html.replace(/^[\s]*[-*]\s+(.+)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>');

    // Ordered lists
    html = html.replace(/^\d+\.\s+(.+)$/gm, '<li>$1</li>');

    // Paragraphs (lines not already wrapped in tags)
    const lines = html.split('\n');
    const result = [];
    let inParagraph = false;

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        const isTag = /^<(h[1-6]|ul|ol|li|table|thead|tbody|tr|th|td|pre|code|blockquote|hr|div|img)/.test(line);
        const isEmpty = line === '';

        if (isEmpty) {
            if (inParagraph) {
                result.push('</p>');
                inParagraph = false;
            }
            continue;
        }

        if (isTag) {
            if (inParagraph) {
                result.push('</p>');
                inParagraph = false;
            }
            result.push(line);
        } else {
            if (!inParagraph) {
                result.push('<p>');
                inParagraph = true;
            }
            result.push(line);
        }
    }
    if (inParagraph) result.push('</p>');

    return result.join('\n');
}

// HTML template for each page
function pageTemplate(title, content, langContents, nav, isIndex = false) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - Investment Tutorial</title>
    <style>
        :root {
            --bg: #ffffff;
            --text: #1a1a2e;
            --heading: #16213e;
            --accent: #0f3460;
            --accent-light: #e8eef7;
            --border: #d4d4d8;
            --code-bg: #f4f4f5;
            --sidebar-bg: #f8f9fa;
            --link: #0f3460;
            --success: #059669;
            --warning: #d97706;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.7;
            color: var(--text);
            background: var(--bg);
        }

        .layout {
            display: flex;
            min-height: 100vh;
        }

        .sidebar {
            width: 280px;
            background: var(--sidebar-bg);
            border-right: 1px solid var(--border);
            padding: 20px;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            z-index: 10;
        }

        .sidebar h2 {
            font-size: 1.1rem;
            color: var(--accent);
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--accent);
        }

        .sidebar .nav-section {
            margin-bottom: 15px;
        }

        .sidebar .nav-section h3 {
            font-size: 0.85rem;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 5px;
        }

        .sidebar a {
            display: block;
            padding: 4px 8px;
            color: var(--text);
            text-decoration: none;
            font-size: 0.85rem;
            border-radius: 4px;
            margin-bottom: 2px;
        }

        .sidebar a:hover, .sidebar a.active {
            background: var(--accent-light);
            color: var(--accent);
        }

        .main-content {
            flex: 1;
            margin-left: 280px;
            padding: 30px 50px;
            max-width: 900px;
        }

        .top-bar {
            position: fixed;
            top: 0;
            left: 280px;
            right: 0;
            background: white;
            border-bottom: 1px solid var(--border);
            padding: 10px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 5;
        }

        .lang-toggle {
            display: flex;
            gap: 5px;
        }

        .lang-toggle button {
            padding: 5px 12px;
            border: 1px solid var(--border);
            border-radius: 4px;
            background: white;
            cursor: pointer;
            font-size: 0.85rem;
            transition: all 0.2s;
        }

        .lang-toggle button:hover {
            border-color: var(--accent);
            color: var(--accent);
        }

        .lang-toggle button.active {
            background: var(--accent);
            color: white;
            border-color: var(--accent);
        }

        .content-area {
            margin-top: 60px;
        }

        .lang-content { display: none; }
        .lang-content.active { display: block; }

        h1 { font-size: 2rem; color: var(--heading); margin: 30px 0 15px; border-bottom: 2px solid var(--accent); padding-bottom: 10px; }
        h2 { font-size: 1.5rem; color: var(--heading); margin: 25px 0 12px; }
        h3 { font-size: 1.2rem; color: var(--heading); margin: 20px 0 10px; }
        h4 { font-size: 1.05rem; color: var(--heading); margin: 15px 0 8px; }

        p { margin-bottom: 12px; }

        ul, ol { margin: 10px 0 15px 25px; }
        li { margin-bottom: 5px; }

        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th, td { padding: 8px 12px; border: 1px solid var(--border); text-align: left; }
        th { background: var(--accent-light); font-weight: 600; }

        pre { background: var(--code-bg); padding: 15px; border-radius: 6px; overflow-x: auto; margin: 15px 0; }
        code { font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.9em; }
        p code { background: var(--code-bg); padding: 2px 6px; border-radius: 3px; }

        blockquote { border-left: 4px solid var(--accent); padding: 10px 20px; margin: 15px 0; background: var(--accent-light); }

        hr { border: none; border-top: 1px solid var(--border); margin: 30px 0; }

        a { color: var(--link); }

        img { max-width: 100%; height: auto; border-radius: 6px; margin: 10px 0; }

        .nav-buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid var(--border);
        }

        .nav-buttons a {
            padding: 8px 16px;
            background: var(--accent-light);
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.9rem;
        }

        .nav-buttons a:hover {
            background: var(--accent);
            color: white;
        }

        .hamburger {
            display: none;
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 20;
            background: var(--accent);
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1.2rem;
        }

        @media (max-width: 768px) {
            .sidebar { transform: translateX(-100%); transition: transform 0.3s; }
            .sidebar.open { transform: translateX(0); }
            .main-content { margin-left: 0; padding: 20px; }
            .top-bar { left: 0; padding: 10px 20px; }
            .content-area { margin-top: 50px; }
            .hamburger { display: block; }
        }
    </style>
</head>
<body>
    <button class="hamburger" onclick="document.querySelector('.sidebar').classList.toggle('open')">&#9776;</button>

    <div class="layout">
        <nav class="sidebar">
            <h2>Investment Tutorial</h2>
            ${nav}
        </nav>

        <main class="main-content">
            <div class="top-bar">
                <span style="font-weight:600;color:var(--accent);">${title}</span>
                <div class="lang-toggle">
                    <button class="active" onclick="switchLang('en')">EN</button>
                    <button onclick="switchLang('hk')">HK</button>
                    <button onclick="switchLang('tw')">TW</button>
                    <button onclick="switchLang('cn')">CN</button>
                </div>
            </div>

            <div class="content-area">
                <div id="content-en" class="lang-content active">
                    ${content}
                </div>
                <div id="content-hk" class="lang-content">
                    ${langContents.hk || '<p><em>Translation coming soon...</em></p>'}
                </div>
                <div id="content-tw" class="lang-content">
                    ${langContents.tw || '<p><em>Translation coming soon...</em></p>'}
                </div>
                <div id="content-cn" class="lang-content">
                    ${langContents.cn || '<p><em>Translation coming soon...</em></p>'}
                </div>
            </div>
        </main>
    </div>

    <script>
        function switchLang(lang) {
            document.querySelectorAll('.lang-content').forEach(el => el.classList.remove('active'));
            document.getElementById('content-' + lang).classList.add('active');
            document.querySelectorAll('.lang-toggle button').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            localStorage.setItem('preferred-lang', lang);
        }

        // Restore language preference
        const savedLang = localStorage.getItem('preferred-lang');
        if (savedLang && savedLang !== 'en') {
            switchLang(savedLang);
            document.querySelectorAll('.lang-toggle button').forEach(btn => {
                btn.classList.remove('active');
                if (btn.textContent.toLowerCase() === savedLang) btn.classList.add('active');
            });
        }
    </script>
</body>
</html>`;
}

// Build navigation HTML
function buildNav(files) {
    const levels = [
        { name: 'Level 1: Foundation', range: [1, 12] },
        { name: 'Level 2: Intermediate', range: [13, 24] },
        { name: 'Level 3: Advanced', range: [25, 36] },
        { name: 'Level 4: Sophisticated', range: [37, 46] },
        { name: 'Level 5: Expert', range: [47, 52] },
    ];

    let nav = '<div class="nav-section"><h3>Home</h3><a href="index.html">Course Overview</a></div>';

    for (const level of levels) {
        nav += `<div class="nav-section"><h3>${level.name}</h3>`;
        for (let i = level.range[0]; i <= level.range[1]; i++) {
            const weekNum = String(i).padStart(2, '0');
            const file = files.find(f => f.startsWith(`week${weekNum}_`));
            if (file) {
                const title = file.replace(/^week\d+_/, '').replace('.md', '').replace(/_/g, ' ');
                const capitalTitle = title.charAt(0).toUpperCase() + title.slice(1);
                nav += `<a href="week${weekNum}.html">Week ${i}: ${capitalTitle}</a>`;
            }
        }
        nav += '</div>';
    }

    // Side lessons
    nav += '<div class="nav-section"><h3>Side Lessons</h3>';
    const sideFiles = files.filter(f => f.startsWith('side'));
    for (const file of sideFiles) {
        const match = file.match(/side(\d+)_(.+)\.md/);
        if (match) {
            const num = parseInt(match[1]);
            const title = match[2].replace(/_/g, ' ');
            const capitalTitle = title.charAt(0).toUpperCase() + title.slice(1);
            nav += `<a href="side${match[1]}.html">Side ${num}: ${capitalTitle}</a>`;
        }
    }
    nav += '</div>';

    return nav;
}

// Main build function
function build() {
    const rootDir = path.resolve(__dirname, '..');
    const courseDir = path.join(rootDir, 'course');
    const hkDir = path.join(rootDir, 'course_hk');
    const twDir = path.join(rootDir, 'course_tw');
    const cnDir = path.join(rootDir, 'course_cn');
    const docsDir = __dirname;

    // Get all markdown files
    let files = [];
    try {
        files = fs.readdirSync(courseDir).filter(f => f.endsWith('.md')).sort();
    } catch (e) {
        console.error('Error reading course directory:', e.message);
        return;
    }

    if (files.length === 0) {
        console.log('No markdown files found in course/. Nothing to build.');
        return;
    }

    console.log(`Found ${files.length} markdown files in course/`);

    const nav = buildNav(files);

    // Build index page
    let readmePath = path.join(rootDir, 'README.md');
    let readmeContent = '<h1>Investment Tutorial</h1><p>Welcome to the course.</p>';
    if (fs.existsSync(readmePath)) {
        readmeContent = markdownToHtml(fs.readFileSync(readmePath, 'utf8'));
    }

    const indexHtml = pageTemplate('Home', readmeContent, {}, nav, true);
    fs.writeFileSync(path.join(docsDir, 'index.html'), indexHtml);
    console.log('Built: index.html');

    // Build each lesson page
    for (const file of files) {
        const mdContent = fs.readFileSync(path.join(courseDir, file), 'utf8');
        const htmlContent = markdownToHtml(mdContent);

        // Try to load translations
        const langContents = {};
        for (const [lang, dir] of [['hk', hkDir], ['tw', twDir], ['cn', cnDir]]) {
            const langFile = path.join(dir, file);
            if (fs.existsSync(langFile)) {
                langContents[lang] = markdownToHtml(fs.readFileSync(langFile, 'utf8'));
            }
        }

        // Extract title from first # heading
        const titleMatch = mdContent.match(/^#\s+(.+)$/m);
        const title = titleMatch ? titleMatch[1] : file.replace('.md', '');

        // Determine output filename
        let outName;
        const weekMatch = file.match(/week(\d+)/);
        const sideMatch = file.match(/side(\d+)/);
        if (weekMatch) {
            outName = `week${weekMatch[1]}.html`;
        } else if (sideMatch) {
            outName = `side${sideMatch[1]}.html`;
        } else {
            outName = file.replace('.md', '.html');
        }

        const html = pageTemplate(title, htmlContent, langContents, nav);
        fs.writeFileSync(path.join(docsDir, outName), html);
        console.log(`Built: ${outName}`);
    }

    console.log(`\nDone! Built ${files.length + 1} pages in docs/`);
}

build();
