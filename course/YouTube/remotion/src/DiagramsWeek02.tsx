import React from 'react';
import {Img, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

import spivaSrc from '../../../../image/week02_spiva.png';
import expenseDragSrc from '../../../../image/week02_expense_drag.png';
import buyTermSrc from '../../../../image/week02_buy_term_invest_difference.png';

const FONT = 'Inter, system-ui, -apple-system, sans-serif';
const GOLD = '#f5c518';
const DIM = 'rgba(255,255,255,0.62)';
const RED = '#e5484d';
const GREEN = '#46a758';
const BLUE = '#3e8ef7';
const AMBER = '#f0a020';

type DiagramId =
  | 'tickers'
  | 'capweights'
  | 'spiva'
  | 'expensedrag'
  | 'advisors'
  | 'buyterm'
  | 'countdown'
  | 'pie'
  | 'timeline'
  | 'recap'
  | 'outro';

interface DiagramSlot {
  id: DiagramId;
  start: number; // seconds
  end: number; // seconds
  title: string;
}

/**
 * Week 2 visual-learning overlays, timed to the Week 2 transcript.
 * Mirrors the [ANIMATION:] cues in week02_index_funds_etfs.md: three cues
 * are the lesson's own matplotlib charts (shown as image cards), the rest
 * are animated SVG diagrams in the Week 1 style.
 * Times are filled in from the aligned transcript (see transcript.ts).
 */
export const DIAGRAM_TIMELINE_WEEK02: DiagramSlot[] = [
  {id: 'tickers', start: 79, end: 112, title: '500 stocks → one fund'},
  {id: 'capweights', start: 114, end: 147, title: 'Weighted by market cap'},
  {id: 'spiva', start: 331, end: 373, title: 'SPIVA: active vs the index'},
  {id: 'expensedrag', start: 442, end: 476, title: 'The fee drag — $100k, 30 years'},
  {id: 'advisors', start: 529, end: 584, title: 'How your advisor gets paid'},
  {id: 'buyterm', start: 714, end: 747, title: 'Buy term, invest the difference'},
  {id: 'countdown', start: 1011, end: 1075, title: 'Buy your first ETF — 15 minutes'},
  {id: 'pie', start: 1099, end: 1160, title: 'The three-fund portfolio'},
  {id: 'timeline', start: 1236, end: 1302, title: 'It worked for 40 years'},
  {id: 'recap', start: 1355, end: 1403, title: 'Six things to remember'},
  {id: 'outro', start: 1426, end: 1454, title: 'Next week'},
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

/* ---------------- diagrams ---------------- */

/** Hundreds of tickers swirling, swept into a single basket: ONE ETF. */
const Tickers: React.FC<{lt: number}> = ({lt}) => {
  const names = [
    'AAPL', 'MSFT', 'NVDA', 'AMZN', 'META', 'GOOGL', 'TSLA', 'JPM',
    'XOM', 'WMT', 'HD', 'COST', 'AVGO', 'NFLX', 'AMD', 'UNH',
  ];
  // deterministic scattered start positions + swirl phase per chip
  const chips = names.map((n, i) => {
    const sx = 60 + ((i * 197) % 700);
    const sy = 30 + ((i * 131) % 190);
    const col = i % 4;
    const row = Math.floor(i / 4);
    const tx = 262 + col * 78;
    const ty = 96 + row * 52;
    return {n, sx, sy, tx, ty, ph: i * 1.7};
  });
  const gather = interpolate(lt, [2.2, 6.2], [0, 1], clamp);
  const basketIn = interpolate(lt, [1.6, 2.6], [0, 1], clamp);
  const labelIn = interpolate(lt, [6.2, 7.2], [0, 1], clamp);
  return (
    <div>
      <svg width={824} height={330} viewBox="0 0 824 330">
        <g opacity={basketIn}>
          <rect x={222} y={66} width={380} height={196} rx={20} fill="rgba(245,197,24,0.10)" stroke={GOLD} strokeWidth={3} />
        </g>
        {chips.map((c, i) => {
          const swirl = gather < 1 ? Math.sin(lt * 1.6 + c.ph) * 9 : 0;
          const swirlY = gather < 1 ? Math.cos(lt * 1.3 + c.ph) * 7 : 0;
          const x = c.sx + (c.tx - c.sx) * gather + swirl * (1 - gather);
          const y = c.sy + (c.ty - c.sy) * gather + swirlY * (1 - gather);
          return (
            <g key={i} transform={`translate(${x},${y})`}>
              <rect x={-32} y={-19} width={64} height={38} rx={9} fill="#232a35" stroke="rgba(255,255,255,0.35)" strokeWidth={1.5} />
              <SvgText x={0} y={7} size={17} anchor="middle" weight={800}>
                {c.n}
              </SvgText>
            </g>
          );
        })}
        <g opacity={labelIn}>
          <SvgText x={412} y={306} size={34} fill={GOLD} anchor="middle" weight={800}>
            ONE ETF
          </SvgText>
        </g>
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: lt > 6.4 ? GOLD : DIM, marginTop: 2, minHeight: 34, fontWeight: lt > 6.4 ? 800 : 400}}>
        {lt > 6.4 ? 'And it beats 90% of the pros.' : 'Hundreds of stocks. One basket.'}
      </div>
    </div>
  );
};

