# Plan: ArchiMate-indeling, lichtere kenmerken, data-object en capability

Goedgekeurd door de redacteur op 2026-10-15. Basis: main op 98ff33f.

## Context

Twee vragen van de redacteur samen:

1. **Todo "ArchiMate-indeling als eerste selectie in de beslistabel".** Het doel heeft twee kanten:
   - beter overzicht en inzicht in de kenmerken en de beslisregels;
   - vooral een lichtere aanpak: minder werk en minder tokens voor het beoordelen en voor alles wat met kenmerken werkt.

   De AI kiest eerst het vak in de ArchiMate-matrix (laag, aspect, intern of extern). De kenmerken worden de controle op die keuze, en waar dat kan, leidt het script ze af.
2. **Twee elementtypen erbij**:
   - **Data-object** wordt een element (nu een annotatie). Eén of meer data-objecten realiseren een bedrijfsobject, met een terugmelding aan het GGM. Registratie is een eis voor een data-object; bij een bedrijfsobject mag registratietaal staan.
   - **Capability** wordt afgeleid, nadat we samen de kenmerken en het verschil met de bedrijfsfunctie hebben bepaald.

Besluiten van de redacteur (2026-10-15):

- één plan;
- *aard* heet voortaan **hoofdkenmerk**, het dominante kenmerk;
- een data-object is een veld bij het bedrijfsobject;
- bij een bedrijfsobject geen registr*-signaal meer, al blijft registratie geen argument voor het type;
- de naam blijft **Capability**;
- de technologielaag is een laag in de matrix: ze zit in GEMMA en komt misschien nog;
- Capability eerst samen bepalen, met het kader van de redacteur (deel 3).

