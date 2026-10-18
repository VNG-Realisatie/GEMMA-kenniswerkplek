---
name: gemma-archimate-model-beoordelen
description: Fase B van de beoordeling in gemma-archimate-model — per begrip de kenmerken van het type, naam, definitie, beschrijving, GGM- en GEMMA-match op betekenis, relaties, hiërarchie en terugmeldingen, in onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml. Scripts leiden daaruit type en status af en maken de pagina's. Gebruik in fase 2 van gemma-archimate-model-update, door een beoordelingsagent per cluster of door de hoofdsessie, na fase A (gemma-archimate-model-criteria).
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-criteria"
  requires-tools: "python:tools/beslissen.py python:tools/bepaal_type.py python:tools/beoordeling.py python:tools/relaties.py python:tools/ggm.py python:tools/gemma.py"
  reads: "bronduiding"
  writes: "beoordeling"
---

# Beoordelen: fase B

De AI schrijft alleen het oordeel. Type, status, letterlijke modelvelden, paginapad en de pagina zelf komen uit de scripts. Het formaat staat in `schemas/beoordeling.schema.json`; `tools/beslissen.py` toetst het. Je begint met de beoordelingen van fase A (skill `gemma-archimate-model-criteria`) en het werkpakket van je cluster; zoek niet ad hoc wat daarin staat. Lees een reference alleen als je het veld invult dat erbij hoort. Lees na het schrijven een bestand niet terug: de scripts controleren het.

## Stappen per begrip

**Sjabloon.** Een UPL-product dat een extern gedrag aanbiedt en door een bedrijfsproces met een kernobject wordt gerealiseerd, zet je klaar met `uv run python tools/beoordeling.py sjabloon upl-dienst <id> --naam … --onderwerp … --kernobject <id> --bron <bron-id> (--proces <id> | --proces-naam …) [--upl-nr … --taakveld … --beleidsdomein … --domein … --toegang raadplegen|registreren]`. Met `--proces` krijgt een bestaand proces alleen de relatie realisatie; met `--proces-naam` komt er een nieuw proces bij. Het sjabloon zet de structuur en de bronnen, geen inhoud: elke `TODO` vervang je door de onderbouwing uit de bronnen (`toon <id>`, `zet <id> <veld> <waarde>`), of je past het kenmerk aan als het geval afwijkt. `beslissen.py` meldt een fout zolang er een TODO staat.

1. **Wat al besloten is.** Een besluit met zekerheid `kennis` volg je als regel; wijk je af van een besluit met `logica` of `indruk`, zet dat dan met de reden in `vragen:` (regel Navragen). Een bestaande beoordeling bekijk je compact met `uv run python tools/beoordeling.py toon <id> --oordeel`.
2. **Kenmerken van het type.** `uv run python tools/bepaal_type.py vragen <id>` geeft de vragen van fase B. Schrijf één regel per kenmerk, net als in fase A, met een onderbouwing bij elke nee. Draai daarna `uv run python tools/beoordeling.py normaliseer <id>`. Let op:
   - Een relationeel kenmerk (†) met ja noemt zijn tegenpartij: `toegewezen_partij: {waarde: ja, naar: [houder-van-de-begraafplaats]}`; leg de relatie vast (stap 5), haar bron geldt voor het kenmerk. Is de tegenpartij (nog) geen element: onderbouwing, bron en `naar: [{naam: …, type: …}]`.
   - *Zelfstandige specialisatie* (standaard ja) en *generiek* (standaard nee) alleen bij een afwijking.
   - *zelfstandige specialisatie*: kijk eerst naar boven, naar de generalisaties in de wiki, in het GGM (`tools/ggm.py generalisaties`) en in GEMMA (`tools/gemma.py zoek`), en noteer de keten (Besluit → Beschikking → Vergunning → Vergunning tot opgraving). Kies het hoogste niveau dat domeinexperts herkennen; bedenk nooit een kunstmatige verzamelnaam. Bij nee is `genoemd_begrip` het bredere begrip (`references/hierarchie.md`).
   - *gebruikt objecten* en *wordt bewerkt*: noem de handeling uit de vaste reeks ([kennismodel](../../../kennismodel/README.md), Relatietypen).
   - Het procesniveau, het objectniveau en de velden van het type (zie Velden; ook `deelprocessen`) volgen de modelleerafspraken van het type; *soort partij* die van Actor. Bij *generiek* (gebeurtenis, rol, dienst, bedrijfsproces) vul je `gemma_generiek` in: een specialisatie van een GEMMA-element met een exacte match. Ontbreekt dat element, meld het dan als voorstel aan GEMMA.
   - Een capability leid je af uit de functies en diensten van een onderwerp: `references/capability.md`.
   - Een vervallen of samengevoegd element krijgt het besluit `afwijzen`.
