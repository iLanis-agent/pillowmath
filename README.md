# Pillow math

Which insert actually plumps the cover, how much fill the loft takes, and the cut list for an envelope cover. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/pillowmath/

## The three tools

- **Insert pick** - `insertPlan(coverCm)`: labeled 5 cm plump rule, snapped up to labeled standard sizes (40-70 cm).
- **Fill plan** - `fillPlan(sideCm, loftCm)`: side x side x loft becomes liters, then grams at a labeled 10 g a liter.
- **Cut list** - `cutPlan(coverCm)`: front square and two envelope backs with labeled 1 cm seams and a 10 cm overlap.

## Labeled norms (illustrative references, not rules)

- Plump rule: insert about 5 cm bigger than the cover. Standard sizes: 40, 45, 50, 55, 60, 65, 70 cm.
- Fill density: about 10 g a liter for hollowfiber-style fill.
- Sewing allowance: 1 cm seams, 10 cm envelope overlap.

Down and feather blends compress differently than hollowfiber.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (35 cases, 105 checks)

Regenerate the oracle expectations: `python3 oracle.py`
