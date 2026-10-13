# fr.code_civil_1804

Code civil des Français (1804), first edition: property and prescription, intestate succession, contracts, delicts, sale, loan, deposit — slice for the comparative private-law chain

> Independent demonstration model. It is not an implementation by or
> for an authority and does not establish legal accuracy or completeness.
> For a real case, rely on the official texts and competent bodies.

## Package snapshot

| Item | Value |
|---|---|
| Version | `0.1.0` |
| Namespace | `urn:fr:corpus:clir:code-civil-1804` |
| Dependencies | `doctrine.ius_privatum` |

## Run an example

Install the CLI as described in the [repository README](../../README.md).
From the repository root:

```sh
cd packages/fr.code_civil_1804
law test . --file tests/01-prescription-1804-base.lawtest --json
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

- Hors de la liste d'articles épinglés (SCOPE du script de synchro) : « hors de la chaîne comparative », pas une dette du modèle.
- Le texte est une transcription Wikisource du fac-similé, copie non officielle.
- Les successions de 1804 au-delà de la dévolution entre descendants, de l’enfant naturel en concours avec eux (757 al. 1), du conjoint résiduel (767) et de la réserve 913–914 : fente des lignes, collatéraux, al. 2–3 de 757, enfans adultérins, représentation au-delà du premier degré de petits-enfants.
- Правила заведены у 53 закреплённых фрагментов из 136: остальные закреплены байтами публикации, но исполняемых норм не несут. Отсутствие карточки означает «в модели нормы нет», а не «право молчит».
- 4 выводов пакета остались без исполнимого свидетельства: их посылки содержат дизъюнкцию, текстовое значение или вызов терма, либо голова вычисляемая. Такие выводы записаны в internal и станут карточками вместе со сценариями, написанными руками.
- Сроки считаются термами §86: дело обязано нести политику исчисления (OECD_CODE_CIVIL_1804_PRESCRIPTION), снимок календаря §85 и сам пакет календаря в программе, иначе документ отвечает MISSING_CALENDAR или MISSING_POLICY.
- Деонтических позиций (§§122–140) пакет не объявляет: требования выражены институциональными предикатами, и запрос positions по ним не отвечает.

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
