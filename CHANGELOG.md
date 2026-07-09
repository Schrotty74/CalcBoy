# Changelog

All notable changes to **CALC BOY** are documented here.

The repository currently uses the app header version `v3.0` and service-worker cache `calcboy-v3.0.2`. This changelog keeps the public release line as `v3.0.2 / 1.7` for the current uploaded build.

## v3.0.2 / 1.7

### Added
- Formula Assistant (`FORM`) with percent, rule of three, circle, Pythagoras, Ohm, BMI, average, speed and VAT helper functions.
- RPN mode on the programmer page.
- PNG export for the calculation history.
- Unlockable Virtual Boy theme as seventh console theme.

### Changed
- Finance `INFO` now shows end value, total paid in and interest earned.
- iPhone PWA Safe Area handling keeps `THEME`, `GAME` and `SND` reachable below the iOS status bar.
- LCD result line keeps a fixed height when long results switch to smaller text.

### Fixed
- Prevented display layout shift for long results such as `√2`.
- Improved standalone iPhone PWA layout with status bar overlay enabled.

## v3.0 / 1.6

### Added
- Function plotter page with 20 pixel-style function graphs.
- Programmer page with HEX, BIN, OCT, bitwise operators and shifts.
- Finance page with compound interest, monthly saving rate, tips, bill splitting and manual currency conversion.
- Extended conversion page with common unit conversions and VAT helpers.
- Math Attack and Snake mini games.
- Secret Konami-code unlock for the Virtual Boy theme.

### Changed
- Expanded the single-file PWA structure.
- Improved local storage for settings, history, high scores, memory, angle mode and finance parameters.

## v2.x

### Added
- Scientific functions: trigonometry, logarithms, powers, roots, factorial and constants.
- Memory functions.
- Calculation history with reuse and text export.
- Multiple console themes and theme-specific sounds.

## v1.0

### Added
- Initial CALC BOY release.
- Basic arithmetic calculator.
- Game Boy inspired visual design.
- Offline-capable PWA foundation.
