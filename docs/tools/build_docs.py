#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image as RLImage,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
DATA = json.loads((DOCS / "data" / "calcboy_features.json").read_text(encoding="utf-8"))
SRC = DOCS / "src"
PDF_OUT = DOCS / "output" / "pdf"
SHOT_DIR = DOCS / "assets" / "screenshots"

PAGE_W, PAGE_H = A4
MARGIN_X = 18 * mm
MARGIN_TOP = 18 * mm
MARGIN_BOTTOM = 16 * mm
CONTENT_W = PAGE_W - 2 * MARGIN_X

COLORS = {
    "case": "#b8b4ac",
    "case_dark": "#77746d",
    "lcd": "#9bbc0f",
    "ink": "#0f380f",
    "red": "#a43632",
    "yellow": "#e0c35a",
    "paper": "#fffdf7",
    "blue": "#315f7d",
    "green": "#4d7b4d",
    "line": "#d5d0c5",
}


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in candidates:
        if p and Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def safe_name(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def make_calculator_shot(page_id: str, title: str, buttons: list[str], filename: str, landscape=False, annotate=False, display="0", expr=""):
    scale = 2
    w, h = (980, 620) if landscape else (620, 880)
    im = Image.new("RGB", (w * scale, h * scale), COLORS["paper"])
    d = ImageDraw.Draw(im)
    f_title = font(28 * scale, True)
    f_small = font(13 * scale, True)
    f_lcd = font(26 * scale, True)
    f_btn = font(17 * scale, True)
    pad = 28 * scale
    case = (pad, pad, w * scale - pad, h * scale - pad)
    rounded(d, case, 34 * scale, COLORS["case"], COLORS["case_dark"], 4 * scale)
    d.text((case[0] + 28 * scale, case[1] + 20 * scale), "CALC BOY", fill="#2b2b2e", font=f_title)
    d.text((case[2] - 170 * scale, case[1] + 28 * scale), title, fill=COLORS["red"], font=f_small)
    for i, label in enumerate(["THEME", "GAME", "SND ON"]):
        x = case[0] + (48 + i * 168) * scale if not landscape else case[0] + (250 + i * 142) * scale
        rounded(d, (x, case[1] + 68 * scale, x + 110 * scale, case[1] + 102 * scale), 16 * scale, "#d8d3c9", "#67635c", 2 * scale)
        d.text((x + 18 * scale, case[1] + 79 * scale), label, fill="#222", font=f_small)
    if landscape:
        lcd = (case[0] + 34 * scale, case[1] + 134 * scale, case[0] + 390 * scale, case[1] + 430 * scale)
        key = (case[0] + 420 * scale, case[1] + 132 * scale, case[2] - 34 * scale, case[2] - 36 * scale)
    else:
        lcd = (case[0] + 42 * scale, case[1] + 128 * scale, case[2] - 42 * scale, case[1] + 330 * scale)
        key = (case[0] + 42 * scale, case[1] + 370 * scale, case[2] - 42 * scale, case[2] - 40 * scale)
    rounded(d, (lcd[0] - 12 * scale, lcd[1] - 18 * scale, lcd[2] + 12 * scale, lcd[3] + 28 * scale), 18 * scale, "#56585a", "#333", 2 * scale)
    rounded(d, lcd, 8 * scale, COLORS["lcd"], "#536b18", 2 * scale)
    d.text((lcd[0] + 18 * scale, lcd[1] + 20 * scale), expr or page_id.upper(), fill=COLORS["ink"], font=f_small)
    d.text((lcd[2] - 230 * scale, lcd[3] - 62 * scale), display, fill=COLORS["ink"], font=f_lcd)
    if page_id == "history":
        y = lcd[1] + 58 * scale
        for line in ["VERLAUF - TIPPEN = UEBERNEHMEN", ">> TEILEN / EXPORT", ">> PNG TEILEN", "12 + 30        = 42", "7 x 6          = 42", "SUMME          = 84"]:
            d.text((lcd[0] + 16 * scale, y), line, fill=COLORS["ink"], font=f_small)
            y += 24 * scale
    if page_id == "plot":
        x0, y0, x1, y1 = lcd[0] + 20 * scale, lcd[1] + 50 * scale, lcd[2] - 20 * scale, lcd[3] - 34 * scale
        d.line((x0, (y0 + y1) // 2, x1, (y0 + y1) // 2), fill=COLORS["ink"], width=1 * scale)
        d.line(((x0 + x1) // 2, y0, (x0 + x1) // 2, y1), fill=COLORS["ink"], width=1 * scale)
        pts = []
        for i in range(180):
            x = -math.pi * 2 + math.pi * 4 * i / 179
            px = x0 + (x + math.pi * 2) / (math.pi * 4) * (x1 - x0)
            py = (y0 + y1) / 2 - math.sin(x) * (y1 - y0) / 3
            pts.append((px, py))
        d.line(pts, fill=COLORS["ink"], width=3 * scale)
        d.text((x0, y1 + 8 * scale), "y = sin x  (TASTE = ZURUECK)", fill=COLORS["ink"], font=f_small)
    if page_id == "snake":
        x0, y0 = lcd[0] + 16 * scale, lcd[1] + 60 * scale
        d.text((lcd[0] + 16 * scale, lcd[1] + 18 * scale), "SNAKE  S:3  2/4/6/8 = STEUERN", fill=COLORS["ink"], font=f_small)
        for x, y in [(3, 4), (4, 4), (5, 4), (6, 4), (6, 5)]:
            d.rectangle((x0 + x * 24 * scale, y0 + y * 18 * scale, x0 + (x + 1) * 24 * scale - 4, y0 + (y + 1) * 18 * scale - 4), fill=COLORS["ink"])
        d.rectangle((x0 + 11 * 24 * scale, y0 + 7 * 18 * scale, x0 + 11 * 24 * scale + 10 * scale, y0 + 7 * 18 * scale + 10 * scale), fill=COLORS["ink"])
    cols = 4
    rows = math.ceil(len(buttons) / cols)
    gap = 9 * scale
    bx0, by0, bx1, by1 = key
    bw = (bx1 - bx0 - gap * (cols - 1)) / cols
    bh = min(58 * scale, (by1 - by0 - gap * (rows - 1)) / rows)
    for i, b in enumerate(buttons):
        row, col = divmod(i, cols)
        x = bx0 + col * (bw + gap)
        y = by0 + row * (bh + gap)
        fill = COLORS["red"] if b in ["=", "+", "-", "*", "/", "EXT", "MEHR", "BASIC"] else "#e9e3d7"
        rounded(d, (x, y, x + bw, y + bh), 14 * scale, fill, "#5f5b55", 2 * scale)
        tw = d.textlength(b, font=f_btn)
        d.text((x + max(4 * scale, (bw - tw) / 2), y + bh / 2 - 9 * scale), b, fill="#111", font=f_btn)
    if annotate:
        items = [("1", "Top controls", (case[0] + 80 * scale, case[1] + 78 * scale)), ("2", "LCD", (lcd[0] + 28 * scale, lcd[1] + 28 * scale)), ("3", "Keys", (bx0 + 30 * scale, by0 + 30 * scale))]
        for n, label, pos in items:
            d.ellipse((pos[0] - 12 * scale, pos[1] - 12 * scale, pos[0] + 12 * scale, pos[1] + 12 * scale), fill=COLORS["yellow"], outline="#665500", width=2 * scale)
            d.text((pos[0] - 5 * scale, pos[1] - 9 * scale), n, fill="#111", font=f_small)
            d.text((pos[0] + 18 * scale, pos[1] - 8 * scale), label, fill="#111", font=f_small)
    im = im.resize((w, h), Image.Resampling.LANCZOS)
    path = SHOT_DIR / filename
    im.save(path)
    return path


def create_screenshots():
    SHOT_DIR.mkdir(parents=True, exist_ok=True)
    expected = {
        "basic": "basic.png",
        "ext": "ext.png",
        "conv": "conv.png",
        "fin": "fin.png",
        "prg": "prg.png",
        "plot": "plot.png",
        "form": "form.png",
        "history": "history.png",
        "plot_sin": "plot-sin.png",
        "snake": "snake.png",
        "landscape": "landscape.png"
    }
    if os.environ.get("CALCBOY_USE_EXISTING_SCREENSHOTS") == "1" and all((SHOT_DIR / f).exists() for f in expected.values()):
        return {k: SHOT_DIR / v for k, v in expected.items()}
    paths = {}
    for page in DATA["pages"]:
        paths[page["id"]] = make_calculator_shot(page["id"], page["title"], page["buttons"], f"{page['id']}.png", annotate=(page["id"] == "basic"), display="42", expr=page["title"])
    paths["history"] = make_calculator_shot("history", "HISTORY", DATA["pages"][0]["buttons"], "history.png", display="42")
    paths["plot_sin"] = make_calculator_shot("plot", "PLOT", DATA["pages"][5]["buttons"], "plot-sin.png", display="sin")
    paths["snake"] = make_calculator_shot("snake", "SNAKE", DATA["pages"][0]["buttons"], "snake.png", display="S:3")
    paths["landscape"] = make_calculator_shot("landscape", "LANDSCAPE", DATA["pages"][1]["buttons"], "landscape.png", landscape=True, display="3,14159265", expr="EXT")
    return paths


STR = {
    "de": {
        "quick": "Schnellstart",
        "manual": "Benutzerhandbuch",
        "intro": "CALC BOY ist ein lokal laufender PWA-Taschenrechner im Stil klassischer Handheld-Konsolen. Diese Dokumentation beschreibt den aktuellen Quellcode der Version 3.1.0.",
        "install": "Installation",
        "install_steps": ["Live-Link in Safari oder Chrome öffnen.", "Über Teilen bzw. Browsermenü Zum Home-Bildschirm hinzufügen wählen.", "CALC BOY vom Home-Bildschirm starten. Im installierten Modus läuft die App im Vollbild."],
        "offline": "Offline-Betrieb",
        "offline_text": "Der Service Worker speichert App-Shell, index.html und Icons im Cache calcboy-v3.1.0. Die Registrierung erfolgt nur auf HTTPS. Nach dem ersten Online-Start kann die App aus dem Cache starten.",
        "storage": "Speicher und Datenschutz",
        "storage_text": "Alle Daten bleiben im Browser-localStorage. Es gibt keine Analytics, keine externen Schriftaufrufe und keine Live-Wechselkurs-API.",
        "limitations": "Grenzen",
        "trouble": "Fehlerbehebung",
        "keyboard": "Tastatur",
        "games": "Spiele",
        "themes": "Themes",
        "examples": "Beispiele",
        "version": "Versionsinformation",
        "created": "Erstellt aus dem aktuellen Repository-Stand.",
        "toc": "Inhalt"
    },
    "en": {
        "quick": "Quick Start Guide",
        "manual": "User Manual",
        "intro": "CALC BOY is a local-first PWA calculator styled after classic handheld consoles. This documentation describes the current source code for version 3.1.0.",
        "install": "Installation",
        "install_steps": ["Open the live link in Safari or Chrome.", "Use Share or the browser menu and choose Add to Home Screen.", "Launch CALC BOY from the home screen. Installed mode opens the app fullscreen."],
        "offline": "Offline Mode",
        "offline_text": "The service worker caches the app shell, index.html and icons under calcboy-v3.1.0. Registration runs only on HTTPS. After the first online launch, the app can start from cache.",
        "storage": "Storage and Privacy",
        "storage_text": "All data remains in browser localStorage. There is no analytics code, no external font request and no live exchange-rate API.",
        "limitations": "Limitations",
        "trouble": "Troubleshooting",
        "keyboard": "Keyboard",
        "games": "Games",
        "themes": "Themes",
        "examples": "Examples",
        "version": "Version Information",
        "created": "Generated from the current repository state.",
        "toc": "Contents"
    }
}


def p(txt: str) -> str:
    return txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def markdown(lang: str, kind: str, shots: dict[str, Path]) -> str:
    s = STR[lang]
    title = s["quick"] if kind == "quick" else s["manual"]
    lines = [f"# CALC BOY - {title}", "", f"Version: {DATA['app']['version']}", "", s["intro"], ""]
    lines += [f"## {s['install']}", ""]
    for i, step in enumerate(s["install_steps"], 1):
        lines.append(f"{i}. {step}")
    lines += ["", f"## {s['offline']}", "", s["offline_text"], "", "![BASIC](../assets/screenshots/basic.png)", ""]
    sections = ["basic", "ext", "conv", "fin", "prg", "plot", "form"]
    lines += ["## Interface overview" if lang == "en" else "## Bedienueberblick", ""]
    lines += ["Use EXT to leave BASIC, MEHR to cycle through the extra pages, and BASIC to return." if lang == "en" else "Mit EXT verlaesst du BASIC, mit MEHR wechselst du durch die Zusatzseiten, mit BASIC kehrst du zurueck.", ""]
    for pid in sections:
        page = next(x for x in DATA["pages"] if x["id"] == pid)
        details = page_detail(pid, lang)
        lines += [f"### {page['title']}", "", f"![{page['title']}](../assets/screenshots/{pid}.png)", "", details["overview"], ""]
        lines += [f"**{label('how', lang)}**", ""]
        for item in details["how"]:
            lines.append(f"- {item}")
        lines += ["", f"**{label('notes', lang)}**", ""]
        for item in details["notes"]:
            lines.append(f"- {item}")
        lines += ["", f"**{label('example', lang)}e**" if lang == "de" else "**Examples**", ""]
        for name, steps in example_rows(pid, lang):
            lines.append(f"- **{name}:** {steps}")
        if kind == "manual":
            lines += ["", f"**{label('buttons', lang)}**", ""]
            for b in page["buttons"]:
                lines.append(f"- `{b}` - {describe_button(b, lang)}")
        lines.append("")
    lines += [f"## {s['games']}", "", "GAME opens the menu. Press 1, 2 or 3 for Math Attack levels, or 5 for Snake." if lang == "en" else "GAME oeffnet das Menue. 1, 2 oder 3 startet Math Attack, 5 startet Snake.", "", f"## {s['keyboard']}", ""]
    for key, desc in keyboard_rows(lang):
        lines.append(f"- `{key}` - {desc}")
    lines += ["", f"## {s['storage']}", "", s["storage_text"], "", ", ".join(storage_items(lang)), "", f"## {s['limitations']}", "", limitation_text(lang)]
    lines += ["", f"## {s['version']}", "", f"{DATA['app']['name']} {DATA['app']['version']} / {DATA['app']['cache']}"]
    return "\n".join(lines) + "\n"


class NumberedDoc(BaseDocTemplate):
    def __init__(self, filename, title, lang):
        super().__init__(filename, pagesize=A4, rightMargin=MARGIN_X, leftMargin=MARGIN_X, topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM)
        self.title = title
        self.lang = lang
        frame = Frame(MARGIN_X, MARGIN_BOTTOM, CONTENT_W, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id="normal")
        self.addPageTemplates(PageTemplate(id="p", frames=[frame], onPage=self.footer))

    def footer(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor(COLORS["line"]))
        canvas.line(MARGIN_X, 13 * mm, PAGE_W - MARGIN_X, 13 * mm)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#66615a"))
        canvas.drawString(MARGIN_X, 8 * mm, f"CALC BOY {DATA['app']['version']}")
        canvas.drawCentredString(PAGE_W / 2, 8 * mm, self.title)
        canvas.drawRightString(PAGE_W - MARGIN_X, 8 * mm, str(canvas.getPageNumber()))
        canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    base.add(ParagraphStyle(name="CoverTitle", parent=base["Title"], fontSize=30, leading=34, alignment=TA_CENTER, textColor=colors.HexColor("#222222"), spaceAfter=12))
    base.add(ParagraphStyle(name="H1x", parent=base["Heading1"], fontSize=18, leading=22, textColor=colors.HexColor(COLORS["red"]), spaceBefore=8, spaceAfter=8))
    base.add(ParagraphStyle(name="H2x", parent=base["Heading2"], fontSize=13, leading=16, textColor=colors.HexColor(COLORS["blue"]), spaceBefore=8, spaceAfter=4))
    base.add(ParagraphStyle(name="Bodyx", parent=base["BodyText"], fontSize=9.2, leading=12.2, spaceAfter=5))
    base.add(ParagraphStyle(name="Smallx", parent=base["BodyText"], fontSize=8, leading=10))
    base.add(ParagraphStyle(name="Boxx", parent=base["BodyText"], fontSize=8.5, leading=11, backColor=colors.HexColor("#f3efe4"), borderColor=colors.HexColor("#d2c8ae"), borderWidth=0.5, borderPadding=6, spaceBefore=4, spaceAfter=6))
    return base


def bullet_list(items, st):
    return ListFlowable([ListItem(Paragraph(p(str(x)), st["Bodyx"])) for x in items], bulletType="bullet", leftIndent=12)


def shot(path: Path, width=CONTENT_W * 0.78):
    return RLImage(str(path), width=width, height=width * path.stat().st_size * 0 + width * 0.72)


def img(path: Path, width=CONTENT_W * 0.45, max_height=86 * mm):
    im = Image.open(path)
    ratio = im.height / im.width
    height = width * ratio
    if height > max_height:
        height = max_height
        width = height / ratio
    return RLImage(str(path), width=width, height=height)


def table(rows, st, widths=None):
    t = Table([[Paragraph(p(str(c)), st["Smallx"]) for c in row] for row in rows], colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9e3d7")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#222222")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor(COLORS["line"])),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def compact_table(rows, st, widths=None):
    t = table(rows, st, widths)
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 7.2),
        ("LEADING", (0, 0), (-1, -1), 8.2),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def label(key: str, lang: str) -> str:
    labels = {
        "key": ("Key", "Taste"),
        "function": ("Function", "Funktion"),
        "example": ("Example", "Beispiel"),
        "steps": ("Steps", "Eingabe / Ergebnis"),
        "overview": ("What this page does", "Wofuer diese Seite da ist"),
        "how": ("How to use it", "So verwendest du es"),
        "notes": ("Important details", "Wichtige Details"),
        "buttons": ("Button reference", "Tastenuebersicht"),
    }
    return labels[key][0 if lang == "en" else 1]


def button_table(buttons, lang, st, page_id=None):
    items = [[b, describe_button(b, lang, page_id)] for b in buttons]
    half = math.ceil(len(items) / 2)
    rows = [[label("key", lang), label("function", lang), label("key", lang), label("function", lang)]]
    for i in range(half):
        left = items[i]
        right = items[i + half] if i + half < len(items) else ["", ""]
        rows.append(left + right)
    return compact_table(rows, st, [18 * mm, 60 * mm, 18 * mm, CONTENT_W - 96 * mm])


def examples_table(page_id: str, lang: str, st):
    examples = example_rows(page_id, lang)
    rows = [[label("example", lang), label("steps", lang)]] + examples
    return [
        Paragraph(label("example", lang) + "e" if lang == "de" else "Examples", st["H2x"]),
        compact_table(rows, st, [28 * mm, CONTENT_W * 0.46])
    ]


def page_detail(page_id: str, lang: str) -> dict[str, list[str] | str]:
    de = lang == "de"
    data = {
        "basic": {
            "overview": ("Standard calculator for everyday arithmetic, signs, square roots and smart percent calculations.",
                         "Standardrechner fuer Grundrechenarten, Vorzeichen, Quadratwurzel und smarte Prozentrechnung."),
            "how": ([
                "Enter the first number, choose an operator, enter the second number, then press =.",
                "Use AC to clear the current calculation. After ERROR, the next digit starts a new entry.",
                "Tap the LCD to open history; long-press the LCD to copy the displayed result."
            ], [
                "Erste Zahl eingeben, Rechenzeichen waehlen, zweite Zahl eingeben und = druecken.",
                "AC loescht Eingabe und laufende Rechnung. Nach ERROR beginnt die naechste Ziffer eine neue Eingabe.",
                "LCD antippen oeffnet den Verlauf; langes Druecken kopiert das angezeigte Ergebnis."
            ]),
            "notes": (["The percent key is context-aware: with + or - it calculates a percentage of the first operand."],
                      ["Die Prozent-Taste ist kontextabhaengig: Bei + oder - berechnet sie einen Prozentanteil des ersten Operanden."])
        },
        "ext": {
            "overview": ("Scientific and memory page with trigonometry, logarithms, powers, roots, factorial, pi and e.",
                         "Wissenschafts- und Speicherseite mit Trigonometrie, Logarithmen, Potenzen, Wurzeln, Fakultaet, pi und e."),
            "how": ([
                "For direct functions such as sin, log, x^2 or 1/x, enter a value and press the function key.",
                "For x^y, enter the base, press x^y, enter the exponent, then press =.",
                "Use DEG/RAD before trigonometry. DEG is saved and is the default unless changed."
            ], [
                "Bei direkten Funktionen wie sin, log, x^2 oder 1/x zuerst den Wert eingeben, dann die Funktion druecken.",
                "Fuer x^y zuerst die Basis eingeben, x^y druecken, den Exponenten eingeben und = druecken.",
                "Vor Trigonometrie DEG/RAD passend setzen. DEG wird gespeichert und ist die Voreinstellung, solange du sie nicht aenderst."
            ]),
            "notes": (["Factorial works only for whole numbers from 0 to 170."],
                      ["n! funktioniert nur fuer ganze Zahlen von 0 bis 170."])
        },
        "conv": {
            "overview": ("One-tap converters for distance, temperature, mass, volume, speed, time and German VAT.",
                         "Direktumrechner fuer Strecke, Temperatur, Gewicht, Volumen, Geschwindigkeit, Zeit und deutsche Mehrwertsteuer."),
            "how": ([
                "Enter the source value and press the desired conversion key.",
                "Use the matching reverse key if you need to convert back.",
                "VAT keys treat the entered value as net or gross according to the key label."
            ], [
                "Ausgangswert eingeben und die passende Umrechnungstaste druecken.",
                "Zum Zurueckrechnen die jeweilige Gegenrichtung verwenden.",
                "MW+ behandelt den Wert als netto, MW- behandelt ihn als brutto."
            ]),
            "notes": (["US gallons are used for litre/gallon conversion."],
                      ["Bei Liter/Gallone wird die US-Gallone verwendet."])
        },
        "fin": {
            "overview": ("Finance helpers for compound interest with monthly savings, interest amount, tips, bill splitting and manual currency conversion.",
                         "Finanzhilfen fuer Zinseszins mit Monatsrate, Zinsertrag, Trinkgeld, Rechnung teilen und manuelle Waehrungsumrechnung."),
            "how": ([
                "Set K0, P%, years and monthly rate with SET keys. ENDWERT calculates the future value.",
                "ZINSEN shows only the earned interest: future value minus start capital and deposits.",
                "Set persons before / PERS. Set exchange rate before EUR->$ or $->EUR."
            ], [
                "K0, P%, Jahre und Monatsrate mit SET-Tasten speichern. ENDWERT berechnet den spaeteren Wert.",
                "ZINSEN zeigt nur den Ertrag: Endwert minus Startkapital und Einzahlungen.",
                "Vor / PERS die Personenzahl setzen. Vor EUR->$ oder $->EUR den Kurs setzen."
            ]),
            "notes": (["Default values are K0 1000, P 3, years 10, monthly rate 50, persons 2 and exchange rate 1.08."],
                      ["Standardwerte sind K0 1000, P 3, Jahre 10, Monatsrate 50, Personen 2 und Kurs 1,08."])
        },
        "prg": {
            "overview": ("Programmer functions, integer base display, bitwise operators, random number and RPN mode.",
                         "Programmierfunktionen, Ganzzahl-Anzeige in anderen Zahlensystemen, Bitoperatoren, Zufallszahl und RPN-Modus."),
            "how": ([
                "HEX, BIN and OCT show the integer part of the display in the status line.",
                "AND, OR, XOR, MOD, << and >> are binary operators: enter first value, operator, second value, =.",
                "RPN changes = into push: enter a value, press =, enter the next value, then press an operator."
            ], [
                "HEX, BIN und OCT zeigen den ganzzahligen Anteil des Displays in der Statuszeile.",
                "AND, OR, XOR, MOD, << und >> sind Zweier-Operatoren: erster Wert, Operator, zweiter Wert, =.",
                "RPN macht = zur Stapel-Taste: Wert eingeben, = druecken, zweiten Wert eingeben, dann Operator druecken."
            ]),
            "notes": (["Bitwise functions use JavaScript integer behaviour and truncate decimal parts."],
                      ["Bitfunktionen verwenden JavaScript-Ganzzahlen; Nachkommastellen werden abgeschnitten."])
        },
        "plot": {
            "overview": ("Draws 20 built-in function graphs as pixel plots on the LCD.",
                         "Zeichnet 20 eingebaute Funktionsgraphen als Pixelgrafik im LCD."),
            "how": ([
                "Open PLOT and press a function key such as sin x, x^2 or GAUSS.",
                "The graph replaces the LCD temporarily and scales itself automatically.",
                "Press any other key or tap the display to close the graph."
            ], [
                "PLOT oeffnen und eine Funktion wie sin x, x^2 oder GAUSS druecken.",
                "Der Graph ersetzt kurz das LCD und skaliert sich automatisch.",
                "Eine andere Taste druecken oder das Display antippen, um den Graphen zu schliessen."
            ]),
            "notes": (["Asymptotes such as tan x or 1/x are clipped so the plot stays readable."],
                      ["Asymptoten wie tan x oder 1/x werden begrenzt, damit der Plot lesbar bleibt."])
        },
        "form": {
            "overview": ("Formula assistant based on three stored variables A, B and C.",
                         "Formel-Assistent mit drei gespeicherten Variablen A, B und C."),
            "how": ([
                "Enter a number and press SET A, SET B or SET C to store it.",
                "Press INFO to check stored values. CLR ABC resets all variables to 0.",
                "Press a formula key; the result appears on the display and is added to history."
            ], [
                "Zahl eingeben und mit SET A, SET B oder SET C speichern.",
                "INFO zeigt die gespeicherten Werte. CLR ABC setzt alle Variablen auf 0.",
                "Formeltaste druecken; das Ergebnis erscheint im Display und wird in den Verlauf geschrieben."
            ]),
            "notes": (["Formula keys use fixed roles: for example BMI uses A as kg and B as metres; speed uses A as kilometres and B as hours."],
                      ["Die Formeln nutzen feste Rollen: BMI verwendet A als kg und B als Meter; KM/H verwendet A als Kilometer und B als Stunden."])
        }
    }
    item = data[page_id]
    return {
        "overview": item["overview"][1 if de else 0],
        "how": item["how"][1 if de else 0],
        "notes": item["notes"][1 if de else 0],
    }


def detail_box(page_id: str, lang: str, st):
    details = page_detail(page_id, lang)
    rows = [
        [label("overview", lang), details["overview"]],
        [label("how", lang), " ".join(details["how"])],
        [label("notes", lang), " ".join(details["notes"])],
    ]
    return table(rows, st, [34 * mm, CONTENT_W * 0.56])


def keyboard_rows(lang: str):
    if lang == "de":
        return [
            ["0-9", "Zifferneingabe"],
            [", oder .", "Dezimalkomma"],
            ["+ - * /", "Grundrechenarten"],
            ["Enter oder =", "Berechnen"],
            ["Escape", "AC / loeschen"],
            ["%", "Prozent"],
            ["r oder w", "Quadratwurzel"],
            ["Pfeiltasten", "Snake-Steuerung und Geheimcode-Eingabe"],
        ]
    return DATA["keyboard"]


def storage_items(lang: str):
    if lang == "de":
        return ["Theme", "Sound", "Winkelmodus", "Verlauf", "Speicherwert", "Finanzparameter", "Wechselkurs", "Personenzahl", "RPN-Modus", "RPN-Stack", "Formelvariablen", "Highscores", "Virtual-Boy-Freischaltung"]
    return DATA["storage"]


def limitation_text(lang: str):
    if lang == "de":
        return "Der Service Worker wird nur auf HTTPS registriert. Das Inline-Manifest enthaelt Icons nur bei HTTP oder HTTPS. Die Waehrungsumrechnung nutzt einen manuell gespeicherten Kurs und keine Live-API. Zahlensystem-Umrechnungen der PRG-Seite erscheinen in der Statuszeile und ersetzen nicht das Hauptdisplay. Teilen, Zwischenablage, Vibration und Batterieanzeige haengen vom Browser ab. Die App-Oberflaeche selbst ist deutsch."
    return " ".join(DATA["limitations"])


def trouble_text(lang: str):
    if lang == "de":
        return "Wenn nach einem Update noch die alte Version erscheint, App oder Tab komplett schliessen und zweimal neu oeffnen. Wenn kein Ton kommt, einmal in die App tippen und SND ON pruefen. Wenn Teilen nicht verfuegbar ist, Zwischenablage oder Download-Fallback verwenden. Zum kompletten Zuruecksetzen die Websitedaten dieser Domain loeschen."
    return "If an old version appears after update, close and reopen the app twice. If sound does not play, tap once inside the app and check SND ON. If sharing is unavailable, use clipboard copy or browser download fallback. To reset all data, delete website data for this domain."


def build_pdf(lang: str, kind: str, shots: dict[str, Path]):
    s = STR[lang]
    title = s["quick"] if kind == "quick" else s["manual"]
    name = f"CALC-BOY-{safe_name(title)}-{lang}.pdf"
    doc = NumberedDoc(str(PDF_OUT / name), f"{title} ({lang.upper()})", lang)
    st = styles()
    story = []
    toc_items = ["Installation", "PWA / Offline", "Interface", "Pages", "History", "Games", "Themes", "Keyboard", "Storage", "Troubleshooting", "Version"]
    if lang == "de":
        toc_items = ["Installation", "PWA / Offline", "Oberflaeche", "Seiten", "Verlauf", "Spiele", "Themes", "Tastatur", "Speicher", "Fehlerbehebung", "Version"]
    story += [
        Spacer(1, 16 * mm),
        Paragraph("CALC BOY", st["CoverTitle"]),
        Paragraph(p(title), st["CoverTitle"]),
        Spacer(1, 4 * mm),
        img(shots["basic"], CONTENT_W * 0.28, 60 * mm),
        Spacer(1, 5 * mm),
        Paragraph(p(f"Version {DATA['app']['version']} - {s['created']}"), st["Bodyx"]),
        Paragraph(p(s["toc"]), st["H1x"]),
        bullet_list(toc_items, st),
        PageBreak()
    ]
    story += [Paragraph("Introduction" if lang == "en" else "Einleitung", st["H1x"]), Paragraph(p(s["intro"]), st["Bodyx"]), Paragraph(p("Tip: The display is also interactive. Tap it for history; long-press it to copy the current result." if lang == "en" else "Tipp: Das Display ist interaktiv. Tippen oeffnet den Verlauf; langes Druecken kopiert das aktuelle Ergebnis."), st["Boxx"])]
    story += [Paragraph(p(s["install"]), st["H1x"]), bullet_list(s["install_steps"], st), Paragraph(p(s["offline"]), st["H2x"]), Paragraph(p(s["offline_text"]), st["Bodyx"])]
    story += [Paragraph("First calculation" if lang == "en" else "Erste Rechnung", st["H1x"]), KeepTogether([img(shots["basic"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("Example: 12 + 30 = shows 42 and adds the expression to history." if lang == "en" else "Beispiel: 12 + 30 = zeigt 42 und legt die Rechnung im Verlauf ab."), st["Bodyx"])])]
    story += [Paragraph("History, copy and share" if lang == "en" else "Verlauf, Kopieren und Teilen", st["H1x"]), KeepTogether([img(shots["history"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("The last ten successful calculations are saved. The history view also shows sum and average. Text and PNG export are available when the browser supports sharing or clipboard APIs." if lang == "en" else "Die letzten zehn erfolgreichen Rechnungen werden gespeichert. Der Verlauf zeigt auch Summe und Durchschnitt. Text- und PNG-Export nutzen Teilen- oder Zwischenablagefunktionen des Browsers."), st["Bodyx"])])]
    if kind == "quick":
        rows = [[("Page" if lang == "en" else "Seite"), label("overview", lang)]] + [[x["title"], page_detail(x["id"], lang)["overview"]] for x in DATA["pages"]]
        story += [Paragraph("Calculator pages" if lang == "en" else "Rechnerseiten", st["H1x"]), table(rows, st, [28 * mm, CONTENT_W - 28 * mm])]
        story += [Paragraph(p(s["themes"]), st["H1x"]), Paragraph(p(", ".join(DATA["themes"])), st["Bodyx"]), Paragraph(p(s["games"]), st["H1x"]), KeepTogether([img(shots["snake"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("GAME opens the menu. Press 1, 2 or 3 for Math Attack levels, or 5 for Snake." if lang == "en" else "GAME oeffnet das Menue. 1, 2 oder 3 startet Math Attack, 5 startet Snake."), st["Bodyx"])])]
    else:
        for page in DATA["pages"]:
            intro = Table(
                [[img(shots[page["id"]], CONTENT_W * 0.22, 54 * mm), detail_box(page["id"], lang, st)]],
                colWidths=[CONTENT_W * 0.30, CONTENT_W * 0.70]
            )
            intro.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story += [PageBreak(), Paragraph(page["title"], st["H1x"]), intro]
            story += examples_table(page["id"], lang, st)
            story += [Paragraph(p(label("buttons", lang)), st["H2x"]), button_table(page["buttons"], lang, st, page["id"])]
        story += [PageBreak(), Paragraph("Plotting" if lang == "en" else "Graphen", st["H1x"]), KeepTogether([img(shots["plot_sin"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("A plot replaces the LCD with a pixel graph. Press any non-plot key or tap the display to close it." if lang == "en" else "Ein Plot ersetzt das LCD durch einen Pixelgraphen. Jede andere Taste oder ein Tipp auf das Display schliesst ihn."), st["Bodyx"])])]
        story += [PageBreak(), Paragraph(p(s["games"]), st["H1x"]), KeepTogether([img(shots["snake"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("Math Attack asks arithmetic questions for 30 seconds. Snake uses the number pad 2/4/6/8 or arrow keys and stores its own high score." if lang == "en" else "Math Attack stellt 30 Sekunden lang Kopfrechenaufgaben. Snake nutzt 2/4/6/8 oder Pfeiltasten und speichert einen eigenen Highscore."), st["Bodyx"])])]
        story += [Paragraph("Landscape mode" if lang == "en" else "Querformat", st["H1x"]), KeepTogether([img(shots["landscape"], CONTENT_W * 0.50, 70 * mm), Paragraph(p("In landscape, the scientific shortcut column is visible beside BASIC, giving quick access to sin, cos, tan, log, ln, powers, pi and e." if lang == "en" else "Im Querformat erscheint neben BASIC eine Wissenschafts-Spalte mit sin, cos, tan, log, ln, Potenzen, pi und e."), st["Bodyx"])])]
    story += [PageBreak(), Paragraph(p(s["keyboard"]), st["H1x"]), table([[label("key", lang), ("Action" if lang == "en" else "Aktion")]] + keyboard_rows(lang), st, [35 * mm, CONTENT_W - 35 * mm])]
    story += [
        Paragraph(p(s["storage"]), st["H1x"]),
        Paragraph(p(s["storage_text"]), st["Bodyx"]),
        Paragraph(p(", ".join(storage_items(lang)) + "."), st["Bodyx"]),
        Paragraph(p(s["limitations"]), st["H1x"]),
        Paragraph(p(limitation_text(lang)), st["Bodyx"]),
        Paragraph(p(s["trouble"]), st["H1x"]),
        Paragraph(p(trouble_text(lang)), st["Bodyx"]),
    ]
    story += [Paragraph(p(s["version"]), st["H1x"]), Paragraph(p(f"{DATA['app']['name']} {DATA['app']['version']} - {DATA['app']['cache']} - {DATA['app']['license']}"), st["Bodyx"])]
    doc.build(story)
    return PDF_OUT / name


def describe_button(b: str, lang: str, page_id=None) -> str:
    if page_id == "plot":
        plot_desc = {
            "x^2": ("Draws y = x^2.", "Zeichnet y = x^2."),
            "x^3": ("Draws y = x^3.", "Zeichnet y = x^3."),
            "e^x": ("Draws y = e^x.", "Zeichnet y = e^x."),
        }
        if b in plot_desc:
            return plot_desc[b][0 if lang == "en" else 1]
    desc = {
        "AC": ("Clears entry and active operation; in RPN it also clears the stack.", "Loescht Eingabe und laufende Operation; im RPN-Modus auch den Stack."),
        "+/-": ("Changes the sign of the displayed number.", "Wechselt das Vorzeichen der angezeigten Zahl."),
        "%": ("Smart percent. Example: 100 + 10 % becomes 110.", "Smarte Prozentrechnung. Beispiel: 100 + 10 % ergibt 110."),
        "sqrt": ("Calculates the square root; negative values show ERROR.", "Berechnet die Quadratwurzel; negative Werte zeigen ERROR."),
        "/": ("Divides the first value by the second; division by zero shows ERROR.", "Teilt den ersten Wert durch den zweiten; Division durch 0 zeigt ERROR."),
        "*": ("Multiplies two values.", "Multipliziert zwei Werte."),
        "-": ("Subtracts the second value from the first.", "Zieht den zweiten Wert vom ersten ab."),
        "+": ("Adds two values.", "Addiert zwei Werte."),
        ",": ("Adds the decimal separator.", "Fuegt das Dezimalkomma ein."),
        "=": ("Evaluates the current calculation; in RPN it pushes the value to the stack.", "Berechnet die aktuelle Eingabe; in RPN legt = den Wert auf den Stack."),
        "EXT": ("Opens the extended scientific page.", "Oeffnet die erweiterte Wissenschaftsseite."),
        "BASIC": ("Returns to the standard calculator page.", "Kehrt zur Standard-Rechnerseite zurueck."),
        "MEHR": ("Cycles EXT -> CONV -> FIN -> PRG -> PLOT -> FORM.", "Wechselt EXT -> CONV -> FIN -> PRG -> PLOT -> FORM."),
        "MC": ("Clears calculator memory.", "Loescht den Speicherwert."),
        "MR": ("Recalls the saved memory value to the display.", "Ruft den gespeicherten Speicherwert ins Display."),
        "M+": ("Adds the displayed value to memory.", "Addiert den angezeigten Wert zum Speicher."),
        "M-": ("Subtracts the displayed value from memory.", "Zieht den angezeigten Wert vom Speicher ab."),
        "sin": ("Sine of the displayed value, using DEG or RAD mode.", "Sinus des angezeigten Werts im aktiven DEG- oder RAD-Modus."),
        "cos": ("Cosine of the displayed value, using DEG or RAD mode.", "Kosinus des angezeigten Werts im aktiven DEG- oder RAD-Modus."),
        "tan": ("Tangent of the displayed value, using DEG or RAD mode.", "Tangens des angezeigten Werts im aktiven DEG- oder RAD-Modus."),
        "log": ("Base-10 logarithm of the displayed value.", "Zehnerlogarithmus des angezeigten Werts."),
        "ln": ("Natural logarithm of the displayed value.", "Natuerlicher Logarithmus des angezeigten Werts."),
        "DEG/RAD": ("Toggles saved angle mode for trigonometry.", "Schaltet den gespeicherten Winkelmodus fuer Trigonometrie um."),
        "10^x": ("Calculates ten to the power of the displayed value.", "Berechnet zehn hoch angezeigter Wert."),
        "e^x": ("Calculates e to the power of the displayed value.", "Berechnet e hoch angezeigter Wert."),
        "x^2": ("Squares the displayed value.", "Quadriert den angezeigten Wert."),
        "x^3": ("Cubes the displayed value.", "Bildet die dritte Potenz des angezeigten Werts."),
        "x^y": ("Binary power: enter base, press x^y, enter exponent, press =.", "Zweistellige Potenz: Basis eingeben, x^y, Exponent eingeben, =."),
        "cbrt": ("Calculates the cube root.", "Berechnet die Kubikwurzel."),
        "1/x": ("Calculates the reciprocal; 0 shows ERROR.", "Berechnet den Kehrwert; 0 zeigt ERROR."),
        "n!": ("Calculates factorial for whole numbers from 0 to 170.", "Berechnet die Fakultaet fuer ganze Zahlen von 0 bis 170."),
        "pi": ("Inserts pi.", "Fuegt pi ein."),
        "e": ("Inserts Euler's number e.", "Fuegt die Eulersche Zahl e ein."),
        "SET K0": ("Stores start capital for compound interest.", "Speichert das Startkapital fuer Zinseszins."),
        "SET P%": ("Stores yearly interest rate in percent.", "Speichert den Jahreszins in Prozent."),
        "SET JAHRE": ("Stores duration in years.", "Speichert die Laufzeit in Jahren."),
        "SET RATE/M": ("Stores the monthly savings amount.", "Speichert die monatliche Sparrate."),
        "ENDWERT": ("Calculates future value including start capital and monthly payments.", "Berechnet den Endwert inklusive Startkapital und Monatsraten."),
        "ZINSEN": ("Shows only earned interest.", "Zeigt nur den Zinsertrag."),
        "RESET": ("Restores finance defaults.", "Setzt die Finanzwerte auf Standard zurueck."),
        "TIP+10%": ("Adds 10 percent tip to the displayed amount.", "Addiert 10 Prozent Trinkgeld zum angezeigten Betrag."),
        "TIP+15%": ("Adds 15 percent tip to the displayed amount.", "Addiert 15 Prozent Trinkgeld zum angezeigten Betrag."),
        "TIP+20%": ("Adds 20 percent tip to the displayed amount.", "Addiert 20 Prozent Trinkgeld zum angezeigten Betrag."),
        "SET PERS": ("Stores number of people for bill splitting.", "Speichert die Personenzahl zum Teilen einer Rechnung."),
        "/ PERS": ("Divides the displayed amount by the stored number of people.", "Teilt den angezeigten Betrag durch die gespeicherte Personenzahl."),
        "SET KURS": ("Stores the manual exchange rate.", "Speichert den manuellen Wechselkurs."),
        "EUR->$": ("Converts euros to dollars with the stored rate.", "Rechnet Euro mit gespeichertem Kurs in Dollar um."),
        "$->EUR": ("Converts dollars to euros with the stored rate.", "Rechnet Dollar mit gespeichertem Kurs in Euro um."),
        "INFO": ("Shows stored parameters or variables.", "Zeigt gespeicherte Parameter oder Variablen."),
        "->HEX": ("Shows the integer part in hexadecimal in the status line.", "Zeigt den ganzzahligen Anteil hexadezimal in der Statuszeile."),
        "->BIN": ("Shows the integer part in binary in the status line.", "Zeigt den ganzzahligen Anteil binaer in der Statuszeile."),
        "->OCT": ("Shows the integer part in octal in the status line.", "Zeigt den ganzzahligen Anteil oktal in der Statuszeile."),
        "NOT": ("Bitwise NOT of the integer part.", "Bitweises NOT des ganzzahligen Anteils."),
        "AND": ("Bitwise AND for two integer operands.", "Bitweises AND fuer zwei ganzzahlige Operanden."),
        "OR": ("Bitwise OR for two integer operands.", "Bitweises OR fuer zwei ganzzahlige Operanden."),
        "XOR": ("Bitwise XOR for two integer operands.", "Bitweises XOR fuer zwei ganzzahlige Operanden."),
        "MOD": ("Integer remainder; modulo by 0 shows ERROR.", "Ganzzahliger Rest; Modulo durch 0 zeigt ERROR."),
        "<<": ("Shifts the integer part left.", "Verschiebt den ganzzahligen Wert nach links."),
        ">>": ("Shifts the integer part right.", "Verschiebt den ganzzahligen Wert nach rechts."),
        "ABS": ("Absolute value.", "Betrag des Werts."),
        "INT": ("Integer part without decimals.", "Ganzzahliger Anteil ohne Nachkommastellen."),
        "SGN": ("Sign of the number: -1, 0 or 1.", "Vorzeichen der Zahl: -1, 0 oder 1."),
        "ZUFALL": ("Random integer from 1 to 100.", "Zufallszahl von 1 bis 100."),
        "RPN": ("Toggles Reverse Polish Notation mode.", "Schaltet den RPN-Modus um."),
        "SET A": ("Stores the displayed value in variable A.", "Speichert den angezeigten Wert in Variable A."),
        "SET B": ("Stores the displayed value in variable B.", "Speichert den angezeigten Wert in Variable B."),
        "SET C": ("Stores the displayed value in variable C.", "Speichert den angezeigten Wert in Variable C."),
        "% VON": ("Calculates A percent of B.", "Berechnet A Prozent von B."),
        "DREISATZ": ("Calculates B times C divided by A.", "Berechnet B mal C geteilt durch A."),
        "KREIS A": ("Circle area with radius A.", "Kreisflaeche mit Radius A."),
        "KREIS U": ("Circle circumference with radius A.", "Kreisumfang mit Radius A."),
        "PYTH": ("Pythagoras: square root of A^2 + B^2.", "Pythagoras: Wurzel aus A^2 + B^2."),
        "OHM": ("Ohm helper: A times B.", "Ohm-Hilfe: A mal B."),
        "BMI": ("BMI with A as kg and B as metres.", "BMI mit A als kg und B als Meter."),
        "AVG ABC": ("Average of A, B and C.", "Durchschnitt aus A, B und C."),
        "CLR ABC": ("Resets A, B and C to 0.", "Setzt A, B und C auf 0."),
        "KM/H": ("Speed: A kilometres divided by B hours.", "Geschwindigkeit: A Kilometer geteilt durch B Stunden."),
        "NET19": ("Net amount from a gross amount with 19 percent VAT.", "Netto aus Brutto mit 19 Prozent MwSt."),
        "BRU19": ("Gross amount from a net amount with 19 percent VAT.", "Brutto aus Netto mit 19 Prozent MwSt."),
        "km->mi": ("Kilometres to miles.", "Kilometer in Meilen."),
        "mi->km": ("Miles to kilometres.", "Meilen in Kilometer."),
        "m->ft": ("Metres to feet.", "Meter in Fuss."),
        "ft->m": ("Feet to metres.", "Fuss in Meter."),
        "C->F": ("Celsius to Fahrenheit.", "Celsius in Fahrenheit."),
        "F->C": ("Fahrenheit to Celsius.", "Fahrenheit in Celsius."),
        "kg->lb": ("Kilograms to pounds.", "Kilogramm in Pfund."),
        "lb->kg": ("Pounds to kilograms.", "Pfund in Kilogramm."),
        "cm->in": ("Centimetres to inches.", "Zentimeter in Zoll."),
        "in->cm": ("Inches to centimetres.", "Zoll in Zentimeter."),
        "l->gal": ("Litres to US gallons.", "Liter in US-Gallonen."),
        "gal->l": ("US gallons to litres.", "US-Gallonen in Liter."),
        "km/h->mph": ("Kilometres per hour to miles per hour.", "Kilometer pro Stunde in Meilen pro Stunde."),
        "mph->km/h": ("Miles per hour to kilometres per hour.", "Meilen pro Stunde in Kilometer pro Stunde."),
        "h->min": ("Hours to minutes.", "Stunden in Minuten."),
        "min->h": ("Minutes to hours.", "Minuten in Stunden."),
        "MW+19": ("Adds 19 percent German VAT to a net amount.", "Addiert 19 Prozent MwSt. auf einen Nettowert."),
        "MW-19": ("Removes 19 percent German VAT from a gross amount.", "Entfernt 19 Prozent MwSt. aus einem Bruttowert."),
        "MW+7": ("Adds 7 percent German VAT to a net amount.", "Addiert 7 Prozent MwSt. auf einen Nettowert."),
        "MW-7": ("Removes 7 percent German VAT from a gross amount.", "Entfernt 7 Prozent MwSt. aus einem Bruttowert."),
        "sin x": ("Draws y = sin x.", "Zeichnet y = sin x."),
        "cos x": ("Draws y = cos x.", "Zeichnet y = cos x."),
        "tan x": ("Draws y = tan x with clipping near asymptotes.", "Zeichnet y = tan x mit Begrenzung an Asymptoten."),
        "sqrt x": ("Draws y = square root of x.", "Zeichnet y = Wurzel aus x."),
        "log x": ("Draws y = log10 x.", "Zeichnet y = log10 x."),
        "ln x": ("Draws y = ln x.", "Zeichnet y = ln x."),
        "|x|": ("Draws the absolute-value graph.", "Zeichnet den Betragsgraphen."),
        "2^x": ("Draws y = 2^x.", "Zeichnet y = 2^x."),
        "sinh": ("Draws hyperbolic sine.", "Zeichnet den hyperbolischen Sinus."),
        "cosh": ("Draws hyperbolic cosine.", "Zeichnet den hyperbolischen Kosinus."),
        "tanh": ("Draws hyperbolic tangent.", "Zeichnet den hyperbolischen Tangens."),
        "x^4": ("Draws y = x^4.", "Zeichnet y = x^4."),
        "GAUSS": ("Draws the Gaussian bell curve e^(-x^2).", "Zeichnet die Gauss-Glocke e^(-x^2)."),
        "FLOOR": ("Draws the floor step function.", "Zeichnet die Abrundungs-Stufenfunktion."),
        "sinc x": ("Draws sin x / x, with value 1 at x = 0.", "Zeichnet sin x / x, mit Wert 1 bei x = 0."),
        "x*sin x": ("Draws y = x times sin x.", "Zeichnet y = x mal sin x."),
    }
    if b in desc:
        return desc[b][0 if lang == "en" else 1]
    if re.match(r"^-?\d+$", b):
        return "Digit input." if lang == "en" else "Zifferneingabe."
    if "->" in b or "<-" in b or "MW" in b or "km" in b or "mi" in b or "kg" in b or "lb" in b or "gal" in b or "mph" in b or "min" in b:
        return "Converts the displayed value in the direction shown by the key." if lang == "en" else "Rechnet den angezeigten Wert in die auf der Taste angegebene Richtung um."
    if any(x in b for x in ["sin", "cos", "tan", "log", "ln", "^", "sqrt", "n!", "pi", "e"]):
        return "Applies the scientific function to the displayed value." if lang == "en" else "Wendet die wissenschaftliche Funktion auf den angezeigten Wert an."
    return "Runs the function shown on the key." if lang == "en" else "Fuehrt die auf der Taste angezeigte Funktion aus."


def example_rows(page_id: str, lang: str):
    en = lang == "en"
    if en:
        examples = {
            "basic": [("Smart percent", "100 + 10 % = 110; 100 - 10 % = 90"), ("Square root", "144 sqrt -> 12")],
            "ext": [("DEG/RAD", "DEG: 30 sin -> 0.5; RAD: pi sin -> approximately 0"), ("Memory", "42 M+, AC, MR -> 42; 10 M- leaves 32 in memory"), ("Powers", "2 x^y 8 = -> 256")],
            "conv": [("VAT", "100 MW+19 -> 119; 119 MW-19 -> 100"), ("Temperature", "20 C->F -> 68; 68 F->C -> 20"), ("Speed", "100 km/h->mph -> 62.137119224")],
            "fin": [("Compound interest", "SET K0=1000, SET P%=3, SET JAHRE=10, SET RATE/M=50, ENDWERT -> 8336.42449101"), ("Interest only", "With the same values, ZINSEN -> 1336.42449101"), ("Bill split", "SET PERS=4, enter 80, / PERS -> 20"), ("Currency", "SET KURS=1.08, 100 EUR->$ -> 108; 108 $->EUR -> 100")],
            "prg": [("Base display", "255 ->HEX shows FF; ->BIN shows 11111111"), ("Binary operations", "5 AND 3 = 1; 5 OR 2 = 7; 9 MOD 4 = 1"), ("RPN", "RPN on: 12 =, 3 + -> 15; AC clears the stack")],
            "plot": [("Graph", "sin x draws y = sin x; any non-plot key closes it"), ("Compare", "x^2 and x^3 use different automatic scales")],
            "form": [("Percent", "SET A=20, SET B=150, % VON -> 30"), ("Pythagoras", "SET A=3, SET B=4, PYTH -> 5"), ("BMI", "SET A=80, SET B=1.8, BMI -> 24.6913580247"), ("Net/gross", "SET A=119, NET19 -> 100; SET A=100, BRU19 -> 119")],
        }
    else:
        examples = {
            "basic": [("Smarte Prozentrechnung", "100 + 10 % = 110; 100 - 10 % = 90"), ("Quadratwurzel", "144 sqrt -> 12")],
            "ext": [("DEG/RAD", "DEG: 30 sin -> 0,5; RAD: pi sin -> etwa 0"), ("Speicher", "42 M+, AC, MR -> 42; 10 M- laesst 32 im Speicher"), ("Potenzen", "2 x^y 8 = -> 256")],
            "conv": [("Mehrwertsteuer", "100 MW+19 -> 119; 119 MW-19 -> 100"), ("Temperatur", "20 C->F -> 68; 68 F->C -> 20"), ("Geschwindigkeit", "100 km/h->mph -> 62,137119224")],
            "fin": [("Zinseszins", "SET K0=1000, SET P%=3, SET JAHRE=10, SET RATE/M=50, ENDWERT -> 8336,42449101"), ("Nur Zinsen", "Mit denselben Werten: ZINSEN -> 1336,42449101"), ("Rechnung teilen", "SET PERS=4, 80 eingeben, / PERS -> 20"), ("Waehrung", "SET KURS=1,08, 100 EUR->$ -> 108; 108 $->EUR -> 100")],
            "prg": [("Zahlensysteme", "255 ->HEX zeigt FF; ->BIN zeigt 11111111"), ("Bitoperationen", "5 AND 3 = 1; 5 OR 2 = 7; 9 MOD 4 = 1"), ("RPN", "RPN an: 12 =, 3 + -> 15; AC leert den Stack")],
            "plot": [("Graph", "sin x zeichnet y = sin x; jede Nicht-Plot-Taste schliesst ihn"), ("Vergleich", "x^2 und x^3 nutzen jeweils automatische Skalierung")],
            "form": [("Prozent", "SET A=20, SET B=150, % VON -> 30"), ("Pythagoras", "SET A=3, SET B=4, PYTH -> 5"), ("BMI", "SET A=80, SET B=1,8, BMI -> 24,6913580247"), ("Netto/Brutto", "SET A=119, NET19 -> 100; SET A=100, BRU19 -> 119")],
        }
    return examples.get(page_id, [])


def main():
    SRC.mkdir(parents=True, exist_ok=True)
    PDF_OUT.mkdir(parents=True, exist_ok=True)
    shots = create_screenshots()
    for lang in ["de", "en"]:
        for kind in ["quick", "manual"]:
            title = STR[lang]["quick"] if kind == "quick" else STR[lang]["manual"]
            (SRC / f"{safe_name(title)}.{lang}.md").write_text(markdown(lang, kind, shots), encoding="utf-8")
    pdfs = [build_pdf(lang, kind, shots) for lang in ["de", "en"] for kind in ["quick", "manual"]]
    for path in pdfs:
        reader = PdfReader(str(path))
        print(f"{path.name}: {len(reader.pages)} pages")


if __name__ == "__main__":
    main()
