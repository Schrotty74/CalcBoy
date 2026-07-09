# Änderungsprotokoll

Alle wichtigen Änderungen an **CALC BOY** werden hier dokumentiert.

Das Repository verwendet aktuell im App-Header `v3.0` und im Service-Worker-Cache `calcboy-v3.0.2`. Dieses Änderungsprotokoll führt den aktuellen hochgeladenen Stand als `v3.0.2 / 1.7`.

## v3.0.2 / 1.7

### Neu
- Formel-Assistent (`FORM`) mit Prozent, Dreisatz, Kreis, Pythagoras, Ohm, BMI, Durchschnitt, Geschwindigkeit und MwSt.-Hilfen.
- RPN-Modus auf der Programmierer-Seite.
- PNG-Export für den Rechenverlauf.
- Freischaltbares Virtual-Boy-Theme als siebtes Konsolen-Theme.

### Geändert
- `INFO` im Finanzbereich zeigt jetzt Endwert, Einzahlungen und Zinsertrag.
- iPhone-PWA-Safe-Area-Behandlung hält `THEME`, `GAME` und `SND` unterhalb der iOS-Statusleiste erreichbar.
- Die LCD-Ergebniszeile behält eine feste Höhe, wenn lange Ergebnisse in kleinerer Schrift angezeigt werden.

### Behoben
- Layout-Sprung der Anzeige bei langen Ergebnissen wie `√2` verhindert.
- Standalone-iPhone-PWA-Layout mit aktivierter Statusleisten-Überlagerung verbessert.

## v3.0 / 1.6

### Neu
- Funktionsplotter-Seite mit 20 Pixel-Funktionsgraphen.
- Programmierer-Seite mit HEX, BIN, OCT, Bit-Operatoren und Shifts.
- Finanzseite mit Zinseszins, monatlicher Sparrate, Trinkgeld, Rechnungssplitting und manueller Währungsumrechnung.
- Erweiterte Einheitenumrechnung mit häufigen Umrechnungen und MwSt.-Hilfen.
- Math Attack und Snake als Minispiele.
- Geheimen Konami-Code zum Freischalten des Virtual-Boy-Themes.

### Geändert
- Single-File-PWA-Struktur erweitert.
- Lokale Speicherung für Einstellungen, Verlauf, Highscores, Speicher, Winkelmodus und Finanzparameter verbessert.

## v2.x

### Neu
- Wissenschaftliche Funktionen: Trigonometrie, Logarithmen, Potenzen, Wurzeln, Fakultät und Konstanten.
- Speicherfunktionen.
- Rechenverlauf mit Wiederverwendung und Textexport.
- Mehrere Konsolen-Themes und themespezifische Sounds.

## v1.0

### Neu
- Erste CALC-BOY-Version.
- Grundrechenarten.
- Game-Boy-inspiriertes Design.
- Offlinefähige PWA-Grundlage.
