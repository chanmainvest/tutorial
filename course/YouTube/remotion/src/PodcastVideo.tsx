import React, {useMemo} from 'react';
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {Character, HostRig} from './Character';
import {DIAGRAM_TIMELINE, Diagrams} from './Diagrams';
import {DIAGRAM_TIMELINE_WEEK02, DiagramsWeek02} from './DiagramsWeek02';
import {DIAGRAM_TIMELINE_WEEK03, DiagramsWeek03} from './DiagramsWeek03';
import {CaptionCue, Line, buildCaptionCues, getCaptionAt} from './transcript';

const FONT = 'Inter, system-ui, -apple-system, sans-serif';

const Caption: React.FC<{cues: CaptionCue[]}> = ({cues}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const cue = getCaptionAt(cues, frame / fps);
  if (!cue) {
    return null;
  }
  return (
    <div
      style={{
        position: 'absolute',
        bottom: 48,
        left: '50%',
        transform: 'translateX(-50%)',
        maxWidth: 1240,
        backgroundColor: 'rgba(15,12,8,0.66)',
        color: '#fff',
        borderRadius: 14,
        padding: '14px 30px',
        fontFamily: FONT,
        fontSize: 40,
        lineHeight: 1.3,
        textAlign: 'center',
        whiteSpace: 'nowrap',
      }}
    >
      {cue.text}
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
  /** Precomputed per-frame voice loudness (one value per frame at 30fps). */
  loudness: number[];
  backgroundSrc: string;
  horace: HostRig;
  stella: HostRig;
  weekLabel: string;
  title: string;
  subtitle: string;
  /** Which episode's diagram set to show (default: week01). */
  episode?: 'week01' | 'week02' | 'week03';
}> = ({lines, audioSrc, loudness, backgroundSrc, horace, stella, weekLabel, title, subtitle, episode = 'week01'}) => {
  const cues = useMemo(() => buildCaptionCues(lines), [lines]);

  // Hosts step back (shrink slightly) while a diagram takes the stage.
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const timeline =
    episode === 'week03'
      ? DIAGRAM_TIMELINE_WEEK03
      : episode === 'week02'
        ? DIAGRAM_TIMELINE_WEEK02
        : DIAGRAM_TIMELINE;
  const diagramActive = timeline.some(
    (s) => frame / fps >= s.start && frame / fps < s.end,
  );

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
        rig={horace}
        lines={lines}
        loudness={loudness}
        x={440}
        width={650}
        apart={-130}
        recessed={diagramActive}
      />
      <Character
        speaker="Stella"
        displayName="Stella"
        role="Student"
        rig={stella}
        lines={lines}
        loudness={loudness}
        x={1480}
        width={650}
        apart={130}
        recessed={diagramActive}
      />
      {episode === 'week03' ? (
        <DiagramsWeek03 />
      ) : episode === 'week02' ? (
        <DiagramsWeek02 />
      ) : (
        <Diagrams />
      )}
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
      <Caption cues={cues} />
      <IntroTitle weekLabel={weekLabel} title={title} subtitle={subtitle} />
      <Audio src={audioSrc} />
    </AbsoluteFill>
  );
};
