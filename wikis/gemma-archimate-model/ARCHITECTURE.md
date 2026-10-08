# Architectuur van de wiki gemma-archimate-model

Deze wiki bouwt het GEMMA-architectuurmodel voor de bedrijfslaag onderbouwd opnieuw op: bedrijfsobjecten, contracten, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen, kanalen en beleidskaders. Elk element is herleidbaar tot bronnen, gematcht op het GGM en op het huidige GEMMA-model, en pas na akkoord van een redacteur vastgesteld. Het is een wiki van het type `curation` (zie de `ARCHITECTURE.md` van de repository voor de algemene opzet). De regels staan in [AGENTS.md](AGENTS.md); dit document legt uit hoe alles samenhangt.

## 1. Plaats in de keten

```text
wetten, informatiemodellen, beleid (sources/)  ─┐
GGM-XMI (sources/, via tools/ggm.py)           ─┼─►  deze wiki  ─►  export naar Archi (.archimate) ─► GEMMA-model
GEMMA-model (sources/, via tools/gemma.py)     ─┘
```

Het GGM is zowel bron (kandidaat-begrippen, definities, relaties) als toets. Het GEMMA-model is alleen matchdoel: het laat zien hoe een element nu in GEMMA staat. Terugschrijven gaat via een `.archimate` met de id's van GEMMA (§12).

## 2. Zacht oordeel, harde vorm

| | Wie | Waar |
|---|---|---|
| **Oordeel** per begrip: kenmerken met onderbouwing en bron, naam, definitie, beschrijving, tekst per onderwerp, GGM- en GEMMA-match op betekenis, relaties, hiërarchie, open vragen | AI | `beoordelingen/begrippen/<id>.yaml` |
| **Besluiten** van de redacteur over een voorgelegd punt | redacteur, vastgelegd door de AI | `besluiten:` in de beoordeling; eerdere besluiten in [analyses/besluiten-redacteur.md](analyses/besluiten-redacteur.md) |
| **Afleiding**: type uit de beslistabel, status, letterlijke GGM- en GEMMA-velden, paginapad, herkomst, nummers van terugmeldingen; harde controles en signalen | [tools/afleiden.py](tools/afleiden.py), [tools/signalen.py](tools/signalen.py) | `status:` en `afgeleid:` in de beoordeling |
| **Vorm**: alle leesbare pagina's en overzichten | [tools/render.py](tools/render.py) | zie §4 |
| **Akkoord** | redacteur, met het woord AKKOORD in de chat | `llmwiki promote plan/apply`, `log.md` |

De AI schrijft dus geen pagina's, geen links en geen statussen. Wat het render-script garandeert, hoeft geen regel te zijn; wat het schema of het afleid-script tegenhoudt, ook niet. De regels in [AGENTS.md](AGENTS.md) gaan over het oordeel.

## 3. Plattegrond

```text
wikis/gemma-archimate-model/
├── AGENTS.md · ARCHITECTURE.md · wiki.yaml · todo.md · log.md
├── beoordelingen/
│   ├── begrippen/<id>.yaml           het oordeel per begrip (AI); status en afgeleid (scripts)
│   ├── onderwerpen/<onderwerp>.yaml  naam, omschrijving, bronnen en status van een onderwerp
│   ├── terugmeldingen.yaml           register van GGM-terugmeldingen
│   ├── procesarchitectuur-terugmeldingen.yaml   register van terugmeldingen aan de GEMMA-procesarchitectuur
│   ├── objecten.yaml                 welk Archi-object een hernoemd, samengevoegd of gesplitst element voortzet
│   └── beleidsdomeinen.yaml          de beschrijving van een beleidsdomein (Beleidsdomeinindeling)
├── bronanalyses/<onderwerp>/<brontype>/<bron-id>.md   wat een bron betekent voor de architectuur (AI)
├── analyses/                         analyses en besluiten (AI), plus ggm-terugmeldingen.md en procesarchitectuur-terugmeldingen.md (gegenereerd)
├── bedrijfsarchitectuur/ · motivatie/ · begrippen/   gegenereerd door tools/render.py
├── ter-beoordeling.md · voortgang.md                gegenereerd door tools/render.py
├── ggm/ · gemma/                     gegenereerd door tools/ggm.py en tools/gemma.py
├── export/                           gegenereerd door tools/archimate_export.py: het Archi-bestand en het rapport
├── schemas/                          beoordeling (gegenereerd uit tools/bepaal_type.py), bronanalyse, analyse
├── tools/                            Python-gereedschap van deze wiki (met tests in tools/tests/)
└── .agents/skills/                   vaardigheden van deze wiki
```

