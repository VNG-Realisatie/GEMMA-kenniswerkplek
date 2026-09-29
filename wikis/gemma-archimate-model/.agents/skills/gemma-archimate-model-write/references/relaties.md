# Relaties

Een relatie staat één keer, als rij in `## Relaties` op de pagina van het **bronelement** (de kant waar de ArchiMate-relatie begint), met een relatieve link naar het doel. Obsidian toont de andere kant als backlink; `tools/relaties.py inkomend <id>` geeft haar op de opdrachtregel.

```markdown
## Relaties

| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |
|---|---|---|---|---|---|---|
| compositie | [Onderdeel beschikking](onderdeel-beschikking.md) | bevat | 1 → 1..* | ggm-exact | EAID_… | 2026-overheid-awb (art. 1:3) |
| associatie (gericht) | [Zaak](../../../zaken/zaak.md) | hoort bij / leidt tot | 0..* → 1..* | ggm-afgeleid | EAID_…, EAID_… | |
| toegang (schrijven) | [Beschikking](…) | stelt vast | | bron | | 2026-utrecht-nota (§3.2) |
```

Relatie: `associatie`, `associatie (gericht)`, `aggregatie`, `compositie`, `specialisatie`, `toewijzing`, `toegang (lezen|schrijven|lezen-schrijven)`, `triggering`, `stroom`, `realisatie`, `bediening`.

## Uit het GGM (grondslag `ggm-exact` of `ggm-afgeleid`)

`uv run python tools/relaties.py voorstel <id> --bronnen <assessment.json> --markdown` geeft de kandidaten uit het GGM, samengevoegd met die uit de bronnen; voor het GGM-deel past de tool deze regels toe:

- **Mappen waar het kan.** `ggm-exact`: één GGM-relatie tussen de GGM-entiteiten van beide elementen.
- **Subtypes overslaan.** Relaties lopen alleen tussen opgenomen elementen. Een relatie op een specialisatie zonder pagina of een GGM-component wordt opgetild naar het element dat die draagt. Een keten A–X–B via een niet-opgenomen X wordt A–B (`ggm-afgeleid`), met het zwakste type in de keten (compositie > aggregatie > associatie) en een samengestelde kardinaliteit. Specialisaties worden niet geketend. Relaties naar enumeraties vervallen (eigenschap); dubbelingen worden samengevoegd; lussen vervallen.
- **Relatietype.**

  | GGM | Voorwaarde | ArchiMate |
  |---|---|---|
  | Generalization | beide kanten opgenomen | specialisatie |
  | Aggregation composite | naam wijst op deel-geheel ("bevat", "bestaat uit") of ontbreekt | compositie (geheel → deel) |
  | Aggregation shared | idem | aggregatie (geheel → deel) |
  | Aggregation | naam is geen deel-geheel ("leidt tot", "beschrijft") | associatie (gericht) + terugmeldkandidaat |
  | Association, Usage | — | associatie; gericht als de naam een leesrichting heeft |
  | Abstraction | "is een" | specialisatie, anders associatie; terugmeldkandidaat |

Jij kiest welke kandidaten je overneemt, geeft een herkenbare naam (beleid levert de taal) en laat puur technische relaties weg. Controleer de richting en de kardinaliteit: in het GGM-export zijn die niet altijd eenduidig.

## Uit de bronnen (grondslag `bron`, of bevestiging van een GGM-relatie)

Relaties uit de bronnen worden samen met de elementen gevonden:

1. **INGEST** — de bronanalyse noemt in `## Relaties` de relaties tussen begrippen zoals de bron ze formuleert: `| Van | Werkwoord | Naar | Vindplaats |`, met begripsnamen als platte tekst en het werkwoord letterlijk uit de bron.
2. **ASSESS** — de relaties gaan mee in het voorstel van het begrip aan de van-kant: `"relaties": [{"van": "…", "werkwoord": "…", "naar": "…", "bronnen": ["<bron-id>"], "vindplaats": "…"}]`. Na `bepaal_type.py evalueer --schrijf` toont `uv run python tools/relaties.py uit-bronnen <assessment.json>` welke relaties overblijven, welke zijn opgetild (een kant is een eigenschap of specialisatie zonder pagina) en welke vervallen (een kant is geen element), met reden. Leg vervallen relaties die wel belangrijk lijken voor aan de redacteur.
3. **WRITE** — `uv run python tools/relaties.py voorstel <id> --bronnen <assessment.json> --markdown` voegt ze samen met de GGM-kandidaten. Een bronrelatie tussen dezelfde elementen als een GGM-relatie bevestigt die (bron-id in kolom `Bron`, grondslag blijft `ggm-*`); anders wordt het een rij met grondslag `bron`, met de bron-id's en vindplaats in kolom `Bron`.

De typen van beide elementen bepalen de soort relatie, het werkwoord de richting en de variant:

| Van → naar | Relatie | Uit het werkwoord |
|---|---|---|
| actor/rol → proces, functie, rol | toewijzing | — |
| proces/functie → object | toegang | schrijven ("stelt vast", "neemt", "legt vast", "wijzigt" …) of lezen ("gebruikt", "toetst", "raadpleegt" …); anders lezen-schrijven |
| object → proces/functie | toegang, omgedraaid | idem |
| gebeurtenis ↔ gedrag, gedrag → gedrag | triggering | "leidt tot", "start"; "volgt op" draait de richting om |
| proces/functie → dienst | realisatie | — |
| dienst → actor/rol of gedrag | bediening | — |
| gedrag → gedrag | stroom | "levert aan", "geeft door aan" |
| elk → gelijk type | specialisatie | "is een" |
| object → object, product → dienst/object | compositie of aggregatie | "bestaat uit" → compositie; "bevat", "omvat" → aggregatie; "maakt deel uit van" draait de richting om |
| overig | associatie (gericht) | — |

Controleer elke voorgestelde relatie op richting en betekenis; de tool kent alleen de typen en het werkwoord. `tools/check_elementen.py` toetst elke rij aan de ArchiMate-relatietabel en eist dat elke bron-id een bronanalyse heeft.

## Terugmelden

Alleen bij `ggm-exact`: fout type, richting, kardinaliteit, naam of een dubbele relatie → `tools/terugmelding.py add --type relatie …` (de voorstel-uitvoer noemt kandidaten in het veld `terugmelding`). Nieuwe en afgeleide relaties worden niet teruggemeld. Bij tegenspraak tussen wet en GGM wint de wet.
