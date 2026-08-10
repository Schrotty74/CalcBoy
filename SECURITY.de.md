# Sicherheit & Datenschutz

🇬🇧 [English version](SECURITY.md)

- **Prüfdatum:** 10. August 2026
- **Geprüfte Version:** CALC BOY 3.1.0
- **Methode:** Statische Prüfung von `index.html`, `sw.js`, den Sicherheitsdokumenten und dem Dokumentations-Build. Die App wurde nicht ausgeführt und während der Prüfung wurde kein Netzwerkdienst aufgerufen.

## Ergebnis der Prüfung

Die Prüfung hat eine Cache-Einschränkung im Service Worker ergeben, die am 10. August 2026 behoben und mit einem gezielten Regressionstest geprüft wurde. Für Tracking, Analytics, eingebettete Zugangsdaten, XSS, Remote-Code-Ausführung oder eine automatische Übertragung von Rechnerdaten bleibt kein offener quellcodebasierter Befund.

| Bereich | Ergebnis |
|---|---|
| Persönliche Daten, lokale Pfade, API-Keys, Tokens und Passwörter | Im geprüften Quellcode nicht gefunden |
| Analytics, Cookies und Werbedienste | Nicht gefunden |
| Automatische Drittanbieter-Requests | Nicht gefunden |
| Schrift | Lokal als Base64 eingebettet, kein Font-CDN-Request |
| Rechnerdaten | Ausschließlich lokal im Browser-`localStorage` |
| Service-Worker-Cache | Auf die vier bekannten lokalen App-Dateien begrenzt; Query-URLs und andere Pfade werden nicht gecacht |

## Lokale Daten und bewusstes Teilen

CALC BOY speichert Einstellungen und Rechnerzustand nur lokal im Browser: Theme, Sound, Rechenverlauf, Highscores, Speicherwert, Winkelmodus, Finanzparameter, Wechselkurs, RPN-Stack und Formelwerte. Die App hat kein Konto, keine Serverdatenbank und keinen Analytics-Endpunkt.

Die App überträgt Berechnungen oder Einstellungen nicht automatisch an andere Dienste. Verlaufsexport und Teilen verwenden die Zwischenablage beziehungsweise Web Share **nur nach einer ausdrücklichen Aktion**. Das Ziel wählst du im Teilen-Dialog des Betriebssystems.

Im Menü befinden sich optionale Links zu GitHub und Discord. Das Öffnen eines solchen Links ist eine bewusste Navigation zu diesem externen Dienst; dafür gelten dessen übliche Browser-Verbindung und Datenschutzregeln.

Zum Löschen der lokal gespeicherten Rechnerdaten entfernst du die Website-Daten dieser Domain im Browser.

## Schutz des Offline-Caches

Der Service Worker legt die vier bekannten App-Dateien im Cache ab und aktualisiert nur diese gleichoriginären, erlaubten URLs. Anfragen mit Query-String, unbekannten Pfaden, anderen HTTP-Methoden oder fremden Ursprüngen werden nicht vom Laufzeit-Cache verarbeitet. Mit der Behebung wurde die Cache-Revision geändert, sodass beim Aktivieren die frühere Cache-Version entfernt wird.

Ein Regressionstest bestätigt, dass `index.html` weiterhin cachebar bleibt und Query-URLs, unbekannte Pfade, externe URLs sowie `POST`-Anfragen nicht gecacht werden. Damit ist die zuvor festgestellte Verfügbarkeits-Einschränkung des lokalen Speichers behoben.

## Optionale Browser-APIs

CALC BOY fordert keine eigenen Berechtigungsdialoge an. Soweit der Browser sie unterstützt, kann die App diese APIs lokal verwenden:

- **Web Audio API** für optionale 8-Bit-Tastentöne
- **Vibration API** für optionale haptische Rückmeldung
- **Battery Status API** für die lokale Batterieanzeige
- **Clipboard- und Web-Share-APIs** nach einer ausdrücklichen Kopier- oder Teilen-Aktion

Unterstützung und Berechtigungen werden vom Browser beziehungsweise Betriebssystem gesteuert.

## Umfang und Grenzen

Dies ist eine technische Quellcodeprüfung und keine Rechtsberatung. Hosting-Header, Browser-Speicherquoten und die bereitgestellte GitHub-Pages-Konfiguration liegen außerhalb dieses Repositorys und wurden nicht getestet. Das Cache-Verhalten wurde über einen isolierten Service-Worker-Regressionstest geprüft; ein vollständiger manueller Browser-Test war nicht Teil dieser Prüfung.

## Sicherheitslücken melden

Melde mögliche Sicherheitslücken bitte über einen privaten Sicherheitskanal, falls verfügbar, oder ansonsten als [Issue](../../issues), ohne sensible Proof-of-Concept-Details öffentlich zu veröffentlichen.
