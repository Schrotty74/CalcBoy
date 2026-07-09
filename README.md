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

- 🎮 **7 console themes**: Game Boy, GB Color, NES, Super NES, Switch, Famicom, plus unlockable Virtual Boy.
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

## 📖 Documentation

- [Manual](MANUAL.md)
- [Changelog](CHANGELOG.md)
- [Security & Privacy](SECURITY.md)

## 📄 License

GPL-3.0-or-later. See [LICENSE](LICENSE).
