#!/usr/bin/env python3
"""Oracle mirror of engine.js for Pillow math. Writes expected.json (with trailing newline)."""
import json, math

def r1(x): return math.floor(x * 10 + 0.5) / 10

def jsnum(x):
    if isinstance(x, float) and x == int(x) and abs(x) < 1e15:
        return int(x)
    return x

def fmt(x):
    if isinstance(x, float) and x == int(x):
        return str(int(x))
    return repr(x) if isinstance(x, float) else str(x)

SIZES = [40, 45, 50, 55, 60, 65, 70]

def insertPlan(coverCm):
    if not (coverCm > 0):
        return {"error": "cover size must be positive"}
    ideal = coverCm + 5
    for s in SIZES:
        if s >= ideal:
            return {"coverCm": jsnum(float(coverCm)), "ideal": jsnum(float(ideal)), "size": s, "over": False}
    return {"coverCm": jsnum(float(coverCm)), "ideal": jsnum(float(ideal)), "size": SIZES[-1], "over": True}

def fillPlan(sideCm, loftCm):
    if not (sideCm > 0) or not (loftCm > 0):
        return {"error": "side and loft must be positive"}
    liters = sideCm * sideCm * loftCm / 1000
    grams = math.floor(liters * 10 + 0.5)
    return {"sideCm": jsnum(float(sideCm)), "loftCm": jsnum(float(loftCm)), "liters": jsnum(r1(liters)), "grams": grams}

def cutPlan(coverCm):
    if not (coverCm > 0):
        return {"error": "cover size must be positive"}
    return {"coverCm": jsnum(float(coverCm)), "front": jsnum(float(coverCm) + 2),
            "backW": jsnum(r1(coverCm / 2 + 10)), "backH": jsnum(float(coverCm) + 2)}

def renderInsert(r):
    if r["over"]:
        return ("A " + fmt(r["coverCm"]) + " cm cover wants a " + fmt(r["ideal"]) + " cm insert on the labeled 5 cm plump rule - past the labeled standards, so take a " + str(r["size"]) + " cm insert.")
    return ("A " + fmt(r["coverCm"]) + " cm cover wants a " + fmt(r["ideal"]) + " cm insert on the labeled 5 cm plump rule - a labeled standard " + str(r["size"]) + " cm insert fits.")

def renderFill(r):
    return ("A " + fmt(r["sideCm"]) + " cm pillow at " + fmt(r["loftCm"]) + " cm loft is " + fmt(r["liters"]) +
            " liters - about " + str(r["grams"]) + " g of fill at the labeled 10 g a liter.")

def renderCut(r):
    return ("For a " + fmt(r["coverCm"]) + " cm cover cut the front " + fmt(r["front"]) + " cm square and two backs " +
            fmt(r["backH"]) + " x " + fmt(r["backW"]) + " cm (labeled 1 cm seams, 10 cm envelope overlap).")

CASES = []
def add(fn, args): CASES.append({"fn": fn, "args": args})

for a in [(45,), (38,), (50,), (35,), (40,), (55,), (60,), (68,), (30,), (42.5,), (0,), (-45,)]:
    add("insertPlan", list(a))
for a in [(45, 15), (50, 18), (40, 12), (60, 20), (35, 10), (55, 16), (30, 8), (48, 14), (0, 15), (45, 0), (45, -5)]:
    add("fillPlan", list(a))
for a in [(45,), (50,), (40,), (60,), (35,), (55,), (30,), (65,), (42,), (0,), (-45,), (48,)]:
    add("cutPlan", list(a))

out = []
for c in CASES:
    fn = {"insertPlan": insertPlan, "fillPlan": fillPlan, "cutPlan": cutPlan}[c["fn"]]
    res = fn(*c["args"])
    is_err = "error" in res
    if is_err:
        render = res["error"]
    else:
        render = {"insertPlan": renderInsert, "fillPlan": renderFill, "cutPlan": renderCut}[c["fn"]](res)
    out.append({"fn": c["fn"], "args": c["args"], "result": res, "render": render, "isError": is_err})

with open("expected.json", "w") as f:
    f.write(json.dumps(out, separators=(",", ":")) + "\n")
print("wrote", len(out), "cases")
