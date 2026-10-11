# Plan: bronnen, inhoud en indelingen

Na akkoord komt dit plan letterlijk in `wikis/gemma-archimate-model/plannen/2026-10-10-indelingen.md`. Basis: main op a3c7250.

## 1. Doel

**Aanleiding.** De todo *Map indelingen/* en de acht waarschuwingen "model als bron" bij de functies boven het niveau van een onderwerp.

**Doel.** Helder krijgen hoe de wiki omgaat met bronnen, inhoud en indelingen, en dat vastleggen in de architectuur. Daarbij twee aanvullende doelen:

- een folderstructuur die overzichtelijk is voor de redacteur;
- het GEMMA-model, het GGM en de UPL herbruikbaar maken voor andere wiki's.

## 2. Uitgangspunten, en wat ze in de architectuur aanvullen of vervangen

| # | Uitgangspunt | Wat er nu staat | Wat er verandert |
|---|---|---|---|
| U1 | **Inhoud komt uit bronnen** die voor alle gemeenten gelden (wetten), en wordt daarna gematcht met GEMMA. Functies zijn geen uitzondering | Wiki-ARCH 3.4: een landelijke wettelijke grondslag per element. Wiki-ARCH 4.4 (*Plek in een GEMMA-indeling*): "Wat een bedrijfsfunctie is, staat wel in redactionele tekst en heeft daar zijn bron" | 3.4 blijft. De zin over redactionele tekst in 4.4 wordt **vervangen**: een functie heeft een bron zoals elk element |
| U2 | **Een bron heeft een rol, los van haar vorm.** *Bron voor de inhoud*: wetten en andere landelijke bronnen. *Bron voor de methode*: Over GEMMA, Proceshiërarchie en Impact van ketensamenwerking voor het kennismodel. *Matchdoel*: het GEMMA-model en GEMMA Online zijn allebei inhoud van GEMMA (gestructureerd en ongestructureerd, ze vullen elkaar aan), plus het GGM; de UPL is bron én matchdoel. De vorm (document of model) bepaalt alleen de map in `sources/` (U6) | Wiki-ARCH 2 noemt Over GEMMA een matchdoel, en alleen het GEMMA-model als inhoud van GEMMA. Regel Bronvoorrang: "alleen de redactionele tekst ervan is bron, van brontype `overig`" | Wiki-ARCH 2 wordt **vervangen** door de drie rollen (zie §2a), met de context dat de wiki later naar conflicten met GEMMA Online kijkt (§4). Bronvoorrang wordt **vervangen**: een inhoudspagina van GEMMA Online krijgt brontype `model` (matchdoel); een methodepagina en Over GEMMA houden `overig` |
| U3 | **Soorten indelingen.** *Ontstaan uit de bronnen*: de thuisonderwerpen samen, de Procesindeling naar kernobject en de Grondslagindeling. *Overgenomen uit modellen*: GEMMA (functiehiërarchie, domeinen, Beleidsdomeinindeling), Iv3, GGM-beleidsdomeinen en UPL; later NORA. *De ArchiMate-indeling* (architectuurlaag › elementtype, uit de ArchiMate-standaard) ordent geen inhoud maar de wiki zelf: het kennismodel, de elementpagina's, de mappen in de Archi-export en de typen van de beslistabel. Overlap mag. Indelingen zijn niet leidend en worden later geconsolideerd | Wiki-ARCH 4.4 *GEMMA volgen*: "Een nieuwe indeling komt er alleen waar GEMMA er geen heeft". Wiki-ARCH 3.3 noemt onderwerpen alleen voor het thuishoren | 4.4 wordt **vervangen** door de twee soorten, met de regel dat overlap mag. 3.3 wordt **aangevuld**: de thuisonderwerpen samen zijn een ontstane indeling, met de criteria van §3. Nieuw in `todo.md`: een plan voor consolidatie |
| U4 | **Overnemen is letterlijk.** Een overgenomen indeling komt as-is uit het model, zonder beoordeling en zonder bron. Een wiki-element hangt erin met de relatie uit het model (`gemma_relatie`), of met een bron als het model die relatie niet heeft | Wiki-ARCH 4.1 *Groepering*: een groepering krijgt geen beoordeling. Wiki-ARCH 4.4 *Alles ingedeeld*: een functie zonder match breidt de keten uit | 4.1 wordt **aangevuld**: ook de functies in een overgenomen hiërarchie zijn knopen zonder beoordeling. Een functie wordt alleen een wiki-element als een onderwerp haar betekenis geeft, met een bron. De acht functies vervallen als beoordeling |
| U5 | **Export van een indeling**: per overgenomen indeling de gebruikte takken tot en met de wortel, letterlijk (§5) | Wiki-ARCH 6.5 *Indelingen*: aggregatie vanuit de groepering van GEMMA | 6.5 wordt **aangevuld** met het meenemen tot de wortel, het niet overschrijven van knopen en de optie `--volledig` |
| U6 | **Modellen en lijsten zijn bronbestanden.** Ze staan in `sources/modellen/` met hun omzetting naar JSON, zoals een pdf naar Markdown. De omzetting zit in llmwiki; elke wiki maakt een eigen bronduiding | Repo-ARCH *Bronnen: drie lagen*: laag 1 is `sources/raw/`. Wiki-ARCH 6.4: de modellen worden gelezen via `gemma/` en `ggm/` in de wiki | Laag 1 wordt **aangevuld** met `sources/modellen/`. Wiki-ARCH 6.4 wordt **vervangen**: de tools lezen de JSON in `sources/modellen/`; `gemma/` en `ggm/` vervallen |
| U7 | **Eerst voorleggen wat onderhoud vraagt.** Informatie die bij elke wijziging bijgehouden moet worden (tellingen, samenvattingen van lijsten, wijzigingen per release) komt pas in een pagina of overzicht na een besluit van de redacteur, en alleen als llmwiki of de AI haar nodig heeft | — (nieuw) | Nieuw in repo-AGENTS.md (Werkwijze) en repo-ARCH. Dit plan legt daarom de dekking per indeling voor (§5); de bronduidingen bevatten alleen stabiele inhoud (§6) |

Wiki-ARCH 3.1 (herleidbaarheid) en 3.5 (GEMMA volgen of afwijken en terugmelden) blijven gelden. Zij krijgen alleen verwijzingen naar U2 en U4.

### 2a. Over GEMMA: waarom geen matchdoel

Wiki-ARCH 2 noemt Over GEMMA nu een matchdoel, omdat de export per elementtype en relatietype aangeeft of het *in Over GEMMA* staat. Dat is een vergelijking van het kennismodel van de wiki met dat van GEMMA, niet het matchen van inhoud.

Over GEMMA bevat de metadata van GEMMA: de elementtypen, de relaties en de werkwijze. Daarmee is het een **bron voor de methode**, net als Proceshiërarchie. De markering *in Over GEMMA* blijft. Zij laat zien waar het kennismodel van de wiki afwijkt, en dat is een kandidaat voor een terugmelding (wiki-ARCH 3.5).

In `sources/` staat Over GEMMA in `modellen/`, vanwege de vorm (XML met JSON-omzetting), en met brontype `overig` (de methode).

## 3. Criteria voor de ontstane indeling: de onderwerpen

Nu staan ze nergens expliciet. Er is alleen de regel Thuishoren (waar een element thuishoort) en stap 1 van skill `gemma-archimate-model-update` (een onderwerp maak je "in overleg"). In de praktijk zijn de onderwerpen zo ontstaan:

- Lijkbezorging uit de Wet op de lijkbezorging;
- Burgerzaken uit de Wet BRP, BW 1, de Paspoortwet en andere wetten.

**Voorstel voor expliciete criteria** (komen in de regel Thuishoren en in wiki-ARCH 3.3; leg ik apart voor):

1. **Eigen onderwerp.** Eén samenhangende taak van de gemeente uit landelijke regelgeving, met eigen kernobjecten die de gemeente over hun hele levensloop beheert (Graf, Reisdocument). Het onderwerp heet naar die taak.
2. **Thematisch gedeeld onderwerp.** Begrippen die meer eigen onderwerpen op dezelfde manier gebruiken en uit een eigen algemene regeling komen: de Awb voor Besluitvorming, de Gemeentewet voor Bestuur en organisatie, de belastingwetgeving voor Heffingen en betalingen.
3. **Kern.** Wat overal voorkomt en te breed is voor een thema, bij voorkeur met een match in GGM 99-kern.
4. **Geen onderwerp** wordt een indeling uit een model, zoals de functiehiërarchie of een beleidsdomein. Die staat ernaast (U3).

**Het niveau in deze indeling.** Het veld `laag: thematisch | kern` in een onderwerp is het niveau in de ontstane onderwerpen-indeling (eigen › thematisch › kern). Een eigen onderwerp heeft nu géén waarde. Het woord *laag* betekent in de wiki al de architectuurlaag en de bronlaag (laag 1–3). **Voorstel:** hernoem het naar `niveau: eigen | thematisch | kern`, met `eigen` expliciet.

## 4. GEMMA Online, de wikis `gemma` en `gemma-online`, en conflicten

**De wiki `gemma` bestaat niet meer als wiki.** Hij is hernoemd naar `gemma-online` (commit e15b04d). Wat in `wikis/gemma/` overbleef, zijn drie lokale testvoorstellen voor publiceren van 28 september (`akkoord_voor_publicatie: nee`). Ze zijn genegeerd door `.gitignore` en staan niet in Git. **Voorstel:** verwijder de map in fase 0. Verwijderen is onomkeerbaar; met je akkoord op dit plan doe ik het.

De wiki die GEMMA Online beheert met pywikibot, is dus `gemma-online`. Dit past in de opzet, als de uitwisseling via `sources/` en terugmeldingen loopt en nooit via links tussen wiki's (repo-ARCH: "Een wiki verwijst niet naar pagina's van een andere wiki"). Er ontstaan dan twee kopieën, elk met een eigen doel:

| Kopie | Waar | Wat | Doel |
|---|---|---|---|
| Momentopname | `sources/` | een volledige kopie van GEMMA Online (productie), opgehaald met pywikibot, nooit bewerkt (laag 1, brontype `model`) | bron en matchdoel voor elke wiki |
| Werkkopie | `wikis/gemma-online/content/` | een gedeeltelijke sync van de redactieomgeving (redactie.gemmaonline.nl), die wordt bewerkt en na akkoord gepubliceerd | pagina's op GEMMA Online beheren |

De stroom is dan:

1. Deze wiki vergelijkt haar inhoud met de momentopname. Een conflict wordt een GEMMA-terugmelding.
2. De wiki `gemma-online` verwerkt zo'n terugmelding in haar werkkopie, met haar eigen sync-workflow.
3. Een nieuwe momentopname laat het resultaat zien.

Waar het inzicht komt:

- In de AGENTS.md van `gemma-online` (sectie Domein), want het is vooral daar van belang: de twee kopieën en hun verschil.
- Als context in repo-ARCH (de keten) en wiki-ARCH 2.
- Het ophalen van de momentopname en de conflictcontrole komen in `todo.md`.

## 5. Export en dekking

**Export.** Je importeert eerst in een tussenmodel, controleert daar het resultaat en maakt er views; daarna importeer je in GEMMA. Daarom:

- **Standaard.** Per overgenomen indeling elke gebruikte tak helemaal, tot en met de wortel. Alle knopen op de weg gaan letterlijk mee, met GEMMA-id's en de GEMMA-relatie-id's, en worden niet als wiki-element overschreven.
- **Met `--volledig`.** De hele indeling, om in het tussenmodel de gaten te zien.
- **De onderwerpen-indeling** gaat pas mee na de consolidatie. GEMMA heeft er geen tegenhanger van, dus het zouden nieuwe groeperingen zijn.

**Dekking: wie maakt het en wanneer.** De dekking is onderhoudsgevoelig (U7), daarom leg ik haar hier voor. Ze wordt volledig gegenereerd, dus niemand houdt haar met de hand bij. Ze is nodig om de gaten te zien die de bronnen nog niet hebben gevonden.

| Wat | Tool | Stap (skill `gemma-archimate-model-update`) |
|---|---|---|
| Pagina per indeling: de hele indeling as-is, per knoop de wiki-elementen eronder en of er inhoud onder hangt | `tools/render.py` | stap 4, *Beslissen en renderen* (bij elke run); ook na een nieuwe release (skill `-gemma-release`) |
| Telling per indeling: knopen met en zonder inhoud | `tools/archimate_export.py`, in het exportrapport | stap 9, *Exporteren* |

## 6. Bronduidingen (laag 3)

Een bron uit de bronnen van een onderwerp heeft haar bronduiding in `onderwerpen/<onderwerp>/bronduidingen/`, bij het onderwerp waarin ze het eerst is geduid. Dat zijn dezelfde sleutels als nu in `bronanalyses/<onderwerp>/` en `beoordelingen/onderwerpen/`. Nieuw zijn de bronduidingen van GEMMA, GGM en UPL in `modellen/<model>/bronduidingen/`.

Volgens U7 bevat een bronduiding alleen stabiele inhoud: geen tellingen, geen wijzigingen per release, geen samenvatting van terugmeldingen.

- **GEMMA-model:**
  - de rol van het model voor de wiki: matchdoel, de id's in de export, wat de import overschrijft en wat niet;
  - welke delen de wiki gebruikt: de elementtypen en de overgenomen indelingen;
  - welke eigenschappen de wiki leest (GEMMA type, Object ID, profielen). Die heeft de AI nodig bij het matchen.
- **Over GEMMA**: de bestaande analyse, verplaatst, als bron voor de methode (§2a).
- **GGM, hoog over:**
  - wat het GGM is;
  - de opbouw: beleidsdomeinen en 99-kern;
  - de verhouding tot GEMMA: bedrijfsobject en entiteit;
  - wat het betekent voor het model: matchdoel voor bedrijfsobjecten, data-objecten en beleidsdomeinen, en dekking per beleidsdomein.

  Erbij komt een nieuwe bron: het ongestructureerde deel van het GGM (https://www.gemeentelijkgegevensmodel.nl/latest/). Welke pagina's erbij horen, leg ik eerst voor.
- **UPL**: de echte bron en de aangevulde lijsten.
  - De echte bron is de UPL van Logius (https://data.overheid.nl/dataset/uniforme-productnamenlijst). Die is nieuw.
  - De aangevulde lijsten extern en intern van GEMMA Online zijn de bestaande bronnen. Ze zijn de uitzondering: een bron die wel van GEMMA Online komt.
  - Hoog over in de bronduiding:
    - een UPL-item wordt altijd een dienst;
    - diensten met en zonder landelijke grondslag;
    - welke diensten voor gemeenten zijn, uit de landelijke lijst;
    - wat de aanvulling van GEMMA toevoegt (taakveld, GEMMA-domein, soort).
  - Een twijfelgeval: één element is nu een product, Grafuitgifte. Dat leg ik voor.

## 7. Plattegrond

Twee ordeningen naast elkaar: wat uit de bronnen ontstaat, staat per onderwerp; wat van een model komt, staat per model. Elementpagina's volgen de ArchiMate-indeling.

```text
second-brain/
├── sources/
│   ├── raw/          documenten en pagina's: origineel + Markdown (o.a. de aangevulde UPL-lijsten van GEMMA Online)
│   ├── modellen/     modellen en lijsten: origineel + JSON — GEMMA-model, GGM, Over GEMMA, UPL (Logius)
│   └── index/        technische index per bron
└── tools/llmwiki/modellen/   omzetting ArchiMate, XMI en UPL → JSON (gedeeld)

wikis/gemma-archimate-model/
├── ARCHITECTURE.md · AGENTS.md · wiki.yaml · todo.md · log.md · plannen/ · kennismodel/
├── onderwerpen/<onderwerp>/              de ontstane indeling: per onderwerp alles bij elkaar
│   ├── afbakening.yaml                   naam, niveau, status, omschrijving (kernobjecten, wat erbuiten valt), bronnen, besluiten
│   ├── beoordelingen/<id>.yaml           de begrippen met dit thuisonderwerp
│   ├── bronduidingen/<brontype>/<bron-id>.md
│   ├── begrippen.md                      gegenereerd: de begrippenlijst
│   └── overzicht.md                      gegenereerd: de views op de indelingen
├── modellen/<model>/                     per model: bronduidingen, overgenomen indelingen en terugmeldingen
│   ├── gemma/
│   │   ├── bronduidingen/<brontype>/…     GEMMA-model (matchdoel); Over GEMMA, Proceshiërarchie, Impact (methode)
│   │   ├── indelingen/beleidsdomeinen.yaml   register
│   │   ├── terugmeldingen/{gemma-team,procesarchitectuur}.yaml   registers (AI)
│   │   └── terugmeldingen/{gemma-team,procesarchitectuur}.md     gegenereerd
│   ├── ggm/
│   │   ├── bronduidingen/<brontype>/…     GGM, GGM-website
│   │   └── terugmeldingen.yaml · terugmeldingen.md
│   └── upl/
│       └── bronduidingen/<brontype>/…     UPL Logius, aangevulde lijsten
├── elementpaginas/                       gegenereerd, volgens de ArchiMate-indeling (gespiegeld aan kennismodel/)
│   ├── bedrijfsarchitectuur/<type>/…
│   ├── motivatie/beleidskaders/…
│   └── overig/indelingen/{onderwerpen,beleidsdomeinen,bedrijfsfuncties,…}.md   de groeperingen, met dekking
├── ter-beoordeling.md · voortgang.md     gegenereerd
└── export/ · schemas/ · tools/
```

**Terugmeldingen bij hun model.**

- Een terugmelding gaat naar de beheerder van een model, en staat daarom bij dat model, met het register (AI) en de gegenereerde lijst naast elkaar.
- De procesarchitectuur (de UPL-lijsten van GEMMA en het kennismodel) is van GEMMA. Haar register staat daarom bij `gemma/`.
- Komt er een terugmelding aan Logius over de UPL zelf, dan krijgt `upl/` een eigen register.

**`objecten.yaml` vervalt; het wordt een veld in de beoordeling.**

Wat het is:

- De export geeft een nieuw element een vast Archi-id dat is afgeleid van het begrip-id.
- Wordt een begrip hernoemd (`lijk` → `stoffelijk-overschot`), samengevoegd of gesplitst, dan krijgt het een nieuw begrip-id en dus een nieuw Archi-object. Jouw views in Archi werken dan niet meer.
- `beoordelingen/objecten.yaml` legt daarom vast welk oud object het element voortzet. Er staan nu 6 regels in, alle zes hernoemingen uit lijkbezorging van 2026-10-05.

Waar het beschreven is:

- de regel Objectbehoud (modelleerregels);
- wiki-ARCH 6.5 (*Objectbehoud*);
- skill `gemma-archimate-model-archimate-export`;
- de tools: `archimate_export.py` (`object_sleutels`, die ook een typewijziging weigert) en `beslissen.py` (de controle van het register).

Waarom het geen register moet zijn: het is een feit over één element, en een besluit van de redacteur over dat element hoort bij het begrip (wiki-ARCH 3.1).

**Voorstel:** het veld `object_van` (met `wijziging` en `datum`), letterlijk verhuisd naar de beoordeling van het element. Het register vervalt.

- De zes beoordelingen veranderen daardoor van inhoud. Ze worden `review` en vragen opnieuw AKKOORD; ik leg ze samen met fase 5 voor.
- Werk de regel Objectbehoud, wiki-ARCH 6.5, de skill, het schema (`bepaal_type.py`), `beslissen.py` en `archimate_export.py` bij.

**`afbakening.yaml`** (nu `beoordelingen/onderwerpen/<onderwerp>.yaml`). Het bestand bevat naam, niveau, status, omschrijving, bronnen en besluiten over het onderwerp als geheel. De kern ervan is de afbakening: welke kernobjecten erbij horen en wat erbuiten valt.

**Bronduiding.** Laag 3 heet voortaan *bronduiding*: de uitleg van wat een bron betekent vanuit het perspectief van de wiki. Het woord is kort en onderscheidend: geen samenvatting van de bron en geen analyse in het algemeen, maar haar betekenis voor deze wiki. Het vervangt *domein-lens* (repo-ARCH, repo-AGENTS.md) en *bronanalyse* (deze wiki), overal:

- de mappen: `onderwerpen/<onderwerp>/bronduidingen/` en `modellen/<model>/bronduidingen/`;
- het paginatype in `wiki.yaml` en het schema (`schemas/bronduiding.schema.json`, `type: bronduiding` in de frontmatter);
- de tools (`gam_gemeen`, `render`, `beslissen`), de skills (ook de gedeelde, zoals `wiki-ingest`) en llmwiki (`source bronregel`);
- de regels en de architectuur (regel Eén naamgeving).

**Elementpagina's horen niet onder een onderwerp.** Ze volgen de ArchiMate-indeling (U3), net als het kennismodel en de mappen in Archi:

- Een element komt één keer voor in het hele model, en meer onderwerpen gebruiken het.
- Een verhuizing van thuisonderwerp verandert het pad van de pagina niet, dus links naar de pagina blijven werken.
- Een onderwerp toont zijn elementen in `begrippen.md` en `overzicht.md`.

**Wat deze opzet kost.**

- `curation.beoordelingen` in `wiki.yaml` wordt een patroon (`onderwerpen/*/beoordelingen`). Dat raakt `tools/llmwiki/{beoordeling,akkoord}.py`.
- De thuis volgt uit de map. `beslissen.py` controleert dat het eerste item in `onderwerpen` gelijk is aan de map.
- In een onderwerpmap staan handwerk en gegenereerde bestanden naast elkaar. De render beheert daar alleen `begrippen.md` en `overzicht.md`.
- Een bron die meer onderwerpen gebruiken, staat bij één onderwerp. Zo werkt het nu ook.
- `gam_gemeen.bronduidingen` en `bron_doel` zoeken in `onderwerpen/*/bronduidingen/` en `modellen/*/bronduidingen/`.

## 8. Fasen

**Werkwijze:**

- Twijfelgevallen één voor één voorleggen, met de bronpassage en per optie wat er gebeurt.
- Het woord AKKOORD typt alleen de redacteur.
- Elke fase eindigt met een commit op main.
- Bij een wissel van denkniveau meld ik dat in één zin.

**Fase 0 — Werkplek (laag).**

- Draai `workspace-check --fix`; dat herstelt de verouderde harness-kopie van skill `gemma-archimate-model-beoordelen`.
- Verwijder `wikis/gemma/` (§4).
- Sla dit plan op in `plannen/`.

**Fase 1 — Architectuur (hoog).**

- Zet de inzichten in de architectuur: kort, compleet en goed leesbaar, elk op één plek, met verwijzingen in plaats van herhaling.
  - **Repo-ARCH** (geldt voor alle wiki's):
    - de rol van een bron los van haar vorm (U2): bron voor de inhoud, bron voor de methode, matchdoel;
    - `sources/modellen/` met de JSON-omzetting door llmwiki (U6);
    - ontstane en overgenomen indelingen (U3), waarbij overlap mag en consolidatie later volgt;
    - de keten met twee kopieën van een externe site (momentopname in `sources/`, werkkopie in een sync-wiki), en uitwisseling via `sources/` en terugmeldingen (§4);
    - U7: eerst voorleggen wat onderhoud vraagt.
  - **Wiki-ARCH** (deze wiki): de tabel van §2 sectie voor sectie, §2a (Over GEMMA), §3 (criteria voor onderwerpen) en §5 (export en dekking).
  - **`docs/onderbouwing.md`**: het waarom per keuze, kort.
- Pas de regels Bronvoorrang, Elke claim een bron en Thuishoren aan.
- Vervang *domein-lens* en *bronanalyse* door *bronduiding* in repo-ARCH, repo-AGENTS.md, wiki-ARCH, AGENTS.md, de regels, de skills (ook de gedeelde) en de teksten van llmwiki.
- Zet U7 in repo-AGENTS.md.
- Zet de twee kopieën van GEMMA Online in de AGENTS.md van `gemma-online`.
- Leg de criteria van §3 een voor een voor, en het voorstel `niveau`.
- `todo.md` krijgt: consolidatie van indelingen, de conflictcontrole met GEMMA Online, en pywikibot-momentopnamen in `sources/`.

Commit.

**Fase 2 — Folderstructuur (middel).** Ik verplaats alles op bestandsniveau met `git mv`, volgens de plattegrond van §7, met de hernoeming naar `afbakening.yaml` (commit 1) en het veld `niveau` (commit 2). Dat is veiliger dan in Obsidian, omdat Obsidian ook links in andere bestanden herschrijft.

- Commit 1 bevat alleen de verplaatsingen (ook `bronanalyses/` → `bronduidingen/` en `schemas/bronanalyse.schema.json` → `schemas/bronduiding.schema.json`), zodat Git ze als verplaatsing herkent en `git log --follow` werkt. De lint staat in `sources/` een verplaatsing zonder inhoudswijziging toe.
- Commit 2 bevat de reparaties: tools, `wiki.yaml` (paginatype `bronduiding`), `type:` in de frontmatter, links, skills, documentatie en opnieuw renderen.
- Commit 3: `objecten.yaml` wordt het veld `object_van` in de zes beoordelingen (§7).

**Fase 3 — Modellen herbruikbaar (middel).**

- `parse_archimate` en `parse_ameff` (`tools/gemma.py`) en `parse_xmi` (`tools/ggm.py`) gaan naar `tools/llmwiki/modellen/`; er komt een omzetting voor de UPL bij. Het JSON-formaat wordt gedocumenteerd.
- `llmwiki source add` met `brontype model` schrijft het origineel en de JSON naar `sources/modellen/`.
- `sources.py` zoekt in `raw/` en `modellen/`. `lint.py` en `markdown.py` gelden ook voor `modellen/`.
- Over GEMMA houdt `brontype: overig` (methode), maar staat vanwege de vorm in `modellen/`.
- `tools/gemma.py` en `tools/ggm.py` lezen de JSON.
- De skills `-gemma-release` en `-ggm-release` worden aangepast, en er komen tests.

Commit.

**Fase 4 — Bronduidingen (hoog).**

- Schrijf de bronduidingen van §6.
- Neem de nieuwe bronnen op met skill `wiki-ingest`: de UPL van Logius en de GGM-website (eerst de selectie van pagina's voorleggen).
- Werk de bronnen en de omschrijving van Kern bij.

Commit.

**Fase 5 — Indelingen en functies (middel; de twijfelgevallen hoog).**

1. **Het register** van beleidsdomeinen verhuist letterlijk naar zijn nieuwe plek.
2. **De functiehiërarchie** wordt as-is gelezen uit de JSON (`tools/gemma.py`).
3. **Een nieuw veld `gemma_functie`**: de plek van een wiki-functie of -dienst in de hiërarchie, met `id` en daarnaast `gemma_relatie` of `bronnen` met `vindplaats`. Het raakt het schema (`bepaal_type.py`), de controle (`beslissen.py`, hergebruik van `_controleer_gemma_relaties`), de render, `kennismodel.py` en de export (§5).
4. **Indelingspagina's** in `elementpaginas/overig/indelingen/` voor de onderwerpen, de beleidsdomeinen en de bedrijfsfuncties, met dekking.
5. **Mechanisch** (regel Letterlijk verplaatsen):
   - De aggregatie van een bovenliggende functie wordt `gemma_functie` bij het kind. Dat zijn 14 kinderen: 6 wiki-functies en 8 diensten.
   - De acht beoordelingen vervallen.
6. **Twijfelgevallen, één voor één:**
   1. Bediening met een wettelijke bron door een bovenliggende functie. Producten- en dienstenrealisatie fysieke leefomgeving bedient Verlenen verlof tot ontleding (Wlb art. 68) en Afgeven laissez-passer (BOL art. 11). Vergunningenbeheer Publieksdiensten bedient Stellen andere termijn (Wlb art. 17). Opties: de functie blijft een wiki-element, de relatie gaat naar een lagere functie, of de relatie vervalt.
   2. De realisatie van Legalisatie handtekening door Producten- en dienstenrealisatie publieksdiensten.
   3. Een wettelijke bron voor *gedrag* (en bij twee ook *eigen identiteit*) in plaats van *Bedrijfsfuncties*: Bevolkingsadministratie bijhouding, Nederlanderschap diensten, Officiële documenten verstrekking en Verkiezingen gerelateerde diensten.
   4. Grafuitgifte als dienst (§6, UPL).
   5. Besluiten in Kern (herziening van het besluit over Producten- en dienstenrealisatie publieksdiensten) en in Lijkbezorging.
7. **Bronduidingen die vervallen:** die van Bedrijfsfuncties en van de drie pagina's over de bedrijfsarchitectuur per domein.
8. **Afronden.**
   - Werk de skills, de kaart in AGENTS.md en `todo.md` bij.
   - Draai `beslissen` en `render`, en leg voor met `promote plan`. Na AKKOORD: `promote apply`, de export en een commit.

**Daarna:** Besluitvorming (Awb, Belanghebbende, Aanvraag, Bestuursorgaan).

**Sessies:**

- Fase 0 en 1 in deze sessie.
- Fasen 2 tot en met 4 in een nieuwe sessie.
- Fase 5 in een nieuwe sessie.

Aan het eind van elke sessie geef ik een startprompt.

## 9. Verificatie

- `uv run pytest tests wikis/gemma-archimate-model/tools/tests`
- `tools/beslissen.py`: 0 fouten en geen waarschuwing "model als bron"
- `tools/render.py --check`
- `uv run python -m llmwiki lint` en de pre-commit-controles
- `git log --follow` op een verplaatst bestand toont de oude geschiedenis
- De JSON in `sources/modellen/` is gelijk aan de huidige `*_parsed.json`; `tools/gemma.py kandidaten` en `tools/ggm.py kandidaten` geven dezelfde uitkomst als ervoor
- `tools/archimate_export.py --concept`: de gebruikte takken staan er tot en met de wortel in, met GEMMA-id's, en het rapport toont de dekking; met `--volledig` staat de hele indeling erin
- `workspace-check`: `ok`

## 10. Besluiten in fase 5

De besluiten over de twijfelgevallen (§8, fase 5, punt 6), zoals de redacteur ze nam. Ze worden verwerkt in de beoordelingen, de afbakeningen en de regels; dit is het verslag.

1. **Bediening door een bovenliggende functie** (2026-10-11).
   - Producten- en dienstenrealisatie fysieke leefomgeving vervalt als wiki-element en wordt een knoop van de functiehiërarchie; de bediening van Verlenen verlof tot ontleding (Wlb art. 68) en Afgeven laissez-passer (BOL art. 11) vervalt. De bron noemt de burgemeester en de handeling, niet de functie, en GEMMA heeft onder deze functie geen bladfunctie voor de verloven bij lijkbezorging. De drie diensten krijgen `gemma_functie` met de UPL als bron.
   - Vergunningenbeheer Publieksdiensten blijft een wiki-element: een bladfunctie die Stellen andere termijn (Wlb art. 17) bedient, zoals de zes andere bladfuncties. Zij krijgt `gemma_functie` met de GEMMA-relatie; haar diensten blijven een aggregatie.
   - Daarmee geldt: een bladfunctie van GEMMA die een proces van een onderwerp bedient, met een bron, wordt een wiki-element; een functie erboven is een knoop zonder beoordeling.
2. **Legalisatie handtekening en de UPL-diensten zonder grondslag** (2026-10-11).
   - Legalisatie handtekening is een UPL-dienst (Logius: gemeente, burger, medebewind, zonder grondslag; GEMMA-lijst extern nr. 226 met art. 23 Wet griffierechten burgerlijke zaken, dat alleen het griffierecht van de rechtbank regelt). Een landelijke bevoegdheidsgrondslag is opnieuw niet gevonden. De dienst blijft in de wiki (UPL-regel), wordt teruggemeld aan de procesarchitectuur als geen wettelijke taak, en gaat niet naar GEMMA.
   - Regel, vereenvoudigd: een UPL-dienst zonder landelijke wettelijke grondslag wordt in de wiki uitgewerkt voor zover mogelijk (een element met pagina, zonder processen, objecten, gebeurtenissen of rollen), teruggemeld aan de procesarchitectuur en niet geëxporteerd. Een VNG-model is nooit grondslag: de relatie heet altijd *werkt uit voor* (Asverstrooiing, Gedenkteken plaatsingsvergunning en Grafonderhoud vallen daarmee ook in deze groep).
   - De hoek *zonder grondslag*: het script herkent de groep (UPL als bron, geen bron van `europese-regelgeving` of `rijksregelgeving`, geen *is grondslag voor* van een beleidskader van de EU of het Rijk). Zo'n dienst krijgt een melding op haar pagina en staat op de gegenereerde lijst `elementpaginas/overig/zonder-grondslag.md` met haar terugmelding; de export laat haar weg en het rapport noemt haar; de kernrelatie hoeft geen relatie naar een element te zijn (het kenmerk *gerealiseerd door* steunt op de bron); een signaal als de terugmelding ontbreekt.
3. **Bron voor wat een functie is** (2026-10-11).
   - De kenmerken die op de pagina Bedrijfsfuncties of op het GEMMA-model steunen, krijgen de wet die de groep taken aan de gemeente toewijst, zoals bij Burgerlijke stand diensten: Bevolkingsadministratie bijhouding (Wet BRP art. 1.4 lid 1), Nederlanderschap diensten (Besluit verkrijging en verlies Nederlanderschap art. 2), Officiële documenten verstrekking (Paspoortwet art. 40 lid 1; Wegenverkeerswet 1994 art. 116 lid 1), Verkiezingen gerelateerde diensten (Kieswet art. D 1, J 7) en Vergunningenbeheer Publieksdiensten (Wlb art. 17 lid 1).
   - Regel, bij de voorrangsregels (regel Bronvoorrang): VNG-modellen en GEMMA Online zijn voor matchen, niet een bron voor een claim; net als gemeentelijke beleidsstukken mogen ze worden gebruikt voor de termen en de taal. De regel geldt nu; de herbeoordeling van de elementen die op een VNG-model steunen (vooral de Model beheersverordening begraafplaatsen, 42 elementen), en de vraag of Model-APV en Model beheersverordening beleidskader blijven, is een eigen klus in `todo.md`.
4. **Grafuitgifte** (2026-10-11). Grafuitgifte (UPL nr. 165) wordt een dienst, volgens de regel dat een UPL-item altijd een dienst is; het besluit van 2026-10-05 (product bij een dienst met een afspraak) is herzien. Graf aanvragen gaat erin op: één dienst Grafuitgifte met de synoniemen Graf aanvragen en Grafrecht aanvragen, en de relaties van beide (Exploiteren van begraafplaatsen omvat haar, Verlenen grafrecht realiseert haar, zij bedient de Rechthebbende op het graf). Zij zet het Archi-object van Graf aanvragen voort (`object_van`, zelfde type). Er komt geen product; de afspraak Grafrecht blijft via Verlenen grafrecht.
5. **Besluiten in Kern en Lijkbezorging** (2026-10-11). Het resultaat telt, de besluiten zijn het log.
   - Resultaat: Kern houdt alleen de rol Ketenpartner, zonder bronnen; de omschrijving noemt alleen nog "rollen van GEMMA die in meer onderwerpen gelden, zoals Ketenpartner". In Lijkbezorging blijven van de functies Exploiteren van begraafplaatsen en Vergunningenbeheer Publieksdiensten; er is geen product meer; Verlenen verlof tot ontleding en Afgeven laissez-passer worden door geen functie bediend. Burgerzaken houdt haar vijf functies.
   - Het log: de bestaande besluiten blijven letterlijk, met een `stand` waar ze herzien zijn (Kern 2026-10-10 over Producten- en dienstenrealisatie publieksdiensten; Lijkbezorging 2026-10-05 over Grafuitgifte); de besluiten van de vervallen beoordelingen verhuizen letterlijk naar de afbakening van hun onderwerp, met `begrip`; per onderwerp één nieuw besluit van 2026-10-11 met dit resultaat. Het besluit van Graf aanvragen gaat mee naar Grafuitgifte.
