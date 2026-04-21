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
const MAX_CONTEXT_CHARS = 12000;
const MAX_HISTORY_TURNS = 6;
const MAX_NEW_TOKENS = 512;

const CDN_URL = "https://cdn.jsdelivr.net/npm/@huggingface/transformers@4/+esm";

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

function buildSystemPrompt() {
    const lessonText = getActiveLessonText() || t("no_lesson");
    return (
        "You are an investing tutor for the Chanma Investment Tutorial. " +
        "Answer the user's question using ONLY the lesson text below. " +
        "If the lesson does not cover the question, say so honestly rather than guessing. " +
        "Reply in the same language the user uses. Keep answers concise (under ~200 words) " +
        "unless the user explicitly asks for more detail.\n\n" +
        "LESSON:\n" + lessonText
    );
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

function applyInlineMarkdown(text) {
    let html = escapeHtml(text);
    html = html.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (match, label, url) => (
        `<a href="${escapeAttr(url)}" target="_blank" rel="noreferrer noopener">${label}</a>`
    ));
    html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
    html = html.replace(/\*\*\*([^*]+?)\*\*\*/g, "<strong><em>$1</em></strong>");
    html = html.replace(/\*\*([^*]+?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/(^|[^\*])\*([^*\n]+?)\*(?!\*)/g, "$1<em>$2</em>");
    return html;
}

function renderMarkdownChunk(markdown) {
    const lines = normaliseBlockText(markdown).split("\n");
    const html = [];
    let paragraph = [];
    let listItems = [];
    let listType = null;
    let quoteLines = [];

    function flushParagraph() {
        if (!paragraph.length) return;
        html.push(`<p>${paragraph.map(applyInlineMarkdown).join("<br>")}</p>`);
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
        html.push(`<blockquote>${quoteLines.map(applyInlineMarkdown).join("<br>")}</blockquote>`);
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
            html.push(`<h${level}>${applyInlineMarkdown(heading[2])}</h${level}>`);
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
            listItems.push(`<li>${applyInlineMarkdown((ordered || bullet)[1])}</li>`);
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

function renderMarkdown(text) {
    return splitMarkdownBlocks(text).map((block) => {
        if (block.type === "code") return renderCodeBlock(block.lang, block.content);
        return renderMarkdownChunk(block.content);
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

function renderBotMessage(node, text) {
    node.classList.add("markdown-rendered");
    node.innerHTML = renderMarkdown(text);
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
        intro.appendChild(el("p", { class: "muted" }, t("subtitle")));
    }
    body.appendChild(intro);
}

// ----- Model state --------------------------------------------------------
let pipelinePromise = null;
let generator = null;
let chatHistory = [];
let pendingAbort = null;

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
    try {
        await loadGenerator(intro);
        showChatUI(panel, body);
    } catch (err) {
        const errBox = el("p", { class: "chat-msg error" }, t("load_failed") + (err && err.message || String(err)));
        intro.appendChild(errBox);
        loadBtn.disabled = false;
        loadBtn.textContent = t("load_btn");
    }
}

// ----- Chat UI ------------------------------------------------------------
function showChatUI(panel, body) {
    body.innerHTML = "";
    body.classList.add("chat-body");
    const sys = el("div", { class: "chat-msg system" }, t("ready"));
    body.appendChild(sys);

    let composer = panel.querySelector(".chat-composer");
    if (!composer) {
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
    }
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

    const messages = [
        { role: "system", content: buildSystemPrompt() },
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
        renderBotMessage(botNode, acc);
        chatHistory.push({ role: "assistant", content: acc });
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
    const body = el("div", { class: "chat-body" });
    panel.appendChild(body);
    document.body.appendChild(panel);
    buildIntroPanel(panel, body);
    return panel;
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

document.addEventListener("DOMContentLoaded", () => {
    buildFab();
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
