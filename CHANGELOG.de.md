# Änderungsprotokoll

Alle wichtigen Änderungen an **CALC BOY** werden hier dokumentiert. Diese Datei ist die einzige Versionshistorie. Versionen folgen `MAJOR.MINOR.PATCH`; die Version im `index.html`-Header und der Service-Worker-Cache-Name (`calcboy-vX.Y.Z`) entsprechen immer dem neuesten Eintrag.

## v3.1.0 – 10.07.2026

### Neu
- **Formel-Assistent (FORM-Seite)**: Prozent-von, Dreisatz, Kreisfläche & -umfang, Pythagoras, Ohmsches Gesetz, BMI, Durchschnitt, Geschwindigkeit und MwSt.-Hilfen – gesteuert über drei lokale Variablen **A, B, C** (SET A/B/C, INFO, löschbar).
- **RPN-Modus** auf der Programmierer-Seite mit lokal gespeichertem Stack.
- **PNG-Export** für den Rechenverlauf (zusätzlich zum Text-Export).

### Geändert
- **INFO** im Finanzbereich zeigt jetzt Endwert, Gesamteinzahlungen und Zinsertrag.
- Verbesserte iPhone-PWA-Safe-Area: THEME, GAME und SND bleiben im installierten (Standalone-)Modus unterhalb der iOS-Statusleiste.
- Seitenreihenfolge ist jetzt BASIC → EXT → CONV → FIN → PRG → PLOT → FORM.
- Dokumentation umstrukturiert: Dieses Änderungsprotokoll ist die einzige Versionshistorie; die README verlinkt darauf.
- Handbuch komplett neu geschrieben: Seite für Seite wie die App gegliedert, jede einzelne Taste separat erklärt (Belegung, Formel, Beispiel); Gemini aus den README-KI-Links entfernt, Prompts zeigen jetzt auf die Raw-Manual-URL.

### Behoben
- Die Variablen-Lösch-Taste der FORM-Seite war irreführend mit VAR C beschriftet (wirkte wie eine Abruf-Taste); jetzt **CLR ABC**. DREI in **DREISATZ** umbenannt, und FORM-Tasten nutzen die kleinere Beschriftungsschrift für bessere Lesbarkeit.
- Die LCD-Ergebniszeile behält eine feste Höhe, wenn lange Ergebnisse (z. B. √2) auf kleinere Schrift wechseln – kein Layout-Sprung mehr.

## v3.0.2 – 09.07.2026

### Neu
- Plot-Seite von 8 auf **20 Funktionen** erweitert (e^x, ln x, |x|, 2^x, sinh, cosh, tanh, x⁴, Gauß-Glocke e^(−x²), Floor, sinc x, x·sin x), jeweils mit passendem Wertebereich.

### Behoben
- Plot-Tasten nicht mehr überdimensioniert; die Seite füllt ein volles, einheitliches Raster.

## v3.0.1 – 09.07.2026

### Behoben
- Alle Tastenseiten teilen sich jetzt ein festes 6-Reihen-Raster: identische Tastengrößen auf jeder Seite, und die BASIC/MEHR/=-Navigationszeile ist überall in der untersten Reihe verankert.

## v3.0.0 – 09.07.2026

### Neu
- **Finanz-Seite (FIN)**: Zinseszins mit monatlicher Sparrate (SET K0/P%/JAHRE/RATE, ENDWERT, ZINSEN, INFO, RESET), Trinkgeld +10/15/20 %, Rechnung durch Personen teilen, Währungsumrechnung mit manuell gesetztem Kurs (bewusst ohne Live-Kurs-API).
- **Programmierer-Seite (PRG)**: →HEX/→BIN/→OCT-Anzeige, AND, OR, XOR, MOD, Bit-Shifts « », NOT, ABS, INT, SGN, Zufallszahl.
- **Plot-Seite**: Funktionen als Pixel-Graphen im LCD mit Auto-Skalierung und Achsen.
- **SNAKE** als zweites Spiel (GAME-Menü → 5), Steuerung mit 2/4/6/8 oder Pfeiltasten, steigendes Tempo, eigener Highscore.
- Smarte Prozent-Taste: `100 + 10 %` = 110 (Prozent vom ersten Operanden bei + und −).
- Verlauf zeigt **Σ** (Summe) und **Ø** (Mittelwert) der gespeicherten Ergebnisse.
- Seiten-Navigation per MEHR durch die Zusatzseiten.

