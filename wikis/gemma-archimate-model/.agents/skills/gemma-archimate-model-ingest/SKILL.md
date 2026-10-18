---
name: gemma-archimate-model-ingest
description: Bronnen voor gemma-archimate-model — brontype vastleggen, bronnen selecteren, een bronduiding schrijven (wat de bron betekent voor de architectuur) en de kernpunten met de redacteur bespreken. Gebruik binnen gemma-archimate-model-update, stap 2.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "wiki-ingest"
  requires-tools: "llmwiki"
  reads: "source"
  writes: "bronduiding"
---

# Bronnen en bronduiding

## 1. Bron opnemen (laag 1 en 2)

Volg `wiki-ingest`. Voor deze wiki is `--brontype` verplicht:

Kies het brontype volgens de regel Bronvoorrang in `kennismodel/modelleerregels.md`; daar staan de volgorde en de betekenis. Voorbeelden:

| Brontype | Voorbeelden |
|---|---|
| `europese-regelgeving` | eur-lex.europa.eu: AVG, AI-verordening |
| `rijksregelgeving` | wetten.overheid.nl: wetten, AMvB's, ministeriële regelingen, verdragen |
| `informatiemodel` | RSGB, RGBZ, ZTC, MIM-modellen, catalogi van basisregistraties, de UPL van Logius en de UPL-lijsten van GEMMA (zelfde voorrang) |
| `richtlijn` | HUP en circulaires van RvIG, handreikingen en werkinstructies van NVVB, VNG-handreikingen en -raadgevers, Divosa |
| `gemeentelijke-regelgeving` | lokaleregelgeving.overheid.nl: verordeningen (ook de APV), nadere regels, beleidsregels; VNG-modelverordeningen |
| `beleid` | beleidsnota's, visies, programma's en raadsvoorstellen van een gemeente |
| `overig` | productpagina's, websites, presentaties |
| `model` | matchdoel, geen bron voor een claim en buiten de volgorde: het GEMMA-model, het GGM en de GGM-website, een inhoudspagina van GEMMA Online |

Alleen `europese-regelgeving` en `rijksregelgeving` tellen als landelijke wettelijke bron (regel Wettelijke grondslag).

Het GGM en het GEMMA-model komen niet via deze stap binnen, maar via de release-skills; hun bronduiding verhuist bij een release mee. Een webpagina of lijst die bij een model hoort (de GGM-website, de UPL van Logius) neem je wel via deze stap op, met het brontype van haar rol: `model` voor het ongestructureerde deel van een matchdoel, `informatiemodel` voor de UPL.

Een bron wordt letterlijk bewaard: ophalen met `llmwiki source add --url` (nooit een samenvatting of WebFetch-weergave als bron), nooit vertalen of herschrijven.

## 2. Bronselectie (kwaliteit bespreken)

- NOOIT een bron afwijzen omdat die van een andere gemeente dan de eigen komt; bronnen uit meerdere gemeenten leveren elementen op die voor alle gemeenten bruikbaar zijn.
- Beoordeel een bron ALLEEN op inhoudelijke relevantie: noemt ze begrippen die elementen van dit model kunnen zijn?
- NOOIT een bron afwijzen omdat ze niet beschrijft wat gemeenten registreren. Ook strategie- en governancedocumenten noemen concrete objecten, rollen en processen.
- Een bron zonder bruikbare begrippen krijgt toch een bronduiding, met `relevant: nee` en een reden; het bestand in `sources/` blijft ongemoeid.
- ALS een onderwerp alleen een wettekst (of informatiemodel) heeft en geen beleids- of praktijkbron → signaleer dat aan de redacteur en stel een aanvullende bron voor (een VNG-handreiking, een model- of gemeentelijke verordening, een gemeentelijke webpagina). Zonder zo'n bron ontbreekt de gangbare taal voor namen en herkenbare definities.

## 3. Kernpunten bespreken

Lees de bron en bespreek met de redacteur, vóór je schrijft: hoe rijk is de bron, welke begrippen, relaties en specialisaties springen eruit, en wat is de rol van de bron in de bronvoorrang (is het de formele grondslag, of levert ze de gangbare taal?). Dit is signaleren, nog geen beoordeling.

## 4. Bronduiding schrijven

**Eén bronduiding per bron, per deel van de wet.** Zoek eerst of de bron al een bronduiding heeft, in welk onderwerp dan ook: `ls onderwerpen/*/bronduidingen/*/<bron-id>.md modellen/*/bronduidingen/*/<bron-id>.md`. Bestaat zij, vul haar dan aan met de delen die dit onderwerp raakt en zet de bron alleen in `bronnen` van `afbakening.yaml` van dit onderwerp; maak geen tweede bronduiding. Links naar de bron lossen wiki-breed op naar die ene bronduiding.

