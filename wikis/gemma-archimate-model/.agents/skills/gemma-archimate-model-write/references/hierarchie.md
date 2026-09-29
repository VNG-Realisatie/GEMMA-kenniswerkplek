# Hiërarchie: generalisatie, specialisaties, GGM-componenten

## Specialisaties (neerwaarts)

Welk niveau een eigen pagina krijgt, volgt uit ASSESS (`gemma-archimate-model-assess` §3, *het hoogste herkenbare niveau*) en de uitkomst van de beslistabel (stap 5). Een specialisatie krijgt ALLEEN een eigen pagina als domeinexperts de term zelf gebruiken, ze eigen gegevens of een eigen levenscyclus heeft (niet alleen een eigen wetsartikel) en GEMMA vergelijkbare specialisaties op dat niveau kent. Anders is ze een specialisatie zonder pagina van het bredere element, met omschrijving en vindplaats.

Eén sectie `## Specialisaties` voor alle specialisaties, met of zonder eigen pagina:

```markdown
## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit | GGM-guid | GGM-attribuut |
|---|---|---|---|---|
| [Sportpark](../../5-sport/sport/sportpark.md) | Heeft een eigen pagina | Sportpark | EAID_… | |
| Sociale huurwoning | Geen eigen pagina: uitwisselbaar, zelfde processen | Huurwoningen | EAID_… | typeWoning |
```

- **Met eigen pagina** (de specialisatie is zelf een element): de cel is een link; de specialisatie heeft in haar eigen `## Relaties` een rij `specialisatie` naar dit element. Dit element legt die relatie niet vast.
- **Zonder eigen pagina**: platte tekst met een omschrijving; vul `GGM-guid` als het GGM de specialisatie als aparte entiteit kent (dan tilt `tools/relaties.py` haar GGM-relaties op naar dit element), of `GGM-attribuut` als het GGM haar als attribuutwaarde draagt.
- Bronnen voor specialisaties zonder pagina: typen of categorieën die de bronnen apart noemen met eigen kenmerken (levensduur, regime, aanpak); besluiten, vergunningen of processen die de wet per artikel onderscheidt maar die varianten zijn van een breder begrip (bijv. Vergunning tot opgraving bij een vergunning); GGM-attributen als `type`, `soort`, `materiaal`; GGM-generalisaties. De GGM-hiërarchie kan afwijken van het beleidsperspectief (bijv. Brug onder Overbruggingsobject): documenteer dat.
- Twee onafhankelijke indelingen (bijv. Woning naar marktsegment én naar bouwvorm): subkoppen `### Naar <as>`, elk met een tabel.

## Generalisatie (opwaarts)

`## Generalisatie` als dit element deel is van een reeks elementen met dezelfde structuur (bijv. Gemeente → Woonplaats → Wijk → Buurt): de keten met links, wat alle niveaus delen en wat dit niveau onderscheidt. De relaties tussen de niveaus staan als rijen in `## Relaties` (aggregatie, compositie of associatie).

## GGM-componenten

GGM-entiteiten die deel zijn van dit element maar zelf geen element (procesfasen, deelregistraties):

```markdown
## GGM-componenten

| Component | GGM-guid | Toelichting |
|---|---|---|
| Loopbaanstap | EAID_… | Stap binnen de onderwijsloopbaan; geen zelfstandig begrip |
```

`tools/relaties.py` tilt de GGM-relaties van componenten op naar dit element.
