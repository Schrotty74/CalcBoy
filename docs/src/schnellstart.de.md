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

## Interface overview

Mit EXT verlassen Sie BASIC, mit MEHR wechseln Sie durch die Zusatzseiten, mit BASIC kehren Sie zurück.

### BASIC

AC, +/-, %, sqrt, 7, 8, 9, /, 4, 5, 6, *, 1, 2, 3, -, 0, ,, +, EXT, =

### EXT

MC, MR, M+, M-, sin, cos, tan, DEG/RAD, log, ln, 10^x, e^x, x^2, x^3, x^y, cbrt, 1/x, n!, pi, e, BASIC, MEHR, =

### CONV

km->mi, mi->km, m->ft, ft->m, C->F, F->C, kg->lb, lb->kg, cm->in, in->cm, l->gal, gal->l, km/h->mph, mph->km/h, h->min, min->h, MW+19, MW-19, MW+7, MW-7, BASIC, MEHR, =

### FIN

SET K0, SET P%, SET JAHRE, SET RATE/M, INFO, ENDWERT, ZINSEN, RESET, TIP+10%, TIP+15%, TIP+20%, SET PERS, / PERS, SET KURS, EUR->$, $->EUR, BASIC, MEHR, =

### PRG

->HEX, ->BIN, ->OCT, NOT, AND, OR, XOR, MOD, <<, >>, ABS, INT, SGN, ZUFALL, pi, e, RPN, BASIC, MEHR, =

### PLOT

sin x, cos x, tan x, x^2, x^3, sqrt x, log x, 1/x, e^x, ln x, |x|, 2^x, sinh, cosh, tanh, x^4, GAUSS, FLOOR, sinc x, x*sin x, BASIC, MEHR, =

### FORM

SET A, SET B, SET C, INFO, % VON, DREISATZ, KREIS A, KREIS U, PYTH, OHM, BMI, AVG ABC, CLR ABC, KM/H, NET19, BRU19, BASIC, MEHR, =

## Spiele

Math Attack startet über GAME und 1/2/3. Snake startet über GAME und 5.

## Tastatur

- `0-9` - digits
- `, or .` - decimal separator
- `+ - * /` - basic operators
- `Enter or =` - equals
- `Escape` - AC
- `%` - percent
- `r or w` - square root
- `arrow keys` - Snake direction and secret-code input

## Speicher und Datenschutz

Alle Daten bleiben im Browser-localStorage. Es gibt keine Analytics, keine externen Schriftaufrufe und keine Live-Wechselkurs-API.

theme, sound, angle mode, history, memory, finance parameters, exchange rate, persons, RPN mode, RPN stack, formula variables, game high scores, Virtual Boy unlock

## Grenzen

- Service worker registration only runs on HTTPS.
- The inline manifest has icons only when opened via HTTP or HTTPS.
- Currency conversion uses a manually stored rate and no live-rate API.
- Programmer base conversion displays the converted value in the status line; it does not replace the main display.
- Browser sharing, clipboard, vibration and battery display depend on browser support.
- The UI language inside the app is German.

## Versionsinformation

CALC BOY 3.1.0 / calcboy-v3.1.0
