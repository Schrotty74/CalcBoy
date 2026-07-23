# CALC BOY – Nächste Schritte

**Stand:** 2026-07-23

Diese Liste enthält nur aus dem aktuellen Repository belegte, offene Punkte. Bei größeren Änderungen aktualisieren.

## Priorität hoch

- **Dokumentationsmenü abgleichen:** Der aktuelle Kopfbereich in `index.html` nutzt ein einzelnes Menü mit Theme, Spiel, Sound, About, GitHub und Discord. Bestehende Handbücher und der Generator `docs/tools/build_docs.py` zeigen beziehungsweise beschreiben noch einzelne THEME-, GAME- und SND-Buttons. Vor einer Dokumentationsveröffentlichung Markdown-Quellen, Generator, Screenshots und betroffene PDFs gemeinsam aktualisieren.

## Priorität normal

- **Dokumentationsumgebung verifizieren:** Vor dem nächsten PDF-Build feststellen, welche lokale Python-Umgebung `reportlab`, `Pillow` und `pypdf` bereitstellt. Keine Pakete global installieren oder aktualisieren; es gibt keine versionierte Abhängigkeitsdatei im Repository.
- **Sicherheitsdokumentation prüfen:** `SECURITY.md` und `SECURITY.de.md` nennen einen älteren Audit-Stand als den aktuellen Anwendungscode. Erst nach einer tatsächlichen neuen Prüfung aktualisieren.

## Vor einer öffentlichen Veröffentlichung

- [PORTFOLIO_UPDATE.md](PORTFOLIO_UPDATE.md) prüfen und gegebenenfalls die zentrale Portfolio-Darstellung aktualisieren.
- Sicherstellen, dass öffentliche Screenshots nur synthetische Demo-Daten zeigen.
- Versionsangaben in App, Service Worker, Changelog und erzeugter Dokumentation bewusst abgleichen.

## Nicht als offene Aufgabe behandeln

- Es wurden keine automatisierten Tests oder CI-Dateien im Repository gefunden. Das ist ein festgestellter Zustand, keine Aufforderung, ohne Auftrag neue Infrastruktur einzuführen.
- Lokale `.DS_Store`-Dateien gehören nicht zum Projektinhalt und bleiben unberührt.
