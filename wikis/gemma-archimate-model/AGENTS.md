# gemma-archimate-model-wiki (curation)

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt. Dit bestand zegt hoe de AI werkt. Wat het model is (elementtypen, relaties, indelingen) en de regels voor het modelleren staan in het kennismodel (`kennismodel/`, met `kennismodel/modelleerregels.md`); waarom het model is zoals het is en hoe de wiki werkt (mappen, beoordelingen, scripts, render) in `ARCHITECTURE.md`, dat leidend is; hoe je het doet in de skills. Waar je wat vindt: de kaart onderaan.

## Domein

- Het GEMMA-architectuurmodel, bedrijfslaag: bedrijfsobjecten, afspraken, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen, kanalen en bedrijfsinteracties, plus beleidskaders (motivatielaag). Elk element wordt onderbouwd met bronnen en gematcht op de matchdoelen (ARCHITECTURE.md, sectie 2).
- Doelgroep: het GEMMA-team van VNG. Het resultaat voedt een landelijke standaard; kwaliteit en herleidbaarheid gaan voor snelheid.
- Taal: Nederlands; gevestigde ArchiMate-termen mogen Engels blijven.

## Standaard Workflow

Gebruik skill `gemma-archimate-model-update` voor elke inhoudelijke wijziging. De AI geeft het oordeel per begrip in een beoordeling (`onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml`); scripts beslissen type en status en maken alle pagina's (`tools/beslissen.py`, `tools/render.py`). Pagina's en overzichten worden nooit met de hand bewerkt. De redacteur beoordeelt de pagina's en geeft akkoord met het woord AKKOORD in de chat. Besluiten van de redacteur over een begrip staan in de `besluiten:` van zijn beoordeling, over een onderwerp als geheel in de `besluiten:` van het onderwerp; besluiten over de werkwijze staan in de regel of skill waar ze gelden.

## Regels

Verwijs naar een regel met haar naam, bijvoorbeeld "regel Navragen". Achter een regel staat of een script haar controleert: *(schema)* en *(script)* houden een fout tegen, *(signaal)* geeft een waarschuwing die de AI inhoudelijk beoordeelt. Zonder markering is het een regel voor het oordeel van de AI.

Wat het render-script garandeert, is geen regel: bronverwijzingen als link naar de bronduiding, relaties in beide richtingen, één toegangsrelatie per paar elementen (zoals in de export), geen verwijzingen in de frontmatter, geen links naar tools of regels, de vorm van de pagina. De status zetten de scripts en het akkoord; de AI zet nooit een status.

Een regel is kort: de kern. Staat er meer bij een regel, dan noemt zij waar de uitwerking staat (hoe, in een skill) en de onderbouwing (waarom, in `ARCHITECTURE.md`).

### Werkwijze

- **Navragen** — Bij twijfel over een begrip, bron, naam of match: vraag het de redacteur, met context, argumenten en advies. Nooit gokken. Wat al besloten is (de `besluiten:` van de beoordeling en van het onderwerp), vraag je naar zijn zekerheid opnieuw: `kennis` nooit, `logica` als nieuwe informatie de redenering raakt, `indruk` in fase 3 altijd.
- **Eén naamgeving** — Noem brontypen, groepen en mappen precies zoals in de regel Bronvoorrang (`rijksregelgeving`, groep *Rijksregelgeving*; samen met `europese-regelgeving` heten ze landelijke regelgeving), in beoordelingen, analyses, terugmeldingen en de chat. Een modelverordening van de VNG heet een VNG-modelverordening, nooit VNG-model: dat is te verwarren met het GEMMA-model en andere modellen.
- **Bestaand bijwerken** — Bestaat een beoordeling al, werk haar dan bij. Neem niet aan wat erin hoort.
- **Per geval** — Een besluit (hernoemen, samenvoegen, afwijzen, herformuleren) nooit in bulk doorvoeren op grond van één eerder akkoord; leg elk geval apart voor.
- **Letterlijk verplaatsen** — Bij verplaatsen of splitsen de bestaande tekst ongewijzigd overnemen, tenzij de redacteur iets anders vraagt.

