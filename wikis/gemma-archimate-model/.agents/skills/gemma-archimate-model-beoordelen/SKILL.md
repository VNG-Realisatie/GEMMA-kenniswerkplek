---
name: gemma-archimate-model-beoordelen
description: Beoordeel de begrippen van een onderwerp in gemma-archimate-model — per begrip een beoordeling (beoordelingen/begrippen/<id>.yaml) met kenmerken, naam, definitie, beschrijving, GGM- en GEMMA-match op betekenis, relaties, hiërarchie en GGM-terugmeldingen. Scripts leiden daaruit type en status af en maken de pagina's. Gebruik binnen gemma-archimate-model-update, na de bronanalyse.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-criteria"
  requires-tools: "python:tools/beslissen.py python:tools/bepaal_type.py python:tools/relaties.py python:tools/ggm.py python:tools/gemma.py"
  reads: "bronanalyse"
  writes: "beoordeling"
---

# Beoordelen: het oordeel per begrip

De AI schrijft alleen het oordeel. Type, status, letterlijke modelvelden, paginapad en de hele pagina komen uit de scripts. Het formaat van een beoordeling staat in `schemas/beoordeling.schema.json` (gegenereerd door `tools/bepaal_type.py schema`); `tools/beslissen.py` toetst het.

## 1. Lezen

Eerst `besluiten/per-begrip.md` (wat al beslist is, vraag je niet opnieuw), dan de technische index (`sources/index/`), de bronanalyses van dit onderwerp, en uit `sources/raw/` alleen de passages die index of bronanalyse aanwijzen. Houd de regel Bronvoorrang aan: de hogere brontypen bepalen welke begrippen er zijn en wat ze formeel betekenen; `richtlijn`, `beleid` en `overig` laten zien hoe erover gesproken wordt.

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
kwaliteitsdoelen: [{id: id-…, sterkte: "++", onderbouwing: "De wet regelt de taak.", bronnen: [2026-rijk-…], vindplaats: art. 1}]   # beleidskader: GEMMA-kwaliteitsdoelen waaraan het grondslag geeft
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
| `onderwerpen`, `per_onderwerp`, `synoniem_van` (één model over de onderwerpen heen) | de regels Eén element in het hele model, Thuishoren en Relaties tussen onderwerpen in `kennismodel/modelleerregels.md` |
| `besluiten` | `references/besluiten.md` |
| `kwaliteitsdoelen` (alleen bij een beleidskader) | de modelleerafspraken van Kwaliteitsdoel en Beleidskader in het kennismodel. Een kwaliteitsdoel is een element van GEMMA: kies het uit `uv run python tools/gemma.py kwaliteitsdoelen` en noem het `id`. De sterkte en wat ze betekent, staan in de modelleerafspraken van Kwaliteitsdoel; onderbouw ze met de bepalingen uit de regeling die eisen of normen voor het doel stellen. |
| `kernobject`, `afnemer`, `domein`, `doelgroep`, `regelgever`, `gemma_generiek` | skill `gemma-archimate-model-criteria`, stap 7 (achtergrond: `docs/indelingen.md`) |

De beschrijving van een beleidsdomein (wat erbij hoort, met bronnen) staat niet in een beoordeling of in de omschrijving van een onderwerp, maar in het register `beoordelingen/beleidsdomeinen.yaml` (`beleidsdomein`, `taakveld`, `beschrijving`, `bronnen`); de render toont haar in het overzicht en de export zet haar op de groepering. `tools/beslissen.py` controleert dat een element het beleidsdomein gebruikt en het taakveld klopt.

## 5. Match op betekenis

`uv run python tools/ggm.py kandidaten <naam> [--synoniemen a,b]` en `uv run python tools/gemma.py kandidaten <naam> [--ggm-guid <guid>]` geven in één overzicht de naamgenoten (mogelijke homoniemen), de treffers met definitie en beleidsdomein, en de generalisaties. Kies op betekenis: vergelijk definities, volg relaties en generalisaties, en let op homoniemen en synoniemen. Vul alleen `guid` of `id`, `sterkte` en `onderbouwing` in; de letterlijke velden haalt `tools/beslissen.py` op.

## 6. Relaties

Na een eerste `uv run python tools/beslissen.py` (zonder relaties werkt dat al): `uv run python tools/relaties.py voorstel <id>` geeft kandidaten uit het GGM en uit de relatietabellen van de bronanalyses, als YAML voor `relaties:`. Kies, geef een herkenbare naam, controleer richting en kardinaliteit. Een relatie staat alleen in de beoordeling van het bronelement; de render zet de inkomende kant op de pagina van het doel. `uv run python tools/relaties.py uit-bronnen <onderwerp>` toont welke relaties uit de bronnen vervallen omdat een kant geen element is; leg belangrijke vervallen relaties voor.

## 7. Terugmeldingen (GGM, procesarchitectuur en GEMMA)

Een bevinding over het GGM, over de GEMMA-procesarchitectuur (UPL-lijsten, kennismodel procesarchitectuur) of over het GEMMA-model zelf zet je zonder nummer in het register van de ontvanger: `beoordelingen/terugmeldingen/ggm.yaml`, `procesarchitectuur.yaml` of `gemma.yaml`. Welk register, welke velden en typen, de opbouw (**GGM:**/**UPL:**/**Kennismodel:**/**GEMMA:**, **Bevinding:**, **Voorstel:**) en hoe je schrijft voor een lezer buiten de wiki: `references/terugmeldingen.md`.

## 8. Beslissen en voorleggen

Draai `uv run python tools/beslissen.py`. De uitkomst van de beslistabel is bindend; pas een kenmerk alleen aan als het aantoonbaar fout was. Wat dan nog een keuze van de redacteur vraagt, leg je één voor één voor in de chat en leg je vast in `besluiten:`: `references/besluiten.md`.
