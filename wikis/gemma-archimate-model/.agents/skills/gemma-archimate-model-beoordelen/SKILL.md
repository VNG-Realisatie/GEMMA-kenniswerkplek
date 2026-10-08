---
name: gemma-archimate-model-beoordelen
description: Beoordeel de begrippen van een onderwerp in gemma-archimate-model — per begrip een beoordeling (beoordelingen/begrippen/<id>.yaml) met kenmerken, naam, definitie, beschrijving, GGM- en GEMMA-match op betekenis, relaties, hiërarchie en GGM-terugmeldingen. Scripts leiden daaruit type en status af en maken de pagina's. Gebruik binnen gemma-archimate-model-update, na de bronanalyse.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-criteria"
  requires-tools: "python:tools/afleiden.py python:tools/bepaal_type.py python:tools/relaties.py python:tools/ggm.py python:tools/gemma.py"
  reads: "bronanalyse"
  writes: "beoordeling"
---

# Beoordelen: het oordeel per begrip

De AI schrijft alleen het oordeel. Type, status, letterlijke modelvelden, paginapad en de hele pagina komen uit de scripts. Het formaat van een beoordeling staat in `schemas/beoordeling.schema.json` (gegenereerd door `tools/bepaal_type.py schema`); `tools/afleiden.py` toetst het.

## 1. Lezen

Eerst `besluiten/per-begrip.md` (wat al beslist is, vraag je niet opnieuw), dan de technische index (`sources/index/`), de bronanalyses van dit onderwerp, en uit `sources/raw/` alleen de passages die index of bronanalyse aanwijzen. Houd de regel Bronvoorrang aan (`europese-regelgeving` → `rijksregelgeving` → `informatiemodel` → `richtlijn` → `gemeentelijke-regelgeving` → `beleid` → `overig`): de hogere brontypen bepalen welke begrippen er zijn en wat ze formeel betekenen; `richtlijn`, `beleid` en `overig` laten zien hoe erover gesproken wordt.

## 2. Begrippen verzamelen

- Alle kernbegrippen uit de bronanalyses van het onderwerp, plus wat al als beoordeling bestaat met dit onderwerp in `onderwerpen`.
- De GGM-entiteiten van de betrokken beleidsdomeinen. Sla nooit een begrip over omdat het GGM er al een entiteit voor heeft: deze stap toetst ook het GGM.
- Kijk per partij ook naar kanalen, beleidskaders en samenwerkingen; die typen bestaan sinds 2026-10-01.
- Een wet die de UPL noemt als grondslag van een UPL-product haal je op als bron (besluit redacteur 2026-10-07). Daarna beoordeel je of ze een beleidskader wordt: alleen als ze de gemeente een taak of bevoegdheid geeft. Een wet die alleen een tarief of een regel buiten de gemeentelijke taak bevat (Wet griffierechten burgerlijke zaken, art. 23), blijft bron zonder beleidskader; zoek dan de bevoegdheidsgrondslag. Een verdrag is bron en geen beleidskader zolang de criteria geen regelgever verdrag kennen (Overeenkomst van München 1980; de Nederlandse uitvoering staat in BW boek 1 art. 49a).

## 3. Per begrip, vóór de kenmerken

