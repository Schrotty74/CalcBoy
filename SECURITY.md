# 🔒 Security & Privacy

🇩🇪 [Deutsche Version](SECURITY.de.md)

CALC BOY has been audited for private data, external connections and tracking. As of: July 2026, version 3.0.

## Audit result

**No private data is included and none is collected.**

| Check | Result |
|---|---|
| Personal data (names, e-mails, IDs) | ❌ none included |
| Local paths (e.g. `/Users/…`, `C:\…`) | ❌ none included |
| API keys, tokens, passwords | ❌ none included |
| External connections / requests | ❌ none – the font is embedded as Base64 |
| Tracking, analytics, cookies | ❌ not present |
| Data storage | ⚙️ local only (localStorage): theme, sound, calculation history, high scores, memory value, angle mode, finance parameters, exchange rate – never leaves the device, removable via the browser's website data |

## What this means in practice

- The app consists of one HTML file plus a service worker (sw.js) for offline caching – **only same-origin files** are cached. After the first load it works fully offline.
- **Not a single piece of information** leaves the device – no IP transmission to font CDNs, no telemetry, nothing.
- Only settings and the calculation history are stored – **locally in the browser**, without transmission to anyone. To delete: remove the domain's website data in your browser.
- This makes the app **uncritical under GDPR**: no personal data is processed by third parties, nothing leaves the device.

## Permissions

The app requests no permissions. Only these are used optionally:

- **Web Audio API** for the 8-bit key sounds (generated locally, mutable)
- **Vibration API** for haptic feedback, where the device supports it
- **Battery Status API** (where the browser offers it) to color the BATTERY LED – read locally only, never transmitted
- **Clipboard / Web Share API** only on explicit user action (long-press to copy, share button in the history)

## Reporting vulnerabilities

If you spot something nonetheless, please open an [issue](../../issues) in this repository.
