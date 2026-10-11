import React from 'react';
import {Img, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

import returnDistSrc from '../../../../image/week03_return_distribution.png';
import drawdownsSrc from '../../../../image/week03_drawdowns.png';
import holdingSrc from '../../../../image/week03_holding_periods.png';
import marksSrc from '../../../../image/week03_marks_risk_distribution.png';

const FONT = 'Inter, system-ui, -apple-system, sans-serif';
const GOLD = '#f5c518';
const DIM = 'rgba(255,255,255,0.62)';
const RED = '#e5484d';
const GREEN = '#46a758';
const BLUE = '#3e8ef7';
const AMBER = '#f0a020';

type DiagramId =
  | 'ranges'
  | 'fattails'
  | 'regimes'
  | 'diversify'
  | 'drawdowns'
  | 'holding'
  | 'capacity'
  | 'marks'
  | 'recovery'
  | 'outro';

interface DiagramSlot {
  id: DiagramId;
  start: number; // seconds
  end: number; // seconds
  title: string;
}

/**
 * Week 3 visual-learning overlays, timed to the Week 3 transcript.
 * Four slots are the lesson's own matplotlib charts (image cards); the
 * rest are animated SVG diagrams in the Week 1/2 style. The script's two
 * pre-made animation cues (definitions, diversification) are realised
 * here as the `ranges` and `diversify` SVG diagrams.
 */
export const DIAGRAM_TIMELINE_WEEK03: DiagramSlot[] = [
  {id: 'ranges', start: 43, end: 79, title: 'Risk is a range of outcomes'},
  {id: 'fattails', start: 82, end: 127, title: 'The bell curve that isn’t'},
  {id: 'regimes', start: 193, end: 246, title: 'Three regimes, three averages'},
  {id: 'diversify', start: 360, end: 387, title: 'Diversification: the free lunch'},
  {id: 'drawdowns', start: 468, end: 515, title: 'Drawdowns: peak to trough'},
  {id: 'holding', start: 518, end: 582, title: 'Horizon collapses the range'},
  {id: 'capacity', start: 632, end: 698, title: 'Capacity vs tolerance'},
  {id: 'marks', start: 825, end: 846, title: 'Marks: risk is a distribution'},
  {id: 'recovery', start: 849, end: 868, title: 'The survival math'},
  {id: 'outro', start: 888, end: 957, title: 'Next week'},
];

/* ---------------- shared bits ---------------- */

const Card: React.FC<{title: string; children: React.ReactNode}> = ({
  title,
  children,
}) => (
  <div
    style={{
      width: '100%',
      backgroundColor: 'rgba(14,11,8,0.94)',
      border: `2px solid rgba(245,197,24,0.35)`,
      borderRadius: 24,
      padding: '26px 32px 30px',
      boxShadow: '0 18px 60px rgba(0,0,0,0.55)',
    }}
  >
    <div
      style={{
        fontFamily: FONT,
        fontSize: 26,
        fontWeight: 800,
        letterSpacing: 4,
        color: GOLD,
        textTransform: 'uppercase',
        marginBottom: 18,
      }}
    >
      {title}
    </div>
    {children}
  </div>
);

const SvgText: React.FC<{
  x: number;
  y: number;
  children: React.ReactNode;
  size?: number;
  fill?: string;
  anchor?: 'start' | 'middle' | 'end';
  weight?: number;
}> = ({x, y, children, size = 22, fill = '#fff', anchor = 'start', weight = 600}) => (
  <text
    x={x}
    y={y}
    fontFamily={FONT}
    fontSize={size}
    fontWeight={weight}
    fill={fill}
    textAnchor={anchor}
  >
    {children}
  </text>
);

const clamp = {
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
} as const;

/** A lesson chart PNG shown as a card with a slow zoom and caption. */
const ImageCard: React.FC<{lt: number; src: string; caption: string}> = ({
  lt,
  src,
  caption,
}) => {
  const zoom = interpolate(lt, [0, 40], [1, 1.045], clamp);
  return (
    <div>
      <div style={{overflow: 'hidden', borderRadius: 14}}>
        <Img
          src={src}
          style={{
            width: '100%',
            display: 'block',
            transform: `scale(${zoom})`,
            borderRadius: 14,
          }}
        />
      </div>
      <div style={{fontFamily: FONT, fontSize: 24, color: DIM, marginTop: 14}}>
        {caption}
      </div>
    </div>
  );
};

/* ---------------- diagrams ---------------- */

/** Three outcome ranges: T-bill tight, S&P wide, biotech extreme. */
const Ranges: React.FC<{lt: number}> = ({lt}) => {
  // schematic widths (not to scale across rows); center tick = "expected"
  const rows = [
    {n: 'T-bill', lo: '', hi: '≈ 4.3%', w: 26, c: GREEN, note: 'you know what you’ll have'},
    {n: 'S&P 500', lo: '−38%', hi: '+53%', w: 320, c: BLUE, note: 'a wide year, either way'},
    {n: 'One biotech stock', lo: '−90%', hi: '+400%', w: 560, c: RED, note: 'the future is unknowable'},
  ];
  const cx = 430;
  return (
    <div>
      <svg width={824} height={316} viewBox="0 0 824 316">
        {rows.map((r, i) => {
          const grow = interpolate(lt, [0.5 + i * 1.6, 0.5 + i * 1.6 + 1.6], [0, 1], clamp);
          const y = 52 + i * 92;
          const w = r.w * grow;
          return (
            <g key={i}>
              <SvgText x={70} y={y - 26} size={22} weight={800}>
                {r.n}
              </SvgText>
              <rect x={cx - w / 2} y={y - 14} width={Math.max(2, w)} height={28} rx={14} fill={r.c} opacity={0.85} />
              <line x1={cx} y1={y - 22} x2={cx} y2={y + 22} stroke="#fff" strokeWidth={2.5} />
              {grow > 0.8 && (
                <>
                  {r.lo && (
                    <SvgText x={cx - r.w / 2 - 12} y={y + 8} size={21} fill={r.c} anchor="end" weight={800}>
                      {r.lo}
                    </SvgText>
                  )}
                  <SvgText x={cx + r.w / 2 + 12} y={y + 8} size={21} fill={r.c} weight={800}>
                    {r.hi}
                  </SvgText>
                </>
              )}
              <SvgText x={cx} y={y + 48} size={19} fill={DIM} anchor="middle">
                {r.note}
              </SvgText>
            </g>
          );
        })}
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: lt > 6 ? GOLD : DIM, marginTop: 2, minHeight: 34, fontWeight: lt > 6 ? 800 : 400}}>
        {lt > 6 ? 'Risk is not "bad". Risk is how wide the future is.' : 'Same word — three completely different widths of future.'}
      </div>
    </div>
  );
};

