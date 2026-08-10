# CALC BOY – Nächste Schritte

**Stand:** 2026-08-10

Diese Liste enthält nur aus dem aktuellen Repository belegte, offene Punkte. Bei größeren Änderungen aktualisieren.

## Priorität normal

- **Sicherheitsdokumentation prüfen:** `SECURITY.md` und `SECURITY.de.md` nennen einen älteren Audit-Stand als den aktuellen Anwendungscode. Erst nach einer tatsächlichen neuen Prüfung aktualisieren.

## Vor einer öffentlichen Veröffentlichung

- [PORTFOLIO_UPDATE.md](PORTFOLIO_UPDATE.md) prüfen und gegebenenfalls die zentrale Portfolio-Darstellung aktualisieren.
- Sicherstellen, dass öffentliche Screenshots nur synthetische Demo-Daten zeigen.
- Versionsangaben in App, Service Worker, Changelog und erzeugter Dokumentation bewusst abgleichen.

## Nicht als offene Aufgabe behandeln

- Es wurden keine automatisierten Tests oder CI-Dateien im Repository gefunden. Das ist ein festgestellter Zustand, keine Aufforderung, ohne Auftrag neue Infrastruktur einzuführen.
- Lokale `.DS_Store`-Dateien gehören nicht zum Projektinhalt und bleiben unberührt.
- Die Dokumentationsumgebung ist projektlokal unter `docs/.venv/` eingerichtet; die reproduzierbaren Paketversionen stehen in `docs/requirements.txt`.
