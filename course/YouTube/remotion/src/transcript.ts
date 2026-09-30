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
