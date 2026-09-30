---
name: wiki-intake
description: Maak of vul de technische index van een bron (laag 2, sources/index/<bron-id>.md) — samenvatting, trefwoorden, begrippen en inhoudsopgave met regelnummers — zodat een Agent snel de juiste bron en passage vindt zonder de hele tekst te lezen. Gebruik direct na llmwiki source add, of om een bestaande lege index te vullen.
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "sources/raw/<bron-id>.md"
  writes: "sources/index/<bron-id>.md"
---

# Skill wiki-intake

Doel: laag 2 van de bronnen vullen. De index is een **technisch hulpmiddel om context te sparen**: een Agent leest eerst de index (enkele honderden woorden) om te kiezen welke bron en welke passage ertoe doet, en leest daarna alleen die regels in laag 1. De index is **geen schakel in de herleidbaarheid**: pagina's verwijzen via de domein-lens (laag 3) rechtstreeks naar de tekst in `sources/raw/`, nooit naar de index. Waarom de index deze inhoud heeft: `docs/onderbouwing.md` 5.19.

## Stappen

1. De bron staat in laag 1 en heeft een index (`llmwiki source add`, zie `wiki-ingest`). Lees de frontmatter van `sources/index/<bron-id>.md`; wijzig `id`, `pad`, `hash` en `opgehaald` nooit.
2. **Conversie controleren.** Open `sources/raw/<bron-id>.md` op drie plaatsen (begin, midden, eind) en kijk of koppen, tabellen en opsommingen heel zijn. Meld problemen aan de gebruiker; herschrijf de conversie niet (laag 1 is onveranderlijk).
3. **Inhoudsopgave (gereedschap).** `llmwiki source add` zet `## Inhoud` al, met niveau 3. Ontbreekt de sectie, of is ze te lang of te grof, draai dan `llmwiki source inhoud <bron-id> --schrijf --niveau <n>`. Kies `n` zo dat de tabel hooguit ongeveer 60 rijen heeft: bij een wet meestal de hoofdstukken en paragrafen, niet elk artikel. Heeft de tekst geen koppen, dan zegt de sectie dat; vul dan in stap 4 de begrippen en trefwoorden extra zorgvuldig met regelnummers.
4. **Tekstsecties (Model)**, vóór `## Inhoud`, volgens het sjabloon hieronder. Ze vervangen de regel "Index nog niet gevuld" of "Nog geen samenvatting.". Lees daarvoor de tekst; bij een lange tekst per hoofdstuk uit de inhoudsopgave. Regelnummers haal je uit laag 1 (zoek de passage op), nooit geschat.
5. Controleer: de index heeft geen harde regelovergangen binnen alinea's (`llmwiki lint`), elk regelnummer wijst naar de genoemde passage (steekproef van drie), en de tekstsecties samen zijn hooguit 400 woorden.

## Sjabloon

```markdown
# <titel>

## Samenvatting
Drie tot zes zinnen, neutraal: wat voor document dit is, van wie, voor welke situatie of doelgroep, de reikwijdte (wat regelt of beschrijft het, en wat opvallend niet) en de status (versie, geldig vanaf, vervangt). Geen oordeel over bruikbaarheid voor een wiki.

## Trefwoorden
Komma-gescheiden zoektermen, ook synoniemen en spreektaal die níet letterlijk in de titel staan (bijv. "urn, asbus, as, verstrooien").

## Begrippen
| Begrip | Regel | Soort |
|---|---|---|
| <term zoals in de bron> | <regelnummer in laag 1> | definitie / regeling / verwijzing |

## Verwijst naar
Andere wetten, regelingen of documenten die de bron noemt of uitwerkt, met regelnummer; bron-id als die al in `sources/index/` staat.

## Inhoud
(gegenereerd door `llmwiki source inhoud --schrijf`; niet met de hand wijzigen)
```

Bij een tekst van minder dan 2.000 woorden (zie de eerste regel van `## Inhoud`) volstaan *Samenvatting* en *Trefwoorden*: de tekst zelf lezen is dan goedkoop.

Sectie *Begrippen*: alleen termen die de bron definieert, regelt of als eigen begrip gebruikt, hooguit 40; soort `definitie` bij een begripsbepaling, `regeling` als de bron het onderwerp inhoudelijk regelt, `verwijzing` als de term alleen genoemd wordt.

## Grenzen

- Geen wiki-kennis: niets over elementen, modellen of de rol van de bron in één wiki. Dat hoort in de domein-lens (laag 3, `wiki-ingest`).
- Geen citaten of interpretaties waarop een pagina steunt: pagina's citeren laag 1 via de domein-lens.
- Eén index per bron, gedeeld door alle wiki's; een bestaande index vul je aan, je maakt geen tweede.
