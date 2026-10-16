# Handoff

Overdracht naar de volgende Sessie (2026-10-16). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md): deel 1 en 2 zijn uitgevoerd. De besluiten staan in *Uitkomst stap 3–7* en *Uitkomst stap 8–11*.
- Commit `rules:` (33056c4): het data-object is een element dat `tools/beslissen.py` afleidt uit de GGM-match (`<naam>-data`). Het kenmerk *geautomatiseerd verwerkt* vervalt, het registr*-signaal geldt niet meer bij een bedrijfsobject, en de modelleerregels zijn puntsgewijs (2.217 woorden).
- Commit `add:`: drie extra data-objecten bij Ingeschreven persoon (Gezag-data, Nationaliteit-data, Verblijfstitel-data) en een nieuw AKKOORD voor de 285 elementen. Er zijn nu 21 data-objecten; de export heeft 21 realisaties meer en is verder gelijk.
- Todo: de GGM-match voor rollen, actoren en gebeurtenissen kiezen bij de volgende herbeoordeling. Een match geeft vanzelf een data-object.

## Volgende klus

Deel 3 van het plan: Capability, eerst als bespreking (stap 12). Het is een voorstel zonder code: de definitie en het vak, de criteria als kenmerken, de kernrelatie Bedrijfsfunctie ─realisatie→ Capability, naamvorm, indeling, bron en GEMMA-match, en een kalibratie op de 26 GEMMA-capabilities en 10 à 20 diensten.

## Modeladvies

Deel 3 vraagt denkniveau hoog: oordelen en afwegen in samenhang, met het kader van de redacteur. Begin een nieuwe Sessie met een sterk model of hoge redeneerinspanning; de context van deze Sessie is vol.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en plannen/2026-10-15-archimate-indeling.md (deel 1 en 2 uitgevoerd, zie Uitkomst stap 3–7 en 8–11). Voer deel 3 stap 12 uit: een voorstel ter bespreking over Capability, zonder code, met het kader van de redacteur in het plan. Leg de keuzes met context en gevolgen per optie voor, en leg de besluiten vast in het plan voordat je bouwt.
```
