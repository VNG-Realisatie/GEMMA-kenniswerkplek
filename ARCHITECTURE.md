# Architectuur-Kompas

Dit is de korte uitleg van hoe deze repository werkt. Voor wie een nieuwe wiki inricht: `docs/kluswijzer.md`. Voor de redenen achter elke keuze, met bronnen: `docs/onderbouwing.md`.

## 1. Wat is een LLM-wiki?

Een LLM-wiki is een verzameling kennispagina's die we samen met een AI-assistent bijhouden. Bij elke wiki horen pagina's, een eigen kijk op de gedeelde bronnen, huisregels (Rules), vaardigheden (Skills), werkstromen (Workflows) en gereedschap (Tools). Wat voor elke wiki geldt, staat één keer in de gedeelde laag; wat voor één wiki geldt, in de map van die wiki.

### Soorten wiki's

Drie soorten, benoemd naar hun doel:

| Soort (`wiki.yaml` `type:`) | Doel | Waar staat de waarheid | Laatste stap |
|---|---|---|---|
| `sync` | Een MediaWiki-site beheren, bijvoorbeeld GEMMA Online | Op de site | Publiceren na akkoord (git-diff-review) |
| `curation` | Gestructureerde kennis opbouwen, optioneel tot een export (ArchiMate, UML/XMI, CSV, MediaWiki) | In de repository | Kandidaten goedkeuren (`kandidaat` → `review` → `goedgekeurd`), en met een ingevuld `exports:`-blok: daarna exporteren per doel |
| `knowledge-base` | Ongestructureerde kennis opbouwen: notities, adviezen, ontwerpen, architectuurdocumenten — eigen eindresultaten | In de repository | Geen — review via een gewone `git diff`/commit |

De soorten vormen samen een keten. Wat de ene wiki oplevert, wordt een bron voor de volgende:

```text
Beleidskader (curation) → Begrippen & ArchiMate (curation + exports) → Informatiemodellen (curation + exports) → GEMMA Online (sync)
```

### Gereedschap bij een sync-wiki

Een sync-wiki gebruikt twee soorten toegang tot de externe site, elk voor een ander moment:

| Gereedschap | Wanneer | Wat |
|---|---|---|
| MCP (`mediawiki`) | Tijdens het bewerken: verkennen, opzoeken, een pagina lezen | Alleen-lezen, interactief vanuit de AI-omgeving, wijst altijd naar het hoofddoel (nooit een testomgeving) |
| `llmwiki pull` / `llmwiki publish` (pywikibot) | Vóór het bewerken (ophalen naar `content/`) en ná akkoord (schrijven) | Enige weg naar schrijven; nooit via MCP, altijd na de publicatiegate |

Achtergrond en het volledige ontwerp: `docs/onderbouwing.md` 5.10.

### Bronnen: drie lagen

Alle bronnen staan één keer centraal in de repository en worden door alle wiki's gedeeld.

| Laag | Plaats | Wat | Voor wie |
|---|---|---|---|
| 1. Origineel | `sources/raw/` | Het document (pdf, docx) en een Markdown-versie met dezelfde naam. Wordt nooit gewijzigd | Alle wiki's |
| 2. Intake | `sources/index/<bron>.md` | Gegevens, samenvatting en thema's, één keer gemaakt | Alle wiki's |
| 3. Domein-lens | `wikis/<wiki>/bronnen/<onderwerp>/<bron>.md` | Wat deze bron betekent voor dit domein, met uittreksels | Eén wiki |

Zo voorkomen we dat een wiki verzuipt in alle bronnen:
- **Filter per wiki.** In `wiki.yaml` staat welke thema's (tags) een wiki gebruikt. Andere bronnen ziet de AI voor die wiki niet.
- **Werk vanuit een onderwerp.** Elke taak begint bij een onderwerppagina (`onderwerpen/<thema>.md`). Die pagina noemt de bronnen die ertoe doen; alleen die leest de AI.

## 2. Principes

1. **De mens beslist.** De AI bereidt voor. Publiceren of exporteren gebeurt alleen na een bewuste handeling van een redacteur.
2. **Herleidbaar van bron tot begrip.** Voor elke wijziging is terug te vinden welke bron is gelezen, welk voorstel is gedaan en wie het heeft goedgekeurd.
3. **Eén keer vastleggen.** Gedeelde werkwijzen staan op één plek. Een wiki vult ze aan, maar kopieert ze niet.
4. **Werkt in elke AI-omgeving.** Dezelfde wiki werkt in Claude Code, OpenCode, VS Code/Copilot, Cursor en Codex, op Windows, Linux en macOS. Daarvoor gebruiken we open standaarden (AGENTS.md, Agent Skills, MCP).
5. **Kladblok is geen archief.** Tussenstappen van de AI blijven onzichtbaar en worden opgeruimd. Alleen afgeronde, betekenisvolle verslagen komen in de officiële historie.
6. **Wat vast kan, staat in code.** Ophalen, controleren, vergelijken en publiceren doet een programma, niet de AI.
7. **Niets toevoegen zonder reden.** Een extra bestand, laag of instelling komt er alleen als het een concreet probleem oplost.

