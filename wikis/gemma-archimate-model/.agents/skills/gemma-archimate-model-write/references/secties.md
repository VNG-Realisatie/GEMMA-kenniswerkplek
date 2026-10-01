# Opbouw van een elementpagina

Een elementpagina is een beslisdocument: waarom dit een element van dit type is, hoe het zich verhoudt tot het GGM en GEMMA, en welke gegevens naar het ArchiMate-model gaan. Frontmatter volgens `schemas/<type>.schema.json` (zonder prefix = eigen veld; `ggm_*`/`gemma_*` alleen uit de tools; geen verwijzingen naar andere pagina's).

```markdown
---
id: beschikking
type: bedrijfsobject
status: review
naam: Beschikking
archimate_type: business-object
onderwerp: vergunningen
taakveld: 8 Volkshuisvesting
beleidsdomein: Vergunningen
bronnen: [2026-overheid-awb, 2026-utrecht-vergunningenbeleid]
definitie: Schriftelijk besluit van de gemeente over een individueel geval.
grondslag: ggm-entiteit
match: {ggm: exact, gemma: sterk}
data_object: ja
kenmerken: {herkenbaar: ja, gemeentelijk: ja, …}
ggm_entiteit: Beschikking
ggm_guid: EAID_…
bijgewerkt: 2026-09-29
---

# Beschikking

## Definitie

Schriftelijk besluit van de gemeente over een individueel geval.

## Beschrijving

…
```

Secties, in deze volgorde (alleen wat van toepassing is):

| Sectie | Wanneer | Inhoud |
|---|---|---|
| `# <naam>` | altijd | |
| `## Definitie` | altijd, als eerste sectie | De herkenbare `definitie` uit de frontmatter, letterlijk. Bij een formele definitie daaronder `definitie_formeel` als blockquote met vindplaats, en in één of twee zinnen het verschil (zie `definitie.md`) |
| `## Beschrijving` | altijd | Het element zelf, zoals de gemeente erover praat, los van het onderwerp waarin het is gevonden ([EL19]): de tekst past ongewijzigd in elk ander onderwerp. Bij een partij of generiek begrip uit een algemene bron (Gemeentewet, Awb, BW) |
| `## Per onderwerp` | als het element in een onderwerp een eigen rol speelt | Per onderwerp `### <naam onderwerp>` met een link naar `begrippen/<onderwerp>.md` en twee of drie zinnen met vindplaatsen: wat het element in dat onderwerp doet of betekent. De formele verbanden staan in `## Relaties`. Een nieuw onderwerp voegt een kopje toe en laat de andere ongemoeid |
| `## Kenmerken` | altijd | Tabel `\| Kenmerk \| Waarde \| Onderbouwing \| Bron \|` voor alle kenmerken (onderbouwing uit ASSESS); in kolom Bron elk bron-id als link naar de bronanalyse ([IH2]) |
| `## GGM-bron` | grondslag `ggm-entiteit` | GGM-definitie als blockquote, matchsterkte, afwijkingen |
| `## Afleiding` / `## Procesbron` / `## Juridische bron` | per grondslag | Zie `grondslag.md` |
| `## GEMMA` | altijd | Matchsterkte en wat verandert ten opzichte van GEMMA, of "nieuw voor GEMMA" |
| `## Naamkeuze` | bij naamconflict | Overwogen namen met reden |
| `## Generalisatie` / `## Specialisaties` / `## GGM-componenten` | bij hiërarchie | Zie `hierarchie.md` |
| `## GGM-duplicaten` | bij duplicaten in het GGM | Zie `ggm-match.md` |
| `## Homoniemen` | bij een homoniem (elke bron, elk type) | Tabel Begrip, Betekenis, Waar, Naamkeuze; zie `naamgeving.md` |
| `## Tegenhanger` | bij tegenhanger | Zie `tegenhangers.md` |
| `## Relaties` | als er relaties zijn | Zie `relaties.md`; alleen uitgaande relaties |
| `## Bronnen` | altijd | Per bron in `bronnen:` een link naar de bronanalyse: `[titel](../../../../bronanalyses/<onderwerp>/<bron-id>.md)`; een modelbron (GGM, GEMMA) linkt naar `sources/raw/<bron-id>.md` ([IH2]) |
| `## Ter discussie` | status `kandidaat` | Wat de redacteur moet beslissen, met de redenen uit de beslistabel |
| `## Terugmelding GGM` | bij terugmelding | Link naar `analyses/ggm-terugmeldingen.md` met het nummer |

Bron-id's als platte tekst zet `gam_gemeen.bronnen_als_link(<pad van de pagina>, <tekst>)` om naar links; `tools/relaties.py voorstel --markdown` levert de kolom Bron al met links.

Voor actor, rol, gebeurtenis, dienst, proces en functie gelden dezelfde secties; "welke rollen een actor vervult" of "wie een proces uitvoert" zijn relaties (toewijzing) in `## Relaties`, geen aparte secties. De omgekeerde kant ("vervuld door", "gebruikt door") is de backlink.
