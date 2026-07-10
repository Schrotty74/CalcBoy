# 📖 CALC BOY Manual

🇩🇪 [Deutsche Anleitung](MANUAL.de.md)

CALC BOY is a Nintendo-style calculator PWA. This manual documents the current app behavior.

## Getting started

Open https://schrotty74.github.io/CalcBoy/ in your browser.

On iPhone, open the page in Safari and add it to the Home Screen. CALC BOY then launches as a fullscreen PWA. The layout respects the iOS Safe Area, so `THEME`, `GAME` and `SND` stay below the status bar.

After the first load the app works offline through the service worker.

Numbers are displayed in German number format:
- comma as decimal separator
- dot as thousands separator

## Top buttons

- **THEME**: cycles through the console themes.
- **GAME**: opens the game menu. During a game, it exits the game.
- **SND**: toggles 8-bit key sounds.

Available themes:
1. Game Boy
2. GB Color
3. NES
4. Super NES
5. Switch
6. Famicom
7. Virtual Boy, unlocked by the secret code

The selected theme is saved locally.

## Display gestures

- **Tap the LCD**: opens the history.
- **Long-press the LCD**: copies the current result to the clipboard.
- **M indicator**: memory contains a stored value.

The history contains the last 10 calculations. Tap an entry to reuse its result. The history also shows:
- **Σ**: sum of stored results
- **Ø**: average of stored results

History export:
- `TEILEN / EXPORT` exports the history as text through the share sheet or clipboard.
- `PNG EXPORT` exports the history as a PNG image in CALC BOY display style.

## Page navigation

The page order is:

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

- **EXT** opens the extended pages.
- **MEHR** cycles to the next extended page.
- **BASIC** returns to the standard keypad.

## BASIC page

Standard calculator page.

Buttons:
- Digits `0–9`
- comma
- `+`, `−`, `×`, `÷`
- **AC**: clears input, operator state and menus
- **±**: toggles sign
- **%**: smart percent
- **√**: square root
- **=**: evaluates
- **EXT**: opens extended pages

Smart percent examples:
- `100 + 10 % = 110`
- `50 × 10 % = 5`
- `10 % = 0.1`

Invalid operations show `ERROR`. Entering a digit starts fresh.

## EXT page

Scientific and memory functions.

Memory:
- **MC**: clear memory
- **MR**: recall memory
- **M+**: add current value to memory
- **M−**: subtract current value from memory

Scientific functions:
- `sin`, `cos`, `tan`
- `DEG` / `RAD`
- `log`, `ln`
- `10^x`, `e^x`
- `x²`, `x³`, `xʸ`
- cube root
- `1/x`
- `n!`
- `π`, `e`

## CONV page

Unit conversion page.

Conversions:
- km ↔ mi
- m ↔ ft
- °C ↔ °F
- kg ↔ lb
- cm ↔ in
- liter ↔ gallon (US)
- km/h ↔ mph
- hours ↔ minutes
- VAT 19% net ↔ gross
- VAT 7% net ↔ gross

## FIN page

Finance page.

Stored parameters:
- **SET K0**: initial capital
- **SET P%**: annual interest rate
- **SET JAHRE**: years
- **SET RATE/M**: monthly savings rate
- **SET PERS**: number of people
- **SET KURS**: manual exchange rate

Results:
- **ENDWERT**: final value with monthly compounding
- **ZINSEN**: interest earned only
- **INFO**: compact summary with end value, total paid in and interest earned
- **RESET**: resets finance parameters

Other helpers:
- **TIP+10%**, **TIP+15%**, **TIP+20%**
- **÷ PERS**: split current amount by stored number of people
- **€→$**, **$→€**: manual exchange rate conversion

No live exchange-rate API is used.

## PRG page

Programmer page.

Functions:
- `→HEX`
- `→BIN`
- `→OCT`
- `NOT`
- `AND`
- `OR`
- `XOR`
- `MOD`
- bit shifts `«` and `»`
- `ABS`
- `INT`
- `SGN`
- `ZUFALL`
- constants `π` and `e`
- **RPN** mode toggle

## RPN mode

RPN mode is available on the PRG page.

- Press **RPN** to toggle RPN mode.
- Enter a number and press **=** to push it onto the stack.
- Enter the next number and press an operator to calculate with the previous stack value.
- Supported operators include arithmetic and programmer operators.
- **AC** clears the current input and the RPN stack while RPN mode is active.
- The mode and stack are stored locally.

Example:
1. Enter `2`
2. Press `=`
3. Enter `3`
4. Press `+`
5. Result: `5`

## PLOT page

The plot page draws functions as pixel-style LCD graphs.

Available functions:
- sin x
- cos x
- tan x
- x²
- x³
- √x
- log x
- 1/x
- e^x
- ln x
- |x|
- 2^x
- sinh
- cosh
- tanh
- x⁴
- Gaussian curve
- floor
- sinc x
- x·sin x

Press any key to return from a plot.

## FORM page

Formula Assistant page.

Variables:
- **SET A**: store current value as A
- **SET B**: store current value as B
- **SET C**: store current value as C
- **INFO**: show current formula variables
- **CLR ABC**: clear formula variables

Formulas:
- **% VON**: A percent of B
- **DREISATZ**: rule of three, `B × C / A`
- **KREIS A**: circle area from radius A
- **KREIS U**: circle circumference from radius A
- **PYTH**: hypotenuse from A and B
- **OHM**: voltage from resistance A and current B
- **BMI**: BMI from weight A and height B
- **Ø ABC**: average of A, B and C
- **KM/H**: speed from distance A and time B
- **NET19**: net value from gross value A at 19% VAT
- **BRU19**: gross value from net value A at 19% VAT

Formula variables are stored locally.

## Games

Press **GAME** to open the game menu.

### Math Attack

Mental arithmetic game:
- 30-second rounds
- Easy, Normal and Hard levels
- per-level high score
- PERFECT jingle for flawless rounds

### Snake

Snake game:
- control with `2`, `4`, `6`, `8` or arrow keys
- speed increases over time
- high score is saved
- **AC** quits

## Secret theme unlock

Enter:

`8 8 2 2 4 6 4 6 − +`

This unlocks the Virtual Boy theme, stores it permanently in local storage and makes it available through the **THEME** button.

## Local storage

CALC BOY stores only local data in `localStorage`:
- theme
- sound setting
- history
- unlocked themes
- high scores
- memory value
- angle mode
- finance parameters
- exchange rate
- people count
- RPN mode
- RPN stack
- formula variables

Nothing is sent anywhere.

## Offline behavior

The service worker caches only same-origin app files:
- `./`
- `./index.html`
- `./apple-touch-icon.png`
- `./icon-512.png`

The app uses a cache-first strategy with background refresh.
