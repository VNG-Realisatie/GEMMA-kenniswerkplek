# gemma-archimate-model-wiki (curation)

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt. Dit bestand zegt hoe de AI werkt. Wat het model is (elementtypen, relaties, indelingen) en de regels voor het modelleren staan in het kennismodel (`kennismodel/`, met `kennismodel/modelleerregels.md`); hoe de wiki werkt (mappen, beoordelingen, scripts, render) in `ARCHITECTURE.md`, waarom het model is zoals het is in `docs/`, en hoe je het doet in de skills. Waar je wat vindt: de kaart onderaan.

## Domein

- Het GEMMA-architectuurmodel, bedrijfslaag: bedrijfsobjecten, contracten, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen en kanalen, plus beleidskaders (motivatielaag). Elk element wordt onderbouwd afgeleid uit bronnen en gematcht op het GGM en het GEMMA-model.
- Doelgroep: het GEMMA-team van VNG. Het resultaat voedt een landelijke standaard; kwaliteit en herleidbaarheid gaan voor snelheid.
- Taal: Nederlands; gevestigde ArchiMate-termen mogen Engels blijven.

## Standaard Workflow

Gebruik skill `gemma-archimate-model-update` voor elke inhoudelijke wijziging. De AI geeft het oordeel per begrip in een beoordeling (`beoordelingen/begrippen/<id>.yaml`); scripts leiden type en status af en maken alle pagina's (`tools/beslissen.py`, `tools/render.py`). Pagina's en overzichten worden nooit met de hand bewerkt. De redacteur beoordeelt de pagina's en geeft akkoord met het woord AKKOORD in de chat. Eerdere besluiten van de redacteur staan in `besluiten/per-begrip.md` (per begrip) en `besluiten/werkwijze.md` (over de werkwijze, met waar ze nu staan).

## Regels

Verwijs naar een regel met haar naam, bijvoorbeeld "regel Navragen". Achter een regel staat of een script haar controleert: *(schema)* en *(script)* houden een fout tegen, *(signaal)* geeft een waarschuwing die de AI inhoudelijk beoordeelt. Zonder markering is het een regel voor het oordeel van de AI.

Wat het render-script garandeert, is geen regel: bronverwijzingen als link naar de bronanalyse, relaties in beide richtingen, geen verwijzingen in de frontmatter, geen links naar tools of regels, de vorm van de pagina. De status zetten de scripts en het akkoord; de AI zet nooit een status.

Een regel is kort: de kern. Staat er meer bij een regel, dan noemt zij waar de uitwerking staat (hoe, in een skill) en de onderbouwing (waarom, in `docs/`).

### Werkwijze

- **Navragen** — Bij twijfel over een begrip, bron, naam of match: vraag het de redacteur, één vraag tegelijk, met context, argumenten en advies. Nooit gokken. Wat al in `besluiten/per-begrip.md` staat, vraag je niet opnieuw.
- **Eén naamgeving** — Noem brontypen, groepen en mappen precies zoals in de regel Bronvoorrang (`rijksregelgeving`, groep *Rijksregelgeving*; samen met `europese-regelgeving` heten ze landelijke regelgeving), in beoordelingen, analyses, terugmeldingen en de chat.
- **Bestaand bijwerken** — Bestaat een beoordeling al, werk haar dan bij. Neem niet aan wat erin hoort.
- **Per geval** — Een besluit (hernoemen, samenvoegen, afwijzen, herformuleren) nooit in bulk doorvoeren op grond van één eerder akkoord; leg elk geval apart voor.
- **Letterlijk verplaatsen** — Bij verplaatsen of splitsen de bestaande tekst ongewijzigd overnemen, tenzij de redacteur iets anders vraagt.

### Modelleren