## 4. Render

[tools/render.py](tools/render.py) maakt alle leesbare bestanden uit de beoordelingen, de bronanalyses en de titels in `sources/index`. Het oordeelt niet en schrijft nooit in `beoordelingen/`. Twee keer renderen geeft hetzelfde resultaat. `tools/afleiden.py` draait het na elke afleiding; `llmwiki promote apply` na elk akkoord.

| Commando | Wat |
|---|---|
| `uv run python tools/render.py` | Alles opnieuw maken; pagina's zonder beoordeling worden verwijderd |
| `uv run python tools/render.py --check` | Elke pagina gelijk aan de beoordelingen? (pre-commit: `llmwiki precommit render-check`) |
| `uv run python tools/render.py --voorbeeld <id>` | Eén elementpagina naar het scherm |

| Bestand | Inhoud |
|---|---|
| `bedrijfsarchitectuur/<map>/<taakveld>/<beleidsdomein>/<id>.md`, `bedrijfsarchitectuur/bedrijfsfuncties/<domein>/<id>.md`, `motivatie/beleidskaders/<id>.md` | Elementpagina; de map volgt uit het type (`wiki.yaml` `page_types`), de submappen uit taakveld en beleidsdomein, bij een functie uit het domein (kleine letters met koppeltekens) |
| `begrippen/<onderwerp>.md` | Begrippenlijst: per begrip de uitkomst (element met link en status, synoniem van, specialisatie van, geen element …), de reden, de herkomst en de GGM-entiteit |
| `analyses/ggm-terugmeldingen.md` | Doorlopende lijst van GGM-terugmeldingen |
| `analyses/procesarchitectuur-terugmeldingen.md` | Doorlopende lijst van terugmeldingen aan de GEMMA-procesarchitectuur (UPL-lijsten, kennismodel), uit `beoordelingen/procesarchitectuur-terugmeldingen.yaml` |
| `ter-beoordeling.md` | Wat wacht op akkoord (status `review`), en wat nog moet worden voorgelegd |
| `voortgang.md` | Aantallen per onderwerp, type en status |

Opbouw van een elementpagina, in vaste volgorde (een sectie zonder inhoud vervalt):

1. Frontmatter: `id`, `type`, `archimate_type`, `status`, `naam`, `onderwerpen`, `taakveld`, `beleidsdomein`, `definitie`, `grondslag`, `match`, `data_object`, `procesniveau`, `synoniemen`, `bronnen`, en de letterlijke `ggm_*`- en `gemma_*`-velden. Geen verwijzingen naar andere pagina's: die staan als links in de body, zodat Obsidian backlinks toont.
2. Titel en een regel met de status.
3. *Definitie* (met de formele definitie als citaat), *Beschrijving*, *Per onderwerp*, *Synoniemen*.
4. *Kenmerken*: de uitkomst van de beslistabel en per kenmerk de waarde, onderbouwing en bron.
5. *GGM*, *GEMMA*: match, sterkte, onderbouwing en de letterlijke definitie uit het model.
6. *Grondslag*, *Naamkeuze*, *Homoniemen*, *Generalisatie*, *Specialisaties*, *GGM-componenten*, *Tegenhanger*.
7. *Relaties* (uitgaand) en *Inkomende relaties* (verzameld uit de andere beoordelingen).
8. *GGM-terugmeldingen*, *Ter discussie* (open redenen en vragen), *Besluiten redacteur*, *Bronnen*.

