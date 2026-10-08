# Relaties

Een relatie staat één keer, in `relaties` van de beoordeling van het **bronelement** (de kant waar de ArchiMate-relatie begint). Het render-script zet haar op de pagina van het bronelement en zet de inkomende kant op de pagina van het doel.

```yaml
relaties:
  - {soort: compositie, naar: onderdeel-beschikking, naam: bevat, kardinaliteit: "1 → 1..*", grondslag: ggm-exact, ggm_relatie: [EAID_…], bronnen: [2026-overheid-awb], vindplaats: art. 1:3}
  - {soort: associatie (gericht), naar: zaak, naam: hoort bij, grondslag: ggm-afgeleid, ggm_relatie: [EAID_…, EAID_…]}
  - {soort: toegang (registreren), naar: beschikking, naam: stelt vast, grondslag: bron, bronnen: [2026-utrecht-nota], vindplaats: § 3.2}
```

`soort`: `associatie`, `associatie (gericht)`, `aggregatie`, `compositie`, `specialisatie`, `toewijzing`, `toegang (<handeling>)` vanuit gedrag of `toegang (<verantwoordelijkheid>)` vanuit een rol of bedrijfssamenwerking, `triggering`, `stroom`, `realisatie`, `bediening`. `grondslag`: `ggm-exact`, `ggm-afgeleid` of `bron`; bij `bron` zijn `bronnen` verplicht. `tools/afleiden.py` toetst elke relatie aan de ArchiMate-relatietabel met de GEMMA-modelleerafspraken, en dat het doel een element is.

## Kandidaten

`uv run python tools/relaties.py voorstel <id>` geeft de kandidaten uit het GGM en uit de relatietabellen van de bronanalyses samen, als YAML voor `relaties:`; inkomende kandidaten staan als commentaar (die horen in de beoordeling van het andere element). Kies, geef een herkenbare naam (beleid levert de taal), laat puur technische relaties weg, en controleer richting en kardinaliteit: in het GGM-export zijn die niet altijd eenduidig.

Voor het GGM-deel past de tool deze regels toe:

- **Mappen waar het kan.** `ggm-exact`: één GGM-relatie tussen de GGM-entiteiten van beide elementen.
- **Subtypes overslaan.** Een relatie op een specialisatie zonder pagina of een GGM-component wordt opgetild naar het element dat die draagt. Een keten A–X–B via een niet-opgenomen X wordt A–B (`ggm-afgeleid`), met het zwakste type in de keten (compositie > aggregatie > associatie) en een samengestelde kardinaliteit. Specialisaties worden niet geketend. Relaties naar enumeraties vervallen (eigenschap); dubbelingen worden samengevoegd; lussen vervallen.
- **Relatietype.**

  | GGM | Voorwaarde | ArchiMate |
  |---|---|---|
  | Generalization | beide kanten opgenomen | specialisatie |
  | Aggregation composite | naam wijst op deel-geheel ("bevat", "bestaat uit") of ontbreekt | compositie (geheel → deel) |
  | Aggregation shared | idem | aggregatie (geheel → deel) |
  | Aggregation | naam is geen deel-geheel ("leidt tot", "beschrijft") | associatie (gericht) + terugmeldkandidaat |
  | Association, Usage | — | associatie; gericht als de naam een leesrichting heeft |
  | Abstraction | "is een" | specialisatie, anders associatie; terugmeldkandidaat |

Een bronrelatie tussen dezelfde elementen als een GGM-relatie bevestigt die (de bron komt erbij, de grondslag blijft `ggm-*`); anders wordt het een relatie met grondslag `bron`.

## Uit de bronnen

De bronanalyse noemt in `## Relaties` de verbanden tussen begrippen zoals de bron ze formuleert (`| Van | Werkwoord | Naar | Vindplaats |`). De tool lost de begrippen op via de beoordelingen (naam of synoniem); is een kant een eigenschap, onderdeel of specialisatie zonder pagina, dan wordt de relatie opgetild naar het genoemde begrip; is een kant geen element, dan vervalt ze (`tools/relaties.py uit-bronnen <onderwerp>` toont welke en waarom). Leg vervallen relaties die wel belangrijk lijken voor aan de redacteur.

De typen van beide elementen bepalen de soort relatie, het werkwoord de richting en de variant:

| Van → naar | Relatie | Uit het werkwoord |
|---|---|---|
| rol, bedrijfssamenwerking → proces, functie | toewijzing | — |
| actor → rol | toewijzing | alleen bij "vervult", "treedt op als", "fungeert als"; andere werkwoorden tussen partijen ("benoemt", "waarschuwt") → gerichte associatie |
| actor → gedrag of object | — | een actor hangt alleen via een rol aan gedrag en objecten (besluit 2026-10-01): leg de rol vast |
| rol → object | toegang (verantwoordelijkheid) | houder ("houdt"), bronhouder ("houdt bij"), beheerder ("beheert", "onderhoudt"), verstrekker, afnemer ("ontvangt", "gebruikt"), toezichthouder, betrokkene, partij (alleen naar een afspraak); een handeling ("vraagt aan", "geeft af") wordt een toewijzing van de rol aan het proces |
| proces/functie → object | toegang (handeling) | registreren ("stelt vast", "legt vast", "verleent", "ontvangt" …), bijwerken ("wijzigt", "onderhoudt", "ruimt" …), beëindigen ("trekt in", "heft op" …), raadplegen ("gebruikt", "vereist", "toetst" …), verstrekken, bewaren, overbrengen, vernietigen |
| object → proces/functie | toegang (handeling), omgedraaid | idem |
| functie → proces | bediening | de functie bedient het proces; geen aggregatie |
| kanaal → dienst; kanaal → rol | toewijzing; bediening | — |
| gebeurtenis ↔ gedrag, gedrag → gedrag | triggering | "leidt tot", "start"; "volgt op" draait de richting om |
| proces/functie → dienst | realisatie | — |
| dienst → rol of gedrag | bediening | — (een dienst krijgt geen rol toegewezen en heeft geen toegang tot een object) |
| beleidskader → proces, dienst, product | associatie (gericht), naam "is grondslag voor"; bij een beleidskader in de groep Richtlijn "geeft richtlijn voor" (geen wettelijke grondslag) | — |
| gedrag → gedrag | stroom | "levert aan", "geeft door aan" |
| elk → gelijk type | specialisatie | "is een" |
| object → object, product → dienst/object | compositie of aggregatie | "bestaat uit" → compositie; "bevat", "omvat" → aggregatie; "maakt deel uit van" draait de richting om |
| overig | associatie (gericht) | — |

Controleer elke voorgestelde relatie op richting en betekenis; de tool kent alleen de typen en het werkwoord.

## Terugmelden

Alleen bij `ggm-exact`: fout type, richting, kardinaliteit, naam of een dubbele relatie → een terugmelding van type `relatie` in `beoordelingen/terugmeldingen/ggm.yaml` (het voorstel noemt kandidaten in het commentaar). Nieuwe en afgeleide relaties worden niet teruggemeld. Bij tegenspraak tussen wet en GGM wint de wet.
