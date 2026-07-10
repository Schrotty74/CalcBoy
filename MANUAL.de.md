# 📖 CALC BOY Anleitung

🇬🇧 [English manual](MANUAL.md)

CALC BOY ist eine Taschenrechner-PWA im Nintendo-Stil. Diese Anleitung beschreibt das aktuelle Verhalten der App.

## Erste Schritte

Öffne https://schrotty74.github.io/CalcBoy/ im Browser.

Auf dem iPhone: Seite in Safari öffnen und zum Home-Bildschirm hinzufügen. CALC BOY startet dann als Vollbild-PWA. Das Layout berücksichtigt die iOS-Safe-Area, damit `THEME`, `GAME` und `SND` unterhalb der Statusleiste erreichbar bleiben.

Nach dem ersten Laden funktioniert die App offline über den Service Worker.

Zahlen werden im deutschen Format angezeigt:
- Komma als Dezimaltrenner
- Punkt als Tausendertrenner

## Obere Tasten

- **THEME**: wechselt durch die Konsolen-Themes.
- **GAME**: öffnet das Spielemenü. Während eines Spiels beendet die Taste das Spiel.
- **SND**: schaltet die 8-Bit-Tastentöne ein oder aus.

Verfügbare Themes:
1. Game Boy
2. GB Color
3. NES
4. Super NES
5. Switch
6. Famicom
7. Virtual Boy, per Geheimcode freischaltbar

Das gewählte Theme wird lokal gespeichert.

## Display-Gesten

- **LCD antippen**: öffnet den Verlauf.
- **LCD lange drücken**: kopiert das aktuelle Ergebnis in die Zwischenablage.
- **M-Anzeige**: Im Speicher liegt ein Wert.

Der Verlauf enthält die letzten 10 Rechnungen. Ein Eintrag kann angetippt werden, um das Ergebnis wiederzuverwenden. Zusätzlich zeigt der Verlauf:
- **Σ**: Summe der Ergebnisse
- **Ø**: Durchschnitt der Ergebnisse

Verlauf exportieren:
- `TEILEN / EXPORT` exportiert den Verlauf als Text über Share-Sheet oder Zwischenablage.
- `PNG EXPORT` exportiert den Verlauf als PNG-Bild im CALC-BOY-Display-Stil.

## Seitennavigation

Die Seitenreihenfolge lautet:

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

- **EXT** öffnet die erweiterten Seiten.
- **MEHR** wechselt zur nächsten Zusatzseite.
- **BASIC** kehrt zum Standard-Tastenfeld zurück.

## BASIC-Seite

Standard-Rechnerseite.

Tasten:
- Ziffern `0–9`
- Komma
- `+`, `−`, `×`, `÷`
- **AC**: löscht Eingabe, Operatorstatus und Menüs
- **±**: wechselt das Vorzeichen
- **%**: smarte Prozentlogik
- **√**: Quadratwurzel
- **=**: rechnet aus
- **EXT**: öffnet die erweiterten Seiten

Beispiele für smarte Prozentlogik:
- `100 + 10 % = 110`
- `50 × 10 % = 5`
- `10 % = 0,1`

Ungültige Operationen zeigen `ERROR`. Eine Ziffer startet danach neu.

## EXT-Seite

Wissenschaftliche Funktionen und Speicher.

Speicher:
- **MC**: Speicher löschen
- **MR**: Speicher abrufen
- **M+**: aktuellen Wert zum Speicher addieren
- **M−**: aktuellen Wert vom Speicher abziehen

Wissenschaftliche Funktionen:
- `sin`, `cos`, `tan`
- `DEG` / `RAD`
- `log`, `ln`
- `10^x`, `e^x`
- `x²`, `x³`, `xʸ`
- Kubikwurzel
- `1/x`
- `n!`
- `π`, `e`

## CONV-Seite

Einheitenumrechnung.

Umrechnungen:
- km ↔ mi
- m ↔ ft
- °C ↔ °F
- kg ↔ lb
- cm ↔ in
- Liter ↔ Gallone (US)
- km/h ↔ mph
- Stunden ↔ Minuten
- MwSt. 19% Netto ↔ Brutto
- MwSt. 7% Netto ↔ Brutto

## FIN-Seite

Finanzseite.

Gespeicherte Parameter:
- **SET K0**: Startkapital
- **SET P%**: jährlicher Zinssatz
- **SET JAHRE**: Laufzeit in Jahren
- **SET RATE/M**: monatliche Sparrate
- **SET PERS**: Personenanzahl
- **SET KURS**: manueller Wechselkurs

