import React from 'react';
import {Composition} from 'remotion';
import {PodcastVideo} from './PodcastVideo';
import {Line} from './transcript';

import transcriptData from '../../week01_why_invest_transcript.json';
import envelopeData from '../../week01_loudness_envelope.json';
import audioSrc from '../../week01_why_invest.mp3';
import transcriptDataW2 from '../../week02_index_funds_etfs_transcript.json';
import envelopeDataW2 from '../../week02_loudness_envelope.json';
import audioSrcW2 from '../../week02_index_funds_etfs.mp3';
import transcriptDataW3 from '../../week03_risk_and_return_transcript.json';
import envelopeDataW3 from '../../week03_loudness_envelope.json';
import audioSrcW3 from '../../week03_risk_and_return.mp3';
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

const horaceRig = {
  body: horaceBody,
  headBase: horaceHeadBase,
  headHalf: horaceHeadHalf,
  headOpen: horaceHeadOpen,
  headBlink: horaceHeadBlink,
  neckPivot: {x: 795 / 1600, y: 950 / 1600},
};

const stellaRig = {
  body: stellaBody,
  headBase: stellaHeadBase,
  headHalf: stellaHeadHalf,
  headOpen: stellaHeadOpen,
  headBlink: stellaHeadBlink,
  ponytail: stellaPonytail,
  neckPivot: {x: 770 / 1600, y: 985 / 1600},
  tailPivot: {x: 865 / 1600, y: 155 / 1600},
};

const week01Props = {
  lines,
  audioSrc,
  loudness: (envelopeData as {envelope: number[]}).envelope,
  backgroundSrc,
  horace: horaceRig,
  stella: stellaRig,
  weekLabel: 'WEEK 1',
  title: 'Why Invest?',
  subtitle: 'The textbook chart is a lie',
};

const linesW2 = (transcriptDataW2 as {lines: Line[]}).lines;
const durationSecsW2 = (transcriptDataW2 as {duration_secs: number})
  .duration_secs;

const week02Props = {
  lines: linesW2,
  audioSrc: audioSrcW2,
  loudness: (envelopeDataW2 as {envelope: number[]}).envelope,
  backgroundSrc,
  horace: horaceRig,
  stella: stellaRig,
  weekLabel: 'WEEK 2',
  title: 'Index Funds & ETFs',
  subtitle: 'The One ETF That Beats 90% of Wall Street',
  episode: 'week02' as const,
};

const linesW3 = (transcriptDataW3 as {lines: Line[]}).lines;
const durationSecsW3 = (transcriptDataW3 as {duration_secs: number})
  .duration_secs;

const week03Props = {
  lines: linesW3,
  audioSrc: audioSrcW3,
  loudness: (envelopeDataW3 as {envelope: number[]}).envelope,
  backgroundSrc,
  horace: horaceRig,
  stella: stellaRig,
  weekLabel: 'WEEK 3',
  title: 'Risk and Return',
  subtitle: 'The two forces \u2014 and the five-sigma lie',
  episode: 'week03' as const,
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
      <Composition
        id="Week02"
        component={PodcastVideo}
        durationInFrames={Math.ceil(durationSecsW2 * FPS) + FPS}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={week02Props}
      />
      <Composition
        id="Week02Preview"
        component={PodcastVideo}
        durationInFrames={300}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={week02Props}
      />
      <Composition
        id="Week03"
        component={PodcastVideo}
        durationInFrames={Math.ceil(durationSecsW3 * FPS) + FPS}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={week03Props}
      />
      <Composition
        id="Week03Preview"
        component={PodcastVideo}
        durationInFrames={300}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={week03Props}
      />
    </>
  );
};