Garanties: elke bronverwijzing is een link naar de bronanalyse (een modelbron linkt naar `sources/raw/`); relaties staan in beide richtingen; er staan geen links naar tools of regels; elke alinea staat op één regel.

## 5. Werkstroom

Skill [gemma-archimate-model-update](.agents/skills/gemma-archimate-model-update/SKILL.md) volgt de gedeelde `wiki-curatie-update`. Er is geen run: de werkboom is de toestand.

```text
 STAP                           WIE        RESULTAAT                                        STATUS
 1 Onderwerp                    AI+redact. beoordelingen/onderwerpen/<onderwerp>.yaml         —
 2 Bronnen en bronanalyse       AI         sources/, bronanalyses/                            —
 3 Beoordelen                   AI         beoordelingen/begrippen/<id>.yaml                  —
 4 Afleiden en renderen         script     status, afgeleid, alle pagina's                    kandidaat of review
 5 Voorleggen (één voor één)    AI→redact. besluiten: in de beoordeling → terug naar 4        kandidaat → review of afgewezen
 6 Bekijken                     redacteur  llmwiki promote plan; ter-beoordeling.md, pagina's, Source Control
 7 AKKOORD in de chat           redacteur
 8 Vastleggen                   script     llmwiki promote apply (klik "toestaan"); log.md   review → goedgekeurd
 9 Exporteren                   script     tools/archimate_export.py; export/                 —
10 Commit                       redact./AI pre-commit: render-check, goedgekeurd-guard
```

| Stap | Skill | Gereedschap |
|---|---|---|
| 2 | [gemma-archimate-model-ingest](.agents/skills/gemma-archimate-model-ingest/SKILL.md) | `llmwiki source add` (ook `--url`, pdf, `--brontype`), `llmwiki source bronregel` |
| 3 | [gemma-archimate-model-beoordelen](.agents/skills/gemma-archimate-model-beoordelen/SKILL.md) + [criteria](.agents/skills/gemma-archimate-model-criteria/SKILL.md) | `tools/ggm.py kandidaten`, `tools/gemma.py kandidaten`, `tools/relaties.py voorstel` |
| 4 | — | `tools/afleiden.py` (roept `tools/render.py` aan) |
| 6–8 | — | `llmwiki promote plan`, `llmwiki promote apply --akkoord-woord AKKOORD` |
| 9 | [gemma-archimate-model-archimate-export](.agents/skills/gemma-archimate-model-archimate-export/SKILL.md) | `tools/archimate_export.py --check`, `tools/archimate_export.py` |

Nieuwe modelversies: [gemma-archimate-model-ggm-release](.agents/skills/gemma-archimate-model-ggm-release/SKILL.md) en [gemma-archimate-model-gemma-release](.agents/skills/gemma-archimate-model-gemma-release/SKILL.md): release, daarna `tools/afleiden.py`.

## 6. Status

| Status | Wie | Wanneer |
|---|---|---|
| `kandidaat` | `tools/afleiden.py` | Er staat een reden open die geen besluit van de redacteur dekt: de beslistabel zegt "voorleggen", de grondslag is `regelgeving`, of het is een gegevensobject zonder sterke GGM-match |
| `review` | `tools/afleiden.py` | Niets meer voor te leggen; wacht op akkoord |
| `goedgekeurd` | `llmwiki promote apply`, na AKKOORD en de klik | Met een regel in `log.md` met de hash van de inhoud van de beoordeling (alles behalve `status` en `afgeleid`) |
| `afgewezen` | `tools/afleiden.py`, na het besluit `afwijzen` | Geen pagina; blijft in de begrippenlijst |

Een inhoudelijke wijziging aan een goedgekeurde beoordeling maakt haar weer `review`; een andere opmaak, een nieuw render-script of een nieuwe modelrelease niet. De pre-commit-controle `llmwiki precommit goedgekeurd-guard` weigert `goedgekeurd` zonder overeenkomende regel in `log.md`.