/** Equity returns by regime: 9.5 / 11 / 14.5, then the CAPE asterisk. */
const Regimes: React.FC<{lt: number}> = ({lt}) => {
  const bars = [
    {era: '1928–1971', sub: 'Bretton Woods', v: 9.5, c: BLUE},
    {era: '1971–2008', sub: 'Fiat, disinflation', v: 11, c: GREEN},
    {era: '2009–2024', sub: 'Zero rates + QE', v: 14.5, c: GOLD},
  ];
  const capeAt = 36; // CAPE turn starts ≈ slot lt 36.7 (abs 229.7)
  return (
    <div>
      <svg width={824} height={300} viewBox="0 0 824 300">
        {bars.map((b, i) => {
          const grow = interpolate(lt, [0.5 + i * 1.2, 0.5 + i * 1.2 + 1.4], [0, 1], clamp);
          const h = (b.v / 16) * 210 * grow;
          const x = 110 + i * 235;
          return (
            <g key={i}>
              <rect x={x} y={252 - h} width={140} height={Math.max(0.1, h)} rx={10} fill={b.c} />
              {grow > 0.85 && (
                <SvgText x={x + 70} y={238 - h} size={27} anchor="middle" weight={800} fill={b.c}>
                  {b.v}%
                </SvgText>
              )}
              <SvgText x={x + 70} y={280} size={20} anchor="middle">
                {b.era}
              </SvgText>
              <SvgText x={x + 70} y={300} size={17} fill={DIM} anchor="middle">
                {b.sub}
              </SvgText>
            </g>
          );
        })}
      </svg>
      <div
        style={{
          fontFamily: FONT,
          fontSize: 24,
          color: lt > capeAt ? RED : DIM,
          marginTop: 8,
          minHeight: 34,
          fontWeight: lt > capeAt ? 800 : 400,
        }}
      >
        {lt > capeAt
          ? 'CAPE in the high 30s today → forward ≈ 3–4% real. Don’t extrapolate the last regime.'
          : 'S&P 500 nominal return per year — and T-bills paid ≈ 0 in the third era.'}
      </div>
    </div>
  );
};

