#!/usr/bin/env python3
"""Build the chatbot RAG index.

Walks every lesson markdown across the four locales, strips the YouTube
script section (Part 2), splits the reading section into ~600-character
chunks with 100-character overlap, and writes a single
``docs/assets/chatbot_chunks.json`` containing records of the form::

    {"id": int, "lang": "en|hk|tw|cn", "url": "weekNN.html",
     "title": "Week N: Topic", "text": "<chunk>"}

The browser-side chatbot fetches this file, embeds chunks via an in-page
embedding model (transformers.js), caches the embeddings in IndexedDB,
and uses cosine similarity to retrieve the top-K most relevant chunks
for each user question. Embedding is *not* done here so that this build
step has no Python ML dependencies — pure stdlib.

Usage: uv run python scripts/build_chatbot_index.py
"""

import json
import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(PROJECT_ROOT, "docs", "assets", "chatbot_chunks.json")

LOCALES = {
    "en": "course",
    "hk": "course_hk",
    "tw": "course_tw",
    "cn": "course_cn",
}

CHUNK_SIZE = 600       # characters per chunk
CHUNK_OVERLAP = 100    # overlap between consecutive chunks


# ---------------------------------------------------------------------------
# Markdown helpers (mirrored from scripts/build.py so the chunks the chatbot
# sees match what the website displays)
# ---------------------------------------------------------------------------
def strip_youtube_section(md: str) -> str:
    """Strip Part 2 (YouTube Script) regardless of locale."""
    pattern = r"\n---\s*\n\s*##[^\n]*[Yy]ou[Tt]ube[^\n]*\n.*"
    return re.sub(pattern, "", md, flags=re.DOTALL)


def extract_title(md: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else "Untitled"


def normalise_text(md: str) -> str:
    """Strip code fences, inline html, image refs, and excess whitespace.

    The chatbot only needs natural-language prose for embedding-based
    retrieval. Stripping markdown sigils keeps each chunk denser and
    avoids polluting embeddings with `![](image.png)` noise.
    """
    text = md
    # Drop fenced code blocks entirely
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Drop image references
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    # Convert markdown links [label](url) -> label
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    # Strip leading markdown sigils (##, *, -, >, etc.) but keep the text
    text = re.sub(r"^[#>\-*]+\s+", "", text, flags=re.MULTILINE)
    # Collapse runs of whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Filename → URL slug
# ---------------------------------------------------------------------------
def slug_for(filename: str) -> str | None:
    """Map a course markdown filename to the published page slug.

    Returns None for files that don't appear in the navigation
    (e.g. unmatched files, draft notes).
    """
    base = os.path.splitext(filename)[0]
    if base == "overview":
        return "index"
    if re.fullmatch(r"level[1-5]_overview", base):
        return base.replace("_overview", "")
    m = re.match(r"week(\d{1,2})_", base)
    if m:
        return f"week{int(m.group(1)):02d}"
    m = re.match(r"side(\d{1,2})_", base)
    if m:
        return f"side{int(m.group(1)):02d}"
    if base in {"faq", "disclaimer"}:
        return base
    return None


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------
def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping windows. Tries to break on sentence /
    paragraph boundaries when possible to avoid mid-word cuts; falls
    back to hard cuts when no boundary is nearby.
    """
    if len(text) <= size:
        return [text] if text.strip() else []

    chunks: list[str] = []
    step = max(1, size - overlap)
    i = 0
    while i < len(text):
        end = min(i + size, len(text))
        # Try to extend to the next sentence / paragraph boundary within
        # ~80 chars of the hard end, so we don't slice mid-word.
        if end < len(text):
            window = text[end:end + 80]
            for boundary in ("\n\n", "。", "！", "？", ". ", "! ", "? ", "\n"):
                idx = window.find(boundary)
                if 0 <= idx < 80:
                    end = end + idx + len(boundary)
                    break
        chunk = text[i:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        i = max(i + step, end - overlap)
    return chunks


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def collect_chunks() -> list[dict]:
    records: list[dict] = []
    next_id = 0

    for lang, dirname in LOCALES.items():
        course_dir = os.path.join(PROJECT_ROOT, dirname)
        if not os.path.isdir(course_dir):
            print(f"  warn: missing locale directory {dirname}/, skipping", file=sys.stderr)
            continue

        files = sorted(f for f in os.listdir(course_dir) if f.endswith(".md"))
        lang_chunks = 0
        for filename in files:
            slug = slug_for(filename)
            if slug is None:
                continue
            path = os.path.join(course_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                md = f.read()
            md = strip_youtube_section(md)
            title = extract_title(md)
            body = normalise_text(md)
            for chunk in chunk_text(body):
                records.append({
                    "id": next_id,
                    "lang": lang,
                    "url": f"{slug}.html",
                    "title": title,
                    "text": chunk,
                })
                next_id += 1
                lang_chunks += 1
        print(f"  {lang}: {len(files)} files -> {lang_chunks} chunks")

    return records


def main():
    print(f"Building chatbot RAG index at {OUT_PATH}")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    records = collect_chunks()
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, separators=(",", ":"))
    size_mb = os.path.getsize(OUT_PATH) / 1024 / 1024
    print(f"\nWrote {len(records)} chunks across {len(LOCALES)} locales ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
