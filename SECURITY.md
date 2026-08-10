# Security & Privacy

🇩🇪 [Deutsche Version](SECURITY.de.md)

- **Audit date:** 10 August 2026
- **Audited version:** CALC BOY 3.1.0
- **Method:** Static review of `index.html`, `sw.js`, the security documents and the documentation build. The app was not executed and no network service was accessed during this review.

## Audit result

The audit identified a service worker cache limitation that was fixed on 10 August 2026 and verified with a focused regression test. No open source-backed finding remains for tracking, analytics, embedded credentials, XSS, remote code execution or automatic transmission of calculator data.

| Area | Result |
|---|---|
| Personal data, local paths, API keys, tokens and passwords | Not found in the reviewed source |
| Analytics, cookies and advertising services | Not found |
| Automatic third-party requests | Not found |
| Font loading | Embedded locally as Base64; no font CDN request |
| Calculator data | Stored locally in browser `localStorage` only |
| Service worker cache | Restricted to the four known local application assets; query URLs and other paths are not cached |

## Local data and deliberate sharing

CALC BOY stores its settings and calculator state locally in the browser: theme, sound, calculation history, high scores, memory value, angle mode, finance parameters, exchange rate, RPN stack and formula values. The app has no account, server database or analytics endpoint.

The app does not automatically send calculations or settings to another service. History export and sharing use the browser's clipboard or Web Share feature **only after an explicit user action**. The user chooses the destination in the operating system's share sheet.

The menu includes optional GitHub and Discord links. Opening either link is an explicit navigation to that external service; its normal browser connection and privacy rules then apply.

To remove locally stored calculator data, delete this website's data in the browser.

## Offline cache protection

The service worker precaches the four known application files and now updates only those same-origin, allowlisted URLs. Requests with query strings, unknown paths, non-GET methods or external origins are not handled by the runtime cache. The cache revision changed with this fix, so activation removes the earlier cache version.

A regression test verifies that `index.html` remains cacheable and that query URLs, unknown paths, external URLs and `POST` requests are not cached. This removes the previously identified local-storage availability risk.

## Optional browser APIs

CALC BOY does not request its own permission prompts. Where the browser supports them, it can use these APIs locally:

- **Web Audio API** for optional 8-bit key sounds
- **Vibration API** for optional haptic feedback
- **Battery Status API** to display the local battery indicator
- **Clipboard and Web Share APIs** after an explicit copy or share action

Browser support and permissions are controlled by the browser or operating system.

## Scope and limitations

This is a technical source audit, not legal advice. Hosting headers, browser storage quotas and the deployed GitHub Pages configuration are outside this repository and were not tested. The cache behavior was verified through an isolated service-worker regression test; a full manual browser test was not part of this audit.

## Reporting vulnerabilities

Please report potential vulnerabilities through a private security report where available, or otherwise open an [issue](../../issues) without publishing sensitive proof-of-concept details.