1. **Welk begrip?** Bestaat er al een beoordeling met deze naam of als synoniem? Een ander woord voor een bestaand begrip: `synoniem_van`. Dezelfde naam voor een ander begrip (in de wiki, het GGM, het GEMMA-model of een bron): `homoniem_van`, en de naamkeuze wordt voorgelegd. Een GGM-duplicaat (zelfde begrip, andere GUID) is geen homoniem; een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger.
2. **Domein.** Zoek het begrip eerst in alle beoordelingen van alle onderwerpen, op naam en synoniemen (regel Eén element in het hele model): bestaat het al, werk die beoordeling bij en voeg je onderwerp toe aan `onderwerpen`, achter het thuisonderwerp. Bepaal het thuisonderwerp op inhoud (regel Thuishoren): generiek of een orgaan van de gemeente is Algemeen; anders de taak waarin het element ontstaat of verandert (het proces dat het object maakt, het kernobject van een proces, dienst of product, het object waarvan een gebeurtenis de toestand verandert, het meeste gedrag van een rol). Het thuisonderwerp staat als eerste in `onderwerpen`. Hoort het bij een onderwerp dat nog niet bestaat, dan is *betekenis in onderwerp* nee (verwijzing); bij twijfel voorleggen. Leg de relaties naar elementen van andere onderwerpen vast (regel Relaties tussen onderwerpen).
3. **Naam.** De gangbare term uit beleid en praktijk; de wetsterm wordt een synoniem met context "wet" (regel Bronvoorrang). Zie `references/naamgeving.md`.
4. **Hoogste herkenbare niveau.** Kijk eerst naar boven: generalisaties in de wiki, het GGM (`tools/ggm.py kandidaten <naam>`) en het GEMMA-model. Kies het hoogste niveau dat domeinexperts herkennen; bedenk nooit een kunstmatige verzamelnaam. Een specialisatie krijgt alleen een eigen pagina als domeinexperts de term zelf gebruiken, ze eigen gegevens of een eigen levenscyclus heeft en GEMMA vergelijkbare specialisaties op dat niveau kent; anders *zelfstandige specialisatie* nee en `genoemd_begrip`. Zie `references/hierarchie.md`.
5. **Attribuut of onderdeel?** `tools/ggm.py attribuut <term>`; een eigenschap of waarde van een ander begrip: *slechts eigenschap* ja, met `genoemd_begrip`.

## 4. De beoordeling schrijven

Eén bestand per begrip: `beoordelingen/begrippen/<id>.yaml`, met als id de naam in kleine letters met koppeltekens. Ook een begrip dat geen element wordt, krijgt een beoordeling (alle kenmerken en een `toelichting`); het komt dan alleen in de begrippenlijst. Elke tekst staat op één regel; meer alinea's zijn meer lijstitems. Bron-id's in lopende tekst worden vanzelf links.

```yaml
begrip: Begraafplaats
onderwerpen: [lijkbezorging]
kenmerken:                        # alle kenmerken uit gemma-archimate-model-criteria
  herkenbaar: {waarde: ja, onderbouwing: "Gangbaar begrip (Groningen art. 1).", bronnen: [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen]}
  gedrag: {waarde: nee, onderbouwing: "Een passief ding."}
  # …
# Alleen bij een element:
definitie: Terrein waar lijken worden begraven en urnen worden bijgezet.          # één zin, ≤160 tekens
beschrijving:
  - Elke gemeente heeft ten minste één gemeentelijke begraafplaats (2026-rijk-wet-op-de-lijkbezorging-wettekst, art. 33).
per_onderwerp:
  lijkbezorging:
    - De gemeente geeft graven uit en ruimt ze.
synoniemen: [{naam: begraafterrein, context: beleid}]
taakveld: 7 Volksgezondheid en Milieu         # bij typen met submappen taakveld en beleidsdomein (wiki.yaml); niet bij een functie (submap domein)
beleidsdomein: Begraafplaatsen en crematoria
grondslag: bron                               # ggm-entiteit | ggm-afgeleid | procesobject | regelgeving | bron
grondslag_toelichting: []                     # verplicht bij regelgeving, procesobject, ggm-afgeleid
ggm: {sterkte: geen, onderbouwing: "Het GGM kent geen begraafplaats."}          # bij gegevensobjecten; met guid bij een match
gemma: {sterkte: geen, onderbouwing: "Nieuw voor GEMMA."}                       # altijd; met id bij een match
# Indeling (stap 7 van skill gemma-archimate-model-criteria), alleen waar het type erom vraagt:
kernobject: graf                              # levensloopproces, bedrijfsproces, bedrijfsinteractie: het object waarvan het de levensloop omvat, waarin het een mutatie doet of dat door de keten gaat
afnemer: extern                               # proces, product, dienst: extern of intern
domein: Fysieke leefomgeving                  # functie, product, dienst: GEMMA-domein
doelgroep: gemeente                           # actor, rol, samenwerking, kanaal: gemeente | inwoners en ondernemers | ketenpartners
regelgever: rijk                              # beleidskader: EU | rijk | VNG-model
gemma_generiek: {id: id-…, onderbouwing: "Een vergunningaanvraag."}   # specialisatie van een generiek GEMMA-element (exacte match)
specialisaties: [{naam: Bijzondere begraafplaats, omschrijving: "Van een kerkgenootschap of rechtspersoon (art. 24)."}]
relaties:
  - {soort: aggregatie, naar: graf, naam: bevat, grondslag: bron, bronnen: [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen], vindplaats: art. 1}
vragen: []                                    # open vragen aan de redacteur
besluiten: []                                 # alleen na een antwoord van de redacteur
```

