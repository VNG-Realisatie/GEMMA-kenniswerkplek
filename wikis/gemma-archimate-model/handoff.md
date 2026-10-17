# Handoff

Overdracht naar de volgende Sessie (2026-10-17). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md): deel 1 en 2 uitgevoerd; van deel 3 zijn stap 12 (besluiten K1–K8) en stap 13 (vastleggen) klaar, zie *Uitkomst stap 12* en *Uitkomst stap 13*.
- Commit 487489b: het kennismodel een vijfde korter (relaties alleen bij het brontype, eigenschappen en vaste namen in de README, *Buiten het kennismodel* als naslag in `elementpaginas/overig/`).
- Commit van stap 13: Capability staat in het kennismodel (laag Strategie, vak `strategie/gedrag`, hoofdkenmerk *vermogen*, kenmerken *beoordeelbaar* en *onderscheidend*, Capabilitykaart, paginatype `capability` in `wiki.yaml`), in de ArchiMate-toets (`tools/relaties.py`) en in ARCHITECTURE.md. Er is nog geen capability beoordeeld.

## Volgende klus

Stap 14, zoals deel 2 werd gebouwd:

1. Scripts (denkniveau middel): de toets op ten minste twee realiserende functies (K3: *gerealiseerd door* met minder dan twee functies in `naar` is geen element, voorleggen), de grondslag via de realiserende functies in de signalen, het sjabloon en de render van de elementpagina, de Capabilitykaart in de indelingspagina's, en de export (`Strategy / wiki-gemma-model`, map Capabilitykaart). Tests.
2. Skills: in `gemma-archimate-model-criteria` en `-beoordelen` hoe de AI een capability afleidt uit de functies en diensten van een onderwerp (K1), met de bronnen (K6) en de GEMMA-match (K7). Let op het woordbudget van de skills.
3. Afleiden (denkniveau hoog): de kandidaten uit de kalibratie (Personen registreren, Identiteit vaststellen, Lijkbezorging waarborgen; niet Verkiezingen organiseren en Nationaliteit verlenen), één tabel voorleggen, AKKOORD. De terugmelding aan het GEMMA-team over de ontbrekende capabilitykaart van de bedrijfslaag (K7).

## Modeladvies

Stap 14 begint met scriptwerk (middel); het afleiden en voorleggen van de capabilities vraagt denkniveau hoog. Begin een nieuwe Sessie: bouwen is een andere fase, en deze Sessie heeft een volle context.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en plannen/2026-10-15-archimate-indeling.md (Uitkomst stap 12 en 13). Voer stap 14 uit: bouw de capability zoals deel 2 het data-object bouwde (toets op ten minste twee realiserende functies, signalen, render, Capabilitykaart, export, tests, skills), en leid daarna de capabilities af uit de functies van burgerzaken en lijkbezorging; leg ze in één tabel voor. Het kennismodel en de kenmerken staan vast; wijzig ze alleen na voorleggen. Houd je aan de woordbudgetten in wiki.yaml.
```
