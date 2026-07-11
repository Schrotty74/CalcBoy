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

One tap opens an AI chat that reads the manual first and then answers your questions:

- [**Ask ChatGPT**](https://chatgpt.com/?q=Please%20read%20the%20CALC%20BOY%20manual%20at%20https%3A%2F%2Fraw.githubusercontent.com%2FSchrotty74%2FCalcBoy%2Fmain%2FMANUAL.md%20and%20then%20answer%20my%20questions%20about%20this%20calculator%20app%20and%20its%20functions.)
- [**Ask Claude**](https://claude.ai/new?q=Please%20read%20the%20CALC%20BOY%20manual%20at%20https%3A%2F%2Fraw.githubusercontent.com%2FSchrotty74%2FCalcBoy%2Fmain%2FMANUAL.md%20and%20then%20answer%20my%20questions%20about%20this%20calculator%20app%20and%20its%20functions.)

## 📖 Documentation

- **PDF guides**
  - [Quick Start Guide (PDF)](docs/output/pdf/CALC-BOY-quick-start-guide-en.pdf)
  - [Complete User Manual (PDF)](docs/output/pdf/CALC-BOY-user-manual-en.pdf)
  - [German Quick Start (PDF)](docs/output/pdf/CALC-BOY-schnellstart-de.pdf)
  - [German User Manual (PDF)](docs/output/pdf/CALC-BOY-benutzerhandbuch-de.pdf)
- **Editable sources**
  - [English Quick Start](docs/src/quick-start-guide.en.md)
  - [English User Manual](docs/src/user-manual.en.md)
  - [German Quick Start](docs/src/schnellstart.de.md)
  - [German User Manual](docs/src/benutzerhandbuch.de.md)
- [Manual](MANUAL.md)
- [Changelog](CHANGELOG.md)
- [Security & Privacy](SECURITY.md)

## 📄 License

GPL-3.0-or-later. See [LICENSE](LICENSE).
