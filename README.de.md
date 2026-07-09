> 📋 **Neueste Änderungen:** Siehe [CHANGELOG.de.md](CHANGELOG.de.md).

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

- 7 Konsolen-Themes: Game Boy, GB Color, NES, Super NES, Switch, Famicom (THEME-Taste) – Auswahl wird gemerkt, inklusive freischaltbarem Virtual Boy
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

Ein Tipp öffnet einen KI-Chat, der die Anleitung bereits kennt (sie steckt direkt im Prompt – kein Webzugriff nötig):

- [**ChatGPT fragen**](https://chatgpt.com/?q=Du%20bist%20Experte%20fuer%20die%20Taschenrechner-App%20CALC%20BOY%20%28Nintendo-Stil-PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Beantworte%20Fragen%20dazu%20anhand%20dieser%20Kurzanleitung%3A%0AOBEN%3A%20THEME%20wechselt%207%20Konsolen-Looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%20plus%20freischaltbares%20Virtual%20Boy%3B%20wird%20gespeichert%29.%20GAME%20oeffnet%20Spielemenue.%20SND%20schaltet%208-Bit-Toene.%0ADISPLAY%3A%20Tippen%20%3D%20Verlauf%20%28letzte%2010%20Rechnungen%2C%20Eintrag%20tippen%20uebernimmt%20Ergebnis%2C%20zeigt%20Summe%2FMittelwert%2C%20TEILEN%20exportiert%29.%20Langes%20Druecken%20%3D%20Ergebnis%20kopieren.%20M%20oben%20links%20%3D%20Speicher%20belegt.%0ASEITEN%20%28EXT-Taste%2C%20dann%20MEHR%20zum%20Weiterschalten%2C%20BASIC%20zurueck%29%3A%20BASIC%20%3D%20Grundrechenarten%2C%20smarte%20%25-Taste%20%28100%2B10%25%3D110%29%2C%20Wurzel%2C%20%2B%2F-.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20mit%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20x2%2C%20x3%2C%20x%5Ey%2C%20Kubikwurzel%2C%201%2Fx%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%2C%20cm%2Fin%2C%20l%2Fgal%2C%20km%2Fh-mph%2C%20h%2Fmin%2C%20MwSt%2019%2F7%25%20%28MW%2B19%20Netto-%3EBrutto%2C%20MW-19%20Brutto-%3ENetto%29.%20FIN%20%3D%20Zinseszins%3A%20Zahl%20tippen%2C%20dann%20SET%20K0%2FP%25%2FJAHRE%2FRATE%20setzen%3B%20ENDWERT%20rechnet%20%28monatl.%20Verzinsung%29%2C%20ZINSEN%20nur%20Ertrag%2C%20INFO%20zeigt%20Endwert%2C%20Einzahlungen%20und%20Zinsertrag%3B%20Trinkgeld%20TIP%2B10%2F15%2F20%25%2C%20SET%20PERS%20%2B%20geteilt-durch-PERS%20splittet%3B%20Waehrung%20mit%20SET%20KURS%20und%20Euro%2FDollar-Tasten%20%28manueller%20Kurs%2C%20keine%20Live-Daten%29.%20PRG%20%3D%20HEX%2FBIN%2FOCT-Anzeige%2C%20AND%2FOR%2FXOR%2FMOD%2FShifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20Zufall.%20PLOT%20%3D%20zeichnet%2020%20Funktionen%20%28sin%20bis%20Gauss-Glocke%29%20als%20Pixelgraph.%0ASPIELE%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%20Kopfrechnen%2C%20Level%20Easy%2FNormal%2FHard%2C%20Highscore%20je%20Level%2C%20fehlerfrei%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%28Steuerung%202%2F4%2F6%2F8%20oder%20Pfeile%2C%20wird%20schneller%2C%20Highscore%29.%20AC%20beendet.%0AGEHEIM%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20schaltet%20VIRTUAL-BOY-Theme%20frei.%0ASONSTIGES%3A%20Alles%20wird%20nur%20lokal%20gespeichert%20%28Theme%2C%20Sound%2C%20Verlauf%2C%20Highscores%2C%20Speicher%2C%20Winkelmodus%2C%20FIN-Parameter%2C%20Kurs%29%2C%20keine%20externen%20Verbindungen%2C%20offline-faehig%2C%20GPL-3.0.%20Batterie-LED%20zeigt%20Ladestand%20nur%20auf%20Android%2FChrome.%20Volle%20Anleitung%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.de.md%0AFrage%20mich%20jetzt%2C%20was%20du%20wissen%20moechtest.)
- [**Claude fragen**](https://claude.ai/new?q=Du%20bist%20Experte%20fuer%20die%20Taschenrechner-App%20CALC%20BOY%20%28Nintendo-Stil-PWA%2C%20schrotty74.github.io%2FCalcBoy%29.%20Beantworte%20Fragen%20dazu%20anhand%20dieser%20Kurzanleitung%3A%0AOBEN%3A%20THEME%20wechselt%207%20Konsolen-Looks%20%28Game%20Boy%2C%20GB%20Color%2C%20NES%2C%20SNES%2C%20Switch%2C%20Famicom%20plus%20freischaltbares%20Virtual%20Boy%3B%20wird%20gespeichert%29.%20GAME%20oeffnet%20Spielemenue.%20SND%20schaltet%208-Bit-Toene.%0ADISPLAY%3A%20Tippen%20%3D%20Verlauf%20%28letzte%2010%20Rechnungen%2C%20Eintrag%20tippen%20uebernimmt%20Ergebnis%2C%20zeigt%20Summe%2FMittelwert%2C%20TEILEN%20exportiert%29.%20Langes%20Druecken%20%3D%20Ergebnis%20kopieren.%20M%20oben%20links%20%3D%20Speicher%20belegt.%0ASEITEN%20%28EXT-Taste%2C%20dann%20MEHR%20zum%20Weiterschalten%2C%20BASIC%20zurueck%29%3A%20BASIC%20%3D%20Grundrechenarten%2C%20smarte%20%25-Taste%20%28100%2B10%25%3D110%29%2C%20Wurzel%2C%20%2B%2F-.%20EXT%20%3D%20MC%2FMR%2FM%2B%2FM-%2C%20sin%2Fcos%2Ftan%20mit%20DEG%2FRAD%2C%20log%2C%20ln%2C%2010%5Ex%2C%20e%5Ex%2C%20x2%2C%20x3%2C%20x%5Ey%2C%20Kubikwurzel%2C%201%2Fx%2C%20n%21%2C%20Pi%2C%20e.%20CONV%20%3D%20km%2Fmi%2C%20C%2FF%2C%20kg%2Flb%2C%20cm%2Fin%2C%20l%2Fgal%2C%20km%2Fh-mph%2C%20h%2Fmin%2C%20MwSt%2019%2F7%25%20%28MW%2B19%20Netto-%3EBrutto%2C%20MW-19%20Brutto-%3ENetto%29.%20FIN%20%3D%20Zinseszins%3A%20Zahl%20tippen%2C%20dann%20SET%20K0%2FP%25%2FJAHRE%2FRATE%20setzen%3B%20ENDWERT%20rechnet%20%28monatl.%20Verzinsung%29%2C%20ZINSEN%20nur%20Ertrag%2C%20INFO%20zeigt%20Endwert%2C%20Einzahlungen%20und%20Zinsertrag%3B%20Trinkgeld%20TIP%2B10%2F15%2F20%25%2C%20SET%20PERS%20%2B%20geteilt-durch-PERS%20splittet%3B%20Waehrung%20mit%20SET%20KURS%20und%20Euro%2FDollar-Tasten%20%28manueller%20Kurs%2C%20keine%20Live-Daten%29.%20PRG%20%3D%20HEX%2FBIN%2FOCT-Anzeige%2C%20AND%2FOR%2FXOR%2FMOD%2FShifts%2C%20NOT%2C%20ABS%2C%20INT%2C%20SGN%2C%20Zufall.%20PLOT%20%3D%20zeichnet%2020%20Funktionen%20%28sin%20bis%20Gauss-Glocke%29%20als%20Pixelgraph.%0ASPIELE%20%28GAME%29%3A%201%2F2%2F3%20%3D%20MATH%20ATTACK%20%2830s%20Kopfrechnen%2C%20Level%20Easy%2FNormal%2FHard%2C%20Highscore%20je%20Level%2C%20fehlerfrei%20%3D%20PERFECT%29.%205%20%3D%20SNAKE%20%28Steuerung%202%2F4%2F6%2F8%20oder%20Pfeile%2C%20wird%20schneller%2C%20Highscore%29.%20AC%20beendet.%0AGEHEIM%3A%20Code%208%208%202%202%204%206%204%206%20-%20%2B%20schaltet%20VIRTUAL-BOY-Theme%20frei.%0ASONSTIGES%3A%20Alles%20wird%20nur%20lokal%20gespeichert%20%28Theme%2C%20Sound%2C%20Verlauf%2C%20Highscores%2C%20Speicher%2C%20Winkelmodus%2C%20FIN-Parameter%2C%20Kurs%29%2C%20keine%20externen%20Verbindungen%2C%20offline-faehig%2C%20GPL-3.0.%20Batterie-LED%20zeigt%20Ladestand%20nur%20auf%20Android%2FChrome.%20Volle%20Anleitung%3A%20schrotty74.github.io%2FCalcBoy%2FMANUAL.de.md%0AFrage%20mich%20jetzt%2C%20was%20du%20wissen%20moechtest.)
- **Gemini fragen**: [Gemini öffnen](https://gemini.google.com/app) und den Prompt unten einfügen (Gemini unterstützt keine vorausgefüllten Links):

<details><summary>Prompt zum Kopieren</summary>

```
Du bist Experte fuer die Taschenrechner-App CALC BOY (Nintendo-Stil-PWA, schrotty74.github.io/CalcBoy). Beantworte Fragen dazu anhand dieser Kurzanleitung:
OBEN: THEME wechselt 7 Konsolen-Looks (Game Boy, GB Color, NES, SNES, Switch, Famicom; wird gespeichert). GAME oeffnet Spielemenue. SND schaltet 8-Bit-Toene.
DISPLAY: Tippen = Verlauf (letzte 10 Rechnungen, Eintrag tippen uebernimmt Ergebnis, zeigt Summe/Mittelwert, TEILEN exportiert). Langes Druecken = Ergebnis kopieren. M oben links = Speicher belegt.
SEITEN (EXT-Taste, dann MEHR zum Weiterschalten, BASIC zurueck): BASIC = Grundrechenarten, smarte %-Taste (100+10%=110), Wurzel, +/-. EXT = MC/MR/M+/M-, sin/cos/tan mit DEG/RAD, log, ln, 10^x, e^x, x2, x3, x^y, Kubikwurzel, 1/x, n!, Pi, e. CONV = km/mi, C/F, kg/lb, cm/in, l/gal, km/h-mph, h/min, MwSt 19/7% (MW+19 Netto->Brutto, MW-19 Brutto->Netto). FIN = Zinseszins: Zahl tippen, dann SET K0/P%/JAHRE/RATE setzen; ENDWERT rechnet (monatl. Verzinsung), ZINSEN nur Ertrag, INFO zeigt Endwert, Einzahlungen und Zinsertrag; Trinkgeld TIP+10/15/20%, SET PERS + geteilt-durch-PERS splittet; Waehrung mit SET KURS und Euro/Dollar-Tasten (manueller Kurs, keine Live-Daten). PRG = HEX/BIN/OCT-Anzeige, AND/OR/XOR/MOD/Shifts, NOT, ABS, INT, SGN, Zufall. PLOT = zeichnet 20 Funktionen (sin bis Gauss-Glocke) als Pixelgraph.
SPIELE (GAME): 1/2/3 = MATH ATTACK (30s Kopfrechnen, Level Easy/Normal/Hard, Highscore je Level, fehlerfrei = PERFECT). 5 = SNAKE (Steuerung 2/4/6/8 oder Pfeile, wird schneller, Highscore). AC beendet.
GEHEIM: Code 8 8 2 2 4 6 4 6 - + schaltet VIRTUAL-BOY-Theme frei.
SONSTIGES: Alles wird nur lokal gespeichert (Theme, Sound, Verlauf, Highscores, Speicher, Winkelmodus, FIN-Parameter, Kurs), keine externen Verbindungen, offline-faehig, GPL-3.0. Batterie-LED zeigt Ladestand nur auf Android/Chrome. Volle Anleitung: schrotty74.github.io/CalcBoy/MANUAL.de.md
Frage mich jetzt, was du wissen moechtest.
```

</details>

## ⌨️ Tastatur (Mac/iPad)

Ziffern, `+ - * /`, `Enter` = Ergebnis, `Esc` = AC, `%`, `R` oder `W` = Wurzel

## 🔒 Datenschutz

Keine externen Requests, kein Tracking, keine Analytics. Einstellungen, Verlauf und Highscore werden ausschließlich lokal im Browser gespeichert. Details in der [SECURITY.de.md](SECURITY.de.md).

## 📄 Lizenz

[GPL-3.0](LICENSE) – Schrift „Press Start 2P" von CodeMan38 unter SIL Open Font License 1.1.
