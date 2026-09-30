import React from 'react';
import {Composition} from 'remotion';
import {PodcastVideo} from './PodcastVideo';
import {Line} from './transcript';

import transcriptData from '../../week01_why_invest_transcript.json';
import audioSrc from '../../week01_why_invest.mp3';
import backgroundSrc from '../../assets/studio_background.png';
import horaceBase from '../../assets/characters/horace_base_cutout.png';
import horaceHalf from '../../assets/characters/horace_mouth_half_cutout.png';
import horaceOpen from '../../assets/characters/horace_mouth_open_cutout.png';
import horaceBlink from '../../assets/characters/horace_blink_cutout.png';
import stellaBase from '../../assets/characters/stella_base_cutout.png';
import stellaHalf from '../../assets/characters/stella_mouth_half_cutout.png';
import stellaOpen from '../../assets/characters/stella_mouth_open_cutout.png';
import stellaBlink from '../../assets/characters/stella_blink_cutout.png';

const FPS = 30;
const lines = (transcriptData as {lines: Line[]}).lines;
const durationSecs = (transcriptData as {duration_secs: number}).duration_secs;

const week01Props = {
  lines,
  audioSrc,
  backgroundSrc,
  horace: {base: horaceBase, half: horaceHalf, open: horaceOpen, blink: horaceBlink},
  stella: {base: stellaBase, half: stellaHalf, open: stellaOpen, blink: stellaBlink},
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
