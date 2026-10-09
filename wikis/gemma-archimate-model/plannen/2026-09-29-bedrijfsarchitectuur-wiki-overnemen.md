# Plan: Bedrijfsarchitectuur-wiki overnemen als `wikis/gemma-archimate-model` (curation)

## Context

De oude wiki `~/Documents/GitHub/llm-wikis/Bedrijfsarchitectuur/` bouwt het GEMMA-bedrijfsobjectenmodel (plus actoren, rollen, functies en processen) opnieuw op, met onderbouwing uit beleidsbronnen en verrijkt met het GGM. De regels staan verspreid over `CLAUDE.md` (PR/IH/VR/BO/SRC/WC), 8 templates, 13 `.claude/commands` en 9 Python-tools. Die worden overgezet naar second-brain: een **curation**-wiki met gedeelde bronnen (3 lagen), `wiki-update` (INGEST→ASSESS→WRITE→VALIDATE→gate→PROMOTE), wiki-skills met prefix en deterministische logica in code. **Content (pagina's, bronnen) wordt niet overgenomen.** De oude wiki draaide om bedrijfsobjecten; de nieuwe opzet is algemeen ArchiMate. BO-naamgeving (`bo_*`, "BO-criteria", "BO-pagina") verdwijnt.

Beslissingen van de gebruiker:
- Key `gemma-archimate-model`, type `curation` (nog zonder `exports:`).
- In scope: de keten curatie → element schrijven, de GGM-pipeline, bronnen ophalen (fetch/pdf; clip vervalt), GGM-terugmeldingen (aangevuld ná het schrijven van een element), het GEMMA-model als bron voor matching (`gemma_*`).
- Autonomie → status: de AI mag het zelf afhandelen → `review`; het moet voorgelegd worden → `kandidaat`; `goedgekeurd` alleen via `promote apply`.
- Elementen onder `bedrijfsarchitectuur/` (ruimte voor een map `applicatiearchitectuur/`); domeingebonden typen in `{taakveld}/{beleidsdomein}/`.
- Mappen `begrippen/` (was onderwerpoverzicht) en `bronanalyses/` (was bronsamenvatting); wiki-code in `tools/`.
- Criteria: één bestand, één gezamenlijke evaluatie via **benoemde kenmerken** + een leesbare beslistabel; de tool leidt het type af.
- Ketenpartner: een actor-pagina bij directe samenwerking.
- Bronvoorrang wet > informatiemodel > beleid; een herkenbare en, alleen bij een wezenlijk verschil, een formele definitie.
- Relaties op GGM mappen; composition/aggregation overnemen; relaties vastleggen als links (backlinks in Obsidian).
- Prefixen: `ggm_` = letterlijk uit het GGM, `gemma_` = letterlijk uit het GEMMA-model na een match, zonder prefix = eigen veld van de wiki. De velden `ggm_gemma_*` vervallen.

## 1. Doelstructuur

```
wikis/gemma-archimate-model/
├── ARCHITECTURE.md · AGENTS.md · wiki.yaml
├── begrippen/<onderwerp>.md                 begrippenlijst per onderwerp = ingang van een run
├── bronanalyses/<onderwerp>/<bron-id>.md    wat de bron betekent voor de architectuur
├── bedrijfsarchitectuur/
│   ├── bedrijfsobjecten/{taakveld}/{beleidsdomein}/<id>.md   business-object | contract
│   ├── producten/ · bedrijfsdiensten/ · bedrijfsprocessen/ · bedrijfsfuncties/   ({taakveld}/{beleidsdomein}/)
│   ├── bedrijfsgebeurtenissen/ · actoren/ · rollen/          plat
├── (later) applicatiearchitectuur/
├── analyses/ggm-terugmeldingen.md           doorlopende lijst (niet gecureerd)
├── ggm/  · gemma/                           gegenereerd: geparsede modellen + leesbare pagina's (nooit handmatig)
├── schemas/ · tools/ · .agents/skills/
└── log.md · voortgang.md · voorstellen/     beheerd door de CLI
```

`begrippen/` en `bronanalyses/` zijn apart gehouden: het zijn verschillende paginatypen met een andere levensloop. Ze gebruiken dezelfde onderwerp-id, dus de koppeling loopt via de naam.

**Veldnamen** (frontmatter van een element):

| Groep | Velden | Wie vult |
|---|---|---|
| Generiek | `id`, `type`, `status`, `onderwerp`, `bronnen`, `bijgewerkt` | model, gecontroleerd door de core |
| Eigen veld van de wiki (ArchiMate-algemeen) | `naam`, `archimate_type`, `taakveld`, `beleidsdomein`, `definitie`, `definitie_formeel`, `definitie_formeel_bron {bron, plaats}`, `toelichting`, `synoniemen [{naam, context}]`, `grondslag`, `match {ggm, gemma}`, `data_object` | model |
| `ggm_*` (letterlijk uit het GGM) | `ggm_entiteit`, `ggm_guid`, `ggm_uml_type`, `ggm_beleidsdomein`, `ggm_taakveld`, `ggm_diagram(_ids)`, `ggm_definitie`, `ggm_toelichting`, `ggm_synoniemen`, `ggm_herkomst`, `ggm_duplicaat_entiteiten` | alleen `tools/ggm.py` |
| `gemma_*` (letterlijk uit het GEMMA-model) | `gemma_id`, `gemma_naam`, `gemma_type`, `gemma_definitie`, `gemma_map`, `gemma_eigenschappen` | alleen `tools/gemma.py` |

Oud → nieuw: `bo_definitie`→`definitie`, `bo_toelichting`→`toelichting`, `bo_synoniemen`→`synoniemen`; `bo_homoniemen`, `element_tegenhangers`, `bo_relaties`, `bedrijfsprocessen`/`bedrijfsfuncties` → secties in de body met links (§4); `bo_subtypes` → sectie `## Specialisaties` (rij zonder link = geen eigen pagina); `ggm_gemma_*` vervalt; `bo_via_kandidaten` en `analyse_ggm_dekking` → buiten scope. **Regel:** in de frontmatter staan geen verwijzingen naar andere elementen. Alle verwijzingen tussen elementen zijn relatieve links in de body, zodat Obsidian de backlinks toont.

## 2. Criteria: analyse en advies

Geanalyseerd: `templates/elementtype-criteria.md`, `assess-element` stap 2–11, `write-element` stap 0/6/11/12, `CLAUDE.md` [BO1]–[BO3]/[WC4]/[WC5], template `onderwerpoverzicht`, plus tellingen in de oude content (alleen gelezen).

### 2a. Overlap: dezelfde vraag op meerdere plekken

| Onderwerp van de vraag | Komt voor in |
|---|---|
| Eigen identiteit / zelfstandig bestaan | BO-criterium 3, actor-vraag 1 en 4, rol-vraag 5 (omgekeerd), assess stap 6 |
| Herkenbaar voor domeinexperts | BO-criteria 1 en 2 (vrijwel gelijk), functie-vraag 6 |
| Meerdere exemplaren / instanties | BO-criterium 4, proces-vraag 5, rol-vraag 2 |
| Tijd: levenscyclus, begin/einde | BO-criterium 5, proces-vraag 1, functie-vragen 2/3/5 (omgekeerd) |
| Relaties / toewijsbaarheid | BO-criterium 6, actor-vraag 5, rol-vraag 6, proces-vraag 6 |
| "Is het een verantwoordelijkheid" | rol-vragen 1, 4 en 6: drie formuleringen van dezelfde vraag |
| "Slechts eigenschap/type van iets anders" | negatieve toets, assess stap 5, write 6b |
| Begripstypenlijst | elementtype-criteria, assess stap 3/11, onderwerpoverzicht-template (verouderd) |
| Zelfstandig ding met exemplaren/levenscyclus | data-object (stap 9) tegenover BO-criteria 3–5 |
| Richtinggevend | abstractieniveau "beleidsmatig" tegenover begripstype thema/doel/waarde |

### 2b. Tegenstrijdigheden

| # | Tegenstrijdigheid |
|---|---|
| T1 | Doelgroep = "classificatie" → BO, maar de negatieve toets zegt: classificatie van iets anders = geen BO |
| T2 | Governance-instrument (wet, verordening) → BO, maar de negatieve toets sluit "regel" uit; en de afbeelding op "Contract / Product" klopt niet |
| T3 | De tweede BO-pagina bij actor/rol ontstaat "zodra er gegevens worden vastgelegd", terwijl [BO1] registr* verbiedt |
| T4 | Rol "geen eigen identiteit" tegenover BO "eigen bestaan"; functie "geen begin/einde" tegenover BO "levenscyclus": het twee-pagina-patroon kan hier niet |
| T5 | De negatieve toets sluit "activiteit" uit, maar de procesinstantie wordt als BO-uitzondering genoemd |
| T6 | De actor-scope (direct handelen → pagina) botst met [WC5] (ketenpartner nooit een pagina); de praktijk heeft GGD, Veilig Thuis, woningcorporatie. **Besloten:** een pagina bij directe samenwerking |
| T7 | Autonomie: functie/proces zou zelfstandig kunnen, maar de eis "GGM-match exact/sterk" kan daar nooit slagen; de eis "5/6 BO-criteria" past niet bij actor/rol |
| T8 | [WC4]-scope noemt "wat de gemeente registreert" tegenover [BO1] |
| T9 | De BO-beslisvraag trekt naar beleidsmatig; de combinatietabel ziet operationeel als sterkste kandidaat |
| T10 | Thema/doel/waarde heten "geen element", terwijl ze ArchiMate-elementen zijn (Grouping/Goal/Driver): ze vallen buiten **dit model** |

### 2c. Hiaten

- Geen criteria voor Business Object ↔ Contract ↔ Product (in de praktijk 8× contract, 1× product).
- Business Event, Service, Collaboration, Interaction, Interface, Representation en Location ontbreken; in de praktijk opgelost met eigen begripstypen.
- De enum wordt niet afgedwongen: in de oude begrippentabellen staan **20** verschillende begripstypen, terwijl er 10 gedefinieerd zijn.
- Geen beslissing bij gelijkspel (actor/rol, functie/proces, doelgroep/rol); geen vaste volgorde tussen knock-out, score en beslisvraag.
- De drempel 5/6 heeft weinig onderscheidend vermogen: vier van de zes criteria zijn bijna altijd "ja".

### 2d. Kenmerken en criteria

**Waarom "kenmerk" en niet "criterium".** Een criterium is een oordeel per type (*voldoet dit als bedrijfsobject?*). Daarom moest in de oude opzet eerst het type gekozen worden, en kwamen dezelfde vragen in vier lijsten terug. Een **kenmerk** is een neutrale eigenschap van het begrip zelf, met bewijs uit een bron. Eén kenmerk voedt meerdere typen, en daardoor is één gezamenlijke evaluatie mogelijk. Het oordeel zit in de beslistabel: de regels daarvan zijn de **criteria**. Het model beantwoordt de kenmerken (ja/nee + onderbouwing + bron-id); `tools/bepaal_type.py` past de criteria toe. Het begripstype wordt een uitkomst, geen invoer.

**Toetsing aan ArchiMate 3.2** (herkomst van elk kenmerk):
- Bedrijfsobject: *"a concept used within a particular business domain"*, passief, *accessed by behavior*. "Eigen identiteit", "onderscheidbare exemplaren" en "levenscyclus" komen niet uit ArchiMate. Ze blijven als GEMMA-eis; "wordt bewerkt" komt wel uit ArchiMate en is verplicht.
- Actor: mag extern en generiek zijn ("Customer"). Dat bevestigt het besluit over ketenpartners. Rol omvat ook *"the part an actor plays in a particular action or event"*: aanvrager en belastingplichtige zijn dus rollen, en de vraag doelgroep-of-rol is daarmee opgelost.
- Functie = *"collection of business behavior based on … required resources and/or competencies"*. "Wat de gemeente kan" is Capability (strategielaag) en valt buiten dit model.
- Proces-vraag "valt onder een functie" is een relatie, geen eigenschap.
- Contract is tweezijdig en hoort bij een product; een beschikking of verordening is geen contract.
- Product is een **samengesteld** element, geen passief element.
- Losse normen uit wetgeving zijn Requirement/Constraint (motivatielaag); de regeling als geheel is een bedrijfsobject.

**Kenmerken** (één keer per begrip beantwoorden):

| Groep | Kenmerk | Vraag | Herkomst |
|---|---|---|---|
| Scope | herkenbaar | Kennen domeinexperts dit als eigen begrip binnen het onderwerp? | ArchiMate + GEMMA |
| | gemeentelijk | Ziet, doet of beslist de gemeente hierover, of werkt ze rechtstreeks samen met deze partij? | GEMMA |
| | buiten kernlagen | Is het een thema, doel, waarde, drijfveer, principe, losse norm/eis of vermogen? Noem welke | ArchiMate (motivatie/strategie) |
| Afhankelijkheid | slechts eigenschap | Is het alleen een eigenschap, status, waarde of indeling van één ander begrip? Noem dat begrip | GEMMA |
| Aard | gedrag | Beschrijft het iets wat gedaan wordt of gebeurt, en niet een ding, partij of plaats? | ArchiMate |
| | handelende partij | Is het een persoon, organisatie of organisatie-eenheid (ook extern of generiek) die zelf kan handelen? | ArchiMate Actor |
| | hoedanigheid | Is het een verantwoordelijkheid waaraan een actor wordt toegewezen, of de hoedanigheid waarin een partij optreedt in een handeling of gebeurtenis? | ArchiMate Role |
| | samenwerkingsverband | Is het een verband van twee of meer partijen dat samen gedrag uitvoert? | ArchiMate Collaboration |
| | toegangspunt | Is het een punt waarlangs een dienst beschikbaar komt (loket, website, kanaal)? | ArchiMate Interface |
| | plaats | Is het een fysieke plaats als zodanig (niet een gebiedsindeling als gegevensconcept)? | ArchiMate Location |
| | aanbod als geheel | Is het een samenhangend pakket van diensten/objecten dat met voorwaarden als geheel wordt aangeboden? | ArchiMate Product |
| Soort gedrag | per keer doorlopen | Is het een reeks activiteiten die per keer wordt doorlopen en een benoembaar resultaat oplevert? | ArchiMate Process |
| | gegroepeerd gedrag | Is het een doorlopende groepering van gedrag, ingedeeld naar kennis/middelen, zonder volgorde of doorlooptijd? | ArchiMate Function |
| | toestandsverandering | Is het een ogenblikkelijke toestandsverandering (geboorte, verhuizing, ontvangst aanvraag) die gedrag start of afsluit? | ArchiMate Event |
| | aangeboden gedrag | Is het expliciet beschreven gedrag dat aan de omgeving wordt aangeboden, los van de uitvoering? | ArchiMate Service |
| | gezamenlijk gedrag | Is het gedrag dat alleen door twee of meer partijen samen wordt uitgevoerd (overleg, zitting)? | ArchiMate Interaction |
| Passief | eigen identiteit | Bestaat het zelfstandig, niet alleen als onderdeel van één ander ding? | GEMMA |
| | onderscheidbare exemplaren | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | GEMMA |
| | levenscyclus | Ontstaan, veranderen en eindigen de exemplaren? | GEMMA |
| | wordt bewerkt | Wordt het door gemeentelijk gedrag gebruikt, gemaakt of gewijzigd? | ArchiMate (access) |
| | afspraak | Is het een tweezijdige afspraak met rechten en plichten (overeenkomst, convenant), geen eenzijdig besluit of regeling? | ArchiMate Contract |
| | waarneembare vorm | Is het de vorm (document, formulier, bericht) waarin informatie van een ander begrip wordt overgebracht? Noem dat begrip | ArchiMate Representation |
| | geautomatiseerd verwerkt | Is het een gegevensstructuur voor geautomatiseerde verwerking? | ArchiMate Data Object (applicatielaag) |

**Beslistabel = de criteria** (van boven naar beneden; de eerste passende regel beslist):

| Stap | Als | Dan |
|---|---|---|
| 1 Scope | niet *herkenbaar* of niet *gemeentelijk* | buiten scope, met reden |
| | *buiten kernlagen* | buiten dit model, met het ArchiMate-type (Goal, Driver, Capability …) |
| 2 Afhankelijk | *slechts eigenschap* | eigenschap of specialisatie zonder pagina van het genoemde begrip |
| 3 Aard | *handelende partij* én *hoedanigheid* | Actor als het een benoemde persoon/organisatie/eenheid is, anders Rol |
| | *handelende partij* | Business Actor |
| | *hoedanigheid* | Business Role |
| | *aanbod als geheel* | Product |
| | *samenwerkingsverband* / *toegangspunt* / *plaats* | Collaboration / Interface / Location: herkend, voorleggen |
| | *gedrag* | naar stap 4 |
| | meer dan één aard (behalve actor + rol) | conflict: voorleggen |
| | geen aard | passief: naar stap 5 |
| 4 Gedrag | precies één van *per keer doorlopen* / *gegroepeerd gedrag* / *toestandsverandering* / *aangeboden gedrag* / *gezamenlijk gedrag* | Process / Function / Event / Service / Interaction (Interaction: voorleggen) |
| | geen of meer dan één | conflict: voorleggen |
| 5 Passief | *waarneembare vorm* | Representation van het genoemde begrip: herkend, voorleggen |
| | *eigen identiteit* + *onderscheidbare exemplaren* + *wordt bewerkt* + *afspraak* | Contract |
| | *eigen identiteit* + *onderscheidbare exemplaren* + *wordt bewerkt* | Business Object (een wet/verordening als geheel: grondslag governance-object) |
| | één van die drie ontbreekt | geen element; noem het ontbrekende kenmerk |
| | geen *levenscyclus* bij een uitkomst hierboven | voorleggen |
| 6 Tegenhanger | Actor/Rol met *onderscheidbare exemplaren* + *levenscyclus* + *wordt bewerkt* | ook een bedrijfsobjectpagina (zonder registr*); bij gedrag nooit: het resultaat is een apart begrip |
| 7 Annotatie | *geautomatiseerd verwerkt* | `data_object: ja` (voedt het hiaat-signaal) |

Gevolgen: de drempels, het abstractieniveau en "doelgroep" als type vervallen. Autonomie (in assess): zelfstandig afhandelen alleen bij een uitkomst zonder conflict of "voorleggen". De eis "GGM-match" geldt alleen bij `data_object: ja`.

### 2e. Eén bestand: `.agents/skills/gemma-archimate-model-criteria/SKILL.md`

Inhoud, in deze volgorde: kenmerk tegenover criterium → per ArchiMate-type de definitie (Engels citaat + Nederlandse duiding) → de kenmerken per groep, bij naam, met vraag, herkomst, voorbeeld en tegenvoorbeeld → de beslistabel → scope → anti-patronen (registr*, eigendom, systeembeheer, regie, extern systeem: nergens een kenmerk; *geautomatiseerd verwerkt* is de enige toegestane plek) → begripstype tegenover entiteitstype. De kenmerken heten in het `beoordeling`-schema net als in de tabel (bijv. `onderscheidbare_exemplaren`). De beslistabel staat als code in `tools/bepaal_type.py`; de tabel in SKILL.md wordt door `bepaal_type.py --markdown` gegenereerd, en een test controleert dat ze gelijk blijven.

## 3. Bronvoorrang en twee definities

- **Brontype** één keer, bij de intake: `wet | informatiemodel | beleid | overig | model` (generiek veld in `source-index`).
  - wet: wetten.overheid.nl en lokale verordeningen;
  - informatiemodel: GGM, RSGB, RGBZ, catalogi, ZTC, MIM;
  - beleid: nota's, raadsvoorstellen, VNG-handreikingen;
  - model: het GEMMA-model. Dat is een matchdoel, geen bron voor begrippen, en valt daarom buiten de voorrang.

  `wiki.yaml` `bronvoorrang: [wet, informatiemodel, beleid, overig]`; `run start --onderwerp` leest in die volgorde.
- **Betekenis van voorrang:** leesvolgorde, herkomst van een begrip, en wie wint bij tegenstrijdige formele betekenis (wet boven GGM + terugmelding `definitie`). Voorrang bepaalt **niet** of iets een element is; dat doet de beslistabel.
- **Twee definities.**
  - `definitie` = herkenbaar: altijd aanwezig, ≤160 tekens, 1 zin, gangbare taal (beleid), gaat naar GEMMA. Spreekt ze de formele tegen, dan `⚠️ Tegenspraak`.
  - `definitie_formeel` + `definitie_formeel_bron {bron, plaats}` = letterlijk uit de hoogst gerangschikte bron, alleen bij een **wezenlijk verschil**.
  - Toets: *vallen onder beide definities precies dezelfde exemplaren?* Ja → alleen de herkenbare. Nee, of de formele heeft voorwaarden die ertoe doen (termijn, uitzondering, afbakening) → beide, met één zin over het verschil. Twijfel → beide.
  - Komt de formele definitie uit het GGM, dan staat ze al in `ggm_definitie` en komt er geen kopie. De uitzondering in [VR3] voor letterlijk overnemen vervalt.
  - Naam = de herkenbare naam; een afwijkende wetsterm wordt een synoniem met context "wet". Tonen op GEMMA Online komt later.
- **Afdwinging:** de check eist dat de bron van de formele definitie bestaat en brontype wet/informatiemodel heeft, dat formeel ≠ herkenbaar en dat er een verschilzin is.

## 4. Relaties

Het GGM bevat (gemeten): Association 1002 (44 «Relatiesoort»), Generalization 304, Aggregation 87, Usage 17, Abstraction «Derive» 1. Het XMI onderscheidt composite (124 uiteinden) en shared (46), maar de oude parser gooit dat weg. In GEMMA is aggregatie nu de groepering op beleidsdomein; tussen bedrijfsobjecten staan alleen specialisatie en associatie.

- **Vastleggen als link.** Elke relatie staat één keer, op de pagina van het bronelement, als rij in `## Relaties` met een relatieve link. Obsidian toont de omgekeerde kant als backlink. De tool leest de tabel (vaste kolommen), en `relaties.py --inkomend` geeft de omgekeerde kant voor de controles. Hetzelfde patroon geldt voor `## Specialisaties`, `## Generalisatie`, `## Tegenhanger` en `## Homoniemen`.
  ```
  | Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie |
  |---|---|---|---|---|---|
  | compositie | [Onderdeel beschikking](onderdeel-beschikking.md) | bevat | 1 → 1..* | ggm-exact | EAID_… |
  ```
- **Mappen op GGM-relaties waar het kan.** Grondslag `ggm-exact` (één GGM-relatie tussen de gematchte entiteiten), `ggm-afgeleid` (keten, zie hieronder) of `bron` (niet in het GGM; met bron-id, volgens de bronvoorrang).
- **Terugmelden alleen bij `ggm-exact`**: fout type, richting, kardinaliteit, naam of een dubbele relatie → terugmelding van het nieuwe type `relatie`. Nieuwe en afgeleide relaties worden niet teruggemeld (een fout in een schakel wel, als die schakel).
- **Subtypes overslaan** (deterministisch, in de tool):
  - is een uiteinde een specialisatie zonder pagina of een GGM-component, dan wordt de relatie opgetild naar het element dat die draagt;
  - A–X–B via een niet-opgenomen X wordt A–B, met het zwakste type in de keten (compositie > aggregatie > associatie, volgens de ArchiMate-afleidingsregel);
  - specialisatie wordt niet geketend;
  - kardinaliteit wordt samengesteld;
  - relaties naar enumeraties/typetabellen vervallen; dubbelingen worden samengevoegd; lussen vervallen.
- **Mapping van GGM-relatietypen** (besloten: composition/aggregation overnemen):

  | GGM | Voorwaarde | ArchiMate |
  |---|---|---|
  | Generalization | beide uiteinden opgenomen | specialization (anders: specialisatie zonder pagina) |
  | Aggregation composite | naam wijst op deel-geheel ("bevat", "bestaat uit") | composition |
  | Aggregation shared | idem | aggregation |
  | Aggregation | naam is geen deel-geheel ("leidt tot", "beschrijft") | association (gericht) + terugmelding `relatie` |
  | Association (± «Relatiesoort»), Usage | — | association; gericht als de naam een leesrichting heeft |
  | Abstraction «Derive» | "is een" | specialization, anders association; terugmelding |

- **Groepering op beleidsdomein** is in het GEMMA-model een aggregatie vanuit een Grouping. Die leggen we niet vast als relatie: de tool leidt haar af uit `taakveld`/`beleidsdomein` (map + frontmatter) en controleert haar tegen de groepering in het GEMMA-model. Een afwijking is een signaal.
- **Relaties van de nieuwe typen** (grondslag `bron`): assignment (actor→rol, actor/rol→gedrag), access (gedrag→object, lezen/schrijven), triggering/flow, realization (proces→dienst, representation→object), serving (dienst→actor/rol), aggregation/composition (product→dienst/object, functie→proces). De tool toetst tegen de ArchiMate-relatietabel (deelverzameling business-laag).
- Bronvoorrang geldt ook hier: een wet wint van het GGM (terugmelding); beleid levert de herkenbare naam.

## 5. GEMMA-model als bron (`gemma_*`)

**Advies voor de invoer: het Archi-bronbestand (`.archimate`).** Het is completer dan een Open Exchange-export (AMEFF): mappen met id's, alle eigenschappen en views staan erin. AMEFF verliest de mapstructuur, en bij importeren maakt het een nieuw model of nieuwe mappen aan (vandaar de dubbele mappen). Werkwijze: `tools/gemma.py release <bestand.archimate>` voegt het toe als bron (brontype `model`, nieuwe versie = nieuw bron-id) en parset het naar `gemma/gemma_parsed.json`. Bevragingen: `zoek`, `element`, `velden` (geeft het `gemma_*`-blok), `groepering`, `relaties`. De match gaat bij voorkeur deterministisch via de GGM-GUID-eigenschap op het GEMMA-element, anders via naam/synoniemen, met `match.gemma` als matchsterkte.

**Advies voor later terugschrijven (export, buiten scope nu):** geen AMEFF, maar een **deel-`.archimate`** dat de id's van bestaande elementen, relaties en **mappen** uit het bronbestand behoudt. Nieuwe elementen krijgen een nieuwe id in een bestaande map. Archi's "Import model into current model" voegt samen op id, dus zonder dubbele mappen. Dit gedrag eerst in Archi testen met een klein deelbestand (verificatiepunt) voordat het exportdoel wordt gebouwd.

## 6. Wat gebeurt er met elke regel

Legenda: **T-core** = `tools/llmwiki` · **T-wiki** = `wikis/…/tools` of `schemas` · **R** = wiki-`AGENTS.md` · **S** = wiki-skill · **C** = criteria-skill · **—** = vervalt. Regelgroep `BO` wordt `EL` (elementen); de teksten worden algemeen ArchiMate.

| Oud | Wordt | Toelichting |
|---|---|---|
| §1 ad-hoc vragen | R (kort) | Antwoord vanuit begrippen- en elementpagina's; de vraag-antwoordpagina vervalt |
| §2 bronnen toevoegen | T-core + `wiki-ingest` | `source add` + `brontype` (§3, §9) |
| §3 wikilinks/aliassen, [WC1]–[WC3], [SRC9] | — | Relatieve links; `validate` verbiedt `[[…]]` |
| §3 bestandsnamen, [VR1] | T-wiki | `id`-patroon in het schema |
| §3 citaten als blockquote | S (write) | |
| [PR1], [SRC6] | T-core | `precommit sources-immutable` bestaat al |
| [PR2], [PR4], [PR5], [WC13], [W4] | — | Staging/promote, generieke criteria, log via de CLI, `run complete` + VALIDATE |
| [PR3] eerst bespreken | S | Kernpunten na ASSESS, vóór WRITE |
| [PR6]/[PR7], [VR2], [BO9]→[EL9], [SRC3]/[SRC5], [WC8]–[WC11], [W1]–[W3] | R | [WC8]–[WC11] ook als waarschuwing in de check |
| [IH1]/[IH2]/[IH5] | T-core + T-wiki | `bronnen:` gevalideerd; bronanalyse bestaat; element staat in de begrippenlijst |
| [IH3]/[IH4]/[IH6] | R + T-wiki | Voorleggen = `kandidaat` + `## Ter discussie` |
| [VR3] | T-wiki | Geldt voor `definitie` (herkenbaar); uitzondering voor letterlijk overnemen vervalt (§3) |
| [BO1]–[BO3] | C + T-wiki (waarschuwing) | Anti-patronen |
| [BO4]–[BO8] | S (`naamgeving.md`) | "BO-naam" → "elementnaam" |
| [BO10] | later `hernoem.py` | Met links in de body: links bijwerken is een deterministische tool |
| [BO11] | — | Entiteitendekking buiten scope |
| [BO12]–[BO14] prefixen/herkomst | T-wiki + R | Nieuwe prefix-regel (§1): `ggm_`/`gemma_` alleen door de tools gevuld; de check eist gelijkheid met het geparsede model |
| [BO15]/[BO16] subtypes/specialisaties | S + T-wiki | `## Specialisaties` in de body; veld `bo_subtypes` vervalt |
| write stap 7, `bo_relaties`, `bedrijfsprocessen`/`-functies` | T-wiki + S | §4, `tools/relaties.py` |
| [SRC1]/[SRC2]/[SRC4] | T-wiki + S | `tools/ggm.py`, skill `…-ggm-release` |
| [SRC7]/[SRC8] | T-core + `wiki-ingest` | `source add --url`, deterministisch opschonen |
| [WC4]/[WC5] | C (*gemeentelijk*) + R | [WC5] aangepast (directe samenwerking) |
| [WC6] | S + T-wiki | Bij `afgerond` is een conclusie verplicht |
| [WC7], [WC12] | T-wiki | Geen verwijzingen naar technische bestanden; hash-kop in `ggm/`/`gemma/` |
| frontmatter-stijl, §8 gedragsprincipes | — | `frontmatter.write` schrijft uniform; generiek |

## 7. Skills (oud → nieuw)

| Oud | Nieuw | Soort (`metadata.kind`) |
|---|---|---|
| ingest + element-pipeline | `gemma-archimate-model-update`: dun, `wiki-update` plus uitbreidingen per fase | workflow |
| ingest (lens, bronselectie) | `gemma-archimate-model-ingest`: bronanalyse (samenvatting ≤500 woorden, begrippen met brontype, relevantie, citaten), bronselectie-regels, [PR3] | capability · INGEST |
| — | `gemma-archimate-model-criteria` (§2e) | capability |
| assess-element | `gemma-archimate-model-assess`: domeinbepaling, kenmerken invullen → `bepaal_type.py`, naamgenoten (`ggm.py`/`gemma.py`), structuuranalyse, hiaat, autonomie → `voorgestelde_status`, per begrip presenteren, begrippenlijst | capability · ASSESS |
| write-element | `gemma-archimate-model-write` + references `naamgeving`, `grondslag`, `ggm-match`, `gemma-match`, `definitie` (§3), `hierarchie`, `relaties` (§4), `secties` (per type), `tegenhangers`; terugmeldingen via `terugmelding.py` | capability · WRITE |
| generate-ggm | `gemma-archimate-model-ggm-release`; nieuw: `gemma-archimate-model-gemma-release` | capability |
| fetch, convert_pdf | `llmwiki source add --url/--pdf` + gedeelde `wiki-ingest` | core |
| clip (Obsidian Web Clipper) | vervalt (niet in gebruik) | — |
| lint (binnen scope) | `tools/check_elementen.py` op het uitbreidingspunt van VALIDATE | tool |
| lint (rest), audit-element, domain-status, entiteitendekking, export-ggm | buiten scope (§11) | — |

## 8. Documentatie

- **Root `ARCHITECTURE.md`**: subparagraaf skill-soorten (`metadata.kind` workflow/capability, `metadata.scope` core/wiki, prefixen, `requires-*`, `references/`, uitbreidingspunten) en plaats van code (`tools/llmwiki`, `wikis/<key>/tools/`, `<skill>/scripts/`; de root-map `scripts/` is alleen voor setup). Melden dat een wiki een eigen `ARCHITECTURE.md` mag hebben, en dat mapnamen per wiki instelbaar zijn via `page_types.<type>.dir`.
- **`docs/onderbouwing.md`**: `scripts/` → `tools/` voor wiki-code in 5.8, 5.13, 5.15 (permissieregels), 5.18; noot over instelbare mapnamen in 5.18/5.19.
- **Nieuw: `wikis/gemma-archimate-model/ARCHITECTURE.md`**. Wiki-specifieke opzet, met verwijzingen, in gewone taal voor het GEMMA-team:
  1. Doel en plaats in de keten (bronnen → dit model → GEMMA Online / Archi-model).
  2. Plattegrond (§1) en paginatypen met hun schema (`schemas/…`).
  3. Veldnamen en prefixen (`ggm_`/`gemma_`/eigen).
  4. Herleidbaarheid: bron → bronanalyse → begrippenlijst → element.
  5. Werkstroom per fase: welke skill (`.agents/skills/…`) en welke tool.
  6. Criteria: waar ze staan (criteria-skill, `bepaal_type.py`) en hoe ze werken.
  7. Bronvoorrang en definities.
  8. Relaties en het vastleggen als link.
  9. GGM en GEMMA als bron (`ggm.py`, `gemma.py`, release-skills).
  10. Status, gate en autonomie.
  11. Controles (`check_elementen.py`).
  12. Rules (`AGENTS.md`, per regel-id).
  13. Buiten scope.

  `AGENTS.md` van de wiki blijft kort (Rules) en verwijst naar dit document.

## 9. Tools

**T-core (`tools/llmwiki`, met tests):**
1. `validate.py`: `page_types.<t>.schema` echt toepassen; dode relatieve links melden.
2. `lint.py:129` `check_goedgekeurd_guard`: `rglob` (taakveldmappen).
3. `gate.py:93` `_materialize_curation`: alleen `review` → `goedgekeurd`; `kandidaat` ongewijzigd, zonder logregel; het voorstel toont beide groepen.
4. `runs.py:109`: onderwerppagina via `page_types.onderwerp.dir` (standaard `onderwerpen`); bronlijst ordenen volgens `bronvoorrang`.
5. `source add`: `--url` (HTML→MD met de opschoonregels uit `fetch.md`, iBabs-resolver, wetten.overheid.nl), pdf via pymupdf4llm; `source-index.schema` + `url`, `url_pagina`, `opgehaald`, `beschrijving`, `brontype`.

**T-wiki (`wikis/gemma-archimate-model/tools/`):**
- `bepaal_type.py`: kenmerken → type, tegenhanger, conflict, voorgestelde status; `--markdown` voor de criteria-skill.
- `ggm.py`: `release` (poort van parse/generate/enrich; houdt composite/shared vast) + bevragingen `zoek`, `entiteit`, `velden`, `naamgenoten`, `generalisaties`, `attribuut`, `relaties`.
- `gemma.py`: `release <.archimate>` + bevragingen `zoek`, `element`, `velden`, `groepering`, `relaties`.
- `relaties.py`: `voorstel <id>` (kandidaat-relaties uit het GGM, met optillen/ketenen/mapping, en terugmeldkandidaten bij exacte matches), `--inkomend <id>`, tabel lezen/schrijven.
- `check_elementen.py`: lint_checks binnen scope (schema; herleidbaarheid; bronanalyse in begrippen; id's uniek over submappen; map = taakveld/beleidsdomein; specialisaties; duplicaten; homoniemen/tegenhangers via links wederzijds; wees-elementen) + nieuw:
  - `ggm_*`/`gemma_*` gelijk aan de geparsede modellen;
  - beoordeling past bij het type;
  - `definitie`-vorm en regels voor de formele definitie;
  - relatietabel: ArchiMate-tabel, link bestaat, GGM-relatie past bij de uiteinden, geen dubbelingen;
  - groepering tegenover GEMMA;
  - [WC7] en [WC12];
  - registr* en verboden zinnen als waarschuwing;
  - `ter discussie` ↔ terugmeldingen.
- `terugmelding.py add --run <id>`: rij in de gestagede `analyses/ggm-terugmeldingen.md` (volgnummer, enums, type `relatie` erbij) + changeset.json.

**Schemas:** `element-basis` ($defs volgens de veldtabel in §1), per type `bedrijfsobject`, `product`, `bedrijfsdienst`, `bedrijfsgebeurtenis`, `bedrijfsproces`, `bedrijfsfunctie`, `actor`, `rol`; `onderwerp` (begrippenlijst), `bronanalyse`, `analyse`, `beoordeling` (kenmerken bij naam + onderbouwing + bron-id's).

**Vervalt:** `migrate_frontmatter_style.py`, de fix-functies in `lint_checks.py`, `export_ggm_csv.py`, `entiteitendekking*.py`.

## 10. Uitvoeringsvolgorde

1. T-core 1–5 + tests.
2. Documentatie root (§8).
3. Wiki-skelet: `wiki.yaml`, `AGENTS.md` (kolom R, groep EL), `ARCHITECTURE.md` (eerst als skelet, na stap 8 compleet).
4. Schemas.
5. `bepaal_type.py` + criteria-skill (gegenereerde tabel).
6. `ggm.py`, `gemma.py` + release-skills.
7. `relaties.py`; skills `…-ingest`, `…-assess`, `…-write`, workflow `…-update`; aanpassing aan de gedeelde `wiki-ingest`.
8. `check_elementen.py`, `terugmelding.py`; `ARCHITECTURE.md` van de wiki afmaken.
9. `uv run llmwiki harness sync`, `llmwiki lint`.

## 11. Buiten scope (later)

Entiteitendekking, CSV-export en `.archimate`-export (advies §5), audit-element, de semantische lint-stap, `hernoem.py`, domain-status, vraag-antwoordpagina's, ToDo-backlogs, paginatypen voor Collaboration/Interface/Interaction/Location/Representation, `applicatiearchitectuur/`, tonen van de formele definitie op GEMMA Online, migratie van oude content.

## 12. Aannames (corrigeer bij akkoord)

- A1 `onderwerp:` is één id (hoofdonderwerp).
- A2 Een niet-relevante bron = een bronanalyse met `relevant: nee` + reden.
- A4 `wiki.yaml` `ggm.bron` en `gemma.bron` wijzen naar de actuele modelbronnen; de Markdown-versie in `sources/raw` is een gegenereerd structuuroverzicht.
- A5 De root-rules blijven ongewijzigd.
- A6 `sources.tags` bepalen bij de eerste ingest.
- A7 Gebeurtenissen, actoren en rollen plat; overige typen per taakveld/beleidsdomein.
- A8 Brontype-indeling: verordening = wet, VNG-handreiking = beleid, standaard/catalogus = informatiemodel, GEMMA-model = model.
- A9 Elke rij in de relatietabel is vastgelegd op het bronelement; de richting volgt de ArchiMate-relatie.

## Verificatie

- `uv run pytest`:
  - core: gate (kandidaat niet gepromoveerd), guard recursief, schema per paginatype, dode links, `runs.start` met `begrippen/` + bronvoorrang, `source add --url`/pdf;
  - `bepaal_type`: een tabel met testbegrippen die T1–T7 dekken, en de SKILL.md-tabel gelijk aan de `--markdown`-uitvoer;
  - `relaties.py`: optillen, keten met het zwakste type, "leidt tot" → association + terugmeldkandidaat, composite → composition, een ongeldige ArchiMate-combinatie wordt geweigerd;
  - definities: een formele definitie met een bron van brontype beleid wordt geweigerd.
- `uv run llmwiki lint` + `harness check` slagen.
- `ggm.py velden <guid>` levert voor 3 bekende GUID's dezelfde waarden als de oude enrich (oude pagina's alleen gelezen). `gemma.py` parset het huidige GEMMA-`.archimate` en vindt voor dezelfde 3 elementen de GEMMA-tegenhanger.
- In Obsidian (root-vault): een link in `## Relaties` verschijnt als backlink op de doelpagina.
- End-to-end met één testbron: `run start --onderwerp` → ingest → assess (één `review`, één `kandidaat`) → write (inclusief relatie en terugmelding) → validate met bewust ingebrachte fouten → `promote plan`. Alleen de review-pagina wordt `goedgekeurd`. Apply alleen na AKKOORD.
- Later, vóór de exportbouw: een deel-`.archimate` importeren in een kopie van het GEMMA-model in Archi zonder dubbele mappen (§5).
