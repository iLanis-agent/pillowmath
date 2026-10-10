/* Pillow math engine - pure arithmetic, every borrowed number labeled. */
(function (root) {
  "use strict";
  function r1(x) { return Math.round(x * 10) / 10; }
  var SIZES = [40, 45, 50, 55, 60, 65, 70];

  function insertPlan(coverCm) {
    if (!(coverCm > 0)) return { error: "cover size must be positive" };
    var ideal = coverCm + 5;
    for (var i = 0; i < SIZES.length; i++) {
      if (SIZES[i] >= ideal) return { coverCm: coverCm, ideal: ideal, size: SIZES[i], over: false };
    }
    return { coverCm: coverCm, ideal: ideal, size: SIZES[SIZES.length - 1], over: true };
  }

  function fillPlan(sideCm, loftCm) {
    if (!(sideCm > 0) || !(loftCm > 0)) return { error: "side and loft must be positive" };
    var liters = sideCm * sideCm * loftCm / 1000;
    var grams = Math.round(liters * 10);
    return { sideCm: sideCm, loftCm: loftCm, liters: r1(liters), grams: grams };
  }

  function cutPlan(coverCm) {
    if (!(coverCm > 0)) return { error: "cover size must be positive" };
    return { coverCm: coverCm, front: coverCm + 2, backW: r1(coverCm / 2 + 10), backH: coverCm + 2 };
  }

  function renderInsert(r) {
    if (r.over) return "A " + r.coverCm + " cm cover wants a " + r.ideal + " cm insert on the labeled 5 cm plump rule - past the labeled standards, so take a " + r.size + " cm insert.";
    return "A " + r.coverCm + " cm cover wants a " + r.ideal + " cm insert on the labeled 5 cm plump rule - a labeled standard " + r.size + " cm insert fits.";
  }

  function renderFill(r) {
    return "A " + r.sideCm + " cm pillow at " + r.loftCm + " cm loft is " + r.liters + " liters - about " + r.grams + " g of fill at the labeled 10 g a liter.";
  }

  function renderCut(r) {
    return "For a " + r.coverCm + " cm cover cut the front " + r.front + " cm square and two backs " + r.backH + " x " + r.backW + " cm (labeled 1 cm seams, 10 cm envelope overlap).";
  }

  var api = { insertPlan: insertPlan, fillPlan: fillPlan, cutPlan: cutPlan, renderInsert: renderInsert, renderFill: renderFill, renderCut: renderCut };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.PillowMath = api;
})(typeof window !== "undefined" ? window : this);