Velden en wat erin hoort:

| Veld | Zie |
|---|---|
| `definitie`, `definitie_formeel`, `definitie_formeel_bron`, `beschrijving`, `per_onderwerp` | `references/definitie.md` |
| `begrip`, `synoniemen`, `naamkeuze`, `homoniemen` | `references/naamgeving.md` |
| `grondslag`, `grondslag_toelichting` | `references/grondslag.md` |
| `ggm` (guid, sterkte, onderbouwing, duplicaten) | `references/ggm-match.md` |
| `gemma` (id, sterkte, onderbouwing) | `references/gemma-match.md` |
| `generalisatie`, `specialisaties`, `ggm_componenten` | `references/hierarchie.md` |
| `tegenhanger` | `references/tegenhangers.md` |
| `relaties` (ook `via`: de specialisatie zonder pagina van het generieke doel) | `references/relaties.md` |
| `kernobject`, `afnemer`, `domein`, `doelgroep`, `regelgever`, `gemma_generiek` | skill `gemma-archimate-model-criteria`, stap 7 (achtergrond: `docs/indelingen.md`) |

De beschrijving van een beleidsdomein (wat erbij hoort, met bronnen) staat niet in een beoordeling of in de omschrijving van een onderwerp, maar in het register `beoordelingen/beleidsdomeinen.yaml` (`beleidsdomein`, `taakveld`, `beschrijving`, `bronnen`); de render toont haar in het overzicht en de export zet haar op de groepering. `tools/afleiden.py` controleert dat een element het beleidsdomein gebruikt en het taakveld klopt.

## 5. Match op betekenis

`uv run python tools/ggm.py kandidaten <naam> [--synoniemen a,b]` en `uv run python tools/gemma.py kandidaten <naam> [--ggm-guid <guid>]` geven in één overzicht de naamgenoten (mogelijke homoniemen), de treffers met definitie en beleidsdomein, en de generalisaties. Kies op betekenis: vergelijk definities, volg relaties en generalisaties, en let op homoniemen en synoniemen. Vul alleen `guid` of `id`, `sterkte` en `onderbouwing` in; de letterlijke velden haalt `tools/afleiden.py` op.

## 6. Relaties

Na een eerste `uv run python tools/afleiden.py` (zonder relaties werkt dat al): `uv run python tools/relaties.py voorstel <id>` geeft kandidaten uit het GGM en uit de relatietabellen van de bronanalyses, als YAML voor `relaties:`. Kies, geef een herkenbare naam, controleer richting en kardinaliteit. Een relatie staat alleen in de beoordeling van het bronelement; de render zet de inkomende kant op de pagina van het doel. `uv run python tools/relaties.py uit-bronnen <onderwerp>` toont welke relaties uit de bronnen vervallen omdat een kant geen element is; leg belangrijke vervallen relaties voor.

## 7. Terugmeldingen (GGM en procesarchitectuur)

Een bevinding over het GGM (hiaat, definitie, structuur, scope, duplicaat, homoniem, relatie) zet je in `beoordelingen/terugmeldingen/ggm.yaml`, zonder nummer: `{domein, entiteit, type, bevinding, element}`. `tools/afleiden.py` geeft het volgende nummer. Een hiaat alleen bij een gegevensobject zonder GGM-match, conservatief: motiveer waar de gegevens worden beheerd, welke attributen relevant zijn en in welk beleidsdomein het past. Een proces, functie of regeling zonder GGM-entiteit is geen hiaat. Schrijf een bevinding als lijst alinea's: **GGM:** (wat er nu staat), **Bevinding:** (wat er niet klopt, met bron) en **Voorstel:**; een alinea die met `- ` begint, wordt een lijstitem (attributen, dubbele GUID's). In de tabel van de analyse staan de alinea's in één cel, met regelovergangen.