## 3. Plattegrond

De hele repository is één Obsidian-vault, zodat links naar de gedeelde bronnen overal werken.

```text
llm-wikis/                    open deze map in Obsidian
├── AGENTS.md                 huisregels voor de hele repository
├── ARCHITECTURE.md           dit kompas
├── docs/                     kluswijzer en onderbouwing
├── sources/
│   ├── raw/                  originelen + Markdown-versie   (nooit wijzigen)
│   └── index/                één intakepagina per bron
├── .agents/skills/           gedeelde vaardigheden en de gedeelde werkstroom
├── tools/llmwiki/              gereedschap
└── wikis/
    ├── gemma/                type sync: GEMMA Online, kale werkkopie
    │   ├── AGENTS.md · wiki.yaml
    │   ├── content/          de MediaWiki-pagina's, directe werkkopie
    │   ├── revisies.json     conflictbasis: titel → laatst bekende revisie
    │   ├── log.md            logboek: wie publiceerde wat, wanneer (alleen aanvullen)
    │   └── voorstellen/      publicatievoorstellen ter beoordeling
    ├── gemma-kennis/         type knowledge-base: notities/adviezen/ontwerpen
    │   ├── AGENTS.md · wiki.yaml
    │   └── <onderwerp>/<document>.md
    └── opzet2/               type curation (met of zonder exports:)
        ├── AGENTS.md · wiki.yaml
        ├── onderwerpen/      ingang voor elke taak
        ├── bronnen/<onderwerp>/
        ├── kandidaten/       voorgestelde begrippen met status
        ├── export/           goedgekeurde exports (alleen met exports:-blok)
        ├── log.md            logboek: wie keurde wat goed   (alleen aanvullen)
        ├── voortgang.md      overzicht van open werk        (automatisch)
        └── voorstellen/
```

Links tussen pagina's zijn gewone relatieve Markdown-links; ze werken in Obsidian en in VS Code. Mappen die met een punt beginnen (`.agents`, `.work`, `.claude` enzovoort) zijn voor de AI-omgevingen; `.work/` is het kladblok van de AI en staat niet in Git.

## 4. Hoe een update verloopt

### Voorbeeld: een pagina bijwerken op GEMMA Online (sync)

De redacteur vraagt: *"Werk de pagina Zaakgericht werken bij met deze wijziging,
met wiki-edit."*

| Stap | Wat gebeurt er | Wie |
|---|---|---|
| PULL | Pagina ophalen naar `content/` (of al lokaal aanwezig) | Gereedschap, via pywikibot |
| BEWERK | `content/`-bestand direct aanpassen | AI |
| VALIDATE | Controle op vorm, links | Gereedschap en AI |
| PLAN | Voorstel met git-diff, gebaseerd op de actuele revisie op de site | Gereedschap |
| Akkoord | Beoordelen van het publicatievoorstel en akkoord geven | Redacteur |
| PUBLISH | Publiceren naar de wiki en een regel in `log.md` | Gereedschap, na goedkeuring |

Een tussentijdse wijziging van diezelfde pagina op de site (door iemand anders)
wordt bij PUBLISH herkend en geweigerd — niet stilzwijgend overschreven.

### Voorbeeld: een beleidsnota verwerken in een curatie-wiki

De redacteur vraagt: *"Verwerk deze nota voor onderwerp zaakgericht werken met
opzet2-update-wiki."*

| Stap | Wat gebeurt er | Wie |
|---|---|---|
| INGEST | Nieuwe bron: origineel en Markdown-versie in `sources/raw/`, intake in `sources/index/`. Bestaat de intake al, dan wordt die hergebruikt. Daarna de domein-lens in `bronnen/<onderwerp>/` | Gereedschap en AI |
| ASSESS | Welke kandidaat-begrippen moeten veranderen, en waarom? | AI |
| WRITE | Voorstellen voor nieuwe of gewijzigde kandidaten | AI |
| VALIDATE | Controle op vorm, links, curatieregels | Gereedschap en AI |
| Akkoord | Beoordelen van het promotievoorstel en akkoord geven | Redacteur |
| PROMOTE | Kandidaat op `goedgekeurd` zetten en vastleggen in `log.md` | Gereedschap, na goedkeuring |

Na elke stap wordt het tussenresultaat in het kladblok bewaard. Wordt het werk
onderbroken, dan pakt de AI het later op vanaf de laatste afgeronde stap. Een
afgebroken taak laat niets achter in de wiki. Voor beide soorten geldt: de
publicatie/promotie staat na afloop in `log.md` — dat is het blijvende verslag,
niet op de externe site.