De regels voor het modelleren staan in [kennismodel/modelleerregels.md](kennismodel/modelleerregels.md), met de voorrang: Bronvoorrang, Beslistabel beslist, Match op betekenis, Zwakke match voorleggen, Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen, Gemeentelijk perspectief, Tegenspraak, Wettelijke grondslag, Begrijpelijk, Los van het onderwerp, Naamvorm, Afwijken mits teruggemeld en Objectbehoud. Wat per elementtype geldt, staat in zijn modelleerafspraken ([kennismodel/README.md](kennismodel/README.md)).

### Bronnen

- **Elke claim een bron** — Elk kenmerk `ja`, elke relatie en elke bewering steunt op een bron; citaten letterlijk, met vindplaats. *(script: elk kenmerk `ja` en elk element heeft een bron; elke bron bestaat en heeft een bronanalyse)*
- **Zonder bron** — Een claim zonder bron wordt een open vraag ("verificatie nodig").

### Tekst

- **Geen absolute taal** — Geen "structureel buiten scope", "per definitie" of "het GGM modelleert nooit X" zonder concrete, domeinspecifieke reden; schrijf dan "in het GGM niet compleet gedekt". Een bewering met een concrete reden (ontbrekend beleidsdomein, wetsartikel, attribuutvergelijking) blijft staan. Beoordeel elk geval apart. *(signaal)*

### Terugmeldingen

- **Drie registers** — Een bevinding over het GGM, over de GEMMA-procesarchitectuur (UPL-lijsten, kennismodel) of over het GEMMA-model zelf gaat als terugmelding naar het register van die ontvanger: wat er nu staat, **Bevinding:** en **Voorstel:**, geschreven voor een lezer buiten de wiki. Uitwerking: skill gemma-archimate-model-beoordelen, `references/terugmeldingen.md`. *(script: een open melding zonder Bevinding of Voorstel)*
- **GEMMA-terugmeldingen formuleren** — Het wiki-model wordt in het GEMMA-model geïmporteerd: een wiki-element dat aan een GEMMA-element is gekoppeld, werkt dat element bij (naam, definitie, relaties, indeling). Formuleer een melding daarom als wat de import in GEMMA verandert en wat het GEMMA-team moet controleren of beslissen, niet als een verzoek om iets over te nemen. De import verwijdert niets: wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team besluit.

## Waar vind je wat

### Per soort

| Soort | Waar | Paginatype | Wie schrijft | Met de hand? |
|---|---|---|---|---|
| Werkwijze van de AI | dit bestand | — | de AI, na een besluit van de redacteur | ja |
| Wat het model is: elementtypen, relaties, indelingen | [kennismodel/](kennismodel/README.md), per type de modelleerafspraken | kennismodel | `tools/kennismodel.py` | nee |
| Regels voor het modelleren, met de voorrang | [kennismodel/modelleerregels.md](kennismodel/modelleerregels.md) | kennismodel | de AI, na een besluit van de redacteur | ja |
| Werkstroom: de stappen | skill `gemma-archimate-model-update` | — | — | ja |
| Criteria: is het een element, en welk type | skill `gemma-archimate-model-criteria`; [kennismodel/kenmerken-en-beslistabel.md](kennismodel/kenmerken-en-beslistabel.md) | kennismodel | de vragenlijst en de stappentabel: `tools/bepaal_type.py` | alleen de tekst buiten het gegenereerde blok van de skill |
| Werkinstructie per veld van een beoordeling | skill gemma-archimate-model-beoordelen en zijn `references/` | — | — | ja |
| Sjablonen | beoordeling: skill gemma-archimate-model-beoordelen §4; bronanalyse: skill gemma-archimate-model-ingest §4; terugmelding: `references/terugmeldingen.md`; besluit en voorleggen: `references/besluiten.md`; vorm: `schemas/` | — | — | ja |
| Oordeel per begrip | `beoordelingen/begrippen/<id>.yaml` | — | de AI; `status` en `beslist` de scripts | ja, behalve `status` en `beslist` |
| Registers | `beoordelingen/terugmeldingen/`, `objecten.yaml`, `beleidsdomeinen.yaml`, `besluiten-eerder.yaml`, `onderwerpen/` | — | de AI | ja |
| Wat een bron betekent | `bronanalyses/<onderwerp>/<brontype>/<bron-id>.md` | bronanalyse | de AI | ja |
| Waarom: onderbouwing | [docs/](docs/README.md) | doc | de AI | ja |
| Besluiten over de werkwijze (geschiedenis) | [besluiten/werkwijze.md](besluiten/werkwijze.md) en de besluitentabellen in `docs/` | doc | de AI | ja |
| Besluiten per begrip | [besluiten/per-begrip.md](besluiten/per-begrip.md) | lijst | `tools/render.py` | nee |
| Elementpagina's en overzichten | `bedrijfsarchitectuur/`, `motivatie/`, `begrippen/`, `overzichten/` | per elementtype | `tools/render.py` | nee |
| Terugmeldlijsten, ter beoordeling, voortgang | `terugmeldingen/`, [ter-beoordeling.md](ter-beoordeling.md), [voortgang.md](voortgang.md) | lijst | `tools/render.py` | nee |
| Open punten | [todo.md](todo.md) | — | de AI | ja |
| Plannen voor grotere wijzigingen (een plan dat klaar is, blijft als geschiedenis) | `plannen/<datum>-<titel>.md` | — | de AI, met de redacteur | ja |
| Akkoorden | [log.md](log.md) | — | `llmwiki promote apply` | nee |
| Controles | `tools/beslissen.py` (fout), `tools/signalen.py` (signaal) | — | — | — |

