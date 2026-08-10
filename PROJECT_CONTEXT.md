# CALC BOY – Projektkontext

**Stand:** 2026-08-10
**Zweck:** Diese Datei ist die zentrale Einstiegshilfe für neue Chats und nach einer Neuinstallation. Sie beschreibt den belegten Projektstand, keine Produkt-Roadmap.

## Zuerst lesen

1. Diese Datei.
2. [NEXT_STEPS.md](NEXT_STEPS.md) für den aktuellen, tatsächlich offenen Stand.
3. [README.de.md](README.de.md) und [SECURITY.de.md](SECURITY.de.md) für Produkt- und Datenschutzinformationen.
4. Bei Dokumentationsarbeit: [docs/README.md](docs/README.md), die passenden Quellen in `docs/src/` und [PORTFOLIO_UPDATE.md](PORTFOLIO_UPDATE.md).
5. Vor einer Veröffentlichung außerdem [CHANGELOG.de.md](CHANGELOG.de.md) und [PORTFOLIO_UPDATE.md](PORTFOLIO_UPDATE.md).

Die englischen Gegenstücke liegen jeweils neben den deutschen Dateien. Bestehende Dokumentation nicht ohne Anlass umstrukturieren oder doppeln.

## Projektziel

CALC BOY ist eine deutschsprachige, installierbare Taschenrechner-PWA im Stil klassischer Handheld-Konsolen. Sie soll nach dem ersten Laden offline funktionieren, ohne Tracking oder externe Laufzeit-Anfragen.

## Architektur und wichtige Dateien

- `index.html`: Die Anwendung. HTML, CSS, eingebettete Schrift, Manifest und JavaScript befinden sich bewusst in einer Datei.
- `sw.js`: Service Worker für den Cache eigener Dateien derselben Domain. Die Cache-Version muss bei einer veröffentlichten App-Version zum Versionsstand passen.
- `apple-touch-icon.png`, `icon-512.png`: App-Icons.
- `docs/data/calcboy_features.json`: Gemeinsame Datenquelle für die Dokumentationsgenerierung.
- `docs/src/`: Bearbeitbare Markdown-Quellen für deutsch- und englischsprachigen Schnellstart sowie Handbuch.
- `docs/assets/screenshots/`: Dokumentationsbilder.
- `docs/tools/build_docs.py`: Erzeugt Dokumentationsbilder, Markdown und PDFs.
- `docs/requirements.txt`: Versionierte Python-Abhängigkeiten für den Dokumentations-Build.
- `docs/output/pdf/`: Erzeugte PDFs.
- `CALC-BOY-Offline-3.1.0.zip`: Schlankes Offline-Paket mit App, Icons, GPL-Lizenz und den vollständigen DE/EN-Handbüchern.

Es gibt keine gefundenen Paketmanifeste, Lockfiles, CI-Konfigurationen oder automatisierten Anwendungstests im Repository. Eine nicht vorhandene Konfiguration nicht als bestehend voraussetzen.

## Daten und Datenschutz

Die App verwendet `localStorage` ausschließlich lokal für Theme, Sound, Winkelmodus, Verlauf, Speicherwert, FIN-Parameter, Wechselkurs, Personenzahl, RPN-Modus und -Stack, Formelvariablen, Highscores und die Virtual-Boy-Freischaltung. Es gibt keine Live-Wechselkurse, Analyse- oder Tracking-Dienste. Details stehen in [SECURITY.de.md](SECURITY.de.md).

Keine lokalen Pfade, Zugangsdaten, Tokens, privaten Testdaten, Exporte oder Backups in das Repository oder öffentliche Materialien aufnehmen. Öffentliche Namen ausschließlich als `Schrotty74` verwenden.

## Umgesetzte Funktionen

- BASIC, EXT, CONV, FIN, PRG, PLOT und FORM als Rechnerseiten.
- Verlauf, Text- und PNG-Export, Speicherfunktionen, RPN, lokale Finanzparameter, Funktionsgraphen und Formel-Assistent.
- Math Attack und Snake, Themes, optionale Tastentöne, Hochformat- und Quermodus.
- Ein Kopfmenü mit Theme, Spiel, Sound, About-Dialog, GitHub- und Discord-Link.
- Offline-Cache über den Service Worker und iOS-PWA-Metadaten.

Die fachlichen Bedienungsdetails stehen in den Handbüchern, nicht zusätzlich in dieser Datei.

## Build, Tests und Abhängigkeiten

Die Anwendung selbst benötigt keinen Build-Schritt. Für die Dokumentation ist der vorhandene Generator vorgesehen:

```sh
python3 -m venv docs/.venv
docs/.venv/bin/python -m pip install -r docs/requirements.txt
docs/.venv/bin/python docs/tools/build_docs.py
```

Der Generator importiert `reportlab`, `Pillow` und `pypdf`. Diese Python-Pakete sind projektgebundene Build-Abhängigkeiten und in `docs/requirements.txt` festgehalten. Die lokale Umgebung `docs/.venv/` ist absichtlich nicht versioniert. Nicht automatisch global installieren oder aktualisieren.

Vor jeder neuen App-Arbeit außerdem Projekt-Dokumentation, Manifeste, Lockfiles, Build-Skripte und CI-Konfiguration lesen. Allgemein wiederverwendbare Werkzeuge nur als Vorschlag mit Zweck, Quelle, offiziellem Installationsweg und Verifikation dokumentieren. Projektgebundene oder lockfile-gesteuerte Abhängigkeiten nicht global aufnehmen. Zugangsdaten und Zertifikate niemals automatisch anlegen oder speichern.

## Feste Arbeitsregeln

- Bestehende App-Dateien nur für die konkret angeforderte Änderung bearbeiten.
- Bei Änderungen an `index.html` die PWA-Version und `sw.js` nicht beiläufig verändern. Bei einer echten Versionsveröffentlichung beide bewusst abgleichen und die vorhandene Versionshistorie aktualisieren.
- Dokumentationsquellen, Screenshots und PDFs sind ein zusammenhängender Workflow. Keine generierten PDFs manuell als Ersatz für ihre Markdown-Quellen pflegen.
- Vor Veröffentlichungen, Beta-Ankündigungen oder neuen öffentlichen Materialien die Portfolio-Regel in [PORTFOLIO_UPDATE.md](PORTFOLIO_UPDATE.md) anwenden.
- Keine Releases, Tags, Commits oder Pushes ohne ausdrücklichen Auftrag erstellen.
- Bei größeren Änderungen diese Datei und [NEXT_STEPS.md](NEXT_STEPS.md) aktualisieren.

## Bekannte Einschränkungen und belegte Inkonsistenzen

- Offline-Betrieb erfordert einen ersten erfolgreichen Aufruf über HTTPS. Browser-Funktionen wie Teilen, Zwischenablage, Vibration und Batterieanzeige sind abhängig von der Plattform.
- Die App-Oberfläche ist deutsch; die Dokumentation liegt zusätzlich auf Englisch vor.
- Die Dokumentation beschreibt das aktuelle Kopfmenü. Die beiden Ansichten `menu-closed.png` und `menu-open.png` werden vom Generator in alle vier Handbücher eingebunden.

## Unbekannt oder nicht geprüft

- Es ist nicht belegt, ob außerhalb dieses Repositorys eine CI-Pipeline oder ein Hosting-Workflow konfiguriert ist.
- Es wurde in diesem Arbeitsgang kein vollständiger manueller Browser-Test aller Rechnerseiten ausgeführt.
