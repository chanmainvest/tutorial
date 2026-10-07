export interface Word {
  w: string;
  start: number;
  end: number;
}

export interface Line {
  speaker: string;
  text: string;
  start: number;
  end: number;
  words: Word[];
}

/** The transcript line sounding at time t (seconds), or null in gaps. */
export function getLineAt(lines: Line[], t: number): Line | null {
  for (const line of lines) {
    if (t >= line.start && t <= line.end) {
      return line;
    }
  }
  return null;
}

/** True while the given speaker has a word actually sounding at t. */
export function isWordSounding(
  lines: Line[],
  speaker: string,
  t: number,
): boolean {
  const line = getLineAt(lines, t);
  if (!line || line.speaker !== speaker) {
    return false;
  }
  return line.words.some((w) => t >= w.start && t <= w.end);
}

export interface CaptionCue {
  text: string;
  start: number;
  end: number;
}

const MAX_CAPTION_WORDS = 7;
const MAX_CAPTION_CHARS = 44;

/**
 * Split transcript lines into one-line caption cues, chunked on word
 * boundaries using the word-level timings. Each cue holds until just
 * before the next one starts so there are no dead gaps mid-sentence.
 */
export function buildCaptionCues(lines: Line[]): CaptionCue[] {
  const cues: CaptionCue[] = [];
  for (const line of lines) {
    let cur: Word[] = [];
    let curLen = 0;
    const flush = () => {
      if (cur.length === 0) {
        return;
      }
      cues.push({
        text: cur.map((w) => w.w).join(' '),
        start: cur[0].start,
        end: cur[cur.length - 1].end,
      });
      cur = [];
      curLen = 0;
    };
    for (const w of line.words) {
      const addLen = (cur.length > 0 ? 1 : 0) + w.w.length;
      if (cur.length >= MAX_CAPTION_WORDS || curLen + addLen > MAX_CAPTION_CHARS) {
        flush();
      }
      cur.push(w);
      curLen += addLen;
    }
    flush();
  }
  for (let i = 0; i < cues.length; i++) {
    const next = cues[i + 1];
    cues[i].end = next
      ? Math.min(cues[i].end + 0.3, next.start - 0.02)
      : cues[i].end + 0.6;
  }
  return cues;
}

/** The caption cue visible at time t (seconds), or null. */
export function getCaptionAt(cues: CaptionCue[], t: number): CaptionCue | null {
  for (const c of cues) {
    if (t >= c.start && t <= c.end) {
      return c;
    }
  }
  return null;
}