## 7. Criteria: is een begrip een element, en welk?

Eén plek: skill [gemma-archimate-model-criteria](.agents/skills/gemma-archimate-model-criteria/SKILL.md), met de code in [tools/bepaal_type.py](tools/bepaal_type.py).

- **Kenmerken** zijn neutrale eigenschappen van een begrip (bijv. *onderscheidbare exemplaren*). De AI beantwoordt ze allemaal, één keer, met onderbouwing en bron-id's.
- **Criteria** zijn de regels van de beslistabel: welke combinatie van kenmerken tot welk type leidt. Het script past ze toe; het type is een uitkomst, geen keuze vooraf.
- De beslistabel heeft acht stappen: welk begrip (synoniem of homoniem), scope, afhankelijkheid, consistentie, type, een **drempel** per type (een kernrelatie die ja moet zijn, eventueel een eis, en van de overige drempelcriteria hoogstens één nee), de **zelfstandige specialisatie** en de **indeling** (stap 7: procesniveau en objectniveau, met de plaats in de indelingen; `tools/bepaal_type.py indeling` heeft de context van alle begrippen). Criteria van 2026-10-04 (`analyses/indelingen.md`); de onderbouwing staat in `analyses/kenmerken.md`, `analyses/gemma-kennismodel.md`, `analyses/gegevensrollen.md` en `analyses/synoniemen-en-homoniemen.md`.
- De documentatie in de skill en in [analyses/beslistabel.md](analyses/beslistabel.md), en het schema [schemas/beoordeling.schema.json](schemas/beoordeling.schema.json), worden uit de code gegenereerd; een test bewaakt dat ze gelijk blijven.
- Interaction wordt herkend, maar heeft geen paginatype: zo'n begrip wordt voorgelegd. Representation en Location zijn een vaste uitkomst zonder pagina. Van de motivatielaag zit alleen het beleidskader in dit model.

## 8. Bronvoorrang en definities

- Brontype per bron (in de intake): `europese-regelgeving`, `rijksregelgeving`, `informatiemodel`, `richtlijn`, `gemeentelijke-regelgeving`, `beleid`, `overig`, `model`. De volgorde staat in `wiki.yaml` (`bronvoorrang`); `model` (het GEMMA-model) is een matchdoel en valt erbuiten. De herkomst op de begrippenlijst is het brontype van de hoogste bron van het begrip.
- De betekenis van elk brontype staat in de regel Bronvoorrang (`AGENTS.md`). Landelijke regelgeving (`europese-regelgeving`, `rijksregelgeving`) en `informatiemodel` bepalen welke begrippen er zijn en wat ze formeel betekenen; `richtlijn`, `beleid` en `overig` leveren de gangbare taal. Voorrang bepaalt niet of iets een element is.
- De naam en de herkenbare `definitie` komen uit de gangbare taal; de wetsterm wordt een synoniem met context "wet" (bijv. *Urn*, met *asbus*). Zie [references/naamgeving.md](.agents/skills/gemma-archimate-model-beoordelen/references/naamgeving.md) en [references/definitie.md](.agents/skills/gemma-archimate-model-beoordelen/references/definitie.md).

## 9. Relaties

Elementen en relaties worden samen gevonden. Een relatie wordt pas een ArchiMate-relatie als van beide kanten vaststaat wat voor element het is.