/** Volatility vs number of holdings: decay to the systematic floor. */
const Diversify: React.FC<{lt: number}> = ({lt}) => {
  // x: holdings (log-ish spacing), y: annual volatility %
  const pts: Array<[number, number]> = [
    [70, 46], [150, 38], [250, 30], [350, 26], [450, 23.5], [550, 22], [650, 21], [740, 20.5],
  ];
  const floorY = 268 - 20 * 5.2; // vol 20% on the scale below
  const Y = (v: number) => 268 - v * 5.2;
  const path = pts.map(([x, v], i) => `${i === 0 ? 'M' : 'L'}${x},${Y(v).toFixed(1)}`).join(' ');
  const draw = interpolate(lt, [0.5, 9], [1400, 0], clamp);
  return (
    <div>
      <svg width={824} height={320} viewBox="0 0 824 320">
        {/* diversifiable band */}
        <path d={`${path} L740,${floorY} L70,${floorY} Z`} fill="rgba(70,167,88,0.16)" />
        <line x1={56} y1={floorY} x2={770} y2={floorY} stroke={RED} strokeWidth={2.5} strokeDasharray="9 7" />
        <SvgText x={770} y={floorY + 26} size={19} fill={RED} anchor="end" weight={800}>
          SYSTEMATIC RISK — the floor
        </SvgText>
        <path d={path} fill="none" stroke={GOLD} strokeWidth={5} strokeDasharray={1400} strokeDashoffset={draw} strokeLinecap="round" />
        <SvgText x={86} y={Y(46) - 14} size={20} fill={DIM}>
          1 stock ≈ 46% vol
        </SvgText>
        {lt > 6 && (
          <g>
            <line x1={450} y1={Y(23.5)} x2={450} y2={286} stroke="rgba(255,255,255,0.4)" strokeWidth={2} />
            <SvgText x={462} y={306} size={19} fill="#fff" weight={800}>
              15–20 names: most of the benefit
            </SvgText>
          </g>
        )}
        {lt > 8.5 && (
          <SvgText x={90} y={103} size={21} fill={GREEN} weight={800}>
            unsystematic risk — diversifiable
          </SvgText>
        )}
        <SvgText x={56} y={306} size={18} fill={DIM}>
          number of stocks held →
        </SvgText>
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: DIM, marginTop: 2}}>
        25–40 well-spread names capture ≈ 95% of it. The index buys the last few percent.
      </div>
    </div>
  );
};


