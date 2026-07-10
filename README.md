<p align="center">
  <img src="icon-512.png" width="128" height="128" alt="CALC BOY icon">
</p>

<h1 align="center">CALC BOY</h1>

<p align="center">
  🇩🇪 <a href="README.de.md">Deutsche Version</a>
</p>

<p align="center">
  <strong>Classic Nintendo-style calculator PWA</strong><br>
  One HTML file, offline-capable, local-only, no tracking.
</p>

> 📋 **Latest changes:** See [CHANGELOG.md](CHANGELOG.md).

## ▶️ Launch

**[➤ Open CALC BOY now](https://schrotty74.github.io/CalcBoy/)**

## 📱 Install on iPhone

1. Open the link above in **Safari**.
2. Tap the **Share** button.
3. Choose **Add to Home Screen**.
4. CALC BOY launches as a fullscreen PWA.

The app supports the iPhone PWA Safe Area, so the top buttons stay reachable below the iOS status bar.

## ✨ Features

- 🎮 **6 console themes + 1 unlockable Virtual Boy theme**: Game Boy, GB Color, NES, Super NES, Switch and Famicom are available immediately. The Virtual Boy theme can be unlocked with the secret code.
- 🧮 **Basic calculator**: arithmetic, smart percent logic, sign toggle and square root.
- ➕ **Extended scientific page**: memory keys, trigonometry, DEG/RAD, logarithms, powers, roots, factorial, π and e.
- 🔄 **Unit conversion page**: distance, temperature, weight, length, volume, speed, time and German VAT 19% / 7%.
- 💰 **Finance page**: compound interest, monthly savings rate, interest-only result, tips, bill splitting and manual currency conversion.
- ℹ️ **Finance INFO summary**: shows end value, total paid in and interest earned.
- 💻 **Programmer page**: HEX, BIN, OCT, bitwise operators, shifts, ABS, INT, SGN and random number.
- 🧮 **RPN mode** on the programmer page with a locally stored stack.
- 📈 **Plot page** with 20 pixel-style function graphs.
- 📐 **Formula Assistant** for percent, rule of three, circle, Pythagoras, Ohm, BMI, average, speed and VAT helpers.
- 📜 **History**: last 10 calculations, tap-to-reuse, sum and average.
- 📤 **History export** as text and PNG.
- 🎵 Theme-specific 8-bit key sounds, optional sound toggle and cartridge-style theme animation.
- 🕹️ **Math Attack** and **Snake** mini games.
- 🔋 Battery LED where the browser supports the Battery Status API.
- 🔒 Local-only storage. No external requests, no analytics, no tracking.

## 🧭 Pages

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

Use **EXT**, then **MEHR**, to cycle through the extra pages. Use **BASIC** to return to the standard keypad.

## 🔐 Privacy

CALC BOY stores settings and history only in the browser via `localStorage`. Nothing leaves the device. The embedded font avoids font-CDN requests. The service worker caches only same-origin app files.

More details: [SECURITY.md](SECURITY.md)

## 🤖 Ask an AI about CALC BOY

One tap opens an AI chat that already knows the manual (it is embedded in the prompt – no web access needed):

- [**Ask ChatGPT**](https://chatgpt.com/?q=You%20are%20an%20expert%20on%20the%20CALC%20BOY%20calculator%20app%20%28Nintendo-style%20PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Answer%20questions%20based%20on%20this%20condensed%20manual%3A%0ATOP%3A%20THEME%20cycles%207%20console%20looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%20%2B%20unlockable%20Virtual%20Boy%29.%20GAME%20opens%20the%20game%20menu.%20SND%20toggles%208-bit%20sounds.%0ADISPLAY%3A%20Tap%20%3D%20history%20%28last%2010%20calculations%2C%20tap%20entry%20to%20reuse%20result%2C%20shows%20sum%2Faverage%2C%20export%20as%20text%20or%20PNG%29.%20Long-press%20%3D%20copy%20result.%20M%20top-left%20%3D%20memory%20in%20use.%0APAGES%20%28EXT%20button%2C%20then%20MEHR%3A%20BASIC%20-%3E%20EXT%20-%3E%20CONV%20-%3E%20FIN%20-%3E%20PRG%20-%3E%20PLOT%20-%3E%20FORM%29%3A%20BASIC%20%3D%20arithmetic%2C%20smart%20%25%20key%20%28100%2B10%25%3D110%29%2C%20square%20root.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20with%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20powers%2C%20roots%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20units%20%28km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%20etc.%29%20and%20German%20VAT%2019%2F7%25.%20FIN%20%3D%20compound%20interest%20%28SET%20K0%2FP%25%2FJAHRE%2FRATE%2C%20ENDWERT%2C%20ZINSEN%3B%20INFO%20shows%20end%20value%2C%20paid-in%20total%2C%20interest%29%2C%20tips%2C%20bill%20splitting%2C%20currency%20with%20manual%20rate.%20PRG%20%3D%20HEX%2FBIN%2FOCT%2C%20AND%2FOR%2FXOR%2FMOD%2Fshifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20random%2C%20plus%20an%20RPN%20mode%20with%20stack.%20PLOT%20%3D%2020%20functions%20as%20pixel%20graphs.%20FORM%20%3D%20formula%20assistant%20with%20variables%20A%2FB%2FC%3A%20percent-of%2C%20rule%20of%20three%2C%20circle%2C%20Pythagoras%2C%20Ohm%2C%20BMI%2C%20average%2C%20speed%2C%20VAT.%0AGAMES%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%2C%20levels%20Easy%2FNormal%2FHard%2C%20per-level%20high%20score%2C%20flawless%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%282%2F4%2F6%2F8%20or%20arrows%29.%20AC%20quits.%0ASECRET%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20unlocks%20the%20VIRTUAL%20BOY%20theme.%0AMISC%3A%20Everything%20stored%20locally%20only%2C%20no%20external%20connections%2C%20works%20offline%2C%20GPL-3.0.%20Full%20manual%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.md%0ANow%20ask%20me%20what%20you%20want%20to%20know.)
- [**Ask Claude**](https://claude.ai/new?q=You%20are%20an%20expert%20on%20the%20CALC%20BOY%20calculator%20app%20%28Nintendo-style%20PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Answer%20questions%20based%20on%20this%20condensed%20manual%3A%0ATOP%3A%20THEME%20cycles%207%20console%20looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%20%2B%20unlockable%20Virtual%20Boy%29.%20GAME%20opens%20the%20game%20menu.%20SND%20toggles%208-bit%20sounds.%0ADISPLAY%3A%20Tap%20%3D%20history%20%28last%2010%20calculations%2C%20tap%20entry%20to%20reuse%20result%2C%20shows%20sum%2Faverage%2C%20export%20as%20text%20or%20PNG%29.%20Long-press%20%3D%20copy%20result.%20M%20top-left%20%3D%20memory%20in%20use.%0APAGES%20%28EXT%20button%2C%20then%20MEHR%3A%20BASIC%20-%3E%20EXT%20-%3E%20CONV%20-%3E%20FIN%20-%3E%20PRG%20-%3E%20PLOT%20-%3E%20FORM%29%3A%20BASIC%20%3D%20arithmetic%2C%20smart%20%25%20key%20%28100%2B10%25%3D110%29%2C%20square%20root.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20with%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20powers%2C%20roots%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20units%20%28km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%20etc.%29%20and%20German%20VAT%2019%2F7%25.%20FIN%20%3D%20compound%20interest%20%28SET%20K0%2FP%25%2FJAHRE%2FRATE%2C%20ENDWERT%2C%20ZINSEN%3B%20INFO%20shows%20end%20value%2C%20paid-in%20total%2C%20interest%29%2C%20tips%2C%20bill%20splitting%2C%20currency%20with%20manual%20rate.%20PRG%20%3D%20HEX%2FBIN%2FOCT%2C%20AND%2FOR%2FXOR%2FMOD%2Fshifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20random%2C%20plus%20an%20RPN%20mode%20with%20stack.%20PLOT%20%3D%2020%20functions%20as%20pixel%20graphs.%20FORM%20%3D%20formula%20assistant%20with%20variables%20A%2FB%2FC%3A%20percent-of%2C%20rule%20of%20three%2C%20circle%2C%20Pythagoras%2C%20Ohm%2C%20BMI%2C%20average%2C%20speed%2C%20VAT.%0AGAMES%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%2C%20levels%20Easy%2FNormal%2FHard%2C%20per-level%20high%20score%2C%20flawless%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%282%2F4%2F6%2F8%20or%20arrows%29.%20AC%20quits.%0ASECRET%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20unlocks%20the%20VIRTUAL%20BOY%20theme.%0AMISC%3A%20Everything%20stored%20locally%20only%2C%20no%20external%20connections%2C%20works%20offline%2C%20GPL-3.0.%20Full%20manual%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.md%0ANow%20ask%20me%20what%20you%20want%20to%20know.)
- **Ask Gemini**: [open Gemini](https://gemini.google.com/app) and paste the prompt below (Gemini doesn't support prefilled links):

<details><summary>Prompt to copy</summary>

```
You are an expert on the CALC BOY calculator app (Nintendo-style PWA, schrotty74.github.io/CalcBoy). Answer questions based on this condensed manual:
TOP: THEME cycles 7 console looks (Game Boy, GB Color, NES, SNES, Switch, Famicom + unlockable Virtual Boy). GAME opens the game menu. SND toggles 8-bit sounds.
DISPLAY: Tap = history (last 10 calculations, tap entry to reuse result, shows sum/average, export as text or PNG). Long-press = copy result. M top-left = memory in use.
PAGES (EXT button, then MEHR: BASIC -> EXT -> CONV -> FIN -> PRG -> PLOT -> FORM): BASIC = arithmetic, smart % key (100+10%=110), square root. EXT = MC/MR/M+/M-, sin/cos/tan with DEG/RAD, log, ln, 10^x, e^x, powers, roots, n!, Pi, e. CONV = units (km/mi, C/F, kg/lb etc.) and German VAT 19/7%. FIN = compound interest (SET K0/P%/JAHRE/RATE, ENDWERT, ZINSEN; INFO shows end value, paid-in total, interest), tips, bill splitting, currency with manual rate. PRG = HEX/BIN/OCT, AND/OR/XOR/MOD/shifts, NOT, ABS, INT, SGN, random, plus an RPN mode with stack. PLOT = 20 functions as pixel graphs. FORM = formula assistant with variables A/B/C: percent-of, rule of three, circle, Pythagoras, Ohm, BMI, average, speed, VAT.
GAMES (GAME): 1/2/3 = MATH ATTACK (30s, levels Easy/Normal/Hard, per-level high score, flawless = PERFECT). 5 = SNAKE (2/4/6/8 or arrows). AC quits.
SECRET: Code 8 8 2 2 4 6 4 6 - + unlocks the VIRTUAL BOY theme.
MISC: Everything stored locally only, no external connections, works offline, GPL-3.0. Full manual: schrotty74.github.io/CalcBoy/MANUAL.md
Now ask me what you want to know.
```

</details>

## 📖 Documentation

- [Manual](MANUAL.md)
- [Changelog](CHANGELOG.md)
- [Security & Privacy](SECURITY.md)

## 📄 License

GPL-3.0-or-later. See [LICENSE](LICENSE).
