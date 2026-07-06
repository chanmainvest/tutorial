/* On-device AI tutor for Chanma Investment Tutorial.
 *
 * Loads Gemma in the browser via transformers.js v4 + WebGPU. The model
 * weights are fetched from Hugging Face on first use and cached in
 * IndexedDB by the library — subsequent visits skip the download.
 *
 * Page-context strategy: at send-time, read .innerText of
 * .lang-content.active and stuff the first ~12 K characters into the
 * system prompt. This means the assistant always answers about whatever
 * lesson and language the user is currently looking at.
 *
 * No data leaves the browser.
 */

const MODEL_OPTIONS = {
    "gemma-4-e2b": {
        id: "onnx-community/gemma-4-E2B-it-ONNX",
        size_mb: 3100,
        label: "Gemma 4 E2B (≈ 3.1 GB)",
    },
    // Fallback — Gemma 3 1B (smaller download, simpler text-only):
    // "gemma-3-1b": { id: "onnx-community/gemma-3-1b-it-ONNX", size_mb: 600, label: "Gemma 3 1B (≈ 600 MB)" },
};

const ACTIVE_MODEL = "gemma-4-e2b";
const MAX_CONTEXT_CHARS = 6000;       // current-page slice in the system prompt
const MAX_HISTORY_TURNS = 6;
const MAX_NEW_TOKENS = 512;

const CDN_URL = "https://cdn.jsdelivr.net/npm/@huggingface/transformers@4/+esm";

// ----- Cross-lesson RAG ---------------------------------------------------
// A small multilingual embedding model + a static JSON of every lesson's
// reading section, chunked at build time by scripts/build_chatbot_index.py.
// Embeddings are computed on-device the first time a given language is
// used and cached in IndexedDB. At query time we cosine-sim the user's
// question against the cached embeddings and inject the top-K chunks
// into the system prompt alongside the current page text.
const EMBED_MODEL_ID = "onnx-community/embeddinggemma-300m-ONNX";
const CHUNKS_URL = "assets/chatbot_chunks.json";
const TOP_K = 5;
const RAG_DB_NAME = "chanma-chatbot-rag";
const RAG_STORE = "embeddings";
const RAG_DB_VERSION = 2;

// Prebuilt embedding cache (shipped as a static binary so users get instant
// cross-lesson search instead of a 30s+ in-browser indexing step). Produced
// by scripts/build_chatbot_embeddings.mjs. See .claude/docs/chatbot-architecture.md
// for the format. The browser still downloads the embedding model at runtime
// to embed user queries (dynamic, can't be precomputed), but skips the slow
// per-chunk indexing because the vectors are already in the bin.
const EMBEDDINGS_BIN_URL = "assets/chatbot_embeddings.bin";
const EMBED_BIN_MAGIC = 0x42454d43;   // "CMEB" read as little-endian u32
const EMBED_BIN_VERSION = 1;
const EMBED_BIN_DTYPE_F32 = 1;
const EMBED_BIN_LANGS = ["en", "hk", "tw", "cn"]; // canonical order in the bin

const I18N = {
    en: {
        title: "Ask the AI tutor",
        subtitle: "Runs on your device — no data leaves your browser.",
        intro_h: "Lesson assistant",
        intro_p: "Ask any question about this lesson. The assistant runs a small Gemma model entirely inside your browser using WebGPU. Your questions never leave your device.",
        notes: [
            "First load downloads the model (≈ 3.1 GB) and caches it. Subsequent visits are instant.",
            "Best on a recent desktop browser. Mobile and low-RAM machines may run out of memory.",
            "The assistant reads the lesson currently shown — switch language to ask in 中文.",
        ],
        load_btn: "Load assistant (≈ 3.1 GB)",
        loading: "Loading model…",
        no_webgpu: "Your browser does not support WebGPU. Try the latest Chrome, Edge, Firefox, or Safari on a desktop.",
        unsupported_title: "On-device AI not available",
        ready: "Ready. Ask anything about this lesson.",
        thinking: "Thinking…",
        send: "Send",
        clear: "Clear conversation",
        close: "Close",
        placeholder: "Ask about this lesson…",
        load_failed: "Could not load the model: ",
        gen_failed: "Generation failed: ",
        no_lesson: "(no lesson text found on this page)",
        retrieved_header: "RELEVANT EXCERPTS FROM OTHER LESSONS",
        current_page_header: "CURRENT LESSON (priority — answer using this first)",
        index_section_label: "Pre-index for cross-lesson search",
        index_section_help: "Without an index, the assistant answers from the current page only. The index is prebuilt — it downloads once (~18 MB) and is cached for future visits.",
        chip_ready: "Cross-lesson search on",
        chip_indexing: "Indexing",
        chip_none: "Index this language",
        chip_error: "Index failed — retry",
        chip_ready_title: "The assistant can pull excerpts from any lesson in this language.",
        chip_index_title: "Click to build the cross-lesson search index for this language (one-time per browser).",
        chip_retry_title: "Click to retry building the index.",
        lang_en_full: "English",
        lang_hk_full: "Hong Kong Chinese",
        lang_tw_full: "Taiwan Chinese",
        lang_cn_full: "Mainland Chinese",
        mermaid_chart: "Chart",
        mermaid_source: "Source",
        mermaid_toggle_label: "Toggle Mermaid chart display",
        mermaid_selected_line: "Line {line}",
        mermaid_selected_lines: "Lines {start}-{end}",
    },
    hk: {
        title: "請教 AI 導師",
        subtitle: "完全在你裝置上運行,資料不會離開瀏覽器。",
        intro_h: "課程助手",
        intro_p: "你可以就本堂課問任何問題。助手使用 WebGPU 在你的瀏覽器內運行小型 Gemma 模型,所有對話不會離開你的裝置。",
        notes: [
            "首次載入會下載模型(約 3.1 GB)並儲存於瀏覽器。下次再用即時開啟。",
            "桌面瀏覽器體驗最佳;手機或記憶體較少的電腦可能會失敗。",
            "助手只會讀取你目前看到的課程內容 — 切換語言即可用中文發問。",
        ],
        load_btn: "載入助手(約 3.1 GB)",
        loading: "正在載入模型……",
        no_webgpu: "你的瀏覽器不支援 WebGPU。請使用最新版桌面 Chrome、Edge、Firefox 或 Safari。",
        unsupported_title: "本機 AI 暫時不能使用",
        ready: "準備就緒。請就本課發問。",
        thinking: "思考中……",
        send: "發送",
        clear: "清除對話",
        close: "關閉",
        placeholder: "就本課提問……",
        load_failed: "模型載入失敗: ",
        gen_failed: "生成失敗: ",
        no_lesson: "(本頁找不到課程內容)",
        retrieved_header: "其他課程相關摘錄",
        current_page_header: "目前課程(優先 — 請先用這部分回答)",
        index_section_label: "預先建立跨課程搜尋索引",
        index_section_help: "未建立索引時,助手只會看當前頁面。索引為預先建立——下載一次(約 18 MB)後即快取供日後使用。",
        chip_ready: "跨課搜尋已啟用",
        chip_indexing: "建立索引中",
        chip_none: "為此語言建立索引",
        chip_error: "建立索引失敗 — 點擊重試",
        chip_ready_title: "助手可以從本語言的任何課程取出相關摘錄。",
        chip_index_title: "點擊以為此語言建立跨課程搜尋索引(每個瀏覽器只需一次)。",
        chip_retry_title: "點擊重試建立索引。",
        lang_en_full: "英文",
        lang_hk_full: "中文(香港)",
        lang_tw_full: "中文(台灣)",
        lang_cn_full: "中文(大陸)",
        mermaid_chart: "圖表",
        mermaid_source: "原始碼",
        mermaid_toggle_label: "切換 Mermaid 圖表顯示方式",
        mermaid_selected_line: "第 {line} 行",
        mermaid_selected_lines: "第 {start} 至 {end} 行",
    },
    tw: {
        title: "請教 AI 老師",
        subtitle: "完全在您裝置上執行,資料不會離開瀏覽器。",
        intro_h: "課程助理",
        intro_p: "您可以針對本單元提出任何問題。助理使用 WebGPU 於您的瀏覽器內執行小型 Gemma 模型,對話不會離開您的裝置。",
        notes: [
            "首次載入會下載模型(約 3.1 GB)並儲存於瀏覽器,之後開啟即可立即使用。",
            "建議使用桌面瀏覽器;行動裝置或記憶體較少的電腦可能會失敗。",
            "助理只會讀取您目前顯示的課程 — 切換語言即可用中文提問。",
        ],
        load_btn: "載入助理(約 3.1 GB)",
        loading: "正在載入模型……",
        no_webgpu: "您的瀏覽器不支援 WebGPU。請使用最新版桌面 Chrome、Edge、Firefox 或 Safari。",
        unsupported_title: "本機 AI 目前無法使用",
        ready: "準備就緒。請就本單元提問。",
        thinking: "思考中……",
        send: "傳送",
        clear: "清除對話",
        close: "關閉",
        placeholder: "就本單元提問……",
        load_failed: "模型載入失敗: ",
        gen_failed: "生成失敗: ",
        no_lesson: "(本頁找不到課程內容)",
        retrieved_header: "其他單元相關摘錄",
        current_page_header: "目前單元(優先 — 請先用這部分回答)",
        index_section_label: "預先建立跨單元搜尋索引",
        index_section_help: "未建立索引時,助理只會看目前頁面。索引為預先建立——下載一次(約 18 MB)後即快取供日後使用。",
        chip_ready: "跨單元搜尋已啟用",
        chip_indexing: "建立索引中",
        chip_none: "為此語言建立索引",
        chip_error: "建立索引失敗 — 點擊重試",
        chip_ready_title: "助理可以從本語言的任何單元取出相關摘錄。",
        chip_index_title: "點擊以為此語言建立跨單元搜尋索引(每個瀏覽器只需一次)。",
        chip_retry_title: "點擊重試建立索引。",
        lang_en_full: "英文",
        lang_hk_full: "中文(香港)",
        lang_tw_full: "中文(台灣)",
        lang_cn_full: "中文(大陸)",
        mermaid_chart: "圖表",
        mermaid_source: "原始碼",
        mermaid_toggle_label: "切換 Mermaid 圖表顯示方式",
        mermaid_selected_line: "第 {line} 行",
        mermaid_selected_lines: "第 {start} 至 {end} 行",
    },
    cn: {
        title: "向 AI 老师提问",
        subtitle: "完全在您设备上运行,数据不会离开浏览器。",
        intro_h: "课程助手",
        intro_p: "您可以就本课提出任何问题。助手通过 WebGPU 在您的浏览器中运行小型 Gemma 模型,所有对话不会离开您的设备。",
        notes: [
            "首次加载会下载模型(约 3.1 GB)并缓存,后续打开即开即用。",
            "建议使用桌面浏览器;手机或内存较少的电脑可能会失败。",
            "助手只读取您目前显示的课程 — 切换语言即可用中文提问。",
        ],
        load_btn: "加载助手(约 3.1 GB)",
        loading: "正在加载模型……",
        no_webgpu: "您的浏览器不支持 WebGPU。请使用最新版桌面 Chrome、Edge、Firefox 或 Safari。",
        unsupported_title: "本地 AI 暂不可用",
        ready: "准备就绪。请就本课提问。",
        thinking: "思考中……",
        send: "发送",
        clear: "清除对话",
        close: "关闭",
        placeholder: "就本课提问……",
        load_failed: "模型加载失败: ",
        gen_failed: "生成失败: ",
        no_lesson: "(本页找不到课程内容)",
        retrieved_header: "其他课程相关摘录",
        current_page_header: "当前课程(优先 — 请先用这部分回答)",
        index_section_label: "预先建立跨课程搜索索引",
        index_section_help: "未建立索引时,助手只会看当前页面。索引为预先建立——下载一次(约 18 MB)后即缓存供日后使用。",
        chip_ready: "跨课程搜索已启用",
        chip_indexing: "建立索引中",
        chip_none: "为此语言建立索引",
        chip_error: "建立索引失败 — 点击重试",
        chip_ready_title: "助手可以从本语言的任何课程取出相关摘录。",
        chip_index_title: "点击为此语言建立跨课程搜索索引(每个浏览器只需一次)。",
        chip_retry_title: "点击重试建立索引。",
        lang_en_full: "英文",
        lang_hk_full: "中文(香港)",
        lang_tw_full: "中文(台湾)",
        lang_cn_full: "中文(大陆)",
        mermaid_chart: "图表",
        mermaid_source: "源码",
        mermaid_toggle_label: "切换 Mermaid 图表显示方式",
        mermaid_selected_line: "第 {line} 行",
        mermaid_selected_lines: "第 {start} 至 {end} 行",
    },
};

