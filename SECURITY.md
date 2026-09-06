# Security Policy

[Deutsch](SECURITY.de.md)

## Supported Versions

| Version | Supported |
| --- | --- |
| 3.1.x | Yes |
| 3.0.x and earlier | No |

The currently documented release is 3.1.0.

## Security Model

CALC BOY is a local-only PWA with no account, analytics or tracking. Calculator state and settings are stored in browser `localStorage`. The service worker is restricted to known local application assets. Clipboard and Web Share functionality is used only after explicit user action.

## Reporting a Vulnerability

Please report potential vulnerabilities privately through the repository owner where possible. Do not publish sensitive proof-of-concept details in a public issue. Include the CALC BOY version, browser/OS and reproduction steps, with private data removed.

## Scope

Relevant reports include calculator-data storage, service-worker/offline caching, imported or exported history, browser APIs, script injection, unintended network requests and behavior that could expose or alter locally stored data.

Thank you for helping keep CALC BOY safe.
