import React from 'react';
import {Composition} from 'remotion';
import {PodcastVideo} from './PodcastVideo';
import {Line} from './transcript';

import transcriptData from '../../week01_why_invest_transcript.json';
import envelopeData from '../../week01_loudness_envelope.json';
import audioSrc from '../../week01_why_invest.mp3';
import backgroundSrc from '../../assets/studio_background.png';
import horaceBody from '../../assets/characters/horace_body.png';
import horaceHeadBase from '../../assets/characters/horace_head_base.png';
import horaceHeadHalf from '../../assets/characters/horace_head_mouth_half.png';
import horaceHeadOpen from '../../assets/characters/horace_head_mouth_open.png';
import horaceHeadBlink from '../../assets/characters/horace_head_blink.png';
import stellaBody from '../../assets/characters/stella_body.png';
import stellaHeadBase from '../../assets/characters/stella_head_base.png';
import stellaHeadHalf from '../../assets/characters/stella_head_mouth_half.png';
import stellaHeadOpen from '../../assets/characters/stella_head_mouth_open.png';
import stellaHeadBlink from '../../assets/characters/stella_head_blink.png';
import stellaPonytail from '../../assets/characters/stella_ponytail.png';

const FPS = 30;
const lines = (transcriptData as {lines: Line[]}).lines;
const durationSecs = (transcriptData as {duration_secs: number}).duration_secs;

const week01Props = {
  lines,
  audioSrc,
  loudness: (envelopeData as {envelope: number[]}).envelope,
  backgroundSrc,
  horace: {
    body: horaceBody,
    headBase: horaceHeadBase,
    headHalf: horaceHeadHalf,
    headOpen: horaceHeadOpen,
    headBlink: horaceHeadBlink,
    neckPivot: {x: 795 / 1600, y: 950 / 1600},
  },
  stella: {
    body: stellaBody,
    headBase: stellaHeadBase,
    headHalf: stellaHeadHalf,
    headOpen: stellaHeadOpen,
    headBlink: stellaHeadBlink,
    ponytail: stellaPonytail,
    neckPivot: {x: 770 / 1600, y: 985 / 1600},
    tailPivot: {x: 865 / 1600, y: 155 / 1600},
  },
  weekLabel: 'WEEK 1',
  title: 'Why Invest?',
  subtitle: 'The textbook chart is a lie',
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Week01"
        component={PodcastVideo}
        durationInFrames={Math.ceil(durationSecs * FPS) + FPS}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={week01Props}
      />
      <Composition
        id="Week01Preview"
        component={PodcastVideo}
        durationInFrames={300}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={week01Props}
      />
    </>
  );
};