function currentLocale() {
    const html = document.documentElement.getAttribute("lang") || "en";
    if (html.startsWith("zh-HK")) return "hk";
    if (html.startsWith("zh-TW")) return "tw";
    if (html.startsWith("zh-CN")) return "cn";
    const active = document.querySelector(".lang-content.active");
    if (active && active.id) {
        const m = active.id.match(/^content-(en|hk|tw|cn)$/);
        if (m) return m[1];
    }
    return "en";
}

function t(key) {
    const loc = currentLocale();
    return (I18N[loc] && I18N[loc][key]) || I18N.en[key] || key;
}

function tf(key, vars = {}) {
    const template = t(key);
    if (typeof template !== "string") return template;
    return template.replace(/\{(\w+)\}/g, (_, name) => (
        vars[name] == null ? `{${name}}` : String(vars[name])
    ));
}

// ----- Page-context extraction --------------------------------------------
function getActiveLessonText() {
    const active = document.querySelector(".lang-content.active");
    if (!active) return "";
    let text = active.innerText || "";
    text = text.replace(/\s+\n/g, "\n").replace(/\n{3,}/g, "\n\n").trim();
    if (text.length > MAX_CONTEXT_CHARS) {
        text = text.slice(0, MAX_CONTEXT_CHARS) + "\n…(truncated)";
    }
    return text;
}

async function buildSystemPrompt(userQuestion) {
    const lessonText = getActiveLessonText() || t("no_lesson");
    let retrieved = [];
    if (userQuestion) {
        retrieved = await retrieveContext(userQuestion);
    }
    const blocks = [
        "You are an investing tutor for the Chanma Investment Tutorial.",
        "Answer the user's question using ONLY the course material provided below.",
        "Prefer the CURRENT LESSON section. Use the RELEVANT EXCERPTS only when",
        "the current lesson does not cover the question, and cite the lesson",
        "title in brackets when you draw on an excerpt (e.g. \"[Week 5: Bonds] …\").",
        "If neither section covers the question, say so honestly rather than guessing.",
        "Reply in the same language the user uses. Keep answers concise (~200 words)",
        "unless the user explicitly asks for more detail.",
        "",
        t("current_page_header") + ":",
        lessonText,
    ];
    if (retrieved.length) {
        blocks.push("");
        blocks.push(t("retrieved_header") + ":");
        for (const { chunk } of retrieved) {
            blocks.push(`[${chunk.title}] ${chunk.text}`);
        }
    }
    return blocks.join("\n");
}

// ----- DOM scaffolding ----------------------------------------------------
function el(tag, attrs = {}, ...children) {
    const node = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
        if (k === "class") node.className = v;
        else if (k === "html") node.innerHTML = v;
        else if (k.startsWith("on") && typeof v === "function") node.addEventListener(k.slice(2), v);
        else node.setAttribute(k, v);
    }
    for (const c of children) {
        if (c == null) continue;
        node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    }
    return node;
}