/** Market-cap weights: a few giants, then a long tail to a 0.02% sliver. */
const CapWeights: React.FC<{lt: number}> = ({lt}) => {
  const rows = [
    {n: 'Apple', v: 7.0, c: GOLD},
    {n: 'Microsoft', v: 6.5, c: BLUE},
    {n: 'Nvidia', v: 5.6, c: GREEN},
    {n: 'Alphabet', v: 4.3, c: '#9e8cfc'},
    {n: 'Amazon', v: 3.6, c: AMBER},
    {n: 'Meta', v: 2.6, c: '#e93d82'},
    {n: 'Smallest of the 500', v: 0.02, c: 'rgba(255,255,255,0.5)'},
  ];
  const maxW = 560;
  return (
    <div>
      <svg width={824} height={300} viewBox="0 0 824 300">
        {rows.map((r, i) => {
          const grow = interpolate(lt, [0.4 + i * 0.9, 0.4 + i * 0.9 + 1.1], [0, 1], clamp);
          const y = 18 + i * 40;
          const w = Math.max(3, (r.v / 7) * maxW) * grow;
          return (
            <g key={i}>
              <SvgText x={196} y={y + 24} size={20} anchor="end">
                {r.n}
              </SvgText>
              <rect x={212} y={y} width={w} height={30} rx={7} fill={r.c} />
              {grow > 0.85 && (
                <SvgText x={224 + (r.v / 7) * maxW} y={y + 23} size={20} weight={800} fill={r.c}>
                  {r.v.toFixed(2).replace(/0$/, '')}%
                </SvgText>
              )}
            </g>
          );
        })}
      </svg>
      <div
        style={{
          fontFamily: FONT,
          fontSize: 24,
          color: lt > 14 ? GOLD : DIM,
          marginTop: 2,
          minHeight: 34,
          fontWeight: lt > 14 ? 800 : 400,
        }}
      >
        {lt > 14 ? 'The top 10 alone are roughly a third of the index.' : 'Weighted by market value — not one stock, one vote.'}
      </div>
    </div>
  );
};

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

/** Three advisor compensation models, popping in as they are named. */
const Advisors: React.FC<{lt: number; t0: number}> = ({lt, t0}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const boxes = [
    {
      n: 'COMMISSION-BASED',
      c: RED,
      d: 'Paid by the fund company for every product sold.',
      conflict: 'Conflict: HIGH',
    },
    {
      n: 'FEE-BASED',
      c: AMBER,
      d: 'A mix — fees from you, plus commissions from funds.',
      conflict: 'Conflict: MODERATE',
    },
    {
      n: 'FEE-ONLY FIDUCIARY',
      c: GREEN,
      d: 'Paid only by you. Legally bound to your best interest.',
      conflict: 'Conflict: LOW',
    },
  ];
  const at = [1.2, 11.3, 17.3]; // word times of Commission-based / Fee-based / Fee-only
  return (
    <div style={{display: 'flex', gap: 20}}>
      {boxes.map((b, i) => {
        if (lt < at[i]) {
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
                minHeight: 190,
              }}
            >
              <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: 'rgba(255,255,255,0.28)', letterSpacing: 2}}>
                {b.n}
              </div>
            </div>
          );
        }
        const pop = spring({
          frame: frame - (t0 + at[i]) * fps,
          fps,
          config: {damping: 14, stiffness: 160},
        });
        return (
          <div
            key={i}
            style={{
              flex: 1,
              backgroundColor: 'rgba(255,255,255,0.06)',
              border: `2px solid ${b.c}`,
              borderRadius: 16,
              padding: '20px 22px',
              transform: `scale(${pop})`,
              opacity: pop,
              minHeight: 190,
            }}
          >
            <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: b.c, letterSpacing: 2, marginBottom: 10}}>
              {b.n}
            </div>
            <div style={{fontFamily: FONT, fontSize: 21, color: '#fff', lineHeight: 1.45, marginBottom: 12}}>
              {b.d}
            </div>
            <div style={{fontFamily: FONT, fontSize: 20, fontWeight: 800, color: b.c}}>
              {b.conflict}
            </div>
          </div>
        );
      })}
    </div>
  );
};


