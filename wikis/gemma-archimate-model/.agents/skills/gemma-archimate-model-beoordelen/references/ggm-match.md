# GGM-match

## Zoeken

`uv run python tools/ggm.py kandidaten <naam> [--synoniemen a,b]` geeft in één overzicht de entiteiten met dezelfde naam (mogelijke homoniemen of duplicaten), de treffers op naam, synoniem en definitie, en de termen die als attribuut of waarde voorkomen, elk met definitie, beleidsdomein en generalisaties. Verder: `entiteit <guid|naam>`, `relaties <guid>`, `generalisaties <guid>`. Nooit het XMI of `ggm/ggm_parsed.json` zelf doorzoeken; `ggm/` is alleen om te lezen.

## Kiezen op betekenis

Vergelijk de definities, volg relaties en generalisaties, en kijk naar het beleidsdomein. Een gelijke naam is geen match als de betekenis verschilt (homoniem); een andere naam kan wel een match zijn (synoniem).

## Sterkte (`ggm.sterkte`)

| Sterkte | Betekenis | Actie |
|---|---|---|
| `exact` | Zelfde begrip, definitie klopt | `guid` invullen |
| `sterk` | Zelfde begrip, definitie of reikwijdte wijkt licht af | `guid` invullen, afwijking in de onderbouwing, terugmelden |
| `partieel` | GGM dekt een deel, of het element bundelt meerdere entiteiten | `guid` van de beste entiteit, toelichting, terugmelding overwegen |
| `zwak` | Verwant, maar wezenlijk andere reikwijdte of granulariteit | Geen `guid`; hooguit een relatie noteren |
| `geen` | Geen GGM-entiteit | Geen `guid`; bij een object zeg je in de onderbouwing in welk proces het ontstaat, met de bron |

Een gegevensobject (`data_object: ja`) met een match zwakker dan `sterk` wordt voorgelegd. Elk bedrijfsobject en product heeft een `ggm`-blok, ook bij `geen`.

## Wat het GGM dekt

Het GGM modelleert vooral gegevens. Processen, functies, diensten, gebeurtenissen en regelingen zijn er doorgaans niet compleet in gedekt (uitzonderingen bestaan, bijv. GGM-beleidsdomein Normafwijking met Maatregel en Boete). Het ontbreken van een GGM-match is daar normaal en geen hiaat.

## Duplicaten en homoniemen

- **Eerst de betekenis, ook bij gelijke definitie.** Een naamgenoot is pas een duplicaat als het hetzelfde begrip is. Kijk naar de klant: de GEMMA-procesarchitectuur onderscheidt processen met externe klanten (van aanvraag tot product) van processen met interne klanten (Proceshiërarchie, Typen processen; Over GEMMA, Klant intern of extern). Een begrip dat de wet aan een externe klant koppelt, zoals de aanvraag, het besluit en de belanghebbende uit de Awb, is in een beleidsdomein van de interne organisatie (Financiën, HR, ICT, Inkoop, Organisatie, Subsidies, Vastgoed) meestal een ander begrip: een homoniem, ook als de GGM-definitie gelijk is. Precedent: Aanvraag in ICT is een interne aanvraag, Aanvraag in Archief en Diensten de externe aanvraag volgens de Awb.
- **Duplicaat** (zelfde begrip in meer beleidsdomeinen, andere GUID): één element. De thematisch passende GUID wordt `guid`; de andere gaan in `duplicaten` (`guid`, `toelichting`). Voor de relaties tellen alle GUID's even zwaar (`tools/relaties.py`); de keuze van de primaire GUID bepaalt alleen welke GGM-velden de pagina toont en welk GEMMA-object de wiki koppelt (zie `gemma-match.md`). Leg de keuze voor als de entiteiten elk een GEMMA-object hebben. Meld een duplicaat niet terug: het GGM werkt bewust met duplicaten, en dat GEMMA ze als losse bedrijfsobjecten overneemt, staat in één GEMMA-terugmelding voor alle duplicaten (Aanvraag en Pand als voorbeeld).
- **Homoniem** (zelfde naam, ander begrip): niet in `duplicaten`, wel in `homoniemen`; naam kiezen volgens `naamgeving.md`, terugmelden als `homoniem`, met een voorstel voor een onderscheidende naam en een definitie die het verschil vastlegt (zoals Interne aanvraag).

## Velden en afwijking

De letterlijke `ggm_*`-velden haalt `tools/beslissen.py` bij elke run op; vul ze nooit zelf in. Een nieuwe GGM-release is na `beslissen` dus vanzelf verwerkt. Wijkt de GGM-definitie inhoudelijk af van de wet of de bronnen: zeg dat in de onderbouwing en meld terug als `definitie`. Wijkt de GGM-naam af van de naam: neem haar op in `synoniemen` met context "GGM".
