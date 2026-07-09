<p align="center">
  <img src="icon-512.png" width="128" height="128" alt="CALC BOY Icon">
</p>

<h1 align="center">CALC BOY</h1>

<p align="center">
  🇬🇧 <a href="README.md">English version</a>
</p>

<p align="center">
  <strong>Taschenrechner-PWA im klassischen Nintendo-Stil</strong><br>
  Eine HTML-Datei, offlinefähig, nur lokal, kein Tracking.
</p>

> 📋 **Neueste Änderungen:** Siehe [CHANGELOG.de.md](CHANGELOG.de.md).

## ▶️ Direkt starten

**[➤ CALC BOY jetzt öffnen](https://schrotty74.github.io/CalcBoy/)**

## 📱 Als App aufs iPhone

1. Link oben in **Safari** öffnen.
2. **Teilen** antippen.
3. **Zum Home-Bildschirm** auswählen.
4. CALC BOY startet als Vollbild-PWA.

Die App unterstützt die iPhone-PWA-Safe-Area, damit die oberen Schaltflächen unterhalb der iOS-Statusleiste erreichbar bleiben.

## ✨ Funktionen

- 🎮 **7 Konsolen-Themes**: Game Boy, GB Color, NES, Super NES, Switch, Famicom plus freischaltbares Virtual Boy.
- 🧮 **Basisrechner**: Grundrechenarten, smarte Prozentlogik, Vorzeichenwechsel und Quadratwurzel.
- ➕ **Erweiterte wissenschaftliche Seite**: Speicherfunktionen, Trigonometrie, DEG/RAD, Logarithmen, Potenzen, Wurzeln, Fakultät, π und e.
- 🔄 **Einheitenumrechnung**: Strecke, Temperatur, Gewicht, Länge, Volumen, Geschwindigkeit, Zeit und deutsche MwSt. 19% / 7%.
- 💰 **Finanzseite**: Zinseszins, monatliche Sparrate, Zinsertrag, Trinkgeld, Rechnungssplitting und manuelle Währungsumrechnung.
- ℹ️ **Finanz-INFO**: zeigt Endwert, Einzahlungen und Zinsertrag.
- 💻 **Programmierer-Seite**: HEX, BIN, OCT, Bit-Operatoren, Shifts, ABS, INT, SGN und Zufallszahl.
- 🧮 **RPN-Modus** auf der Programmierer-Seite mit lokal gespeichertem Stack.
- 📈 **Plot-Seite** mit 20 Pixel-Funktionsgraphen.
- 📐 **Formel-Assistent** für Prozent, Dreisatz, Kreis, Pythagoras, Ohm, BMI, Durchschnitt, Geschwindigkeit und MwSt.-Hilfen.
- 📜 **Verlauf**: letzte 10 Rechnungen, Tippen zum Übernehmen, Summe und Durchschnitt.
- 📤 **Verlaufsexport** als Text und PNG.
- 🎵 Themespezifische 8-Bit-Tastentöne, Sound-Schalter und Cartridge-Animation beim Theme-Wechsel.
- 🕹️ **Math Attack** und **Snake** als Minispiele.
- 🔋 Batterie-LED, sofern der Browser die Battery Status API unterstützt.
- 🔒 Nur lokale Speicherung. Keine externen Requests, keine Analyse, kein Tracking.

## 🧭 Seiten

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

Mit **EXT** und danach **MEHR** wechselst du durch die Zusatzseiten. Mit **BASIC** kommst du zurück zum Standard-Tastenfeld.

## 🔐 Datenschutz

CALC BOY speichert Einstellungen und Verlauf nur lokal im Browser über `localStorage`. Nichts verlässt das Gerät. Die eingebettete Schrift vermeidet Font-CDN-Requests. Der Service Worker cached nur eigene App-Dateien derselben Domain.

Mehr Details: [SECURITY.de.md](SECURITY.de.md)

## 📖 Dokumentation

- [Anleitung](MANUAL.de.md)
- [Änderungsprotokoll](CHANGELOG.de.md)
- [Sicherheit & Datenschutz](SECURITY.de.md)

## 📄 Lizenz

GPL-3.0-or-later. Siehe [LICENSE](LICENSE).
