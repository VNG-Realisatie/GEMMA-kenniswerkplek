# Besluiten: voorleggen en vastleggen

## Voorleggen

Leg per Sessie in één tabel voor in de chat: in Sessie 1 de uitkomst van Typeren voor het hele onderwerp, in Sessie 3 na `uv run python tools/beslissen.py` de begrippen met redenen om voor te leggen (`beslist.open`, ook in `ter-beoordeling.md`) en de `vragen:`. Spaar vragen op in `vragen:`; alleen een blokkerende vraag komt meteen.

**Alleen echte twijfel.** Een twijfelgeval is een keuze tussen verdedigbare alternatieven die niet volgt uit de beslistabel, een regel, een bron of een eerder besluit. Alleen dat leg je voor, zoals aan een architect, niet aan een jurist. De redacteur kent ArchiMate, GEMMA, de opbouw van het GGM, de beslistabel en de regels van deze wiki: leg die niet uit, en geef geen juridische uitleg, geen lange citaten (alleen een citaat dat de doorslag geeft) en niet de volledige kenmerkenlijst. Geef per twijfelgeval mee:

- het begrip in één zin in gewone taal: wie doet wat, met welk object, met welk resultaat;
- wat de bron zegt, samengevat, met de bron als link en het artikel als vindplaats, en wat GEMMA en het GGM hebben;
- de opties, met per optie het gevolg voor het model: welk element, welke relaties, welke pagina, wat de export in GEMMA verandert;
- een concreet voorbeeld uit het model, een advies met de reden en een eerder besluit met zijn zekerheid.

Wat eenduidig volgt, staat ter bevestiging in de samenvatting en leg je niet los voor: een stop in Afbakenen zonder twijfel, een toets die het script doet, een thuisonderwerp dat eenduidig uit de inhoud volgt (regel Thuishoren) en een landelijke grondslag die eenduidig in de nagelezen wettekst staat (regel Wettelijke grondslag).

## Vastleggen

Een besluit staat bij waar het over gaat, zonder register.

- **Over één begrip:** in `besluiten:` van zijn beoordeling.
- **Over een onderwerp als geheel** (afbakening, indeling, afronding): in `besluiten:` van het onderwerp (`onderwerpen/<onderwerp>/afbakening.yaml`).
- **Over een begrip zonder beoordeling:** voorlopig in `besluiten:` van het onderwerp, met `begrip`; krijgt het begrip een beoordeling, dan verhuist het besluit letterlijk daarheen (regel Letterlijk verplaatsen).

In een beoordeling:

```yaml
besluiten:
  - datum: 2026-10-01
    besluit: Geen GEMMA-match met Uitvoeren participatie (Omgevingswet): een andere participatie; afgewezen: deelproces van Vaststellen beleid.
    gevolg: verwerkt                # verwerkt | afwijzen
    zekerheid: logica               # kennis | logica | indruk
    stand: open: …                  # alleen bij een besluit dat nog open staat
```

`afwijzen` maakt een element `afgewezen`; `verwerkt` legt een keuze vast die de AI in de beoordeling heeft doorgevoerd. Het ja op opnemen is geen besluit maar het AKKOORD, dat de redenen om voor te leggen (`beslist.open`) afsluit.

In een onderwerp:

```yaml
besluiten:
  - datum: 2026-10-07
    besluit: Afbakening Burgerzaken: …
  - datum: 2026-09-30
    begrip: Uitdaagrecht            # alleen bij een begrip zonder beoordeling
    besluit: Geen eigen pagina: …
```

Een besluittekst noemt een regel of een sectie van ARCHITECTURE.md bij naam (regel Thuishoren, ARCHITECTURE.md *Processen en ketens*), nooit een bestandspad: een herstructurering van de wiki mag het model en zijn akkoord niet raken. *(script: de vorm van een besluit van een onderwerp, een besluit over een begrip dat een beoordeling heeft, een bestandspad in een besluit of stand)*

## Wat je vastlegt

Toets: zou een nieuwe Sessie met alleen de bronnen, het kennismodel en de beoordeling de vraag opnieuw stellen, of een ander antwoord kiezen? Dan leg je het vast, kort: de keuze, de reden en het afgewezen alternatief.

| Vastleggen | Niet vastleggen (waar het wel staat) |
|---|---|
| Een keuze tussen verdedigbare alternatieven die niet uit de beslistabel, een regel of een bron volgt | Het ja op opnemen (het AKKOORD in `log.md`) |
| Een afgewezen alternatief dat voor de hand ligt | Wat zonder alternatief in de beoordeling staat: naam, type, relatie, tekst |
| Een afwijking van een regel, de beslistabel, een bron, GGM of GEMMA | De toepassing van een regel of precedent (de regel) |
| Domeinkennis van de redacteur die in geen bron staat | Uitstel of een open punt (todo of `vragen:`); een terugmelding (het register) |
| Een afbakening: wat buiten het onderwerp of het model valt | Een herzien besluit (Git) |
| Een afwijzing, met de reden | Een besluit dat in meer onderwerpen geldt: één keer, als regel (Een besluit over de werkwijze) |

Een besluit is nooit een bron in de inhoud: een kenmerk of beschrijving noemt de bron of regel waarop het besluit steunt.

## Zekerheid

`kennis`: domeinkennis van de redacteur of een bron; geldt als regel en precedent. `logica`: afgeleid uit regels en samenhang; een uitgangspunt, opnieuw voorleggen als nieuwe informatie de redenering raakt. `indruk`: voorlopig; in Sessie 3 van hetzelfde onderwerp opnieuw aanbieden, geen precedent. Zonder veld: `logica`. De AI stelt het niveau voor, de redacteur bevestigt; `kennis` zet de AI nooit zelf. Een bevestiging die de zekerheid verhoogt, vervangt het besluit.

## Wat al besloten is

Lees vóór het beoordelen de `besluiten:` van het onderwerp en van de beoordelingen die je bijwerkt; de begrippenlijst van een onderwerp toont de besluiten over het onderwerp. Of je het opnieuw vraagt, hangt af van de zekerheid (regel Navragen). Past een besluit niet meer bij de criteria, leg het dan opnieuw voor, met de reden. Het nieuwe besluit vervangt het oude en noemt wat het herziet.

## Een besluit over de werkwijze

Een besluit over de werkwijze of de criteria, of een besluit dat in meer onderwerpen geldt, verwerk je waar het geldt, met de onderbouwing: de werkwijze in `AGENTS.md`, de modellering in het kennismodel (`kennismodel/modelleerregels.md` of `tools/kennismodel.py`), het waarom in `ARCHITECTURE.md`, de stappen in de skill. Zonder datum en zonder register: Git bewaart de geschiedenis.

Een precedent wordt pas een regel na voorleggen: na drie gelijke gevallen legt de AI een voorstel voor een regel voor; na akkoord komt de regel in het kennismodel. Zonder akkoord blijft het een toepassing per geval (regel Per geval).
