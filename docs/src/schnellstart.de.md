# CALC BOY - Schnellstart

Version: 3.1.0

CALC BOY ist ein lokal laufender PWA-Taschenrechner im Stil klassischer Handheld-Konsolen. Diese Dokumentation beschreibt den aktuellen Quellcode der Version 3.1.0.

## Installation

1. Live-Link in Safari oder Chrome öffnen.
2. Über Teilen bzw. Browsermenü Zum Home-Bildschirm hinzufügen wählen.
3. CALC BOY vom Home-Bildschirm starten. Im installierten Modus läuft die App im Vollbild.

## Offline-Betrieb

Der Service Worker speichert App-Shell, index.html und Icons im Cache calcboy-v3.1.0. Die Registrierung erfolgt nur auf HTTPS. Nach dem ersten Online-Start kann die App aus dem Cache starten.

![BASIC](../assets/screenshots/basic.png)

## Bedienueberblick

Mit EXT verlaesst du BASIC, mit MEHR wechselst du durch die Zusatzseiten, mit BASIC kehrst du zurueck.

### BASIC

![BASIC](../assets/screenshots/basic.png)

Standardrechner fuer Grundrechenarten, Vorzeichen, Quadratwurzel und smarte Prozentrechnung.

**So verwendest du es**

- Erste Zahl eingeben, Rechenzeichen waehlen, zweite Zahl eingeben und = druecken.
- AC loescht Eingabe und laufende Rechnung. Nach ERROR beginnt die naechste Ziffer eine neue Eingabe.
- LCD antippen oeffnet den Verlauf; langes Druecken kopiert das angezeigte Ergebnis.

**Wichtige Details**

- Die Prozent-Taste ist kontextabhaengig: Bei + oder - berechnet sie einen Prozentanteil des ersten Operanden.

**Beispiele**

- **Smarte Prozentrechnung:** 100 + 10 % = 110; 100 - 10 % = 90
- **Quadratwurzel:** 144 sqrt -> 12

### EXT

![EXT](../assets/screenshots/ext.png)

Wissenschafts- und Speicherseite mit Trigonometrie, Logarithmen, Potenzen, Wurzeln, Fakultaet, pi und e.

**So verwendest du es**

- Bei direkten Funktionen wie sin, log, x^2 oder 1/x zuerst den Wert eingeben, dann die Funktion druecken.
- Fuer x^y zuerst die Basis eingeben, x^y druecken, den Exponenten eingeben und = druecken.
- Vor Trigonometrie DEG/RAD passend setzen. DEG wird gespeichert und ist die Voreinstellung, solange du sie nicht aenderst.

**Wichtige Details**

- n! funktioniert nur fuer ganze Zahlen von 0 bis 170.

**Beispiele**

- **DEG/RAD:** DEG: 30 sin -> 0,5; RAD: pi sin -> etwa 0
- **Speicher:** 42 M+, AC, MR -> 42; 10 M- laesst 32 im Speicher
- **Potenzen:** 2 x^y 8 = -> 256

### CONV

![CONV](../assets/screenshots/conv.png)

Direktumrechner fuer Strecke, Temperatur, Gewicht, Volumen, Geschwindigkeit, Zeit und deutsche Mehrwertsteuer.

**So verwendest du es**

- Ausgangswert eingeben und die passende Umrechnungstaste druecken.
- Zum Zurueckrechnen die jeweilige Gegenrichtung verwenden.
- MW+ behandelt den Wert als netto, MW- behandelt ihn als brutto.

**Wichtige Details**

- Bei Liter/Gallone wird die US-Gallone verwendet.

**Beispiele**

- **Mehrwertsteuer:** 100 MW+19 -> 119; 119 MW-19 -> 100
- **Temperatur:** 20 C->F -> 68; 68 F->C -> 20
- **Geschwindigkeit:** 100 km/h->mph -> 62,137119224

### FIN

![FIN](../assets/screenshots/fin.png)

Finanzhilfen fuer Zinseszins mit Monatsrate, Zinsertrag, Trinkgeld, Rechnung teilen und manuelle Waehrungsumrechnung.

**So verwendest du es**

- K0, P%, Jahre und Monatsrate mit SET-Tasten speichern. ENDWERT berechnet den spaeteren Wert.
- ZINSEN zeigt nur den Ertrag: Endwert minus Startkapital und Einzahlungen.
- Vor / PERS die Personenzahl setzen. Vor EUR->$ oder $->EUR den Kurs setzen.

**Wichtige Details**

- Standardwerte sind K0 1000, P 3, Jahre 10, Monatsrate 50, Personen 2 und Kurs 1,08.

**Beispiele**

