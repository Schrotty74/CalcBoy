# 📖 CALC BOY Manual (v3.0)

🇩🇪 [Deutsche Anleitung](MANUAL.de.md)

CALC BOY is a calculator PWA in classic Nintendo style. This manual explains every button, page and hidden feature.

## Getting started

Open https://schrotty74.github.io/CalcBoy/ in your browser. On iPhone: open it in Safari, tap Share → "Add to Home Screen" to install it as a full-screen app. After the first load it works completely offline.

On startup you see a short boot animation ("CALC BOY" drops into the screen). Numbers use the German format: comma as decimal separator, dots as thousands separators.

## The three top buttons

- **THEME** (top left): cycles through the console looks – Game Boy, GB Color, NES, Super NES, Switch, Famicom. Each theme also changes the key sound. Your choice is saved. Switching plays a short cartridge-swap animation.
- **GAME** (top center): opens the game menu (see Games below). Pressing it during a game quits the game.
- **SND** (top right): toggles the 8-bit key sounds on/off. Saved.

## Display (LCD) gestures

- **Tap** the display: opens the **history** – your last 10 calculations. Tap an entry to reuse its result. Below the entries you see **Σ** (sum) and **Ø** (average) of the results. The top row **» TEILEN / EXPORT** shares the history as text (share sheet or clipboard).
- **Long-press** the display (~0.5 s): copies the current result to the clipboard.
- A small **M** in the top left corner means a value is stored in memory.

## BASIC page (standard keypad)

Digits 0–9, comma, and the four operators ÷ × − +. Further keys:

- **AC**: clears everything (also exits games and menus)
- **±**: toggles the sign
- **%**: smart percent. `100 + 10 %` = 110 (10 % *of 100*), `50 × 10 %` = 5. Standing alone, `10 %` = 0.1
- **√**: square root (negative input shows ERROR)
- **=**: evaluates
- **EXT**: switches to the extended pages

Results longer than 12 digits shrink automatically; impossible operations (e.g. ÷ 0) show **ERROR** – any digit starts fresh.

## Page navigation

**EXT** on the BASIC page leads to the first extra page. On every extra page:
**BASIC** returns to the standard keypad, **MEHR** cycles to the next page (EXT → CONV → FIN → PRG → PLOT → EXT), **=** always evaluates.

## EXT page (scientific)

- **MC / MR / M+ / M−**: memory clear, recall, add, subtract. Memory survives restarts.
- **sin / cos / tan** with the **DEG/RAD** toggle (the button shows the active mode; saved)
- **log** (base 10), **ln** (natural), **10^x**, **e^x**
- **x²**, **x³**, **xʸ** (binary operator: enter base, press xʸ, enter exponent, press =), **∛x**
- **1/x**, **n!** (integers 0–170 only), **π**, **e**

## CONV page (unit converter)

Enter a value, tap a conversion – the result replaces the display and the conversion is named above it. Available: km↔mi, m↔ft, °C↔°F, kg↔lb, cm↔in, l↔gal (US), km/h↔mph, h↔min. The **MW** row handles German VAT: **MW+19** = net→gross (×1.19), **MW−19** = gross→net (÷1.19), same for 7 %.

## FIN page (finance)

**Compound interest with monthly savings:** type a number, then press a SET key to store it as parameter:
- **SET K0** – starting capital
- **SET P%** – interest rate per year
- **SET JAHRE** – duration in years
- **SET RATE/M** – monthly savings amount

**INFO** shows the current parameters, **ENDWERT** computes the final value (monthly compounding), **ZINSEN** shows only the earned interest, **RESET** restores the defaults. Example: K0 1000, P 3, JAHRE 10, RATE 50 → ENDWERT ≈ 8,336.42.

**Tip & split:** first set the number of people (type it, press **SET PERS**), then enter the bill, add **TIP+10/15/20%**, then **÷ PERS** for the amount per person.

**Currency:** set your exchange rate once (type it, **SET KURS**), then convert with **€→$** and **$→€**. Deliberately no live rates – nothing leaves your device. The rate works for any currency pair, the labels are just examples.

All FIN parameters are saved locally.

## PRG page (programmer)

- **→HEX / →BIN / →OCT**: shows the integer part of the display in that base (display value stays decimal)
- **AND / OR / XOR / MOD / « / »**: binary operators – enter first number, operator, second number, **=**. Values are truncated to integers; shifts are « (left) and » (right)
- **NOT**: bitwise complement (~x), **ABS**, **INT** (truncate), **SGN** (sign: −1/0/1)
- **ZUFALL**: random integer 1–100

## PLOT page

Tap one of 20 functions (from sin, cos and tan over e^x, sinh/cosh/tanh and |x| up to the Gauss bell e^(−x²), floor, sinc and x·sin x) – it is drawn as a pixel graph on the LCD, with axes where visible. Any key or a tap on the display closes the plot.

## Games (GAME button)

The GAME menu shows: **1 2 3** start MATH ATTACK at that level, **5** starts SNAKE, **AC** cancels.

**MATH ATTACK:** 30 seconds of mental arithmetic. A task appears in the top display line, type the answer, press **=**. Correct = 1 point, wrong = counted as mistake, either way the next task appears. Levels: 1 EASY (small ±), 2 NORMAL (± up to 99, × ÷ up to 12), 3 HARD (± up to 999, × ÷ up to 19). Each level keeps its own high score. Finish a round without a single mistake and you get a **PERFECT!** with its own jingle. **AC** quits early.

**SNAKE:** steer with **2** (down), **4** (left), **6** (right), **8** (up) – or the arrow keys on a physical keyboard. Eat the food to grow; the game speeds up with every bite. Walls and your own tail end the game. High score is saved. **AC** or **GAME** quits.

## Keyboard shortcuts (Mac/iPad with keyboard)

Digits, `+ - * /`, `Enter` = result, `Esc` = AC, `%` percent, `R` or `W` = square root. Arrow keys steer SNAKE.

## Secrets 🥚

There is a seventh console. Old players remember the code… on the calculator keys it is: **8 8 2 2 4 6 4 6 − +** (on a keyboard: ↑ ↑ ↓ ↓ ← → ← → B A). Once entered, the **VIRTUAL BOY** theme (red on black) is permanently unlocked and joins the THEME rotation.

## Storage & privacy

Everything is stored locally in your browser only: theme, sound, history, high scores, memory value, angle mode, finance parameters, exchange rate. Nothing is transmitted anywhere. To wipe everything, delete the website data for this domain in your browser. Details: [SECURITY.md](SECURITY.md).

## Troubleshooting

- **No sound on the very first start:** browsers block audio before the first touch – press any key once.
- **Old version after an update:** the service worker caches the app; close the app/tab completely and reopen it, twice if needed.
- **Battery LED always red:** the Battery API only exists in Chrome/Android. On iPhone the LED stays classic red – like the original Game Boy.

---

## Recent changes

### Finance
- **INFO** now displays a compact summary:
  - End value
  - Total paid in
  - Interest earned

### iPhone PWA
- Improved Safe Area support so the top buttons remain accessible below the status bar.

> If available in your build:
> - Formula Assistant
> - RPN mode
> - History PNG export
