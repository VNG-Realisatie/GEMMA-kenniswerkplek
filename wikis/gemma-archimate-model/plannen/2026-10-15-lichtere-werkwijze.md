# Plan: lichtere werkwijze

Goedgekeurd door de redacteur op 2026-10-15. Basis: main op ffc0df1.

## Context

De redacteur vindt elke stap te zwaar (todo `wikis/gemma-archimate-model/todo.md`, Werkwijze lichter maken). **Lichter** betekent: minder AI-tokens, minder doorlooptijd, en minder vragen aan de redacteur of vragen die worden opgespaard. Meer scripts is prima. **Het belangrijkste blijft de kwaliteit van het ArchiMate-model (de export).** Herleidbaarheid en de publicatiegate blijven intact.

**Scope:** geen inhoudelijke wijzigingen. De beslistabel, de typen en de uitkomsten blijven gelijk, en de export blijft inhoudelijk gelijk. De ArchiMate-indeling als eerste selectie gaat naar de todo.

## Analyse

### Gemeten verbruik (transcripten van de Sessies, 2026-09-28 tot en met 10-15)

Besluitvorming deel 1 en 2 waren de laatste twee onderwerp-Sessies:

| Sessie | Beurten | Totale invoer | Uitvoer | Context bij de start → het eind |
|---|---|---|---|---|
| Deel 1 (2026-10-11) | 185 | 58 miljoen | 195.000 | 42.000 → 515.000 |
| Deel 2 (2026-10-12) | 156 | 48 miljoen | 189.000 | 43.000 → 487.000 |

Van de totale invoer komt 98% uit de cache. Dat is goedkoper, maar telt wel mee in het verbruik.

**Waar de context uit bestaat (deel 2, ongeveer):**

| Onderdeel | Aandeel | Toelichting |
|---|---|---|
| Uitvoer van commando's | ongeveer 60% | Vooral losse `sed -n`, `grep` en `cat` op bronnen, kennismodel, skills, references en beoordelingen (samen tientallen aanroepen). Scripts zoals `gemma.py zoek` zijn klein (ongeveer 3.000 tokens). Twee keer was de uitvoer zo groot dat die naar een bestand ging en opnieuw gelezen werd (ongeveer 9.000 tokens per keer). |
| Schrijven (heredoc, Write, Edit) | ongeveer 20% | Vooral beoordelingen en besluiten. |
| Start (systeem, AGENTS.md, lijst met skills) | ongeveer 15% | |
| Chat | ongeveer 3% | |

### Hoe context meetelt

Bij elke beurt gaat de hele context opnieuw als invoer naar het model. Daarom geldt:

> **Totale invoer ≈ beurten × startcontext + groei per beurt × beurten² / 2**

Voor deel 2: 156 × 43.000 + 2.800 × 156² / 2 ≈ 6,7 + 34 ≈ **41 miljoen**. Gemeten: 48 miljoen. Het model klopt dus in grote lijnen. Drie knoppen volgen daaruit:

1. **Minder beurten.** Het kwadraat telt het zwaarst: de helft van het aantal beurten geeft ongeveer een kwart van het kwadratische deel.
2. **Minder groei per beurt.** Minder lezen en schrijven per beurt.
3. **Kortere Sessies.** Dezelfde beurten verdeeld over k Sessies geven 1/k van het kwadratische deel. Wat tussen Sessies moet blijven, staat al in de werkboom.

Een grote context is ook slecht voor de kwaliteit: het model let slechter op details die ver terug staan, en bij een volle context vat het harness samen en gaat er informatie verloren.

### De duurste tussenproducten

1. **Ad-hoc lezen** van bronnen, regels en beoordelingen: de grootste post. Elke keer wordt opnieuw gezocht met `grep` en `sed`.
2. **Beoordelingen schrijven.** Een begrip kost ongeveer 980 woorden.
   - De kenmerken zijn 74% van de beoordeling; de nee 48%, en de standaardzin "Niet van toepassing" alleen al 31%.
   - In het hele corpus (453 bestanden) is dat samen 444.000 woorden.
3. **Regels.** Ongeveer 33.000 woorden, met ARCHITECTURE.md ongeveer 42.000.
   - De vragenlijst van de kenmerken staat twee keer: in de skill criteria (2.400 woorden) en in `kennismodel/kenmerken-en-beslistabel.md` (4.200 woorden).
4. **Bronduidingen.** 174 bestanden, samen 132.000 woorden.
5. **Besluiten.** 319 besluiten, waarvan 46 met een `stand` (herzien of nog open).
6. **Lange Sessies.** Een heel deel in één Sessie. De regel "Een onderwerp in één keer afronden" werkt dat in de hand.