/** Capacity (objective) vs tolerance (subjective) + the forced-seller question. */
const Capacity: React.FC<{lt: number; t0: number}> = ({lt, t0}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const questionAt = 56; // "if this position dropped 50%…" ≈ abs 688 = lt 56
  const pop = spring({
    frame: frame - (t0 + questionAt) * fps,
    fps,
    config: {damping: 15, stiffness: 150},
  });
  return (
    <div>
      <div style={{display: 'flex', gap: 20, marginBottom: 20}}>
        <div style={{flex: 1, backgroundColor: 'rgba(255,255,255,0.06)', border: `2px solid ${BLUE}`, borderRadius: 16, padding: '18px 22px'}}>
          <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: BLUE, letterSpacing: 2, marginBottom: 8}}>
            RISK CAPACITY
          </div>
          <div style={{fontFamily: FONT, fontSize: 23, fontWeight: 800, color: '#fff', marginBottom: 6}}>
            What you can afford to lose
          </div>
          <div style={{fontFamily: FONT, fontSize: 21, color: DIM, lineHeight: 1.45}}>
            Time horizon · income · whether the portfolio funds your rent. Objective.
          </div>
        </div>
        <div style={{flex: 1, backgroundColor: 'rgba(255,255,255,0.06)', border: `2px solid ${AMBER}`, borderRadius: 16, padding: '18px 22px'}}>
          <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: AMBER, letterSpacing: 2, marginBottom: 8}}>
            RISK TOLERANCE
          </div>
          <div style={{fontFamily: FONT, fontSize: 23, fontWeight: 800, color: '#fff', marginBottom: 6}}>
            How it feels to watch it drop
          </div>
          <div style={{fontFamily: FONT, fontSize: 21, color: DIM, lineHeight: 1.45}}>
            Your stomach, not your spreadsheet. Subjective — and it lies after a bull market.
          </div>
        </div>
      </div>
      {lt > 21 && lt <= questionAt && (
        <div style={{fontFamily: FONT, fontSize: 24, color: RED, fontWeight: 800, textAlign: 'center'}}>
          The blow-up: high tolerance, low capacity — a forced seller at the bottom.
        </div>
      )}
      {lt > questionAt && (
        <div
          style={{
            transform: `scale(${pop})`,
            opacity: pop,
            backgroundColor: 'rgba(245,197,24,0.12)',
            border: `2px solid ${GOLD}`,
            borderRadius: 16,
            padding: '16px 22px',
            textAlign: 'center',
          }}
        >
          <div style={{fontFamily: FONT, fontSize: 26, fontWeight: 800, color: '#fff', lineHeight: 1.4}}>
            “If this dropped 50% next month, would I be a forced seller?”
          </div>
          <div style={{fontFamily: FONT, fontSize: 22, color: GOLD, fontWeight: 700, marginTop: 6}}>
            If yes, the position is too large. Size to capacity, not tolerance.
          </div>
        </div>
      )}
    </div>
  );
};

/** Recovery math: what a loss demands to get back to even. */
const Recovery: React.FC<{lt: number; t0: number}> = ({lt, t0}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const chips = [
    {loss: '−50%', need: '+100%', note: 'painful, survivable', c: AMBER},
    {loss: '−90%', need: '+900%', note: 'a decade of great years', c: RED},
    {loss: '−100%', need: 'a miracle', note: 'game over — no base left', c: RED},
  ];
  const at = [4.5, 9, 13.5]; // "−50%…", "−90%…", "−100%…" in the survival turn
  return (
    <div style={{display: 'flex', gap: 20}}>
      {chips.map((ch, i) => {
        if (lt < at[i]) {
          return (
            <div key={i} style={{flex: 1, borderRadius: 16, padding: '22px', border: '2px dashed rgba(255,255,255,0.18)', display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 170}}>
              <div style={{fontFamily: FONT, fontSize: 30, fontWeight: 800, color: 'rgba(255,255,255,0.28)'}}>{ch.loss}</div>
            </div>
          );
        }
        const p = spring({frame: frame - (t0 + at[i]) * fps, fps, config: {damping: 14, stiffness: 160}});
        return (
          <div key={i} style={{flex: 1, backgroundColor: 'rgba(255,255,255,0.06)', border: `2px solid ${ch.c}`, borderRadius: 16, padding: '22px', transform: `scale(${p})`, opacity: p, minHeight: 170}}>
            <div style={{fontFamily: FONT, fontSize: 21, color: DIM, letterSpacing: 2, marginBottom: 6}}>YOU LOSE</div>
            <div style={{fontFamily: FONT, fontSize: 44, fontWeight: 800, color: ch.c, marginBottom: 10}}>{ch.loss}</div>
            <div style={{fontFamily: FONT, fontSize: 21, color: DIM, letterSpacing: 2, marginBottom: 6}}>TO RECOVER TAKES</div>
            <div style={{fontFamily: FONT, fontSize: 34, fontWeight: 800, color: '#fff', marginBottom: 8}}>{ch.need}</div>
            <div style={{fontFamily: FONT, fontSize: 20, color: DIM}}>{ch.note}</div>
          </div>
        );
      })}
    </div>
  );
};

