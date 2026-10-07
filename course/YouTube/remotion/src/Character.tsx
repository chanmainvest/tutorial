import React from 'react';
import {Img, useCurrentFrame, useVideoConfig} from 'remotion';
import {Line, getLineAt} from './transcript';

/**
 * Layered host rig (sprites built by assets/make_rig.py, all 1600x1600
 * and pixel-aligned):
 *  - body: torso only, NEVER moves (the old whole-portrait bob made
 *    everything wobble, name tag included)
 *  - head: pivots at the neck — small nods/tilts while talking
 *  - ponytail (Stella): nested inside the head group so it inherits
 *    the head motion, plus its own lagged pendulum sway at the tie
 * The name pill lives outside every moving layer.
 */
export interface HostRig {
  body: string;
  headBase: string;
  headHalf: string;
  headOpen: string;
  headBlink: string;
  ponytail?: string;
  /** Neck pivot, as fractions of the square sprite canvas. */
  neckPivot: {x: number; y: number};
  /** Ponytail tie pivot, as fractions of the canvas. */
  tailPivot?: {x: number; y: number};
}

const BLINK_FRAMES = 4;

// Calibrated from the episode mp3: RMS over a 120ms window, every 4th
// sample, averaged across channels. p25 (pauses) ~0.003, p50 ~0.021,
// p75 ~0.052. Precomputed offline (see week01_loudness_envelope.json)
// so the browser never holds the decoded 69MB waveform.
const MOUTH_HALF_THRESHOLD = 0.012;
const MOUTH_OPEN_THRESHOLD = 0.045;

function hashStr(s: string): number {
  let h = 0;
  for (let i = 0; i < s.length; i++) {
    h = (h * 31 + s.charCodeAt(i)) >>> 0;
  }
  return h;
}

export const Character: React.FC<{
  /** Must match the `speaker` field in the transcript JSON. */
  speaker: string;
  displayName: string;
  role: string;
  rig: HostRig;
  lines: Line[];
  /** Precomputed per-frame voice loudness (one value per frame at 30fps). */
  loudness: number[];
  /** Horizontal center of the character, in px (1920-wide canvas). */
  x: number;
  /** Rendered width of the (square) character canvas, in px. */
  width: number;
  /** Signed px this host slides outward when recessed (diagrams up),
   * so the pair parts and leaves the center to the chart. */
  apart?: number;
  /** When a diagram takes the stage, hosts shrink slightly to make room. */
  recessed?: boolean;
}> = ({speaker, displayName, role, rig, lines, loudness, x, width, apart = 0, recessed}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const seed = hashStr(speaker);
  const phase1 = (seed % 628) / 100;
  const phase2 = (seed % 377) / 100;
  const phase3 = (seed % 211) / 100;

  const line = getLineAt(lines, t);
  const isActive = line !== null && line.speaker === speaker;

  // --- Mouth: driven by the real voice amplitude, not a timer ---
  // Only the active speaker's mouth moves (single mixed track, so gate
  // on the transcript's speaker turns). Pauses read as closed mouth.
  const loud = isActive && frame < loudness.length ? loudness[frame] : 0;
  let headSrc = rig.headBase;
  if (loud > MOUTH_OPEN_THRESHOLD) {
    headSrc = rig.headOpen;
  } else if (loud > MOUTH_HALF_THRESHOLD) {
    headSrc = rig.headHalf;
  }

  // --- Blink: every ~3.5-5.5s for 4 frames (~130ms), both hosts,
  // speaking or not — just never mid wide-open mouth, where swapping
  // to the closed-mouth blink sprite would glitch. ---
  const blinkCycle = 105 + (seed % 60);
  if (loud <= MOUTH_OPEN_THRESHOLD && frame % blinkCycle < BLINK_FRAMES) {
    headSrc = rig.headBlink;
  }

  // --- Head motion: pivots at the neck; the body never moves ---
  // Louder voice = slightly bigger nods (energy 0.75x-1.25x).
  const energy = 0.75 + Math.min(loud * 7, 0.5);
  let headRot: number;
  let headBobY: number;
  if (isActive) {
    headRot =
      (Math.sin(t * Math.PI * 2 * 0.85 + phase1) * 1.15 +
        Math.sin(t * Math.PI * 2 * 0.37 + phase2) * 0.55) *
      energy;
    headBobY = Math.sin(t * Math.PI * 2 * 0.85 + phase1) * 3 * energy;
  } else {
    headRot = Math.sin(t * Math.PI * 2 * 0.3 + phase1) * 0.5;
    headBobY = Math.sin(t * Math.PI * 2 * 0.3 + phase1) * 1;
  }

  // --- Ponytail: pendulum lagging the head nod, plus an idle sway ---
  const tailSway = isActive
    ? Math.sin(t * Math.PI * 2 * 0.85 + phase1 - 0.9) * 1.5 * energy +
      Math.sin(t * Math.PI * 2 * 0.45 + phase3) * 0.6
    : Math.sin(t * Math.PI * 2 * 0.45 + phase3) * 0.9;

  const dim = isActive ? 'none' : 'brightness(0.8) saturate(0.9)';
  const layerImg: React.CSSProperties = {
    position: 'absolute',
    inset: 0,
    width: '100%',
    height: '100%',
    display: 'block',
  };

  return (
    <div
      style={{
        position: 'absolute',
        left: x - width / 2,
        bottom: -40, // waist-up crop: torso runs just off-frame
        width,
        // Only per-state transforms (diagram recess: shrink + slide
        // apart) — never per-frame, so the body and the name pill
        // stay rock still.
        transform: `translateX(${recessed ? apart : 0}px) scale(${recessed ? 0.85 : 1})`,
        transformOrigin: '50% 100%',
        transition: 'transform 0.4s',
      }}
    >
      <div style={{position: 'relative', width: '100%', aspectRatio: '1 / 1'}}>
        <Img src={rig.body} style={{...layerImg, filter: dim, transition: 'filter 0.3s'}} />
        <div
          style={{
            position: 'absolute',
            inset: 0,
            transform: `translateY(${headBobY}px) rotate(${headRot}deg)`,
            transformOrigin: `${rig.neckPivot.x * 100}% ${rig.neckPivot.y * 100}%`,
            filter: dim,
            transition: 'filter 0.3s',
          }}
        >
          {rig.ponytail && rig.tailPivot ? (
            <div
              style={{
                position: 'absolute',
                inset: 0,
                transform: `rotate(${tailSway}deg)`,
                transformOrigin: `${rig.tailPivot.x * 100}% ${rig.tailPivot.y * 100}%`,
              }}
            >
              <Img src={rig.ponytail} style={layerImg} />
            </div>
          ) : null}
          <Img src={headSrc} style={layerImg} />
        </div>
      </div>
      {/* Name pill — outside every moving layer, always still */}
      <div
        style={{
          position: 'absolute',
          left: '50%',
          bottom: 24,
          transform: 'translateX(-50%)',
          backgroundColor: 'rgba(20,16,10,0.72)',
          color: '#fff',
          borderRadius: 999,
          padding: '10px 26px',
          fontFamily: 'Inter, system-ui, sans-serif',
          fontSize: 30,
          fontWeight: 700,
          letterSpacing: 1,
          whiteSpace: 'nowrap',
        }}
      >
        {displayName} <span style={{opacity: 0.65, fontWeight: 400}}>· {role}</span>
      </div>
    </div>
  );
};