- **Zinseszins:** SET K0=1000, SET P%=3, SET JAHRE=10, SET RATE/M=50, ENDWERT -> 8336,42449101
- **Nur Zinsen:** Mit denselben Werten: ZINSEN -> 1336,42449101
- **Rechnung teilen:** SET PERS=4, 80 eingeben, / PERS -> 20
- **Waehrung:** SET KURS=1,08, 100 EUR->$ -> 108; 108 $->EUR -> 100

### PRG

![PRG](../assets/screenshots/prg.png)

Programmierfunktionen, Ganzzahl-Anzeige in anderen Zahlensystemen, Bitoperatoren, Zufallszahl und RPN-Modus.

**So verwendest du es**

- HEX, BIN und OCT zeigen den ganzzahligen Anteil des Displays in der Statuszeile.
- AND, OR, XOR, MOD, << und >> sind Zweier-Operatoren: erster Wert, Operator, zweiter Wert, =.
- RPN macht = zur Stapel-Taste: Wert eingeben, = druecken, zweiten Wert eingeben, dann Operator druecken.

**Wichtige Details**

- Bitfunktionen verwenden JavaScript-Ganzzahlen; Nachkommastellen werden abgeschnitten.

**Beispiele**

- **Zahlensysteme:** 255 ->HEX zeigt FF; ->BIN zeigt 11111111
- **Bitoperationen:** 5 AND 3 = 1; 5 OR 2 = 7; 9 MOD 4 = 1
- **RPN:** RPN an: 12 =, 3 + -> 15; AC leert den Stack

### PLOT

![PLOT](../assets/screenshots/plot.png)

Zeichnet 20 eingebaute Funktionsgraphen als Pixelgrafik im LCD.

**So verwendest du es**

- PLOT oeffnen und eine Funktion wie sin x, x^2 oder GAUSS druecken.
- Der Graph ersetzt kurz das LCD und skaliert sich automatisch.
- Eine andere Taste druecken oder das Display antippen, um den Graphen zu schliessen.

**Wichtige Details**

- Asymptoten wie tan x oder 1/x werden begrenzt, damit der Plot lesbar bleibt.

**Beispiele**

- **Graph:** sin x zeichnet y = sin x; jede Nicht-Plot-Taste schliesst ihn
- **Vergleich:** x^2 und x^3 nutzen jeweils automatische Skalierung

### FORM

![FORM](../assets/screenshots/form.png)

Formel-Assistent mit drei gespeicherten Variablen A, B und C.

**So verwendest du es**

- Zahl eingeben und mit SET A, SET B oder SET C speichern.
- INFO zeigt die gespeicherten Werte. CLR ABC setzt alle Variablen auf 0.
- Formeltaste druecken; das Ergebnis erscheint im Display und wird in den Verlauf geschrieben.

**Wichtige Details**

- Die Formeln nutzen feste Rollen: BMI verwendet A als kg und B als Meter; KM/H verwendet A als Kilometer und B als Stunden.

**Beispiele**

- **Prozent:** SET A=20, SET B=150, % VON -> 30
- **Pythagoras:** SET A=3, SET B=4, PYTH -> 5
- **BMI:** SET A=80, SET B=1,8, BMI -> 24,6913580247
- **Netto/Brutto:** SET A=119, NET19 -> 100; SET A=100, BRU19 -> 119

## Spiele

GAME oeffnet das Menue. 1, 2 oder 3 startet Math Attack, 5 startet Snake.

## Tastatur

- `0-9` - Zifferneingabe
- `, oder .` - Dezimalkomma
- `+ - * /` - Grundrechenarten
- `Enter oder =` - Berechnen
- `Escape` - AC / loeschen
- `%` - Prozent
- `r oder w` - Quadratwurzel
- `Pfeiltasten` - Snake-Steuerung und Geheimcode-Eingabe

## Speicher und Datenschutz

Alle Daten bleiben im Browser-localStorage. Es gibt keine Analytics, keine externen Schriftaufrufe und keine Live-Wechselkurs-API.

Theme, Sound, Winkelmodus, Verlauf, Speicherwert, Finanzparameter, Wechselkurs, Personenzahl, RPN-Modus, RPN-Stack, Formelvariablen, Highscores, Virtual-Boy-Freischaltung

## Grenzen

Der Service Worker wird nur auf HTTPS registriert. Das Inline-Manifest enthaelt Icons nur bei HTTP oder HTTPS. Die Waehrungsumrechnung nutzt einen manuell gespeicherten Kurs und keine Live-API. Zahlensystem-Umrechnungen der PRG-Seite erscheinen in der Statuszeile und ersetzen nicht das Hauptdisplay. Teilen, Zwischenablage, Vibration und Batterieanzeige haengen vom Browser ab. Die App-Oberflaeche selbst ist deutsch.

## Versionsinformation

CALC BOY 3.1.0 / calcboy-v3.1.0
