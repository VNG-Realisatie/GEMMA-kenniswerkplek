---
name: wiki-curatie-update
description: Werk een curatie-wiki bij op basis van bronnen — bronnen en bronanalyse, per begrip een beoordeling (het oordeel van de AI), beslissen en renderen door scripts, voorleggen in de chat, en goedkeuren na het woord AKKOORD van de redacteur. Gebruik wanneer de gebruiker vraagt een curatie-wiki bij te werken of een bron te verwerken.
metadata:
  kind: workflow
  scope: core
  requires-skills: "wiki-ingest wiki-intake"
  requires-tools: "llmwiki"
---

# Workflow wiki-curatie-update

Voor een **curatie**-wiki (`wiki.yaml` `type: curation`) met beoordelingen (`curation.beoordelingen`). Werkmap: de wiki-directory (bevat `wiki.yaml`). Een wiki-workflow vult de stappen in met eigen skills en scripts.

## Uitgangspunt: zacht oordeel, harde vorm

- **De AI** schrijft alleen het oordeel per begrip, in een beoordeling (YAML) in de map `curation.beoordelingen`.
- **Scripts van de wiki** leiden daaruit af wat vast kan (`curation.beslissen`: type, status, letterlijke modelgegevens, harde controles) en maken alle leesbare pagina's en overzichten (`curation.render`). Pagina's worden nooit met de hand bewerkt; de pre-commit-controle `llmwiki precommit render-check` vangt dat.
- **De redacteur** beoordeelt de gerenderde pagina's en overzichten (preview en Source Control) en geeft akkoord met het woord AKKOORD in de chat.

Er is geen run en geen kladblok: alles staat in de werkboom en is te zien in Git. Hervatten = `git status` en het overzicht van wat wacht op akkoord lezen.

## Stappen

| # | Stap | Wie | Denkniveau | Hoe |
|---|---|---|---|---|
| 1 | Onderwerp | AI met redacteur | middel | Werk altijd vanuit één onderwerp; de wiki-workflow zegt waar het staat |
| 2 | Bronnen en bronanalyse | AI | middel | `wiki-ingest` (laag 1 en 2, en de domein-lens); kernpunten bespreken met de redacteur |
| 3 | Beoordelen | AI | hoog | De beoordelen-skill van de wiki: per begrip een beoordeling. Lees eerst de besluiten die de redacteur al nam |
| 4 | Beslissen en renderen | script | hoog | Het beslis-script van de wiki (`curation.beslissen`). Een fout los je op in de beoordeling; een waarschuwing beoordeel je inhoudelijk |
| 5 | Voorleggen | AI → redacteur | hoog | Wat het beslis-script als open markeert, één vraag tegelijk in de chat: context, argumenten voor en tegen, advies. Het antwoord komt als besluit in de beoordeling; daarna stap 4 |
| 6 | Bekijken | redacteur | laag | `llmwiki promote plan [--onderwerp <id>]`; toon de samenvatting in de chat. De redacteur leest de pagina's en de wijzigingen in Source Control |
| 7 | Akkoord | redacteur | laag | De redacteur typt letterlijk AKKOORD. "Prima" of "ziet er goed uit" is geen akkoord; vraag dan opnieuw |
| 8 | Vastleggen | script | laag | `llmwiki promote apply --akkoord-woord AKKOORD`. Het harness vraagt de redacteur om een klik; omzeil die niet |
| 9 | Commit | redacteur of AI | laag | Beoordelingen, pagina's en `log.md` samen |

Het denkniveau en wat het Model bij een overgang doet, staan in `AGENTS.md` (Werkwijze). Stap 3 tot en met 5 zijn één lus en houden hetzelfde niveau; zo wisselt het niveau twee keer per update: na de bronanalyse omhoog, na het voorleggen omlaag.

`llmwiki promote apply` weigert als er na de samenvatting iets is gewijzigd; maak dan een nieuw plan. Het zet de status `goedgekeurd` en schrijft per element een regel in `log.md` met de hash van de inhoud van de beoordeling. Een inhoudelijke wijziging maakt een goedgekeurd element via het beslis-script weer `review`; een andere opmaak of een bijgewerkt model niet.

## Een onderwerp in één keer afronden

- Rond een onderwerp zoveel mogelijk in één keer af voordat je aan een volgend begint: elk begrip beoordeeld, elke vraag beslist, elke ontbrekende bron opgenomen. Opnieuw opstarten kost het opnieuw inlezen van bronnen, besluiten en samenhang, en geparkeerde punten raken uit beeld of worden later zonder de oorspronkelijke afweging opgepakt.
- Een open punt binnen de scope van het onderwerp los je meteen op, niet als todo: ontbreekt bijvoorbeeld de wet die grondslag is van een product, haal haar dan op als bron en beoordeel of ze een beleidskader wordt (een wet die alleen een tarief of een andere regel buiten de gemeentelijke taak bevat, is geen grondslag).
- Past een onderwerp niet in één Sessie, verdeel het dan in plakken naar samenhang (een kernobject of proces). Elke plak wordt volledig afgerond (akkoord, vastleggen, commit) en de plakken volgen direct op elkaar; wat voor een volgende plak blijft, staat onder het onderwerp in de todo van de wiki en in de startprompt van die plak, en verdwijnt uit de todo zodra die plak is afgerond.
- Een todo is alleen voor wat binnen het onderwerp niet kan: een begrip dat thuishoort in een onderwerp dat nog niet bestaat (een verwijzing), of een voorstel aan of besluit van een andere partij.

## Grenzen

- Nooit zelf een status zetten of AKKOORD typen; nooit `promote apply` zonder dat de redacteur letterlijk AKKOORD typte.
- Nooit een gegenereerde pagina met de hand wijzigen; wijzig de beoordeling en draai het beslis-script.
- Zet geen automatische goedkeuring aan in een sessie waarin wordt goedgekeurd.

## Wat een wiki levert

Een curatie-wiki die deze workflow volgt, heeft in `wiki.yaml` `curation.beoordelingen` (map), `curation.beslissen` en `curation.render` (scripts die `--wiki <map>` accepteren; render ook `--check`), `curation.approval: chat`, een schema voor de beoordeling, en een eigen workflow- en beoordelen-skill.