Bij een Markdown-wiki (curation) zijn de bron- en kandidaatpagina's zelf het archief. De laatste stap heet daar **goedkeuren**: kandidaten gaan van `kandidaat` via `review` naar `goedgekeurd`. De AI mag een kandidaat ter review aanbieden, maar alleen de redacteur keurt goed, via dezelfde twee smaken als bij publiceren. Elke goedkeuring komt in `log.md`. Een pagina die op `goedgekeurd` staat zonder regel in `log.md`, wordt bij opslaan in Git geweigerd.

## 5. Spelregels

### Wie doet wat

| Rol | Doet | Doet nooit |
|---|---|---|
| Redacteur | Stelt de Vraag, beoordeelt voorstellen, geeft akkoord | — |
| AI-assistent | Leest, analyseert, schrijft voorstellen, controleert | Zelf publiceren of exporteren, akkoordvelden invullen |
| Gereedschap | Haalt pagina's op, controleert, publiceert, legt vast | Inhoudelijk oordelen |
| AI-omgeving | Vraagt de redacteur om een klik voordat er gepubliceerd wordt | — |

### Akkoord geven: twee smaken

Per wiki staat in `wiki.yaml` welke smaak geldt.

- **Smaak A, vrijgave via document.** Geschikt voor grotere of periodieke wijzigingen en voor exports naar het architectuurmodel. De AI zet een publicatievoorstel klaar in `voorstellen/`. De redacteur leest het in de eigen editor, zet `akkoord_voor_publicatie` op `ja`, vult een naam in en vraagt de AI de publicatie uit te voeren. Is het voorstel daarna nog veranderd, dan geldt het akkoord niet meer.
- **Smaak B, bevestigingswoord in de chat.** Geschikt voor dagelijks redactiewerk. De AI toont een samenvatting en vraagt om het woord **AKKOORD**. "Prima" of "ziet er goed uit" is geen akkoord.

In beide smaken vraagt de AI-omgeving daarna nog om één klik op "toestaan". Die klik kan de AI niet zelf geven; dat is de echte beveiliging.

**Daarom: zet automatische goedkeuring in de AI-omgeving uit wanneer je publiceert.** Met automatische goedkeuring vervalt die klik.

### Werkplek eerst

Bij de eerste vraag in een nieuwe sessie controleert de AI of de werkplek in orde is en richt die zo nodig in, na toestemming. Pas daarna begint het inhoudelijke werk. Soms is een handeling van jezelf nodig, zoals het goedkeuren van de koppeling met de wiki of het invullen van je inloggegevens. De AI legt dan uit wat je moet doen. Op Windows zijn geen beheerdersrechten nodig.

### Huisregels

- Regels voor de hele repository staan in `AGENTS.md` in de hoofdmap. Regels voor één wiki staan in `AGENTS.md` in de wikimap en verwijzen naar de hoofdregels.
- Een gedeelde vaardigheid bevat nooit kennis van één specifieke wiki.
- Vaardigheden van een wiki beginnen met de naam van die wiki (`gemma-…`). Gedeelde vaardigheden beginnen met `wiki-`.
- Plaats geen `CLAUDE.md` in de repository: daarmee negeert Claude Code de huisregels.
- Bestanden in `sources/raw/` worden nooit gewijzigd. Een nieuwe versie van een document is een nieuwe bron.
- Een wiki verwijst niet naar pagina's van een andere wiki. Wat de volgende wiki in de keten nodig heeft, wordt na goedkeuring als bron toegevoegd aan `sources/`.

## 6. Begrippen

| Begrip | Betekenis hier |
|---|---|
| Vraag / Antwoord | Wat je de AI vraagt / wat de AI teruggeeft |
| Sessie | Eén gesprek in een AI-omgeving |
| Model | Het taalmodel dat de tekst verwerkt en maakt |
| Rules | Huisregels in `AGENTS.md` |
| Skill | Uitgeschreven werkwijze voor één taak |
| Workflow | Volgorde van stappen, zelf ook vastgelegd als Skill |
| Agent / Rol | De AI die een taak uitvoert / de verantwoordelijkheid die hij daarbij heeft (lezer, beoordelaar, schrijver, controleur) |
| Tool | Programma of functie buiten het model |
| MCP | Standaardkoppeling tussen de AI-omgeving en de MediaWiki-site |
| Context | Wat de AI op dit moment "ziet" |
| State | Waar een taak staat; bewaard in het kladblok |
| Resultaat | Bijgewerkte pagina's, verslagen en na akkoord de publicatie |

## 7. Verder lezen

- Een nieuwe wiki of repository inrichten: `docs/kluswijzer.md`
- Waarom het zo is ingericht, per AI-omgeving: `docs/onderbouwing.md`
