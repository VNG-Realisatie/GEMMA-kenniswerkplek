# gemma-archimate-model-wiki (curation)

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de
Context staan: lees dat bestand voordat je iets wijzigt. De opzet van deze wiki (mappen,
paginatypen, vaardigheden, gereedschap) staat in `ARCHITECTURE.md`.

## Domein

- Het GEMMA-architectuurmodel, bedrijfslaag: bedrijfsobjecten, contracten, producten,
  diensten, processen, functies, gebeurtenissen, actoren en rollen. Elk element wordt
  onderbouwd afgeleid uit bronnen en gematcht op het GGM en het GEMMA-model.
- Doelgroep: het GEMMA-team van VNG. Het resultaat voedt een landelijke standaard;
  kwaliteit en herleidbaarheid gaan voor snelheid.
- Taal: Nederlands; gevestigde ArchiMate-termen mogen Engels blijven.

## Standaard Workflow

Gebruik skill `gemma-archimate-model-update` voor elke inhoudelijke wijziging. Die volgt
`wiki-update` (INGEST → ASSESS → WRITE → VALIDATE → GATE → PROMOTE) met de uitbreidingen
van deze wiki. Of een begrip een element is, bepaalt skill `gemma-archimate-model-criteria`
samen met `tools/bepaal_type.py`, nooit een losse inschatting.

## Regels

Schrijfwijze: `[ID] **kern** — regel`. `ALTIJD` = verplicht, `NOOIT` = verboden,
`ALS … →` = voorwaardelijk, `UITZONDERING:` = afwijking.

### Werkwijze

- [PR6] **Navragen** — ALS onduidelijk is hoe een begrip of bron behandeld moet worden → vraag het de redacteur; NOOIT gokken.
- [PR7] **Bestaande pagina's** — ALS een pagina al bestaat → werk haar bij; neem niet aan wat erin hoort, vraag eerst.
- [EL9] **Geen bulkbesluiten** — NOOIT een besluit (hernoemen, samenvoegen, afwijzen) in bulk doorvoeren op grond van één eerder akkoord; leg elk geval apart voor.
- [W1] **Tekst verplaatsen** — ALS de opdracht "verplaats" of "splits" is → exacte bestaande tekst knippen en plakken; NOOIT herformuleren of inkorten, tenzij de redacteur dat vraagt.

### Inhoud en herleidbaarheid

- [IH1] **Elke claim heeft een bron** — ALTIJD een bron-id in `bronnen:`; citaten als blockquote met bronvermelding.
- [IH3] **Tegenspraak** — ALS bronnen elkaar tegenspreken → beide vastleggen en markeren met `⚠️ Tegenspraak`.
- [IH4] **Zonder bron** — ALS een claim geen bron heeft → markeren met `🔍 Verificatie nodig` en als open vraag opnemen.
- [IH6] **Onzekerheid** — ALS een keuze niet eenduidig is (match, mapping, naam, type) → status `kandidaat` en een sectie `## Ter discussie`; elke aanname vastleggen.
- [VR2] **Begrijpelijk Nederlands** — ALTIJD herkenbaar voor domeinexperts; geen jargon tenzij nodig.

### Bronnen en modellen

- [SRC1] **GGM en GEMMA alleen via de tools** — Het GGM-XMI en het GEMMA-model (AMEFF of `.archimate`) NOOIT direct lezen; ALLEEN via `tools/ggm.py` en `tools/gemma.py`.
- [SRC3] **Geen afgeleide modelbronnen** — NOOIT CSV-exports of kopieën elders als GGM- of GEMMA-bron gebruiken.
- [SRC5] **Gegenereerde modelmappen** — `ggm/` en `gemma/` ALLEEN om te lezen; NOOIT handmatig bewerken (de check herkent wijzigingen).
- [SRC10] **Bronvoorrang** — Voor begrippen en formele betekenis: wet > informatiemodel > beleid > overig (`wiki.yaml` `bronvoorrang`). Beleid levert de gangbare taal. Voorrang bepaalt NOOIT of iets een element is.

### Elementen

- [EL1] **Alleen de beslistabel** — Of een begrip een element is en van welk type, volgt ALLEEN uit de kenmerken en de beslistabel (skill `gemma-archimate-model-criteria`). NOOIT registr*, eigendom, systeembeheer, regie of extern systeem als argument.
- [EL12] **Veldprefixen** — Zonder prefix = eigen veld van de wiki; `ggm_` = letterlijk uit het GGM; `gemma_` = letterlijk uit het GEMMA-model na een match. `ggm_`- en `gemma_`-velden ALLEEN laten vullen door `tools/ggm.py` en `tools/gemma.py`; NOOIT zelf invullen of aanpassen.
- [EL17] **Verwijzingen als link** — NOOIT verwijzingen naar andere elementen in de frontmatter; ALTIJD als relatieve link in de body (relaties, specialisaties, tegenhanger, homoniemen), zodat backlinks zichtbaar zijn.
- [EL18] **Status** — De AI zet een element ALLEEN op `review` bij een uitkomst van de beslistabel zonder conflict of "voorleggen" (en bij `data_object: ja` een GGM-match exact of sterk); anders `kandidaat`. NOOIT `goedgekeurd`.

### Scope en formulering

- [WC4] **Gemeentelijk perspectief** — ALTIJD vanuit wat de gemeente ziet, doet en beslist. Een externe partij krijgt ALLEEN een actorpagina bij directe samenwerking; haar interne processen blijven buiten scope ([WC5]).
- [WC7] **Geen technische verwijzingen** — NOOIT vanuit een pagina verwijzen naar `AGENTS.md`, `ARCHITECTURE.md`, `.agents/`, `tools/` of `schemas/`; onderbouwing staat op eigen kracht.
- [WC8] **Geen absolute taal** — NOOIT "structureel buiten scope", "per definitie" of "het GGM modelleert nooit X" zonder domeinspecifieke reden.
- [WC9] **Herformuleren** — ALS een bewering "het GGM doet dit niet" geen specifieke reden heeft → "in het GGM niet compleet gedekt".
- [WC10] **Concrete reden blijft** — ALS een bewering een concrete reden geeft (ontbrekend beleidsdomein, wetsartikel, attribuutvergelijking) → NIET aanpassen.
- [WC11] **Per geval** — NOOIT dit soort formuleringen in bulk vervangen; per geval beoordelen.