3. **Tekst** (alleen bij een element). `definitie`, `definitie_formeel`, `beschrijving` en `per_onderwerp`: `references/definitie.md`; wat alleen in één onderwerp geldt, staat onder `per_onderwerp` (regel Los van het onderwerp). De naam, `synoniemen`, `naamkeuze` en `homoniemen`: `references/naamgeving.md`, alleen bij een naamconflict, bij hernoemen of bij een bredere GGM-entiteit.
4. **Match op betekenis.** Gebruik de kandidaten uit het werkpakket; heb je er meer nodig, dan `uv run python tools/ggm.py kandidaten <naam> [--synoniemen a,b]` en `uv run python tools/gemma.py kandidaten <naam> [--ggm-guid <guid>]`. Vul alleen `guid` of `id`, `sterkte` en `onderbouwing` in; de letterlijke velden haalt `tools/beslissen.py` op. GGM (bij bedrijfsobjecten; bij een rol, actor of gebeurtenis mag het) en data-objecten: `references/ggm-match.md`. GEMMA (altijd), met `gemma_relatie` en `gemma_functie`: `references/gemma-match.md`. Bij een beleidskader kies je de `kwaliteitsdoelen` uit `uv run python tools/gemma.py kwaliteitsdoelen`, en onderbouw je de sterkte met de bepalingen uit de regeling die eisen of normen voor het doel stellen (modelleerafspraken van Kwaliteitsdoel).
5. **Relaties.** Begin bij de relatievoorstellen in het werkpakket of bij `uv run python tools/relaties.py voorstel <id>`. Kies, geef een herkenbare naam en controleer richting en kardinaliteit. Een relatie staat alleen in de beoordeling van het bronelement, ook naar een element van een ander onderwerp (regel Relaties tussen onderwerpen). Een relatie naar een generiek object noemt in `via` de specialisatie zonder pagina. Toevoegen gaat met `uv run python tools/beoordeling.py relatie <id> --soort … --naar … [--naam …] --bron … --vindplaats …`. Bij twijfel over soort of richting: `references/relaties.md`.
6. **Hiërarchie en tegenhanger.** `generalisatie`, `specialisaties` en `ggm_componenten`: `references/hierarchie.md`. `tegenhanger`: `references/tegenhangers.md`.
7. **Terugmeldingen.** Een bevinding over het GGM, over de GEMMA-procesarchitectuur of over het GEMMA-model gaat naar het register van de ontvanger (`references/terugmeldingen.md`). Een beoordelingsagent schrijft niet in de registers: hij zet de terugmelding in zijn verslag.
8. **Controleren.** Een beoordelingsagent draait `uv run python tools/beslissen.py --alleen <id> …` voor zijn eigen beoordelingen, nooit zonder `--alleen`. De hoofdsessie draait `tools/beslissen.py`. De uitkomst van de beslistabel is bindend: pas een kenmerk alleen aan als het aantoonbaar fout was. Een conflict, een open reden of twijfel gaat als vraag in `vragen:`, met context en advies; een antwoord van de redacteur komt in `besluiten:` (`references/besluiten.md`).

## Velden

Eén bestand per begrip. Elke tekst staat op één regel, en meer alinea's zijn meer lijstitems. Een bron-id in lopende tekst wordt vanzelf een link.

```yaml
begrip: Begraafplaats
vak: bedrijf/passief                           # fase A
onderwerpen: [lijkbezorging]
bronnen: [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen]
kenmerken:                                     # één regel per kenmerk; normaliseer maakt er de opgeslagen vorm van
  levenscyclus: ja — Aangelegd en gesloten (Groningen art. 3). [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen]
  wordt_bewerkt: {waarde: ja, naar: [beheren-begraafplaatsen]}
definitie: Terrein waar lijken worden begraven en urnen worden bijgezet.          # één zin, ≤160 tekens
beschrijving:
  - Elke gemeente heeft ten minste één gemeentelijke begraafplaats (2026-rijk-wet-op-de-lijkbezorging-wettekst, art. 33).
per_onderwerp:
  lijkbezorging:
    - De gemeente geeft graven uit en ruimt ze.
synoniemen: [{naam: begraafterrein, context: beleid}]
taakveld: 7 Volksgezondheid en Milieu         # bij typen met submappen taakveld en beleidsdomein (wiki.yaml)
beleidsdomein: Begraafplaatsen en crematoria
ggm: {sterkte: geen, onderbouwing: "Het GGM kent geen begraafplaats."}          # bij gegevensobjecten; met guid bij een match
gemma: {sterkte: geen, onderbouwing: "Nieuw voor GEMMA."}                       # altijd; met id bij een match
# Alleen waar het type erom vraagt (modelleerafspraken, Afspraken):
kernobject: graf                              # levensloopproces, bedrijfsproces, bedrijfsinteractie
afnemer: extern                               # proces, product, dienst
domein: Fysieke leefomgeving                  # functie, product, dienst, capability
doelgroep: gemeente                           # actor, rol, samenwerking, kanaal
regelgever: rijk                              # beleidskader
kwaliteitsdoelen: [{id: id-…, sterkte: "++", onderbouwing: "De wet regelt de taak.", bronnen: [2026-rijk-…], vindplaats: art. 1}]   # beleidskader
gemma_generiek: {id: id-…, onderbouwing: "Een vergunningaanvraag."}
gemma_functie: {id: id-…, gemma_relatie: id-…}
specialisaties: [{naam: Bijzondere begraafplaats, omschrijving: "Van een kerkgenootschap of rechtspersoon (art. 24)."}]
relaties:
  - {soort: aggregatie, naar: graf, naam: bevat, ggm_match: geen, bronnen: [2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen], vindplaats: art. 1}
vragen: []                                    # open vragen aan de redacteur
besluiten: []                                 # alleen na een antwoord van de redacteur
```

De beschrijving van een beleidsdomein staat in het register `modellen/gemma/indelingen/beleidsdomeinen.yaml` (`beleidsdomein`, `taakveld`, `beschrijving`, `bronnen`), niet in een beoordeling of onderwerp. `tools/beslissen.py` controleert dat een element het beleidsdomein gebruikt en dat het taakveld klopt.
