# 🔒 Sicherheit & Datenschutz

CALC BOY wurde auf private Daten, externe Verbindungen und Tracking geprüft. Stand: Juli 2026, Version 1.0.

## Ergebnis der Prüfung

**Es sind keine privaten Daten enthalten und es werden keine erhoben.**

| Prüfpunkt | Ergebnis |
|---|---|
| Persönliche Daten (Namen, E-Mails, IDs) | ❌ keine enthalten |
| Lokale Pfade (z. B. `/Users/…`, `C:\…`) | ❌ keine enthalten |
| API-Keys, Tokens, Passwörter | ❌ keine enthalten |
| Externe Verbindungen / Requests | ❌ keine – Schrift ist als Base64 eingebettet |
| Tracking, Analytics, Cookies | ❌ nicht vorhanden |
| Datenspeicherung (localStorage, IndexedDB, Cookies) | ❌ nicht vorhanden – Berechnungen existieren nur im Arbeitsspeicher |

## Was das konkret bedeutet

- Die App ist eine **einzelne, in sich geschlossene HTML-Datei**. Nach dem ersten Laden funktioniert sie vollständig offline.
- Es verlässt **keine einzige Information** das Gerät – keine IP-Übertragung an Font-CDNs, keine Telemetrie, nichts.
- Beim Schließen der App ist alles weg. Es gibt keine gespeicherten Verläufe oder Einstellungen.
- Damit ist die App **DSGVO-unkritisch**: Es findet keine Verarbeitung personenbezogener Daten statt.

## Berechtigungen

Die App fordert keine Berechtigungen an. Optional genutzt werden nur:

- **Web Audio API** für die 8-Bit-Tastentöne (lokal erzeugt, abschaltbar)
- **Vibration API** für haptisches Feedback, sofern das Gerät sie unterstützt

## Sicherheitslücken melden

Falls dir dennoch etwas auffällt, eröffne bitte ein [Issue](../../issues) in diesem Repository.
