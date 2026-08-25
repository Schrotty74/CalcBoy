# CALC BOY – Nächste Schritte

**Stand:** 2026-08-10

Diese Liste enthält nur aus dem aktuellen Repository belegte, offene Punkte. Bei größeren Änderungen aktualisieren. Allgemeine Arbeits-, Git-, Veröffentlichungs- und Repository-Datenschutzregeln stehen in `AGENTS.md`.

## Vor einer öffentlichen Veröffentlichung

- [PORTFOLIO_UPDATE.md](PORTFOLIO_UPDATE.md) prüfen und gegebenenfalls die zentrale Portfolio-Darstellung aktualisieren.
- Versionsangaben in App, Service Worker, Changelog und erzeugter Dokumentation bewusst abgleichen.

## Nicht als offene Aufgabe behandeln

- Es wurden keine automatisierten Tests oder CI-Dateien im Repository gefunden. Das ist ein festgestellter Zustand, keine Aufforderung, ohne Auftrag neue Infrastruktur einzuführen.
- Lokale `.DS_Store`-Dateien gehören nicht zum Projektinhalt und bleiben unberührt.
- Die Dokumentationsumgebung ist projektlokal unter `docs/.venv/` eingerichtet; die reproduzierbaren Paketversionen stehen in `docs/requirements.txt`.
