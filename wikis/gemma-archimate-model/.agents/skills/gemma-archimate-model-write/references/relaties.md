# Relaties

Een relatie staat één keer, als rij in `## Relaties` op de pagina van het **bronelement** (de kant waar de
ArchiMate-relatie begint), met een relatieve link naar het doel. Obsidian toont de andere kant als backlink;
`tools/relaties.py inkomend <id>` geeft haar op de opdrachtregel.

```markdown
## Relaties

| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie |
|---|---|---|---|---|---|
| compositie | [Onderdeel beschikking](onderdeel-beschikking.md) | bevat | 1 → 1..* | ggm-exact | EAID_… |
| associatie (gericht) | [Zaak](../../../zaken/zaak.md) | hoort bij / leidt tot | 0..* → 1..* | ggm-afgeleid | EAID_…, EAID_… |
| toegang (schrijven) | [Beschikking](…) | maakt | | bron | |
```

Relatie: `associatie`, `associatie (gericht)`, `aggregatie`, `compositie`, `specialisatie`, `toewijzing`,
`toegang (lezen|schrijven|lezen-schrijven)`, `triggering`, `stroom`, `realisatie`, `bediening`.

## Uit het GGM (grondslag `ggm-exact` of `ggm-afgeleid`)

`uv run python tools/relaties.py voorstel <id> --markdown` geeft de kandidaten; de tool past deze regels toe:

- **Mappen waar het kan.** `ggm-exact`: één GGM-relatie tussen de GGM-entiteiten van beide elementen.
- **Subtypes overslaan.** Relaties lopen alleen tussen opgenomen elementen. Een relatie op een specialisatie zonder
  pagina of een GGM-component wordt opgetild naar het element dat die draagt. Een keten A–X–B via een niet-opgenomen X
  wordt A–B (`ggm-afgeleid`), met het zwakste type in de keten (compositie > aggregatie > associatie) en een
  samengestelde kardinaliteit. Specialisaties worden niet geketend. Relaties naar enumeraties vervallen (eigenschap);
  dubbelingen worden samengevoegd; lussen vervallen.
- **Relatietype.**

  | GGM | Voorwaarde | ArchiMate |
  |---|---|---|
  | Generalization | beide kanten opgenomen | specialisatie |
  | Aggregation composite | naam wijst op deel-geheel ("bevat", "bestaat uit") of ontbreekt | compositie (geheel → deel) |
  | Aggregation shared | idem | aggregatie (geheel → deel) |
  | Aggregation | naam is geen deel-geheel ("leidt tot", "beschrijft") | associatie (gericht) + terugmeldkandidaat |
  | Association, Usage | — | associatie; gericht als de naam een leesrichting heeft |
  | Abstraction | "is een" | specialisatie, anders associatie; terugmeldkandidaat |

Jij kiest welke kandidaten je overneemt, geeft een herkenbare naam (beleid levert de taal) en laat puur technische
relaties weg. Controleer de richting en de kardinaliteit: in het GGM-export zijn die niet altijd eenduidig.

## Uit de bronnen (grondslag `bron`)

Relaties die niet in het GGM staan, met bron-id in de toelichting of in de bronanalyse. Typisch bij de andere typen:
toewijzing (actor → rol, actor/rol → proces of functie), toegang (proces/functie → object), triggering (gebeurtenis →
proces), realisatie (proces → dienst), bediening (dienst → actor/rol), aggregatie/compositie (product → dienst of
object, functie → proces). `tools/check_elementen.py` toetst elke rij aan de ArchiMate-relatietabel.

## Terugmelden

Alleen bij `ggm-exact`: fout type, richting, kardinaliteit, naam of een dubbele relatie → `tools/terugmelding.py add
--type relatie …` (de voorstel-uitvoer noemt kandidaten in het veld `terugmelding`). Nieuwe en afgeleide relaties
worden niet teruggemeld. Bij tegenspraak tussen wet en GGM wint de wet.
