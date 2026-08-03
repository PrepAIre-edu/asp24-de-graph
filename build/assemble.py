# -*- coding: utf-8 -*-
"""Assemble the four syllabus courses into one extractions.json + unit_index.json."""
import json, sys
from pathlib import Path
K = Path("/sessions/happy-trusting-carson/mnt/MIT/_kse_syllabi")
sys.path.insert(0, str(K/"build"))
sys.path.insert(0, "/sessions/happy-trusting-carson/mnt/MIT/_linear_algebra/build")

import src_calc, src_prob, src_ml, src_links
import extractions_src as src_la          # the Linear Algebra work, reused as-is

LA_REL_OLD = "source/Syllabus_Linear_Algebra.pdf"   # same path here, no rewrite needed

def files_for(rel):
    return [{"rel_path": rel, "asset_kind": "handbook",
             "filename": rel.split("/")[-1]}]

units, extractions = [], []

def add(course, unit_id, module, ordinal, title, concepts, rel):
    units.append({"unit_id": unit_id, "course": course, "module": module,
                  "unit": ordinal, "title": title, "n_files": 1,
                  "chars": 0, "files": files_for(rel)})
    extractions.append({"unit_id": unit_id,
                        "concepts": [dict(c) for c in concepts], "links": []})

for mod, course in ((src_calc, "CALC"), (src_prob, "PROB"), (src_ml, "ML")):
    for uid, (m, o, title, cs) in mod.UNITS.items():
        add(course, uid, m, o, title, cs, mod.REL)

# ---- Linear Algebra: rebuild exactly as in _linear_algebra -------------
la_units = {
 "LA-M1U1": (1,1,"PSS 1. Back to School"), "LA-M1U2": (1,2,"PSS 2. Matrices and row operations"),
 "LA-M1U3": (1,3,"PSS 3. Jordan-Gauss method elimination"), "LA-M2U1": (2,1,"PSS 4. Applications for SLE"),
 "LA-M2U2": (2,2,"PSS 5. Test Preparation (Test 1)"),
 "LA-M2U3": (2,3,"PSS 6. Operations with vectors. The concept of a linear space"),
 "LA-M3U1": (3,1,"PSS 7. Matrix operations: addition, scalar multiplication, transposition"),
 "LA-M3U2": (3,2,"PSS 8. Matrix operations: multiplication"),
 "LA-M4U1": (4,1,"PSS 9. Test preparation (Test 2)"), "LA-M4U2": (4,2,"PSS 10. Finding an inverse matrix"),
 "LA-M5U1": (5,1,"PSS 11. Solving SLE using the inverse matrix"),
 "LA-M5U2": (5,2,"PSS 12. Determinants and their applications"),
 "LA-M6U1": (6,1,"PSS 13. Test preparation (Test 3)"),
 "LA-M6U2": (6,2,"PSS 14. Geometric transformations and matrices"),
 "LA-M7U1": (7,1,"PSS 15. Total recall / course wrap-up"),
}
by_slug = {c["slug"]: c for cs in src_la.UNITS.values() for c in cs}
la_entries = {}
for uid, cs in src_la.UNITS.items():
    m, o, title = la_units[uid]
    add("LA", uid, m, o, title, cs, src_la.REL)
    la_entries[uid] = extractions[-1]
for uid, (quote, slugs) in src_la.REVIEW.items():
    e = la_entries[uid]; have = {c["slug"] for c in e["concepts"]}
    for sl in slugs:
        occ = {"rel_path": src_la.REL, "role": "assessed", "quote": quote, "confidence": 0.85}
        if sl in have:
            next(c for c in e["concepts"] if c["slug"] == sl)["occurrences"].append(occ)
        else:
            s = by_slug[sl]
            e["concepts"].append({**{k: v for k, v in s.items() if k != "occurrences"},
                                  "occurrences": [occ]})

# all links go on the first unit; graph.build folds them globally
extractions[0]["links"] = [{"src": a, "dst": b, "type": t, "strength": w, "rationale": r}
                           for a, b, t, w, r in src_links.L + src_la.LINKS]

(K/"build/unit_index.json").write_text(json.dumps(units, ensure_ascii=False, indent=1), encoding="utf-8")
(K/"build/extractions.json").write_text(json.dumps(extractions, ensure_ascii=False, indent=1), encoding="utf-8")
import collections
print("units:", len(units), dict(collections.Counter(u["course"] for u in units)))
print("concept rows:", sum(len(e["concepts"]) for e in extractions),
      "| distinct:", len({c["slug"] for e in extractions for c in e["concepts"]}),
      "| links:", len(extractions[0]["links"]))
