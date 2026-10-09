# Besluiten: voorleggen en vastleggen

## Voorleggen

Leg na `uv run python tools/beslissen.py` per begrip met open redenen (`beslist.open`, ook in `ter-beoordeling.md`) de vraag voor in de chat, één voor één. Voor te leggen is wat een keuze van de redacteur vraagt: een element met open redenen, een open vraag, twijfel over een kenmerk, een nieuw element of een afwijking van een eerder besluit.

- Context: welk begrip, wat de beslistabel zegt.
- Argumenten voor en tegen, en een advies.
- In eenvoudige taal, met een concreet voorbeeld uit het model; per optie wat er gebeurt.

Niet los voorleggen: een begrip zonder pagina waarvan de uitkomst eenduidig uit de beslistabel of een eerdere afbakening volgt (buiten scope, geen element zonder twijfel). Noem die samen in de samenvatting van stap 6 van skill gemma-archimate-model-update (besluit redacteur 2026-10-01). Ook zonder voorleggen, met een vermelding in de samenvatting ter bevestiging: een thuisonderwerp dat eenduidig uit de inhoud volgt (regel Thuishoren) en een landelijke grondslag die eenduidig in de nagelezen wettekst staat (regel Wettelijke grondslag).

## Vastleggen

Het antwoord komt in `besluiten:` van de beoordeling:

```yaml
besluiten:
  - datum: 2026-10-01
    besluit: Opnemen als gegevensobject zonder GGM-entiteit; terugmelding 3.
    gevolg: opnemen                 # opnemen | afwijzen | verwerkt
    redenen: [gegevensobject zonder sterke GGM-match]   # letterlijk uit beslist.voor_te_leggen
```

`opnemen` met de gedekte redenen maakt een kandidaat `review`; `afwijzen` maakt hem `afgewezen`; `verwerkt` legt een besluit vast dat de AI in de beoordeling heeft doorgevoerd (bijvoorbeeld een naamkeuze). Daarna weer `tools/beslissen.py`.

## Wat al besloten is

`besluiten/per-begrip.md` toont alle besluiten uit de beoordelingen en de eerdere besluiten uit `beoordelingen/besluiten-eerder.yaml`. Wat daar staat, vraag je niet opnieuw (regel Navragen). Een besluit dat niet meer past bij de criteria, leg je wel opnieuw voor, met de reden.

## Een algemeen besluit verwerken

Een besluit over de werkwijze of de criteria (niet over één begrip) verwerk je in `AGENTS.md` (werkwijze), in het kennismodel (`kennismodel/modelleerregels.md` of `tools/kennismodel.py`) of in de skill waar het hoort: daar staat wat nu geldt. Daarnaast komt het, met de datum en de kolom Stand, in `besluiten/werkwijze.md` of in de besluitentabel van het document in `docs/` waar het bij hoort. Wordt een eerder besluit herzien, zet dan bij het oude besluit "herzien door <datum>".
