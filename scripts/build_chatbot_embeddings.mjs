#!/usr/bin/env node
/**
 * Prebuild the chatbot's cross-lesson embedding cache as a static binary
 * file so website visitors get instant cross-lesson search instead of
 * waiting 30s+ for in-browser indexing.
 *
 * Uses the SAME library (@huggingface/transformers v4), SAME model
 * (onnx-community/embeddinggemma-300m-ONNX), SAME quantization (q8), and
 * SAME pooling/normalization options as the browser-side chatbot.js, so the
 * vectors here are numerically identical to what the browser would compute.
 * Node has no WebGPU so we run on the CPU device via onnxruntime-node;
 * the q8 weights produce the same vectors regardless of execution provider.
 *
 * Output: docs/assets/chatbot_embeddings.bin  (~18 MB for ~6000 chunks)
 *
 * Binary format (all little-endian):
 *
 *   Header (52 bytes):
 *     magic        [4]    = "CMEB"
 *     version      u32    = 1
 *     count        u32    (total vectors)
 *     dim          u32    = 768
 *     dtype        u32    = 1 (float32)
 *     chunksHash   [32]   SHA-256 of all chunk texts concatenated in id order
 *
 *   Lang table (4 langs × 8 bytes, canonical order en, hk, tw, cn):
 *     offset       u32    (start index within the vector block, in vectors)
 *     count        u32    (number of vectors for this lang)
 *
 *   ids:           count × u32     (chunk id for each row, grouped by lang)
 *   vectors:       count × dim × f32  (mean-pooled + L2-normalized, grouped)
 *
 * Run AFTER scripts/build_chatbot_index.py whenever lesson content changes.
 * Usage:
 *   cd scripts && npm install && node build_chatbot_embeddings.mjs
 */

import { createHash } from "node:crypto";
import { readFile, writeFile, mkdir, readdir, rm, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, "..");
const CHUNKS_PATH = join(ROOT, "docs", "assets", "chatbot_chunks.json");
const OUT_PATH = join(ROOT, "docs", "assets", "chatbot_embeddings.bin");
// Per-language checkpoint cache so the script can resume across the
// harness's ~10-minute command timeout: each finished language is written
// here as raw float32 vectors + uint32 ids; re-runs load and skip them.
// Wipe with --clean.
const CACHE_DIR = join(ROOT, "docs", "assets", ".embed_cache");

const EMBED_MODEL_ID = "onnx-community/embeddinggemma-300m-ONNX";
// Canonical order in the final binary (must match the browser's
// EMBED_BIN_LANGS). The build processes langs smallest-first to minimise
// work lost if a run is killed mid-lang, but assembles the bin in this order.
const LANGS = ["en", "hk", "tw", "cn"];
const BATCH_SIZE = 16; // matches chatbot.js embedTexts()

const MAGIC = Buffer.from("CMEB", "ascii"); // 0x43 4D 45 42
const VERSION = 1;
const DTYPE_F32 = 1;
const HEADER_SIZE = 4 + 4 * 4 + 32; // magic + 4 u32 fields + 32-byte hash = 52
const LANG_TABLE_SIZE = LANGS.length * 8; // 4 langs × (u32 offset + u32 count)
const DIM = 768; // embeddinggemma-300m

// Encode a Float32 vector buffer and its ids as a single checkpoint file:
//   u32 count | u32 dim | count × u32 ids | count × dim × f32 vectors
function encodeCheckpoint(ids, vectors) {
  const n = ids.length;
  const buf = Buffer.alloc(8 + n * 4 + n * DIM * 4);
  buf.writeUInt32LE(n, 0);
  buf.writeUInt32LE(DIM, 4);
  for (let i = 0; i < n; i++) buf.writeUInt32LE(ids[i], 8 + i * 4);
  new Float32Array(buf.buffer, buf.byteOffset + 8 + n * 4, n * DIM).set(vectors);
  return buf;
}

function decodeCheckpoint(buf) {
  const n = buf.readUInt32LE(0);
  const dim = buf.readUInt32LE(4);
  if (dim !== DIM) throw new Error(`checkpoint dim ${dim} != ${DIM}`);
  const ids = [];
  for (let i = 0; i < n; i++) ids.push(buf.readUInt32LE(8 + i * 4));
  const vectors = new Float32Array(buf.buffer, buf.byteOffset + 8 + n * 4, n * DIM);
  return { ids, vectors: new Float32Array(vectors) }; // copy out of buffer
}