Een bevinding over de GEMMA-procesarchitectuur (de UPL-lijsten of het kennismodel procesarchitectuur) zet je in `beoordelingen/terugmeldingen/procesarchitectuur.yaml`, zonder nummer: `{type, bevinding, elementen of beleidsdomein}`, met type `indeling`, `grondslag`, `product` of `kennismodel`. De bevinding is voor de werkgroep procesarchitectuur: wat GEMMA anders indeelt of modelleert dan de UPL of het kennismodel, en waarom; geen vraag. Schrijf haar net als een GGM-terugmelding als lijst alinea's: **UPL:** (wat de UPL zegt) of bij type `kennismodel` **Kennismodel:** (wat het kennismodel zegt), dan **Bevinding:** (wat er niet klopt of anders is, hoe GEMMA het modelleert en waarom, met bron) en **Voorstel:** (wat de werkgroep concreet kan veranderen); een alinea die met `- ` begint, wordt een lijstitem. Schrijf voor een lezer zonder deze wiki: korte zinnen, de kern vooraan, bronnen achteraan tussen haakjes, geen interne termen zonder uitleg. Een open melding zonder alinea **Bevinding:** of **Voorstel:** houdt `tools/afleiden.py` tegen, ook bij de GGM (besluit redacteur 2026-10-08). Een UPL-product zonder grondslag, of met een UPL-grondslag die geen taak geeft (alleen een tarief, een beleidsstuk van één gemeente), krijgt een melding van type `grondslag` (regel Wettelijke grondslag). Het model mag afwijken van de UPL-indeling (taakveld, GEMMA-domein) en van het kennismodel procesarchitectuur, mits de afwijking daar is teruggemeld (besluit redacteur 2026-10-05); de terugmelding dekt dan het signaal van `tools/afleiden.py`. Een nieuw element met dezelfde afwijking voeg je toe aan de `elementen` van de bestaande melding.

Een bevinding over het GEMMA-model zelf (een GEMMA-element dat ontbreekt, in de wiki vervalt of herzien moet worden, een afwijkende indeling, definitie of relatie) zet je in `beoordelingen/terugmeldingen/gemma.yaml`, zonder nummer: `{type, bevinding, elementen en/of gemma_elementen}`, met type `element`, `indeling`, `definitie` of `relatie`. Een GEMMA-element dat de wiki niet (meer) kent, noem je in `gemma_elementen` met `id` en `naam` zoals in het GEMMA-model; `tools/afleiden.py` controleert beide. De bevinding volgt dezelfde opbouw: **GEMMA:** (wat het GEMMA-model nu zegt), **Bevinding:** en **Voorstel:** (besluit redacteur 2026-10-08). Laat de wiki een gekoppeld GEMMA-element vervallen, dan blijft het in GEMMA (de sync haalt alleen de wiki-eigenschappen weg); meld het dan hier.

## 8. Afleiden en voorleggen

Draai `uv run python tools/afleiden.py`. De uitkomst van de beslistabel is bindend; pas een kenmerk alleen aan als het aantoonbaar fout was. Leg daarna per begrip met open redenen (`afgeleid.open`) de vraag voor in de chat, één voor één, met context (welk begrip, wat de beslistabel zegt), argumenten voor en tegen, en een advies. Leg het antwoord vast in `besluiten:`:

```yaml
besluiten:
  - datum: 2026-10-01
    besluit: Opnemen als gegevensobject zonder GGM-entiteit; terugmelding 3.
    gevolg: opnemen                 # opnemen | afwijzen | verwerkt
    redenen: [gegevensobject zonder sterke GGM-match]   # letterlijk uit afgeleid.voor_te_leggen
```

`opnemen` met de gedekte redenen maakt een kandidaat `review`; `afwijzen` maakt hem `afgewezen`; `verwerkt` legt een besluit vast dat de AI in de beoordeling heeft doorgevoerd (bijvoorbeeld een naamkeuze).
