# Terugmeldingen

Een bevinding die niet in de wiki kan worden opgelost, gaat als terugmelding naar wie het model, de lijst of het informatiemodel beheert. Je zet haar in het register, zonder nummer; `tools/beslissen.py` geeft het volgende nummer en `tools/render.py` maakt de lijst en de sectie op de elementpagina.

## Drie registers

| Ontvanger | Register | Lijst | Typen | Velden |
|---|---|---|---|---|
| GGM-beheer | `beoordelingen/terugmeldingen/ggm.yaml` | `terugmeldingen/ggm-terugmeldingen.md` | `hiaat`, `definitie`, `structuur`, `scope`, `duplicaat`, `homoniem`, `relatie` | `{domein, entiteit, type, bevinding, element}` |
| Werkgroep procesarchitectuur (UPL-lijsten, kennismodel procesarchitectuur) | `beoordelingen/terugmeldingen/procesarchitectuur.yaml` | `terugmeldingen/procesarchitectuur-terugmeldingen.md` | `indeling`, `grondslag`, `product`, `kennismodel` | `{type, bevinding, elementen of beleidsdomein}` |
| GEMMA-team (het GEMMA-model zelf) | `beoordelingen/terugmeldingen/gemma.yaml` | `terugmeldingen/gemma-terugmeldingen.md` | `element`, `indeling`, `definitie`, `relatie` | `{type, bevinding, elementen en/of gemma_elementen}` |

## Opbouw

Schrijf een bevinding als lijst alinea's: eerst wat er nu staat, dan **Bevinding:** (wat er niet klopt of anders is, met bron) en **Voorstel:** (wat de ontvanger concreet kan veranderen). Een alinea die met `- ` begint, wordt een lijstitem (attributen, dubbele GUID's). In de tabel van de lijst staan de alinea's in één cel, met regelovergangen.

| Register | Eerste alinea |
|---|---|
| GGM | **GGM:** wat er nu staat |
| Procesarchitectuur | **UPL:** wat de UPL zegt, of bij type `kennismodel` **Kennismodel:** wat het kennismodel zegt |
| GEMMA | **GEMMA:** wat het GEMMA-model nu zegt |

Een open melding zonder alinea **Bevinding:** of **Voorstel:** houdt `tools/beslissen.py` tegen, in alle drie de registers (besluit redacteur 2026-10-08).

## Schrijven voor een lezer buiten de wiki

Schrijf voor een lezer zonder deze wiki: korte zinnen, de kern vooraan, bronnen achteraan tussen haakjes, geen interne termen zonder uitleg. Een terugmelding is een bevinding met een voorstel, geen vraag.

## GGM

Een bevinding over het GGM (hiaat, definitie, structuur, scope, duplicaat, homoniem, relatie). Een hiaat alleen bij een gegevensobject zonder GGM-match, conservatief: motiveer waar de gegevens worden beheerd, welke attributen relevant zijn en in welk beleidsdomein het past. Een proces, functie of regeling zonder GGM-entiteit is geen hiaat.

## Procesarchitectuur

De bevinding is voor de werkgroep procesarchitectuur: wat GEMMA anders indeelt of modelleert dan de UPL of het kennismodel, en waarom; geen vraag. In de alinea **Bevinding:** staat ook hoe GEMMA het modelleert en waarom.

- Een UPL-product zonder grondslag, of met een UPL-grondslag die geen taak geeft (alleen een tarief, een beleidsstuk van één gemeente), krijgt een melding van type `grondslag` (regel Wettelijke grondslag).
- Het model mag afwijken van de UPL-indeling (taakveld, GEMMA-domein) en van het kennismodel procesarchitectuur, mits de afwijking daar is teruggemeld (besluit redacteur 2026-10-05); de terugmelding dekt dan het signaal van `tools/beslissen.py`.
- Een nieuw element met dezelfde afwijking voeg je toe aan de `elementen` van de bestaande melding.

## GEMMA

Een bevinding over het GEMMA-model zelf: een GEMMA-element dat ontbreekt, in de wiki vervalt of herzien moet worden, een afwijkende indeling, definitie of relatie.

Het wiki-model wordt in het GEMMA-model geïmporteerd: een wiki-element dat aan een GEMMA-element is gekoppeld, werkt dat element bij (naam, definitie, relaties, indeling). Formuleer een melding daarom als wat de import in GEMMA verandert en wat het GEMMA-team moet controleren of beslissen, niet als een verzoek om iets over te nemen. De import verwijdert niets: wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team besluit. Laat de wiki een gekoppeld GEMMA-element vervallen, dan blijft het in GEMMA (de sync haalt alleen de wiki-eigenschappen weg); meld het dan hier.

Een GEMMA-element dat de wiki niet (meer) kent, noem je in `gemma_elementen` met `id` en `naam` zoals in het GEMMA-model; `tools/beslissen.py` controleert beide.

## Nummering en controles

- Een nieuwe melding heeft geen nummer; `tools/beslissen.py` geeft het volgende nummer en de status `open`.
- Status: open → gemeld → opgelost of afgewezen (met reden).
- `tools/beslissen.py` toetst de typen, de verplichte velden, de alinea's **Bevinding:** en **Voorstel:** bij een open melding, en bij GEMMA de `id` en `naam` van elk GEMMA-element.