### Modelleren

De regels voor het modelleren staan in [kennismodel/modelleerregels.md](kennismodel/modelleerregels.md), met de voorrang: Bronvoorrang, Beslistabel beslist, Match op betekenis, Zwakke match voorleggen, Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen, Gemeentelijk perspectief, Tegenspraak, Wettelijke grondslag, Begrijpelijk, Los van het onderwerp, Naamvorm, Afwijken mits teruggemeld en Objectbehoud. Wat per elementtype geldt, staat in zijn modelleerafspraken ([kennismodel/README.md](kennismodel/README.md)).

### Bronnen

- **Elke claim een bron** — Elk kenmerk `ja`, elke relatie en elke bewering steunt op een bron voor de inhoud; citaten letterlijk, met vindplaats. Een matchdoel (het GEMMA-model, GEMMA Online, het GGM) is nooit die bron. Een doorlopen poort steunt op de bronnen van de beoordeling, een relationeel kenmerk op die van zijn relatie (`naar`). Eén uitzondering: de plek van een element in een overgenomen indeling (de kenmerken *in functie-indeling* en *zelfstandige specialisatie*, en een relatie in de GEMMA-functieketen tussen twee gematchte elementen) steunt op de relatie uit het model (`gemma_relatie`), want de wiki neemt die indeling letterlijk over. Ook uitgezonderd: *beoordeelbaar* en *onderscheidend* van een capability steunen op een landelijke `richtlijn` of op een oordeel met onderbouwing. *(script: elk kenmerk `ja` en elk element heeft een bron, een GEMMA-relatie of een relatie (`naar`) (ook de plek onder een GEMMA-functie zonder beoordeling, `gemma_functie`); elke bron bestaat en heeft een bronduiding; een GEMMA-relatie staat in het model tussen de gematchte elementen; elk citaat in een bronduiding staat letterlijk in de bron)*
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
| Werkstroom: de stappen in drie fasen, met wat je per fase leest en de opdracht voor de beoordelingsagent | skill `gemma-archimate-model-update` | — | — | ja |
| Criteria: is het een element, en welk type (fase A) | skill `gemma-archimate-model-criteria`; de vragen per fase: `tools/bepaal_type.py vragen`; de volledige vragenlijst en de stappentabel: [kennismodel/kenmerken-en-beslistabel.md](kennismodel/kenmerken-en-beslistabel.md) | kennismodel | de vragen en de stappentabel: `tools/bepaal_type.py` | de skill ja; de vragen en de stappentabel nee |
| Werkinstructie per veld van een beoordeling (fase B) | skill gemma-archimate-model-beoordelen en zijn `references/` | — | — | ja |
| Sjablonen | patroon (UPL-dienst met proces en kernobject): `tools/beoordeling.py sjabloon`, skill gemma-archimate-model-beoordelen; beoordeling: skill gemma-archimate-model-criteria, stap 5 (fase A), en skill gemma-archimate-model-beoordelen, Velden (fase B); bronduiding: skill gemma-archimate-model-ingest §4, citaten met `tools/bronduiding.py`; terugmelding: `references/terugmeldingen.md`; besluit en voorleggen: `references/besluiten.md`; vorm: `schemas/` | — | — | ja |
| Oordeel per begrip | `onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml` | — | de AI; `status` en `beslist.yaml` de scripts | ja, behalve `status` |
| Registers | `onderwerpen/<onderwerp>/afbakening.yaml`, `modellen/*/terugmeldingen`, `modellen/gemma/indelingen/beleidsdomeinen.yaml` | — | de AI | ja |
| Wat een bron betekent | `onderwerpen/<onderwerp>/bronduidingen/<brontype>/<bron-id>.md`, of `modellen/<model>/bronduidingen/<brontype>/<bron-id>.md` voor een bron van een model | bronduiding | de AI | ja |
| Waarom: uitgangspunten en onderbouwing | [ARCHITECTURE.md](ARCHITECTURE.md) | — | de AI, na een besluit van de redacteur | ja |
| Besluiten over een begrip of onderwerp | `besluiten:` van de beoordeling of het onderwerp; de begrippenlijst toont die van het onderwerp | — | de AI, met de redacteur | ja |
| Elementpagina's en overzichten | `elementpaginas/`, `onderwerpen/<onderwerp>/begrippen.md` en `overzicht.md` | per elementtype | `tools/render.py` | nee |
| Indelingspagina's: de indelingen as-is met dekking (onderwerpen, beleidsdomeinen, bedrijfsfuncties, capabilities) | `elementpaginas/overig/indelingen/` | indeling | `tools/render.py` (met `tools/indelingspaginas.py`) | nee |
| Terugmeldlijsten, diensten zonder grondslag, ter beoordeling, voortgang | `modellen/*/terugmeldingen/*.md`, `elementpaginas/overig/zonder-grondslag.md`, [ter-beoordeling.md](ter-beoordeling.md), [voortgang.md](voortgang.md) | lijst | `tools/render.py` | nee |
| Open punten | [todo.md](todo.md) (actief), [todo-later.md](todo-later.md) (later) | — | de AI | ja |
| Plannen voor grotere wijzigingen (een plan dat klaar is, blijft als geschiedenis) | `plannen/<datum>-<titel>.md` | — | de AI, met de redacteur | ja |
| Akkoorden | [log.md](log.md) | — | `llmwiki promote apply` | nee |
| Controles | `tools/beslissen.py` (fout), `tools/signalen.py` (signaal) | — | — | — |
| Afronden na het akkoord | `tools/afronden.py` (skill gemma-archimate-model-update, stap 16 en 17) | — | — | — |

