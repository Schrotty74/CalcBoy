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

- 🎮 **6 Konsolen-Themes + 1 freischaltbares Virtual-Boy-Theme**: Game Boy, GB Color, NES, Super NES, Switch und Famicom sind sofort verfügbar. Das Virtual-Boy-Theme kann über den Geheimcode freigeschaltet werden.
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

## 🤖 Frag eine KI zum CALC BOY

Ein Tipp öffnet einen KI-Chat, der die Anleitung bereits kennt (sie steckt direkt im Prompt – kein Webzugriff nötig):

- [**ChatGPT fragen**](https://chatgpt.com/?q=Du%20bist%20Experte%20fuer%20die%20Taschenrechner-App%20CALC%20BOY%20%28Nintendo-Stil-PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Beantworte%20Fragen%20dazu%20anhand%20dieser%20Kurzanleitung%3A%0AOBEN%3A%20THEME%20wechselt%207%20Konsolen-Looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%20%2B%20freischaltbares%20Virtual%20Boy%29.%20GAME%20oeffnet%20Spielemenue.%20SND%20schaltet%208-Bit-Toene.%0ADISPLAY%3A%20Tippen%20%3D%20Verlauf%20%28letzte%2010%20Rechnungen%2C%20Eintrag%20tippen%20uebernimmt%20Ergebnis%2C%20zeigt%20Summe%2FMittelwert%2C%20Export%20als%20Text%20oder%20PNG%29.%20Langes%20Druecken%20%3D%20Ergebnis%20kopieren.%20M%20oben%20links%20%3D%20Speicher%20belegt.%0ASEITEN%20%28EXT-Taste%2C%20dann%20MEHR%3A%20BASIC%20-%3E%20EXT%20-%3E%20CONV%20-%3E%20FIN%20-%3E%20PRG%20-%3E%20PLOT%20-%3E%20FORM%29%3A%20BASIC%20%3D%20Grundrechenarten%2C%20smarte%20%25-Taste%20%28100%2B10%25%3D110%29%2C%20Wurzel.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20mit%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20Potenzen%2C%20Wurzeln%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20Einheiten%20%28km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%20usw.%29%20und%20MwSt%2019%2F7%25.%20FIN%20%3D%20Zinseszins%20%28SET%20K0%2FP%25%2FJAHRE%2FRATE%2C%20ENDWERT%2C%20ZINSEN%3B%20INFO%20zeigt%20Endwert%2C%20Einzahlungen%2C%20Zinsertrag%29%2C%20Trinkgeld%2C%20Rechnung%20splitten%2C%20Waehrung%20mit%20manuellem%20Kurs.%20PRG%20%3D%20HEX%2FBIN%2FOCT%2C%20AND%2FOR%2FXOR%2FMOD%2FShifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20Zufall%2C%20plus%20RPN-Modus%20mit%20Stack.%20PLOT%20%3D%2020%20Funktionen%20als%20Pixelgraph.%20FORM%20%3D%20Formel-Assistent%20mit%20Variablen%20A%2FB%2FC%3A%20Prozent-von%2C%20Dreisatz%2C%20Kreis%2C%20Pythagoras%2C%20Ohm%2C%20BMI%2C%20Durchschnitt%2C%20Geschwindigkeit%2C%20MwSt.%0ASPIELE%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%2C%20Level%20Easy%2FNormal%2FHard%2C%20Highscore%20je%20Level%2C%20fehlerfrei%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%282%2F4%2F6%2F8%20oder%20Pfeile%29.%20AC%20beendet.%0AGEHEIM%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20schaltet%20das%20VIRTUAL-BOY-Theme%20frei.%0ASONSTIGES%3A%20Alles%20nur%20lokal%20gespeichert%2C%20keine%20externen%20Verbindungen%2C%20offline-faehig%2C%20GPL-3.0.%20Volle%20Anleitung%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.de.md%0AFrage%20mich%20jetzt%2C%20was%20du%20wissen%20moechtest.)
- [**Claude fragen**](https://claude.ai/new?q=Du%20bist%20Experte%20fuer%20die%20Taschenrechner-App%20CALC%20BOY%20%28Nintendo-Stil-PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Beantworte%20Fragen%20dazu%20anhand%20dieser%20Kurzanleitung%3A%0AOBEN%3A%20THEME%20wechselt%207%20Konsolen-Looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%20%2B%20freischaltbares%20Virtual%20Boy%29.%20GAME%20oeffnet%20Spielemenue.%20SND%20schaltet%208-Bit-Toene.%0ADISPLAY%3A%20Tippen%20%3D%20Verlauf%20%28letzte%2010%20Rechnungen%2C%20Eintrag%20tippen%20uebernimmt%20Ergebnis%2C%20zeigt%20Summe%2FMittelwert%2C%20Export%20als%20Text%20oder%20PNG%29.%20Langes%20Druecken%20%3D%20Ergebnis%20kopieren.%20M%20oben%20links%20%3D%20Speicher%20belegt.%0ASEITEN%20%28EXT-Taste%2C%20dann%20MEHR%3A%20BASIC%20-%3E%20EXT%20-%3E%20CONV%20-%3E%20FIN%20-%3E%20PRG%20-%3E%20PLOT%20-%3E%20FORM%29%3A%20BASIC%20%3D%20Grundrechenarten%2C%20smarte%20%25-Taste%20%28100%2B10%25%3D110%29%2C%20Wurzel.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20mit%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20Potenzen%2C%20Wurzeln%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20Einheiten%20%28km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%20usw.%29%20und%20MwSt%2019%2F7%25.%20FIN%20%3D%20Zinseszins%20%28SET%20K0%2FP%25%2FJAHRE%2FRATE%2C%20ENDWERT%2C%20ZINSEN%3B%20INFO%20zeigt%20Endwert%2C%20Einzahlungen%2C%20Zinsertrag%29%2C%20Trinkgeld%2C%20Rechnung%20splitten%2C%20Waehrung%20mit%20manuellem%20Kurs.%20PRG%20%3D%20HEX%2FBIN%2FOCT%2C%20AND%2FOR%2FXOR%2FMOD%2FShifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20Zufall%2C%20plus%20RPN-Modus%20mit%20Stack.%20PLOT%20%3D%2020%20Funktionen%20als%20Pixelgraph.%20FORM%20%3D%20Formel-Assistent%20mit%20Variablen%20A%2FB%2FC%3A%20Prozent-von%2C%20Dreisatz%2C%20Kreis%2C%20Pythagoras%2C%20Ohm%2C%20BMI%2C%20Durchschnitt%2C%20Geschwindigkeit%2C%20MwSt.%0ASPIELE%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%2C%20Level%20Easy%2FNormal%2FHard%2C%20Highscore%20je%20Level%2C%20fehlerfrei%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%282%2F4%2F6%2F8%20oder%20Pfeile%29.%20AC%20beendet.%0AGEHEIM%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20schaltet%20das%20VIRTUAL-BOY-Theme%20frei.%0ASONSTIGES%3A%20Alles%20nur%20lokal%20gespeichert%2C%20keine%20externen%20Verbindungen%2C%20offline-faehig%2C%20GPL-3.0.%20Volle%20Anleitung%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.de.md%0AFrage%20mich%20jetzt%2C%20was%20du%20wissen%20moechtest.)
- **Gemini fragen**: [Gemini öffnen](https://gemini.google.com/app) und den Prompt unten einfügen (Gemini unterstützt keine vorausgefüllten Links):

<details><summary>Prompt zum Kopieren</summary>

```
Du bist Experte fuer die Taschenrechner-App CALC BOY (Nintendo-Stil-PWA, schrotty74.github.io/CalcBoy). Beantworte Fragen dazu anhand dieser Kurzanleitung:
OBEN: THEME wechselt 7 Konsolen-Looks (Game Boy, GB Color, NES, SNES, Switch, Famicom + freischaltbares Virtual Boy). GAME oeffnet Spielemenue. SND schaltet 8-Bit-Toene.
DISPLAY: Tippen = Verlauf (letzte 10 Rechnungen, Eintrag tippen uebernimmt Ergebnis, zeigt Summe/Mittelwert, Export als Text oder PNG). Langes Druecken = Ergebnis kopieren. M oben links = Speicher belegt.
SEITEN (EXT-Taste, dann MEHR: BASIC -> EXT -> CONV -> FIN -> PRG -> PLOT -> FORM): BASIC = Grundrechenarten, smarte %-Taste (100+10%=110), Wurzel. EXT = MC/MR/M+/M-, sin/cos/tan mit DEG/RAD, log, ln, 10^x, e^x, Potenzen, Wurzeln, n!, Pi, e. CONV = Einheiten (km/mi, C/F, kg/lb usw.) und MwSt 19/7%. FIN = Zinseszins (SET K0/P%/JAHRE/RATE, ENDWERT, ZINSEN; INFO zeigt Endwert, Einzahlungen, Zinsertrag), Trinkgeld, Rechnung splitten, Waehrung mit manuellem Kurs. PRG = HEX/BIN/OCT, AND/OR/XOR/MOD/Shifts, NOT, ABS, INT, SGN, Zufall, plus RPN-Modus mit Stack. PLOT = 20 Funktionen als Pixelgraph. FORM = Formel-Assistent mit Variablen A/B/C: Prozent-von, Dreisatz, Kreis, Pythagoras, Ohm, BMI, Durchschnitt, Geschwindigkeit, MwSt.
SPIELE (GAME): 1/2/3 = MATH ATTACK (30s, Level Easy/Normal/Hard, Highscore je Level, fehlerfrei = PERFECT). 5 = SNAKE (2/4/6/8 oder Pfeile). AC beendet.
GEHEIM: Code 8 8 2 2 4 6 4 6 - + schaltet das VIRTUAL-BOY-Theme frei.
SONSTIGES: Alles nur lokal gespeichert, keine externen Verbindungen, offline-faehig, GPL-3.0. Volle Anleitung: schrotty74.github.io/CalcBoy/MANUAL.de.md
Frage mich jetzt, was du wissen moechtest.
```

</details>

## 📖 Dokumentation

- [Anleitung](MANUAL.de.md)
- [Änderungsprotokoll](CHANGELOG.de.md)
- [Sicherheit & Datenschutz](SECURITY.de.md)

## 📄 Lizenz

GPL-3.0-or-later. Siehe [LICENSE](LICENSE).
