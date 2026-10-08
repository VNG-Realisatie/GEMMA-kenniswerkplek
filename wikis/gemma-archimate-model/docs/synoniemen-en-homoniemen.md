---
id: synoniemen-en-homoniemen
type: doc
titel: Synoniemen en homoniemen
bijgewerkt: '2026-10-01'
---

# Synoniemen en homoniemen

Hoe gaat het model om met andere woorden voor hetzelfde begrip, en met dezelfde naam voor een ander begrip? Deze analyse vergelijkt hoe de vorige bedrijfsobjectenwiki (repository GEMMA-GGM-bedrijfsobjectenwiki, map Bedrijfsarchitectuur) met synoniemen en homoniemen omging, met wat deze wiki nu doet, en adviseert hoe het past in de aanpak met kenmerken en beslistabel ([kenmerken per elementtype](kenmerken.md)).

## Begrippen

| Verhouding | Betekenis | Voorbeeld |
|---|---|---|
| Synoniem | ander woord, zelfde begrip | urn en asbus |
| Homoniem | zelfde woord, ander begrip | Regeling (soort wet of verordening) en Regeling in het GGM-domein Inkomen (afspraak met een cliënt) |
| Duplicaat | zelfde begrip, twee keer vastgelegd in een bron (in het GGM: andere GUID in een ander beleidsdomein) | Beschikking in Generiek Jeugd en Wmo en in Diensten |

## De vorige wiki

- **Naamconflict als eerste stap.** Vóór de grondslag werd gecontroleerd of de naam ondubbelzinnig is: een *wiki-collisie* (de naam bestaat al) of een *GGM-homoniem* (dezelfde GGM-entiteitnaam betekent in een ander beleidsdomein iets anders). Bij een conflict kreeg de redacteur twee of drie namen voorgelegd: domeinprefix, samengesteld woord of functionele naam, nooit haakjes. De keuze stond in `## Naamkeuze`. Voorbeeld: GGM-entiteit Inschrijving werd Opleidingsinschrijving, naast Aanbieding (Inschrijving in Inkoop).
- **Homoniem alleen bij een GGM-entiteit.** Een homoniem was "per definitie een naamcollisie tussen twee GGM-entiteiten". Een bedrijfsobject zonder eigen GGM-entiteit kon geen homoniem hebben.
- **Gestructureerd vastgelegd.** In de frontmatter stond `bo_homoniemen`, per item: link naar het andere bedrijfsobject, GGM-entiteit, GUID, beleidsdomein en toelichting. `bo_synoniemen` had per item een naam en een context (GGM, beleidsdocumenten, dagelijks gebruik). Duplicaten gingen naar `ggm_duplicaat_entiteiten`.
- **Detectie is een signaal, classificatie een besluit.** De beoordelingsstap signaleerde; de redacteur besliste of het een duplicaat of homoniem was. Beide werden teruggemeld aan het GGM.
- **Controle achteraf.** Een audit-modus "duplicaten" spoorde ongedocumenteerde naamconflicten op, nooit als bulkactie. De lint controleerde of homoniemen wederzijds waren en of synoniemen een naam en context hadden; of een afwijkende GGM-naam als synoniem was opgenomen, was nog niet geautomatiseerd.

## Deze wiki nu

Het meeste is al overgenomen:

- De beoordelingsstap signaleert een naamconflict (bestaand element of synoniem, GGM-naamgenoten) en classificeert duplicaat, homoniem of geen conflict; een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen conflict.
- De naamkeuze volgt dezelfde regels (twee of drie namen, geen haakjes, `## Naamkeuze`).
- Duplicaten gaan naar `ggm_duplicaat_entiteiten`; een homoniem staat in `## Homoniemen` met een link naar het andere element; de controle waarschuwt als die link niet wederzijds is.
- `synoniemen` heeft per item een naam en een context. Nieuw is de regel dat de naam uit de gangbare taal komt en de wetsterm synoniem wordt (precedent Urn, niet Asbus); de controle waarschuwt als dat lijkt om te draaien.
- Duplicaat en homoniem zijn typen van GGM-terugmeldingen.

Wat anders is of ontbreekt:

- **Geen gestructureerde homoniemen.** Verwijzingen naar elementen staan nooit in de frontmatter (render: verwijzingen als link in de body), dus `## Homoniemen` is vrije tekst (zoals bij Regeling). Herkomst (GGM-entiteit, GUID, beleidsdomein, of de bron) staat er niet vast in.
- **Homoniem is nog GGM-gebonden.** De naamgevingsregel noemt alleen de GGM-homoniem. Deze wiki werkt vanuit bronnen en voor alle elementtypen, en daar komen homoniemen voor die niets met het GGM te maken hebben: beheerder van een begraafplaats en beheerder van een landelijke voorziening ([toegang tot een bedrijfsobject](gegevensrollen.md)); rechthebbende op het graf en rechthebbende in het GGM en GEMMA.
- **Synoniem leidt niet tot een uitkomst.** Een begrip dat een synoniem blijkt van een bestaand element, heeft geen eigen uitkomst in de beslistabel; het wordt buiten de tabel om afgehandeld, terwijl de regel is dat alleen de beslistabel beslist of iets een element is (regel Beslistabel beslist).
- **Geen controle op afwijkende modelnamen.** Wijkt de GGM- of GEMMA-naam af van de naam van het element, dan hoort die als synoniem met context "GGM" of "GEMMA" te staan; dat wordt niet gecontroleerd.

