# Het JSON-formaat van sources/modellen/

Een model of lijst staat in `sources/modellen/` als origineel met een omzetting met dezelfde naam: `<bron-id>.<ext>` (het origineel, nooit gewijzigd) en `<bron-id>.json` (de omzetting). Eventueel staat er ook een `<bron-id>.md`: een leesbare weergave die de wiki erbij maakte, met regelnummers waar een bronduiding naar kan verwijzen. `llmwiki source add` kiest de map aan de hand van de vorm van het bestand (`.archimate`, AMEFF-xml en XMI-xml, `.xlsx`); de rol van de bron (`brontype`) doet daarbij niet mee.

Elke omzetting heeft dezelfde omhulling: `{"_gegenereerd": {"tool": "llmwiki.modellen", "vorm": "<vorm>", "hash": "<sha256 van data>"}, "data": {...}}`. De hash laat zien dat niemand de omzetting met de hand wijzigde (`llmwiki.modellen.controleer_json`). De sleutels van `data` staan alfabetisch.

## Vorm `archimate` (`archimate.py`)

Een Archi-bronbestand (`.archimate`, ook het opslagformaat van coArchi 2) of een ArchiMate Open Exchange-export (AMEFF). Het formaat staat in `data.model.formaat` (`archimate` of `ameff`).

- `elementen`: id → `{id, naam, type, documentatie, eigenschappen, map}`. `type` is het ArchiMate-type in kleine letters met koppeltekens (`business-object`). `map` is het pad van de map, gescheiden door ` / `.
- `relaties`: id → hetzelfde, met `bron` en `doel` (element-id's) en `type` met het achtervoegsel `-relationship`; bij toegang `toegang` (het Archi-accessType) en bij een gerichte associatie `gericht`.
- `model`: `{naam, eigenschappen, formaat}`, bij Archi ook `id` en `profielen`.
- Alleen bij Archi: `mappen` (id → `{id, naam, type, ouder, documentatie, eigenschappen}`), `map_id` per element en `profiel` (profiel-id's, gescheiden door een spatie) per element dat een specialisatie heeft. De AMEFF mist deze.

## Vorm `xmi` (`xmi.py`)

Een XMI 2.1-export uit Enterprise Architect, zoals het Gemeentelijk Gegevensmodel (GGM).

- `entities`: GUID → `{id, name, documentation, uml_type, stereotype, attributes, literals, tags, package_id, taakveld, beleidsdomein}`. `taakveld` en `beleidsdomein` komen uit de pakketstructuur (stereotype `Domein` en daarboven).
- `relations`: GUID → `{id, name, uml_type, stereotype, source_id, source_name, target_id, target_name, source_card, target_card, aggregatie, geheel, documentation, tags}`.
- `diagrams`: GUID → `{id, name, subjects}` (de GUID's van de entiteiten in het diagram).
- `packages`: GUID → `{id, name, parent_id, stereotype}`.

## Vorm `lijst` (`lijst.py`)

Een Excel-werkmap, zoals de Uniforme Productnamenlijst (UPL). `data.werkbladen` is een lijst van `{naam, rijen}`; elke rij is `{rij, cellen}` met het rijnummer uit Excel en de niet-lege cellen onder hun kolomletter (`{"A": "1", "B": "aangifte geboorte"}`). De celinhoud staat letterlijk in het JSON; een lege rij ontbreekt. De eerste rij van een werkblad is meestal de kop.
