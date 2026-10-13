# fr.code_civil.liberalites

Code civil — Livre III, titre II : des libéralités (réserve héréditaire, quotité disponible, réunion fictive, imputation et réduction des libéralités excessives)

> Independent demonstration model. It is not an implementation by or
> for an authority and does not establish legal accuracy or completeness.
> For a real case, rely on the official texts and competent bodies.

## Package snapshot

| Item | Value |
|---|---|
| Version | `0.1.0` |
| Namespace | `urn:fr:corpus:clir:code-civil-liberalites` |
| Dependencies | `fr.code_civil.core`, `fr.code_civil.successions` |

## Run an example

Install the CLI as described in the [repository README](../../README.md).
From the repository root:

```sh
cd packages/fr.code_civil.liberalites
law test . --file tests/q01-deux-enfants-quotite-un-tiers.lawtest --json
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
- Правила заведены у 233 закреплённых фрагментов из 233: остальные закреплены байтами публикации, но исполняемых норм не несут. Отсутствие карточки означает «в модели нормы нет», а не «право молчит».
- 1 выводов пакета остались без исполнимого свидетельства: их посылки содержат дизъюнкцию, текстовое значение или вызов терма, либо голова вычисляемая. Такие выводы записаны в internal и станут карточками вместе со сценариями, написанными руками.
- Сроки считаются термами §86: дело обязано нести политику исчисления (CC_LIBERALITES_CALENDRIER), снимок календаря §85 и сам пакет календаря в программе, иначе документ отвечает MISSING_CALENDAR или MISSING_POLICY.

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
