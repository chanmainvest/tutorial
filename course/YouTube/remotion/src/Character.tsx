import React from 'react';
import {Img, useCurrentFrame, useVideoConfig} from 'remotion';
import {Line, getLineAt, isWordSounding} from './transcript';

export interface HostImages {
  base: string;
  half: string;
  open: string;
  blink: string;
}

const BLINK_FRAMES = 5;

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
  images: HostImages;
  lines: Line[];
  /** Horizontal center of the character, in px (1920-wide canvas). */
  x: number;
  /** Rendered width of the character image, in px. */
  width: number;
  /** +1 leans right (left-side host), -1 leans left (right-side host). */
  leanDir: 1 | -1;
}> = ({speaker, displayName, role, images, lines, x, width, leanDir}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;

  const line = getLineAt(lines, t);
  const isActive = line !== null && line.speaker === speaker;
  const sounding = isWordSounding(lines, speaker, t);

  // --- Mouth: flap base/half/open while a word is sounding ---
  const flapPhase = Math.floor(frame / 2.5) % 2; // ~12 fps alternation
  let src = images.base;
  if (sounding) {
    src = flapPhase === 0 ? images.half : images.open;
  }

  // --- Blink: every 4-7s, a few frames, never mid-word ---
  const blinkCycle = 120 + (hashStr(speaker) % 90);
  if (!sounding && frame % blinkCycle < BLINK_FRAMES) {
    src = images.blink;
  }

  // --- Procedural body language ---
  const bob = isActive
    ? Math.sin(t * Math.PI * 2 * 1.4) * 7
    : Math.sin(t * Math.PI * 2 * 0.9) * 3;
  const tilt = isActive ? Math.sin(t * Math.PI * 2 * 0.7) * 1.6 : 0;
  const breathe = 1 + 0.008 * Math.sin(t * Math.PI * 2 * 0.25);
  const lean = isActive ? 14 * leanDir : 0;
  const scale = breathe * (isActive ? 1.015 : 0.97);

  return (
    <div
      style={{
        position: 'absolute',
        left: x - width / 2 + lean,
        bottom: -40, // waist-up crop: torso runs just off-frame
        width,
        transform: `translateY(${bob}px) rotate(${tilt}deg) scale(${scale})`,
        transformOrigin: '50% 100%',
        filter: isActive
          ? 'none'
          : 'brightness(0.8) saturate(0.9)',
        transition: 'filter 0.3s',
      }}
    >
      <Img src={src} style={{width: '100%', display: 'block'}} />
      {/* Name pill */}
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
