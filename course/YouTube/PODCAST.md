# Podcast workflow — course YouTube audio

Each lesson can have a two-voice podcast episode generated from its YouTube
script. Week 1 is the reference implementation. Files involved:

| File | Purpose |
|---|---|
| `course/YouTube/week01_why_invest.md` | Original YouTube video script (visual cues, two hosts) |
| `course/YouTube/week01_why_invest_podcast.txt` | **Spoken-form podcast script — edit this to change the audio.** `Speaker: line` paragraphs, no stage directions, numbers spelled out ("forty-two million", "S and P five hundred", "C P I") |
| `course/YouTube/week01_why_invest.mp3` | Generated episode audio |
| `course/YouTube/week01_why_invest_transcript.json` | Word-level timing: per speaker turn `{speaker, text, start, end, words: [{w, start, end}]}` — for slideshow / talking-head builds |
| `course/YouTube/week01_why_invest_transcript.srt` | Same turns as subtitles |
| `scripts/align_podcast.py` | Forced-alignment tool (faster-whisper transcription + fuzzy match to script) |

## Voices (pinned — do not change)

Same voice = same `--speaker` voice id, every time. Host names are the
show's characters; the voice ids are what keep them sounding identical.

- **Horace** → `avocado_v2:MAI_03` (Meta AI "Helio", masculine)
- **Stella** → `avocado_v2:MAI_01` (Meta AI "Aria", feminine)

These pairings are also recorded in the assistant's memory. New lessons
reuse Horace/Stella so the whole series sounds like one show.

## Regenerating the audio after editing the script

1. Edit `course/YouTube/week01_why_invest_podcast.txt`. Keep the
   `Horace:` / `Stella:` paragraph format. Write for the ear:
   spell out numbers ("twenty twenty-six", "three point five percent"),
   spell out abbreviations ("C P I", "E T F s"→"E T Fs" reads as letters),
   full sentences, no `(pause)` / `[VISUAL]` / `---` / emoji.
2. Generate (from the repo root):
   ```sh
   podcast-helper generate \
     --script course/YouTube/week01_why_invest_podcast.txt \
     --title "Why Invest? The Textbook Chart Is a Lie" \
     --description "<one or two sentences on the episode>" \
     --speaker Horace=avocado_v2:MAI_03 \
     --speaker Stella=avocado_v2:MAI_01 \
     --cover-prompt "<short visual description of the episode theme>" \
     --topics-file /tmp/topics.md
   ```
   Write `/tmp/topics.md` first: a few bullets of what the episode covers
   (used for dedup against future episodes). Do **not** pass `--publish`
   unless the episode should go to the public RSS feed.
3. The output lands in `~/workspace/podcasts/<slug>/<slug>.mp3`.
   Copy it over the repo file, keeping the stable name:
   ```sh
   cp ~/workspace/podcasts/<slug>/<slug>.mp3 \
      course/YouTube/week01_why_invest.mp3
   ```
4. Rebuild the word-level transcript (needs the whisper venv; create once
   with `python3 -m venv ~/workspace/venvs/whisper` then
   `~/workspace/venvs/whisper/bin/pip install faster-whisper`):
   ```sh
   ~/workspace/venvs/whisper/bin/python scripts/align_podcast.py \
     course/YouTube/week01_why_invest_podcast.txt \
     course/YouTube/week01_why_invest.mp3 \
     course/YouTube/week01_why_invest --model small
   ```
   This rewrites `week01_why_invest_transcript.json` and `.srt`.
   (If the model download fails behind the proxy, retry with
   `env -u NO_PROXY -u no_proxy` — httpx chokes on the IPv6 `no_proxy`
   entries.)

## Starting a new lesson's episode

1. Condense `course/YouTube/<lesson>.md` into a spoken two-host script;
   save as `course/YouTube/<lesson>_podcast.txt` (≈130 words/minute,
   10–15 min target).
2. Generate with the same `--speaker` flags above and a per-episode
   `--cover-prompt`; save the MP3 as `course/YouTube/<lesson>.mp3`.
3. Run `scripts/align_podcast.py` to produce the transcript files.

## Notes

- `podcast-helper` does not emit timestamps itself; the `.json`/`.srt`
  files are the timing source for any slideshow or talking-head build.
- The MP3s are committed to the repo alongside the scripts (like the
  `image/` PNGs) — they are part of the lesson, not build artifacts.
  `scripts/build.py` ignores them (it only reads `.md` lesson files).

## Talking-head video (Remotion)

`remotion/` holds the Remotion project that turns the episode audio +
transcript into a talking-head video: studio background, Horace & Stella
as transparent cutouts (`assets/characters/*_cutout.png`), mouth movement
driven by the word-level transcript, blinking, head bob, speaker focus,
captions, and an intro title. See `remotion/README.md` for render commands
and how to add a new episode.