### De beslistabel

[tools/bepaal_type.py](../tools/bepaal_type.py) toetst 60 kenmerken in een vaste volgorde:

| Stap | Kenmerken | Wat volgt |
|---|---|---|
| Poort | 6 | Bij een nee of ja hier valt het begrip af. Dat geldt voor 22% van de begrippen. |
| Aard | 8, precies één ja | Bepaalt welke groep daarna telt. |
| Type | De groep van die aard: soort gedrag 6, partij 6, regeling 3 of passief 10 | Het type. |
| Drempel en specialisatie | Alleen de kenmerken van dat type | Element of geen element, en het niveau. |

## Optimalisaties

**Knop:** N = minder beurten, g = minder groei per beurt, k = kortere Sessies, V = minder vragen aan de redacteur.

**Kwaliteit:** + beter, 0 neutraal, − risico.

**Besparing:** het aandeel in de totale invoer van een onderwerp (schatting met het model hierboven). Voor de stapnummers: zie de update-skill.

| # | Optimalisatie | Knop | Besparing | Kwaliteit |
|---|---|---|---|---|
| | **A. Een werkpakket in plaats van ad-hoc zoeken** | | | |
| A1 | **Werkpakket per onderwerp of cluster** (`tools/werkpakket.py <onderwerp> [--cluster <kernobject>]`). Eén bestand in `.work/` met alles wat het beoordelen nodig heeft: de begrippen uit de bronduidingen met de passages (via de regelnummers uit `sources/index/`), de treffers in de catalogus, de geldende besluiten, de GGM-, GEMMA- en UPL-kandidaten als compacte tabel, de relatievoorstellen, en welke modelleerafspraken gelden. Vervangt de tientallen `grep` en `sed` en de losse `kandidaten`-aanroepen. | N, g | −25 à −35% | + alles wat telt staat bij elkaar; minder kans om iets te missen |
| A2 | **Catalogus en opzoeken** (`tools/beoordeling.py zoek <naam>…`): naam, synoniemen, type, niveau, thuisonderwerp, kernobject en definitie van elk begrip, op één regel. Dit vervangt het knippen van de yaml: de kleine helft wordt gegenereerd. | g | (zit in A1) | + de regel Eén element in het hele model wordt betrouwbaarder |
| A3 | **Besluiten compact** (`beoordeling.py besluiten <onderwerp>`): alleen de geldende besluiten. | g | (in A1) | + geen verouderde besluiten in beeld |
| A4 | **Alleen het oordeel lezen** (`beoordeling.py toon <id> --oordeel`): zonder `beslist:` en zonder kenmerken buiten het pad. | g | −1 à −2% | 0 |
| A5 | **De vragen uit het script** (`bepaal_type.py vragen <id>`): het script geeft de kenmerken die in de volgende fase nodig zijn, met de vraag en de voorbeelden. De skill criteria en `kenmerken-en-beslistabel.md` hoeven bij het beoordelen niet meer gelezen te worden. | g | −5% | + precies de vragen die tellen, nooit een verouderde kopie |
| A6 | **Regels gericht laden**: de skills worden ingekort tot de stappen, met per stap de commando's. Per type lees je alleen zijn eigen modelleerafspraken (het werkpakket zegt welke). ARCHITECTURE.md hoort niet bij het beoordelen; sectie 4 wordt een verwijzing. | g | −8 à −10% | + een kleinere context; geen tegenspraak tussen samenvattingen |
| A7 | **Compacte uitvoer als standaard**: `beslissen.py` meldt alleen wat in deze run is gewijzigd, en hetzelfde geldt voor `promote plan`, het exportrapport, pytest (`-q`) en lint. Git: `export/*.archimate -diff` in `.gitattributes`, en in de skills `git diff --stat` of een filter op paden, nooit een volledige diff van gegenereerde bestanden. | g | −5% | 0 de volledige lijsten blijven in de bestanden |
| A8 | **Niet teruglezen**: na het schrijven niet opnieuw lezen. Het script valideert. | N, g | −2% | 0 |
| | **B. Een andere volgorde** | | | |
| B1 | **De beslistabel aflopen in twee fasen.** Fase A: poort, aard en de groep van die aard, met een stop als het begrip afvalt; elke nee in de groepen waarvan precies één kenmerk ja moet zijn, zonder onderbouwing. Fase B: alleen de kenmerken van het type, met onderbouwing; buiten het pad leidt het script nee af. | g | −5 à −8% (schrijven −50%) | 0 de nee die de uitkomst bepaalt, blijft als dubbelcheck |
| B2 | **Eerst het hele onderwerp in fase A, dan één tabel** voor de redacteur (type, niveau, kernobject, thuisonderwerp, open keuzes); fase B pas daarna. | N, V | −5% | + de keuze met de meeste gevolgen komt vroeg |
| B3 | **Eerst de catalogus**: een begrip dat al bestaat, krijgt alleen `onderwerpen` en `per_onderwerp` erbij. | g | −2% | + geen dubbele elementen |
| B4 | **Bronduiding na fase A**, alleen voor de delen van de wet (hoofdstukken of afdelingen) die een element onderbouwen. | g | −3% | 0; − een later onderwerp moet soms aanvullen |
| | **C. Scripts voor het schrijven** | | | |
| C1 | **Compacte schrijfvorm**: per kenmerk één regel (`herkenbaar: ja — onderbouwing [bron]`); `beoordeling.py normaliseer` maakt er de yaml van. | g | −2% | 0 |
| C2 | **Wijzigen met een commando** (`beoordeling.py zet <id> <veld> <waarde>`, `relatie <id> …`, `besluit <id> …`). | N, g | −3% | 0 |
| C3 | **Sjablonen voor patronen** (`beoordeling.py sjabloon <patroon> …`): bijvoorbeeld een UPL-dienst met een generiek proces en een kernobject (7 keer in deel 2). Het script zet de beoordelingen klaar met de kenmerken van fase A en de standaardrelaties. | N, g | −3 à −8%, afhankelijk van het onderwerp | + gelijke gevallen worden gelijk gemodelleerd; − een afwijking van het patroon kan gemist worden, daarom is de onderbouwing verplicht |
| C4 | **Citaten uit de vindplaats**: het script haalt het citaat uit `sources/raw/` en zet het in de bronduiding. | g | −1% | + het citaat is letterlijk |
| C5 | **Opschonen van de 453 bestaande beoordelingen** (eenmalig, voor B1), met de controle dat elke uitkomst gelijk blijft. | g | elke herlezing −50% | 0 gecontroleerd |
| | **D. Hergebruik** | | | |
| D1 | **Een precedent wordt een regel**: na drie gevallen legt de AI het voorstel voor; na akkoord komt de regel in het kennismodel. | V | klein | + consistent; de redacteur beslist over elke regel |
| D2 | **Eén bronduiding per deel van de wet**, gedeeld door de onderwerpen. | g | −1% | 0 |
| | **E. Kortere Sessies en een kleinere context** | | | |
| E1 | **Eén Sessie per fase**: (1) bronnen en fase A met de tabel; (2) fase B; (3) beslissen, voorleggen, promote, export en commit. De overdracht staat in de werkboom (beoordelingen, `vragen:`) en in de handoff. De denkniveaus wisselen toch al tussen de fasen. De regel "Een onderwerp in één keer afronden" wordt: in opeenvolgende Sessies, zonder ander werk ertussen. | k | −30 à −40% | + elke fase begint met een schone context |
| E2 | **Een beoordelingsagent voor fase B, per cluster** (een kernobject met zijn processen, gebeurtenissen en diensten), op denkniveau hoog, parallel. Vragen gaan in `vragen:`; de hoofdsessie bundelt ze en zet zo nodig dezelfde agent voort. Een agent controleert alleen zijn eigen bestanden (`beslissen.py --alleen <id>`). **Tokens:** na A tot en met E1 ongeveer neutraal, want elke agent heeft zijn eigen startcontext. De winst zit in doorlooptijd, in grote onderwerpen, en in kwaliteit. | k | 0 à −10% | + een kleine context per cluster; − relaties tussen clusters, opgevangen door fase A en de controle achteraf |
| E3 | **Afronden in één commando** (`tools/afronden.py`): na `promote apply` (dat los blijft, voor de klik van de redacteur) draaien export-check, export, lint en commit met het opgegeven bericht. | N | −2% | 0 de gate blijft |
| E4 | **Een kleine handoff**: verwijst naar de commits en de todo, herhaalt geen regels. De todo wordt gesplitst in actief en later (de wiki-todo is 2.000 woorden). | g | −1% | 0 |
| | **F. Vragen en besluiten** | | | |
| F1 | **Vragen opsparen** in `vragen:`, per fase in één tabel; alleen een blokkerende vraag komt meteen. | N, V | −3% | 0 |
| F2 | **Voorleggen voor een architect**: in gewone taal en analytisch, met de stand in GGM en GEMMA, de opties, het gevolg voor het model en een advies; de bron als link. | V | 0 | + de redacteur beslist op modellogica |
| F3 | **Minder besluiten** (zie de tabel hieronder); bij advies gevolgd een besluit zonder tekst. | N, V | −2% | 0 de gate blijft; + een aanvulling wordt een bron |
| | **G. Bundelen, geschiedenis, en blijvend licht** | | | |
| G1 | **Promote, terugmeldingen en AKKOORD per afgerond onderwerp of deel.** | N, V | −1% | 0 |
| G2 | **Export alleen op verzoek**; per commit `--check`. | g | −1% | 0 |
| G3 | **Korte commitberichten met een prefix**, gecontroleerd door de pre-commit-controle. | — | klein | 0; leesbare geschiedenis |
| G4 | **Woordbudget in `llmwiki lint`** voor skills, kennismodel en AGENTS.md; een nieuwe regel wordt altijd voorgelegd. | g | houdt A6 vast | + overzichtelijke regels |
| G5 | **Opruimen in `.claude/skills/`**: de oude kopieën. | — | klein | + geen verkeerde skill |