const Outro: React.FC<{lt: number; t0: number}> = ({lt, t0}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pop = spring({frame: frame - t0 * fps, fps, config: {damping: 14, stiffness: 120}});
  return (
    <div style={{transform: `scale(${pop})`, opacity: pop, textAlign: 'center', padding: '10px 0'}}>
      <div style={{fontFamily: FONT, fontSize: 30, fontWeight: 800, letterSpacing: 4, color: GOLD, marginBottom: 14}}>
        NEXT WEEK
      </div>
      <div style={{fontFamily: FONT, fontSize: 54, fontWeight: 800, color: '#fff', marginBottom: 12}}>
        The 60/40 Portfolio
      </div>
      <div style={{fontFamily: FONT, fontSize: 26, color: DIM, marginBottom: 18}}>
        Why it worked for forty years — and why it broke in 2022. Subscribe so you don’t miss Week 4.
      </div>
      <div style={{fontFamily: FONT, fontSize: 26, fontWeight: 700, color: GOLD}}>
        The destination: asymmetric trades — big upside, small downside.
      </div>
    </div>
  );
};

const renderDiagram = (id: DiagramId, lt: number, t0: number): React.ReactNode => {
  switch (id) {
    case 'ranges':
      return <Ranges lt={lt} />;
    case 'fattails':
      return (
        <ImageCard
          lt={lt}
          src={returnDistSrc}
          caption="The bars are real. The smooth curve is the model. The tails disagree."
        />
      );
    case 'regimes':
      return <Regimes lt={lt} />;
    case 'diversify':
      return <Diversify lt={lt} />;
    case 'drawdowns':
      return (
        <ImageCard
          lt={lt}
          src={drawdownsSrc}
          caption="Peak to trough — the number your nervous system actually uses."
        />
      );
    case 'holding':
      return (
        <ImageCard
          lt={lt}
          src={holdingSrc}
          caption="Time crushes the range of the rate — not the dollar consequence. And this is the US sample."
        />
      );
    case 'capacity':
      return <Capacity lt={lt} t0={t0} />;
    case 'marks':
      return (
        <ImageCard
          lt={lt}
          src={marksSrc}
          caption="Higher risk promises a wider range — including outcomes far worse than playing it safe."
        />
      );
    case 'recovery':
      return <Recovery lt={lt} t0={t0} />;
    case 'outro':
      return <Outro lt={lt} t0={t0} />;
  }
};

export const DiagramsWeek03: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const slot = DIAGRAM_TIMELINE_WEEK03.find((s) => t >= s.start && t < s.end);
  if (!slot) {
    return null;
  }
  const lt = t - slot.start;
  const dur = slot.end - slot.start;
  const enter = spring({
    frame: frame - slot.start * fps,
    fps,
    config: {damping: 200, stiffness: 180},
  });
  const exit = interpolate(lt, [dur - 0.5, dur], [1, 0], clamp);
  return (
    <div
      style={{
        position: 'absolute',
        left: '50%',
        top: 140,
        width: 920,
        transform: `translateX(-50%) scale(${0.92 + 0.08 * enter})`,
        opacity: Math.min(enter, exit),
      }}
    >
      <Card title={slot.title}>{renderDiagram(slot.id, lt, slot.start)}</Card>
    </div>
  );
};
