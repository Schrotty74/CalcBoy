# 📖 CALC BOY Handbuch (v3.1.0)

🇬🇧 [English manual](MANUAL.md)

CALC BOY ist eine Taschenrechner-PWA im klassischen Nintendo-Stil. Dieses Handbuch ist wie die App aufgebaut: ein Kapitel pro Seite, und darin jede Taste einzeln erklärt.

## Inhalt

1. [Erste Schritte](#erste-schritte)
2. [Bedienkonzept](#bedienkonzept)
3. [Die drei Tasten oben](#die-drei-tasten-oben)
4. [Das Display (LCD)](#das-display-lcd)
5. [BASIC-Seite](#basic-seite)
6. [EXT-Seite (wissenschaftlich)](#ext-seite-wissenschaftlich)
7. [CONV-Seite (Einheiten)](#conv-seite-einheiten)
8. [FIN-Seite (Finanzen)](#fin-seite-finanzen)
9. [PRG-Seite (Programmierer & RPN)](#prg-seite-programmierer--rpn)
10. [PLOT-Seite (Funktionsgraphen)](#plot-seite-funktionsgraphen)
11. [FORM-Seite (Formel-Assistent)](#form-seite-formel-assistent)
12. [Spiele](#spiele)
13. [Quermodus](#quermodus)
14. [Tastatur-Kürzel](#tastatur-kürzel)
15. [Geheim-Theme freischalten](#geheim-theme-freischalten)
16. [Speicherung & Datenschutz](#speicherung--datenschutz)
17. [Problemlösung](#problemlösung)

## Erste Schritte

Öffne https://schrotty74.github.io/CalcBoy/ im Browser. Auf dem iPhone: in Safari öffnen, Teilen → „Zum Home-Bildschirm" – dann startet CALC BOY als Vollbild-App. Nach dem ersten Laden funktioniert alles komplett offline.

Beim Start läuft eine kurze Boot-Animation. Zahlen werden im deutschen Format angezeigt: Komma als Dezimaltrenner, Punkte als Tausendertrenner. Maximal 12 Stellen sind eingebbar; lange Ergebnisse werden automatisch kleiner dargestellt. Unmögliche Operationen (z. B. Division durch 0) zeigen **ERROR** – die nächste Ziffer startet neu.

## Bedienkonzept

Die App besteht aus drei Bereichen: den **Pill-Tasten oben** (THEME, GAME, SND), dem **LCD** und dem **Tastenfeld**. Das Tastenfeld hat sieben Seiten:

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

- **EXT** (auf der BASIC-Seite, unten links) öffnet die erste Zusatzseite.
- **MEHR** (auf jeder Zusatzseite) schaltet zur nächsten Seite weiter.
- **BASIC** (auf jeder Zusatzseite) kehrt zum Standard-Tastenfeld zurück.
- **=** funktioniert auf jeder Seite.

## Die drei Tasten oben

**THEME** (links) – schaltet zum nächsten Konsolen-Look. Verfügbar sind sechs Themes: Game Boy (Standard), GB Color, NES, Super NES, Switch und Famicom; ein siebtes (Virtual Boy) ist freischaltbar (siehe [Geheim-Theme](#geheim-theme-freischalten)). Der Name erscheint kurz im LCD, der Wechsel spielt eine Cartridge-Animation, und jedes Theme hat einen eigenen Tastenklang (z. B. NES dumpfer, Switch heller). Die Auswahl wird gespeichert.

**GAME** (Mitte) – öffnet das Spielemenü (siehe [Spiele](#spiele)). Während eines laufenden Spiels beendet die Taste das Spiel.

**SND** (rechts) – schaltet die 8-Bit-Tastentöne ein (SND ON) oder aus (SND OFF, Taste erscheint gedimmt). Wird gespeichert.

## Das Display (LCD)

Das LCD hat zwei Zeilen: oben die **Statuszeile** (laufende Rechnung, Meldungen, Spielstand), unten die **Ergebniszeile**. Ein kleines **M** oben links bedeutet: Im Speicher (M+/M−) liegt ein Wert ungleich 0.

**Tippen aufs Display** öffnet den **Verlauf**:
- Zeigt die letzten 10 Rechnungen mit Ergebnis.
- **Eintrag antippen** übernimmt dessen Ergebnis in die Anzeige.
- **» TEILEN / EXPORT** exportiert den Verlauf als Text über das Share-Sheet (oder in die Zwischenablage).
- **» PNG TEILEN** rendert den Verlauf als Bild und teilt/lädt es als PNG-Datei.
- Unter den Einträgen stehen **Σ** (Summe aller Ergebnisse) und **Ø** (deren Mittelwert).
- Erneutes Tippen (oder jede Taste) schließt den Verlauf.

**Langes Drücken** (~0,5 s) aufs Display kopiert das aktuelle Ergebnis in die Zwischenablage („KOPIERT" erscheint).

## BASIC-Seite

Tasten: `AC ± % √ | 7 8 9 ÷ | 4 5 6 × | 1 2 3 − | 0 , + | EXT =`

- **0–9** – Zifferneingabe (max. 12 Stellen).
- **,** – Dezimalkomma. Nur ein Komma pro Zahl möglich.
- **÷ × − +** – Grundrechenarten. Kettenrechnungen werden von links nach rechts ausgewertet: `2 + 3 × 4 =` ergibt 20 (erst 2+3, dann ×4) – wie bei einem klassischen Tischrechner, ohne Punkt-vor-Strich.
- **=** – rechnet aus und schreibt die Rechnung in den Verlauf. (Im RPN-Modus: legt die Zahl auf den Stack, siehe [PRG-Seite](#prg-seite-programmierer--rpn).)
- **AC** – löscht Eingabe und laufende Rechnung. Beendet auch Spiele/Menüs; im RPN-Modus leert AC zusätzlich den Stack.
- **±** – wechselt das Vorzeichen der angezeigten Zahl.
- **%** – smarte Prozent-Taste mit drei Fällen:
  - Nach **+ oder −**: Prozent vom ersten Operanden. `100 + 10 %` → 110; `200 − 25 %` → 150.
  - Nach **× oder ÷**: wandelt in den Faktor um. `50 × 10 %` → 5.
  - **Alleinstehend**: teilt durch 100. `10 %` → 0,1.
- **√** – Quadratwurzel der angezeigten Zahl. Negative Eingabe → ERROR.
- **EXT** – wechselt zu den Zusatzseiten.

## EXT-Seite (wissenschaftlich)

Tasten: `MC MR M+ M− | sin cos tan DEG | log ln 10^x e^x | x² x³ xʸ ∛x | 1/x n! π e | BASIC MEHR =`

**Speicher (Memory):**
- **MC** – löscht den Speicher (M-Anzeige verschwindet).
- **MR** – ruft den Speicherwert in die Anzeige.
- **M+** – addiert die angezeigte Zahl zum Speicher.
- **M−** – subtrahiert die angezeigte Zahl vom Speicher.
- Der Speicher überlebt Neustarts; solange er ≠ 0 ist, zeigt das LCD ein **M**.

**Trigonometrie:**
- **sin / cos / tan** – wenden die Funktion sofort auf die angezeigte Zahl an. Beispiel (DEG): `30` → sin → 0,5.
- **DEG/RAD** – schaltet den Winkelmodus um: **DEG** = Grad, **RAD** = Bogenmaß. Die Taste zeigt den aktiven Modus; die Einstellung wird gespeichert und gilt für alle Trigonometrie-Tasten.

**Logarithmen & Exponenten:**
- **log** – Zehnerlogarithmus. `1000` → log → 3.
- **ln** – natürlicher Logarithmus (Basis e).
- **10^x** – Zehnerpotenz. `3` → 10^x → 1000.
- **e^x** – e hoch x.

**Potenzen & Wurzeln:**
- **x²** / **x³** – Quadrat bzw. Kubik der angezeigten Zahl.
- **xʸ** – beliebige Potenz als *zweistufige* Rechnung: Basis eingeben → xʸ drücken → Exponent eingeben → **=**. Beispiel: `2` xʸ `10` = → 1.024.
- **∛x** – Kubikwurzel. `27` → ∛x → 3.

**Sonstiges:**
- **1/x** – Kehrwert. `4` → 1/x → 0,25.
- **n!** – Fakultät. Nur ganze Zahlen 0–170; sonst ERROR. `5` → n! → 120.
- **π / e** – setzen die Konstante (3,1415926536 / 2,7182818285) in die Anzeige.

## CONV-Seite (Einheiten)

Prinzip: **Wert eingeben, Umrechnungstaste antippen** – das Ergebnis ersetzt die Anzeige, und die Statuszeile benennt die Umrechnung. Alle Umrechnungen lassen sich mit der Gegentaste wieder zurückrechnen.

- **km→mi / mi→km** – Kilometer ↔ Meilen (×0,621371 / ×1,609344).
- **m→ft / ft→m** – Meter ↔ Fuß (×3,28084 / ×0,3048).
- **°C→°F / °F→°C** – Temperatur (`×9/5+32` bzw. `(−32)×5/9`). `100` °C→°F → 212.
- **kg→lb / lb→kg** – Kilogramm ↔ Pfund (×2,204623 / ×0,453592).
- **cm→in / in→cm** – Zentimeter ↔ Zoll (÷2,54 / ×2,54).
- **l→gal / gal→l** – Liter ↔ US-Gallonen (×0,264172 / ×3,785412).
- **km/h→mph / mph→km/h** – Geschwindigkeit (gleiche Faktoren wie km/mi).
- **h→min / min→h** – Stunden ↔ Minuten (×60 / ÷60). `90` min→h → 1,5.
- **MW+19 / MW−19** – deutsche Mehrwertsteuer 19 %: **MW+19** rechnet Netto→Brutto (×1,19), **MW−19** rechnet Brutto→Netto (÷1,19, *nicht* −19 %!). `119` MW−19 → 100.
- **MW+7 / MW−7** – dasselbe mit dem ermäßigten Satz 7 % (×1,07 / ÷1,07).

## FIN-Seite (Finanzen)

Die Seite arbeitet mit **gespeicherten Parametern**: Zahl eintippen, dann mit einer SET-Taste zuweisen. Alle Parameter überleben Neustarts.

**Zinseszins mit Sparrate:**
- **SET K0** – speichert die Anzeige als Startkapital.
- **SET P%** – speichert den Jahreszinssatz in Prozent.
- **SET JAHRE** – speichert die Laufzeit in Jahren.
- **SET RATE/M** – speichert die monatliche Sparrate.
- **INFO** – zeigt die Zusammenfassung: Endwert, Summe der Einzahlungen und Zinsertrag.
- **ENDWERT** – berechnet das Endkapital mit **monatlicher Verzinsung**: `K0·(1+i)^m + Rate·((1+i)^m−1)/i` mit `i = P/1200` und `m = Jahre·12`. Beispiel: K0 = 1.000, P = 3, Jahre = 10, Rate = 50 → **8.336,42**. Das Ergebnis landet im Verlauf.
- **ZINSEN** – zeigt nur den Zinsertrag (Endwert − K0 − alle Raten). Im Beispiel: 1.336,42.
- **RESET** – setzt alle FIN-Parameter auf die Standardwerte zurück (K0 1000, P 3, Jahre 10, Rate 50, Personen 2, Kurs 1,08).

**Trinkgeld & Rechnung teilen:**
- **TIP+10% / TIP+15% / TIP+20%** – schlägt das Trinkgeld auf die angezeigte Rechnung auf. `85` TIP+15% → 97,75.
- **SET PERS** – speichert die angezeigte Zahl als Personenanzahl (mindestens 1, wird gerundet).
- **÷ PERS** – teilt die Anzeige durch die gespeicherte Personenzahl. Kompletter Ablauf: `4` SET PERS → `85` TIP+15% → ÷ PERS → **24,44 pro Person**.

**Währung:**
- **SET KURS** – speichert die Anzeige als Wechselkurs (z. B. 1,08 für EUR→USD).
- **€→$** – multipliziert mit dem Kurs. **$→€** – dividiert durch den Kurs.
- Bewusst **ohne Live-Kurse** (nichts verlässt das Gerät). Der Kurs funktioniert für jedes Währungspaar – €/$ ist nur die Beispielbeschriftung.

## PRG-Seite (Programmierer & RPN)

Alle Bit-Operationen arbeiten mit dem **Ganzzahl-Anteil** der Werte (Nachkommastellen werden abgeschnitten).

**Basis-Anzeige:**
- **→HEX / →BIN / →OCT** – zeigt den Ganzzahl-Anteil der Anzeige hexadezimal, binär oder oktal in der Statuszeile. Die Anzeige selbst bleibt dezimal. `255` →HEX → „HEX: FF"; `10` →BIN → „BIN: 1010".

**Binäre Operatoren** (Ablauf wie ÷/×: erste Zahl → Operator → zweite Zahl → =):
- **AND / OR / XOR** – bitweise Verknüpfung. `12 AND 10 =` → 8; `12 OR 10 =` → 14; `12 XOR 10 =` → 6.
- **MOD** – Divisionsrest. `17 MOD 5 =` → 2.
- **«** – Bit-Shift nach links (×2 pro Stelle). `1 « 4 =` → 16.
- **»** – Bit-Shift nach rechts (÷2 pro Stelle). `255 » 4 =` → 15.

**Unäre Funktionen** (wirken sofort):
- **NOT** – bitweises Komplement (~x). `5` → NOT → −6.
- **ABS** – Betrag. `-7` → ABS → 7.
- **INT** – schneidet Nachkommastellen ab. `3,9` → INT → 3.
- **SGN** – Vorzeichenfunktion: −1, 0 oder 1.
- **ZUFALL** – Zufallszahl zwischen 1 und 100.
- **π / e** – Konstanten wie auf der EXT-Seite.

**RPN-Modus (umgekehrte polnische Notation):**
- **RPN** – schaltet den Modus ein/aus (wird gespeichert; die Statuszeile zeigt Stack-Tiefe und obersten Wert). Der Modus gilt, solange er aktiv ist, **auf allen Seiten**.
- Im RPN-Modus ändert sich die Bedeutung von = und Operatoren:
  - **=** legt die angezeigte Zahl auf den **Stack** (max. 8 Einträge, lokal gespeichert).
  - Ein **Operator** (÷ × − + xʸ AND …) nimmt den obersten Stack-Wert als ersten Operanden und verknüpft ihn mit der Anzeige. Beispiel: `3` = `4` + → **7**.
  - **AC** leert zusätzlich den Stack.
- Rechnungen landen mit „RPN"-Präfix im Verlauf.

## PLOT-Seite (Funktionsgraphen)

Eine Funktionstaste antippen – der Graph wird als Pixel-Zeichnung ins LCD gemalt, mit Achsen (wo sichtbar) und automatischer Skalierung. **Jede Taste oder ein Tipp aufs Display schließt den Plot.** Die 20 Funktionen mit ihren Zeichenbereichen:

| Taste | Funktion | Bereich |
|---|---|---|
| sin x / cos x | Sinus / Kosinus | −6,5…6,5 |
| tan x | Tangens (Polstellen ausgeblendet) | −6,5…6,5 |
| x² / x³ / x⁴ | Potenzen | −4…4 / −3…3 / −2,5…2,5 |
| √x | Quadratwurzel | 0…16 |
| log x / ln x | Logarithmen | 0,05…20 / 0,05…12 |
| 1/x | Hyperbel (Polstelle ausgeblendet) | −4…4 |
| e^x / 2^x | Exponentialfunktionen | −3…3 / −3…4 |
| \|x\| | Betragsfunktion | −4…4 |
| sinh / cosh / tanh | Hyperbelfunktionen | −3…3 / −3…3 / −4…4 |
| GAUSS | Glockenkurve e^(−x²) | −3,5…3,5 |
| FLOOR | Treppenfunktion ⌊x⌋ | −4…4 |
| sinc x | sin x ⁄ x | −15…15 |
| x·sin x | wachsende Schwingung | −12…12 |

## FORM-Seite (Formel-Assistent)

Die Seite arbeitet mit drei **Variablen A, B und C**: Werte eintippen und zuweisen, dann eine Formel-Taste drücken. Die Variablen bleiben gespeichert, bis sie überschrieben oder gelöscht werden.

**Variablen verwalten:**
- **SET A / SET B / SET C** – speichert die angezeigte Zahl als A, B bzw. C.
- **INFO** – zeigt die aktuellen Werte von A, B und C.
- **CLR ABC** – setzt alle drei Variablen auf 0 zurück.

**Formeln** (jeweils mit Belegung und Beispiel):
- **% VON** – A Prozent von B: `B·A/100`. A = 15, B = 200 → **30**.
- **DREISATZ** – Verhältnisrechnung `A : B = C : x`, Ergebnis `x = B·C/A`. „3 kg kosten 6 €, was kosten 5 kg?" → A = 3, B = 6, C = 5 → **10**.
- **KREIS A** – Kreisfläche mit Radius A: `π·A²`. A = 2 → 12,566.
- **KREIS U** – Kreisumfang mit Radius A: `2·π·A`. A = 2 → 12,566.
- **PYTH** – Hypotenuse aus den Katheten A und B: `√(A²+B²)`. A = 3, B = 4 → **5**.
- **OHM** – Spannung nach dem Ohmschen Gesetz `U = R·I` mit A = Widerstand (Ω) und B = Strom (A). A = 100, B = 0,5 → **50 V**.
- **BMI** – Body-Mass-Index `A / B²` mit A = Gewicht (kg) und B = Größe (m). A = 80, B = 1,8 → **24,69**.
- **Ø ABC** – Durchschnitt der drei Variablen: `(A+B+C)/3`.
- **KM/H** – Geschwindigkeit `A / B` mit A = Strecke (km) und B = Zeit (h). A = 150, B = 1,5 → **100 km/h**.
- **NET19** – rechnet Brutto→Netto (19 %): `A / 1,19` mit A = Bruttobetrag.
- **BRU19** – rechnet Netto→Brutto (19 %): `A · 1,19` mit A = Nettobetrag.

Jedes Formel-Ergebnis landet im Verlauf; die Statuszeile zeigt kurz die verwendete Belegung.

## Spiele

**GAME** öffnet das Menü: `1`, `2` oder `3` startet MATH ATTACK im jeweiligen Level, `5` startet SNAKE, `AC` bricht ab.

**MATH ATTACK** – 30 Sekunden Kopfrechnen. Die Aufgabe steht in der Statuszeile, Antwort eintippen, **=** drücken. Richtig = 1 Punkt; falsch zählt als Fehler; in beiden Fällen kommt sofort die nächste Aufgabe. Die Statuszeile zeigt Restzeit (T) und Punkte (S).
- Level 1 **EASY**: nur + und − mit kleinen Zahlen (bis 20).
- Level 2 **NORMAL**: + − bis 99, × ÷ mit dem Einmaleins bis 12.
- Level 3 **HARD**: + − bis 999, × ÷ bis 19.
- Jedes Level hat einen **eigenen Highscore**. Eine Runde **ohne einen einzigen Fehler** endet mit **PERFECT!** samt eigenem Jingle. **AC** bricht vorzeitig ab.

**SNAKE** – Klassiker im LCD. Steuerung: **8** = hoch, **2** = runter, **4** = links, **6** = rechts (oder Pfeiltasten). Futter fressen lässt die Schlange wachsen, das Tempo steigt mit jedem Bissen. Wand oder eigener Schwanz beendet das Spiel; der Highscore wird gespeichert. **AC** oder **GAME** beendet.

## Quermodus

iPhone quer drehen: Das Layout wechselt zu Display links, Tastenfeld rechts, und eine zusätzliche **Schnellzugriff-Spalte** mit sin, cos, tan, log, ln, x², 1/x, xʸ, π und e erscheint neben dem BASIC-Tastenfeld. Alle Zusatzseiten funktionieren auch quer.

## Tastatur-Kürzel

Am Mac/iPad mit Tastatur: Ziffern, `+ - * /`, `Enter` = Ergebnis, `Esc` = AC, `%` = Prozent, `R` oder `W` = Quadratwurzel. Pfeiltasten steuern SNAKE.

## Geheim-Theme freischalten

Gib ein:

`8 8 2 2 4 6 4 6 − +`

Dadurch wird das Virtual-Boy-Theme freigeschaltet, dauerhaft lokal gespeichert und kann anschließend über die **THEME**-Taste ausgewählt werden.

## Speicherung & Datenschutz

Alles wird ausschließlich **lokal im Browser** gespeichert: Theme, Sound, Winkelmodus, Rechenverlauf, Highscores (pro Level und für SNAKE), Speicherwert (M), FIN-Parameter, Wechselkurs, Personenzahl, RPN-Modus samt Stack und die Formel-Variablen A/B/C. Nichts wird irgendwohin übertragen; es gibt keine externen Verbindungen. Zum vollständigen Löschen die Website-Daten der Domain im Browser entfernen. Details: [SECURITY.de.md](SECURITY.de.md).

## Problemlösung

- **Kein Ton beim allerersten Start:** Browser blockieren Audio vor der ersten Berührung – einmal eine beliebige Taste drücken.
- **Alte Version nach einem Update:** Der Service Worker cached die App; App/Tab komplett schließen und zweimal neu öffnen.
- **Batterie-LED immer rot:** Die Battery-API gibt es nur in Chrome/Android. Auf dem iPhone bleibt die LED klassisch rot – wie beim originalen Game Boy.
- **= legt Zahlen ab statt zu rechnen:** Der RPN-Modus ist aktiv – auf der PRG-Seite mit **RPN** wieder ausschalten.
