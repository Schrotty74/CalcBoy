# 📖 CALC BOY Anleitung (v3.0)

🇬🇧 [English manual](MANUAL.md)

CALC BOY ist eine Taschenrechner-PWA im klassischen Nintendo-Stil. Diese Anleitung erklärt jede Taste, jede Seite und jedes versteckte Feature.

## Erste Schritte

Öffne https://schrotty74.github.io/CalcBoy/ im Browser. Auf dem iPhone: in Safari öffnen, Teilen → „Zum Home-Bildschirm" – dann startet CALC BOY als Vollbild-App. Nach dem ersten Laden funktioniert alles komplett offline.

Beim Start läuft eine kurze Boot-Animation („CALC BOY" fällt ins Display). Zahlen werden im deutschen Format angezeigt: Komma als Dezimaltrenner, Punkte als Tausendertrenner.

## Die drei Tasten oben

- **THEME** (oben links): schaltet durch die Konsolen-Looks – Game Boy, GB Color, NES, Super NES, Switch, Famicom. Jedes Theme ändert auch den Tastenklang. Die Auswahl wird gespeichert. Beim Wechsel läuft eine kurze Cartridge-Wechsel-Animation.
- **GAME** (oben Mitte): öffnet das Spielemenü (siehe unten). Während eines Spiels beendet die Taste das Spiel.
- **SND** (oben rechts): schaltet die 8-Bit-Tastentöne ein/aus. Wird gespeichert.

## Display-Gesten (LCD)

- **Tippen** aufs Display: öffnet den **Verlauf** – die letzten 10 Rechnungen. Ein Eintrag übernimmt per Tipp sein Ergebnis. Unter den Einträgen stehen **Σ** (Summe) und **Ø** (Mittelwert) der Ergebnisse. Die oberste Zeile **» TEILEN / EXPORT** exportiert den Verlauf als Text (Share-Sheet oder Zwischenablage).
- **Langes Drücken** (~0,5 s): kopiert das aktuelle Ergebnis in die Zwischenablage.
- Ein kleines **M** oben links bedeutet: Im Speicher liegt ein Wert.

## BASIC-Seite (Standard-Tastenfeld)

Ziffern 0–9, Komma und die vier Operatoren ÷ × − +. Weitere Tasten:

- **AC**: löscht alles (beendet auch Spiele und Menüs)
- **±**: wechselt das Vorzeichen
- **%**: smarte Prozent-Taste. `100 + 10 %` = 110 (10 % *von 100*), `50 × 10 %` = 5. Alleinstehend ist `10 %` = 0,1
- **√**: Quadratwurzel (negative Eingabe zeigt ERROR)
- **=**: rechnet aus
- **EXT**: wechselt zu den erweiterten Seiten

Ergebnisse mit mehr als 12 Stellen werden automatisch kleiner dargestellt; unmögliche Operationen (z. B. ÷ 0) zeigen **ERROR** – jede Ziffer startet neu.

## Seiten-Navigation

**EXT** auf der BASIC-Seite führt zur ersten Zusatzseite. Auf jeder Zusatzseite:
**BASIC** führt zurück zum Standard-Tastenfeld, **MEHR** schaltet zur nächsten Seite (EXT → CONV → FIN → PRG → PLOT → EXT), **=** rechnet immer aus.

## EXT-Seite (wissenschaftlich)

- **MC / MR / M+ / M−**: Speicher löschen, abrufen, addieren, subtrahieren. Der Speicher überlebt Neustarts.
- **sin / cos / tan** mit **DEG/RAD**-Umschalter (die Taste zeigt den aktiven Modus; wird gespeichert)
- **log** (Basis 10), **ln** (natürlich), **10^x**, **e^x**
- **x²**, **x³**, **xʸ** (binärer Operator: Basis eingeben, xʸ drücken, Exponent eingeben, =), **∛x**
- **1/x**, **n!** (nur ganze Zahlen 0–170), **π**, **e**

## CONV-Seite (Einheiten-Umrechner)

Wert eingeben, Umrechnung antippen – das Ergebnis ersetzt die Anzeige, die Umrechnung wird darüber benannt. Verfügbar: km↔mi, m↔ft, °C↔°F, kg↔lb, cm↔in, l↔gal (US), km/h↔mph, h↔min. Die **MW**-Reihe rechnet deutsche Mehrwertsteuer: **MW+19** = Netto→Brutto (×1,19), **MW−19** = Brutto→Netto (÷1,19), gleiches für 7 %.

## FIN-Seite (Finanzen)

**Zinseszins mit monatlicher Sparrate:** Zahl eintippen, dann mit einer SET-Taste als Parameter speichern:
- **SET K0** – Startkapital
- **SET P%** – Zinssatz pro Jahr
- **SET JAHRE** – Laufzeit in Jahren
- **SET RATE/M** – monatliche Sparrate

**INFO** zeigt die aktuellen Parameter, **ENDWERT** berechnet den Endwert (monatliche Verzinsung), **ZINSEN** zeigt nur den Zinsertrag, **RESET** stellt die Standardwerte wieder her. Beispiel: K0 1000, P 3, JAHRE 10, RATE 50 → ENDWERT ≈ 8.336,42.

**Trinkgeld & Splitten:** zuerst Personenzahl setzen (eintippen, **SET PERS**), dann den Rechnungsbetrag eingeben, **TIP+10/15/20%** aufschlagen und mit **÷ PERS** durch die Personen teilen.

**Währung:** Wechselkurs einmal setzen (eintippen, **SET KURS**), dann mit **€→$** und **$→€** umrechnen. Bewusst ohne Live-Kurse – nichts verlässt das Gerät. Der Kurs funktioniert für jedes Währungspaar, die Beschriftung ist nur ein Beispiel.

Alle FIN-Parameter werden lokal gespeichert.

## PRG-Seite (Programmierer)

- **→HEX / →BIN / →OCT**: zeigt den Ganzzahl-Anteil der Anzeige in der jeweiligen Basis (der Anzeigewert bleibt dezimal)
- **AND / OR / XOR / MOD / « / »**: binäre Operatoren – erste Zahl, Operator, zweite Zahl, **=**. Werte werden auf Ganzzahlen gekürzt; « und » sind Bit-Shifts nach links/rechts
- **NOT**: Bit-Komplement (~x), **ABS**, **INT** (abschneiden), **SGN** (Vorzeichen: −1/0/1)
- **ZUFALL**: Zufallszahl 1–100

## PLOT-Seite

Eine von 20 Funktionen antippen (von sin, cos und tan über e^x, sinh/cosh/tanh und |x| bis zur Gauß-Glocke e^(−x²), Floor, sinc und x·sin x) – sie wird als Pixel-Graph ins LCD gezeichnet, mit Achsen, wo sichtbar. Jede Taste oder ein Tipp aufs Display schließt den Plot.

## Spiele (GAME-Taste)

Das GAME-Menü zeigt: **1 2 3** starten MATH ATTACK im jeweiligen Level, **5** startet SNAKE, **AC** bricht ab.

**MATH ATTACK:** 30 Sekunden Kopfrechnen. Die Aufgabe erscheint in der oberen Displayzeile, Antwort eintippen, **=** drücken. Richtig = 1 Punkt, falsch = zählt als Fehler, in beiden Fällen kommt die nächste Aufgabe. Level: 1 EASY (kleines ±), 2 NORMAL (± bis 99, × ÷ bis 12), 3 HARD (± bis 999, × ÷ bis 19). Jedes Level hat einen eigenen Highscore. Eine Runde ohne einen einzigen Fehler endet mit **PERFECT!** samt eigenem Jingle. **AC** bricht vorzeitig ab.

**SNAKE:** Steuerung mit **2** (runter), **4** (links), **6** (rechts), **8** (hoch) – oder mit den Pfeiltasten einer echten Tastatur. Futter fressen lässt die Schlange wachsen; mit jedem Bissen wird das Spiel schneller. Wand und eigener Schwanz beenden das Spiel. Highscore wird gespeichert. **AC** oder **GAME** beendet.

## Tastatur-Kürzel (Mac/iPad mit Tastatur)

Ziffern, `+ - * /`, `Enter` = Ergebnis, `Esc` = AC, `%` Prozent, `R` oder `W` = Wurzel. Pfeiltasten steuern SNAKE.

## Geheimnisse 🥚

Es gibt eine siebte Konsole. Alte Spieler kennen den Code… auf den Rechnertasten lautet er: **8 8 2 2 4 6 4 6 − +** (an der Tastatur: ↑ ↑ ↓ ↓ ← → ← → B A). Einmal eingegeben, ist das **VIRTUAL BOY**-Theme (rot auf schwarz) dauerhaft freigeschaltet und reiht sich in die THEME-Rotation ein.

## Speicherung & Datenschutz

Alles wird ausschließlich lokal im Browser gespeichert: Theme, Sound, Verlauf, Highscores, Speicherwert, Winkelmodus, Finanz-Parameter, Wechselkurs. Nichts wird irgendwohin übertragen. Zum vollständigen Löschen die Website-Daten der Domain im Browser entfernen. Details: [SECURITY.de.md](SECURITY.de.md).

## Problemlösung

- **Kein Ton beim allerersten Start:** Browser blockieren Audio vor der ersten Berührung – einmal eine beliebige Taste drücken.
- **Alte Version nach einem Update:** Der Service Worker cached die App; App/Tab komplett schließen und neu öffnen, notfalls zweimal.
- **Batterie-LED immer rot:** Die Battery-API gibt es nur in Chrome/Android. Auf dem iPhone bleibt die LED klassisch rot – wie beim originalen Game Boy.


## Neu in dieser Version

- 7 Game-Boy-Themes (inkl. freischaltbarem Virtual Boy)
- Verbesserte Safe-Area-Unterstützung für iPhone-PWAs