**Alleen de delen die een element onderbouwen.** Bij een wet: `uv run python tools/bronduiding.py delen <bron-id>` toont de hoofdstukken, afdelingen en artikelen met regelnummer. Duid alleen de delen die begrippen, relaties of een grondslag voor dit onderwerp leveren; zeg in de *Samenvatting* welke delen dat zijn en welke je liet liggen. Blijkt na Typeren dat een element een ander deel nodig heeft, vul de bronduiding dan aan (kernbegrippen, relaties, citaten); de bronduiding hoeft niet vooraf af te zijn.

**Citaten komen uit het script, niet uit het geheugen.** `uv run python tools/bronduiding.py citaat <bron-id> "art. 6 lid 2" --schrijf <bronduiding.md>` haalt de letterlijke tekst uit `sources/raw/` en zet haar met de vindplaats onder `## Citaten` (zonder `--schrijf` toont het de regel). Voor een bron zonder artikelen (een webpagina, een handreiking) typ je het citaat over uit de brontekst, met de kop of het alineanummer als vindplaats; weglaten kan met `…`. `uv run python tools/bronduiding.py controleer <bronduiding.md>` meldt een citaat dat niet letterlijk in de bron staat (leestekens en opmaak tellen niet); `tools/beslissen.py` geeft dezelfde melding als waarschuwing (regel Elke claim een bron). Los die op door het citaat te herstellen, niet door de bron te wijzigen.

Pad `onderwerpen/<onderwerp>/bronduidingen/<brontype>/<bron-id>.md`, met het brontype uit de intake (regel Bronvoorrang; `tools/beslissen.py` controleert de map) (schema `schemas/bronduiding.schema.json`):

```markdown
---
id: <bron-id>
type: bronduiding
onderwerp: <onderwerp-id>      # bij een bron van een model: model: <model> (gemma, ggm of upl), en het pad modellen/<model>/bronduidingen/<brontype>/
bronnen: [<bron-id>]
relevant: ja
bijgewerkt: <datum>
---

# <titel van de bron>

Bron: [tekst](../../../../../../sources/raw/<bron-id>.md) · [origineel (pdf)](…) · [online](<url>)

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

Een bron van een model (het GEMMA-model, het GGM, de UPL, en bronnen voor de methode zoals Over GEMMA) heeft haar bronduiding in `modellen/<model>/bronduidingen/<brontype>/`, met `model:` in plaats van `onderwerp:`, en staat niet in de bronnen van een onderwerp. Eén bronduiding duidt soms meer bronnen samen, zoals de pagina's van een website of de tabellen bij een lijst: die bronnen staan alle in `bronnen:`, en een verwijzing naar één ervan linkt naar die bronduiding (`tools/gam_gemeen.py`, `bron_doel`). Een bronduiding van een model bevat alleen wat over releases heen gelijk blijft: geen tellingen, geen wijzigingen per release, geen samenvatting van terugmeldingen.

De regel `Bron:` zet het gereedschap: `uv run python -m llmwiki source bronregel <bron-id> --van onderwerpen/<onderwerp>/bronduidingen/<brontype>/<bron-id>.md --schrijf`, nadat de pagina met titel bestaat. Het is de schakel van de pagina's naar de brontekst; zonder die regel meldt `tools/beslissen.py` een fout. Citaten zijn platte tekst, zonder links.

In *Andere termen in deze bron* staan de andere namen die de bron voor hetzelfde begrip gebruikt, en bij een beleids- of praktijkbron de wetsterm waarnaar de bron verwijst (bijv. "urn" in de bron, wettelijk "asbus"). Zo zijn wetsterm en gangbare term al bij de ingest aan elkaar gekoppeld.

In `## Relaties` staan de verbanden tussen begrippen zoals de bron ze legt, met het werkwoord letterlijk uit de bron ("de heffingsambtenaar legt de aanslag op", "een beschikking bestaat uit onderdelen") en de vindplaats. Gebruik begripsnamen als platte tekst; of een relatie een ArchiMate-relatie wordt, hangt af van de beoordeling van beide begrippen. Neem ook verbanden op met begrippen die mogelijk geen element worden: `tools/relaties.py` tilt ze op of laat ze vervallen.

ALTIJD per partij (persoon, organisatie, verantwoordelijkheid) een rij voor wat zij volgens de bron houdt, beheert, uitvoert of vervult, ook als dat in een bijzin of begripsomschrijving staat ("een kerkgenootschap kan een bijzondere begraafplaats houden" → `kerkgenootschap | houdt | bijzondere begraafplaats | art. 37`). Het kenmerk *relaties* steunt op deze rijen.

## 5. Onderwerp

Zet de bron-id in `bronnen` van `onderwerpen/<onderwerp>/afbakening.yaml`; `tools/beslissen.py` controleert dat elke bronduiding daar staat. Bestaat het onderwerp nog niet, maak het in overleg met de redacteur: `naam`, `omschrijving` (alinea's), `bronnen` en `status: in-behandeling`. De begrippenlijst `begrippen/<onderwerp>.md` maakt het render-script. Een onderwerp wordt altijd afgesloten met `status: afgerond` en een `conclusie`, ook als er geen elementen uit voortkomen.
