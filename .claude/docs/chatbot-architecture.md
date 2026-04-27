# On-Device AI Tutor — Architecture

The website's floating bottom-right "tutor" button on every page. Read
this file before editing `web_assets/chatbot.{js,css}` or
`scripts/build_chatbot_index.py`.

## Model & runtime

- **LLM**: Gemma 4 E2B (~3.1 GB q4f16 on first load, then cached in
  IndexedDB) running directly in the browser via WebGPU + transformers.js
  v4 (`Gemma4ForConditionalGeneration` + `AutoProcessor` + `TextStreamer`).
- **Embedding model**: `Xenova/paraphrase-multilingual-MiniLM-L12-v2`
  (~50 MB q8) for cross-lesson retrieval.
- All inference runs in the browser. **No data leaves the user's device.**

## Cross-lesson RAG (opt-in per language)

A static chunk index (`docs/assets/chatbot_chunks.json`, ~7 MB) lets the
assistant pull in relevant excerpts from the **whole course** in addition
to the current page.

- **Chunk index generator**: `scripts/build_chatbot_index.py` — pure
  stdlib (no external deps). Strips Part 2 (YouTube script), normalises
  markdown, splits into ~600-char overlapping chunks. **Must be
  regenerated whenever lesson content changes.**
- **Indexing is opt-in per language.** The intro panel renders four
  checkboxes (EN/HK/TW/CN, with the current page's language pre-checked).
  Indexing for any checked language runs in **parallel** with the Gemma
  download, so the user never waits at first message.
- **Status chip in chat header** shows whether the current language is
  indexed:
  - `✓ Cross-lesson search on`
  - `⏳ Indexing X%`
  - `○ Index this language`
  - `⚠ Index failed`
  Clicking the chip starts indexing on demand for any language at any time.
- **Fallback when not indexed**: the assistant answers using the **current
  page only**. No auto-trigger from queries.
- **Persistence**: per-language embeddings cached in IndexedDB
  (`chanma-chatbot-rag` DB) and probed on every panel open so
  previously-indexed languages are recognised across browser sessions.

## Query-time prompt assembly

At query time the system prompt is assembled as:

1. The **current page text** as the priority section.
2. The **top-5 retrieved excerpts** from other lessons (when available).
3. Instructions to **cite the source lesson title in brackets** for any
   cross-lesson reference.

## Source files & build wiring

- Source assets: `web_assets/chatbot.js`, `web_assets/chatbot.css`.
- `scripts/build.py` copies them to `docs/assets/` on every build.
- `scripts/build_chatbot_index.py` produces `docs/assets/chatbot_chunks.json`
  and must be re-run after lesson edits if cross-lesson search should
  reflect the new content.

## Browser support

Browsers without WebGPU (older Safari, in-app browsers) see a graceful
"not supported" message instead of a broken UI.