- De bronanalyse noemt de relaties tussen begrippen zoals de bron ze formuleert (`## Relaties`: van, werkwoord, naar, vindplaats).
- `tools/relaties.py voorstel <id>` voegt de kandidaten uit het GGM en uit de bronanalyses samen, als YAML voor `relaties:` in de beoordeling. Uit de bronnen: beide kanten worden opgelost via de beoordelingen; een eigenschap of specialisatie zonder pagina wordt opgetild naar het genoemde begrip; geen element → de relatie vervalt (`tools/relaties.py uit-bronnen <onderwerp>` toont welke en waarom). Uit het GGM: specialisaties zonder pagina en GGM-componenten worden opgetild; ketens via niet-opgenomen entiteiten krijgen het zwakste type en een samengestelde kardinaliteit; relaties naar enumeraties vervallen.
- Een relatie staat één keer, in de beoordeling van het bronelement. De render zet de inkomende kant op de pagina van het doel.
- **Grondslag**: `ggm-exact`, `ggm-afgeleid` of `bron` (bronnen verplicht). Een bronrelatie tussen dezelfde elementen als een GGM-relatie bevestigt die.
- `tools/afleiden.py` toetst elke relatie aan de ArchiMate-relatietabel met de GEMMA-modelleerafspraken (actor via een rol; functie bedient proces; kanaal toegewezen aan dienst; dienst zonder toegang tot een object) en controleert dat het doel een element is.
- **Terugmelden** alleen bij `ggm-exact`. **Aandachtspunt:** in het GGM-export zijn de richting van deel-geheel en de multipliciteiten niet altijd eenduidig; controleer ze. Werkwijze in detail: [references/relaties.md](.agents/skills/gemma-archimate-model-beoordelen/references/relaties.md).

## 10. GGM en GEMMA als bron

