---
id: README
type: doc
titel: 'Documentatie: waarom het model is zoals het is'
bijgewerkt: '2026-10-08'
---

# Documentatie: waarom het model is zoals het is

## Hoe deze map zich verhoudt

| Wat je zoekt | Waar |
|---|---|
| Wat geldt: de regels | [AGENTS.md](../AGENTS.md), met onderaan de kaart *Waar vind je wat* |
| Hoe de wiki werkt: mappen, scripts, statussen, export | [ARCHITECTURE.md](../ARCHITECTURE.md) |
| Hoe je het doet: stappen en sjablonen | de skills in `.agents/skills/` |
| Waarom het model is zoals het is | deze map, `docs/` |
| Wat de redacteur besliste | [Besluiten over de werkwijze](../besluiten/werkwijze.md) en [Besluiten per begrip](../besluiten/per-begrip.md) |

Een document in deze map is geen werkinstructie: wat de AI moet doen, staat in een regel of een skill. Eén uitzondering om te lezen: [Kenmerken en beslistabel](../kennismodel/kenmerken-en-beslistabel.md) is de gegenereerde, geldende beslistabel. Een document legt de vraag, de bronnen, de afweging, de afgewezen opties en de besluiten van de redacteur vast; de kolom Stand bij elk besluit zegt waar het nu als regel staat of door welk besluit het is herzien. Lees een document als een regel ter discussie staat of als je wilt weten waarom.

Tot 2026-10-08 heette deze map `analyses/`; oudere besluitteksten en commits noemen nog die naam. Wat bronnen zeggen die voor de hele wiki gelden (Over GEMMA, de GEMMA-procesarchitectuur), staat in de bronanalyses van het onderwerp Algemeen (`bronanalyses/algemeen/`).

## A Elementtypen en kenmerken

Wanneer is een begrip een element, en van welk type?

| Document | Vraag | Kern |
|---|---|---|
| [Kenmerken en beslistabel](../kennismodel/kenmerken-en-beslistabel.md) | Wat geldt nu: welke kenmerken beantwoord je, en welke uitkomst volgt eruit? | De geldende kenmerken en beslistabel, met voorbeelden en herkomst per kenmerk. Gegenereerd door `tools/kennismodel.py`, nooit met de hand bewerken; de vragenlijst staat ook in skill gemma-archimate-model-criteria. |
| [Elementtypen, kenmerken en het GEMMA-kennismodel](gemma-kennismodel.md) | Welke elementtypen en kenmerken, en hoe verhouden ze zich tot het GEMMA-kennismodel? | De wiki volgt de namen en definities van het kennismodel; per type één kernrelatie en een drempel. |
| [Kenmerken per elementtype](kenmerken.md) | Welke kenmerken bepalen per elementtype of een begrip een element is? | Per type de kenmerken, de kernrelatie en de drempel, getoetst op volledigheid. |
| [Toegang tot een bedrijfsobject](gegevensrollen.md) | Welke verantwoordelijkheid heeft een rol voor een object, en welke handeling voert een proces erop uit? | Een vaste reeks van acht verantwoordelijkheden en acht handelingen, uit de wetten van de basisregistraties, de AVG en de Archiefwet. |
| [Synoniemen en homoniemen](synoniemen-en-homoniemen.md) | Hoe gaat het model om met andere woorden voor hetzelfde begrip, en met dezelfde naam voor een ander begrip? | Stap 0 van de beslistabel: synoniem zonder pagina, homoniem met naamkeuze. |

## B Processen en indelingen

Hoe hangt het model samen?

| Document | Vraag | Kern |
|---|---|---|
| [Processen: niveaus, klant-tot-klant en ketensamenwerking](proceshierarchie.md) | Welke procesniveaus kent het model, wanneer is iets een bedrijfsproces, en hoe modelleren we een keten? | De GEMMA-ladder: levensloopproces per kernobject, bedrijfsproces van klant tot klant, deelproces zonder pagina; een estafette is een bedrijfsinteractie. |
| [Indelingen van de bedrijfsarchitectuur](indelingen.md) | Waar staat elk element in de indelingen van het model? | De GEMMA-indelingen blijven; nieuw zijn de Procesindeling naar kernobject en de indelingsvelden per type. |

## C Bronnen en grondslag

Waarop steunt een element?

| Document | Vraag | Kern |
|---|---|---|
| [Wettelijke grondslag](wettelijke-grondslag.md) | Waarop steunt een element, en wanneer blijft het zonder landelijke wettelijke grondslag? | Elk element heeft een landelijke wettelijke bron; alleen een product of dienst uit de UPL blijft zonder, met een terugmelding. |