async function main() {
  const clean = process.argv.includes("--clean");
  console.log("Loading chunk index...");
  const chunks = JSON.parse(await readFile(CHUNKS_PATH, "utf8"));
  if (!Array.isArray(chunks) || chunks.length === 0) {
    throw new Error(`No chunks in ${CHUNKS_PATH}; run build_chatbot_index.py first.`);
  }
  console.log(`  ${chunks.length} chunks total`);

  // SHA-256 of every chunk text concatenated in ascending id order. The
  // browser recomputes this over the same texts and refuses a stale bin.
  const byIdAsc = [...chunks].sort((a, b) => a.id - b.id);
  const chunksHash = createHash("sha256")
    .update(byIdAsc.map((c) => c.text).join(""))
    .digest();
  console.log(`  chunks hash: ${chunksHash.toString("hex")}`);

  // Group chunks by lang in canonical order; within each, ascending id.
  const grouped = new Map(LANGS.map((l) => [l, []]));
  for (const c of chunks) {
    if (!grouped.has(c.lang)) {
      throw new Error(`Unknown lang '${c.lang}' on chunk id=${c.id}`);
    }
    grouped.get(c.lang).push(c);
  }
  for (const lang of LANGS) grouped.get(lang).sort((a, b) => a.id - b.id);

  // Checkpoint cache: skip langs we've already finished in a prior run.
  if (clean && existsSync(CACHE_DIR)) {
    await rm(CACHE_DIR, { recursive: true, force: true });
    console.log("  cleared checkpoint cache (--clean)");
  }
  await mkdir(CACHE_DIR, { recursive: true });

  // Embed each lang (smallest-first to minimise work lost to a kill),
  // writing a checkpoint after each fully-finished language. The model is
  // loaded lazily so a fully-cached re-run never touches the network.
  const langData = new Map(); // lang → { ids, vectors }
  for (const lang of LANGS) {
    const ckpt = join(CACHE_DIR, `${lang}.bin`);
    if (existsSync(ckpt)) {
      const data = decodeCheckpoint(await readFile(ckpt));
      langData.set(lang, data);
      console.log(`  ${lang}: cached (${data.ids.length} chunks)`);
    }
  }
  let extractor = null;
  const order = [...LANGS].sort((a, b) => grouped.get(a).length - grouped.get(b).length);
  for (const lang of order) {
    if (langData.has(lang)) continue;
    if (!extractor) {
      console.log("Loading embedding model (first run downloads ~300 MB)...");
      const { pipeline } = await import("@huggingface/transformers");
      extractor = await pipeline("feature-extraction", EMBED_MODEL_ID, {
        device: "cpu",
        dtype: "q8",
      });
      console.log("  model ready");
    }
    const subset = grouped.get(lang);
    const ids = new Uint32Array(subset.length);
    const vectors = new Float32Array(subset.length * DIM);
    for (let i = 0; i < subset.length; i += BATCH_SIZE) {
      const batch = subset.slice(i, i + BATCH_SIZE).map((c) => c.text);
      const result = await extractor(batch, { pooling: "mean", normalize: true });
      const data = result.data;
      if (data.length !== batch.length * DIM) {
        throw new Error(
          `Unexpected embedding shape for ${lang}: got ${data.length} floats, ` +
            `expected ${batch.length * DIM} (${batch.length} × ${DIM})`
        );
      }
      for (let j = 0; j < batch.length; j++) {
        ids[i + j] = subset[i + j].id;
        vectors.set(data.subarray(j * DIM, (j + 1) * DIM), (i + j) * DIM);
      }
      const done = Math.min(i + batch.length, subset.length);
      console.log(`  ${lang}: ${done}/${subset.length}`);
    }
    await writeFile(join(CACHE_DIR, `${lang}.bin`), encodeCheckpoint(ids, vectors));
    langData.set(lang, { ids, vectors });
    console.log(`  ${lang}: checkpoint saved`);
  }

  // Assemble the final binary in canonical LANGS order so each language's
  // rows are contiguous and the browser can slice them straight out.
  const totalCount = chunks.length;
  const allIds = new Uint32Array(totalCount);
  const allVectors = new Float32Array(totalCount * DIM);
  const langTable = [];
  let row = 0;
  for (const lang of LANGS) {
    const { ids, vectors } = langData.get(lang);
    allIds.set(ids, row);
    allVectors.set(vectors, row * DIM);
    langTable.push({ offset: row, count: ids.length });
    row += ids.length;
  }
  if (row !== totalCount) {
    throw new Error(`Row count mismatch: wrote ${row}, expected ${totalCount}`);
  }

  // Assemble the binary.
  const buf = Buffer.alloc(HEADER_SIZE + LANG_TABLE_SIZE + totalCount * 4 + totalCount * DIM * 4);
  let off = 0;
  MAGIC.copy(buf, off); off += 4;
  buf.writeUInt32LE(VERSION, off); off += 4;
  buf.writeUInt32LE(totalCount, off); off += 4;
  buf.writeUInt32LE(DIM, off); off += 4;
  buf.writeUInt32LE(DTYPE_F32, off); off += 4;
  chunksHash.copy(buf, off); off += 32;
  for (const { offset, count } of langTable) {
    buf.writeUInt32LE(offset, off); off += 4;
    buf.writeUInt32LE(count, off); off += 4;
  }
  for (let i = 0; i < totalCount; i++) buf.writeUInt32LE(allIds[i], off + i * 4);
  off += totalCount * 4;
  // Float32Array.view over the tail of the Buffer lets us memcpy in one shot.
  new Float32Array(buf.buffer, buf.byteOffset + off, totalCount * DIM).set(allVectors);

  await writeFile(OUT_PATH, buf);
  const sizeMb = buf.length / 1024 / 1024;
  console.log(`\nWrote ${OUT_PATH}`);
  console.log(`  ${totalCount} vectors × ${DIM} dims = ${sizeMb.toFixed(1)} MB`);
  langTable.forEach((lt, i) => {
    console.log(`    ${LANGS[i]}: ${lt.count} chunks`);
  });
}

main().catch((err) => {
  console.error("build_chatbot_embeddings failed:", err);
  process.exit(1);
});
