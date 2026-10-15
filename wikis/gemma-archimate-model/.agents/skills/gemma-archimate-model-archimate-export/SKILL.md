---
name: gemma-archimate-model-archimate-export
description: Exporteer de goedgekeurde elementen en relaties van gemma-archimate-model als Archi-bestand (.archimate) met de technische id's van het GEMMA-model, om in Archi te bekijken en in het GEMMA-model te importeren, met een volledige sync via de exportdatum en een jArchi-script. Gebruik alleen op verzoek van de redacteur (stap 16 van gemma-archimate-model-update), om de export te maken, het model in Archi te zien of naar GEMMA te brengen.
metadata:
  kind: capability
  scope: wiki
  requires-skills: "gemma-archimate-model-gemma-release"
  requires-tools: "python:tools/archimate_export.py python:tools/gemma.py"
---

# Export naar Archi

`tools/archimate_export.py` schrijft `export/gemma-archimate-model.archimate`, in het opslagformaat van Archi (ook dat van coArchi 2). Archi voegt bij *Import › Another model into selected model* samen op id. Daarom neemt de export de id's van GEMMA over:

| Wat | Id | Map |
|---|---|---|
| Element met een GEMMA-match (`gemma.id`) | het GEMMA-id | dezelfde mappen als in GEMMA, met dezelfde map-id's |
| Nieuw element | vast id, afgeleid van het begrip-id; na hernoemen, samenvoegen of splitsen van het begrip-id waarvan het het object voortzet (veld `object_van`) | `<Business of Motivation> / wiki-gemma-model / <paginatype> / <taakveld> / <beleidsdomein>`; een functie `… / Bedrijfsfuncties / <domein>` |
| Relatie die in GEMMA al bestaat (zelfde type, zelfde elementen; bij toegang die met hetzelfde toegangstype, anders de eerste) | het GEMMA-id | dezelfde map als in GEMMA |
| Nieuwe relatie | vast id, afgeleid van bron, soort, doel en naam (bron en doel ook via `object_van`) | `Relations / wiki-gemma-model` |

Naam en definitie komen uit de wiki en overschrijven die van GEMMA. De GEMMA-eigenschappen (`Object ID`, `GEMMA URL`, `GGM-*` …) en het profiel (specialisatie) gaan letterlijk mee; een `Object ID` maakt de export nooit. Eigen eigenschappen beginnen met `wiki-gemma-model`: `id`, `herkomst` (`gekoppeld` of `nieuw`), `exportdatum`, `soort export`, `status`, `GEMMA-match`, `bronnen`, `beschrijving`, `synoniemen`, `pagina`, en bij een gekoppeld element `vorige naam` en `vorige definitie`. Relaties krijgen `id`, `herkomst`, `exportdatum`, `soort export`, `GGM-match` (`exact` of `geen`), `bronnen` en `vindplaats`, een toegangsrelatie ook `toegang` (de handelingen of verantwoordelijkheden uit de beoordeling). **Eén toegangsrelatie per paar.** Heeft een beoordeling meer toegangsrelaties naar hetzelfde doel, dan worden ze in de export één relatie: het toegangstype is de vereniging (lezen en schrijven samen: lezen-schrijven), naam, bronnen en vindplaats zijn die van alle, `id` noemt de nummers (`<begrip-id>#1+2`) en het vaste id is dat van de eerste. De beoordeling houdt elke gevonden relatie; de elementpagina toont ze, net als de export, als één relatie (dezelfde functie, `kennismodel.toegang_per_paar`); het rapport noemt de samengevoegde.

**Kennismodel.** De export neemt het GEMMA-kennismodel mee: de elementen en relaties van de views die `wiki.yaml` `kennismodel.views` noemt, uit de bron Over GEMMA (`sources/raw/<bron>.xml`), met de id's van Over GEMMA. Ze staan in de map `Kennismodel` onder `wiki-gemma-model` van hun laag, hebben `herkomst` `kennismodel` en `exportdatum` (de sync ruimt ze dus mee op), en hangen met een aggregatie aan een groep per laag (Bedrijfsarchitectuur, Applicatiearchitectuur, Technische architectuur, Motivatie), die op haar beurt door de groep `Kennismodel` wordt geaggregeerd (`Other / wiki-gemma-model / Kennismodel`); een element van een andere laag (Capability, Groep) hangt aan `Kennismodel` zelf. **Kennismodel-wiki.** Het kennismodel van de wiki (`tools/kennismodel.py`, de pagina's in `kennismodel/`) gaat volledig mee in de groep `Kennismodel-wiki`, geaggregeerd door `Kennismodel`: een concept per elementtype, een relatie per toegestaan relatietype (bij toegang één per paar elementtypen: die van Over GEMMA met haar toegangstype, anders lezen-schrijven; het toegangstype hoort bij de relatie in het inhoudelijk model) en een groepering per indeling (Beleidsdomeinindeling, Functie-indeling naar domein, Procesindelingen, Doelgroepindeling, Grondslagindeling). Een concept of relatie dat Over GEMMA al heeft, behoudt zijn id en blijft in de map `Kennismodel`; een nieuwe relatie komt in `Relations / wiki-gemma-model / Kennismodel / Kennismodel-wiki`. Elk concept, elke relatie en elke indeling heeft de eigenschap `in Over GEMMA` (ja of nee), een relatie ook `kernrelatie` (ja of nee). De groep `Kennismodel` blijft het GEMMA-kennismodel uit Over GEMMA, ter vergelijking. **Filter.** De relaties van de elementen gaan alleen mee als ze in het kennismodel staan; het rapport noemt de weggelaten relaties met hun reden, en de relaties die de elementen gebruiken maar Over GEMMA niet kent (kandidaten voor een terugmelding over het kennismodel). De views zelf gaan niet mee.

