---
name: gemma-archimate-model-ingest
description: INGEST-uitbreiding voor gemma-archimate-model — brontype vastleggen, bronnen selecteren, een bronanalyse schrijven (wat de bron betekent voor de architectuur) en de kernpunten met de redacteur bespreken. Gebruik binnen gemma-archimate-model-update, na wiki-ingest.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "wiki-ingest"
  requires-tools: "llmwiki"
  reads: "source"
  writes: "bronanalyse"
---

# INGEST-uitbreiding: bronanalyse

## 1. Bron opnemen (laag 1 en 2)

Volg `wiki-ingest`. Voor deze wiki is `--brontype` verplicht:

| Brontype | Voorbeelden |
|---|---|
| `wet` | wetten.overheid.nl, lokale verordeningen en regelingen |
| `informatiemodel` | GGM, RSGB, RGBZ, catalogi van basisregistraties, ZTC, MIM-modellen |
| `beleid` | beleidsnota's, raadsvoorstellen, VNG-handreikingen |
| `overig` | websites, presentaties, overige documenten |

Het GGM en het GEMMA-model komen niet via deze stap binnen, maar via de release-skills.

Een bron wordt letterlijk bewaard: ophalen met `llmwiki source add --url` (nooit een samenvatting of
WebFetch-weergave als bron), nooit vertalen of herschrijven. Pdf's vergen eenmalig `uv sync --extra pdf`.

## 2. Bronselectie (kwaliteit bespreken)

- NOOIT een bron afwijzen omdat die van een andere gemeente dan de eigen komt; bronnen uit meerdere
  gemeenten leveren elementen op die voor alle gemeenten bruikbaar zijn.
- Beoordeel een bron ALLEEN op inhoudelijke relevantie: noemt ze begrippen die elementen van dit model kunnen zijn?
- NOOIT een bron afwijzen omdat ze niet beschrijft wat gemeenten registreren. Ook strategie- en
  governancedocumenten noemen concrete objecten, rollen en processen.
- Een bron zonder bruikbare begrippen krijgt toch een bronanalyse, met `relevant: nee` en een reden;
  het bestand in `sources/` blijft ongemoeid.

## 3. Kernpunten bespreken ([PR3])

Lees de bron en bespreek met de redacteur, vóór je schrijft: hoe rijk is de bron, welke begrippen,
relaties en specialisaties springen eruit, en wat is de rol van de bron in de bronvoorrang (is het de
formele grondslag, of levert ze de gangbare taal?). Dit is signaleren, nog geen beoordeling.

## 4. Bronanalyse schrijven

Pad `bronanalyses/<onderwerp>/<bron-id>.md` (schema `schemas/bronanalyse.schema.json`):

```markdown
---
id: <bron-id>
type: bronanalyse
onderwerp: <onderwerp-id>
bronnen: [<bron-id>]
relevant: ja
bijgewerkt: <datum>
---

# <titel van de bron>

## Samenvatting
Wat deze bron betekent voor de architectuur van dit onderwerp (max. 500 woorden; herhaal de intake niet).

## Kernbegrippen
| Begrip | Omschrijving in de bron | Vindplaats |
|---|---|---|

## Relevantie voor de architectuur
Welke objecten, rollen, processen, diensten of gebeurtenissen; welke relaties en specialisaties.

## Citaten
> Letterlijke tekst die een begrip definieert. (vindplaats: art./§/pagina)
```

Links naar elementpagina's voeg je toe zodra die bestaan. Citaten zijn platte tekst, zonder links.

## 5. Begrippenlijst

Zet de bron-id in `bronnen:` van `begrippen/<onderwerp>.md`. Bestaat die pagina nog niet, maak haar dan
(schema `schemas/onderwerp.schema.json`) met `status: in-behandeling` en de secties `## Omschrijving`,
`## Begrippen` (tabel `| Begrip | Uitkomst | Reden | Herkomst | GGM |`) en `## Open vragen`.
Een onderwerp wordt altijd afgesloten (`status: afgerond` + `conclusie`), ook als er geen elementen uit voortkomen.
