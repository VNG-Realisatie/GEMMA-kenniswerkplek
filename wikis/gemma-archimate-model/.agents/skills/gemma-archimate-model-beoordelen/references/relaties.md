# Relaties

Een relatie staat één keer, in `relaties` van de beoordeling van het **bronelement** (de kant waar de ArchiMate-relatie begint). Het render-script zet haar op de pagina van het bronelement en zet de inkomende kant op de pagina van het doel.

```yaml
relaties:
  - {soort: compositie, naar: onderdeel-beschikking, naam: bevat, kardinaliteit: "1 → 1..*", grondslag: ggm-exact, ggm_relatie: [EAID_…], bronnen: [2026-overheid-awb], vindplaats: art. 1:3}
  - {soort: associatie (gericht), naar: zaak, naam: hoort bij, grondslag: ggm-afgeleid, ggm_relatie: [EAID_…, EAID_…]}
  - {soort: toegang (registreren), naar: beschikking, naam: stelt vast, grondslag: bron, bronnen: [2026-utrecht-nota], vindplaats: § 3.2}
```

`soort`: `associatie`, `associatie (gericht)`, `aggregatie`, `compositie`, `specialisatie`, `toewijzing`, `toegang (<handeling>)` vanuit gedrag of `toegang (<verantwoordelijkheid>)` vanuit een rol of bedrijfssamenwerking, `triggering`, `stroom`, `realisatie`, `bediening`. `grondslag`: `ggm-exact`, `ggm-afgeleid` of `bron`; bij `bron` zijn `bronnen` verplicht. `tools/beslissen.py` toetst of de relatie geldig is in ArchiMate en of het doel een element is; dat zijn de enige fouten.

## Volgorde

Leg per element alle relaties vast die de bronnen noemen en die geldig zijn in ArchiMate, ook als het kennismodel ze niet kent. Het kennismodel bepaalt niet wat je vastlegt maar wat de export meeneemt: een relatie erbuiten krijgt een signaal en een markering op de pagina (*niet in het kennismodel, gaat niet mee in de export*), en vervalt in de export. Welke relaties per elementtype toegestaan zijn, en welke zijn weggefilterd met reden, staat in de modelleerafspraken van dat type (`kennismodel/README.md`); herhaal die tabel hier niet. Een signaal beoordeel je per geval: de relatie hoort bij een andere vorm van modelleren (leg dat de redacteur voor), of ze blijft staan omdat de bron haar noemt.

De stappen, in deze volgorde; bij het beoordelen gebeuren ze vaak tegelijk, uit dezelfde wettekst:

1. **Grondslag:** *is grondslag voor* vanuit een beleidskader (regel Wettelijke grondslag).
2. **Kernrelatie** van het type: de relatie die het kenmerk waarmaakt. Een kenmerk `ja` zonder zo'n relatie geeft een signaal.
3. **Indelingsrelaties:** levensloopproces → aggregatie → bedrijfsproces, de functieketen, het kernobject.
4. **Overige relaties** uit de bronanalyse: per partij wat zij houdt, beheert, uitvoert of vervult; toegang met een handeling of verantwoordelijkheid.
5. **GGM-match van de relatie**, alleen bij bedrijfsobjecten, data-objecten en beleidsdomeinen (zie `ggm-match.md`).
6. **GEMMA:** zonder match gaat de relatie als nieuw mee in de export.

## Kandidaten

`uv run python tools/relaties.py voorstel <id>` geeft de relaties uit de relatietabellen van de bronanalyses, met hun match in het GGM, als YAML voor `relaties:`; inkomende kandidaten staan als commentaar (die horen in de beoordeling van het andere element). Kies, geef een herkenbare naam (beleid levert de taal), laat puur technische relaties weg, en controleer richting en kardinaliteit: in het GGM-export zijn die niet altijd eenduidig.

Het GGM is matchdoel, geen bron: een GGM-relatie dient alleen om een gevonden relatie te matchen. Bij het zoeken van de match past de tool deze regels toe:

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

Een gevonden relatie tussen dezelfde elementen als een GGM-relatie krijgt die als match (de bron komt erbij, de grondslag wordt `ggm-*`); zonder GGM-relatie wordt het een relatie met grondslag `bron`. Een GGM-relatie zonder gevonden relatie wordt geen voorstel: de tool noemt haar als commentaar, met een aanwijzing als er al een relatie met dat element in de beoordeling staat (match die dan met de hand). Neem haar alleen op als een bron haar noemt (regel Elke claim een bron).

