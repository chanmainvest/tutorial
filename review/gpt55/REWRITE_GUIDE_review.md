# Review: course/REWRITE_GUIDE.md

## Overall Assessment

The rewrite guide is useful and practical. It captures the intended lesson structure, image-script style, interactive requirements, and SOUL voice anchors.

However, it appears stale in several operational details. The biggest risks are wrong paths, unrealistic script-length guidance, and hard rules that may conflict with actual course topics.

## Content / Instruction Critique

- `Workspace root: c:\Users\hevan\work\chanmainvest\tutorial` is stale for the current workspace (`b:\chanmainvest\tutorial`). Use relative paths instead.
- `course/SOUL.md` is wrong; `SOUL.md` lives at the repository root.
- The per-lesson workflow also says to read `course/SOUL.md`; this will mislead future agents.
- The guide calls Week 1 and Week 2 `LOCKED` canonical templates, but several reviews found issues in early weeks. If they remain canonical, add `structure reference, not fact/error-free reference`.
- `~500-900 script lines` is unrealistic for an 18-minute YouTube script. It likely means words or dialogue lines, but as written it encourages massive scripts.
- `US-listed equities only` is too absolute for lessons that teach international markets, FX, global diversification, or jurisdiction caveats. Better: `default implementation examples use US-listed instruments unless the lesson is explicitly about global markets`.
- `Date frame: April 2026` should require visible `as of` labels and source-date labels in lessons, charts, and interactives.
- Add a hard rule that the reading section is canonical and the YouTube script, image, animation, and interactive must stay consistent with it.
- Add a reminder not to run build/translation scripts unless explicitly requested, matching repository guidance.

## Presentation Critique

- The structure block is clear and valuable.
- The chart and interactive templates are specific enough to prevent drift.
- Consider adding a final `common failure modes` section: stale source dates, synthetic data not labeled, contract multipliers wrong, tax assumptions hidden, and Week outro cross-reference drift.

## SOUL Consistency Flags

- The style anchors correctly point to SOUL themes.
- The wording `Don't sticker -- fold them in` is a good instruction and should stay.
- Needs the current SOUL workflow pointer: `.claude/docs/soul-application.md` should be read before lesson rewrite/review work.
