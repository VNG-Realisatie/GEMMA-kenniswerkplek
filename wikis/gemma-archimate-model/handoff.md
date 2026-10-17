# Handoff

Overdracht naar de volgende Sessie (2026-10-17). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md): deel 1 en 2 zijn uitgevoerd (Uitkomst stap 3–7 en 8–11). Van deel 3 is stap 12 klaar: het voorstel over Capability staat in *Voorstel stap 12*, met de kalibratie op de 26 GEMMA-capabilities en 22 diensten, en de besluiten K1–K8 in *Uitkomst stap 12*.
- Er is nog niets gebouwd: geen code, geen kennismodel, geen beoordelingen.
- De kern van de besluiten: een capability is een beoordeling van de AI, afgeleid uit functies. Vak `strategie/gedrag`, hoofdkenmerk *vermogen*. Alleen een bedrijfsfunctie realiseert haar, en ze is alleen een element als ten minste twee functies haar realiseren. De naam is object en werkwoord (Identiteit vaststellen), in een eigen Capabilitykaart naar het GEMMA-domein. Bronnen: die van de functies plus strategische VNG-bronnen. GEMMA is optioneel matchdoel, met één terugmelding. Het woordbudget van het kennismodel gaat naar 21.800.

## Volgende klus

Stap 13: de besluiten vastleggen in ARCHITECTURE.md en het kennismodel (`tools/kennismodel.py`: Capability van de elementtypen zonder element (motivatie) naar laag strategie; pagina's strategie; de kenmerken *beoordeelbaar* en *onderscheidend*; de aanscherping van *gegroepeerd gedrag* en *stabiel over tijd*; poortkenmerk 3 zonder "vermogen"; de Capabilitykaart in de indelingen; de uitzondering in regel Elke claim een bron; budget in `wiki.yaml`). Leg eerst het open punt voor: het brontype van VNG-impactanalyses, implementatieplannen en beleidsadviezen (nu `overig`, of `beleid`). Daarna stap 14: bouwen zoals in deel 2, de capabilities afleiden, voorleggen en AKKOORD.

## Modeladvies

Stap 13 vraagt denkniveau hoog voor de regeltekst en de kenmerken (ze werken door in alle beoordelingen), daarna middel voor de uitvoering in de scripts. Begin een nieuwe Sessie met een sterk model of hoge redeneerinspanning: deze Sessie was een bespreking, en het bouwen is een andere fase.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en plannen/2026-10-15-archimate-indeling.md (deel 1 en 2 uitgevoerd; deel 3 stap 12 besloten, zie Voorstel stap 12 en Uitkomst stap 12). Voer stap 13 uit: leg eerst het open punt over het brontype van VNG-impactanalyses voor, en leg dan de besluiten K1–K8 vast in ARCHITECTURE.md en het kennismodel (tools/kennismodel.py, bepaal_type.py voor de kenmerken, wiki.yaml voor het budget). Bouw nog geen capabilities (dat is stap 14). Houd je aan het woordbudget van 21.800 en leg elke tekst die de regels raakt eerst voor.
```