### Per regel

| Regel | Waar | Hoe (skill) | Waarom (docs, besluiten) | Controle |
|---|---|---|---|---|
| Navragen, Per geval | dit bestand | `references/besluiten.md` | `besluiten/werkwijze.md` | — |
| Eén naamgeving, Bestaand bijwerken, Letterlijk verplaatsen | dit bestand | — | — | — |
| Elke claim een bron, Zonder bron | dit bestand | skill gemma-archimate-model-ingest | — | script |
| Geen absolute taal | dit bestand | `references/definitie.md` | — | signaal |
| Drie registers, GEMMA-terugmeldingen formuleren | dit bestand | `references/terugmeldingen.md` | `docs/wettelijke-grondslag.md` (besluit 4 en 15) | script |
| Bronvoorrang, Tegenspraak, Wettelijke grondslag | modelleerregels | skill gemma-archimate-model-ingest; `references/grondslag.md` | `docs/wettelijke-grondslag.md` | script, signaal |
| Beslistabel beslist | modelleerregels | skill gemma-archimate-model-criteria | `docs/kenmerken.md`, `docs/gemma-kennismodel.md`, `docs/proceshierarchie.md`, `docs/indelingen.md` | script, signaal |
| Match op betekenis, Zwakke match voorleggen | modelleerregels | `references/ggm-match.md`, `references/gemma-match.md` | `docs/synoniemen-en-homoniemen.md` | script, signaal |
| Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen | modelleerregels | `references/relaties.md` | `besluiten/werkwijze.md`, thema 3 | signaal |
| Gemeentelijk perspectief | modelleerregels | `references/relaties.md` | `docs/gegevensrollen.md` | — |
| Begrijpelijk, Los van het onderwerp, Naamvorm | modelleerregels; de naamvorm per type in de modelleerafspraken | `references/definitie.md`, `references/naamgeving.md` | — | signaal |
| Afwijken mits teruggemeld | modelleerregels | `references/terugmeldingen.md` | `docs/wettelijke-grondslag.md` (besluit 4 en 15) | signaal |
| Objectbehoud | modelleerregels | skill gemma-archimate-model-archimate-export | `besluiten/werkwijze.md`, thema 6 | script |

De `references/` in deze tabel zijn die van skill gemma-archimate-model-beoordelen.
