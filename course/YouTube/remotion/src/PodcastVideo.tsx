import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {Character, HostImages} from './Character';
import {Line, getLineAt} from './transcript';

const FONT = 'Inter, system-ui, -apple-system, sans-serif';

const Caption: React.FC<{lines: Line[]}> = ({lines}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const line = getLineAt(lines, frame / fps);
  if (!line) {
    return null;
  }
  return (
    <div
      style={{
        position: 'absolute',
        bottom: 56,
        left: '50%',
        transform: 'translateX(-50%)',
        maxWidth: 1050,
        backgroundColor: 'rgba(15,12,8,0.62)',
        color: '#fff',
        borderRadius: 18,
        padding: '18px 34px',
        fontFamily: FONT,
        fontSize: 38,
        lineHeight: 1.45,
        textAlign: 'center',
      }}
    >
      {line.text}
    </div>
  );
};

const IntroTitle: React.FC<{weekLabel: string; title: string; subtitle: string}> = ({
  weekLabel,
  title,
  subtitle,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  // Visible ~0-4.5s, fading in and out.
  const opacity = interpolate(
    frame,
    [0, 0.6 * fps, 3.6 * fps, 4.5 * fps],
    [0, 1, 1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );
  if (opacity === 0) {
    return null;
  }
  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'rgba(12,10,7,0.45)',
        opacity,
      }}
    >
      <div
        style={{
          fontFamily: FONT,
          fontSize: 44,
          fontWeight: 800,
          letterSpacing: 8,
          color: '#f5c518',
          marginBottom: 18,
        }}
      >
        {weekLabel}
      </div>
      <div
        style={{
          fontFamily: FONT,
          fontSize: 96,
          fontWeight: 800,
          color: '#fff',
          marginBottom: 14,
        }}
      >
        {title}
      </div>
      <div style={{fontFamily: FONT, fontSize: 44, color: 'rgba(255,255,255,0.85)'}}>
        {subtitle}
      </div>
    </div>
  );
};

export const PodcastVideo: React.FC<{
  lines: Line[];
  audioSrc: string;
  backgroundSrc: string;
  horace: HostImages;
  stella: HostImages;
  weekLabel: string;
  title: string;
  subtitle: string;
}> = ({lines, audioSrc, backgroundSrc, horace, stella, weekLabel, title, subtitle}) => {
  return (
    <AbsoluteFill style={{backgroundColor: '#14100b'}}>
      <Img
        src={backgroundSrc}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
      {/* soft vignette so hosts pop */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at center, transparent 55%, rgba(10,8,5,0.42) 100%)',
        }}
      />
      <Character
        speaker="Horace"
        displayName="Horace"
        role="Teacher"
        images={horace}
        lines={lines}
        x={440}
        width={560}
        leanDir={1}
      />
      <Character
        speaker="Stella"
        displayName="Stella"
        role="Student"
        images={stella}
        lines={lines}
        x={1480}
        width={560}
        leanDir={-1}
      />
      {/* episode badge */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: '50%',
          transform: 'translateX(-50%)',
          backgroundColor: 'rgba(20,16,10,0.6)',
          color: '#f5c518',
          borderRadius: 999,
          padding: '10px 30px',
          fontFamily: FONT,
          fontSize: 28,
          fontWeight: 700,
          letterSpacing: 3,
        }}
      >
        {weekLabel}
      </div>
      <Caption lines={lines} />
      <IntroTitle weekLabel={weekLabel} title={title} subtitle={subtitle} />
      <Audio src={audioSrc} />
    </AbsoluteFill>
  );
};
