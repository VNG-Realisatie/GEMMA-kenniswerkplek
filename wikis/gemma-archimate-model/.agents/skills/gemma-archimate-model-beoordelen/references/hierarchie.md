# Hiërarchie: generalisatie, specialisaties, GGM-componenten

## Specialisaties (neerwaarts)

Welk niveau een eigen element wordt, volgt uit het hoogste herkenbare niveau (SKILL.md §3) en de beslistabel (stap 6, *zelfstandige specialisatie*). Een specialisatie wordt alleen een eigen element als domeinexperts de term zelf gebruiken, ze eigen gegevens of een eigen levenscyclus heeft (niet alleen een eigen wetsartikel) en GEMMA vergelijkbare specialisaties op dat niveau kent. Anders is ze een specialisatie zonder pagina van het bredere element.

Alle specialisaties, met of zonder eigen element, staan in `specialisaties` van het bredere element:

```yaml
specialisaties:
  - {naam: Sportpark, omschrijving: "Heeft een eigen pagina.", element: sportpark}
  - {naam: Sociale huurwoning, omschrijving: "Geen eigen pagina: uitwisselbaar, zelfde processen.", ggm_guid: EAID_…, ggm_attribuut: typeWoning}
```

- **Met eigen element**: `element` is het id; dat element heeft zelf een relatie `specialisatie` naar het bredere element.
- **Zonder eigen element**: een omschrijving met vindplaats; `ggm_guid` als het GGM de specialisatie als aparte entiteit kent (dan tilt `tools/relaties.py` haar GGM-relaties op naar het bredere element), of `ggm_attribuut` als het GGM haar als attribuutwaarde draagt.
- Bronnen voor specialisaties zonder pagina: typen of categorieën die de bronnen apart noemen; besluiten, vergunningen of processen die de wet per artikel onderscheidt maar die varianten zijn van een breder begrip (bijv. Vergunning tot opgraving bij Vergunning); GGM-attributen als `type`, `soort`, `materiaal`; GGM-generalisaties. Wijkt de GGM-hiërarchie af van het beleidsperspectief, zeg dat in de omschrijving.

Precedent: bij lijkbezorging (2026-09-29) leverden vier soorten vergunningen eerst vier bedrijfsobjecten op en processen als "afgeven verlof tot begraving of crematie" eigen pagina's. Dat is te specifiek voor GEMMA: het zijn varianten van Vergunning en van het behandelen van een vergunningaanvraag.

## Generalisatie (opwaarts)

`generalisatie` (alinea's) als dit element deel is van een reeks met dezelfde structuur (bijv. Gemeente → Woonplaats → Wijk → Buurt): de keten, wat alle niveaus delen en wat dit niveau onderscheidt. De relaties tussen de niveaus staan in `relaties`.

## GGM-componenten

GGM-entiteiten die deel zijn van dit element maar zelf geen element (procesfasen, deelregistraties):

```yaml
ggm_componenten:
  - {naam: Loopbaanstap, guid: EAID_…, toelichting: "Stap binnen de onderwijsloopbaan; geen zelfstandig begrip."}
```

`tools/relaties.py` tilt de GGM-relaties van componenten op naar dit element.
