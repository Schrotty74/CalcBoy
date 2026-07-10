# CALC BOY – Nächste Schritte

Stand: 10.07.2026  
Ausgangsbasis: **v3.1.0** auf `main`

## Aktueller Zustand

Version 3.1.0 ist in `index.html`, `sw.js`, den beiden Changelogs und den beiden Handbüchern konsistent dokumentiert. Die PWA umfasst BASIC, EXT, CONV, FIN, PRG, PLOT und FORM sowie Verlaufsexport, Themes, Math Attack und Snake.

Für die nächste Arbeitssitzung ist keine bereits beauftragte Funktionsänderung dokumentiert.

## Geprüfter offener Dokumentationspunkt

- `SECURITY.md` und `SECURITY.de.md` nennen noch „v3.0.2 / 1.7“, während App, Service Worker, Changelog und Handbuch bereits auf v3.1.0 stehen.
- Vor der Korrektur sollte geklärt werden, wofür „1.7“ steht. Wenn es keine eigenständige, weiterhin gültige Versionsnummer ist, sollte der Zusatz entfernt und der Stand in beiden Dateien auf v3.1.0 gesetzt werden.

## Prüfung vor dem nächsten Release

Da das Repository keinen Build-Schritt und keine automatisierte Testsuite enthält, ist derzeit ein manueller Smoke-Test erforderlich:

- App online laden, anschließend offline neu öffnen.
- Installation/Start als iPhone-PWA und Safe Areas im Hoch- und Querformat prüfen.
- BASIC-Rechnung, smarte Prozentfälle und ERROR-Verhalten testen.
- Jede Zusatzseite über `EXT`/`MEHR` erreichen und mit `BASIC` zurückkehren.
- FIN-Parameter, RPN-Stack und Formelvariablen nach einem Neustart prüfen.
- Verlauf übernehmen sowie Text- und PNG-Export testen.
- Theme, Sound, Math Attack und Snake kurz prüfen.
- Vorhandene `localStorage`-Daten aus einer älteren Version weiterverwenden.
- Versionsgleichheit zwischen Changelog, `index.html` und `sw.js` kontrollieren.
- Englische und deutsche Dokumentation gemeinsam aktualisieren.

## Nur bei ausdrücklichem Auftrag

- Neue Funktionen oder weitere Formeln/Umrechnungen ergänzen.
- `index.html` auf mehrere Dateien aufteilen oder ein Framework einführen.
- Externe APIs, Live-Wechselkurse, Analytics oder sonstige Netzwerk-Abhängigkeiten hinzufügen.
- Versionsnummer erhöhen oder einen Release markieren.

## Übergabehinweis

Vor weiterer Arbeit zuerst [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), danach die tatsächliche Implementierung in `index.html` und `sw.js` lesen. README und Handbuch erklären die Bedienung; das Verhalten der App wird jedoch durch den Code bestimmt.
