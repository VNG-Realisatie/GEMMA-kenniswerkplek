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
| `zwak` | Verwant, maar wezenlijk andere reikwijdte of granulariteit | Geen grondslag; hooguit een relatie noteren |
| `geen` | Geen GGM-entiteit | Geen `guid`; grondslag zonder GGM |

Een gegevensobject (`data_object: ja`) met een match zwakker dan `sterk` wordt voorgelegd. Elk bedrijfsobject en product heeft een `ggm`-blok, ook bij `geen`.

## Duplicaten en homoniemen

- **Duplicaat** (zelfde begrip in meerdere beleidsdomeinen, andere GUID): één element. De thematisch passende GUID wordt `guid`; de andere gaan in `duplicaten` (`guid`, `toelichting`). Leg de keuze van de primaire GUID voor en meld terug als `duplicaat`.
- **Homoniem** (zelfde naam, ander begrip): niet in `duplicaten`, wel in `homoniemen`; naam kiezen volgens `naamgeving.md`, terugmelden als `homoniem`.

## Velden en afwijking

De letterlijke `ggm_*`-velden haalt `tools/beslissen.py` bij elke run op; vul ze nooit zelf in. Een nieuwe GGM-release is na `beslissen` dus vanzelf verwerkt. Wijkt de GGM-definitie inhoudelijk af van de wet of de bronnen: zeg dat in de onderbouwing en meld terug als `definitie`. Wijkt de GGM-naam af van de naam: neem haar op in `synoniemen` met context "GGM".
