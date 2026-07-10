# 📖 CALC BOY Manual (v3.1.0)

🇩🇪 [Deutsche Anleitung](MANUAL.de.md)

CALC BOY is a calculator PWA in classic Nintendo style. This manual mirrors the app's structure: one chapter per page, with every key explained individually.

## Contents

1. [Getting started](#getting-started)
2. [Operating concept](#operating-concept)
3. [The three top buttons](#the-three-top-buttons)
4. [The display (LCD)](#the-display-lcd)
5. [BASIC page](#basic-page)
6. [EXT page (scientific)](#ext-page-scientific)
7. [CONV page (units)](#conv-page-units)
8. [FIN page (finance)](#fin-page-finance)
9. [PRG page (programmer & RPN)](#prg-page-programmer--rpn)
10. [PLOT page (function graphs)](#plot-page-function-graphs)
11. [FORM page (formula assistant)](#form-page-formula-assistant)
12. [Games](#games)
13. [Landscape mode](#landscape-mode)
14. [Keyboard shortcuts](#keyboard-shortcuts)
15. [Secret theme unlock](#secret-theme-unlock)
16. [Storage & privacy](#storage--privacy)
17. [Troubleshooting](#troubleshooting)

## Getting started

Open https://schrotty74.github.io/CalcBoy/ in your browser. On iPhone: open it in Safari, tap Share → "Add to Home Screen" – CALC BOY then launches as a full-screen app. After the first load everything works completely offline.

A short boot animation plays on startup. Numbers use the German format: comma as decimal separator, dots as thousands separators. Up to 12 digits can be entered; long results shrink automatically. Impossible operations (e.g. division by 0) show **ERROR** – the next digit starts fresh.

## Operating concept

The app has three areas: the **pill buttons on top** (THEME, GAME, SND), the **LCD** and the **keypad**. The keypad has seven pages:

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

- **EXT** (bottom left on the BASIC page) opens the first extra page.
- **MEHR** (on every extra page) cycles to the next page.
- **BASIC** (on every extra page) returns to the standard keypad.
- **=** works on every page.

## The three top buttons

**THEME** (left) – switches to the next console look. Six themes are available: Game Boy (default), GB Color, NES, Super NES, Switch and Famicom; a seventh (Virtual Boy) is unlockable (see [Secret theme unlock](#secret-theme-unlock)). The name flashes in the LCD, switching plays a cartridge-swap animation, and each theme has its own key sound (NES darker, Switch brighter etc.). Your choice is saved.

**GAME** (center) – opens the game menu (see [Games](#games)). During a running game the button quits the game.

**SND** (right) – toggles the 8-bit key sounds on (SND ON) or off (SND OFF, button dims). Saved.

## The display (LCD)

The LCD has two lines: the **status line** on top (running calculation, messages, game state) and the **result line** below. A small **M** in the top-left corner means the memory (M+/M−) holds a non-zero value.

**Tapping the display** opens the **history**:
- Shows the last 10 calculations with their results.
- **Tap an entry** to bring its result back into the display.
- **» TEILEN / EXPORT** exports the history as text via the share sheet (or clipboard).
- **» PNG TEILEN** renders the history as an image and shares/downloads it as a PNG file.
- Below the entries you see **Σ** (sum of all results) and **Ø** (their average).
- Tapping again (or any key) closes the history.

**Long-pressing** (~0.5 s) the display copies the current result to the clipboard ("KOPIERT" appears).

## BASIC page

Keys: `AC ± % √ | 7 8 9 ÷ | 4 5 6 × | 1 2 3 − | 0 , + | EXT =`

- **0–9** – digit entry (max. 12 digits).
- **,** – decimal comma. Only one comma per number.
- **÷ × − +** – basic arithmetic. Chained calculations evaluate left to right: `2 + 3 × 4 =` gives 20 (first 2+3, then ×4) – like a classic desk calculator, without operator precedence.
- **=** – evaluates and writes the calculation to the history. (In RPN mode: pushes the number onto the stack, see [PRG page](#prg-page-programmer--rpn).)
- **AC** – clears the entry and the running calculation. Also exits games/menus; in RPN mode AC additionally clears the stack.
- **±** – toggles the sign of the displayed number.
- **%** – smart percent key with three cases:
  - After **+ or −**: percent of the first operand. `100 + 10 %` → 110; `200 − 25 %` → 150.
  - After **× or ÷**: converts to the factor. `50 × 10 %` → 5.
  - **Standalone**: divides by 100. `10 %` → 0.1.
- **√** – square root of the displayed number. Negative input → ERROR.
- **EXT** – switches to the extra pages.

## EXT page (scientific)

Keys: `MC MR M+ M− | sin cos tan DEG | log ln 10^x e^x | x² x³ xʸ ∛x | 1/x n! π e | BASIC MEHR =`

**Memory:**
- **MC** – clears the memory (M indicator disappears).
- **MR** – recalls the memory value into the display.
- **M+** – adds the displayed number to memory.
- **M−** – subtracts the displayed number from memory.
- Memory survives restarts; while it is ≠ 0 the LCD shows an **M**.

**Trigonometry:**
- **sin / cos / tan** – apply the function immediately to the displayed number. Example (DEG): `30` → sin → 0.5.
- **DEG/RAD** – toggles the angle mode: **DEG** = degrees, **RAD** = radians. The button shows the active mode; the setting is saved and applies to all trigonometry keys.

**Logarithms & exponentials:**
- **log** – base-10 logarithm. `1000` → log → 3.
- **ln** – natural logarithm (base e).
- **10^x** – power of ten. `3` → 10^x → 1000.
- **e^x** – e to the power of x.

**Powers & roots:**
- **x²** / **x³** – square / cube of the displayed number.
- **xʸ** – arbitrary power as a *two-step* operation: enter the base → press xʸ → enter the exponent → **=**. Example: `2` xʸ `10` = → 1,024.
- **∛x** – cube root. `27` → ∛x → 3.

**Miscellaneous:**
- **1/x** – reciprocal. `4` → 1/x → 0.25.
- **n!** – factorial. Integers 0–170 only; otherwise ERROR. `5` → n! → 120.
- **π / e** – put the constant (3.1415926536 / 2.7182818285) into the display.

## CONV page (units)

Principle: **enter a value, tap a conversion key** – the result replaces the display, and the status line names the conversion. Every conversion can be reversed with its counterpart key.

- **km→mi / mi→km** – kilometers ↔ miles (×0.621371 / ×1.609344).
- **m→ft / ft→m** – meters ↔ feet (×3.28084 / ×0.3048).
- **°C→°F / °F→°C** – temperature (`×9/5+32` and `(−32)×5/9`). `100` °C→°F → 212.
- **kg→lb / lb→kg** – kilograms ↔ pounds (×2.204623 / ×0.453592).
- **cm→in / in→cm** – centimeters ↔ inches (÷2.54 / ×2.54).
- **l→gal / gal→l** – liters ↔ US gallons (×0.264172 / ×3.785412).
- **km/h→mph / mph→km/h** – speed (same factors as km/mi).
- **h→min / min→h** – hours ↔ minutes (×60 / ÷60). `90` min→h → 1.5.
- **MW+19 / MW−19** – German VAT 19 %: **MW+19** converts net→gross (×1.19), **MW−19** converts gross→net (÷1.19, *not* −19 %!). `119` MW−19 → 100.
- **MW+7 / MW−7** – the same with the reduced 7 % rate (×1.07 / ÷1.07).

## FIN page (finance)

This page works with **stored parameters**: type a number, then assign it with a SET key. All parameters survive restarts.

**Compound interest with savings rate:**
- **SET K0** – stores the display as starting capital.
- **SET P%** – stores the annual interest rate in percent.
- **SET JAHRE** – stores the duration in years.
- **SET RATE/M** – stores the monthly savings amount.
- **INFO** – shows the summary: end value, total paid in and interest earned.
- **ENDWERT** – computes the final capital with **monthly compounding**: `K0·(1+i)^m + rate·((1+i)^m−1)/i` with `i = P/1200` and `m = years·12`. Example: K0 = 1,000, P = 3, years = 10, rate = 50 → **8,336.42**. The result goes to the history.
- **ZINSEN** – shows only the interest earned (end value − K0 − all payments). In the example: 1,336.42.
- **RESET** – restores all FIN parameters to defaults (K0 1000, P 3, years 10, rate 50, persons 2, rate 1.08).

**Tip & bill splitting:**
- **TIP+10% / TIP+15% / TIP+20%** – adds the tip to the displayed bill. `85` TIP+15% → 97.75.
- **SET PERS** – stores the displayed number as the number of people (minimum 1, rounded).
- **÷ PERS** – divides the display by the stored number of people. Complete flow: `4` SET PERS → `85` TIP+15% → ÷ PERS → **24.44 per person**.

**Currency:**
- **SET KURS** – stores the display as the exchange rate (e.g. 1.08 for EUR→USD).
- **€→$** – multiplies by the rate. **$→€** – divides by the rate.
- Deliberately **without live rates** (nothing leaves the device). The rate works for any currency pair – €/$ is only the example labeling.

## PRG page (programmer & RPN)

All bit operations use the **integer part** of the values (decimals are truncated).

**Base display:**
- **→HEX / →BIN / →OCT** – shows the integer part of the display in hexadecimal, binary or octal in the status line. The display itself stays decimal. `255` →HEX → "HEX: FF"; `10` →BIN → "BIN: 1010".

**Binary operators** (same flow as ÷/×: first number → operator → second number → =):
- **AND / OR / XOR** – bitwise combination. `12 AND 10 =` → 8; `12 OR 10 =` → 14; `12 XOR 10 =` → 6.
- **MOD** – remainder of a division. `17 MOD 5 =` → 2.
- **«** – bit shift left (×2 per position). `1 « 4 =` → 16.
- **»** – bit shift right (÷2 per position). `255 » 4 =` → 15.

**Unary functions** (apply immediately):
- **NOT** – bitwise complement (~x). `5` → NOT → −6.
- **ABS** – absolute value. `-7` → ABS → 7.
- **INT** – truncates decimals. `3.9` → INT → 3.
- **SGN** – sign function: −1, 0 or 1.
- **ZUFALL** – random number between 1 and 100.
- **π / e** – constants as on the EXT page.

**RPN mode (Reverse Polish Notation):**
- **RPN** – toggles the mode on/off (saved; the status line shows stack depth and top value). While active, the mode applies **on every page**.
- In RPN mode the meaning of = and the operators changes:
  - **=** pushes the displayed number onto the **stack** (max. 8 entries, stored locally).
  - An **operator** (÷ × − + xʸ AND …) takes the top stack value as the first operand and combines it with the display. Example: `3` = `4` + → **7**.
  - **AC** additionally clears the stack.
- Calculations appear in the history with an "RPN" prefix.

## PLOT page (function graphs)

Tap a function key – the graph is drawn as pixel art on the LCD, with axes (where visible) and automatic scaling. **Any key or a tap on the display closes the plot.** The 20 functions and their ranges:

| Key | Function | Range |
|---|---|---|
| sin x / cos x | sine / cosine | −6.5…6.5 |
| tan x | tangent (poles blanked) | −6.5…6.5 |
| x² / x³ / x⁴ | powers | −4…4 / −3…3 / −2.5…2.5 |
| √x | square root | 0…16 |
| log x / ln x | logarithms | 0.05…20 / 0.05…12 |
| 1/x | hyperbola (pole blanked) | −4…4 |
| e^x / 2^x | exponentials | −3…3 / −3…4 |
| \|x\| | absolute value | −4…4 |
| sinh / cosh / tanh | hyperbolic functions | −3…3 / −3…3 / −4…4 |
| GAUSS | bell curve e^(−x²) | −3.5…3.5 |
| FLOOR | step function ⌊x⌋ | −4…4 |
| sinc x | sin x ⁄ x | −15…15 |
| x·sin x | growing oscillation | −12…12 |

## FORM page (formula assistant)

This page works with three **variables A, B and C**: type values and assign them, then press a formula key. The variables stay stored until overwritten or cleared.

**Managing variables:**
- **SET A / SET B / SET C** – stores the displayed number as A, B or C.
- **INFO** – shows the current values of A, B and C.
- **CLR ABC** – resets all three variables to 0.

**Formulas** (each with variable roles and an example):
- **% VON** – A percent of B: `B·A/100`. A = 15, B = 200 → **30**.
- **DREISATZ** – rule of three `A : B = C : x`, result `x = B·C/A`. "3 kg cost 6 €, what do 5 kg cost?" → A = 3, B = 6, C = 5 → **10**.
- **KREIS A** – circle area with radius A: `π·A²`. A = 2 → 12.566.
- **KREIS U** – circle circumference with radius A: `2·π·A`. A = 2 → 12.566.
- **PYTH** – hypotenuse from legs A and B: `√(A²+B²)`. A = 3, B = 4 → **5**.
- **OHM** – voltage from Ohm's law `U = R·I` with A = resistance (Ω) and B = current (A). A = 100, B = 0.5 → **50 V**.
- **BMI** – body mass index `A / B²` with A = weight (kg) and B = height (m). A = 80, B = 1.8 → **24.69**.
- **Ø ABC** – average of the three variables: `(A+B+C)/3`.
- **KM/H** – speed `A / B` with A = distance (km) and B = time (h). A = 150, B = 1.5 → **100 km/h**.
- **NET19** – converts gross→net (19 %): `A / 1.19` with A = gross amount.
- **BRU19** – converts net→gross (19 %): `A · 1.19` with A = net amount.

Every formula result goes to the history; the status line briefly shows the variable roles used.

## Games

**GAME** opens the menu: `1`, `2` or `3` starts MATH ATTACK at that level, `5` starts SNAKE, `AC` cancels.

**MATH ATTACK** – 30 seconds of mental arithmetic. The task appears in the status line, type the answer, press **=**. Correct = 1 point; wrong counts as a mistake; either way the next task appears immediately. The status line shows remaining time (T) and score (S).
- Level 1 **EASY**: only + and − with small numbers (up to 20).
- Level 2 **NORMAL**: + − up to 99, × ÷ within the 12× tables.
- Level 3 **HARD**: + − up to 999, × ÷ up to 19.
- Each level keeps its **own high score**. A round **without a single mistake** ends with **PERFECT!** and its own jingle. **AC** quits early.

**SNAKE** – the classic on the LCD. Controls: **8** = up, **2** = down, **4** = left, **6** = right (or arrow keys). Eating food grows the snake, and the speed increases with every bite. Walls or your own tail end the game; the high score is saved. **AC** or **GAME** quits.

## Landscape mode

Rotate the iPhone: the layout switches to display on the left, keypad on the right, and an additional **quick-access column** with sin, cos, tan, log, ln, x², 1/x, xʸ, π and e appears next to the BASIC keypad. All extra pages work in landscape too.

## Keyboard shortcuts

On Mac/iPad with a keyboard: digits, `+ - * /`, `Enter` = result, `Esc` = AC, `%` = percent, `R` or `W` = square root. Arrow keys steer SNAKE.

## Secret theme unlock

Enter:

`8 8 2 2 4 6 4 6 − +`

This unlocks the Virtual Boy theme, stores it permanently in local storage and makes it available through the **THEME** button.

## Storage & privacy

Everything is stored **locally in the browser** only: theme, sound, angle mode, calculation history, high scores (per level and for SNAKE), memory value (M), FIN parameters, exchange rate, number of people, RPN mode with its stack, and the formula variables A/B/C. Nothing is transmitted anywhere; there are no external connections. To wipe everything, delete the website data for this domain in your browser. Details: [SECURITY.md](SECURITY.md).

## Troubleshooting

- **No sound on the very first start:** browsers block audio before the first touch – press any key once.
- **Old version after an update:** the service worker caches the app; close the app/tab completely and reopen it twice.
- **Battery LED always red:** the Battery API only exists in Chrome/Android. On iPhone the LED stays classic red – like the original Game Boy.
- **= stores numbers instead of calculating:** RPN mode is active – turn it off with **RPN** on the PRG page.
