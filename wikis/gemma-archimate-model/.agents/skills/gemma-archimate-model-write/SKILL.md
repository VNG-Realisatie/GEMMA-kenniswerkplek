---
name: gemma-archimate-model-write
description: WRITE-uitbreiding voor gemma-archimate-model — elementpagina's schrijven voor beoordeelde begrippen (naam, grondslag, GGM- en GEMMA-match, herkenbare en formele definitie, hiërarchie, relaties als links), de begrippenlijst bijwerken en GGM-terugmeldingen toevoegen, alles gestaged in de run. Gebruik binnen gemma-archimate-model-update, na ASSESS.
metadata:
  kind: capability
  scope: wiki
  requires-tools: "llmwiki python:tools/ggm.py python:tools/gemma.py python:tools/relaties.py python:tools/bepaal_type.py python:tools/terugmelding.py"
  reads: "assessment"
  writes: "changeset"
---

# WRITE-uitbreiding: elementen vastleggen

Werkt alleen voor begrippen die in ASSESS een uitkomst `element` kregen. Doet zelf geen beoordeling van het type. Alles wordt gestaged in `.work/runs/<run-id>/changeset/` en in `.work/runs/<run-id>/changeset-concept.json` (per pagina `pad`, `staged_bestand`, `actie`, `type`); niets gaat rechtstreeks in de werkboom.

## Stappen per element

1. **Plaats.** Het paginatype volgt uit de uitkomst. Pad: `bedrijfsarchitectuur/<map>/<taakveld>/<beleidsdomein>/<id>.md` voor bedrijfsobject, product, dienst, proces en functie; plat (`…/<map>/<id>.md`) voor gebeurtenis, actor en rol. Mapnamen zijn de naam in kleine letters met koppeltekens (`8 Volkshuisvesting` → `8-volkshuisvesting`).
2. **Naam** — `references/naamgeving.md`.
3. **Grondslag** — `references/grondslag.md`.
4. **GGM-match** — `references/ggm-match.md`. De `ggm_*`-velden neem je letterlijk over uit `uv run python tools/ggm.py velden <guid>`; nooit zelf invullen of verbeteren.
5. **GEMMA-match** — `references/gemma-match.md`. De `gemma_*`-velden letterlijk uit `tools/gemma.py velden <id>`.
6. **Definities** — `references/definitie.md` (herkenbaar, en alleen bij wezenlijk verschil ook formeel).
7. **Hiërarchie** — `references/hierarchie.md` (generalisatie, specialisaties, GGM-componenten).
8. **Relaties** — `references/relaties.md`; kandidaten uit het GGM en uit de bronnen samen: `uv run python tools/relaties.py voorstel <id> --bronnen <assessment.json> --markdown`. Een relatie staat alleen op de pagina van het bronelement; kolom `Bron` met bron-id en vindplaats.
9. **Tegenhanger** — `references/tegenhangers.md`, als de uitkomst een tegenhanger noemt.
10. **Pagina** — opbouw volgens `references/secties.md`; frontmatter volgens het schema van het paginatype (`schemas/<type>.schema.json`). In de frontmatter staan geen verwijzingen naar andere pagina's; die staan als relatieve links in de body.
11. **Status.** `uv run python tools/bepaal_type.py status --uitkomst <uitkomst.json> --ggm-match <sterkte> --grondslag <grondslag>` geeft `review` of `kandidaat`. Bij `kandidaat`: sectie `## Ter discussie` met wat de redacteur moet beslissen. Zet nooit `goedgekeurd`.

## Daarna, voor het hele onderwerp

12. **Begrippenlijst.** Werk `begrippen/<onderwerp>.md` bij (ook gestaged): één rij per beoordeeld begrip in `## Begrippen` — `| Begrip | Uitkomst | Reden | Herkomst | GGM |` —, met een link naar de elementpagina als die er is, anders platte tekst. Herkomst = het brontype van de hoogst gerangschikte bron.
13. **GGM-terugmeldingen**, ná het schrijven van de elementen, per bevinding: `uv run python tools/terugmelding.py add --run <run-id> --type <type> --domein <beleidsdomein> --entiteit <GGM-naam> --bevinding "<tekst>" --element <id>`. Typen: `definitie` (GGM wijkt af van wet of bronnen), `hiaat` (data-object zonder GGM-entiteit, conservatief), `duplicaat`, `homoniem`, `structuur`, `scope`, `relatie` (alleen fouten in exact gematchte relaties; nieuwe relaties worden niet teruggemeld). Verwijs op de elementpagina naar de terugmelding.
14. Rond af: `uv run python -m llmwiki run complete write --run <run-id> --data .work/runs/<run-id>/changeset-concept.json`.

## Regels bij het schrijven

- Elke claim met bron ([IH1]); tegenspraak markeren met `⚠️ Tegenspraak` ([IH3]); zonder bron `🔍 Verificatie nodig` ([IH4]).
- Geen verwijzingen naar `AGENTS.md`, `ARCHITECTURE.md`, skills, `tools/` of `schemas/` in pagina's ([WC7]).
- Geen absolute taal zonder concrete reden ([WC8]–[WC11]); geen registr*-argumenten ([EL1]).
- Citaten als blockquote met vindplaats; citaten zijn platte tekst.
