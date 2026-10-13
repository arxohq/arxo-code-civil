# fr.code_civil.vente_louage

Code civil — Livre III, titres VI à VIII bis : vente, échange, louage et promotion immobilière

> Independent demonstration model. It is not an implementation by or
> for an authority and does not establish legal accuracy or completeness.
> For a real case, rely on the official texts and competent bodies.

## Package snapshot

| Item | Value |
|---|---|
| Version | `0.1.0` |
| Namespace | `urn:fr:corpus:clir:code-civil-vente-louage` |
| Dependencies | `fr.code_civil.core` |

## Run an example

Install the CLI as described in the [repository README](../../README.md).
From the repository root:

```sh
cd packages/fr.code_civil.vente_louage
law test . --file tests/vente-garanties.lawtest --json
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

- Les articles déclarés SOURCE_ONLY dans sources/*/articles.json n'ont pas de tête exécutable. Les appréciations déléguées au juge passent par le canal externe §47.3 et ne sont pas déduites d'un dossier vide.
- Правила заведены у 226 закреплённых фрагментов из 268: остальные закреплены байтами публикации, но исполняемых норм не несут. Отсутствие карточки означает «в модели нормы нет», а не «право молчит».
- Сроки считаются термами §86: дело обязано нести политику исчисления (CC_VENTE_LOUAGE_AN), снимок календаря §85 и сам пакет календаря в программе, иначе документ отвечает MISSING_CALENDAR или MISSING_POLICY.

| Inspect | What it contains |
|---|---|
| [law.toml](law.toml) | Package identity, dependencies and declared scenario groups |
| [tests/](tests/) | Declared scenarios and their fixtures |
| [sources/](sources/) | Captured source material; individual reproduction terms apply |
| [sources.law](sources.law) | Model declarations and source references |

## Reproduction and rights

See the [repository instructions](../../README.md) for rebuilding
a source package and restoring any withheld sources. The [repository licence](../../LICENSE)
covers the model code; captured publisher texts keep their own terms in
[NOTICE](../../NOTICE) and [package-info.json](package-info.json).
