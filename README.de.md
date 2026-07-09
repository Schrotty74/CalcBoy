<p align="center">
  <img src="icon-512.png" width="128" height="128" alt="CALC BOY Icon">
</p>

<h1 align="center">CALC BOY</h1>

<p align="center">
  🇬🇧 <a href="README.md">English version</a>
</p>

Ein Taschenrechner im klassischen Nintendo-Look – als Progressive Web App in einer einzigen HTML-Datei (plus kleinem Service Worker). Keine Installation, kein App Store, keine externen Verbindungen, kein Tracking.

## ▶️ Direkt starten

**[➤ CALC BOY jetzt öffnen](https://schrotty74.github.io/CalcBoy/)**

## 📱 Als App aufs iPhone

1. Link oben in **Safari** öffnen
2. **Teilen-Symbol** → **„Zum Home-Bildschirm"**
3. CALC BOY startet ab dann als Vollbild-App

## ✨ Features (v3.0)

- 6 Konsolen-Themes: Game Boy, GB Color, NES, Super NES, Switch, Famicom (THEME-Taste) – Auswahl wird gemerkt
- 🕹️ **MATH ATTACK**: Kopfrechnen gegen die Uhr (GAME-Menü) mit 3 Schwierigkeitsstufen, Highscore pro Level und PERFECT-Jingle für fehlerfreie Runden
- 🔄 **Einheiten-Umrechner** (CONV-Seite): km↔mi, °C↔°F, kg↔lb, cm↔in, l↔gal, km/h↔mph, h↔min, MwSt (19 %/7 % Netto↔Brutto)
- 📋 **Kopieren & Teilen**: langes Drücken aufs Display kopiert das Ergebnis; Verlauf per Share-Sheet exportieren
- 🎵 Jedes Konsolen-Theme hat einen eigenen Tastenklang; der Theme-Wechsel spielt eine Cartridge-Wechsel-Animation
- 🔋 Batterie-LED zeigt den echten Ladestand, wo der Browser es unterstützt (Chrome/Android; iOS behält die klassische rote LED)
- ➕ **Erweiterter Modus** (EXT-Taste): Speicher (MC/MR/M+/M−), sin/cos/tan mit DEG/RAD-Umschalter, log, ln, 10^x, e^x, x², x³, xʸ, ∛, 1/x, Fakultät, π, e
- 💰 **Finanz-Seite** (FIN): Zinseszins-Rechner mit monatlicher Sparrate, Trinkgeld & Rechnung splitten, Währungsumrechnung mit manuell gesetztem Kurs (bewusst ohne Live-Kurs-API – nichts verlässt das Gerät)
- 💻 **Programmierer-Seite** (PRG): HEX/BIN/OCT-Anzeige, AND, OR, XOR, NOT, MOD, Bit-Shifts, ABS, INT, SGN, Zufallszahl
- 📈 **Plot-Seite**: zeichnet sin, cos, tan, x², x³, √x, log x und 1/x als Pixel-Graphen ins LCD
- 🐍 **SNAKE**: zweites Spiel über das GAME-Menü, gesteuert mit 2/4/6/8 (oder Pfeiltasten), eigener Highscore
- Smarte Prozent-Taste: `100 + 10 %` ergibt 110, wie beim echten Rechner
- Verlauf zeigt Summe (Σ) und Mittelwert (Ø) der letzten Ergebnisse
- 🔬 **Wissenschaftlicher Modus**: iPhone quer drehen für eine Schnellzugriff-Funktionsspalte
- 📜 **Rechenverlauf**: aufs Display tippen zeigt die letzten 10 Rechnungen, Antippen übernimmt das Ergebnis
- Grundrechenarten, Prozent, Vorzeichen, Quadratwurzel
- Boot-Animation und 8-Bit-Sounds, abschaltbar (SND-Taste)
- Deutsches Zahlenformat (Komma, Tausenderpunkte)
- Offline-fähig per Service Worker; alle Daten bleiben lokal auf dem Gerät
- 🥚 Es heißt, ein alter Code schaltet eine siebte Konsole frei …

## 📖 Anleitung

Die vollständige Anleitung steht in [MANUAL.de.md](MANUAL.de.md) (🇬🇧 [English](MANUAL.md)).

## 🤖 Frag eine KI zum CALC BOY

Ein Tipp öffnet einen KI-Chat, der zuerst die Anleitung liest und dann deine Fragen beantwortet:

- [**ChatGPT fragen**](https://chatgpt.com/?q=Bitte%20lies%20die%20CALC-BOY-Anleitung%20unter%20https%3A%2F%2Fschrotty74.github.io%2FCalcBoy%2FMANUAL.de.md%20%28Fallback%2C%20falls%20das%20fehlschlaegt%3A%20https%3A%2F%2Fraw.githubusercontent.com%2FSchrotty74%2FCalcBoy%2Fmain%2FMANUAL.de.md%29%20und%20beantworte%20anschliessend%20meine%20Fragen%20zu%20diesem%20Taschenrechner%20und%20seinen%20Funktionen.)
- [**Claude fragen**](https://claude.ai/new?q=Bitte%20lies%20die%20CALC-BOY-Anleitung%20unter%20https%3A%2F%2Fschrotty74.github.io%2FCalcBoy%2FMANUAL.de.md%20%28Fallback%2C%20falls%20das%20fehlschlaegt%3A%20https%3A%2F%2Fraw.githubusercontent.com%2FSchrotty74%2FCalcBoy%2Fmain%2FMANUAL.de.md%29%20und%20beantworte%20anschliessend%20meine%20Fragen%20zu%20diesem%20Taschenrechner%20und%20seinen%20Funktionen.)
- **Gemini fragen**: [Gemini öffnen](https://gemini.google.com/app) und diesen Prompt einfügen (Gemini unterstützt keine vorausgefüllten Links):

```
Bitte lies die CALC-BOY-Anleitung unter https://schrotty74.github.io/CalcBoy/MANUAL.de.md (Fallback, falls das fehlschlaegt: https://raw.githubusercontent.com/Schrotty74/CalcBoy/main/MANUAL.de.md) und beantworte anschliessend meine Fragen zu diesem Taschenrechner und seinen Funktionen.
```

## ⌨️ Tastatur (Mac/iPad)

Ziffern, `+ - * /`, `Enter` = Ergebnis, `Esc` = AC, `%`, `R` oder `W` = Wurzel

## 🔒 Datenschutz

Keine externen Requests, kein Tracking, keine Analytics. Einstellungen, Verlauf und Highscore werden ausschließlich lokal im Browser gespeichert. Details in der [SECURITY.de.md](SECURITY.de.md).

## 📄 Lizenz

[GPL-3.0](LICENSE) – Schrift „Press Start 2P" von CodeMan38 unter SIL Open Font License 1.1.
