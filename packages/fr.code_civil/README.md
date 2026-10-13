# fr.code_civil

Code civil — prescription extinctive: Titre XX actuel, anciennes règles nécessaires et transition de la loi n° 2008-561

> Independent demonstration model. It is not an implementation by or
> for an authority and does not establish legal accuracy or completeness.
> For a real case, rely on the official texts and competent bodies.

## Package snapshot

| Item | Value |
|---|---|
| Version | `0.1.0` |
| Namespace | `urn:fr:corpus:clir:code-civil` |
| Dependencies | `doctrine.ius_privatum` |

## Run an example

Install the CLI as described in the [repository README](../../README.md).
From the repository root:

```sh
cd packages/fr.code_civil
law test . --file tests/01-transition-2008.lawtest --json
```

Success checks the declared expectations of the model; it does not certify
that the model covers the whole subject or every possible case.

## Scope and inputs

The executable scope is defined by the rules and declared scenarios in this
snapshot. Each rule has its own dates, prerequisites and source anchors.
Use the supplied facts and any explicitly selected readings of the scenario;
do not infer wider coverage from the subject named above.

The package author records these limitations (retained from
[package-info.json](package-info.json)):

- La date à laquelle le titulaire aurait dû connaître les faits nécessaires au sens de l'article 2224 n'est pas déduite mécaniquement : le juge la fixe par le canal externe titulaire_aurait_du_connaitre_les_faits_le.
- Le cas exécutable de suspension couvre seulement une suspension qui commence au point de départ applicable et se termine à la date de reprise ; le reliquat d'une suspension survenue en cours de délai reste hors de cette démonstration.
- Quatre articles restent SOURCE_ONLY avec une raison nominative dans sources/fr-code-civil/articles.json : 2223 (renvoi aux lois spéciales hors du titre), 2255 et 2258 (définitions de la possession et de la prescription acquisitive), 2259 (renvoi d'application au titre XX). Les délais particuliers du titre (2225 à 2227) et le délai butoir de vingt ans (2232) sont exécutés.
- Certains alinéas restent sans date d'effet calculée : 2222 alinéa 2 (forme générale de la réduction de durée, exécutée seulement pour 2008), 2238 et 2239 alinéa 1 (point de départ de la suspension), 2245 alinéas 2 et 3 (héritiers d'un débiteur solidaire, obligation divisible), 2254 alinéa 2 (causes conventionnelles de suspension ou d'interruption), 2277 alinéa 2 (revendication du bailleur).
- Le module de l'article 2254 alinéa 1 (durée convenue en mois, quatre règles, dossiers p35 à p38) ne peut pas s'exécuter sous law.core/0.2.4 : le littéral entier du cas est refusé à l'admission des deux évaluateurs (STD_TYPE_UNAVAILABLE ; contre-épreuve ae/gratuity avec le littéral 0 : même refus). Limite moteur, pas défaut des normes : aucun contournement par les règles (décision phase 2 : signalé, non masqué).

| Inspect | What it contains |
|---|---|
| [law.toml](law.toml) | Package identity, dependencies and declared scenario groups |
| [tests/](tests/) | Declared scenarios and their fixtures |
| [sources/](sources/) | Captured source material; individual reproduction terms apply |
| [01-sources.law](01-sources.law) | Model declarations and source references |

## Reproduction and rights

See the [repository instructions](../../README.md) for rebuilding
a source package and restoring any withheld sources. The [repository licence](../../LICENSE)
covers the model code; captured publisher texts keep their own terms in
[NOTICE](../../NOTICE) and [package-info.json](package-info.json).
