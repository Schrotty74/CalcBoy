# CALC BOY Documentation

This folder contains the maintainable documentation package for CALC BOY.

## Structure

- `data/calcboy_features.json` - shared source for version, pages, buttons, themes, games, keyboard shortcuts, storage and limitations.
- `assets/screenshots/` - generated documentation screenshots and annotated UI images.
- `src/` - editable Markdown sources for German and English quick starts and manuals.
- `output/pdf/` - final A4 PDFs.
- `tools/build_docs.py` - local generator for screenshots, Markdown sources and PDFs.

The application files are not modified by this documentation build.

## Build

Use the bundled Codex Python runtime or any Python environment with `reportlab`, `Pillow` and `pypdf`:

```bash
python3 docs/tools/build_docs.py
```

The generated PDFs are written to `docs/output/pdf/`.
