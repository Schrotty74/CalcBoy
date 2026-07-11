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
    if kind == "quick":
        sections = ["basic", "ext", "conv", "fin", "prg", "plot", "form"]
        lines += ["## Interface overview", "", "Use EXT to leave BASIC, MEHR to cycle through the extra pages, and BASIC to return." if lang == "en" else "Mit EXT verlassen Sie BASIC, mit MEHR wechseln Sie durch die Zusatzseiten, mit BASIC kehren Sie zurück.", ""]
        for pid in sections:
            page = next(x for x in DATA["pages"] if x["id"] == pid)
            lines += [f"### {page['title']}", "", ", ".join(page["buttons"]), ""]
        lines += [f"## {s['games']}", "", "Math Attack uses GAME then 1/2/3. Snake uses GAME then 5." if lang == "en" else "Math Attack startet über GAME und 1/2/3. Snake startet über GAME und 5.", "", f"## {s['keyboard']}", ""]
    else:
        for page in DATA["pages"]:
            lines += [f"## {page['title']}", "", f"![{page['title']}](../assets/screenshots/{page['id']}.png)", "", "Buttons: " + ", ".join(page["buttons"]), ""]
        lines += [f"## {s['games']}", "", "![Snake](../assets/screenshots/snake.png)", ""]
    for key, desc in DATA["keyboard"]:
        lines.append(f"- `{key}` - {desc}")
    lines += ["", f"## {s['storage']}", "", s["storage_text"], "", ", ".join(DATA["storage"]), "", f"## {s['limitations']}", ""]
    for item in DATA["limitations"]:
        lines.append(f"- {item}")
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


def button_table(buttons, lang, st):
    items = [[b, describe_button(b, lang)] for b in buttons]
    half = math.ceil(len(items) / 2)
    rows = [["Key", "Function", "Key", "Function"]]
    for i in range(half):
        left = items[i]
        right = items[i + half] if i + half < len(items) else ["", ""]
        rows.append(left + right)
    return compact_table(rows, st, [18 * mm, 60 * mm, 18 * mm, CONTENT_W - 96 * mm])