## v2.2.0 – 09.07.2026

### Neu
- **Einheiten-Umrechner (CONV)**: km↔mi, m↔ft, °C↔°F, kg↔lb, cm↔in, l↔gal (US), km/h↔mph, h↔min und deutsche MwSt. 19 %/7 % Netto↔Brutto.
- **MATH-ATTACK-Schwierigkeitsstufen** (EASY/NORMAL/HARD) mit Highscore pro Level und PERFECT-Jingle für fehlerfreie Runden.
- **Langes Drücken** aufs Display kopiert das Ergebnis; der Verlauf erhielt einen **Teilen/Export**-Eintrag (Text).
- **Theme-abhängige Tastentöne** (Wellenform und Tonhöhe pro Konsole).
- **Cartridge-Wechsel-Animation** beim Theme-Umschalten (respektiert „Bewegung reduzieren").
- **Batterie-LED** zeigt den echten Ladestand, wo die Battery-Status-API existiert (Chrome/Android); sonst klassische rote LED.

## v2.1.0 – 09.07.2026

### Neu
- **Erweiterte Seite (EXT)**: Speichertasten MC/MR/M+/M− mit persistentem Speicher und M-Anzeige im LCD, sin/cos/tan mit gespeichertem **DEG/RAD**-Umschalter, log, ln, 10^x, e^x, x², x³, xʸ, ∛x, 1/x, Fakultät n!, π und e.

### Geändert
- Untere Reihe in EXT + = geteilt, um die neue Seite zu erreichen.

## v2.0.0 – 09.07.2026

### Neu
- **Boot-Animation** mit Jingle („CALC BOY" fällt ins LCD).
- **Persistente Einstellungen**: Theme und Sound überleben Neustarts (localStorage).
- **Verlauf**: letzte 10 Rechnungen im LCD (Tippen öffnet, Eintrag antippen übernimmt das Ergebnis).
- **MATH ATTACK**: 30-Sekunden-Kopfrechenspiel mit Highscore.
- **Wissenschaftlicher Quermodus**: zusätzliche Funktionsspalte bei gedrehtem Gerät.
- **Konami-Code** (8 8 2 2 4 6 4 6 − +) schaltet das geheime **VIRTUAL-BOY**-Theme dauerhaft frei.
- **Service Worker** (sw.js) für volle Offline-Fähigkeit.

## v1.1.0 – 09.07.2026

### Neu
- Pixel-Art-App-Icon (apple-touch-icon 180 px + 512-px-Manifest-Icon), programmatisch im Game-Boy-Stil gezeichnet.

### Behoben
- Manifest-/Icon-Code abgesichert, sodass Sandbox-Vorschauen ohne echte URL keinen Skriptfehler mehr werfen.

## v1.0.0 – 09.07.2026

### Neu
- Erstveröffentlichung: Game-Boy-inspirierter Single-File-PWA-Taschenrechner.
- 6 Konsolen-Themes (Game Boy, GB Color, NES, Super NES, Switch, Famicom) mit Theme-Umschalter.
- Grundrechenarten, Prozent, Vorzeichen, Quadratwurzel; deutsches Zahlenformat (Dezimalkomma, Tausenderpunkte); 12-Stellen-Limit mit automatisch schrumpfender Anzeige; ERROR-Behandlung.
- 8-Bit-Tastentöne mit SND-Umschalter; Tastatur-Unterstützung.
- Eingebettete Schrift „Press Start 2P" (Base64) – null externe Requests.
- Inline-Web-App-Manifest und iOS-Meta-Tags für „Zum Home-Bildschirm" ohne Entwickler-Account.
- GPL-3.0-Lizenz, Sicherheits-/Datenschutz-Dokumentation.