## Uit de bronnen

De bronanalyse noemt in `## Relaties` de verbanden tussen begrippen zoals de bron ze formuleert (`| Van | Werkwoord | Naar | Vindplaats |`). De tool lost de begrippen op via de beoordelingen (naam of synoniem); is een kant een eigenschap, onderdeel of specialisatie zonder pagina, dan wordt de relatie opgetild naar het genoemde begrip; is een kant geen element, dan vervalt ze (`tools/relaties.py uit-bronnen <onderwerp>` toont welke en waarom). Leg vervallen relaties die wel belangrijk lijken voor aan de redacteur.

De typen van beide elementen bepalen de soort relatie, het werkwoord de richting en de variant:

| Van → naar | Relatie | Uit het werkwoord |
|---|---|---|
| rol, bedrijfssamenwerking → proces, functie | toewijzing | — |
| actor → rol | toewijzing | alleen bij "vervult", "treedt op als", "fungeert als"; andere werkwoorden tussen partijen ("benoemt", "waarschuwt") → gerichte associatie |
| actor → gedrag of object | — | een actor hangt alleen via een rol aan gedrag en objecten: leg de rol vast |
| rol → object | toegang (verantwoordelijkheid) | houder ("houdt"), bronhouder ("houdt bij"), beheerder ("beheert", "onderhoudt"), verstrekker, afnemer ("ontvangt", "gebruikt"), toezichthouder, betrokkene, partij (alleen naar een afspraak); bij de AVG een toevoeging in de naam, bijvoorbeeld "houder (verwerkingsverantwoordelijke)", met het wetsartikel als vindplaats; een handeling ("vraagt aan", "geeft af") wordt een toewijzing van de rol aan het proces |
| proces/functie → object | toegang (handeling) | registreren ("stelt vast", "legt vast", "verleent", "ontvangt" …), bijwerken ("wijzigt", "onderhoudt", "ruimt" …), beëindigen ("trekt in", "heft op" …), raadplegen ("gebruikt", "vereist", "toetst" …), verstrekken, bewaren, overbrengen, vernietigen |
| object → proces/functie | toegang (handeling), omgedraaid | idem |
| functie → proces | bediening | de functie bedient het proces; geen aggregatie |
| kanaal → dienst; kanaal → rol | toewijzing; bediening | — |
| gebeurtenis ↔ gedrag, gedrag → gedrag | triggering | "leidt tot", "start"; "volgt op" draait de richting om |
| proces/functie → dienst | realisatie | — |
| dienst → rol of gedrag | bediening | — (een dienst krijgt geen rol toegewezen en heeft geen toegang tot een object) |
| product → rol | bediening | het product bedient de rol van de afnemer (kennismodel regel 596: Product → bediening → Klant; Grafuitgifte bedient Rechthebbende op het graf) |
| beleidskader → proces, dienst, product | associatie (gericht), naam "is grondslag voor"; bij een beleidskader in de groep Richtlijn "geeft richtlijn voor" (geen wettelijke grondslag); bij een beleidskader in de groep Gemeentelijke regelgeving alleen "is grondslag voor" naar een UPL-product of -dienst zonder landelijke grondslag, anders "werkt uit voor" (regel Wettelijke grondslag). Bij voorkeur naar een product (kennismodel regel 595); naar een proces of dienst als er geen product is | — |
| gedrag → gedrag | stroom | "levert aan", "geeft door aan" |
| elk → gelijk type | specialisatie | "is een" |
| object → object, product → dienst/object | compositie of aggregatie | "bestaat uit" → compositie; "bevat", "omvat" → aggregatie; "maakt deel uit van" draait de richting om |
| overig | associatie (gericht) | — |

Controleer elke voorgestelde relatie op richting en betekenis; de tool kent alleen de typen en het werkwoord.

## Terugmelden

Alleen bij `ggm-exact`: fout type, richting, kardinaliteit, naam of een dubbele relatie → een terugmelding van type `relatie` in `beoordelingen/terugmeldingen/ggm.yaml` (het voorstel noemt kandidaten in het commentaar). Nieuwe en afgeleide relaties worden niet teruggemeld. Bij tegenspraak tussen wet en GGM wint de wet.