/** Five steps to your first ETF, against a draining 15:00 countdown bar. */
const Countdown: React.FC<{lt: number; dur: number}> = ({lt, dur}) => {
  const steps = [
    {t: 'Open a brokerage account', d: 'Fidelity · Schwab · Vanguard — or Interactive Brokers'},
    {t: 'Link your bank & transfer', d: 'ACH arrives in 1–3 business days'},
    {t: 'Search the ticker', d: 'Type V O O — the fund profile pops up'},
    {t: 'Place a buy order', d: 'Market order, any dollar amount'},
    {t: 'Automate it, then forget it', d: '$500 on the 1st of every month'},
  ];
  // step turns land at these local times in the Week 2 transcript
  const at = [3.5, 20.5, 27.5, 33.5, 45.5];
  const remaining = Math.max(0, 900 * (1 - lt / dur));
  const mm = Math.floor(remaining / 60);
  const ss = Math.floor(remaining % 60);
  const barW = interpolate(lt, [0, dur], [856, 0], clamp);
  return (
    <div>
      <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: 10}}>
        <div style={{fontFamily: FONT, fontSize: 22, color: DIM, letterSpacing: 2}}>
          TIME BUDGET
        </div>
        <div style={{fontFamily: FONT, fontSize: 34, fontWeight: 800, color: GOLD, fontVariantNumeric: 'tabular-nums'}}>
          {mm}:{ss.toString().padStart(2, '0')}
        </div>
      </div>
      <div style={{height: 14, borderRadius: 7, backgroundColor: 'rgba(255,255,255,0.10)', marginBottom: 22}}>
        <div style={{height: 14, borderRadius: 7, backgroundColor: GOLD, width: barW}} />
      </div>
      <div style={{display: 'flex', flexDirection: 'column', gap: 10}}>
        {steps.map((s, i) => {
          const on = lt >= at[i];
          return (
            <div
              key={i}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 16,
                opacity: on ? 1 : 0.32,
                transition: 'opacity 0.3s',
              }}
            >
              <div
                style={{
                  width: 40,
                  height: 40,
                  borderRadius: 20,
                  backgroundColor: on ? GREEN : 'rgba(255,255,255,0.15)',
                  color: on ? '#14100b' : '#fff',
                  fontFamily: FONT,
                  fontSize: 21,
                  fontWeight: 800,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  flexShrink: 0,
                }}
              >
                {on ? '✓' : i + 1}
              </div>
              <div style={{fontFamily: FONT, fontSize: 24, fontWeight: 800, color: '#fff'}}>
                {s.t}
              </div>
              <div style={{fontFamily: FONT, fontSize: 21, color: DIM}}>{s.d}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

/** Three-fund pie: VTI 60 / VXUS 25 / BND 15 — BND flagged late in the slot. */
const Pie: React.FC<{lt: number}> = ({lt}) => {
  const slices = [
    {n: 'VTI', sub: 'Total US stocks', v: 60, c: GREEN},
    {n: 'VXUS', sub: 'International stocks', v: 25, c: BLUE},
    {n: 'BND', sub: 'US bonds', v: 15, c: AMBER},
  ];
  const cx = 190;
  const cy = 165;
  const r = 140;
  const polar = (angDeg: number): [number, number] => {
    const a = ((angDeg - 90) * Math.PI) / 180;
    return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
  };
  const arc = (from: number, to: number): string => {
    const [x1, y1] = polar(from);
    const [x2, y2] = polar(to);
    const large = to - from > 180 ? 1 : 0;
    return `M${cx},${cy} L${x1.toFixed(1)},${y1.toFixed(1)} A${r},${r} 0 ${large} 1 ${x2.toFixed(1)},${y2.toFixed(1)} Z`;
  };
  let acc = 0;
  const flagAt = 48; // fires as the "bonds as ballast" critique turn begins (abs ~1147s)
  const flagPulse = lt > flagAt ? 0.75 + 0.25 * Math.sin((lt - flagAt) * 6) : 0;
  return (
    <div style={{display: 'flex', gap: 36, alignItems: 'center'}}>
      <svg width={380} height={330} viewBox="0 0 380 330">
        {slices.map((s, i) => {
          const from = acc;
          acc += s.v * 3.6;
          const sweep = interpolate(lt, [0.5 + i * 1.1, 0.5 + i * 1.1 + 1.4], [0, 1], clamp);
          const to = from + s.v * 3.6 * sweep;
          if (sweep <= 0) return null;
          const isBnd = s.n === 'BND';
          return (
            <path
              key={i}
              d={arc(from, Math.max(to, from + 0.5))}
              fill={s.c}
              opacity={isBnd && lt > flagAt ? flagPulse : 0.92}
              stroke={isBnd && lt > flagAt ? RED : 'rgba(14,11,8,0.9)'}
              strokeWidth={isBnd && lt > flagAt ? 5 : 3}
            />
          );
        })}
        {lt > flagAt && (
          <SvgText x={cx} y={cy + 168} size={21} fill={RED} anchor="middle" weight={800}>
            BND: shortest shelf life
          </SvgText>
        )}
      </svg>
      <div style={{flex: 1}}>
        {slices.map((s, i) => {
          const on = lt > 0.5 + i * 1.1;
          return (
            <div key={i} style={{display: 'flex', alignItems: 'baseline', gap: 14, marginBottom: 16, opacity: on ? 1 : 0.25}}>
              <div style={{width: 22, height: 22, borderRadius: 6, backgroundColor: s.c, flexShrink: 0, position: 'relative', top: 3}} />
              <div style={{fontFamily: FONT, fontSize: 30, fontWeight: 800, color: '#fff', minWidth: 96}}>
                {s.n}
              </div>
              <div style={{fontFamily: FONT, fontSize: 30, fontWeight: 800, color: s.c}}>{s.v}%</div>
              <div style={{fontFamily: FONT, fontSize: 22, color: DIM}}>{s.sub}</div>
            </div>
          );
        })}
        <div style={{fontFamily: FONT, fontSize: 22, color: DIM, marginTop: 10, lineHeight: 1.5}}>
          Total cost ≈ 0.04% — about $4 a year on $10,000. Bond rule of thumb: your age minus 20.
        </div>
      </div>
    </div>
  );
};

/** 1980→2025: the forty years passive worked — and the flip ahead. */
const Timeline: React.FC<{lt: number}> = ({lt}) => {
  const x0 = 50;
  const x1 = 690; // 2025
  const xFlip = 745;
  const yr = (y: number) => x0 + ((y - 1980) / 45) * (x1 - x0);
  let d = '';
  for (let x = 0; x <= x1 - x0; x += 10) {
    const t = x / (x1 - x0);
    const y = 268 - 225 * Math.pow(t, 1.7) - Math.sin(t * 22) * 7 * (1 - t);
    d += `${x === 0 ? 'M' : 'L'}${(x0 + x).toFixed(1)},${y.toFixed(1)} `;
  }
  const draw = interpolate(lt, [0.5, 11], [1500, 0], clamp);
  const flipAt = 40; // "When the demographic flip arrives…" (abs ~1276s)
  return (
    <div>
      <svg width={824} height={320} viewBox="0 0 824 320">
        <line x1={x0} y1={272} x2={790} y2={272} stroke="rgba(255,255,255,0.3)" strokeWidth={2} />
        {[1980, 1990, 2000, 2010, 2020].map((y) => (
          <g key={y}>
            <line x1={yr(y)} y1={272} x2={yr(y)} y2={282} stroke="rgba(255,255,255,0.4)" strokeWidth={2} />
            <SvgText x={yr(y)} y={306} size={19} fill={DIM} anchor="middle">
              {y}
            </SvgText>
          </g>
        ))}
        <path d={d} fill="none" stroke={GREEN} strokeWidth={5} strokeDasharray={1500} strokeDashoffset={draw} strokeLinecap="round" />
        {lt > 4 && (
          <g>
            <SvgText x={120} y={120} size={20} fill={DIM}>falling interest rates</SvgText>
            <SvgText x={330} y={88} size={20} fill={DIM}>globalisation</SvgText>
            <SvgText x={520} y={64} size={20} fill={DIM}>the Fed put</SvgText>
          </g>
        )}
        {lt > flipAt && (
          <g>
            <line x1={xFlip} y1={36} x2={xFlip} y2={272} stroke={RED} strokeWidth={3} strokeDasharray="9 7" />
            <SvgText x={xFlip} y={26} size={21} fill={RED} anchor="middle" weight={800}>
              DEMOGRAPHIC FLIP
            </SvgText>
            <path
              d={`M${x1},${(268 - 225 - Math.sin(22) * 0).toFixed(0)} L760,120 L790,170`}
              fill="none"
              stroke="rgba(255,255,255,0.55)"
              strokeWidth={4}
              strokeDasharray="10 8"
            />
            <SvgText x={786} y={110} size={44} fill="#fff" anchor="middle" weight={800}>
              ?
            </SvgText>
          </g>
        )}
      </svg>
      <div style={{fontFamily: FONT, fontSize: 24, color: lt > flipAt ? RED : DIM, marginTop: 2, minHeight: 34, fontWeight: lt > flipAt ? 800 : 400}}>
        {lt > flipAt
          ? 'Boomers switch from net buyers to net sellers — the flow can reverse.'
          : 'Forty years of tailwinds: demographics, rates, globalisation.'}
      </div>
    </div>
  );
};

/** The six-point recap, rows appearing as Horace counts them off. */
const Recap: React.FC<{lt: number}> = ({lt}) => {
  const rows = [
    'An index is a list — the ETF buys all of it for ~0.03%',
    '90% of pros lose to that list over 20 years',
    'Fees are the lever you control: 2% ≈ −$715k on $100k',
    'Not a fee-only fiduciary? Then a salesperson',
    'Insurance ≠ investing: buy term, invest the difference',
    'VOO or VTI + VXUS + BND — the foundation portfolio',
  ];
  const at = [2.0, 9.8, 15.4, 25.8, 31.3, 37.6]; // word times of One: … Six: in the recap turn
  return (
    <div style={{display: 'flex', flexDirection: 'column', gap: 11}}>
      {rows.map((r, i) => {
        const on = lt >= at[i];
        return (
          <div key={i} style={{display: 'flex', alignItems: 'center', gap: 16, opacity: on ? 1 : 0.22}}>
            <div
              style={{
                width: 38,
                height: 38,
                borderRadius: 19,
                backgroundColor: on ? GOLD : 'rgba(255,255,255,0.15)',
                color: '#14100b',
                fontFamily: FONT,
                fontSize: 21,
                fontWeight: 800,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                flexShrink: 0,
              }}
            >
              {i + 1}
            </div>
            <div style={{fontFamily: FONT, fontSize: 25, fontWeight: 700, color: '#fff'}}>{r}</div>
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
        Risk and Return
      </div>
      <div style={{fontFamily: FONT, fontSize: 26, color: DIM, marginBottom: 18}}>
        The risk that pays you — and the kind that doesn&apos;t. Subscribe so you don&apos;t miss Week 3.
      </div>
      <div style={{fontFamily: FONT, fontSize: 26, fontWeight: 700, color: GOLD}}>
        Investing is a must. Everything else is a nice-to-have.
      </div>
    </div>
  );
};

const renderDiagram = (id: DiagramId, lt: number, t0: number, dur: number): React.ReactNode => {
  switch (id) {
    case 'tickers':
      return <Tickers lt={lt} />;
    case 'capweights':
      return <CapWeights lt={lt} />;
    case 'spiva':
      return (
        <ImageCard
          lt={lt}
          src={spivaSrc}
          caption="The longer the window, the worse active management looks."
        />
      );
    case 'expensedrag':
      return (
        <ImageCard
          lt={lt}
          src={expenseDragSrc}
          caption="Same $100k, same 10% gross return — only the fee changes."
        />
      );
    case 'advisors':
      return <Advisors lt={lt} t0={t0} />;
    case 'buyterm':
      return (
        <ImageCard
          lt={lt}
          src={buyTermSrc}
          caption="Whole life crawls. Term + the difference, invested, climbs."
        />
      );
    case 'countdown':
      return <Countdown lt={lt} dur={dur} />;
    case 'pie':
      return <Pie lt={lt} />;
    case 'timeline':
      return <Timeline lt={lt} />;
    case 'recap':
      return <Recap lt={lt} />;
    case 'outro':
      return <Outro lt={lt} t0={t0} />;
  }
};

export const DiagramsWeek02: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const slot = DIAGRAM_TIMELINE_WEEK02.find((s) => t >= s.start && t < s.end);
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
      <Card title={slot.title}>{renderDiagram(slot.id, lt, slot.start, dur)}</Card>
    </div>
  );
};