**Objectbehoud.** Een hernoemd, samengevoegd of gesplitst element zet het Archi-object voort dat het veld `object_van` van de beoordeling noemt (regel Objectbehoud): Archi werkt bij de import naam, definitie en eigenschappen bij, en views met het object blijven werken. De export weigert als het type van een voortgezet object wijzigt ten opzichte van de vorige export, want dat kan Archi bij een import niet.

**De export vertrouwt de match.** Elke match met een id overschrijft het GEMMA-element, ook een zwakke of partiële. Matchen is de verantwoordelijkheid van de wiki en de redacteur (regel Zwakke match voorleggen in `kennismodel/modelleerregels.md`), niet van de export of van Archi.

## Stappen

1. **Voorwaarden** (denkniveau laag): `uv run python tools/archimate_export.py --check`. De export weigert als beslissen fouten geeft of verouderd is, als de pagina's afwijken van de beoordelingen, als een goedgekeurde beoordeling geen promotieregel in `log.md` heeft, als het type afwijkt van het gekoppelde GEMMA-element, of als het GEMMA-model niet als `.archimate` is ingelezen. In het laatste geval: skill `gemma-archimate-model-gemma-release` met een `.archimate`-bestand. Geef elke fout in gewone taal door; een afwijkend type leg je voor aan de redacteur (regel Navragen).
2. **Exporteren** (laag): `uv run python tools/archimate_export.py`. Alleen begrippen met status `goedgekeurd` gaan mee. De tool schrijft ook `export/rapport.md` (gegenereerd). Geef het rapport door en noem expliciet elk GEMMA-element waarvan de naam of definitie verandert, de overgeslagen relaties (het doel is nog niet goedgekeurd of een domein of doelgroep ontbreekt in GEMMA), de specialisaties naar een GEMMA-element (dat letterlijk meegaat), de nieuwe groeperingen (een beleidsdomein dat GEMMA niet kent: een voorstel aan het GEMMA-team), de dekking van de functiehiërarchie (`gemma_functie` wordt de aggregatie vanaf de GEMMA-functie, die met haar tak tot en met het domein letterlijk meegaat; `--volledig` neemt de hele hiërarchie mee) en de diensten zonder grondslag, die niet meegaan omdat ze geen wettelijke taak zijn.
3. **Bekijken:** in Archi `File › Open` op `export/gemma-archimate-model.archimate`. Voor een blik op alles wat nog niet goedgekeurd is: `--concept` schrijft `.work/export/gemma-archimate-model-concept.archimate`, met modelnaam `CONCEPT – wiki-gemma-model`. Dat bestand is nooit voor import in GEMMA; het sync-script weigert het.
4. **Importeren in GEMMA** (door de redacteur of het GEMMA-team, niet door de AI):
   1. De eerste keer, en na een wijziging van deze tool: op een kopie van het GEMMA-model.
   2. Selecteer het GEMMA-model in de modelboom, dan `File › Import › Another model into selected model…` (Archi 5.10; de naam verschilt per versie), kies het exportbestand en zet de optie aan om bestaande objecten bij te werken.
   3. Draai in Archi het jArchi-script [scripts/wiki-gemma-model-sync.ajs](scripts/wiki-gemma-model-sync.ajs) (de plugin jArchi is nodig). Het toont eerst de lijst en voert pas uit na bevestiging. Wat de wiki zelf maakte en niet meer in de export staat, wordt verwijderd. Bij een GEMMA-object dat niet meer gekoppeld is, gaan alleen de `wiki-gemma-model`-eigenschappen weg.
   4. Controleer het resultaat en commit met coArchi.
5. **Daarna:** na de volgende GEMMA-release (skill `gemma-archimate-model-gemma-release`) staan de `wiki-gemma-model`-eigenschappen in GEMMA. De export negeert ze bij het overnemen en zet ze opnieuw.

## Grenzen

- Nooit exporteren of importeren zonder akkoord van de redacteur. De export draait alleen op verzoek van de redacteur; het AKKOORD bij `llmwiki promote apply` dekt hem niet. Importeren in GEMMA blijft aan de redacteur. Een definitieve export bevat alleen goedgekeurde elementen; akkoordvelden vul je nooit zelf in.
- Het exportbestand en het rapport zijn gegenereerd: nooit met de hand bewerken.
- Geen views: de export bevat alleen elementen, relaties en mappen.