Wat gelijk blijft: de uitkomsten van de bestaande beoordelingen (type, status, pagina's, export), de publicatiegate en de herleidbaarheid.

## Analyse: waar de kenmerken zwaar zijn (gemeten 2026-10-15, 481 beoordelingen)

De kenmerken zijn 137.000 van de 249.000 woorden in de beoordelingen (55%), gemiddeld 23 per begrip. Per groep:

| Groep | Woorden | Aandeel | Wat opvalt |
|---|---|---|---|
| Poort | 52.000 | 38% | bijna altijd hetzelfde antwoord: *herkenbaar* 480 van 481 ja, *gemeentelijk* 475 ja, *buiten dit model* 5 ja, *slechts eigenschap* 27 ja |
| Gedrag | 33.000 | 24% | veel kenmerken herhalen een relatie (*toegewezen partij* = toewijzing, *gebruikt objecten* = toegang, *aanleiding* = triggering, *gerealiseerd door* = realisatie); *afnemer* 93 van 93 ja, *benoembaar resultaat* 189 van 189 ja |
| Passief | 17.000 | 12% | *geautomatiseerd verwerkt* 382 keer gevraagd, 19 keer ja |
| Specialisatie | 12.000 | 9% | *zelfstandige specialisatie* 380 van 432 ja (zonder breder begrip altijd ja); *generiek* 20 van 382 ja |
| Hoofdkenmerk (nu Aard) | 11.000 | 8% | acht vragen, precies één ja |
| Soort gedrag | 8.000 | 6% | zes vragen, precies één ja |
| Partij, Beleidskader | 4.500 | 3% | |

Een kenmerk *ja* steunt op een bron (regel Elke claim een bron). Een relatie in een beoordeling heeft al bronnen en een vindplaats, dus een kenmerk dat uit een relatie wordt afgeleid, blijft herleidbaar.

## Advies: vijf optimalisaties

Samen ongeveer 60–70% minder woorden in de kenmerken. Dat is een derde minder per beoordeling: minder schrijven in fase A en B, kortere precedenten om te lezen, en kortere uitvoer van `vragen` en het werkpakket.

| # | Optimalisatie | Besparing (schatting) | Besluit nodig |
|---|---|---|---|
| O1 | **Keuzevelden** in plaats van ja/nee-lijsten: `vak` (laag, aspect, extern), `hoofdkenmerk` (één waarde, of `ding`) en `soort_gedrag` (één waarde). Het script leidt de nee's af. | ongeveer 17.000 | nee: volgt uit de matrix |
| O2 | **Poort als uitzondering**: alleen een afwijking schrijven, met onderbouwing (niet herkenbaar, niet gemeentelijk, buiten dit model, eigenschap, onderdeel, ander onderwerp). Zonder afwijking geldt de poort als doorlopen; *herkenbaar* en *gemeentelijk* steunen dan op de bronnen bij de definitie. | ongeveer 45.000 | **ja**: raakt regel Elke claim een bron |
| O3 | **Kenmerken uit relaties**: het script leidt het kenmerk af uit de relatie met haar bronnen. Het gaat om *toegewezen partij*, *gebruikt objecten*, *aanleiding*, *gerealiseerd door*, *leidt tot gedrag*, *bedient gedrag*, *levert aanbod*, *leidt tot gebeurtenis*, *bijdrage aan groter proces*, *omvat processen*, *vervult een rol*, *voert gedrag uit*, *ontsluit een dienst*, *wordt bewerkt*, *is grondslag voor* en *in functie-indeling*. Het signaal "kernrelatie zonder relatie" valt weg, want de relatie ís het kenmerk. | ongeveer 18.000 | ja (licht): de vraag wordt "noem de relatie" |
| O4 | **Standaardwaarden**: *zelfstandige specialisatie* is ja tenzij `specialisatie_van` een breder begrip noemt; *generiek* is nee tenzij ja. | ongeveer 10.000 | nee |
| O5 | **Data-objecten in plaats van *geautomatiseerd verwerkt***: de lijst `data_objecten` is het antwoord (deel 2). | ongeveer 4.500 | al besloten |

Verder, minder groot:

- **`beslist` uit de beoordeling halen.** Het script schrijft het blok (23.000 woorden). Agenten lezen het mee als ze een precedent openen. Het kan naar een gegenereerd bestand per onderwerp. Dit is een ander onderwerp: ik zet het alleen in de todo.
- **Een overzicht van de beslisregels per vak.** `kenmerken-en-beslistabel.md` (4.200 woorden) krijgt bovenaan de matrix. Per vak volgt dan alleen wat daar gevraagd wordt; dat geeft overzicht en inzicht. De skill criteria verwijst ernaar in plaats van de vragen te herhalen.

## Uitkomst stap 2: besluiten over O2 en O3 (2026-10-15)

- **O2, poort als uitzondering: ja.** Zonder afwijking geldt de poort als doorlopen; *herkenbaar* en *gemeentelijk* steunen dan op de bronnen van de beoordeling (veld `bronnen`, ook die bij definitie en beschrijving). Een afwijking krijgt een onderbouwing en een bron. Het script controleert dat de beoordeling een bron heeft. Regel Elke claim een bron krijgt deze zin in stap 6, samen met het script.
- **O3, kenmerken uit relaties: ja.** Het script leidt ja en nee af voor de relationele kenmerken uit de relaties, ook die in andere beoordelingen; de bron is die van de relatie. In fase B wordt de vraag "leg de relatie vast". Het signaal "kernrelatie zonder relatie" vervalt. Een verschil tussen kenmerk en relatie bij de omzetting (stap 5) wordt per geval voorgelegd.
- Voorbeeld *Ruimen graf*: de kenmerken gaan van ongeveer 560 naar ongeveer 150 woorden.

## Uitkomst stap 3–7 (2026-10-15)

- **O3 bijgesteld door de redacteur.** Een kenmerk afleiden uit een relatie is fragiel: een relatie bestaat alleen zolang beide elementen bestaan, en een kenmerk kan ja zijn door een relatie met een element dat er nog niet is. Daarom blijft het kenmerk de bewering en noemt het zijn tegenpartij in `naar`: het id van een element, of naam en type van een potentieel element. Bestaat de relatie, dan steunt het kenmerk op haar bron (zonder eigen onderbouwing); anders met eigen onderbouwing en bron. Vervalt de relatie, dan blijft de uitkomst en meldt het script dat de bron ontbreekt. Een relatie bij een kenmerk nee is een signaal.
- **Gemeten vóór de omzetting**: 239 relationele kenmerken ja zonder relatie (bij elementen 104, het meest *aanleiding* 63 en *toegewezen partij* 17). Strikt afleiden had 80 processen tot geen element gemaakt. Ze blijven met hun onderbouwing staan; de tegenpartij met naam en type komt bij de volgende herbeoordeling (todo).
- **Per geval besloten**: vier processen hadden *leidt tot gebeurtenis* nee met een triggering naar een gebeurtenis; het kenmerk is ja. GGD heeft hoofdkenmerk *samenwerkingsverband* (altijd een samenwerkingsverband, als partij via een rol); *los van verantwoordelijkheid* mag daarom ook bij een samenwerkingsverband.
- **Beslistabel**: de regels voor een combinatie van aarden en voor gedrag zonder soort gedrag vervallen (één hoofdkenmerk; de soort gedrag is verplicht). Regel 7 (consistentie) toetst ook het vak. De regelnummers vanaf 8 schuiven op; ze staan niet op de pagina's.
- **Omzetting**: alle 481 beoordelingen met een script. Uitkomst: `beslist` gelijk aan main (op de regelnummers na); alleen de status van de 285 goedgekeurde elementen gaat naar review, omdat het akkoord-hash de kenmerken telt (nieuw AKKOORD, zoals in 13c5312). De sectie Kenmerken op de pagina's toont vak, hoofdkenmerk, soort gedrag, de poort en de kenmerken met ja, met de tegenpartij als link. Bronnen die alleen in geschrapte kenmerken stonden, staan nu in `bronnen` van de beoordeling, zodat de bronnenlijst gelijk blijft.
- **Woorden**: kenmerken van 136.947 naar 51.354, plus 1.210 voor de keuzevelden (−62%); de beoordelingen samen van 249.150 naar 166.584 (−33%).
- **Open punt Extern bij gedrag**: volgt uit het vak (`bedrijf/gedrag-extern` is de dienst).
- **Woordbudget** (besluit van de redacteur): kennismodel 21.100, skill beoordelen 6.700, AGENTS.md 1.720.

## Deel 1 — Matrix en lichtere kenmerken (denkniveau hoog)

### De matrix

| Laag | Actief intern | Actief extern | Gedrag intern | Gedrag extern | Passief | Samengesteld |
|---|---|---|---|---|---|---|
| bedrijf | Actor, Rol, Bedrijfssamenwerking | Kanaal | Bedrijfsproces, Bedrijfsfunctie, Bedrijfsinteractie, Gebeurtenis | Dienst | Bedrijfsobject, Afspraak, Representatie | Product |
| applicatie | weggefilterd | weggefilterd | weggefilterd | weggefilterd | Data-object (deel 2) | — |
| technologie | weggefilterd: komt misschien nog | | | | | |
| strategie | Capability (deel 3: het vak dan bevestigen) | | | | | |
| overig | | | | | | Locatie (geen pagina), Groepering |

**Motivatie** valt buiten de aspecten, zoals in ArchiMate: daar zijn geen aspecten. In die laag zijn twee typen onderdeel van het model:

- **Beleidskader** (Driver): een element met pagina, uit externe bronnen (Europese regelgeving, Rijksregelgeving, VNG-modelverordeningen);
- **Kwaliteitsdoel**: een matchdoel uit GEMMA.

De overige motivatietypen (doel, principe, eis, waarde, kernwaarde) blijven *buiten dit model*.

- **Product** krijgt `samengesteld`: ArchiMate noemt het een samengesteld element van de bedrijfslaag.
- **Locatie** krijgt laag `overig` en aspect `samengesteld`, en blijft zonder pagina.

Fase A wordt drie keuzes:

1. het vak;
2. het hoofdkenmerk binnen het vak; dat valt weg als het vak maar één hoofdkenmerk heeft;
3. bij gedrag de soort gedrag.

Een poortafwijking komt er alleen bij als die er is. Stap 3 (Consistentie) krijgt een regel: past het hoofdkenmerk niet bij het vak, dan is er een conflict en wordt het voorgelegd. Regels 8–21 van de stappentabel blijven, met het vak als voorwaarde.

### Stappen

1. Plan in `plannen/`; todo bijwerken (laag).
2. **Besluiten over O2 en O3** voorleggen, met regel Elke claim een bron en een voorbeeld vóór en na van één beoordeling (hoog).
3. **Schema en `tools/bepaal_type.py`** (hoog):
   - de keuzevelden `vak`, `hoofdkenmerk` en `soort_gedrag`;
   - `VAKKEN`, en `AARD` wordt `HOOFDKENMERK`;
   - poort met uitzonderingen;
   - kenmerken afleiden uit relaties (het script kijkt ook naar de relaties in andere beoordelingen, zoals de toewijzing van een rol aan een proces);
   - standaardwaarden;
   - de consistentieregel;
   - `vragen` en `fase_a` vragen alleen wat per vak nodig is;
   - `CRITERIA_VERSIE` omhoog.
4. **Kennismodel** (middel):
   - `tools/kennismodel.py` geeft elk `Elementtype` zijn vak;
   - de matrix komt in `kennismodel/README.md` en in `kenmerken-en-beslistabel.md`, met de vragen per vak;
   - "aard" wordt "hoofdkenmerk" in *Herken je aan*;
   - een weggefilterd-pagina voor de technologielaag.
5. **Omzetting met een script** (middel). Een eenmalig script in de scratchpad zet alle 481 beoordelingen om. Het vult de keuzevelden in uit de huidige ja's. Het schrapt wat nu wordt afgeleid of standaard is, maar alleen als de afleiding hetzelfde antwoord geeft. Een verschil (een kenmerk ja zonder relatie, of andersom) komt op een lijst om voor te leggen, per geval.
   - `tools/beslissen.py` draait vóór en na. De `beslist`-blokken, `elementpaginas/` en `archimate_export.py --check` blijven gelijk.
   - Telt een veld mee in de hash van het akkoord, dan wordt het uitgezonderd of de hash omgezet, zodat er geen nieuw AKKOORD nodig is voor een vormwijziging.
6. **Skills en uitleg** (middel):
   - skill `gemma-archimate-model-criteria` (fase A: vak, hoofdkenmerk, soort gedrag, poortafwijking);
   - skill `gemma-archimate-model-beoordelen` (fase B zonder afgeleide kenmerken);
   - `tools/sjablonen.py` (`STANDAARD_NEE` vervalt grotendeels), `tools/werkpakket.py`;
   - AGENTS.md van de wiki, en ARCHITECTURE.md §4.1 met de reden.
7. Commit `rules: …`, en de woordentelling vóór en na in de uitkomst van het plan.

## Deel 2 — Data-object als element (hoog voor het ontwerp, middel voor de uitvoering)

**Ontwerp:**

- **Veld `data_objecten`** bij een bedrijfsobject. Per item:
  - `naam` en `definitie`;
  - `vastlegging`: de eis, met citaat en bron van de registratie (register, basisregistratie, zaaksysteem). Zonder bron is het geen data-object (*script*);
  - `ggm` (entiteit, sterkte, onderbouwing);
  - `gemma`: optioneel, een match met een van de 14 GEMMA-data-objecten.
- **Het script maakt het element**: een element `data-object` (`<bedrijfsobject>-<slug>`), een pagina in `elementpaginas/data-object/` en *realisatie* Data-object → Bedrijfsobject. Het data-object volgt de status van zijn bedrijfsobject; de hash telt `data_objecten` mee. De annotatie `data_object` vervalt.
- **GGM-terugmelding**: een match zwakker dan `sterk` wordt voorgelegd (`REDEN_GEEN_GGM` bestaat al). Bij `geen` hoort een melding `hiaat` in `modellen/ggm/terugmeldingen.yaml` (*script*).
- **Registr*-signaal**: `tools/signalen.py` slaat `REGISTR_RE` over bij een bedrijfsobject en in `data_objecten`.
  - Regel Beslistabel beslist wordt: registratie is geen argument voor het type; bij een bedrijfsobject mag de tekst haar noemen; bij een data-object is ze de eis.
  - De afspraken in `tools/kennismodel.py` volgen.
- **Kennismodel en export**: Data-object krijgt paginatype `data-object` (geen annotatie meer), met *realisatie* naar Bedrijfsobject. `archimate_export.py` zet het in de applicatielaag.

**Stappen:**

8. Schema, `bepaal_type.py`, `kennismodel.py`, `signalen.py`, `modelleerregels.md` (hoog).
9. `beslissen.py`, `render.py`, `archimate_export.py`, tests; een nieuwe `references/data-object.md` in skill `gemma-archimate-model-beoordelen` (middel).
10. De 19 bedrijfsobjecten met *geautomatiseerd verwerkt: ja*, per geval (hoog): de data-objecten, de bron van de vastlegging, de GGM-match en de terugmeldingen. Eén tabel voorleggen; AKKOORD.
11. Commits `rules:` en `add:`.

## Deel 3 — Capability (eerst samen bepalen, denkniveau hoog)

**Kader van de redacteur.** Het abstractieniveau volgt uit de vraag die het model beantwoordt, niet uit omvang of detail.

| | Capability | Bedrijfsfunctie | Bedrijfsproces |
|---|---|---|---|
| Vraag | Wat moet de gemeente kunnen? | Welke activiteiten horen inhoudelijk bij elkaar? | Hoe wordt een dienst gerealiseerd? |
| Afbakening | vermogen of opgave | gedeelde aard van activiteiten, kennis of middelen | dienst, resultaat en kernobject |
| Verandert bij | andere strategische opgaven | andere clustering van activiteiten | andere uitvoering van de dienst |
| Niveau | strategisch/tactisch | tactisch | tactisch/operationeel |

**Criteria:**

- **Capability**: onderscheidend, beoordeelbaar (volwassenheid, ontwikkelbehoefte), ontleedbaar, duurzaam, niet uitvoeringsgericht. Splits een capability als de delen apart ontwikkeld, beoordeeld of bestuurd kunnen worden.
- **Bedrijfsfunctie**: inhoudelijke samenhang (aard, deskundigheid, middelen), procesoverstijgend, stabiel, geen processtap. Splits bij wezenlijk andere deskundigheid; voeg samen als het onderscheid geen inzicht geeft.
- **Bedrijfsproces**: dienstgericht, een eigen kernobject, een herkenbaar resultaat, afgrensbaar. Vergelijk met de bestaande kenmerken.

Eén toets per type, maar geen gelijke omvang afdwingen. Voorbeelden:

| Voorbeeld | Type | Oordeel |
|---|---|---|
| Dienstverlening | Capability | te breed |
| Aanvraag controleren op volledigheid | Capability | te concreet |
| Aanvragen beoordelen | Bedrijfsfunctie | passend als het over meer diensten terugkomt |
| Omgevingsvergunning verlenen | Bedrijfsfunctie | te dicht bij één proces |

**Beslisregel**: kies het grofste niveau dat genoeg onderscheid geeft; meer detail alleen als het een aantoonbare vraag beantwoordt.

**Stappen:**

12. **Voorstel ter bespreking** (geen code):
    - de definitie (Over GEMMA: "Een vermogen waarover een organisatie, persoon of systeem beschikt") en het vak;
    - de criteria als kenmerken in de vorm van de beslistabel, en daartegen aangescherpt *gegroepeerd gedrag* en *stabiel over tijd*;
    - de kernrelatie Bedrijfsfunctie ─realisatie→ Capability;
    - naamvorm, indeling, bron en GEMMA-match;
    - een kalibratie op de 26 GEMMA-capabilities en op 10 à 20 diensten uit de bestaande onderwerpen, met de toetsvragen: waar investeren, welke competenties hergebruiken, welke diensten afhangen van hetzelfde vermogen.
13. Besluiten vastleggen in ARCHITECTURE.md en het kennismodel. Capability gaat van `motivatie/weggefilterd` naar laag `strategie`.
14. Bouwen zoals in deel 2; capabilities afleiden; voorleggen; AKKOORD.

## Volgorde en Sessies

- **Sessie 1**: stap 1–2 (plan en besluiten O2/O3).
- **Sessie 2**: stap 3–7 (de omzetting).
- **Sessie 3**: deel 2.
- **Sessie 4**: deel 3, eerst als bespreking.
- Na elk deel: handoff.md en todo.md bijwerken.

## Open punten (regel Navragen, tijdens de uitvoering)

- **Naam van een data-object**: als het bedrijfsobject, of een gegevensnaam ("Zaakgegevens")?
- **Wie nog meer data-objecten heeft**: kan ook een afspraak, of een rol of actor met tegenhanger, data-objecten hebben?
- **Extern bij gedrag**: volgt uit het vak (opgelost in stap 3).

## Verificatie

- `uv run pytest wikis/gemma-archimate-model/tools/tests` is groen, met nieuwe tests:
  - vak en hoofdkenmerk in conflict;
  - een poortafwijking;
  - een kenmerk afgeleid uit een relatie in een andere beoordeling;
  - een data-object zonder vastlegging geeft een fout;
  - een bedrijfsobject geeft geen registr*-signaal, een proces wel;
  - de realisatie staat in de export.
- **Deel 1**: `tools/beslissen.py` vóór en na de omzetting. Het verschil in `beslist` en `elementpaginas/` is leeg, en `archimate_export.py --check` is gelijk. Er is een woordentelling van de kenmerken vóór en na.
- **Deel 2**: de 19 objecten hebben data-objectpagina's met realisatie; het GGM-register is bijgewerkt; de export heeft de applicatielaag.
- **Steeds**: `uv run python -m llmwiki lint` en `uv run python -m llmwiki commit-check`.
