# gemma-archimate-model-wiki (curation)

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt. De opzet van deze wiki (mappen, beoordelingen, scripts, render) staat in `ARCHITECTURE.md`.

## Domein

- Het GEMMA-architectuurmodel, bedrijfslaag: bedrijfsobjecten, contracten, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen en kanalen, plus beleidskaders (motivatielaag). Elk element wordt onderbouwd afgeleid uit bronnen en gematcht op het GGM en het GEMMA-model.
- Doelgroep: het GEMMA-team van VNG. Het resultaat voedt een landelijke standaard; kwaliteit en herleidbaarheid gaan voor snelheid.
- Taal: Nederlands; gevestigde ArchiMate-termen mogen Engels blijven.

## Standaard Workflow

Gebruik skill `gemma-archimate-model-update` voor elke inhoudelijke wijziging. De AI geeft het oordeel per begrip in een beoordeling (`beoordelingen/begrippen/<id>.yaml`); scripts leiden type en status af en maken alle pagina's (`tools/afleiden.py`, `tools/render.py`). Pagina's en overzichten worden nooit met de hand bewerkt. De redacteur beoordeelt de pagina's en geeft akkoord met het woord AKKOORD in de chat. Eerdere besluiten van de redacteur staan in `analyses/besluiten-redacteur.md`.

## Regels

Verwijs naar een regel met haar naam, bijvoorbeeld "regel Navragen". Achter een regel staat of een script haar controleert: *(schema)* en *(script)* houden een fout tegen, *(signaal)* geeft een waarschuwing die de AI inhoudelijk beoordeelt. Zonder markering is het een regel voor het oordeel van de AI.

Wat het render-script garandeert, is geen regel: bronverwijzingen als link naar de bronanalyse, relaties in beide richtingen, geen verwijzingen in de frontmatter, geen links naar tools of regels, de vorm van de pagina. De status zetten de scripts en het akkoord; de AI zet nooit een status.

### Werkwijze

- **Navragen** — Bij twijfel over een begrip, bron, naam of match: vraag het de redacteur, één vraag tegelijk, met context, argumenten en advies. Nooit gokken. Wat al in `analyses/besluiten-redacteur.md` staat, vraag je niet opnieuw.
- **Bestaand bijwerken** — Bestaat een beoordeling al, werk haar dan bij. Neem niet aan wat erin hoort.
- **Per geval** — Een besluit (hernoemen, samenvoegen, afwijzen, herformuleren) nooit in bulk doorvoeren op grond van één eerder akkoord; leg elk geval apart voor.
- **Letterlijk verplaatsen** — Bij verplaatsen of splitsen de bestaande tekst ongewijzigd overnemen, tenzij de redacteur iets anders vraagt.
- **Objectbehoud** — Hernoemen, samenvoegen of splitsen van een element leidt niet vanzelf tot een nieuw object in Archi: de redacteur gebruikt de objecten in views, en de export werkt views niet bij. Leg in `beoordelingen/objecten.yaml` vast welk bestaand object het element voortzet. Bij hernoemen altijd; bij samenvoegen vraag je de redacteur of en welk object blijft; bij splitsen of er een object blijft en welk deel het krijgt. *(script: het register klopt; de export weigert een typewijziging van een voortgezet object)*

### Oordeel

- **Beslistabel beslist** — Of een begrip een element is en van welk type, volgt alleen uit de kenmerken en de beslistabel (skill `gemma-archimate-model-criteria`). Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument. *(script; signaal bij registr*-taal)*
- **Match op betekenis** — Match met GGM en GEMMA op betekenis, niet op naam: herken homoniemen en synoniemen en volg relaties en generalisaties. Lees de modellen alleen via `tools/ggm.py` en `tools/gemma.py`, nooit direct en nooit via kopieën of CSV-exports. *(script: de gekozen match moet bestaan; signaal bij een afwijkende modelnaam)*
- **Zwakke match voorleggen** — Een GEMMA-match met sterkte `zwak` of `partieel` leg je altijd voor aan de redacteur, met wat er in GEMMA verandert: de export naar Archi (skill `gemma-archimate-model-archimate-export`) neemt het GEMMA-id over en overschrijft naam en definitie van dat GEMMA-element. Matchen is de verantwoordelijkheid van de wiki en de redacteur; de export en Archi vertrouwen de match. Past het GEMMA-element niet echt, kies dan `sterkte: geen` en noem het in de onderbouwing.
- **Gemeentelijk perspectief** — Beschrijf wat de gemeente ziet, doet en beslist. Een externe partij wordt alleen een element bij een structurele relatie met de gemeente (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht); een partij die alleen als context in de bron staat, noem je in de beschrijving. Precedent: GGD wel.

### Bronnen

- **Elke claim een bron** — Elk kenmerk `ja`, elke relatie en elke bewering steunt op een bron; citaten letterlijk, met vindplaats. *(script: elk kenmerk `ja` en elk element heeft een bron; elke bron bestaat en heeft een bronanalyse)*
- **Zonder bron** — Een claim zonder bron wordt een open vraag ("verificatie nodig").
- **Tegenspraak** — Spreken bronnen elkaar tegen, leg dan beide vast en markeer de tegenspraak.
- **Bronvoorrang** — Voor welke begrippen er zijn en wat ze formeel betekenen: wet, dan informatiemodel, dan beleid, dan overig (`wiki.yaml` `bronvoorrang`). Voorrang bepaalt nooit of iets een element is. De naam en de herkenbare definitie komen uit de gangbare taal van beleids- en praktijkbronnen; de wetsterm wordt een synoniem met context "wet". Precedent: Urn, niet Asbus. *(signaal)*

### Tekst

- **Begrijpelijk** — Herkenbaar voor domeinexperts; geen jargon tenzij nodig. De definitie is één zin. *(signaal)*
- **Los van het onderwerp** — Definitie en beschrijving gelden in elk onderwerp; toets: past de tekst ongewijzigd in elk ander onderwerp? Wat een element in één onderwerp doet, staat onder `per_onderwerp`. *(signaal)*
- **Naamvorm** — Een proces is een infinitief met object in GEMMA-volgorde ("Behandelen aanvraag"), een functie een zelfstandig naamwoord voor het gebied van gedrag ("Vergunningverlening"), een gebeurtenis een voltooide verandering ("Overlijden"), een dienst geformuleerd vanuit de afnemer ("Melding openbare ruimte doen"). Het zelfstandig naamwoord uit de bron wordt een synoniem met context "beleid". Een product of dienst uit de UPL krijgt de UPL-naam letterlijk ("Verlof tot begraven"), met een synoniem waar dat betekenis toevoegt (besluit redacteur 2026-10-05). *(signaal)*
- **Geen absolute taal** — Geen "structureel buiten scope", "per definitie" of "het GGM modelleert nooit X" zonder concrete, domeinspecifieke reden; schrijf dan "in het GGM niet compleet gedekt". Een bewering met een concrete reden (ontbrekend beleidsdomein, wetsartikel, attribuutvergelijking) blijft staan. Beoordeel elk geval apart. *(signaal)*
