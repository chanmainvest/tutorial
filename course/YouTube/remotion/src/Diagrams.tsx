import React from 'react';
import {interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

const FONT = 'Inter, system-ui, -apple-system, sans-serif';
const GOLD = '#f5c518';
const DIM = 'rgba(255,255,255,0.62)';
const RED = '#e5484d';
const GREEN = '#46a758';

type DiagramId =
  | 'textbook'
  | 'rule72'
  | 'treadmill'
  | 'games'
  | 'm2'
  | 'abc'
  | 'takeaways'
  | 'outro';

interface DiagramSlot {
  id: DiagramId;
  start: number; // seconds
  end: number; // seconds
  title: string;
}

/**
 * Visual-learning overlays, timed to the transcript. The first four mirror
 * the [ANIMATION:] cues in the YouTube script; the rest cover the other
 * numbers-heavy stretches (CPI games, M2, A/B/C, takeaways).
 */
export const DIAGRAM_TIMELINE: DiagramSlot[] = [
  {id: 'textbook', start: 34.6, end: 80, title: 'The textbook chart'},
  {id: 'rule72', start: 104.3, end: 127.1, title: 'The Rule of 72'},
  {id: 'treadmill', start: 158.9, end: 186, title: 'Inflation is a treadmill'},
  {id: 'games', start: 238.6, end: 314, title: 'Three games in the CPI'},
  {id: 'm2', start: 364, end: 392, title: 'M2 money supply, 2000 → 2026'},
  {id: 'abc', start: 474.2, end: 583, title: 'Three savers, 55 years'},
  {id: 'takeaways', start: 621.3, end: 691, title: 'Three takeaways'},
  {id: 'outro', start: 692, end: 720, title: 'Next week'},
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

function smoothPath(): string {
  // exponential-looking curve across an 824x300 chart, origin (40, 270)
  let d = '';
  for (let x = 0; x <= 744; x += 8) {
    const y = 270 - 235 * Math.pow(x / 744, 2.4);
    d += `${x === 0 ? 'M' : 'L'}${40 + x},${y.toFixed(1)} `;
  }
  return d;
}

const JAGGED: Array<[number, number]> = [
  [40, 240], [90, 225], [140, 235], [190, 215], [240, 225],
  [290, 150], [330, 175], [380, 160], [430, 140], [480, 90],
  [520, 120], [560, 105], [610, 120], [650, 110], [680, 150],
  [710, 120], [740, 95], [784, 70],
];

function jaggedPath(): string {
  return JAGGED.map(([x, y], i) => `${i === 0 ? 'M' : 'L'}${x},${y}`).join(' ');
}

/* ---------------- diagrams ---------------- */

const Textbook: React.FC<{lt: number}> = ({lt}) => {
  const crackAt = 13.1; // "That chart is a fairy tale."
  const smoothOpacity = interpolate(lt, [crackAt, crackAt + 0.5], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const jaggedDraw = interpolate(lt, [crackAt + 0.4, crackAt + 9], [2000, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const crackOpacity = interpolate(lt, [crackAt, crackAt + 0.15], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const st = lt - crackAt;
  const shake =
    st > 0 && st < 0.6 ? Math.sin(st * 55) * 9 * (1 - st / 0.6) : 0;
  const smoothDraw = interpolate(lt, [0.5, 8], [1200, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <div style={{transform: `translateX(${shake}px)`}}>
      <svg width={824} height={320} viewBox="0 0 824 320">
        <SvgText x={40} y={28} size={20} fill={DIM}>
          $10,000 at 8% / year
        </SvgText>
        <g opacity={smoothOpacity}>
          <path
            d={smoothPath()}
            fill="none"
            stroke={GREEN}
            strokeWidth={5}
            strokeDasharray={1200}
            strokeDashoffset={smoothDraw}
            strokeLinecap="round"
          />
          <SvgText x={620} y={60} size={24} fill={GREEN} weight={800}>
            → $1,000,000
          </SvgText>
        </g>
        <g opacity={crackOpacity}>
          {[
            'M410,140 L370,200 L390,250',
            'M430,130 L470,190 L450,260',
            'M420,135 L420,90 L380,60',
            'M425,140 L480,120 L540,140',
          ].map((d, i) => (
            <path key={i} d={d} stroke="#fff" strokeWidth={3} fill="none" />
          ))}
        </g>
        {lt > crackAt && (
          <g>
            <path
              d={jaggedPath()}
              fill="none"
              stroke={GOLD}
              strokeWidth={5}
              strokeDasharray={2000}
              strokeDashoffset={jaggedDraw}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            <SvgText x={250} y={140} size={20} fill={RED} weight={800}>
              2000 −49%
            </SvgText>
            <SvgText x={440} y={80} size={20} fill={RED} weight={800}>
              2008 −57%
            </SvgText>
            <SvgText x={640} y={140} size={20} fill={RED} weight={800}>
              2020 −34%
            </SvgText>
          </g>
        )}
      </svg>
      <div
        style={{
          fontFamily: FONT,
          fontSize: 24,
          color: DIM,
          marginTop: 6,
          minHeight: 34,
        }}
      >
        {lt > crackAt + 1 ? 'Never a smooth line.' : 'The line every investing book opens with.'}
      </div>
    </div>
  );
};

const Rule72: React.FC<{lt: number}> = ({lt}) => {
  const steps = [
    {yr: 'yr 0', v: '$10k', h: 34},
    {yr: 'yr 9', v: '$20k', h: 68},
    {yr: 'yr 18', v: '$40k', h: 136},
    {yr: 'yr 27', v: '$80k', h: 204},
    {yr: 'yr 36', v: '$160k', h: 260},
  ];
  return (
    <div>
      <svg width={824} height={330} viewBox="0 0 824 330">
        {steps.map((s, i) => {
          const grow = interpolate(lt, [0.5 + i * 1.4, 0.5 + i * 1.4 + 1.2], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          const x = 70 + i * 148;
          const wobble =
            i === 3 && lt > 14 ? Math.sin((lt - 14) * 30) * 4 * Math.max(0, 1 - (lt - 14) / 3) : 0;
          return (
            <g key={i} transform={`translate(${wobble},0)`}>
              <rect
                x={x}
                y={300 - s.h * grow}
                width={96}
                height={Math.max(0.1, s.h * grow)}
                rx={8}
                fill={i === 4 ? GOLD : '#3e8ef7'}
              />
              <SvgText x={x + 48} y={322} size={20} fill={DIM} anchor="middle">
                {s.yr}
              </SvgText>
              <SvgText x={x + 48} y={292 - s.h * grow} size={22} fill="#fff" anchor="middle" weight={800}>
                {s.v}
              </SvgText>
            </g>
          );
        })}
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: lt > 14 ? RED : DIM, marginTop: 6, minHeight: 34, fontWeight: lt > 14 ? 800 : 400}}>
        {lt > 14 ? '2008 doesn\u2019t follow your schedule.' : '8% a year → your money doubles every 9 years.'}
      </div>
    </div>
  );
};

const Treadmill: React.FC<{lt: number}> = ({lt}) => {
  const lanes = [
    {name: 'CASH', color: RED, x: 620 - lt * 24},
    {name: 'BONDS', color: GOLD, x: 400},
    {name: 'STOCKS', color: GREEN, x: 190 + lt * 15},
  ];
  const stripeOff = (lt * 70) % 90;
  return (
    <div>
      <svg width={824} height={300} viewBox="0 0 824 300">
        <SvgText x={40} y={28} size={20} fill={DIM}>
          INFLATION — the belt moves backward at 3–5% / yr
        </SvgText>
        {lanes.map((l, i) => {
          const y = 70 + i * 80;
          return (
            <g key={l.name}>
              <rect x={150} y={y} width={640} height={54} rx={10} fill="rgba(255,255,255,0.07)" />
              {Array.from({length: 10}).map((_, s) => (
                <rect
                  key={s}
                  x={160 + s * 90 - stripeOff}
                  y={y + 8}
                  width={34}
                  height={38}
                  rx={6}
                  fill="rgba(255,255,255,0.10)"
                />
              ))}
              <rect x={36} y={y + 4} width={96} height={46} rx={23} fill={l.color} />
              <SvgText x={84} y={y + 34} size={20} fill="#14100b" anchor="middle" weight={800}>
                {l.name}
              </SvgText>
              <g transform={`translate(${l.x},${y + 27 + Math.sin(lt * 9 + i * 2) * 3})`}>
                <circle r={17} fill={l.color} />
                <circle r={17} fill="none" stroke="rgba(0,0,0,0.25)" strokeWidth={2} />
              </g>
            </g>
          );
        })}
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: DIM, marginTop: 6}}>
        Stand still and the belt carries you backward. Only stocks outrun it.
      </div>
    </div>
  );
};

const GameCards: React.FC<{lt: number; t0: number; games: Array<{n: string; t: string; d: string}>; at: number[]}> = ({
  lt,
  t0,
  games,
  at,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return (
    <div style={{display: 'flex', gap: 20}}>
      {games.map((g, i) => {
        const pop = spring({
          frame: frame - (t0 + at[i]) * fps,
          fps,
          config: {damping: 14, stiffness: 160},
        });
        if (lt < at[i]) {
          // dimmed teaser for games not yet revealed
          return (
            <div
              key={i}
              style={{
                flex: 1,
                borderRadius: 16,
                padding: '20px 22px',
                border: '2px dashed rgba(255,255,255,0.18)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: 'rgba(255,255,255,0.28)', letterSpacing: 2}}>
                {g.n}
              </div>
            </div>
          );
        }
        return (
          <div
            key={i}
            style={{
              flex: 1,
              backgroundColor: 'rgba(255,255,255,0.06)',
              borderRadius: 16,
              padding: '20px 22px',
              transform: `scale(${pop})`,
              opacity: pop,
            }}
          >
            <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: GOLD, letterSpacing: 2, marginBottom: 10}}>
              {g.n}
            </div>
            <div style={{fontFamily: FONT, fontSize: 26, fontWeight: 800, color: '#fff', marginBottom: 10}}>
              {g.t}
            </div>
            <div style={{fontFamily: FONT, fontSize: 21, color: DIM, lineHeight: 1.45}}>
              {g.d}
            </div>
          </div>
        );
      })}
    </div>
  );
};

const Games: React.FC<{lt: number; t0: number}> = ({lt, t0}) => (
  <GameCards
    lt={lt}
    t0={t0}
    at={[0, 39.4, 57.7]}
    games={[
      {
        n: 'GAME 1',
        t: 'Hedonic adjustment',
        d: 'A better iPhone at the same price counts as deflation.',
      },
      {
        n: 'GAME 2',
        t: 'Core inflation',
        d: 'Strip out food & energy — the things you actually buy.',
      },
      {
        n: 'GAME 3',
        t: 'Substitution',
        d: 'Beef → chicken: what gets pricier counts less.',
      },
    ]}
  />
);

const M2: React.FC<{lt: number}> = ({lt}) => {
  // three climbing lines 2000→2026 with a 2020 vertical jump
  const line = (base: number, amp: number, jump: number) => {
    let d = '';
    let lastY = base;
    for (let x = 0; x <= 744; x += 12) {
      const yr = 2000 + (x / 744) * 26;
      const y = Math.max(30, base - amp * (x / 744) - (yr >= 2020 ? jump * Math.min(1, (yr - 2020) / 2 + 0.4) : 0));
      lastY = y;
      d += `${x === 0 ? 'M' : 'L'}${40 + x},${y.toFixed(1)} `;
    }
    return {d, lastY};
  };
  const draw = interpolate(lt, [0.5, 10], [1600, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const jumpX = 40 + ((2020 - 2000) / 26) * 744;
  return (
    <div>
      <svg width={824} height={300} viewBox="0 0 824 300">
        {[
          {d: line(260, 120, 70), c: '#3e8ef7', n: 'USD'},
          {d: line(275, 100, 55), c: GREEN, n: 'EUR'},
          {d: line(285, 85, 45), c: GOLD, n: 'JPY'},
        ].map((l, i) => (
          <g key={i}>
            <path d={l.d.d} fill="none" stroke={l.c} strokeWidth={5} strokeDasharray={1600} strokeDashoffset={draw} strokeLinecap="round" />
            <SvgText x={792} y={l.d.lastY + 7} size={20} fill={l.c} weight={800}>
              {l.n}
            </SvgText>
          </g>
        ))}
        {lt > 8 && (
          <g>
            <line x1={jumpX} y1={30} x2={jumpX} y2={280} stroke={RED} strokeWidth={2} strokeDasharray="8 6" />
            <SvgText x={jumpX - 12} y={60} size={22} fill={RED} weight={800} anchor="end">
              2020: largest peacetime
            </SvgText>
            <SvgText x={jumpX - 12} y={88} size={22} fill={RED} weight={800} anchor="end">
              money expansion
            </SvgText>
          </g>
        )}
        <SvgText x={40} y={300} size={20} fill={DIM}>2000</SvgText>
        <SvgText x={740} y={300} size={20} fill={DIM}>2026</SvgText>
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: DIM, marginTop: 6}}>
        Every major currency. Every line climbs.
      </div>
    </div>
  );
};

const ABC: React.FC<{lt: number}> = ({lt}) => {
  const switchAt = 57.4; // "But nominal numbers lie."
  const morph = interpolate(lt, [switchAt, switchAt + 2.5], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // sqrt scale keeps the small bars visible; note the proportions survive
  const nominal = [550_000, 1_730_000, 42_000_000];
  const real = [66_000, 208_000, 5_000_000];
  const fmt = (v: number) =>
    v >= 1_000_000 ? `$${parseFloat((v / 1_000_000).toFixed(1))}M` : `$${Math.round(v / 1000)}k`;
  const people = [
    {n: 'A · Cash in a drawer', c: '#8a8a8a'},
    {n: 'B · T-bills', c: '#3e8ef7'},
    {n: 'C · S&P 500', c: GREEN},
  ];
  return (
    <div>
      <div style={{fontFamily: FONT, fontSize: 22, color: DIM, marginBottom: 12}}>
        {morph < 0.5 ? 'Same $10,000/yr for 55 years — nominal' : '…restated in 1971 purchasing power'}
      </div>
      <svg width={824} height={300} viewBox="0 0 824 300">
        {people.map((p, i) => {
          const grow = interpolate(lt, [1 + i * 2, 1 + i * 2 + 2], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          const hNom = Math.sqrt(nominal[i] / 42_000_000) * 230;
          const hReal = Math.sqrt(real[i] / 5_000_000) * 230;
          const h = (hNom + (hReal - hNom) * morph) * grow;
          const x = 90 + i * 250;
          const isA = i === 0 && morph > 0.5;
          return (
            <g key={i}>
              <rect x={x} y={270 - h} width={150} height={Math.max(0.1, h)} rx={10} fill={isA ? RED : p.c} />
              <SvgText x={x + 75} y={262 - h} size={24} fill="#fff" anchor="middle" weight={800}>
                {fmt(nominal[i] + (real[i] - nominal[i]) * morph)}
              </SvgText>
              <SvgText x={x + 75} y={292} size={20} fill={DIM} anchor="middle">
                {p.n}
              </SvgText>
            </g>
          );
        })}
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: morph > 0.5 ? RED : DIM, marginTop: 6, minHeight: 34, fontWeight: morph > 0.5 ? 800 : 400}}>
        {morph > 0.5
          ? 'Cash: 55 years of saving → about 6½ years of deposits.'
          : 'Each put in $550,000 of their own money.'}
      </div>
    </div>
  );
};

const Takeaways: React.FC<{lt: number; t0: number}> = ({lt, t0}) => (
  <GameCards
    lt={lt}
    t0={t0}
    at={[0, 13.5, 30.9]}
    games={[
      {
        n: '1',
        t: 'The textbook chart is a fairy tale',
        d: 'No risk-free 8%. A smooth curve is a sales pitch.',
      },
      {
        n: '2',
        t: 'You\u2019re already in a bet',
        d: 'Cash vs inflation. Plan on 4–5% real just to stand still.',
      },
      {
        n: '3',
        t: 'Own things, not currency',
        d: 'Equities, gold, productive real estate — denominated in things.',
      },
    ]}
  />
);

const Outro: React.FC<{lt: number}> = ({lt}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pop = spring({frame: frame - 692 * fps, fps, config: {damping: 14, stiffness: 120}});
  return (
    <div style={{transform: `scale(${pop})`, opacity: pop, textAlign: 'center', padding: '10px 0'}}>
      <div style={{fontFamily: FONT, fontSize: 30, fontWeight: 800, letterSpacing: 4, color: GOLD, marginBottom: 14}}>
        NEXT WEEK
      </div>
      <div style={{fontFamily: FONT, fontSize: 54, fontWeight: 800, color: '#fff', marginBottom: 12}}>
        Index Funds &amp; ETFs
      </div>
      <div style={{fontFamily: FONT, fontSize: 26, color: DIM}}>
        The cheapest way to own it all — subscribe so you don&apos;t miss Week 2.
      </div>
    </div>
  );
};

const renderDiagram = (id: DiagramId, lt: number, t0: number): React.ReactNode => {
  switch (id) {
    case 'textbook':
      return <Textbook lt={lt} />;
    case 'rule72':
      return <Rule72 lt={lt} />;
    case 'treadmill':
      return <Treadmill lt={lt} />;
    case 'games':
      return <Games lt={lt} t0={t0} />;
    case 'm2':
      return <M2 lt={lt} />;
    case 'abc':
      return <ABC lt={lt} />;
    case 'takeaways':
      return <Takeaways lt={lt} t0={t0} />;
    case 'outro':
      return <Outro lt={lt} />;
  }
};

export const Diagrams: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const slot = DIAGRAM_TIMELINE.find((s) => t >= s.start && t < s.end);
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
  const exit = interpolate(lt, [dur - 0.5, dur], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
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
