# Sicherheitsrichtlinie

[English](SECURITY.md)

## Unterstützte Versionen

| Version | Unterstützt |
| --- | --- |
| 3.1.x | Ja |
| 3.0.x und älter | Nein |

Die aktuell dokumentierte Version ist 3.1.0.

## Sicherheitsmodell

CALC BOY ist eine lokale PWA ohne Benutzerkonto, Analytics oder Tracking. Rechnerzustand und Einstellungen werden im Browser-`localStorage` gespeichert. Der Service Worker ist auf bekannte lokale App-Dateien beschränkt. Zwischenablage und Web Share werden nur nach ausdrücklicher Nutzeraktion verwendet.

## Sicherheitslücke melden

Melde mögliche Sicherheitslücken nach Möglichkeit vertraulich an den Repository-Inhaber. Veröffentliche keine sensiblen Proof-of-Concept-Details in einem öffentlichen Issue. Nenne CALC-BOY-Version, Browser/Betriebssystem und Schritte zum Reproduzieren und entferne private Daten.

## Geltungsbereich

Relevante Meldungen umfassen unter anderem lokale Rechnerdaten, Service-Worker-/Offline-Caching, Verlaufsexporte, Browser-APIs, Script-Injection, unbeabsichtigte Netzwerkzugriffe und Verhalten, das lokal gespeicherte Daten offenlegen oder verändern könnte.

Vielen Dank, dass du dabei hilfst, CALC BOY sicher zu halten.