**Afgeraden:** alleen de kenmerken met ja vastleggen. Dan valt de dubbelcheck op de nee die de uitkomst bepaalt weg (kwaliteit −).

### Totaal per onderwerp (schatting, te toetsen in de proef)

| | Nu (deel 2, gemeten) | Straks |
|---|---|---|
| Beurten | 156 | ongeveer 80, verdeeld over 3 Sessies (30, 35, 15) |
| Groei per beurt | ongeveer 2.800 tokens | ongeveer 1.200 tokens |
| Startcontext | 43.000 | ongeveer 40.000 |
| **Totale invoer** | **48 miljoen** | ongeveer **4 à 5 miljoen (−90%)** |
| Grootste context | 487.000 | ongeveer 80.000 |
| Uitvoer | 189.000 | ongeveer 90.000 (−50%) |
| Vragenrondes | verspreid, per begrip | 2 à 3 tabellen (ongeveer −60%) |
| Nieuwe besluiten | ongeveer 30 | ongeveer 10 (−65%) |

Zonder E1 (één Sessie met 80 beurten) is de totale invoer ongeveer 7 miljoen (−85%). De grootste posten zijn A1 (het werkpakket), E1 (een Sessie per fase), B1 en B2 (twee fasen en de tabel), en A5 tot en met A7 (minder regels en minder uitvoer).

