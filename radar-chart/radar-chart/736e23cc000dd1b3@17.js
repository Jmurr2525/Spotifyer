// https://observablehq.com/@palewire/d3-curves-inputs@17
import define1 from "./e93997d5089d7165@2303.js";

function _1(md){return(
md`# d3 curves inputs

A list of all the d3 curve options\``
)}

function _curveSelect(select,curveTypes){return(
select(curveTypes)
)}

function _curveTypes(){return(
[
  "curveBasis",
  "curveBasisClosed",
  "curveBasisOpen",
  "curveBundle",
  "curveCardinal",
  "curveCardinalClosed",
  "curveCardinalOpen",
  "curveCatmullRom",
  "curveCatmullRomClosed",
  "curveCatmullRomOpen",
  "curveLinear",
  "curveLinearClosed",
  "curveMonotoneX",
  "curveMonotoneY",
  "curveNatural",
  "curveStep",
  "curveStepAfter",
  "curveStepBefore",
]
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  main.variable(observer()).define(["md"], _1);
  main.variable(observer("viewof curveSelect")).define("viewof curveSelect", ["select","curveTypes"], _curveSelect);
  main.variable(observer("curveSelect")).define("curveSelect", ["Generators", "viewof curveSelect"], (G, _) => G.input(_));
  main.variable(observer("curveTypes")).define("curveTypes", _curveTypes);
  const child1 = runtime.module(define1);
  main.import("select", child1);
  return main;
}
