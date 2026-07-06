# On-Device AI Tutor — Architecture

The website's floating bottom-right "tutor" button on every page. Read
this file before editing `web_assets/chatbot.{js,css}` or
`scripts/build_chatbot_index.py`.

## Model & runtime

- **LLM**: Gemma 4 E2B (~3.1 GB q4f16 on first load, then cached in
  IndexedDB) running directly in the browser via WebGPU + transformers.js
  v4 (`Gemma4ForConditionalGeneration` + `AutoProcessor` + `TextStreamer`).
- **Embedding model**: `onnx-community/embeddinggemma-300m-ONNX`
  (~300 MB q8) for cross-lesson retrieval. Runs on **WASM** (not WebGPU):
  EmbeddingGemma is Gemma-architected and some of its ops can't compile to a
  WebGPU shader pipeline (`getBindGroupLayout` fails during pipeline
  creation). WASM avoids the failure and avoids contending with Gemma 4 E2B
  for the GPU. The user still downloads this model at runtime because user
  queries are dynamic and can't be precomputed — but the slow per-chunk
  indexing step is eliminated by the prebuilt cache (below).
- All inference runs in the browser. **No data leaves the user's device.**

## Cross-lesson RAG (opt-in per language)

A static chunk index (`docs/assets/chatbot_chunks.json`, ~7 MB) lets the
assistant pull in relevant excerpts from the **whole course** in addition
to the current page.

- **Chunk index generator**: `scripts/build_chatbot_index.py` — pure
  stdlib (no external deps). Strips Part 2 (YouTube script), normalises
  markdown, splits into ~600-char overlapping chunks. **Must be
  regenerated whenever lesson content changes.**
- **Prebuilt embedding cache**: `scripts/build_chatbot_embeddings.mjs`
  (Node + `@huggingface/transformers`, run from `scripts/`). Embeds every
  chunk with the **same model + quantization + pooling** the browser uses
  (`onnx-community/embeddinggemma-300m-ONNX` q8, mean-pool + L2-normalize)
  and writes `docs/assets/chatbot_embeddings.bin` (~18 MB). This replaces
  the old 30s+ per-language in-browser indexing with a one-time download.
  **Must be re-run after `build_chatbot_index.py` whenever lesson content
  changes.** Binary format (all little-endian):

  ```
  Header (52 B): magic "CMEB" | version u32 | count u32 | dim u32 (768)
                 | dtype u32 (1=f32) | chunksHash [32] (SHA-256 of all
                 chunk texts concatenated in ascending id order)
  Lang table (4 × 8 B, order en/hk/tw/cn): offset u32 | count u32
  ids:      count × u32      (chunk id per row, grouped by lang)
  vectors:  count × dim × f32 (mean-pooled + normalized, grouped by lang)
  ```

  The browser recomputes the chunksHash over the loaded `chatbot_chunks.json`
  and refuses a stale bin (lesson content changed) by falling back to
  dynamic indexing. Entries are also stamped with the embedding model id in
  IndexedDB so a model swap invalidates old vectors without a DB-version bump.
- **Indexing is opt-in per language.** The intro panel renders four
  checkboxes (EN/HK/TW/CN, with the current page's language pre-checked).
  For any checked language, the browser first tries the prebuilt bin (one
  ~18 MB download populates all languages); only if the bin is missing,
  stale, or for an unsupported browser does it fall back to per-chunk
  embedding via the WASM embedder. This runs in **parallel** with the Gemma
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
- `scripts/build_chatbot_embeddings.mjs` (Node + transformers.js, optional
  toolchain under `scripts/`) produces `docs/assets/chatbot_embeddings.bin`.
  Regeneration order after lesson edits:
  `build_chatbot_index.py` → `build_chatbot_embeddings.mjs`. Install once
  with `cd scripts && npm install`, then `node build_chatbot_embeddings.mjs`.

## Browser support

Browsers without WebGPU (older Safari, in-app browsers) see a graceful
"not supported" message instead of a broken UI.
