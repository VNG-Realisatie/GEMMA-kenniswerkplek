---
name: gemma-archimate-model-ingest
description: Bronnen voor gemma-archimate-model — brontype vastleggen, bronnen selecteren, een bronanalyse schrijven (wat de bron betekent voor de architectuur) en de kernpunten met de redacteur bespreken. Gebruik binnen gemma-archimate-model-update, stap 2.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "wiki-ingest"
  requires-tools: "llmwiki"
  reads: "source"
  writes: "bronanalyse"
---

# Bronnen en bronanalyse

## 1. Bron opnemen (laag 1 en 2)

Volg `wiki-ingest`. Voor deze wiki is `--brontype` verplicht:

Kies het brontype volgens de regel Bronvoorrang in `kennismodel/modelleerregels.md`; daar staan de volgorde en de betekenis. Voorbeelden:

| Brontype | Voorbeelden |
|---|---|
| `europese-regelgeving` | eur-lex.europa.eu: AVG, AI-verordening |
| `rijksregelgeving` | wetten.overheid.nl: wetten, AMvB's, ministeriële regelingen, verdragen |
| `informatiemodel` | RSGB, RGBZ, ZTC, MIM-modellen, catalogi van basisregistraties, UPL-lijsten (zelfde voorrang) |
| `richtlijn` | HUP en circulaires van RvIG, handreikingen en werkinstructies van NVVB, VNG-handreikingen en -raadgevers, Divosa |
| `gemeentelijke-regelgeving` | lokaleregelgeving.overheid.nl: verordeningen (ook de APV), nadere regels, beleidsregels; VNG-modelverordeningen |
| `beleid` | beleidsnota's, visies, programma's en raadsvoorstellen van een gemeente |
| `overig` | productpagina's, websites, presentaties |

Alleen `europese-regelgeving` en `rijksregelgeving` tellen als landelijke wettelijke bron (regel Wettelijke grondslag).

Het GGM en het GEMMA-model komen niet via deze stap binnen, maar via de release-skills.

Een bron wordt letterlijk bewaard: ophalen met `llmwiki source add --url` (nooit een samenvatting of WebFetch-weergave als bron), nooit vertalen of herschrijven.

## 2. Bronselectie (kwaliteit bespreken)

- NOOIT een bron afwijzen omdat die van een andere gemeente dan de eigen komt; bronnen uit meerdere gemeenten leveren elementen op die voor alle gemeenten bruikbaar zijn.
- Beoordeel een bron ALLEEN op inhoudelijke relevantie: noemt ze begrippen die elementen van dit model kunnen zijn?
- NOOIT een bron afwijzen omdat ze niet beschrijft wat gemeenten registreren. Ook strategie- en governancedocumenten noemen concrete objecten, rollen en processen.
- Een bron zonder bruikbare begrippen krijgt toch een bronanalyse, met `relevant: nee` en een reden; het bestand in `sources/` blijft ongemoeid.
- ALS een onderwerp alleen een wettekst (of informatiemodel) heeft en geen beleids- of praktijkbron → signaleer dat aan de redacteur en stel een aanvullende bron voor (een VNG-handreiking, een model- of gemeentelijke verordening, een gemeentelijke webpagina). Zonder zo'n bron ontbreekt de gangbare taal voor namen en herkenbare definities.

## 3. Kernpunten bespreken

Lees de bron en bespreek met de redacteur, vóór je schrijft: hoe rijk is de bron, welke begrippen, relaties en specialisaties springen eruit, en wat is de rol van de bron in de bronvoorrang (is het de formele grondslag, of levert ze de gangbare taal?). Dit is signaleren, nog geen beoordeling.

## 4. Bronanalyse schrijven

Pad `bronanalyses/<onderwerp>/<brontype>/<bron-id>.md`, met het brontype uit de intake (regel Bronvoorrang; `tools/beslissen.py` controleert de map) (schema `schemas/bronanalyse.schema.json`):

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

Bron: [tekst](../../../../sources/raw/<bron-id>.md) · [origineel (pdf)](…) · [online](<url>)

## Samenvatting
Wat deze bron betekent voor de architectuur van dit onderwerp (max. 500 woorden; herhaal de technische index niet).

## Kernbegrippen
| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|

## Relaties
| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|

## Relevantie voor de architectuur
Welke objecten, rollen, processen, diensten of gebeurtenissen; welke specialisaties.

## Citaten
> Letterlijke tekst die een begrip definieert. (vindplaats: art./§/pagina)
```

De regel `Bron:` zet het gereedschap: `uv run python -m llmwiki source bronregel <bron-id> --van bronanalyses/<onderwerp>/<brontype>/<bron-id>.md --schrijf`, nadat de pagina met titel bestaat. Het is de schakel van de pagina's naar de brontekst; zonder die regel meldt `tools/beslissen.py` een fout. Citaten zijn platte tekst, zonder links.

In *Andere termen in deze bron* staan de andere namen die de bron voor hetzelfde begrip gebruikt, en bij een beleids- of praktijkbron de wetsterm waarnaar de bron verwijst (bijv. "urn" in de bron, wettelijk "asbus"). Zo zijn wetsterm en gangbare term al bij de ingest aan elkaar gekoppeld.

In `## Relaties` staan de verbanden tussen begrippen zoals de bron ze legt, met het werkwoord letterlijk uit de bron ("de heffingsambtenaar legt de aanslag op", "een beschikking bestaat uit onderdelen") en de vindplaats. Gebruik begripsnamen als platte tekst; of een relatie een ArchiMate-relatie wordt, hangt af van de beoordeling van beide begrippen. Neem ook verbanden op met begrippen die mogelijk geen element worden: `tools/relaties.py` tilt ze op of laat ze vervallen.

ALTIJD per partij (persoon, organisatie, verantwoordelijkheid) een rij voor wat zij volgens de bron houdt, beheert, uitvoert of vervult, ook als dat in een bijzin of begripsomschrijving staat ("een kerkgenootschap kan een bijzondere begraafplaats houden" → `kerkgenootschap | houdt | bijzondere begraafplaats | art. 37`). Het kenmerk *relaties* steunt op deze rijen.

## 5. Onderwerp

Zet de bron-id in `bronnen` van `beoordelingen/onderwerpen/<onderwerp>.yaml`; `tools/beslissen.py` controleert dat elke bronanalyse daar staat. Bestaat het onderwerp nog niet, maak het in overleg met de redacteur: `naam`, `omschrijving` (alinea's), `bronnen` en `status: in-behandeling`. De begrippenlijst `begrippen/<onderwerp>.md` maakt het render-script. Een onderwerp wordt altijd afgesloten met `status: afgerond` en een `conclusie`, ook als er geen elementen uit voortkomen.
