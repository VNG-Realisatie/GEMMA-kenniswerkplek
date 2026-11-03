# Plan: gedeelde Archi-sync en een apart wiki-gemma-kennismodel

Opgesteld op 2026-11-03 na een interview met de redacteur; nog niet goedgekeurd. Basis: main op 3bf7a774.

## Context

De redacteur kopieert `wiki-gemma-model-sync.ajs` met de hand naar archi-scripts, de map waar Archi zijn scripts uit draait. Dat is foutgevoelig: de kopie in archi-scripts loopt al achter (zij noemt nog *Import › Model into selected model*, de tekst van vóór commit 99a5ab19 van 2026-10-04). In archi-scripts staan ook de JavaScript-eisen en de gedeelde modules, en daar staat een tweede sync voor de View-architectuurexport, die van dit script is afgeleid. Er komen meer sync-scripts, en die moeten dezelfde conventies gebruiken voor eigenschappen, datum en herkomst.

Doel: één plek van beheer voor de sync-scripts (archi-scripts), met één conventie die elke export volgt; deze wiki legt alleen haar eigen invulling vast. Daarnaast komt het GEMMA-kennismodel niet meer in het GEMMA-model, maar in een eigen Archi-model naast Over GEMMA, net zoals de bronnen parallel staan.

## Bevindingen (stand 2026-11-03)

### Herkomstwaarden in de huidige export

`export/gemma-archimate-model.archimate` (export van 2026-10-18) heeft 1689 objecten met `wiki-gemma-model exportdatum`, alle met dezelfde datum `2026-10-18T17:40:33` en `soort export` `definitief`.

| Herkomst | Aantal | Wat | Id |
|---|---|---|---|
| `nieuw` | 1391 | door de wiki gemaakt element of relatie | vast id: `"id-" + uuid5(NS, "/".join(delen)).hex`, met `NS = uuid5(NAMESPACE_URL, "https://github.com/VNG-Realisatie/GEMMA-kenniswerkplek/wikis/gemma-archimate-model")` (`tools/archimate_export.py` r. 90 en 107) |
| `gekoppeld` | 43 | bestaand GEMMA-element of bestaande GEMMA-relatie | GEMMA-id |
| `kennismodel` | 190 | het GEMMA-kennismodel uit Over GEMMA, letterlijk, met de groepen per laag | id van Over GEMMA; de groepen en aggregaties een vast id |
| `kennismodel-wiki` | 64 | het kennismodel van de wiki | id van Over GEMMA waar dat bestaat, anders een vast id |