**Kwaliteit per saldo: beter.** Een kleinere context, alles wat telt bij elkaar (A1), de keuze van de redacteur vroeg (B2), en gelijke gevallen gelijk (C3, D1). De risico's (B4, C3, E2) worden opgevangen door de controles en de uitkomstvergelijking.

## Analyse van de besluiten (F3)

| Soort besluit | Aantal (grof) | Vastleggen? |
|---|---|---|
| Regelbesluit: raakt de werkwijze, de beslistabel of het kennismodel | — | Ja, als regel, na voorleggen. De grootste impact. |
| Afwijking per element, of een herziening | ongeveer 12 herzieningen, plus een deel van de modelkeuzes | Ja, kort, met de reden. |
| Keuze waar de beslistabel open laat | een deel van 137 | Ja, alleen de optie en waarom. Bij advies gevolgd: zonder tekst. |
| Naam of tekst | 77 | Nee: het resultaat staat in de beoordeling. |
| Toepassing van een regel of precedent | 68 | Nee. Na drie gevallen: een voorstel voor een regel (D1). |
| Bevestiging | veel | Nee: het AKKOORD dekt het. |
| Aanvulling op ontbrekende inhoud | een deel | Nee, een bron. |
| Uitstel of open punt | 24 | Nee, een todo of `vragen:`. |
| Terugmelding | 10 | Nee: de terugmelding is het verslag. |

De gate blijft: `beslissen.py` maakt een kandidaat pas `review` na een besluit met `gevolg: opnemen`. Bestaande besluiten blijven staan.

## Prefixen voor commitberichten (G3)

`<prefix>: <één of twee zinnen>`, in het Nederlands.

| Prefix | Wanneer |
|---|---|
| `add` | nieuw onderwerp, nieuwe elementen of een nieuwe bron |
| `update` | inhoud van bestaande elementen of bronduidingen gewijzigd |
| `fix` | fout hersteld (inhoud, script of export) |
| `remove` | verwijderd of samengevoegd |
| `rules` | werkwijze, kennismodel, beslistabel, skills, AGENTS.md |
| `tools` | scripts en tests, zonder gevolg voor de inhoud |
| `docs` | README, ARCHITECTURE.md, handoff, todo |
| `export` | alleen export of import |
| `chore` | opruimen |

