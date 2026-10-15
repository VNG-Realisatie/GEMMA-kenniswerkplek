# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md) is goedgekeurd (2026-10-15). Drie delen: de ArchiMate-matrix als eerste keuze met lichtere kenmerken (deel 1), data-object als element (deel 2), Capability, eerst samen bepalen (deel 3).
- Stap 1 en 2 zijn gedaan. Besluiten van de redacteur staan in het plan: *aard* heet hoofdkenmerk; de naam blijft Capability; de technologielaag is een laag in de matrix; O2 (poort als uitzondering) en O3 (kenmerken uit relaties) zijn aangenomen, zie *Uitkomst stap 2*.
- Nog niets aan de scripts, het schema of de beoordelingen gewijzigd.

## Volgende klus

Stap 3–7 van het plan: schema en `tools/bepaal_type.py` (keuzevelden `vak`, `hoofdkenmerk`, `soort_gedrag`; poort als uitzondering; kenmerken uit relaties; standaardwaarden; consistentieregel), het kennismodel, de omzetting van alle 481 beoordelingen met een script (de uitkomsten, pagina's en export blijven gelijk), skills en uitleg, commit. Verschillen tussen kenmerk en relatie bij de omzetting per geval voorleggen.

## Modeladvies

Denkniveau hoog voor stap 3 (ontwerp in de code), middel voor stap 4–6. Begin een nieuwe Sessie met een sterk model of hoge redeneerinspanning: de omzetting raakt alle beoordelingen en moet de uitkomsten gelijk houden.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en plannen/2026-10-15-archimate-indeling.md (goedgekeurd; stap 1 en 2 gedaan, besluiten in Uitkomst stap 2). Voer stap 3–7 uit (deel 1): schema en tools/bepaal_type.py met de keuzevelden vak, hoofdkenmerk en soort_gedrag, poort als uitzondering (O2), kenmerken afgeleid uit relaties (O3), standaardwaarden (O4) en de consistentieregel; dan het kennismodel; dan de omzetting van alle beoordelingen met een script in de scratchpad, met tools/beslissen.py vóór en na: beslist, elementpaginas/ en archimate_export.py --check blijven gelijk. Een verschil tussen kenmerk en relatie leg je per geval voor. Werk daarna skills, AGENTS.md en ARCHITECTURE.md bij en commit met prefix rules.
```