def examples_table(page_id: str, lang: str, st):
    en = lang == "en"
    examples = example_rows(page_id, lang)
    rows = [["Example", "Steps"]] + examples
    return [
        Paragraph("Examples" if en else "Beispiele", st["H2x"]),
        compact_table(rows, st, [28 * mm, CONTENT_W * 0.46])
    ]


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
        rows = [["Page", "What it is used for"]] + [[x["title"], ", ".join(x["buttons"][:8]) + "..."] for x in DATA["pages"]]
        story += [Paragraph("Calculator pages" if lang == "en" else "Rechnerseiten", st["H1x"]), table(rows, st, [35 * mm, CONTENT_W - 35 * mm])]
        story += [Paragraph(p(s["themes"]), st["H1x"]), Paragraph(p(", ".join(DATA["themes"])), st["Bodyx"]), Paragraph(p(s["games"]), st["H1x"]), KeepTogether([img(shots["snake"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("GAME opens the menu. Press 1, 2 or 3 for Math Attack levels, or 5 for Snake." if lang == "en" else "GAME oeffnet das Menue. 1, 2 oder 3 startet Math Attack, 5 startet Snake."), st["Bodyx"])])]
    else:
        for page in DATA["pages"]:
            intro = Table(
                [[img(shots[page["id"]], CONTENT_W * 0.24, 58 * mm), examples_table(page["id"], lang, st)]],
                colWidths=[CONTENT_W * 0.32, CONTENT_W * 0.68]
            )
            intro.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story += [PageBreak(), Paragraph(page["title"], st["H1x"]), intro]
            story += [Paragraph(p("Buttons"), st["H2x"]), button_table(page["buttons"], lang, st)]
        story += [PageBreak(), Paragraph("Plotting" if lang == "en" else "Graphen", st["H1x"]), KeepTogether([img(shots["plot_sin"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("A plot replaces the LCD with a pixel graph. Press any non-plot key or tap the display to close it." if lang == "en" else "Ein Plot ersetzt das LCD durch einen Pixelgraphen. Jede andere Taste oder ein Tipp auf das Display schliesst ihn."), st["Bodyx"])])]
        story += [PageBreak(), Paragraph(p(s["games"]), st["H1x"]), KeepTogether([img(shots["snake"], CONTENT_W * 0.38, 83 * mm), Paragraph(p("Math Attack asks arithmetic questions for 30 seconds. Snake uses the number pad 2/4/6/8 or arrow keys and stores its own high score." if lang == "en" else "Math Attack stellt 30 Sekunden lang Kopfrechenaufgaben. Snake nutzt 2/4/6/8 oder Pfeiltasten und speichert einen eigenen Highscore."), st["Bodyx"])])]
        story += [Paragraph("Landscape mode" if lang == "en" else "Querformat", st["H1x"]), KeepTogether([img(shots["landscape"], CONTENT_W * 0.50, 70 * mm), Paragraph(p("In landscape, the scientific shortcut column is visible beside BASIC, giving quick access to sin, cos, tan, log, ln, powers, pi and e." if lang == "en" else "Im Querformat erscheint neben BASIC eine Wissenschafts-Spalte mit sin, cos, tan, log, ln, Potenzen, pi und e."), st["Bodyx"])])]
    story += [PageBreak(), Paragraph(p(s["keyboard"]), st["H1x"]), table([["Key", "Action"]] + DATA["keyboard"], st, [35 * mm, CONTENT_W - 35 * mm])]
    trouble_items = ["If an old version appears after update, close and reopen the app twice.", "If sound does not play, tap once inside the app and check SND ON.", "If sharing is unavailable, use clipboard copy or browser download fallback.", "To reset all data, delete website data for this domain."]
    story += [
        Paragraph(p(s["storage"]), st["H1x"]),
        Paragraph(p(s["storage_text"]), st["Bodyx"]),
        Paragraph(p(", ".join(DATA["storage"]) + "."), st["Bodyx"]),
        Paragraph(p(s["limitations"]), st["H1x"]),
        Paragraph(p(" ".join(DATA["limitations"])), st["Bodyx"]),
        Paragraph(p(s["trouble"]), st["H1x"]),
        Paragraph(p(" ".join(trouble_items)), st["Bodyx"]),
    ]
    story += [Paragraph(p(s["version"]), st["H1x"]), Paragraph(p(f"{DATA['app']['name']} {DATA['app']['version']} - {DATA['app']['cache']} - {DATA['app']['license']}"), st["Bodyx"])]
    doc.build(story)
    return PDF_OUT / name


def describe_button(b: str, lang: str) -> str:
    desc = {
        "AC": ("Clears entry and active operation; in RPN it also clears the stack.", "Loescht Eingabe und laufende Operation; in RPN auch den Stack."),
        "%": ("Smart percent: with + or - it means percent of the first operand.", "Smarte Prozentlogik: bei + oder - Prozent vom ersten Operanden."),
        "DEG/RAD": ("Toggles saved angle mode for trigonometry.", "Schaltet den gespeicherten Winkelmodus fuer Trigonometrie um."),
        "MEHR": ("Cycles EXT -> CONV -> FIN -> PRG -> PLOT -> FORM.", "Wechselt EXT -> CONV -> FIN -> PRG -> PLOT -> FORM."),
        "RPN": ("Toggles Reverse Polish Notation mode.", "Schaltet den RPN-Modus um."),
        "INFO": ("Shows stored parameters or variables.", "Zeigt gespeicherte Parameter oder Variablen."),
        "RESET": ("Restores finance defaults.", "Setzt Finanzwerte auf Standard zurueck.")
    }
    if b in desc:
        return desc[b][0 if lang == "en" else 1]
    if b.startswith("SET"):
        return "Stores the displayed value for this parameter." if lang == "en" else "Speichert den angezeigten Wert fuer diesen Parameter."
    if b in ["BASIC", "EXT"]:
        return "Navigates to this calculator page." if lang == "en" else "Wechselt zu dieser Rechnerseite."
    if any(x in b for x in ["sin", "cos", "tan", "log", "ln", "^", "sqrt", "n!", "pi", "e"]):
        return "Applies the scientific function to the displayed value." if lang == "en" else "Wendet die wissenschaftliche Funktion auf den angezeigten Wert an."
    return "Runs the operation shown on the key." if lang == "en" else "Fuehrt die auf der Taste angezeigte Funktion aus."


def example_rows(page_id: str, lang: str):
    en = lang == "en"
    examples = {
        "basic": [("Smart percent", "100 + 10 % = 110" if en else "100 + 10 % = 110")],
        "ext": [("DEG/RAD", "DEG: 30 sin = 0.5" if en else "DEG: 30 sin = 0,5"), ("Memory", "42 M+ stores 42; MR recalls it." if en else "42 M+ speichert 42; MR ruft es ab.")],
        "conv": [("VAT", "100 MW+19 = 119; 119 MW-19 = 100" if en else "100 MW+19 = 119; 119 MW-19 = 100")],
        "fin": [("Compound interest", "K0 1000, P 3, years 10, rate 50 -> ENDWERT." if en else "K0 1000, P 3, Jahre 10, Rate 50 -> ENDWERT."), ("Bill split", "Set persons to 4, enter 80, press / PERS -> 20." if en else "Personen auf 4 setzen, 80 eingeben, / PERS -> 20.")],
        "prg": [("Binary operations", "5 AND 3 = 1; 5 OR 2 = 7." if en else "5 AND 3 = 1; 5 OR 2 = 7."), ("RPN", "Enter 12 =, enter 3, press + -> 15." if en else "12 = eingeben, 3 eingeben, + druecken -> 15.")],
        "plot": [("Graph", "Press sin x to draw y = sin x." if en else "sin x zeichnet y = sin x.")],
        "form": [("Formula assistant", "SET A=20, SET B=150, % VON -> 30." if en else "SET A=20, SET B=150, % VON -> 30.")]
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