## Hoe het past in de kenmerkenaanpak

Synoniemen en homoniemen zijn geen kenmerken van een begrip: ze gaan over de verhouding tussen een woord en een begrip. Ze horen daarom vóór de kenmerken, in een stap 0 *Welk begrip?*: eerst vaststellen welk begrip bedoeld is, dan pas de kenmerken van dat begrip beantwoorden.

Samen met drie bestaande kenmerken ontstaat zo één overzicht van de verhoudingen tot een ander begrip, elk met een vaste plek:

| Verhouding | Vraag | Plek | Uitkomst |
|---|---|---|---|
| synoniem | Is dit een ander woord voor een begrip dat al een element is (of in deze run wordt beoordeeld)? Noem dat element en de context van het woord. | stap 0 | geen nieuw element; het woord komt in `synoniemen` van het element, met context; staat in de begrippenlijst als "synoniem van" |
| homoniem | Bestaat dezelfde naam al voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron? Noem dat begrip en waar het voorkomt. | stap 0 | het begrip gaat door naar de kenmerken; naamkeuze voorleggen; `## Homoniemen` bij beide; bij een GGM-homoniem ook een terugmelding |
| eigenschap | *slechts eigenschap* | stap 2 | geen pagina; eigenschap van het genoemde begrip |
| onderdeel | *eigen identiteit* nee | stap 2 | geen pagina; relaties naar het geheel |
| specialisatie | *zelfstandige specialisatie* | stap 6 | eigen pagina, of geen pagina en relaties naar het bredere begrip |

Een duplicaat is geen verhouding tussen begrippen maar tussen vastleggingen in een bron; het blijft bij de GGM-match (`ggm_duplicaat_entiteiten`, terugmelding).

## Advies (besloten 2026-10-01, punt 4 en 5 volgen bij de herziening)

1. **Homoniem breed definiëren.** Zelfde naam, ander begrip, ongeacht de bron en voor alle elementtypen. Een GGM-homoniem krijgt daarnaast een terugmelding. Een actor of rol en een bedrijfsobject met dezelfde naam blijven een tegenhanger, geen homoniem.
2. **Stap 0 in de beslistabel.** Twee extra velden in de beoordeling, net als `genoemd_begrip`: `synoniem_van` en `homoniem_van`. Regel 0: `synoniem_van` gevuld → uitkomst *synoniem* (geen pagina, naam naar `synoniemen`); `homoniem_van` gevuld → door naar de kenmerken, met *voorleggen* voor de naamkeuze. Zo beslist de beslistabel ook hier, en staat de uitkomst in de begrippenlijst.
3. **`## Homoniemen` als tabel.** Kolommen: Begrip (link als er een pagina is), Betekenis, Waar (GGM-entiteit met GUID en beleidsdomein, GEMMA-element, of bron-id als link), Naamkeuze. Dat brengt de structuur van de vorige wiki terug zonder verwijzingen in de frontmatter.
4. **Controle uitbreiden.** Waarschuwen als de GGM- of GEMMA-naam afwijkt van de naam en niet als synoniem met context "GGM" of "GEMMA" staat; waarschuwen als een woord in `synoniemen` van twee elementen staat (dan is het een homoniem of een fout).
5. **Retroactief bij de herbeoordeling.** De naamconflicten van de bestaande 57 elementen worden in dezelfde run per onderwerp gecontroleerd, per geval voorgelegd (regel Per geval), zoals de audit-modus van de vorige wiki deed.

## Besluiten van de redacteur

| Datum | Besluit | Stand |
|---|---|---|
| 2026-10-01 | Een homoniem is: zelfde naam, ander begrip, in elke bron (wiki, GGM, GEMMA-model, wet, beleid) en voor elk elementtype. Naamkeuze en wederzijdse verwijzing altijd; een terugmelding alleen bij een GGM-homoniem. Een actor of rol en een bedrijfsobject met dezelfde naam blijven een tegenhanger. | skill beoordelen §3; references/naamgeving.md |
| 2026-10-01 | Synoniem en homoniem komen als stap 0 *Welk begrip?* in de beslistabel, met de velden `synoniem_van` en `homoniem_van` in de beoordeling. Synoniem: uitkomst *synoniem*, geen pagina, het woord naar `synoniemen` van het element, in de begrippenlijst als "synoniem van". Homoniem: door naar de kenmerken, naamkeuze voorleggen. | beslistabel (stap 0); skill criteria |
| 2026-10-01 | `## Homoniemen` wordt een tabel met de kolommen Begrip (link als er een pagina is), Betekenis, Waar (GGM-entiteit met GUID en beleidsdomein, GEMMA-element of bron als link) en Naamkeuze. De controle toetst per rij de wederzijdse link en, bij een GGM-homoniem, de terugmelding. | render (sectie Homoniemen) en tools/afleiden.py (controle) |

## Open vragen

Geen; de vragen van 1 oktober 2026 zijn beantwoord (zie de besluiten bovenaan).