De skill noemt alleen `gekoppeld` en `nieuw`. Geen van de 254 kennismodelobjecten staat in de GEMMA-releases 2026-07-01 en 2026-10-02 (gecontroleerd op de id's): in GEMMA staan ze alleen door een import van de wiki.

### Wat de wiki in GEMMA raakt

| Object | Naam | Documentatie | Eigenschappen | Profiel | Bron |
|---|---|---|---|---|---|
| Gekoppeld element | **uit de wiki** | **definitie uit de wiki** | GEMMA letterlijk, plus `wiki-gemma-model …`, met `vorige naam` en `vorige definitie` (de GEMMA-tekst) | GEMMA letterlijk | `archimate_export.py` r. 397-425 |
| Gekoppelde relatie | uit de wiki, als die een naam heeft | GEMMA letterlijk | GEMMA letterlijk plus wiki-eigenschappen | — | r. 340-348 |
| Bestaande GEMMA-groepering (beleidsdomein) | GEMMA letterlijk | GEMMA letterlijk | plus `wiki-gemma-model beschrijving` en `bronnen` uit het register | — | r. 720-728 |
| Stub (doel van een relatie, knoop van de functiehiërarchie) | letterlijk | letterlijk | letterlijk, geen wiki-eigenschappen | letterlijk | r. 313-325 |
| GEMMA-map | letterlijk | letterlijk | letterlijk | — | r. 251-260 |
| Map van de wiki (`<laag> / wiki-gemma-model / …`) | van de wiki | — | geen (dus ook geen datum) | — | r. 262-272 |

Alleen bij een gekoppeld element (en de naam van een gekoppelde relatie) verandert GEMMA-inhoud; het rapport en stap 2 van de export-skill noemen die gevallen.

### Wat de wiki in het kennismodel raakt

- `kennismodel`: naam, documentatie en eigenschappen letterlijk uit Over GEMMA, plus `id`, `herkomst`, `exportdatum`, `soort export` (r. 849-871).
- `kennismodel-wiki`: een concept dat Over GEMMA al heeft, is hetzelfde object en krijgt alleen `in Over GEMMA` erbij (r. 931-941); een relatie uit Over GEMMA houdt id en toegangstype. De rest is nieuw, met naam en documentatie uit `tools/kennismodel.py`.
- Naam en documentatie van Over GEMMA past de wiki nergens aan.

### Wat de sync nu doet, en waar het niet sluit

Een object met een oudere `exportdatum` dan de nieuwste wordt verwijderd bij `herkomst = nieuw` (relaties eerst); bij elke andere waarde gaan alleen de eigenschappen met het voorvoegsel `wiki-gemma-model ` eraf. Lege mappen onder een map `wiki-gemma-model` worden opgeruimd. Het script weigert een concept-export en stopt als geen object een exportdatum heeft.

1. **Wezen uit het kennismodel.** `kennismodel` en `kennismodel-wiki` worden alleen opgeschoond, nooit verwijderd. De door de wiki gemaakte kennismodelobjecten blijven als eigenschapsloze objecten in GEMMA staan; ook de objecten van Over GEMMA, want die staan niet in de GEMMA-release. De skill (SKILL.md r. 24) zegt dat de sync ze "mee opruimt": dat klopt niet.
2. **De GEMMA-tekst gaat verloren bij ontkoppelen.** Het opschonen haalt ook `vorige naam` en `vorige definitie` weg; het element houdt de wiki-tekst, en de oorspronkelijke tekst staat alleen nog in de coArchi-historie.
3. **Datum in lokale tijd.** `datetime.now().isoformat(timespec="seconds")` (r. 1176): zonder tijdzone. De tekstvergelijking werkt, behalve bij de overgang naar wintertijd.
4. **`soort export` is alleen een merkteken.** De import van een concept-export is al gebeurd als de sync weigert; het merkteken helpt alleen bij het ontdekken.
5. **Optie *bestaande objecten bijwerken*.** Staat die uit, dan krijgen bestaande objecten hun nieuwe datum niet en ziet de sync alle bestaande `nieuw`-objecten als verouderd (afgeleid). De sync kan dat niet zien; de werkinstructie moet het zeggen.
6. **Menunaam.** Voor Archi 5.10 is het *File › Import › Another model into selected model…* (commit 99a5ab19, na een proefimport). Voor Archi 5.9 staat niets in de repo.
7. **ES5 en Nederlands.** ES5 is geen vastgelegde eis (geen bron); Nederlands volgt uit de taalregel van de repository.
8. **Kopieën.** De bron is `.agents/skills/gemma-archimate-model-archimate-export/scripts/`; `.claude/skills/…` is een beheerde kopie (`.bridge-source.json`, `llmwiki harness sync`). Voor archi-scripts is er geen mechanisme.

## Besluiten van de redacteur (2026-11-03)

1. **Twee modellen.** Het kennismodel (de groep *Kennismodel* uit Over GEMMA én *Kennismodel-wiki*) gaat naar een eigen Archi-model `wiki-gemma-kennismodel`, te importeren in (een kopie van) het Over GEMMA-model. Het GEMMA-model krijgt geen kennismodelobjecten meer.
2. **Conventie in archi-scripts.** De gedeelde conventie staat in archi-scripts, met een versienummer, naast de gedeelde module. Deze wiki legt alleen haar invulling vast (voorvoegsels, wat gekoppeld is, de inhoudelijke eigenschappen) en noemt de versie die zij volgt.
3. **Herkomst: twee waarden, onbekend weigert.** `nieuw` (verwijderen als verouderd) en `gekoppeld` (opschonen). Een andere of ontbrekende herkomst op een object met een exportdatum: het script weigert het geheel.
4. **Ontkoppelen: herstellen tenzij aangepast.** Bij een verouderd gekoppeld object zet de sync `vorige naam` en `vorige definitie` terug als naam en documentatie, tenzij de tekst sinds de import in het doelmodel is aangepast; dan blijft die staan en noemt het script het geval in de lijst vooraf.
5. **Datum.** UTC, op de seconde, zonder `Z`: `2026-11-03T13:05:09`. Het script weigert een datum in een ander formaat.
6. **Mappen.** De export geeft elke map die zij zelf maakt een exportdatum en herkomst `nieuw`; mappen van het doelmodel krijgen niets. De sync verwijdert een lege map met herkomst `nieuw` en een oudere datum, de diepste eerst. Geen mapnaam in het script.
7. **Minimale set voor de sync** (Nederlandse achtervoegsels, een voorvoegsel per export):
   - `<voorvoegsel> exportdatum`; een concept-export schrijft `concept`, en wordt daardoor geweigerd;
   - `<voorvoegsel> herkomst`, verplicht, ook voor de View-export;
   - alleen bij `gekoppeld`: `<voorvoegsel> vorige naam` en `<voorvoegsel> vorige definitie`.

   `soort export` en een contractversie op elk object vervallen. Inhoudelijke eigenschappen (bij de wiki `id`, `status`, `bronnen`, `beschrijving`, `pagina`, …) mag elke export toevoegen; ze vallen buiten de conventie, en de sync haalt ze bij het opschonen weg omdat ze het voorvoegsel hebben.
8. **Overgang via de export.** Eén overgangsexport geeft de kennismodelobjecten in wiki-gemma-model herkomst `nieuw`; de export daarna laat ze weg, en de gewone sync ruimt ze op.
9. **Script hier verwijderen.** Het `.ajs` gaat uit de export-skill; stap 4.3 verwijst naar het script in archi-scripts en de versie van de conventie. Een test controleert dat de export aan de conventie voldoet.
10. **Kennismodel zoals GEMMA.** Een Over GEMMA-object dat alleen wordt meegenomen, krijgt geen sync-eigenschappen (zoals een stub); een Over GEMMA-object waar de wiki eigenschappen aan toevoegt, is `gekoppeld`; wat de wiki maakt (concepten, relaties, groeperingen, aggregaties, mappen), is `nieuw`.

## Doelbeeld

| Export van de wiki | Voorvoegsel | Bestand | Doelmodel | Bron van het doelmodel |
|---|---|---|---|---|
| wiki-gemma-model | `wiki-gemma-model` | `export/gemma-archimate-model.archimate` | GEMMA-model | GEMMA-release (`.archimate`) |
| wiki-gemma-kennismodel | `wiki-gemma-kennismodel` | `export/gemma-archimate-kennismodel.archimate` | Over GEMMA-model | `2026-vng-over-gemma` |

Regels van de gedeelde sync (één module in archi-scripts, per export een aanroep met het voorvoegsel):

1. Geen object met `<voorvoegsel> exportdatum`: melding, niets gewijzigd.
2. Een exportdatum die geen datum in het afgesproken formaat is (ook `concept`), of een onbekende of ontbrekende herkomst: weigeren, niets gewijzigd.
3. Nieuwste = het maximum van de datums; verouderd = een oudere datum.
4. Eerst de lijst tonen (verwijderen, opschonen, herstellen, niet herstelbaar), pas na bevestiging uitvoeren.
5. `nieuw` en verouderd: verwijderen, relaties eerst, dan elementen, dan lege mappen van diep naar ondiep.
6. `gekoppeld` en verouderd: naam en documentatie herstellen uit `vorige naam` en `vorige definitie` (tenzij aangepast), dan alle eigenschappen met het voorvoegsel weghalen.
7. Een object zonder exportdatum (stubs, objecten van het doelmodel) raakt de sync nooit.

## Stappen

### Deel A: archi-scripts (buiten deze repo)

1. Conventiedocument met versienummer: de minimale set, het datumformaat, de herkomstwaarden, de regels hierboven en de werkinstructie voor de import (menunaam per Archi-versie; *bestaande objecten bijwerken* moet aan).
2. Gedeelde sync-module volgens de JavaScript-eisen van archi-scripts.
3. Aanroepen: wiki-gemma-model (in GEMMA), wiki-gemma-kennismodel (in Over GEMMA), View-architectuur. De View-export schrijft herkomst `nieuw` en de Nederlandse achtervoegsels.
4. Proef op een kopie van GEMMA en van Over GEMMA, met de open punten hieronder.

### Deel B: deze wiki

1. **Export, conventie.** `archimate_export.py`: datum in UTC zonder `Z`; `soort export` vervalt; `--concept` schrijft `exportdatum` `concept`; de eigen mappen krijgen exportdatum en herkomst `nieuw`; herkomst alleen `nieuw` of `gekoppeld`.
2. **Overgangsexport** (besluit 8): de kennismodelobjecten blijven nog één keer in wiki-gemma-model, met herkomst `nieuw`. Alleen als GEMMA al een import van de wiki heeft gehad (zie open punt 1).
3. **Splitsen.** Het kennismodel (`_kennismodel`, `_kennismodel_wiki`) gaat naar een tweede bestand `export/gemma-archimate-kennismodel.archimate` met voorvoegsel `wiki-gemma-kennismodel` en de herkomstregels van besluit 10; wiki-gemma-model bevat het niet meer. Het rapport krijgt een deel per bestand.
4. **Tests** in `tools/tests/test_gam_archimate_export.py`: elk object met een exportdatum heeft een geldige datum en herkomst; `vorige naam` en `vorige definitie` alleen bij `gekoppeld`; geen kennismodelobject in wiki-gemma-model; elke eigen map heeft datum en herkomst.
5. **Documentatie.** Export-skill (stap 3 en 4, de eigenschappen, het kennismodel), ARCHITECTURE.md §6.5 (twee modellen, sync in archi-scripts), de docstring van `archimate_export.py`. Het woordbudget van de export-skill is 1300 woorden: leg een overschrijding eerst voor.
6. **Script verwijderen** uit `.agents/skills/gemma-archimate-model-archimate-export/scripts/`, daarna `llmwiki harness sync` voor de kopie in `.claude/`.
7. Controle: `llmwiki lint`, de tests, `archimate_export.py --check`. De export zelf alleen op verzoek van de redacteur.

### Deel C: de overgang in GEMMA en Over GEMMA (door de redacteur of het GEMMA-team)

1. Import van de overgangsexport in GEMMA (bestaande objecten bijwerken aan), dan de nieuwe sync.
2. Import van de export zonder kennismodel, dan de sync: de kennismodelobjecten worden verwijderd.
3. Import van wiki-gemma-kennismodel in een kopie van Over GEMMA, dan de sync met voorvoegsel `wiki-gemma-kennismodel`.
4. Controleren en committen met coArchi.

## Open punten

1. **Is er al een import van de wiki in het echte GEMMA-model geweest**, of alleen op een kopie? Zonder import vervallen de overgangsexport (B2) en deel C1-C2.
2. **Gedrag van Archi bij *bestaande objecten bijwerken*:** blijft een eigenschap die alleen in het doelmodel staat (zoals een oude `soort export`, of een eigenschap die het GEMMA-team na de release toevoegde) staan, of verdwijnt ze? Testen op een kopie (A4). Blijft `soort export` staan, dan moet de overgang die ook weghalen.
3. **"Tenzij aangepast" vraagt een referentie.** Om te zien of naam of definitie sinds de import is aangepast, moet de sync weten wat de export schreef. Mogelijkheden: twee extra eigenschappen bij `gekoppeld` (de geschreven naam en definitie), wat de minimale set vergroot; of altijd herstellen en het in de lijst vooraf melden. Voorleggen aan de redacteur.
4. **Scheidingsteken.** Aangenomen: voorvoegsel, spatie, achtervoegsel (`wiki-gemma-model exportdatum`), zoals nu in GEMMA. Bevestigen.
5. **Menunaam in Archi 5.9** vaststellen bij de proef (A4).
6. **Wie importeert in Over GEMMA**, en is een kopie van Over GEMMA het doel of het model zelf?
7. **Overgang van de datum.** De datums in GEMMA zijn lokale tijd (UTC+1 of +2). Een eerste export in UTC binnen twee uur na een lokale export telt als ouder; tussen de laatste export (2026-10-18) en nu speelt dat niet.
