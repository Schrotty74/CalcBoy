# CALC BOY – Projektkontext

Stand: 10.07.2026  
Aktuelle Version: **3.1.0**  
Repository: [Schrotty74/CalcBoy](https://github.com/Schrotty74/CalcBoy)  
Live-PWA: [schrotty74.github.io/CalcBoy](https://schrotty74.github.io/CalcBoy/)

## Ziel des Projekts

CALC BOY ist eine installierbare Taschenrechner-PWA im Stil klassischer Nintendo-Konsolen. Sie läuft nach dem ersten Laden offline, speichert alle Nutzerdaten ausschließlich lokal und verwendet weder Tracking noch externe Laufzeit-Abhängigkeiten.

## Technischer Aufbau

- `index.html`: komplette Anwendung mit HTML, CSS und JavaScript; die Schrift „Press Start 2P“ ist als Base64 eingebettet.
- `sw.js`: Service Worker mit Cache-First/Stale-While-Revalidate-Verhalten für eigene Dateien.
- `apple-touch-icon.png` und `icon-512.png`: App-Symbole.
- Das Web-App-Manifest wird in `index.html` zur Laufzeit als Blob erzeugt.
- Es gibt derzeit keinen Build-Schritt, kein Paketmanagement und keine automatisierte Testsuite.

Die Anwendung ist bewusst als Single-File-PWA aufgebaut. Neue Frameworks, Abhängigkeiten oder eine Aufteilung von `index.html` sollen nur nach ausdrücklicher Entscheidung eingeführt werden.

## Funktionsumfang

Die Seitenreihenfolge lautet:

`BASIC → EXT → CONV → FIN → PRG → PLOT → FORM → BASIC`

- **BASIC:** Grundrechenarten, smarte Prozentlogik, Vorzeichen und Quadratwurzel.
- **EXT:** Speicherfunktionen, Trigonometrie, DEG/RAD, Logarithmen, Potenzen, Wurzeln, Fakultät, π und e.
- **CONV:** Einheiten, Geschwindigkeiten, Zeit sowie deutsche MwSt. mit 19 % und 7 %.
- **FIN:** Zinseszins, Sparrate, Zinsertrag, Trinkgeld, Rechnungsteilung und manuelle Währungsumrechnung.
- **PRG:** Zahlensystem-Anzeige, Bit-Operatoren, Shifts, Ganzzahlfunktionen, Zufallszahl und RPN-Modus.
- **PLOT:** 20 vordefinierte Funktionsgraphen als Pixelgrafik im LCD.
- **FORM:** Formel-Assistent mit den persistenten Variablen A, B und C.
- **Zusätzlich:** Rechenverlauf mit Text-/PNG-Export, sieben Themes (davon Virtual Boy freischaltbar), 8-Bit-Sound, Math Attack und Snake.

Die vollständige Bedienung ist in [MANUAL.de.md](MANUAL.de.md) und [MANUAL.md](MANUAL.md) beschrieben.

## Lokale Daten und Datenschutz

Alle Zustände liegen als JSON unter dem einzigen `localStorage`-Schlüssel `calcboy`. Dazu gehören unter anderem:

- Theme, Sound und freigeschaltetes Virtual-Boy-Theme
- Verlauf und Highscores
- Speicherwert und DEG/RAD-Modus
- Finanzparameter und manueller Wechselkurs
- RPN-Modus und RPN-Stack
- Formelvariablen A, B und C

Bestehende `localStorage`-Daten müssen bei Änderungen kompatibel bleiben. Die App soll keine externen Requests, Telemetrie, Cookies oder Live-APIs erhalten. Clipboard, Web Share, Vibration, Web Audio und Battery Status werden nur lokal beziehungsweise nach Nutzeraktion verwendet.

## Versions- und Release-Regeln

Bei einer neuen Version müssen diese drei Stellen übereinstimmen:

1. neuester Eintrag in `CHANGELOG.md` und `CHANGELOG.de.md`
2. Versionsangabe im Kopf von `index.html`
3. Cache-Name `calcboy-vX.Y.Z` in `sw.js`

Die Version wird nur für einen ausdrücklich gewünschten Release erhöht. Dokumentation und beide Sprachfassungen sind gemeinsam zu aktualisieren.

## Relevante Dokumentation

- `README.md` / `README.de.md`: Überblick, Installation und Funktionsliste
- `MANUAL.md` / `MANUAL.de.md`: vollständige Bedienungsanleitung
- `CHANGELOG.md` / `CHANGELOG.de.md`: einzige Versionshistorie
- `SECURITY.md` / `SECURITY.de.md`: Sicherheit und Datenschutz
- `NEXT_STEPS.md`: geprüfte offene Punkte und Übergabe für die nächste Arbeitssitzung

## Leitplanken für Änderungen

- Vor Änderungen den tatsächlichen Stand in `index.html` und `sw.js` prüfen; sie sind für das Verhalten maßgeblich.
- Offline-first-Verhalten, lokale Speicherung und bestehende Daten erhalten.
- UI, Pixel-Look, deutsche Zahlenformatierung und Bedienlogik konsistent halten.
- Keine neuen Abhängigkeiten ohne zwingenden Grund und ausdrückliche Freigabe.
- Änderungen auf iPhone-PWA-Safe-Areas, Hoch-/Querformat, Tastaturbedienung und reduzierte Bewegung prüfen.
- Produktdokumentation immer gegen die implementierten Funktionen abgleichen.
