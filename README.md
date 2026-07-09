<p align="center">
  <img src="icon-512.png" width="128" height="128" alt="CALC BOY icon">
</p>

<h1 align="center">CALC BOY</h1>

<p align="center">
  🇩🇪 <a href="README.de.md">Deutsche Version</a>
</p>

A calculator in classic Nintendo style – built as a Progressive Web App in a single HTML file (plus a small service worker). No installation, no app store, no external connections, no tracking.

## ▶️ Launch

**[➤ Open CALC BOY now](https://schrotty74.github.io/CalcBoy/)**

## 📱 Install on iPhone

1. Open the link above in **Safari**
2. Tap the **Share icon** → **"Add to Home Screen"**
3. CALC BOY now launches as a full-screen app

## ✨ Features (v3.0)

- 6 console themes: Game Boy, GB Color, NES, Super NES, Switch, Famicom (THEME button) – your choice is remembered
- 🕹️ **MATH ATTACK**: mental math against the clock (GAME menu) with 3 difficulty levels, per-level high scores and a PERFECT jingle for flawless runs
- 🔄 **Unit converter** (CONV page): km↔mi, °C↔°F, kg↔lb, cm↔in, l↔gal, km/h↔mph, h↔min, German VAT (19%/7% net↔gross)
- 📋 **Copy & share**: long-press the display to copy the result; export the history via the share sheet
- 🎵 Each console theme has its own key sound; theme switching plays a cartridge-swap animation
- 🔋 Battery LED shows the real charge level where the browser supports it (Chrome/Android; iOS keeps the classic red LED)
- ➕ **Extended mode** (EXT button): memory (MC/MR/M+/M−), sin/cos/tan with DEG/RAD switch, log, ln, 10^x, e^x, x², x³, xʸ, ∛, 1/x, factorial, π, e
- 💰 **Finance page** (FIN): compound-interest calculator with monthly savings rate, tip & bill splitting, currency conversion with a manually set rate (deliberately no live-rate API – nothing leaves the device)
- 💻 **Programmer page** (PRG): HEX/BIN/OCT display, AND, OR, XOR, NOT, MOD, bit shifts, ABS, INT, SGN, random number
- 📈 **Plot page**: draws sin, cos, tan, x², x³, √x, log x and 1/x as pixel graphs on the LCD
- 🐍 **SNAKE**: second game via the GAME menu, steered with 2/4/6/8 (or arrow keys), own high score
- Smart percent key: `100 + 10 %` gives 110, like a real calculator
- History shows sum (Σ) and average (Ø) of the last results
- 🔬 **Scientific mode**: rotate to landscape for a quick-access function column
- 📜 **History**: tap the display to see your last 10 calculations, tap an entry to reuse its result
- Basic arithmetic, percent, sign toggle, square root
- Boot animation and 8-bit sounds, mutable (SND button)
- German number format (decimal comma, thousands separators)
- Works offline via service worker; all data stays on your device
- 🥚 Legend has it an old code unlocks a seventh console …

## 📖 Manual

The full manual is in [MANUAL.md](MANUAL.md) (🇩🇪 [deutsch](MANUAL.de.md)).

## 🤖 Ask an AI about CALC BOY

One tap opens an AI chat that already knows the manual (it is embedded in the prompt – no web access needed):

- [**Ask ChatGPT**](https://chatgpt.com/?q=You%20are%20an%20expert%20on%20the%20CALC%20BOY%20calculator%20app%20%28Nintendo-style%20PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Answer%20questions%20based%20on%20this%20condensed%20manual%3A%0ATOP%3A%20THEME%20cycles%206%20console%20looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%3B%20saved%29.%20GAME%20opens%20the%20game%20menu.%20SND%20toggles%208-bit%20sounds.%0ADISPLAY%3A%20Tap%20%3D%20history%20%28last%2010%20calculations%2C%20tap%20entry%20to%20reuse%20result%2C%20shows%20sum%2Faverage%2C%20TEILEN%20exports%29.%20Long-press%20%3D%20copy%20result.%20M%20top-left%20%3D%20memory%20in%20use.%0APAGES%20%28EXT%20button%2C%20then%20MEHR%20to%20cycle%2C%20BASIC%20to%20return%29%3A%20BASIC%20%3D%20arithmetic%2C%20smart%20%25%20key%20%28100%2B10%25%3D110%29%2C%20square%20root%2C%20%2B%2F-.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20with%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20x2%2C%20x3%2C%20x%5Ey%2C%20cube%20root%2C%201%2Fx%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%2C%20cm%2Fin%2C%20l%2Fgal%2C%20km%2Fh-mph%2C%20h%2Fmin%2C%20German%20VAT%2019%2F7%25%20%28MW%2B19%20net-%3Egross%2C%20MW-19%20gross-%3Enet%29.%20FIN%20%3D%20compound%20interest%3A%20type%20number%2C%20then%20SET%20K0%2FP%25%2FJAHRE%2FRATE%3B%20ENDWERT%20computes%20%28monthly%20compounding%29%2C%20ZINSEN%20interest%20only%2C%20INFO%20shows%20parameters%3B%20tip%20TIP%2B10%2F15%2F20%25%2C%20SET%20PERS%20%2B%20divide-by-PERS%20splits%20bills%3B%20currency%20via%20SET%20KURS%20and%20euro%2Fdollar%20keys%20%28manual%20rate%2C%20no%20live%20data%29.%20PRG%20%3D%20HEX%2FBIN%2FOCT%20display%2C%20AND%2FOR%2FXOR%2FMOD%2Fshifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20random.%20PLOT%20%3D%20draws%2020%20functions%20%28sin%20to%20Gauss%20bell%29%20as%20pixel%20graphs.%0AGAMES%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%20mental%20math%2C%20levels%20Easy%2FNormal%2FHard%2C%20per-level%20high%20score%2C%20flawless%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%28steer%20with%202%2F4%2F6%2F8%20or%20arrows%2C%20speeds%20up%2C%20high%20score%29.%20AC%20quits.%0ASECRET%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20unlocks%20the%20VIRTUAL%20BOY%20theme.%0AMISC%3A%20Everything%20is%20stored%20locally%20only%20%28theme%2C%20sound%2C%20history%2C%20high%20scores%2C%20memory%2C%20angle%20mode%2C%20FIN%20parameters%2C%20rate%29%2C%20no%20external%20connections%2C%20works%20offline%2C%20GPL-3.0.%20Battery%20LED%20shows%20charge%20only%20on%20Android%2FChrome.%20Full%20manual%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.md%0ANow%20ask%20me%20what%20you%20want%20to%20know.)
- [**Ask Claude**](https://claude.ai/new?q=You%20are%20an%20expert%20on%20the%20CALC%20BOY%20calculator%20app%20%28Nintendo-style%20PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Answer%20questions%20based%20on%20this%20condensed%20manual%3A%0ATOP%3A%20THEME%20cycles%206%20console%20looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%3B%20saved%29.%20GAME%20opens%20the%20game%20menu.%20SND%20toggles%208-bit%20sounds.%0ADISPLAY%3A%20Tap%20%3D%20history%20%28last%2010%20calculations%2C%20tap%20entry%20to%20reuse%20result%2C%20shows%20sum%2Faverage%2C%20TEILEN%20exports%29.%20Long-press%20%3D%20copy%20result.%20M%20top-left%20%3D%20memory%20in%20use.%0APAGES%20%28EXT%20button%2C%20then%20MEHR%20to%20cycle%2C%20BASIC%20to%20return%29%3A%20BASIC%20%3D%20arithmetic%2C%20smart%20%25%20key%20%28100%2B10%25%3D110%29%2C%20square%20root%2C%20%2B%2F-.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20with%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20x2%2C%20x3%2C%20x%5Ey%2C%20cube%20root%2C%201%2Fx%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%2C%20cm%2Fin%2C%20l%2Fgal%2C%20km%2Fh-mph%2C%20h%2Fmin%2C%20German%20VAT%2019%2F7%25%20%28MW%2B19%20net-%3Egross%2C%20MW-19%20gross-%3Enet%29.%20FIN%20%3D%20compound%20interest%3A%20type%20number%2C%20then%20SET%20K0%2FP%25%2FJAHRE%2FRATE%3B%20ENDWERT%20computes%20%28monthly%20compounding%29%2C%20ZINSEN%20interest%20only%2C%20INFO%20shows%20parameters%3B%20tip%20TIP%2B10%2F15%2F20%25%2C%20SET%20PERS%20%2B%20divide-by-PERS%20splits%20bills%3B%20currency%20via%20SET%20KURS%20and%20euro%2Fdollar%20keys%20%28manual%20rate%2C%20no%20live%20data%29.%20PRG%20%3D%20HEX%2FBIN%2FOCT%20display%2C%20AND%2FOR%2FXOR%2FMOD%2Fshifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20random.%20PLOT%20%3D%20draws%2020%20functions%20%28sin%20to%20Gauss%20bell%29%20as%20pixel%20graphs.%0AGAMES%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%20mental%20math%2C%20levels%20Easy%2FNormal%2FHard%2C%20per-level%20high%20score%2C%20flawless%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%28steer%20with%202%2F4%2F6%2F8%20or%20arrows%2C%20speeds%20up%2C%20high%20score%29.%20AC%20quits.%0ASECRET%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20unlocks%20the%20VIRTUAL%20BOY%20theme.%0AMISC%3A%20Everything%20is%20stored%20locally%20only%20%28theme%2C%20sound%2C%20history%2C%20high%20scores%2C%20memory%2C%20angle%20mode%2C%20FIN%20parameters%2C%20rate%29%2C%20no%20external%20connections%2C%20works%20offline%2C%20GPL-3.0.%20Battery%20LED%20shows%20charge%20only%20on%20Android%2FChrome.%20Full%20manual%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.md%0ANow%20ask%20me%20what%20you%20want%20to%20know.)
- **Ask Gemini**: [open Gemini](https://gemini.google.com/app) and paste the prompt below (Gemini doesn't support prefilled links):

<details><summary>Prompt to copy</summary>

```
You are an expert on the CALC BOY calculator app (Nintendo-style PWA, schrotty74.github.io/CalcBoy). Answer questions based on this condensed manual:
TOP: THEME cycles 6 console looks (Game Boy, GB Color, NES, SNES, Switch, Famicom; saved). GAME opens the game menu. SND toggles 8-bit sounds.
DISPLAY: Tap = history (last 10 calculations, tap entry to reuse result, shows sum/average, TEILEN exports). Long-press = copy result. M top-left = memory in use.
PAGES (EXT button, then MEHR to cycle, BASIC to return): BASIC = arithmetic, smart % key (100+10%=110), square root, +/-. EXT = MC/MR/M+/M-, sin/cos/tan with DEG/RAD, log, ln, 10^x, e^x, x2, x3, x^y, cube root, 1/x, n!, Pi, e. CONV = km/mi, C/F, kg/lb, cm/in, l/gal, km/h-mph, h/min, German VAT 19/7% (MW+19 net->gross, MW-19 gross->net). FIN = compound interest: type number, then SET K0/P%/JAHRE/RATE; ENDWERT computes (monthly compounding), ZINSEN interest only, INFO shows parameters; tip TIP+10/15/20%, SET PERS + divide-by-PERS splits bills; currency via SET KURS and euro/dollar keys (manual rate, no live data). PRG = HEX/BIN/OCT display, AND/OR/XOR/MOD/shifts, NOT, ABS, INT, SGN, random. PLOT = draws 20 functions (sin to Gauss bell) as pixel graphs.
GAMES (GAME): 1/2/3 = MATH ATTACK (30s mental math, levels Easy/Normal/Hard, per-level high score, flawless = PERFECT). 5 = SNAKE (steer with 2/4/6/8 or arrows, speeds up, high score). AC quits.
SECRET: Code 8 8 2 2 4 6 4 6 - + unlocks the VIRTUAL BOY theme.
MISC: Everything is stored locally only (theme, sound, history, high scores, memory, angle mode, FIN parameters, rate), no external connections, works offline, GPL-3.0. Battery LED shows charge only on Android/Chrome. Full manual: schrotty74.github.io/CalcBoy/MANUAL.md
Now ask me what you want to know.
```

</details>

## ⌨️ Keyboard (Mac/iPad)

Digits, `+ - * /`, `Enter` = result, `Esc` = AC, `%`, `R` or `W` = square root

## 🔒 Privacy

No external requests, no tracking, no analytics. Settings, history and high score are stored locally in your browser only. Details in [SECURITY.md](SECURITY.md).

## 📄 License

[GPL-3.0](LICENSE) – Font "Press Start 2P" by CodeMan38, licensed under the SIL Open Font License 1.1.


## New in this version

- 7 Game Boy themes (including unlockable Virtual Boy)
- Improved Safe Area support for iPhone PWAs
