#!/usr/bin/env python3
"""Forced-align a podcast script to its generated MP3.

Produces:
  <base>_transcript.json  - per-line speaker turns with word-level timing
  <base>_transcript.srt   - subtitles (one cue per speaker turn)

Usage:
  align.py <script.txt> <audio.mp3> <out_base> [--model small]

The script must be in "Speaker: line" paragraphs (podcast-helper format).
Alignment is fuzzy (difflib on normalized word sequences) so minor
TTS/transcription differences don't break it.
"""
import json
import re
import sys
import unicodedata

from faster_whisper import WhisperModel

# Compat: faster-whisper passes metadata_errors="ignore" to av.open(),
# which PyAV >= 14 removed. Swallow the kwarg instead of pinning PyAV.
try:
    import av as _av

    _orig_av_open = _av.open

    def _av_open_compat(*a, **k):
        k.pop("metadata_errors", None)
        return _orig_av_open(*a, **k)

    _av.open = _av_open_compat
except ImportError:
    pass


def norm_word(w: str) -> str:
    w = unicodedata.normalize("NFKD", w).lower()
    w = re.sub(r"[^a-z0-9']", "", w)
    return w


def parse_script(path):
    """Return list of (speaker, text)."""
    turns = []
    with open(path, encoding="utf-8") as fh:
        for para in fh.read().strip().split("\n\n"):
            para = para.strip().replace("\n", " ")
            m = re.match(r"^([A-Za-z]+):\s*(.*)$", para)
            if not m:
                continue
            turns.append((m.group(1), m.group(2).strip()))
    return turns


def srt_time(s):
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    sec, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"


def main():
    script_path, audio_path, out_base = sys.argv[1:4]
    model_name = "small"
    for i, a in enumerate(sys.argv[4:]):
        if a == "--model":
            model_name = sys.argv[5 + i]

    print(f"Loading whisper model '{model_name}'...", flush=True)
    model = WhisperModel(model_name, device="cpu", compute_type="int8")

    print("Transcribing with word timestamps...", flush=True)
    segments, info = model.transcribe(audio_path, word_timestamps=True, language="en")
    twords = []  # (norm, start, end, raw)
    for seg in segments:
        for w in seg.words or []:
            nw = norm_word(w.word)
            if nw:
                twords.append((nw, w.start, w.end, w.word.strip()))
    print(f"Transcript: {len(twords)} words, detected duration {info.duration:.1f}s", flush=True)
    if not twords:
        sys.exit("No words transcribed; aborting.")

    turns = parse_script(script_path)
    print(f"Script: {len(turns)} speaker turns", flush=True)

    # Flatten script words, remembering which turn/word each belongs to.
    script_words = []   # normalized
    script_raw = []     # display form
    word_turn = []      # turn index per script word
    for ti, (spk, text) in enumerate(turns):
        for raw in text.split():
            nw = norm_word(raw)
            if nw:
                script_words.append(nw)
                script_raw.append(raw)
                word_turn.append(ti)

    import difflib
    sm = difflib.SequenceMatcher(None,
                                 [w for w, _, _, _ in twords],
                                 script_words, autojunk=False)
    # Map each script-word index -> transcript word index.
    align = {}
    for a, b, size in sm.get_matching_blocks():
        for k in range(size):
            align[b + k] = a + k

    # Fill gaps by interpolation between aligned neighbors.
    n = len(script_words)
    aligned_idx = sorted(align)
    t_starts = [s for _, s, _, _ in twords]
    t_ends = [e for _, _, e, _ in twords]
    T = len(twords)

    def tpos_at(si):
        # transcript float position for script word si
        if si in align:
            return float(align[si])
        # find surrounding aligned script words
        prev = next((a for a in reversed(aligned_idx) if a < si), None)
        nxt = next((a for a in aligned_idx if a > si), None)
        if prev is None:
            return float(align[nxt]) - (nxt - si) if nxt is not None else 0.0
        if nxt is None:
            return float(align[prev]) + (si - prev)
        frac = (si - prev) / (nxt - prev)
        return align[prev] + frac * (align[nxt] - align[prev])

    def time_at(pos, use_end=False):
        arr = t_ends if use_end else t_starts
        if pos <= 0:
            return arr[0]
        if pos >= T - 1:
            return arr[T - 1]
        lo = int(pos)
        frac = pos - lo
        return arr[lo] * (1 - frac) + arr[min(lo + 1, T - 1)] * frac

    # Build per-turn output with word timings.
    lines_out = []
    for ti, (spk, text) in enumerate(turns):
        idxs = [i for i in range(n) if word_turn[i] == ti]
        if not idxs:
            continue
        words_out = []
        for si in idxs:
            p0, p1 = tpos_at(si), tpos_at(si + 1) if si + 1 < n else tpos_at(si) + 1
            ws = time_at(p0, use_end=False)
            we = time_at(min(p1, p0 + 1.5), use_end=True)
            if we < ws:
                we = ws + 0.05
            words_out.append({"w": script_raw[si], "start": round(ws, 2), "end": round(we, 2)})
        lines_out.append({
            "speaker": spk,
            "text": text,
            "start": words_out[0]["start"],
            "end": words_out[-1]["end"],
            "words": words_out,
        })

    matched = len(align)
    print(f"Aligned {matched}/{n} script words "
          f"({100.0 * matched / n:.1f}%) to transcript", flush=True)

    with open(out_base + "_transcript.json", "w", encoding="utf-8") as fh:
        json.dump({
            "audio": audio_path.split("/")[-1],
            "duration_secs": round(info.duration, 1),
            "model": f"faster-whisper/{model_name}",
            "lines": lines_out,
        }, fh, ensure_ascii=False, indent=1)

    with open(out_base + "_transcript.srt", "w", encoding="utf-8") as fh:
        for i, L in enumerate(lines_out, 1):
            fh.write(f"{i}\n{srt_time(L['start'])} --> {srt_time(L['end'])}\n"
                     f"[{L['speaker']}] {L['text']}\n\n")

    print(f"Wrote {out_base}_transcript.json and {out_base}_transcript.srt", flush=True)


if __name__ == "__main__":
    main()
