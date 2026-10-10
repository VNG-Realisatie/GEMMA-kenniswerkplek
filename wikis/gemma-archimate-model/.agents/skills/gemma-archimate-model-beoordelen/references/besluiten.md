# Besluiten: voorleggen en vastleggen

## Voorleggen

Leg na `uv run python tools/beslissen.py` per begrip met open redenen (`beslist.open`, ook in `ter-beoordeling.md`) de vraag voor in de chat, één voor één. Voor te leggen is wat een keuze van de redacteur vraagt: een element met open redenen, een open vraag, twijfel over een kenmerk, een nieuw element of een afwijking van een eerder besluit.

- Context: welk begrip, wat de beslistabel zegt, met de bronpassage.
- Argumenten voor en tegen, en een advies.
- In eenvoudige taal, met een concreet voorbeeld uit het model; per optie wat er gebeurt.

Niet los voorleggen: een begrip zonder pagina waarvan de uitkomst eenduidig uit de beslistabel of een eerdere afbakening volgt (buiten scope, geen element zonder twijfel). Noem die samen in de samenvatting van stap 6 van skill gemma-archimate-model-update. Ook zonder voorleggen, met een vermelding in de samenvatting ter bevestiging: een thuisonderwerp dat eenduidig uit de inhoud volgt (regel Thuishoren) en een landelijke grondslag die eenduidig in de nagelezen wettekst staat (regel Wettelijke grondslag).

## Vastleggen

Een besluit staat bij waar het over gaat; er is geen register en geen apart overzicht.

- **Over één begrip:** in `besluiten:` van zijn beoordeling.
- **Over een onderwerp als geheel** (afbakening, indeling, afronding): in `besluiten:` van het onderwerp (`beoordelingen/onderwerpen/<onderwerp>.yaml`).
- **Over een begrip zonder beoordeling:** voorlopig in `besluiten:` van het onderwerp, met `begrip`; krijgt het begrip een beoordeling, dan verhuist het besluit letterlijk daarheen (regel Letterlijk verplaatsen).

In een beoordeling:

```yaml
besluiten:
  - datum: 2026-10-01
    besluit: Opnemen als gegevensobject zonder GGM-entiteit; terugmelding 3.
    gevolg: opnemen                 # opnemen | afwijzen | verwerkt
    redenen: [gegevensobject zonder sterke GGM-match]   # letterlijk uit beslist.voor_te_leggen
    stand: herzien door <datum> (…)      # alleen bij een besluit dat later herzien is of nog open staat
```

`opnemen` met de gedekte redenen maakt een kandidaat `review`; `afwijzen` maakt hem `afgewezen`; `verwerkt` legt een besluit vast dat de AI in de beoordeling heeft doorgevoerd (bijvoorbeeld een naamkeuze). Daarna weer `tools/beslissen.py`.

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

## Wat al besloten is

Lees vóór het beoordelen de `besluiten:` van het onderwerp en van de beoordelingen die je bijwerkt; de begrippenlijst van een onderwerp toont de besluiten over het onderwerp. Wat daar staat, vraag je niet opnieuw (regel Navragen). Een besluit dat niet meer past bij de criteria, leg je wel opnieuw voor, met de reden; het nieuwe besluit komt erbij, het oude blijft staan.

## Een besluit over de werkwijze

Een besluit over de werkwijze of de criteria (niet over één begrip of onderwerp) verwerk je waar het geldt: de werkwijze in `AGENTS.md`, de modellering in het kennismodel (`kennismodel/modelleerregels.md` of `tools/kennismodel.py`), het waarom in `ARCHITECTURE.md`, de stappen in de skill. Zonder datum, zonder verwijzing naar het besluit en zonder register: de regel zegt wat nu geldt, Git bewaart de geschiedenis.
