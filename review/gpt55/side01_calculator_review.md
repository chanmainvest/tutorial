# Review: course/side01_calculator.md

## Overall Assessment

This is a strong practical side lesson and a good model for hands-on tutorial content. The BA II Plus focus is genuinely useful, the keystroke tables are clear, and the browser emulator makes the lesson feel alive.

There is one serious finance/math problem: the NPV/IRR example appears wrong in the reading, script, and interactive preset label.

## Content Critique

- The TVM-key explanation is excellent and beginner-friendly.
- The sign-convention section is one of the strongest parts of the lesson.
- The mortgage example is clear and emotionally effective.
- The statement `every certification body either permits explicitly... or specifies by name` should be softened unless verified for each named body.
- Problem 1 says `8% real, in nominal dollars`, which is internally inconsistent. If the 8% is real, the result is in real purchasing-power terms; if nominal, it is nominal.
- The NPV example is incorrect. For `CF0 = -1000`, `C01 = 300`, `C02 = 400`, `C03 = 500`, and `I = 10%`, NPV is approximately `-20.96`, not `+36.91`. IRR is roughly below 10%, not `roughly 12.0%`. The lesson currently tells students to accept a project that should be rejected at a 10% hurdle.
- The same wrong NPV appears in the YouTube script and interactive preset label.
- The semiannual bond Q&A says TVM gives dirty or clean price depending convention. TVM pricing without accrued-interest handling is not a clean/dirty bond worksheet substitute; the bond worksheet is where settlement date and accrued interest matter.
- The claim that BA II Plus exposes duration should be model-verified because functionality may differ by BA II Plus model/version.

## Structure And Formatting Issues

- The lesson follows the proper Part 1 / Part 2 and decimal section structure.
- It is long, but the length is justified because it functions as a reference manual.

## YouTube Script Critique

The video script has a good hook and practical pacing.

Specific issues:

- `The Only Calculator a Serious Investor Actually Needs` is clickable, but slightly overclaims. Consider `The Finance Calculator Every Serious Investor Should Know`.
- The NPV segment must be fixed before publication.
- `This is the most boring side lesson` is funny but may undercut retention; better: `This is the least glamorous side lesson, but one of the highest-leverage ones`.
- The `Week 1's lie` line is strong, but should say the assumption is fictional, not the math.

## Chart And Interactive Feedback

The emulator is ambitious and useful.

Issues found:

- `side01_calculator.html` preset 4 says NPV at 10% is `~36.91`, but the embedded cash flows would compute roughly `-20.96`.
- The `y^x` key maps to an operator that `applyOp` does not implement, so that key appears nonfunctional.
- The direct `P/Y` action is a placeholder that commits to PMT; this may confuse users if exposed.
- Browser `prompt()` for P/Y and NPV rate works, but a styled in-panel input would feel more professional and mobile-friendly.
- The emulator should show a visible assumption note: educational emulator, not a certified BA II Plus replacement for exams.

## SOUL Consistency Flags

- Strong practical alignment: this is a tool lesson, not a strategy pitch.
- The lesson correctly teaches calculation discipline and input skepticism.
- Fix the NPV example because SOUL's discipline-first philosophy depends on refusing attractive but wrong numbers.
