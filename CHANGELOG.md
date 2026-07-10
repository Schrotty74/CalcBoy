# Changelog

All notable changes to **CALC BOY** are documented here. This file is the single source of version history. Versions follow `MAJOR.MINOR.PATCH`; the version in the `index.html` header and the service-worker cache name (`calcboy-vX.Y.Z`) always match the latest entry.

## v3.1.0 – 2026-07-10

### Added
- **Formula Assistant (FORM page)**: percent-of, rule of three, circle area & circumference, Pythagoras, Ohm's law, BMI, average, speed and VAT helpers – driven by three local variables **A, B, C** (SET A/B/C, INFO, clearable).
- **RPN mode** on the programmer page with a locally stored stack.
- **PNG export** for the calculation history (in addition to text export).

### Changed
- Finance **INFO** now shows end value, total paid in and interest earned.
- Improved iPhone PWA Safe Area handling: THEME, GAME and SND stay below the iOS status bar in installed (standalone) mode.
- Page order is now BASIC → EXT → CONV → FIN → PRG → PLOT → FORM.
- Documentation restructured: this changelog is the only version history; README links to it.

### Fixed
- Variable-clear button on the FORM page was mislabeled VAR C (looked like a recall key); now labeled **CLR ABC**. DREI renamed to **DREISATZ**, and FORM keys use the smaller label font for readability.
- LCD result line keeps a fixed height when long results (e.g. √2) switch to smaller text – no more layout jump.

## v3.0.2 – 2026-07-09

### Added
- Plot page extended from 8 to **20 functions** (e^x, ln x, |x|, 2^x, sinh, cosh, tanh, x⁴, Gauss bell e^(−x²), floor, sinc x, x·sin x added), each with a suitable value range.

### Fixed
- Plot buttons no longer oversized; the page fills a full uniform grid.

## v3.0.1 – 2026-07-09

### Fixed
- All keypad pages now share a fixed 6-row grid: identical button sizes on every page, and the BASIC/MEHR/= navigation row is anchored to the bottom row everywhere.

## v3.0.0 – 2026-07-09

### Added
- **Finance page (FIN)**: compound interest with monthly savings rate (SET K0/P%/JAHRE/RATE, ENDWERT, ZINSEN, INFO, RESET), tip +10/15/20 %, bill splitting by persons, currency conversion with a manually set rate (deliberately no live-rate API).
- **Programmer page (PRG)**: →HEX/→BIN/→OCT display, AND, OR, XOR, MOD, bit shifts « », NOT, ABS, INT, SGN, random number.
- **Plot page**: functions drawn as pixel graphs on the LCD with auto-scaling and axes.
- **SNAKE** as a second game (GAME menu → 5), steered with 2/4/6/8 or arrow keys, increasing speed, own high score.
- Smart percent key: `100 + 10 %` = 110 (percent of the first operand for + and −).
- History shows **Σ** (sum) and **Ø** (average) of the stored results.
- Page navigation via MEHR cycling through the extra pages.

## v2.2.0 – 2026-07-09

### Added
- **Unit converter page (CONV)**: km↔mi, m↔ft, °C↔°F, kg↔lb, cm↔in, l↔gal (US), km/h↔mph, h↔min and German VAT 19 %/7 % net↔gross.
- **MATH ATTACK difficulty levels** (EASY/NORMAL/HARD) with per-level high scores and a PERFECT jingle for flawless runs.
- **Long-press** on the display copies the result; history gained a **share/export** entry (text).
- **Theme-specific key sounds** (waveform and pitch per console).
- **Cartridge-swap animation** when switching themes (respects reduced-motion).
- **Battery LED** shows the real charge level where the Battery Status API exists (Chrome/Android); classic red LED elsewhere.

## v2.1.0 – 2026-07-09

### Added
- **Extended page (EXT)**: memory keys MC/MR/M+/M− with persistent memory and an M indicator in the LCD, sin/cos/tan with a saved **DEG/RAD** toggle, log, ln, 10^x, e^x, x², x³, xʸ, ∛x, 1/x, factorial n!, π and e.

### Changed
- Bottom row split into EXT + = to reach the new page.

## v2.0.0 – 2026-07-09

### Added
- **Boot animation** with jingle ("CALC BOY" drops into the LCD).
- **Persistent settings**: theme and sound survive restarts (localStorage).
- **History**: last 10 calculations in the LCD (tap to open, tap an entry to reuse its result).
- **MATH ATTACK**: 30-second mental-math game with high score.
- **Landscape scientific mode**: extra function column when the phone is rotated.
- **Konami code** (8 8 2 2 4 6 4 6 − +) permanently unlocks the secret **VIRTUAL BOY** theme.
- **Service worker** (sw.js) for full offline capability.

## v1.1.0 – 2026-07-09

### Added
- Pixel-art app icon (apple-touch-icon 180 px + 512 px manifest icon), drawn programmatically in Game Boy style.

### Fixed
- Manifest/icon code guarded so sandboxed previews without a real URL no longer throw a script error.

## v1.0.0 – 2026-07-09

### Added
- Initial release: Game Boy-inspired single-file PWA calculator.
- 6 console themes (Game Boy, GB Color, NES, Super NES, Switch, Famicom) with theme switcher.
- Basic arithmetic, percent, sign toggle, square root; German number format (decimal comma, thousands separators); 12-digit limit with auto-shrinking display; ERROR handling.
- 8-bit key sounds with SND toggle; keyboard support.
- Embedded "Press Start 2P" font (Base64) – zero external requests.
- Inline web-app manifest and iOS meta tags for "Add to Home Screen" without a developer account.
- GPL-3.0 license, security/privacy documentation.