### Per regel

| Regel | Waar | Hoe (skill) | Waarom (ARCHITECTURE.md) | Controle |
|---|---|---|---|---|
| Navragen, Per geval | dit bestand | `references/besluiten.md` | secties 3.1 en 3.2 | — |
| Eén naamgeving, Bestaand bijwerken, Letterlijk verplaatsen | dit bestand | — | — | — |
| Elke claim een bron, Zonder bron | dit bestand | skill gemma-archimate-model-ingest; `gemma_relatie` en `gemma_functie`: `references/gemma-match.md` | secties 3.1 en 4.4 | script |
| Geen absolute taal | dit bestand | `references/definitie.md` | — | signaal |
| Drie registers, GEMMA-terugmeldingen formuleren | dit bestand | `references/terugmeldingen.md` | secties 2 en 3.5 | script |
| Bronvoorrang, Tegenspraak, Wettelijke grondslag | modelleerregels | skill gemma-archimate-model-ingest; de hoek zonder grondslag: `references/terugmeldingen.md` | secties 2, 3.4, 3.7, 4.2 en 6.3 | script, signaal |
| Beslistabel beslist | modelleerregels | skill gemma-archimate-model-criteria | secties 4.1, 4.3 en 4.4 | script, signaal |
| Match op betekenis, Zwakke match voorleggen | modelleerregels | `references/ggm-match.md`, `references/gemma-match.md` | secties 3.7, 4.5 en 6.4 | script, signaal |
| Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen | modelleerregels | `references/relaties.md` | sectie 3.3 | signaal |
| Gemeentelijk perspectief | modelleerregels | `references/relaties.md` | sectie 4.2 | — |
| Begrijpelijk, Los van het onderwerp, Naamvorm | modelleerregels; de naamvorm per type in de modelleerafspraken | `references/definitie.md`, `references/naamgeving.md` | — | signaal |
| Afwijken mits teruggemeld | modelleerregels | `references/terugmeldingen.md` | sectie 3.5 | signaal |
| Objectbehoud | modelleerregels | skill gemma-archimate-model-archimate-export | sectie 6.5 | script |

De `references/` in deze tabel zijn die van skill gemma-archimate-model-beoordelen.
