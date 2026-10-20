# Plan: wijzigingsgerichte werkplek- en validatiechecks

Status: voorstel ter besluitvorming; nog niet uitgevoerd.

## 1 Doel en afbakening

Verminder onnodige werkplekcontroles en repo-brede validaties door de check te kiezen op basis van de werkplekstatus en het geraakte invariant. Behoud volledige controles waar een wijziging of workflow die nodig maakt.

Dit plan staat los van het inhoudelijke voorstel [Onderwerpen sneller en lichter beoordelen](2026-10-20-relaties-en-targets-lichter-beoordelen.md). Een besluit over validatiebeleid keurt geen wijziging van relatie- of modelleerregels goed, en omgekeerd.

## 2 Huidige situatie

- De rootregel schrijft `workspace-check` voor bij de eerste vraag van iedere sessie, ook bij read-only vragen of planwijzigingen. `README.md` herhaalt deze instructie.
- `workspace-check` zonder `--fix` controleert de werkplek read-only. De status `ok` blijft relevant zolang checkout, Python-omgeving en harness-configuratie niet zijn veranderd.
- `workspace-check --fix` kan harness-bindingen synchroniseren en oude afgeronde runs opruimen. Dat is meer dan alleen een controle en kan dus neveneffecten hebben.
- `llmwiki lint` heeft geen bestand- of wiki-argument. Het controleert repo-breed onder meer skills, afhankelijkheden, harde Markdown-regelovergangen en woordbudgetten. Een wijziging van één planbestand vraagt niet automatisch al die controles.
- `llmwiki ontvouw <bestand>` kan de Markdown-regelovergangen in een specifiek bestand controleren zonder wijzigingen aan te brengen. Specifieke tests of toolchecks zijn passender voor andere wijzigingen.
- Een eerdere plan-only wijziging riep volledige lint aan. Dat testte de repo-brede Markdown-regel, maar controleerde niet de inhoudelijke juistheid van het plan.

## 3 Voorgestelde werkwijze

1. Draai `workspace-check` bij een nieuwe of gewijzigde checkout, na setup of wijzigingen aan Python-/harness-configuratie, bij een gemeld workspaceprobleem, of vóór een workflow die een door de check gedekte integratie nodig heeft.
2. Herhaal de check niet binnen dezelfde ongewijzigde werkplek nadat de status `ok` is. Een nieuwe chat op dezelfde checkout is op zichzelf geen wijziging. Onderzoek hoe de status voor volgende sessies licht en betrouwbaar kan worden vastgesteld; zonder betrouwbare statusmarker geldt de check bij een nieuwe checkout of gewijzigde omgeving opnieuw.
3. Kies na een wijziging de kleinste check die het geraakte invariant controleert. Voor een Markdownbestand kan `llmwiki ontvouw <bestand>` volstaan voor de regelovergangsregel; voor Python draaien de relevante tests; voor skillmetadata, afhankelijkheden, gedeelde-skillgrenzen of woordbudgetten kan volledige lint nodig zijn.
4. Gebruik volledige `llmwiki lint` voor repo-brede wijzigingen, wijzigingen aan lintregels, skills of afhankelijkheden, of wanneer gewijzigde bestanden repositorybrede invarianten raken. Behoud lint als expliciete eindcontrole waar een workflow haar voorschrijft.
5. Voer bij een planbestand geen volledige lint uit alleen omdat het bestand is toegevoegd. Voer geen test uit die geen relatie heeft met het gewijzigde invariant. Inhoudelijke review blijft nodig en wordt niet vervangen door lint.
6. Houd `--fix` opt-in. Meld herstelbare bevindingen en vraag toestemming voordat herstel wordt uitgevoerd. Maak zo mogelijk het opruimen van oude afgeronde runs een afzonderlijke actie, zodat harness-herstel niet onverwacht ook runbestanden opruimt.

## 4 Verwachte winst