## Uitvoering

Elke stap is een eigen commit, na akkoord, met de handoff in `wikis/gemma-archimate-model/handoff.md`. Per stap het denkniveau, waar het script klaar is, en wanneer de stap af is.

| Stap | Wat | Denkniveau | Klaar als |
|---|---|---|---|
| 1 | **Afspraken**: G3 (prefixen, controle in de pre-commit), F1–F3, D1, G1 en E1 in AGENTS.md, `references/besluiten.md`, de update-skill en `wiki-curatie-update`; het besluit zonder tekst in `beslissen.py`. | middel | lint en pytest zonder fouten; een commitbericht zonder prefix wordt geweigerd |
| 2 | **`tools/beoordeling.py`**: `zoek`, `besluiten`, `toon --oordeel`, `zet`, `relatie`, `besluit`. Plus A7: compacte uitvoer en `.gitattributes`. | middel | tests per subcommando; `zoek` vindt elk begrip op naam en synoniem |
| 3 | **`tools/werkpakket.py`** (A1), met batch-kandidaten voor GGM, GEMMA en UPL, en relatievoorstellen per onderwerp. | hoog (wat erin moet, bepaalt de kwaliteit) | het werkpakket voor Besluitvorming bevat alles wat in deel 2 met de hand werd opgezocht (te controleren in het transcript) |
| 4 | **Twee fasen** (B1, A5, C1, C5): `bepaal_type.py vragen`, het pad en de afgeleide nee in `beslissen.py`, het schema, `normaliseer`, en het opschonen van de 453 bestanden. | hoog | dezelfde uitkomst (`beslist:`) voor alle 453 beoordelingen; de pagina's gelijk; de export inhoudelijk gelijk |
| 5 | **Skills herschrijven** (A6, B2, B3, E2, A8): de update-, beoordelen- en criteria-skills met fase A en B, het werkpakket, de tabel en de opdracht voor de beoordelingsagent; `beslissen.py --alleen`; ARCHITECTURE.md sectie 4 inkorten. | hoog | gelezen regels per fase ≤ 12.000 woorden; lint zonder fouten |
| 6 | **Sjablonen** (C3) en **afronden** (E3). | middel | een sjabloon geeft een beoordeling die door `beslissen.py` komt |
| 7 | **Bronduiding** (B4, C4, D2) in skill `gemma-archimate-model-ingest`. | middel | een nieuwe bronduiding met citaten uit het script |
| 8 | **G2, G4, G5, E4**: export op verzoek, woordbudget, opruimen, de todo splitsen. | laag | lint met budget zonder fouten |
| 9 | **Proef**: "Levensloopproces realiseert altijd een dienst" en "Verzorgen gemeentebegrafenis", in Sessies per fase. | hoog | beurten, totale invoer, vragen en besluiten gemeten (transcript) en vergeleken met deel 2 |

Stap 1 tot en met 3 leveren al direct winst op, ook zonder de rest.

## Todo (nieuw punt in `wikis/gemma-archimate-model/todo.md`)

**ArchiMate-indeling als eerste selectie in de beslistabel** (vraag redacteur 2026-10-15). De AI kiest eerst het vak in de ArchiMate-matrix: de laag (bedrijf, applicatie, technologie, motivatie, …) en het aspect (actieve structuur, gedrag, passieve structuur), met intern of extern. De bestaande kenmerken worden de controle op die keuze. Nu herkent de aard vooral de actieve structuur en het gedrag; een passief ding is "geen van de acht". Product en Locatie passen niet in één aspect; bepaal waar ze komen. Winst: fase A wordt een paar keuzes; de redacteur beoordeelt in de taal van ArchiMate; de applicatielaag wordt een laag in dezelfde matrix. Het raakt `bepaal_type.py`, het schema en alle beoordelingen (omzetting met een script, de uitkomsten moeten gelijk blijven). Een eigen klus op denkniveau hoog, na de lichtere werkwijze en vóór de Applicatielaag.

## Controle

- Elke stap: `uv run pytest` en `uv run python -m llmwiki lint` zonder fouten.
- Stap 2 tot en met 6: `tools/beslissen.py` geeft voor alle 453 beoordelingen dezelfde uitkomst, de elementpagina's blijven gelijk, en `archimate_export.py --check` slaagt. Aan het eind één exportvergelijking: inhoudelijk gelijk.
- Stap 9: de gemeten waarden naast de tabel "Totaal per onderwerp".
