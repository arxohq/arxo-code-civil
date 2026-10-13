![Le Code civil comme modèle exécutable](assets/cover.svg)

# Arxo Code civil

[Français](README.md) · [English](README.en.md)

Explore the French Civil Code through **facts, legal dates, explicit judicial findings and reproducible answers**. This delivery contains 16 contemporary packages and a separate 1804 model. French source labels stay French; English explanations are unofficial.

[Run a question](#run-a-question) · [Choose a model](#choose-a-model) · [Examples](#examples) · [Inspect a proof](#inspect-a-proof) · [Depth and limits](#depth-and-limits)

## Run a question

Requirements: **Node.js 20+** and Git. Published `@arxo/cli@0.2.4` supports macOS arm64 and Linux x64. Models are delivered here through GitHub; there is no model npm package.

```sh
npm install -g @arxo/cli@0.2.4
git clone https://github.com/arxohq/arxo-code-civil.git
cd arxo-code-civil
law eval examples/renegociation-ouverte
```

Expected: `COMPUTED` / `TRUE_ONLY`. The model establishes the opening of renegotiation under article 1195; it does not rewrite the contract or decide the dispute. Compare accepted risk and missing findings:

```sh
law eval examples/risque-accepte
law eval examples/jugement-manquant
```

These return `COMPUTED / NEITHER` and `REQUIRES_JUDGMENT / NEITHER`. Absence of proof, a negative assertion and conflicting assertions remain distinct.

## Choose a model

**`fr.code_civil` is the limitation package, not an aggregate of the whole Code.** Choose the subject package. Version 0.1.0 is retained for every model; the captured modern source cutoff is 16 September 2026. This is not a continuously updated view of French law.

| Paquet / Package | Sujet / Scope | EXECUTABLE | ANCHORED | SOURCE_ONLY | Autres / Other | Unités / Units |
|---|---|---:|---:|---:|---:|---:|
| [`fr.code_civil`](packages/fr.code_civil) | Prescription / limitation | 57 | 0 | 4 | 0 | 61 |
| [`fr.code_civil_1804`](packages/fr.code_civil_1804) | 1804 / historical slice | 53 | 0 | 83 | 939 | 1075 |
| [`fr.code_civil.biens`](packages/fr.code_civil.biens) | Biens / property | 182 | 0 | 19 | 0 | 201 |
| [`fr.code_civil.contrat`](packages/fr.code_civil.contrat) | Contrat / contract | 151 | 0 | 0 | 0 | 151 |
| [`fr.code_civil.contrats_speciaux`](packages/fr.code_civil.contrats_speciaux) | Contrats spéciaux / special contracts | 264 | 0 | 3 | 0 | 267 |
| [`fr.code_civil.core`](packages/fr.code_civil.core) | Titre préliminaire / shared declarations | 8 | 0 | 0 | 0 | 8 |
| [`fr.code_civil.famille`](packages/fr.code_civil.famille) | Famille / family | 52 | 0 | 343 | 0 | 395 |
| [`fr.code_civil.liberalites`](packages/fr.code_civil.liberalites) | Libéralités / gifts and wills | 233 | 0 | 0 | 0 | 233 |
| [`fr.code_civil.mayotte`](packages/fr.code_civil.mayotte) | Mayotte | 18 | 0 | 23 | 0 | 41 |
| [`fr.code_civil.obligations`](packages/fr.code_civil.obligations) | Obligations | 162 | 0 | 0 | 0 | 162 |
| [`fr.code_civil.personnes`](packages/fr.code_civil.personnes) | Personnes / persons | 425 | 0 | 10 | 0 | 435 |
| [`fr.code_civil.regimes_matrimoniaux`](packages/fr.code_civil.regimes_matrimoniaux) | Régimes matrimoniaux / matrimonial property | 100 | 0 | 39 | 0 | 139 |
| [`fr.code_civil.responsabilite`](packages/fr.code_civil.responsabilite) | Responsabilité / liability | 47 | 0 | 1 | 0 | 48 |
| [`fr.code_civil.successions`](packages/fr.code_civil.successions) | Successions / inheritance | 143 | 1 | 123 | 0 | 267 |
| [`fr.code_civil.suretes`](packages/fr.code_civil.suretes) | Sûretés / security | 223 | 0 | 0 | 0 | 223 |
| [`fr.code_civil.transitions`](packages/fr.code_civil.transitions) | Réformes / transition acts | 4 | 0 | 0 | actes / acts | 4 |
| [`fr.code_civil.vente_louage`](packages/fr.code_civil.vente_louage) | Vente et louage / sale and hire | 222 | 0 | 46 | 0 | 268 |
| [`doctrine.ius_privatum`](packages/doctrine.ius_privatum) | Dépendance / dependency | — | — | — | — | not_measured |
| [`calc.allocation`](packages/calc.allocation) | Dépendance / dependency | — | — | — | — | not_measured |
| [`calc.kinship`](packages/calc.kinship) | Dépendance / dependency | — | — | — | — | not_measured |
| [`units.si`](packages/units.si) | Dépendance / dependency | — | — | — | — | not_measured |

![Modèle + faits + date → réponse → preuve](assets/flow.svg)

## Examples

| Exemple / Example | Question | Statut / Status |
|---|---|---|
| [`prescription-1804`](examples/prescription-1804) | Debt from 2000, action in 2015 — 1804 model | `COMPUTED` / `FALSE_ONLY` |
| [`prescription-actuelle`](examples/prescription-actuelle) | Same debt — current rules and 2008 transition | `COMPUTED` / `TRUE_ONLY` |
| [`contrat-veille-2016`](examples/contrat-veille-2016) | 30 September 2016 contract: outside this model | `COMPUTED` / `TRUE_ONLY` |
| [`contrat-jour-2016`](examples/contrat-jour-2016) | 1 October 2016 contract: 2016 wording | `COMPUTED` / `TRUE_ONLY` |
| [`contrat-2019`](examples/contrat-2019) | 2019 contract: ratified wording | `COMPUTED` / `TRUE_ONLY` |
| [`renegociation-ouverte`](examples/renegociation-ouverte) | Article 1195: renegotiation opens | `COMPUTED` / `TRUE_ONLY` |
| [`risque-accepte`](examples/risque-accepte) | Accepted risk: positive conclusion absent | `COMPUTED` / `NEITHER` |
| [`jugement-manquant`](examples/jugement-manquant) | Article 1218: missing judicial findings | `REQUIRES_JUDGMENT` / `NEITHER` |
| [`embargo-temporaire`](examples/embargo-temporaire) | Temporary impediment: performance suspended | `COMPUTED` / `TRUE_ONLY` |
| [`embargo-definitif`](examples/embargo-definitif) | Permanent impediment: contract terminated | `COMPUTED` / `TRUE_ONLY` |
| [`obligation-active`](examples/obligation-active) | Duty during renegotiation: ACTIVE | `COMPUTED` / `POSITIONS: ACTIVE` |
| [`responsabilite-jugement`](examples/responsabilite-jugement) | Fault: judicial finding required | `REQUIRES_JUDGMENT` / `NEITHER` |
| [`reserve-deux-enfants`](examples/reserve-deux-enfants) | Two children: available portion is one third | `COMPUTED` / `TRUE_ONLY` |
| [`legs-reduit`](examples/legs-reduit) | Legacy reduction: €30,000 | `COMPUTED` / `TRUE_ONLY` |
| [`conjoint-quart`](examples/conjoint-quart) | Surviving spouse: one quarter | `COMPUTED` / `TRUE_ONLY` |
| [`veuve-1804`](examples/veuve-1804) | 1804 reading: spouse receives no share | `COMPUTED` / `TRUE_ONLY` |
| [`veuve-actuelle`](examples/veuve-actuelle) | Current reading: spouse receives one quarter | `COMPUTED` / `TRUE_ONLY` |

Each directory contains the original `input.lawcase`, canonical `case.json`, `query.json`, the native evaluation `request.json` and the saved `result.json`. Requests are captured by the published CLI from existing case collections; no Python or JavaScript legal evaluator is added. `origin adjudicated`, explicit negatives and date policies are retained. [Native collections](collections) also allow `law ask`.

```sh
law ask collections/imprevision-force-majeure --case PrixEnHausse \
  --query-json collections/imprevision-force-majeure/queries/renegociation-ouverte.json \
  --format json
```

![Constatations fournies et manquantes](assets/judgment.svg)

## Inspect a proof

```sh
law inspect examples/renegociation-ouverte/result.json summary
```

The answer carries truth/evaluation status, judgment requests, a proof graph and canonical hashes. Follow the graph’s rule identifiers into [contract rules](packages/fr.code_civil.contrat/chapitre-04-s5-inexecution.law) or the [linked contract world](registry/world/fr.code_civil.contrat.lawir.json).

**CLI limitation:** 0.2.4 leaves evaluation `sourceAnchors` empty on these examples. The applied rule and its model `anchors` are checked separately; the native unfold below resolves article references. Do not interpret an empty array as absence of a source. [Verification](reports/verification.json).

<details>
<summary>Article 1195 — native unfold, depth 2</summary>

![Native unfold of renegociation_ouverte](assets/unfold-renegociation.svg)

[Native document](assets/unfold-renegociation.json).

```sh
law engine unfold registry/world/fr.code_civil.contrat.lawir.json \
  renegociation_ouverte --clir registry/package --depth 2 --lang fr --json
```

</details>

## Depth and limits

The table reports the **current pinned article edition** for modern Code packages. Its combined denominator is **2,899 articles**. Transition acts use a separate four-unit denominator. The 1804 captured text uses its own 1,075-unit denominator: 939 units are outside the model’s anchored scope. Older modern wordings are separate rows in the [per-unit report](reports/formalization-depth.json), never added to the contemporary denominator.

`EXECUTABLE` records a deriving or checking node anchored in the article. It does not establish complete formalization of every paragraph or legal consequence. `ANCHORED` and `SOURCE_ONLY` remain visible; calculation/declaration dependencies have no measured legal-article denominator. Measurement uses the existing `boundaries.depth`, own-package nodes only, with input and implementation hashes.

A pre-reform contract outside a package is **a model boundary, not absence of law**. The 1804 model is a historical slice, not an exhaustive historical Code. The engine does not invent court findings, partition an estate, select a remedy or supply all external statutes/procedures. Normative positions and institutional propositions are different result kinds. Read each [package’s limitations](packages).

## Reproduce selected checks

```sh
law test packages/fr.code_civil.core --file tests/titre-preliminaire.lawtest --json
# Optional maintainer checks / vérification facultative : Python 3.12+
python3.12 tools/check.py
```

Local evidence: 89 scenarios from selected declared files, plus one allocation fixture and its property; 17 reader examples. The allocation package’s historical test declaration lacks `world`: its native package-test refusal is retained, and a direct fixture check is reported separately. `units.si` declares no suite. No complete package suite or full corpus acceptance is claimed. `releaseVerified: false`; corpus `not_checked`. [Delivery](docs/DELIVERY.md) · [Source pin](source-pin.json) · [Runtime pin](toolchain.lock.json) · [Exact inventory](CANON-MANIFEST.json).

## Sources and licence

Model code and examples: [Apache-2.0](LICENSE). Captured LEGI texts: DILA, [Licence Ouverte 2.0](https://www.data.gouv.fr/pages/legal/licences/etalab-2.0), source cutoff 2026-09-16. Historical transcription: Wikisource, with attribution and share-alike terms retained separately. [NOTICE](NOTICE) lists publication URLs, retrieval dates and hashes. Independent research demonstration, not affiliated with DILA or the French State.