| Onderdeel | Verwachte winst | Zekerheid en afbakening |
|---|---|---|
| Voorwaardelijke workspace-check | Vermijdt een check bij nieuwe sessies op dezelfde ongewijzigde checkout; bespaart vooral uitvoeringstijd en meldingsruis. | Hoge zekerheid dat het aantal aanroepen daalt; absolute tijdswinst onbekend en waarschijnlijk klein per sessie. Setup- en integratierisico's blijven afgedekt door de triggers. |
| Wijzigingsgerichte validatie | Vermijdt repo-brede scans wanneer alleen een lokaal invariant geraakt is; een plan-only wijziging kan beperkt blijven tot een bestandscheck of geen executable check vragen. | Middelmatige zekerheid voor minder uitvoertijd en output. Geen betrouwbare procentuele schatting van totale sessie-invoer; minder irrelevante output en beter aantoonbare validatie zijn de belangrijkste winst. |
| Aparte opruimactie | Voorkomt dat harness-herstel tegelijk oude runbestanden opruimt en maakt toestemming gerichter. | Lage zekerheid voor tijdwinst; vooral voorspelbaarheid en minder risico op verrassende neveneffecten. |

Meet over enkele werkitems het aantal checks, hun duur en outputvolume, uitgesplitst naar wijzigingstype. Tel deze winst niet op bij de winstinschattingen uit het inhoudelijke plan.

## 5 Regels en bestanden die moeten veranderen

| Regel of instructie nu | Voorgestelde wijziging | Waar aanpassen |
|---|---|---|
| `workspace-check` bij de eerste vraag van elke sessie, zonder onderscheid naar checkout of taak. | Maak de check afhankelijk van checkout-/setupwijziging, workspaceprobleem of benodigde integratie; een `ok`-status blijft geldig zolang de relevante omgeving gelijk blijft. Definieer hoe die status tussen sessies wordt vastgesteld. | Root `AGENTS.md`, sectie Werkplek eerst; `README.md`, sectie Werkplekcontrole. |
| `workspace-check --fix` kan zowel harness-koppelingen herstellen als oude afgeronde runs opruimen. | Benoem het neveneffect expliciet en maak run-prune bij voorkeur apart aanroepbaar. Houd beide herstelacties opt-in en behoud onafgeronde runs. | Root `AGENTS.md`, regel over run-state; `tools/llmwiki/workspace_check.py`; `tools/llmwiki/runs.py`; `docs/onderbouwing.md`, sectie Workspace-check. |
| Er is geen algemene wijzigingsgerichte validatiematrix. | Leg vast dat de kleinste toepasselijke check wordt gekozen en dat volledige lint geen standaard post-change stap is; specifieke workflowcontroles blijven gelden. | Root `AGENTS.md`, secties Schrijfwijze en Grenzen; eventueel de rationale in `docs/onderbouwing.md`. |
| `wiki-intake` gebruikt repo-brede lint voor de regelovergangen in één index. | Vervang dit onderdeel door `llmwiki ontvouw <index-pad>`; behoud de steekproef op regelnummers en de controle van de woordlimiet. | `.agents/skills/wiki-intake/SKILL.md`. |

## 6 Uitvoering en acceptatie

1. Leg de voorwaardelijke triggers voor `workspace-check` en de wijzigingsgerichte validatiematrix afzonderlijk voor aan de redacteur.
2. Pas root-`AGENTS.md` en `README.md` gelijktijdig aan, zodat de eerste-vraagregel niet op één plek onvoorwaardelijk blijft staan.
3. Pas de rationale en `wiki-intake` aan; controleer of andere skills een repo-brede controle voorschrijven voor een lokaal invariant.
4. Als `--fix` runbestanden blijft opruimen, documenteer dit expliciet. Als prune wordt losgekoppeld, voeg tests toe voor oude afgeronde runs en behoud van onafgeronde runs.
5. Proef de validatiematrix op drie gevallen: alleen een plan/Markdownbestand, een skillwijziging en een wijziging aan Python-tools. Vergelijk de gekozen check, duur en output met de huidige routine.

Acceptatiecriteria:

- Een ongewijzigde checkout vraagt geen herhaalde workspace-check alleen omdat een nieuwe sessie begint.
- Wijzigingen hebben een benoemd geraakt invariant en een passende check, of een expliciete reden waarom geen executable check nodig is.
- Skillmetadata, afhankelijkheden, repositorygrenzen en de eindcontroles van workflows behouden volledige validatie.
- `--fix` heeft voorspelbare, gedocumenteerde neveneffecten en verwijdert nooit onafgeronde runs.
- De proef bevestigt minder onnodige checks zonder regressie in gevonden fouten.
