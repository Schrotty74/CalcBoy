# 🔒 Sicherheit & Datenschutz

🇬🇧 [English version](SECURITY.md)

CALC BOY wurde auf private Daten, externe Verbindungen und Tracking geprüft. Stand: Juli 2026, Version 3.0.

## Ergebnis der Prüfung

**Es sind keine privaten Daten enthalten und es werden keine erhoben.**

| Prüfpunkt | Ergebnis |
|---|---|
| Persönliche Daten (Namen, E-Mails, IDs) | ❌ keine enthalten |
| Lokale Pfade (z. B. `/Users/…`, `C:\…`) | ❌ keine enthalten |
| API-Keys, Tokens, Passwörter | ❌ keine enthalten |
| Externe Verbindungen / Requests | ❌ keine – Schrift ist als Base64 eingebettet |
| Tracking, Analytics, Cookies | ❌ nicht vorhanden |
| Datenspeicherung | ⚙️ nur lokal (localStorage): Theme, Sound, Rechenverlauf, Highscores, Speicherwert, Winkelmodus, Finanz-Parameter, Wechselkurs – verlässt nie das Gerät, löschbar über die Website-Daten des Browsers |

## Was das konkret bedeutet

- Die App besteht aus einer HTML-Datei plus Service Worker (sw.js) fürs Offline-Caching – gecacht werden **nur eigene Dateien derselben Domain**. Nach dem ersten Laden funktioniert sie vollständig offline.
- Es verlässt **keine einzige Information** das Gerät – keine IP-Übertragung an Font-CDNs, keine Telemetrie, nichts.
- Gespeichert werden ausschließlich Einstellungen und der Rechenverlauf – **lokal im Browser**, ohne Übertragung an irgendwen. Löschen: Website-Daten der Domain im Browser entfernen.
- Damit ist die App **DSGVO-unkritisch**: Es findet keine Verarbeitung personenbezogener Daten durch Dritte statt, nichts verlässt das Gerät.

## Berechtigungen

Die App fordert keine Berechtigungen an. Optional genutzt werden nur:

- **Web Audio API** für die 8-Bit-Tastentöne (lokal erzeugt, abschaltbar)
- **Vibration API** für haptisches Feedback, sofern das Gerät sie unterstützt
- **Battery Status API** (wo der Browser sie anbietet) zum Einfärben der BATTERY-LED – wird nur lokal gelesen, nie übertragen
- **Clipboard-/Web-Share-API** nur bei ausdrücklicher Nutzeraktion (Langdruck zum Kopieren, Teilen-Button im Verlauf)

## Sicherheitslücken melden

Falls dir dennoch etwas auffällt, eröffne bitte ein [Issue](../../issues) in diesem Repository.
