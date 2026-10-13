# Delivery and provenance / Livraison et provenance

This is a selected consumer export, not a copy of corpus Git history. `source-pin.json` captures the exact originating revision and working-tree byte hashes: the snapshot is identified by those hashes, not by assuming the source branch was clean. Original own-package CLIR is under `registry/original`; fresh CLI 0.2.4 lowering is under `registry/package`; linked import closures are under `registry/world`. The executable .law and .lawcase bytes were not rewritten. Public README/metadata transformations are recorded separately.

Native case requests were captured by `law ask` from retained fictional case collections. Model semantics, arithmetic and editorial selection are not reproduced in Python. `law eval` consumes the complete captured request. External judgments retain `origin adjudicated`; omitted judgments remain omitted. `NEITHER`, explicit negative assertions, conflicts, normative positions and evaluation status remain distinct.

The source cutoff for the modern Code is 2026-09-16. The 2,899-article denominator belongs only to that pinned edition. Transition acts, old modern wordings and the historical transcription have separate denominators. `reports/formalization-depth.json` pins own-package CLIR, source/declaration hashes and the existing boundaries.depth implementation. Its applicability helper was captured from an earlier measurement because the corpus runtime lock is unpublished: this recorded import-only override is not acceptance of a corpus runtime. Technical dependency denominators are not_measured.

Two observed limitations remain open. Published CLI 0.2.4 omits propagated evaluation sourceAnchors on these cases; proof rule IDs and model anchors are retained, and native unfold resolves the article text. The legacy calc.allocation test declaration lacks explicit world; the native refusal remains recorded, while the unchanged first fixture and property pass with its explicit linked program. No failed expectation was changed to obtain a green report.

Local scoped evidence is 89 declared scenarios plus one direct allocation fixture/property, and 17 reader examples. This does not establish complete execution of all declared package suites or formalization of all legal effects. `releaseVerified: false`, corpus `not_checked`. Source-only units, external statutes, administrative procedures, human findings and historical gaps remain boundaries. All model versions remain 0.1.0.

The exact publication exporter is reused as `tools/canon_publication.py`. To rebuild a consumer artifact into a new directory:

```sh
python3.12 tools/canon_publication.py export --source . --config publication.toml --out /tmp/arxo-code-civil-artifact
python3.12 tools/canon_publication.py verify --artifact /tmp/arxo-code-civil-artifact
```

Runtime installation uses the published npm CLI, independently of model delivery. The unpublished corpus runtime pin is not used or claimed as checked. No model npm package, new MCP deployment, website, SDK release or public central catalog change is part of this delivery. Caches, .law directories, node_modules, private authoring reports and machine paths are outside the exact allowlist.