function escapeHtml(text) {
    return String(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function escapeAttr(text) {
    return escapeHtml(text).replace(/\n/g, "&#10;");
}

function normaliseBlockText(text) {
    return String(text).replace(/\r\n?/g, "\n");
}

function applyInlineMarkdown(text, citeIdx) {
    let html = escapeHtml(text);
    html = html.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (match, label, url) => (
        `<a href="${escapeAttr(url)}" target="_blank" rel="noreferrer noopener">${label}</a>`
    ));
    // Linkify bare-bracket lesson citations the tutor emits, e.g.
    // "[Week 5: Bonds - Your Portfolio's Shock Absorber]" or the
    // abbreviated "[Week 5: Bonds]". Only brackets that start with a
    // Week/Side/Level citation and are NOT followed by "(" (those were
    // already handled as markdown links above). Non-matching brackets
    // are left untouched.
    if (citeIdx) {
        html = html.replace(
            /\[(Week|Side(?:\s+Lesson)?|Level)\s+\d+:[^\]]*\](?!\()/gi,
            (match) => {
                // match still contains escaped entities (e.g. &#39;); decode
                // the common ones so linkifyCitation sees real text.
                const label = match.slice(1, -1)
                    .replace(/&#39;/g, "'").replace(/&quot;/g, '"')
                    .replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">");
                const url = linkifyCitation(label, citeIdx);
                if (!url) return match;
                const safe = escapeHtml(label); // re-escape for display
                return `<a href="${escapeAttr(url)}" target="_blank" rel="noreferrer noopener" class="chat-citation">${safe}</a>`;
            }
        );
    }
    html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
    html = html.replace(/\*\*\*([^*]+?)\*\*\*/g, "<strong><em>$1</em></strong>");
    html = html.replace(/\*\*([^*]+?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/(^|[^\*])\*([^*\n]+?)\*(?!\*)/g, "$1<em>$2</em>");
    return html;
}

function renderMarkdownChunk(markdown, citeIdx) {
    const lines = normaliseBlockText(markdown).split("\n");
    const html = [];
    let paragraph = [];
    let listItems = [];
    let listType = null;
    let quoteLines = [];

    const inline = (t) => applyInlineMarkdown(t, citeIdx);

    function flushParagraph() {
        if (!paragraph.length) return;
        html.push(`<p>${paragraph.map(inline).join("<br>")}</p>`);
        paragraph = [];
    }

    function flushList() {
        if (!listItems.length) return;
        const tag = listType === "ol" ? "ol" : "ul";
        html.push(`<${tag}>${listItems.join("")}</${tag}>`);
        listItems = [];
        listType = null;
    }

    function flushQuotes() {
        if (!quoteLines.length) return;
        html.push(`<blockquote>${quoteLines.map(inline).join("<br>")}</blockquote>`);
        quoteLines = [];
    }

    for (const rawLine of lines) {
        const line = rawLine.trimEnd();
        const trimmed = line.trim();
        const heading = trimmed.match(/^(#{1,6})\s+(.+)$/);
        const bullet = trimmed.match(/^[-*]\s+(.+)$/);
        const ordered = trimmed.match(/^\d+\.\s+(.+)$/);
        const quote = trimmed.match(/^>\s+(.+)$/);

        if (!trimmed) {
            flushParagraph();
            flushList();
            flushQuotes();
            continue;
        }

        if (heading) {
            flushParagraph();
            flushList();
            flushQuotes();
            const level = heading[1].length;
            html.push(`<h${level}>${inline(heading[2])}</h${level}>`);
            continue;
        }

        if (/^---+$/.test(trimmed)) {
            flushParagraph();
            flushList();
            flushQuotes();
            html.push("<hr>");
            continue;
        }

        if (quote) {
            flushParagraph();
            flushList();
            quoteLines.push(quote[1]);
            continue;
        }

        flushQuotes();

        if (bullet || ordered) {
            flushParagraph();
            const nextType = ordered ? "ol" : "ul";
            if (listType && listType !== nextType) flushList();
            listType = nextType;
            listItems.push(`<li>${inline((ordered || bullet)[1])}</li>`);
            continue;
        }

        flushList();
        paragraph.push(trimmed);
    }

    flushParagraph();
    flushList();
    flushQuotes();

    return html.join("\n");
}

function splitMarkdownBlocks(markdown) {
    const input = normaliseBlockText(markdown);
    const blocks = [];
    const fence = /```([\w-]*)\n([\s\S]*?)```/g;
    let cursor = 0;

    for (let match = fence.exec(input); match; match = fence.exec(input)) {
        if (match.index > cursor) {
            blocks.push({ type: "markdown", content: input.slice(cursor, match.index) });
        }
        blocks.push({
            type: "code",
            lang: (match[1] || "").toLowerCase(),
            content: match[2],
        });
        cursor = match.index + match[0].length;
    }

    if (cursor < input.length) {
        blocks.push({ type: "markdown", content: input.slice(cursor) });
    }

    return blocks;
}

function getMermaidSourceLines(source) {
    const lines = normaliseBlockText(source).split("\n");
    if (lines.length > 1 && lines[lines.length - 1] === "") lines.pop();
    return lines;
}

function buildMermaidSourceMarkup(source) {
    return getMermaidSourceLines(source).map((line, index) => {
        const rendered = line.length ? escapeHtml(line) : "&nbsp;";
        return `<span class="chat-mermaid-source-line" data-line-number="${index + 1}">${rendered}</span>`;
    }).join("");
}

function buildMermaidBlock(source) {
    const chartLabel = escapeHtml(t("mermaid_chart"));
    const sourceLabel = escapeHtml(t("mermaid_source"));
    return [
        `<div class="chat-mermaid-block" data-view="diagram">`,
        `<div class="chat-mermaid-toolbar">`,
        `<div class="chat-mermaid-toggle" role="tablist" aria-label="${escapeAttr(t("mermaid_toggle_label"))}">`,
        `<button type="button" class="active" data-view-target="diagram" aria-pressed="true">${chartLabel}</button>`,
        `<button type="button" data-view-target="source" aria-pressed="false">${sourceLabel}</button>`,
        `</div>`,
        `<span class="chat-mermaid-selection-status" aria-live="polite"></span>`,
        `</div>`,
        `<pre class="chat-mermaid-diagram mermaid" tabindex="0">${escapeHtml(normaliseBlockText(source))}</pre>`,
        `<pre class="chat-mermaid-source" tabindex="0"><code>${buildMermaidSourceMarkup(source)}</code></pre>`,
        `<textarea class="chat-mermaid-selection-proxy" aria-hidden="true" tabindex="-1" readonly>${escapeHtml(normaliseBlockText(source))}</textarea>`,
        `</div>`,
    ].join("");
}

function renderCodeBlock(lang, code) {
    if (lang === "mermaid") return buildMermaidBlock(code);
    const languageClass = lang ? ` class="language-${escapeAttr(lang)}"` : "";
    return `<pre class="chat-code-block"><code${languageClass}>${escapeHtml(normaliseBlockText(code))}</code></pre>`;
}

async function renderMarkdown(text) {
    // Build the lesson-citation index once (cached) so applyInlineMarkdown
    // can linkify "[Week 5: Bonds]"-style references in-place.
    const citeIdx = await getLessonUrlIndex().catch(() => null);
    return splitMarkdownBlocks(text).map((block) => {
        if (block.type === "code") return renderCodeBlock(block.lang, block.content);
        return renderMarkdownChunk(block.content, citeIdx);
    }).join("\n");
}

function setMermaidSelectionStatus(block, message) {
    const status = block.querySelector(".chat-mermaid-selection-status");
    if (!status) return;
    status.textContent = message || "";
    status.classList.toggle("has-selection", Boolean(message));
}

function formatMermaidSelection(startLine, endLine) {
    if (!startLine || !endLine) return "";
    if (startLine === endLine) return tf("mermaid_selected_line", { line: startLine });
    return tf("mermaid_selected_lines", { start: startLine, end: endLine });
}

function setMermaidView(block, view) {
    block.setAttribute("data-view", view);
    block.querySelectorAll(".chat-mermaid-toggle button").forEach((button) => {
        const active = button.dataset.viewTarget === view;
        button.classList.toggle("active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    if (view !== "source") setMermaidSelectionStatus(block, "");
}

function getMermaidSource(block) {
    const proxy = block.querySelector(".chat-mermaid-selection-proxy");
    return proxy ? normaliseBlockText(proxy.value) : "";
}

function getMermaidTheme() {
    return document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "default";
}

function renderMermaidBlocks(root = document) {
    if (typeof mermaid === "undefined") return;
    const nodes = root.querySelectorAll(".chat-mermaid-diagram.mermaid:not([data-processed='true'])");
    if (!nodes.length) return;
    mermaid.initialize({ startOnLoad: false, theme: getMermaidTheme(), securityLevel: "loose" });
    try {
        mermaid.run({ nodes });
    } catch (err) {
        console.warn("chat mermaid render failed", err);
    }
}

function rerenderChatMermaid(root = document) {
    root.querySelectorAll(".chat-mermaid-block").forEach((block) => {
        const diagram = block.querySelector(".chat-mermaid-diagram");
        if (!diagram) return;
        diagram.removeAttribute("data-processed");
        diagram.textContent = getMermaidSource(block);
    });
    renderMermaidBlocks(root);
}

function selectAllMermaidSource(block) {
    const source = getMermaidSource(block);
    if (!source) return;
    const proxy = block.querySelector(".chat-mermaid-selection-proxy");
    if (!proxy) return;
    try {
        proxy.focus({ preventScroll: true });
    } catch (err) {
        proxy.focus();
    }
    proxy.select();
    const totalLines = getMermaidSourceLines(source).length;
    setMermaidSelectionStatus(block, formatMermaidSelection(1, totalLines));
}

function getSourceLineElement(node) {
    if (!node) return null;
    const element = node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement;
    return element ? element.closest(".chat-mermaid-source-line") : null;
}

function updateMermaidSelectionFromPage() {
    const selection = window.getSelection();
    const blocks = document.querySelectorAll(".chat-mermaid-block[data-view='source']");

    blocks.forEach((block) => setMermaidSelectionStatus(block, ""));

    if (!selection || selection.rangeCount === 0 || selection.isCollapsed) return;

    const range = selection.getRangeAt(0);
    const startLine = getSourceLineElement(range.startContainer);
    const endLine = getSourceLineElement(range.endContainer);
    if (!startLine || !endLine) return;

    const block = startLine.closest(".chat-mermaid-block");
    if (!block || block !== endLine.closest(".chat-mermaid-block")) return;

    const start = Number(startLine.dataset.lineNumber);
    const end = Number(endLine.dataset.lineNumber);
    setMermaidSelectionStatus(block, formatMermaidSelection(Math.min(start, end), Math.max(start, end)));
}

function initMermaidBlocks(root) {
    root.querySelectorAll(".chat-mermaid-block").forEach((block) => {
        if (block.dataset.initialised === "true") return;
        block.dataset.initialised = "true";

        block.querySelectorAll(".chat-mermaid-toggle button").forEach((button) => {
            button.addEventListener("click", () => {
                setMermaidView(block, button.dataset.viewTarget || "diagram");
            });
        });

        const diagram = block.querySelector(".chat-mermaid-diagram");
        if (diagram) {
            diagram.addEventListener("mouseup", () => {
                if (block.getAttribute("data-view") !== "diagram") return;
                selectAllMermaidSource(block);
            });
        }
    });
}

async function renderBotMessage(node, text) {
    node.classList.add("markdown-rendered");
    node.innerHTML = await renderMarkdown(text);
    initMermaidBlocks(node);
    renderMermaidBlocks(node);
}

function buildIntroPanel(panel, body) {
    body.innerHTML = "";
    const intro = el("div", { class: "chat-intro" });
    intro.appendChild(el("h3", {}, t("intro_h")));
    intro.appendChild(el("p", {}, t("intro_p")));
    const ul = el("ul", {});
    for (const note of I18N[currentLocale()].notes) ul.appendChild(el("li", {}, note));
    intro.appendChild(ul);

    const supported = "gpu" in navigator;
    if (!supported) {
        intro.appendChild(el("p", { class: "chat-msg error" }, t("no_webgpu")));
    } else {
        const loadBtn = el(
            "button",
            { class: "chat-load-btn", onclick: () => startLoad(panel, body, loadBtn, intro) },
            t("load_btn"),
        );
        intro.appendChild(loadBtn);

        // Language checkboxes for cross-lesson indexing. Pre-checks the
        // current page's language. Already-cached languages show ✓ and
        // are checked + disabled (re-indexing them is a no-op anyway).
        const indexSection = el("div", { class: "chat-index-options" });
        indexSection.appendChild(el("p", { class: "chat-index-label" }, t("index_section_label")));
        indexSection.appendChild(el("p", { class: "chat-index-help muted" }, t("index_section_help")));
        const cur = currentLocale();
        for (const lang of SUPPORTED_LANGS) {
            const cbId = `chat-index-cb-${lang}`;
            const wrap = el("label", { class: "chat-index-checkbox", for: cbId });
            const ready = getLangIndexState(lang) === "ready";
            const cb = el("input", { type: "checkbox", id: cbId, "data-lang": lang });
            if (lang === cur || ready) cb.checked = true;
            if (ready) cb.disabled = true;
            wrap.appendChild(cb);
            wrap.appendChild(el("span", {}, t(`lang_${lang}_full`) + (ready ? " ✓" : "")));
            indexSection.appendChild(wrap);
        }
        intro.appendChild(indexSection);

        intro.appendChild(el("p", { class: "muted" }, t("subtitle")));
    }
    body.appendChild(intro);
}

// Update the "✓" + disabled state on intro checkboxes when an indexing
// run completes (e.g. user kicked off indexing via the chip while the
// intro is still visible — though normally the intro is gone by then).
function refreshIntroIndexCheckboxes() {
    for (const lang of SUPPORTED_LANGS) {
        const cb = document.getElementById(`chat-index-cb-${lang}`);
        if (!cb) continue;
        const span = cb.parentElement.querySelector("span");
        const ready = getLangIndexState(lang) === "ready";
        if (ready && span && !span.textContent.includes("✓")) {
            cb.checked = true;
            cb.disabled = true;
            span.textContent = t(`lang_${lang}_full`) + " ✓";
        }
    }
}

// ----- Model state --------------------------------------------------------
let pipelinePromise = null;
let generator = null;
let chatHistory = [];
let pendingAbort = null;

// ----- Cross-page persistence --------------------------------------------
// Two scopes:
//   sessionStorage = current browser tab. Holds the panel's open/closed
//     state, the current conversation, and the user's per-tab language
//     index choice. These are tab-scoped concepts and shouldn't leak
//     across tabs.
//   localStorage = browser-wide, survives tab close. Holds only the
//     "model has been loaded once on this device" flag, which lets
//     `buildPanel` skip the intro/load-button and auto-load from cache
//     on any future visit (any tab, any page). The flag tracks consent
//     to the 3.1 GB download — once given, we don't ask again. If the
//     IndexedDB cache is later evicted, auto-load will silently
//     re-download from Hugging Face (the cache layer handles this).
const STATE_KEYS = {
    open: "chanma-chat-open",
    history: "chanma-chat-history",
    loaded: "chanma-chat-loaded",          // localStorage (persistent)
    indexLangs: "chanma-chat-index-langs",
};

function readState(key) {
    try { return sessionStorage.getItem(key); } catch (err) { return null; }
}
function writeState(key, value) {
    try { sessionStorage.setItem(key, value); } catch (err) { /* quota / disabled */ }
}
function readPersistent(key) {
    try { return localStorage.getItem(key); } catch (err) { return null; }
}
function writePersistent(key, value) {
    try { localStorage.setItem(key, value); } catch (err) { /* quota / disabled */ }
}
function saveOpenState(open) { writeState(STATE_KEYS.open, open ? "1" : "0"); }
function saveHistoryState() {
    try { writeState(STATE_KEYS.history, JSON.stringify(chatHistory)); } catch (err) {}
}
function markLoadedState() { writePersistent(STATE_KEYS.loaded, "1"); }
function saveCheckedLangsState(langs) {
    try { writeState(STATE_KEYS.indexLangs, JSON.stringify(langs)); } catch (err) {}
}
function loadHistoryState() {
    const raw = readState(STATE_KEYS.history);
    if (!raw) return;
    try {
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed)) chatHistory = parsed;
    } catch (err) { /* ignore corrupt entry */ }
}
function wasLoadedBefore() { return readPersistent(STATE_KEYS.loaded) === "1"; }
function getStoredCheckedLangs() {
    const raw = readState(STATE_KEYS.indexLangs);
    if (!raw) return null;
    try {
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed)) return parsed;
    } catch (err) {}
    return null;
}

// ----- RAG state ----------------------------------------------------------
let embedderPromise = null;
let embedder = null;
let chunksPromise = null;
let allChunks = null;                                 // [{id, lang, url, title, text}]
const langEmbeddings = new Map();                     // lang → { ids, vectors: Float32Array, dim }
const langIndexPromises = new Map();                  // lang → Promise<void>  (in-flight build)
const langIndexState = new Map();                     // lang → "none"|"indexing"|"ready"|"error"
const langIndexProgress = new Map();                  // lang → { done, total }
let ragDb = null;                                     // IDBDatabase

const SUPPORTED_LANGS = ["en", "hk", "tw", "cn"];

async function loadGenerator(intro) {
    if (generator) return generator;
    if (!pipelinePromise) {
        pipelinePromise = (async () => {
            const tx = await import(/* @vite-ignore */ CDN_URL);
            const { AutoProcessor, Gemma4ForConditionalGeneration, TextStreamer } = tx;
            const modelInfo = MODEL_OPTIONS[ACTIVE_MODEL];
            const progressEl = ensureProgressUI(intro);
            resetProgressState();
            const onProgress = (data) => updateProgress(progressEl, data);
            const processor = await AutoProcessor.from_pretrained(modelInfo.id, {
                progress_callback: onProgress,
            });
            const model = await Gemma4ForConditionalGeneration.from_pretrained(modelInfo.id, {
                dtype: "q4f16",
                device: "webgpu",
                progress_callback: onProgress,
            });
            generator = { processor, model, TextStreamer };
            return generator;
        })();
    }
    return pipelinePromise;
}

// ----- RAG: embedding model + chunks --------------------------------------
async function loadEmbedder() {
    if (embedder) return embedder;
    if (!embedderPromise) {
        embedderPromise = (async () => {
            const tx = await import(/* @vite-ignore */ CDN_URL);
            const { pipeline } = tx;
            // EmbeddingGemma is Gemma-architected; some of its ops can't be
            // compiled to a WebGPU shader pipeline (getBindGroupLayout fails
            // during pipeline creation), so we run the embedder on WASM.
            // A 300M embedding model is fast enough on WASM — embeddings are
            // computed once per query, not token-by-token like generation —
            // and WASM avoids contending with Gemma 4 E2B for the GPU.
            embedder = await pipeline("feature-extraction", EMBED_MODEL_ID, {
                device: "wasm",
                dtype: "q8",
            });
            return embedder;
        })();
    }
    return embedderPromise;
}

async function loadChunks() {
    if (allChunks) return allChunks;
    if (!chunksPromise) {
        chunksPromise = (async () => {
            const res = await fetch(CHUNKS_URL);
            if (!res.ok) throw new Error(`chunks fetch ${res.status}`);
            allChunks = await res.json();
            return allChunks;
        })();
    }
    return chunksPromise;
}

// ----- Lesson citation → URL index ----------------------------------------
// Maps the bracketed lesson citations the tutor emits (e.g. "[Week 5: Bonds
// - Your Portfolio's Shock Absorber]" or the abbreviated "[Week 5: Bonds]")
// to the corresponding page URL, so renderMarkdown can linkify them in-place.
// Built lazily from allChunks on first use and cached.
let lessonUrlIndex = null;

function normaliseTitleKey(s) {
    return String(s).toLowerCase().replace(/[\s\-—–:,.!?'"`]+/g, " ").trim();
}

async function getLessonUrlIndex() {
    if (lessonUrlIndex) return lessonUrlIndex;
    const chunks = await loadChunks();
    const exact = new Map();                 // normalised full title → url
    const byNumber = new Map();              // "week05" | "side05" | "level1" → url
    const prefixes = [];                     // { key, url }, longest first
    for (const c of chunks) {
        if (!c || !c.title || !c.url) continue;
        const key = normaliseTitleKey(c.title);
        if (key && !exact.has(key)) exact.set(key, c.url);
        // Derive the numeric slug: "Week 5" → "week05",
        // "Side Lesson 12" → "side12", "Level 1" → "level1".
        const m = c.title.match(/^(Week|Side(?:\s+Lesson)?|Level)\s+(\d+)/i);
        if (m) {
            const kind = m[1].toLowerCase().replace(/\s+lesson/, "");
            const slug = kind + String(Number(m[2])).padStart(2, "0");
            if (!byNumber.has(slug)) byNumber.set(slug, c.url);
        }
        if (key) prefixes.push({ key, url: c.url });
    }
    // Longest key first so "[Week 5: Bonds]" can't match "Week 50: …".
    prefixes.sort((a, b) => b.key.length - a.key.length);
    lessonUrlIndex = { exact, byNumber, prefixes };
    return lessonUrlIndex;
}

// Resolve a citation label (bracket inner text) to a lesson URL, or null.
function linkifyCitation(label, idx) {
    const key = normaliseTitleKey(label);
    if (!key) return null;
    // 1. Exact full-title match.
    if (idx.exact.has(key)) return idx.exact.get(key);
    // 2. Prefix match: either the label is a prefix of a canonical title
    //    (LLM abbreviated, e.g. "[Week 5: Bonds]") or vice versa. Iterate
    //    longest-first so "week 5 bonds" is tried before "week 50 …".
    for (const { key: k, url } of idx.prefixes) {
        if (k.startsWith(key) || key.startsWith(k)) return url;
    }
    // 3. Structured fallback: parse "Week 5" / "Side Lesson 5" / "Level 1"
    //    → slug (week05/side05/level1). Catches very abbreviated citations
    //    where the prefix match can't help (e.g. "[Side Lesson 01: Calculator]").
    const m = label.match(/^(Week|Side(?:\s+Lesson)?|Level)\s+(\d+)/i);
    if (m) {
        const kind = m[1].toLowerCase().replace(/\s+lesson/, "");
        const slug = kind + String(Number(m[2])).padStart(2, "0");
        if (idx.byNumber.has(slug)) return idx.byNumber.get(slug);
    }
    return null;
}

// ----- Prebuilt embedding cache (shipped static binary) --------------------
// Downloads docs/assets/chatbot_embeddings.bin (~18 MB) once and populates
// the in-memory + IndexedDB caches for every language, replacing the old
// 30s+ per-language indexing step. Falls back silently (returns false) if
// the bin is missing, corrupt, stale (chunk text changed), or on any parse
// error — callers then use the dynamic embedTexts() path.
let prebuiltBinPromise = null;   // Promise<boolean> — tried at most once

async function loadPrebuiltEmbeddings() {
    if (prebuiltBinPromise) return prebuiltBinPromise;
    prebuiltBinPromise = (async () => {
        let res;
        try {
            res = await fetch(EMBEDDINGS_BIN_URL);
        } catch (err) {
            console.warn("prebuilt embeddings fetch failed", err);
            return false;
        }
        if (!res.ok) {
            // 404 when the bin hasn't been built/shipped yet — normal fallback.
            console.warn(`prebuilt embeddings not available (${res.status})`);
            return false;
        }
        const buf = await res.arrayBuffer();
        const dv = new DataView(buf);
        let off = 0;
        const readU32 = () => { const v = dv.getUint32(off, true); off += 4; return v; };

        // Header (52 bytes): magic, version, count, dim, dtype, 32-byte hash.
        const magic = readU32();
        if (magic !== EMBED_BIN_MAGIC) {
            console.warn("prebuilt embeddings: bad magic", magic.toString(16));
            return false;
        }
        const version = readU32();
        if (version !== EMBED_BIN_VERSION) {
            console.warn(`prebuilt embeddings: version ${version} != ${EMBED_BIN_VERSION}`);
            return false;
        }
        const count = readU32();
        const dim = readU32();
        if (dim !== 768) {
            console.warn(`prebuilt embeddings: unexpected dim ${dim}`);
            return false;
        }
        const dtype = readU32();
        if (dtype !== EMBED_BIN_DTYPE_F32) {
            console.warn(`prebuilt embeddings: unsupported dtype ${dtype}`);
            return false;
        }
        const binHashBytes = new Uint8Array(buf, off, 32);
        off += 32;

        // Staleness check: SHA-256 of every chunk text in ascending id order,
        // exactly as computed by build_chatbot_embeddings.mjs. If lesson
        // content changed, the bin is stale and we must not use it.
        const chunks = await loadChunks();
        const ordered = [...chunks].sort((a, b) => a.id - b.id);
        const textBytes = new TextEncoder().encode(ordered.map((c) => c.text).join(""));
        const digest = await crypto.subtle.digest("SHA-256", textBytes);
        const computed = new Uint8Array(digest);
        for (let i = 0; i < 32; i++) {
            if (computed[i] !== binHashBytes[i]) {
                console.warn("prebuilt embeddings: stale (chunk text changed) — falling back");
                return false;
            }
        }

        // Lang table: 4 langs × (u32 offset, u32 count), canonical order.
        const langTable = [];
        for (let i = 0; i < EMBED_BIN_LANGS.length; i++) {
            const offset = readU32();
            const n = readU32();
            langTable.push({ lang: EMBED_BIN_LANGS[i], offset, count: n });
        }

        // ids: count × u32, then vectors: count × dim × f32, both grouped by lang.
        const idsAll = new Uint32Array(buf, off, count);
        off += count * 4;
        const vectorsAll = new Float32Array(buf, off, count * dim);

        // Slice each language's contiguous block out and hydrate caches.
        for (const { lang, offset, count: n } of langTable) {
            if (n === 0) {
                langEmbeddings.set(lang, { ids: [], vectors: new Float32Array(0), dim });
                setLangIndexState(lang, "ready");
                continue;
            }
            const ids = Array.from(idsAll.subarray(offset, offset + n));
            // Float32Array.subarray is a view into the same ArrayBuffer; copy
            // so the entry owns its memory and survives any future GC of buf.
            const vectors = new Float32Array(vectorsAll.subarray(offset * dim, (offset + n) * dim));
            const entry = { ids, vectors, dim };
            langEmbeddings.set(lang, entry);
            setLangIndexState(lang, "ready");
            // Persist to IndexedDB so the next visit skips the 18 MB download.
            saveCachedEmbeddings(lang, {
                ids,
                vectors: vectors.buffer.slice(0),
                dim,
                model: EMBED_MODEL_ID,
            }).catch((err) => console.warn("prebuilt IDB write failed", lang, err));
        }
        return true;
    })().catch((err) => {
        console.warn("prebuilt embeddings failed", err);
        return false;
    });
    return prebuiltBinPromise;
}

// ----- IndexedDB cache for per-language embeddings ------------------------
function openRagDb() {
    if (ragDb) return Promise.resolve(ragDb);
    return new Promise((resolve, reject) => {
        const req = indexedDB.open(RAG_DB_NAME, RAG_DB_VERSION);
        req.onupgradeneeded = () => {
            const db = req.result;
            if (!db.objectStoreNames.contains(RAG_STORE)) {
                db.createObjectStore(RAG_STORE);
            }
        };
        req.onsuccess = () => { ragDb = req.result; resolve(ragDb); };
        req.onerror = () => reject(req.error);
    });
}

async function loadCachedEmbeddings(lang) {
    try {
        const db = await openRagDb();
        const cached = await new Promise((resolve, reject) => {
            const tx = db.transaction(RAG_STORE, "readonly");
            const req = tx.objectStore(RAG_STORE).get(lang);
            req.onsuccess = () => resolve(req.result || null);
            req.onerror = () => reject(req.error);
        });
        // Reject stale entries written by a different embedding model
        // (e.g. after switching from MiniLM to embeddinggemma). Entries
        // without a model stamp are also rejected now that we stamp on write.
        if (cached && cached.model && cached.model !== EMBED_MODEL_ID) {
            console.warn(`RAG cache for ${lang}: stale model '${cached.model}' != '${EMBED_MODEL_ID}'`);
            return null;
        }
        return cached || null;
    } catch (err) {
        console.warn("RAG cache read failed", err);
        return null;
    }
}

async function saveCachedEmbeddings(lang, payload) {
    // Always stamp the embedding model so future loads can detect a model
    // swap and discard incompatible vectors without a DB-version bump.
    if (payload) payload.model = payload.model || EMBED_MODEL_ID;
    try {
        const db = await openRagDb();
        await new Promise((resolve, reject) => {
            const tx = db.transaction(RAG_STORE, "readwrite");
            tx.objectStore(RAG_STORE).put(payload, lang);
            tx.oncomplete = () => resolve();
            tx.onerror = () => reject(tx.error);
        });
    } catch (err) {
        console.warn("RAG cache write failed", err);
    }
}

// ----- Embedding & retrieval ----------------------------------------------
async function embedTexts(texts, onBatch) {
    const e = await loadEmbedder();
    const dim = 768;                       // embeddinggemma-300m
    const out = new Float32Array(texts.length * dim);
    const batchSize = 16;
    for (let i = 0; i < texts.length; i += batchSize) {
        const batch = texts.slice(i, i + batchSize);
        const result = await e(batch, { pooling: "mean", normalize: true });
        // transformers.js returns a Tensor — flatten its data into our buffer.
        const data = result.data;
        out.set(data, i * dim);
        if (onBatch) onBatch(Math.min(i + batch.length, texts.length), texts.length);
    }
    return { vectors: out, dim };
}

function setLangIndexState(lang, state, progress) {
    langIndexState.set(lang, state);
    if (progress) langIndexProgress.set(lang, progress);
    else langIndexProgress.delete(lang);
    refreshIndexChip();
    refreshIntroIndexCheckboxes();
}

function getLangIndexState(lang) {
    return langIndexState.get(lang) || "none";
}

// Look up a previously-cached embedding set in IndexedDB and hydrate it
// into the in-memory map without re-embedding. Called once per language
// when the chat panel is built so the chip reflects state from past sessions.
// On an IDB miss, opportunistically try the shipped prebuilt binary, which
// populates every language in one ~18 MB download (and writes each back to
// IDB so later visits skip the download).
async function probeCachedIndex(lang) {
    if (langEmbeddings.has(lang)) return true;
    const cached = await loadCachedEmbeddings(lang);
    if (cached && cached.vectors instanceof ArrayBuffer && Array.isArray(cached.ids)) {
        const entry = {
            ids: cached.ids,
            vectors: new Float32Array(cached.vectors),
            dim: cached.dim || 768,
        };
        langEmbeddings.set(lang, entry);
        setLangIndexState(lang, "ready");
        return true;
    }
    // IDB miss — one-shot prebuilt bin fetch (populates all langs at once).
    if (await loadPrebuiltEmbeddings()) {
        return langEmbeddings.has(lang);
    }
    return false;
}

async function probeAllCachedIndexes() {
    for (const lang of SUPPORTED_LANGS) {
        if (!langIndexState.has(lang)) {
            await probeCachedIndex(lang);
        }
    }
}

// Explicitly build (or rebuild) the embedding index for one language.
// Triggered from the intro-panel checkboxes during model load, or from
// the header chip click later. Never called implicitly from a query —
// if the user hasn't opted in, retrieval just returns no excerpts.
async function buildIndexFor(lang) {
    if (getLangIndexState(lang) === "ready") return;
    if (langIndexPromises.has(lang)) return langIndexPromises.get(lang);

    const promise = (async () => {
        // Fast path: the shipped prebuilt binary populates every language in
        // one ~18 MB download. Only fall through to per-chunk embedding if
        // the bin is missing, stale, or doesn't cover this lang.
        if (await loadPrebuiltEmbeddings() && langEmbeddings.has(lang)) {
            return; // setLangIndexState("ready") already called inside
        }
        setLangIndexState(lang, "indexing", { done: 0, total: 0 });
        try {
            await loadEmbedder();
            const chunks = await loadChunks();
            const subset = chunks.filter((c) => c.lang === lang);
            if (subset.length === 0) {
                langEmbeddings.set(lang, { ids: [], vectors: new Float32Array(0), dim: 768 });
                setLangIndexState(lang, "ready");
                return;
            }
            const { vectors, dim } = await embedTexts(
                subset.map((c) => c.text),
                (done, total) => setLangIndexState(lang, "indexing", { done, total }),
            );
            const entry = { ids: subset.map((c) => c.id), vectors, dim };
            langEmbeddings.set(lang, entry);
            await saveCachedEmbeddings(lang, {
                ids: entry.ids,
                vectors: vectors.buffer,
                dim,
            });
            setLangIndexState(lang, "ready");
        } catch (err) {
            console.warn("buildIndexFor failed", lang, err);
            setLangIndexState(lang, "error");
            throw err;
        }
    })();

    langIndexPromises.set(lang, promise);
    try {
        await promise;
    } finally {
        langIndexPromises.delete(lang);
    }
}

function cosineTopK(query, entry, k, excludeChunk) {
    const { ids, vectors, dim } = entry;
    if (!ids.length) return [];
    // Both query and stored vectors are L2-normalized → dot product = cosine.
    const scores = new Float32Array(ids.length);
    for (let i = 0; i < ids.length; i++) {
        let s = 0;
        const off = i * dim;
        for (let d = 0; d < dim; d++) s += query[d] * vectors[off + d];
        scores[i] = s;
    }
    const order = Array.from(scores.keys()).sort((a, b) => scores[b] - scores[a]);
    const picked = [];
    const perUrlCount = new Map();
    for (const i of order) {
        const id = ids[i];
        const chunk = allChunks[id];
        if (!chunk) continue;
        if (excludeChunk && chunk.url === excludeChunk) continue;
        // Diversify: at most 2 chunks per source URL so a single lesson
        // doesn't crowd out everything else.
        const c = perUrlCount.get(chunk.url) || 0;
        if (c >= 2) continue;
        perUrlCount.set(chunk.url, c + 1);
        picked.push({ chunk, score: scores[i] });
        if (picked.length >= k) break;
    }
    return picked;
}

function currentPageUrl() {
    const path = window.location.pathname;
    const last = path.substring(path.lastIndexOf("/") + 1);
    return last || "index.html";
}

async function retrieveContext(question) {
    try {
        const lang = currentLocale();
        // Only retrieve if the user has explicitly opted in to indexing
        // for this language and it has finished building.
        if (getLangIndexState(lang) !== "ready") return [];
        const entry = langEmbeddings.get(lang);
        if (!entry || !entry.ids.length) return [];
        const e = await loadEmbedder();
        const result = await e([question], { pooling: "mean", normalize: true });
        const queryVec = new Float32Array(result.data);
        return cosineTopK(queryVec, entry, TOP_K, currentPageUrl());
    } catch (err) {
        console.warn("retrieveContext failed", err);
        return [];
    }
}

function ensureProgressUI(intro) {
    let p = intro.querySelector(".chat-progress");
    if (p) return p;
    p = el("div", { class: "chat-progress" });
    p.appendChild(el("div", { class: "chat-progress-label" }, el("span", {}, t("loading")), el("span", { class: "pct" }, "0%")));
    const bar = el("div", { class: "chat-progress-bar" });
    bar.appendChild(el("div", { class: "chat-progress-fill" }));
    p.appendChild(bar);
    intro.appendChild(p);
    return p;
}

// Aggregate per-file download bytes across the whole model load so the bar
// climbs monotonically instead of resetting each time a new file starts.
const progressFiles = new Map();   // file name → { loaded, total }
let progressMaxPct = 0;            // monotonic clamp on displayed value

function updateProgress(p, data) {
    if (!data) return;
    const key = data.file || data.name;
    if (key) {
        const entry = progressFiles.get(key) || { loaded: 0, total: 0 };
        if (data.status === "done") {
            // Finalize this file: clamp to its known total (or to loaded if unknown).
            entry.loaded = entry.total || data.total || data.loaded || entry.loaded;
        } else if (data.loaded != null && data.total != null && data.total > 0) {
            entry.loaded = data.loaded;
            entry.total = data.total;
        } else if (typeof data.progress === "number" && data.total > 0) {
            entry.loaded = (data.progress / 100) * data.total;
            entry.total = data.total;
        }
        progressFiles.set(key, entry);
    }

    let sumLoaded = 0;
    let sumTotal = 0;
    for (const e of progressFiles.values()) {
        sumLoaded += e.loaded || 0;
        sumTotal += e.total || 0;
    }
    // Use the known model size as a floor for the denominator so we don't
    // overshoot to ~100% when only the first small file (tokenizer.json,
    // config.json) has been discovered.
    const modelInfo = MODEL_OPTIONS[ACTIVE_MODEL];
    const knownTotal = (modelInfo && modelInfo.size_mb ? modelInfo.size_mb * 1024 * 1024 : 0);
    const denom = Math.max(sumTotal, knownTotal);
    if (denom <= 0) return;

    let pct = (sumLoaded / denom) * 100;
    if (!Number.isFinite(pct)) return;
    pct = Math.max(0, Math.min(100, pct));
    // Monotonic: never go backwards, even if a newly-seen file grows the
    // denominator faster than its bytes have arrived.
    if (pct < progressMaxPct) pct = progressMaxPct;
    progressMaxPct = pct;

    const fill = p.querySelector(".chat-progress-fill");
    const lbl = p.querySelector(".pct");
    if (fill) fill.style.width = pct.toFixed(1) + "%";
    if (lbl) lbl.textContent = pct.toFixed(0) + "%";
}

function resetProgressState() {
    progressFiles.clear();
    progressMaxPct = 0;
}

async function startLoad(panel, body, loadBtn, intro) {
    loadBtn.disabled = true;
    loadBtn.textContent = t("loading");

    // Snapshot the user's checkbox selection BEFORE we tear down the intro
    // panel (showChatUI replaces its DOM).
    const checkedLangs = Array.from(intro.querySelectorAll(".chat-index-checkbox input:checked"))
        .map((cb) => cb.dataset.lang)
        .filter((lang) => SUPPORTED_LANGS.includes(lang));
    saveCheckedLangsState(checkedLangs);

    try {
        // RAG warmup: fetch chunks JSON + embedder model in parallel with
        // the Gemma download. Both are small (~7 MB JSON, ~50 MB model)
        // and will finish long before Gemma's 3.1 GB.
        loadEmbedder().catch((err) => console.warn("embedder load failed", err));
        loadChunks().catch((err) => console.warn("chunks load failed", err));

        // Build embedding indexes for every checked language in parallel
        // with Gemma. We do NOT await this — we let it continue running
        // after the chat UI shows, with the chip reporting progress.
        // Already-cached languages skip embedding (buildIndexFor short-
        // circuits when state is already "ready" via probeCachedIndex).
        const indexingPromise = (async () => {
            await probeAllCachedIndexes();
            for (const lang of checkedLangs) {
                if (getLangIndexState(lang) === "ready") continue;
                try {
                    await buildIndexFor(lang);
                } catch (err) {
                    // Already marked error — chip will surface it. Don't
                    // halt the rest of the languages.
                }
            }
        })();

        await loadGenerator(intro);
        markLoadedState();
        showChatUI(panel, body);
        refreshIndexChip();
        // indexingPromise keeps running in the background; chip updates
        // come through setLangIndexState → refreshIndexChip.
        indexingPromise.catch((err) => console.warn("indexing failed", err));
    } catch (err) {
        const errBox = el("p", { class: "chat-msg error" }, t("load_failed") + (err && err.message || String(err)));
        intro.appendChild(errBox);
        loadBtn.disabled = false;
        loadBtn.textContent = t("load_btn");
    }
}

// ----- Chat UI ------------------------------------------------------------
function ensureComposer(panel) {
    let composer = panel.querySelector(".chat-composer");
    if (composer) return composer;
    composer = el("div", { class: "chat-composer" });
    const ta = el("textarea", { placeholder: t("placeholder"), rows: "1" });
    ta.addEventListener("input", () => {
        ta.style.height = "auto";
        ta.style.height = Math.min(120, ta.scrollHeight) + "px";
    });
    ta.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend(panel, ta);
        }
    });
    const sendBtn = el(
        "button",
        { title: t("send"), onclick: () => handleSend(panel, ta) },
        "↑",
    );
    composer.appendChild(ta);
    composer.appendChild(sendBtn);
    panel.appendChild(composer);
    return composer;
}

function setComposerEnabled(panel, enabled) {
    const composer = panel.querySelector(".chat-composer");
    if (!composer) return;
    const ta = composer.querySelector("textarea");
    const btn = composer.querySelector("button");
    if (ta) ta.disabled = !enabled;
    if (btn) btn.disabled = !enabled;
}

async function renderHistoryIntoBody(body) {
    for (const msg of chatHistory) {
        if (msg.role === "user") {
            appendMsg(body, "user", msg.content);
        } else if (msg.role === "assistant") {
            const node = appendMsg(body, "bot", "");
            await renderBotMessage(node, msg.content);
        }
    }
}

function showChatUI(panel, body) {
    body.innerHTML = "";
    body.classList.add("chat-body");
    if (chatHistory.length) {
        renderHistoryIntoBody(body).catch((err) => console.warn("history render failed", err));
    } else {
        body.appendChild(el("div", { class: "chat-msg system" }, t("ready")));
    }
    ensureComposer(panel);
    body.scrollTop = body.scrollHeight;
}

function appendMsg(body, role, text) {
    const node = el("div", { class: "chat-msg " + role }, text);
    body.appendChild(node);
    body.scrollTop = body.scrollHeight;
    return node;
}

async function handleSend(panel, textarea) {
    const userText = textarea.value.trim();
    if (!userText || !generator) return;
    textarea.value = "";
    textarea.style.height = "auto";

    const body = panel.querySelector(".chat-body");
    appendMsg(body, "user", userText);
    const botNode = appendMsg(body, "bot", "");
    botNode.textContent = t("thinking");

    chatHistory.push({ role: "user", content: userText });
    if (chatHistory.length > MAX_HISTORY_TURNS * 2) {
        chatHistory = chatHistory.slice(-MAX_HISTORY_TURNS * 2);
    }
    saveHistoryState();

    const systemPrompt = await buildSystemPrompt(userText);
    const messages = [
        { role: "system", content: systemPrompt },
        ...chatHistory,
    ];

    try {
        const { processor, model, TextStreamer } = generator;
        // Send text-only turns as plain strings, not as multimodal content
        // arrays. The Gemma 4 chat template applies `| trim` to
        // message.content, which the Jinja engine in transformers.js does
        // not implement for ArrayValue — wrapping text in an array would
        // throw "Unknown ArrayValue filter: trim".
        const prompt = processor.apply_chat_template(messages, {
            enable_thinking: false,
            add_generation_prompt: true,
            tokenize: false,
        });
        const inputs = await processor(prompt, null, null, { add_special_tokens: false });

        let acc = "";
        let started = false;
        const streamer = new TextStreamer(processor.tokenizer, {
            skip_prompt: true,
            skip_special_tokens: true,
            callback_function: (text) => {
                if (typeof text !== "string" || !text) return;
                acc += text;
                if (!started) { botNode.textContent = ""; started = true; }
                botNode.textContent = acc;
                body.scrollTop = body.scrollHeight;
            },
        });

        const outputs = await model.generate({
            ...inputs,
            max_new_tokens: MAX_NEW_TOKENS,
            do_sample: false,
            streamer,
        });

        // Fallback if streamer never fired
        if (!started) {
            const inputLen = inputs.input_ids.dims.at(-1);
            const decoded = processor.batch_decode(
                outputs.slice(null, [inputLen, null]),
                { skip_special_tokens: true },
            );
            acc = (decoded && decoded[0]) || "";
            botNode.textContent = acc;
        }
        await renderBotMessage(botNode, acc);
        chatHistory.push({ role: "assistant", content: acc });
        saveHistoryState();
    } catch (err) {
        botNode.classList.add("error");
        botNode.textContent = t("gen_failed") + (err && err.message || String(err));
    }
}

// ----- Wiring -------------------------------------------------------------
function buildPanel() {
    const panel = el("aside", { class: "chat-panel", id: "chat-panel", role: "dialog", "aria-label": t("title") });
    const header = el("div", { class: "chat-header" });
    const titleWrap = el("div", { class: "chat-title" });
    titleWrap.appendChild(el("span", { class: "chat-header-title" }, t("title")));
    titleWrap.appendChild(el("span", { class: "chat-subtitle" }, t("subtitle")));
    header.appendChild(titleWrap);
    header.appendChild(el("button", { class: "chat-header-clear", onclick: () => clearConversation(panel), title: t("clear") }, "↻"));
    header.appendChild(el("button", { class: "chat-header-close", onclick: () => togglePanel(false), title: t("close") }, "✕"));
    panel.appendChild(header);

    // Status bar with the cross-lesson index chip. Always present so the
    // user can see at a glance whether the current language is indexed,
    // and click to start indexing if not.
    const statusBar = el("div", { class: "chat-status-bar" });
    const chip = el("button", { class: "chat-index-chip", type: "button", onclick: () => onIndexChipClick() }, "");
    statusBar.appendChild(chip);
    panel.appendChild(statusBar);

    const body = el("div", { class: "chat-body" });
    panel.appendChild(body);
    document.body.appendChild(panel);
    if (wasLoadedBefore()) {
        // Model was already loaded earlier in this tab session — the weights
        // are cached, so skip the intro/load-button entirely and auto-load
        // from cache. Restores conversation history if any.
        loadHistoryState();
        restoreLoadedSession(panel, body).catch((err) =>
            console.warn("auto-load on panel build failed", err));
    } else {
        buildIntroPanel(panel, body);
    }
    // Probe IndexedDB for any cached indexes from previous sessions, then
    // render the chip with the correct state for the current language.
    probeAllCachedIndexes().then(refreshIndexChip).catch(() => refreshIndexChip());
    return panel;
}

// Re-create the chat UI for a session where the Gemma weights are already
// in the browser cache (from an earlier load this tab). Used both when
// auto-restoring a panel that was open on the previous page and when the
// user re-opens a closed panel via the FAB on a new page.
async function restoreLoadedSession(panel, body) {
    body.innerHTML = "";
    body.classList.add("chat-body");

    const progressHost = el("div", { class: "chat-intro chat-restore-host" });
    body.appendChild(progressHost);
    if (chatHistory.length) await renderHistoryIntoBody(body);

    ensureComposer(panel);
    setComposerEnabled(panel, false);

    const checkedLangs = getStoredCheckedLangs() || [currentLocale()];

    try {
        loadEmbedder().catch((err) => console.warn("embedder load failed", err));
        loadChunks().catch((err) => console.warn("chunks load failed", err));
        const indexingPromise = (async () => {
            await probeAllCachedIndexes();
            for (const lang of checkedLangs) {
                if (getLangIndexState(lang) === "ready") continue;
                try { await buildIndexFor(lang); } catch (err) { /* chip shows error */ }
            }
        })();

        await loadGenerator(progressHost);
        progressHost.remove();
        setComposerEnabled(panel, true);
        refreshIndexChip();
        indexingPromise.catch((err) => console.warn("indexing failed", err));
    } catch (err) {
        progressHost.appendChild(el("p", { class: "chat-msg error" },
            t("load_failed") + (err && err.message || String(err))));
    }
}

function refreshIndexChip() {
    const chip = document.querySelector(".chat-index-chip");
    if (!chip) return;
    const lang = currentLocale();
    const state = getLangIndexState(lang);
    chip.classList.remove("ready", "indexing", "none", "error");
    chip.classList.add(state);
    if (state === "ready") {
        chip.textContent = "✓ " + t("chip_ready");
        chip.title = t("chip_ready_title");
        chip.disabled = true;
    } else if (state === "indexing") {
        const p = langIndexProgress.get(lang) || { done: 0, total: 0 };
        const pct = p.total ? Math.round(100 * p.done / p.total) : 0;
        chip.textContent = `⏳ ${t("chip_indexing")} ${pct}%`;
        chip.title = "";
        chip.disabled = true;
    } else if (state === "error") {
        chip.textContent = "⚠ " + t("chip_error");
        chip.title = t("chip_retry_title");
        chip.disabled = false;
    } else {
        chip.textContent = "○ " + t("chip_none");
        chip.title = t("chip_index_title");
        chip.disabled = false;
    }
}

async function onIndexChipClick() {
    const lang = currentLocale();
    const state = getLangIndexState(lang);
    if (state === "ready" || state === "indexing") return;
    try {
        await buildIndexFor(lang);
    } catch (err) {
        // setLangIndexState already marked it as error and refreshed the chip.
    }
}

// Re-translate every static label inside the chat panel. Called whenever
// the user toggles language so the header / tooltips / composer follow.
function updateChatI18n() {
    const panel = document.getElementById("chat-panel");
    if (!panel) return;
    panel.setAttribute("aria-label", t("title"));
    const titleEl = panel.querySelector(".chat-header-title");
    if (titleEl) titleEl.textContent = t("title");
    const subtitleEl = panel.querySelector(".chat-subtitle");
    if (subtitleEl) subtitleEl.textContent = t("subtitle");
    const clearBtn = panel.querySelector(".chat-header-clear");
    if (clearBtn) clearBtn.title = t("clear");
    const closeBtn = panel.querySelector(".chat-header-close");
    if (closeBtn) closeBtn.title = t("close");
    const composer = panel.querySelector(".chat-composer");
    if (composer) {
        const ta = composer.querySelector("textarea");
        if (ta) ta.placeholder = t("placeholder");
        const sendBtn = composer.querySelector("button");
        if (sendBtn) sendBtn.title = t("send");
    }
}

function clearConversation(panel) {
    chatHistory = [];
    saveHistoryState();
    const body = panel.querySelector(".chat-body");
    if (!body) return;
    if (generator) {
        body.innerHTML = "";
        body.appendChild(el("div", { class: "chat-msg system" }, t("ready")));
    } else {
        buildIntroPanel(panel, body);
    }
}

function togglePanel(force) {
    const panel = document.getElementById("chat-panel") || buildPanel();
    const open = typeof force === "boolean" ? force : !panel.classList.contains("open");
    panel.classList.toggle("open", open);
    document.body.classList.toggle("chat-open", open);
    saveOpenState(open);
}

function buildFab() {
    const fab = el(
        "button",
        { class: "chat-fab", id: "chat-fab", title: t("title"), "aria-label": t("title"), onclick: () => togglePanel() },
        // Speech-bubble icon
    );
    fab.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.6-.8L3 21l1.9-5.7A8.38 8.38 0 0 1 3 11.5a8.5 8.5 0 0 1 17 0z"/></svg><span class="badge">AI</span>`;
    document.body.appendChild(fab);
}

// If the panel was open on the previous page (sessionStorage), pop it back
// up immediately. If the model had already been loaded once this session,
// `buildPanel` (called below) auto-triggers the load from cache and
// restores the previous conversation. The composer is disabled until the
// model is ready.
async function autoRestorePanel() {
    if (readState(STATE_KEYS.open) !== "1") return;
    loadHistoryState();
    const panel = document.getElementById("chat-panel") || buildPanel();
    panel.classList.add("open");
    document.body.classList.add("chat-open");
}

document.addEventListener("DOMContentLoaded", () => {
    buildFab();
    autoRestorePanel().catch((err) => console.warn("autoRestorePanel failed", err));
    // Keep i18n in sync if the user switches language while the panel is open.
    const observer = new MutationObserver(() => {
        const fab = document.getElementById("chat-fab");
        if (fab) {
            fab.title = t("title");
            fab.setAttribute("aria-label", t("title"));
        }
        const panel = document.getElementById("chat-panel");
        if (panel) {
            updateChatI18n();
            refreshIndexChip();
            if (!generator) {
                const body = panel.querySelector(".chat-body");
                if (body && body.querySelector(".chat-intro")) buildIntroPanel(panel, body);
            }
            rerenderChatMermaid(panel);
        }
    });
    document.querySelectorAll(".lang-content").forEach((n) => observer.observe(n, { attributes: true, attributeFilter: ["class"] }));
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
});

document.addEventListener("selectionchange", updateMermaidSelectionFromPage);