Ergebnisse:
- **ENDWERT**: Endwert mit monatlicher Verzinsung
- **ZINSEN**: nur der Zinsertrag
- **INFO**: kompakte Übersicht mit Endwert, Einzahlungen und Zinsertrag
- **RESET**: setzt Finanzparameter zurück

Weitere Helfer:
- **TIP+10%**, **TIP+15%**, **TIP+20%**
- **÷ PERS**: aktuellen Betrag durch gespeicherte Personenanzahl teilen
- **€→$**, **$→€**: Umrechnung mit manuellem Kurs

Es wird keine Live-Kurs-API verwendet.

## PRG-Seite

Programmierer-Seite.

Funktionen:
- `→HEX`
- `→BIN`
- `→OCT`
- `NOT`
- `AND`
- `OR`
- `XOR`
- `MOD`
- Bit-Shifts `«` und `»`
- `ABS`
- `INT`
- `SGN`
- `ZUFALL`
- Konstanten `π` und `e`
- **RPN**-Modus-Schalter

## RPN-Modus

Der RPN-Modus ist auf der PRG-Seite verfügbar.

- **RPN** schaltet den RPN-Modus ein oder aus.
- Zahl eingeben und **=** drücken, um sie auf den Stack zu legen.
- Nächste Zahl eingeben und einen Operator drücken, um mit dem vorherigen Stack-Wert zu rechnen.
- Unterstützt werden Rechenoperatoren und Programmierer-Operatoren.
- **AC** löscht im aktiven RPN-Modus die aktuelle Eingabe und den RPN-Stack.
- Modus und Stack werden lokal gespeichert.

Beispiel:
1. `2` eingeben
2. `=` drücken
3. `3` eingeben
4. `+` drücken
5. Ergebnis: `5`

## PLOT-Seite

Die Plot-Seite zeichnet Funktionen als Pixelgraph im LCD-Stil.

Verfügbare Funktionen:
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
- Gauß-Kurve
- floor
- sinc x
- x·sin x

Eine beliebige Taste beendet den Plot.

## FORM-Seite

Formel-Assistent.

Variablen:
- **SET A**: aktuellen Wert als A speichern
- **SET B**: aktuellen Wert als B speichern
- **SET C**: aktuellen Wert als C speichern
- **INFO**: aktuelle Formelvariablen anzeigen
- **CLR ABC**: alle Formelvariablen löschen

Formeln:
- **% VON**: A Prozent von B
- **DREISATZ**: Dreisatz, `B × C / A`
- **KREIS A**: Kreisfläche mit Radius A
- **KREIS U**: Kreisumfang mit Radius A
- **PYTH**: Hypotenuse aus A und B
- **OHM**: Spannung aus Widerstand A und Strom B
- **BMI**: BMI aus Gewicht A und Größe B
- **Ø ABC**: Durchschnitt aus A, B und C
- **KM/H**: Geschwindigkeit aus Strecke A und Zeit B
- **NET19**: Netto aus Brutto A bei 19% MwSt.
- **BRU19**: Brutto aus Netto A bei 19% MwSt.

Formelvariablen werden lokal gespeichert.

## Spiele

**GAME** öffnet das Spielemenü.

### Math Attack

Kopfrechenspiel:
- 30-Sekunden-Runden
- Easy, Normal und Hard
- Highscore pro Schwierigkeitsgrad
- PERFECT-Jingle bei fehlerfreier Runde

### Snake

Snake-Spiel:
- Steuerung mit `2`, `4`, `6`, `8` oder Pfeiltasten
- Geschwindigkeit steigt mit der Zeit
- Highscore wird gespeichert
- **AC** beendet das Spiel

## Geheim-Theme freischalten

Gib ein:

`8 8 2 2 4 6 4 6 − +`

Dadurch wird das Virtual-Boy-Theme freigeschaltet, dauerhaft lokal gespeichert und kann anschließend über die **THEME**-Taste ausgewählt werden.

## Lokale Speicherung

CALC BOY speichert nur lokale Daten in `localStorage`:
- Theme
- Sound-Einstellung
- Verlauf
- freigeschaltete Themes
- Highscores
- Speicherwert
- Winkelmodus
- Finanzparameter
- Wechselkurs
- Personenanzahl
- RPN-Modus
- RPN-Stack
- Formelvariablen

Nichts wird übertragen.

## Offline-Verhalten

Der Service Worker cached nur eigene App-Dateien derselben Domain:
- `./`
- `./index.html`
- `./apple-touch-icon.png`
- `./icon-512.png`

Die App verwendet Cache-first mit Aktualisierung im Hintergrund.
