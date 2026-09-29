---
name: gemma-archimate-model-assess
description: ASSESS-uitbreiding voor gemma-archimate-model — begrippen uit de bronanalyses verzamelen, per begrip domein, naamconflicten en structuur (specialisatie, attribuut, onderdeel) bepalen, de kenmerken beantwoorden en de beslistabel laten toepassen. Gebruik binnen gemma-archimate-model-update, na wiki-assess.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-criteria"
  requires-tools: "python:tools/bepaal_type.py python:tools/ggm.py python:tools/gemma.py"
  reads: "bronanalyse"
  writes: "assessment"
---

# ASSESS-uitbreiding: begrippen beoordelen

Deze skill bepaalt per begrip *wat* het is. Ze schrijft nog geen pagina's.

## 1. Lezen

Eerst de intake (`sources/index/`), dan de bronanalyses van dit onderwerp, en de originele tekst (`sources/raw/`) alleen voor specifieke passages. Houd de volgorde van de bronvoorrang aan: wetten en informatiemodellen bepalen welke begrippen er zijn en wat ze formeel betekenen; beleid laat zien hoe erover gesproken wordt.

## 2. Begrippen verzamelen

- Alle kernbegrippen uit de bronanalyses van het onderwerp, plus de begrippen die al in `begrippen/<onderwerp>.md` staan.
- De GGM-entiteiten van de betrokken beleidsdomeinen (`uv run python tools/ggm.py zoek <term>`). NOOIT een beleidsdomein of begrip overslaan omdat het GGM er al entiteiten voor heeft: deze stap toetst ook het GGM. Noteer per GGM-entiteit of de bronnen haar bevestigen, nuanceren of aanvullen.

## 3. Per begrip, vóór de kenmerken

1. **Domein.** Hoort het begrip bij dit onderwerp? Verhuisregel: een begrip verhuist als het primair bij een ander onderwerp hoort (bijv. horecavergunning bij horeca). Bij twijfel: vastleggen waar het is gevonden, met een verwijzing naar het andere onderwerp.
2. **Naamconflict (signaal).** Bestaat er al een element met deze naam of als synoniem? Komt de naam in meerdere GGM-beleidsdomeinen voor (`tools/ggm.py naamgenoten <naam>`)? Classificeer als *duplicaat* (zelfde concept), *homoniem* (ander concept) of *geen conflict*. Een actor/rol en een bedrijfsobject met dezelfde naam zijn geen conflict (tegenhanger). Dit is een signaal; de beslissing valt bij het schrijven.
3. **Structuur.**
   - *Specialisaties en generalisaties* uit de bronnen én uit het GGM (`tools/ggm.py generalisaties <guid>`). Vergelijk beide; afwijkingen zijn bevindingen. Beslisregel: praat de gemeente erover als aparte dingen? Specialisaties met eigen processen of relaties worden eigen elementen; uitwisselbare specialisaties worden *specialisatie zonder pagina* bij het bovenliggende element. Beoordeel het abstracte niveau altijd zelf op zijn kenmerken; sluit het nooit categorisch uit.
   - *Attribuut of waarde?* (`tools/ggm.py attribuut <term>`). Is het begrip slechts een attribuut, status of waarde van een ander begrip, dan beantwoord je het kenmerk *slechts eigenschap* met ja.
   - *Onderdeel?* Een GGM-relatie `[0..*]` naar een groter geheel wijst op een afhankelijk ding zonder eigen identiteit (kenmerk *eigen identiteit*).

## 4. Kenmerken en beslistabel

Beantwoord voor elk begrip alle kenmerken uit `gemma-archimate-model-criteria`, met onderbouwing en bron-id's, en zet ze als `beoordeling` bij het voorstel in `assessment.json`:

```json
{"doel": "bedrijfsarchitectuur/bedrijfsobjecten/<taakveld>/<beleidsdomein>/<id>.md", "soort": "nieuw",
 "motivering": "…", "bronnen": ["<bron-id>"],
 "beoordeling": {"begrip": "Beschikking", "onderwerp": "<onderwerp>", "kenmerken": {"herkenbaar": {"waarde": "ja", "onderbouwing": "…", "bronnen": ["…"]}, "…": {}}}}
```

Neem de relaties uit de bronanalyses op in het voorstel van het begrip aan de van-kant, zodat elementen en relaties samen worden beoordeeld: `"relaties": [{"van": "Heffingsambtenaar", "werkwoord": "legt op", "naar": "Aanslag", "bronnen": ["<bron-id>"], "vindplaats": "art. 231"}]`.

Een begrip dat geen element wordt, krijgt een voorstel met als doel de begrippenlijst (`begrippen/<onderwerp>.md`, soort `wijzigen`) en toch een beoordeling. Draai daarna `uv run python tools/bepaal_type.py evalueer <assessment.json> --schrijf`; de uitkomst is bindend. Draai daarna `uv run python tools/relaties.py uit-bronnen <assessment.json>`: dat toont per relatie de ArchiMate-relatie, of een kant is opgetild, en welke relaties vervallen omdat een kant geen element is.

## 5. GGM-hiaat (alleen bij `data_object: ja` zonder GGM-match)

Conservatief: bij twijfel niet rapporteren. Motiveer waar de gegevens worden beheerd, welke attributen relevant zijn en in welk GGM-beleidsdomein het past. Een proces, functie of regeling zonder GGM-entiteit is **geen** hiaat, tenzij een aanwijsbaar GGM-beleidsdomein dat deel wél modelleert. Schrijf nooit "structureel buiten GGM-scope"; schrijf "in het GGM niet compleet gedekt", met een concrete reden waar mogelijk.

## 6. Presenteren

Per begrip, niet in één blok: de uitkomst van de beslistabel (type of reden), `data_object`, het naamconflict-signaal, de relaties uit de bronnen (en welke vervallen) en één of twee zinnen argument. Leg elk begrip met `voorleggen` of `conflict` voor en wacht op het antwoord van de redacteur. Pas een kenmerk alleen aan als het aantoonbaar fout was.

Rond af met `uv run llmwiki run complete assess --run <run-id> --data <assessment.json>`.