| | GGM | GEMMA-model |
|---|---|---|
| Bronbestand | XMI 2.1 (Enterprise Architect) | Archi-bestand `.archimate` (voorkeur: met map-id's en profielen, nodig voor de export); AMEFF kan ook, zonder export |
| Herkomst | GitHub `Gemeente-Delft/Gemeentelijk-Gegevensmodel`, `wiki.yaml` → `ggm.herkomst` | GitHub `VNG-Realisatie/GEMMA-Archi-repository`, `wiki.yaml` → `gemma.herkomst` (nu de AMEFF; een `.archimate` daar is gevraagd, zie `todo.md`), of een lokaal opgeslagen `.archimate` |
| Tool | [tools/ggm.py](tools/ggm.py) | [tools/gemma.py](tools/gemma.py) |
| Gegenereerd | `ggm/ggm_parsed.json`, `ggm/<taakveld>/<beleidsdomein>.md` | `gemma/gemma_parsed.json`, `gemma/overzicht.md` |
| Zoeken (AI) | `kandidaten`, `entiteit`, `naamgenoten`, `generalisaties`, `attribuut`, `relaties` | `kandidaten`, `element`, `koppel`, `zoek`, `groepering` |
| Letterlijke velden (script) | `velden` → `afgeleid.ggm` | `velden` → `afgeleid.gemma` |
| Nieuwe versie | `release --id <bron-id> [--ref <branch/tag>]`, daarna `tools/afleiden.py` | idem |

De match kiest de AI op betekenis; het afleid-script haalt bij elke run de letterlijke velden op. Gegenereerde modelbestanden hebben een hash-kop; `tools/afleiden.py` meldt een handmatige wijziging als fout.

## 11. Controles

`tools/afleiden.py` houdt tegen (fout, er wordt niets geschreven): het schema van de beoordeling, onvolledige kenmerken, een kenmerk `ja` zonder bron, een element zonder bron, ontbrekende velden van een element (definitie, beschrijving, grondslag, GEMMA-match, en bij een gegevensobject de GGM-match; taakveld en beleidsdomein bij typen met submappen), een bron zonder intake of bronanalyse, een onbekend onderwerp, een niet-bestaande GGM-guid of GEMMA-id, een relatie naar iets dat geen element is of die niet in de relatietabel past, specialisaties, tegenhangers en homoniemen die geen element zijn, dubbele paginapaden, bronanalyses zonder `Bron:`-regel of buiten de bronnenlijst van hun onderwerp, ongeldige terugmeldingen, en handmatig gewijzigde modelbestanden.

[tools/signalen.py](tools/signalen.py) waarschuwt, met de naam van de regel: absolute taal, registr*-taal, een definitie van meer dan één zin, de naamvorm van processen en functies, de wetsterm als naam, een afwijkende GGM- of GEMMA-naam zonder synoniem, onderwerpgebonden tekst in definitie of beschrijving, een dienst zonder realiserend gedrag, een gebeurtenis die niets start, en een synoniem bij meer elementen. Waarschuwingen beoordeelt de AI inhoudelijk.

## 12. Export naar Archi

[tools/archimate_export.py](tools/archimate_export.py) schrijft de goedgekeurde elementen en relaties als `export/gemma-archimate-model.archimate`, om in Archi te bekijken en in het GEMMA-model te importeren (*Import › Another model into selected model*: Archi voegt samen op id). Werkwijze: skill [gemma-archimate-model-archimate-export](.agents/skills/gemma-archimate-model-archimate-export/SKILL.md).

- **Id's:** een element met een GEMMA-match krijgt het GEMMA-id en staat in dezelfde mappen (met dezelfde map-id's) als in GEMMA; een nieuw element krijgt een vast id (uuid5 van het begrip-id) onder `wiki-gemma-model`. Een relatie krijgt het id van de GEMMA-relatie van hetzelfde type tussen dezelfde elementen, anders een vast id. Daarvoor is het GEMMA-model als `.archimate` nodig; de AMEFF heeft geen map-id's.
- **Inhoud:** naam en definitie uit de wiki (ook over een GEMMA-element heen, met de oude als eigenschap); de GEMMA-eigenschappen en het profiel letterlijk; eigen eigenschappen `wiki-gemma-model …`, onder meer `procesniveau`, `objectniveau` en de indelingsvelden.
- **Indelingen** ([analyses/indelingen.md](analyses/indelingen.md)): een proces zonder GEMMA-match staat in de map `Procesindeling naar kernobject`, een bedrijfsinteractie in de map `Ketensamenwerking`; een levensloopproces krijgt GEMMA type *Bedrijfsproces (cluster)*; een aggregatie tussen processen heeft `indeling` en `procesniveau` ("levensloopproces → bedrijfsproces"); `gemma_generiek` wordt een specialisatie naar het GEMMA-element, dat letterlijk meegaat zonder wiki-eigenschappen; beleidsdomein, domein en doelgroep worden een aggregatie vanuit de bestaande GEMMA-groepering (die letterlijk meegaat), of vanuit een nieuwe groepering in de map van de wiki voor een beleidsdomein dat GEMMA niet kent. Het rapport noemt de specialisaties en de nieuwe groeperingen. De export vertrouwt de match: een zwakke of partiële match gaat alleen met akkoord van de redacteur (regel Zwakke match voorleggen).
- **Objectbehoud:** een hernoemd, samengevoegd of gesplitst element zet het Archi-object voort dat `beoordelingen/objecten.yaml` noemt; element- en relatie-id's komen dan van dat begrip-id, zodat views in Archi blijven werken. `tools/afleiden.py` toetst het register; de export weigert een typewijziging van een voortgezet object.
- **Volledige sync:** elk element en elke relatie heeft `wiki-gemma-model exportdatum`. Na de import verwijdert een jArchi-script wat de wiki zelf maakte en een oudere datum heeft; bij een GEMMA-object haalt het alleen de wiki-eigenschappen weg.
- **Gate:** alleen `goedgekeurd`, met een promotieregel in `log.md`; `--concept` (alle statussen, in `.work/`) is alleen om te bekijken. De export weigert bij fouten of een verouderde afleiding of render.

## 13. Nog niet gebouwd

- Dekkingsanalyse van het GGM (entiteitendekking) en de export naar CSV.
- Inhoudelijke audits (definities, duplicaten, werkvoorraad).
- Het hernoemen van een element met automatisch bijwerken van de id's in andere beoordelingen.
- Paginatypen voor Interaction, Location en Representation, en `applicatiearchitectuur/`.
- Het tonen van de formele definitie op GEMMA Online.
