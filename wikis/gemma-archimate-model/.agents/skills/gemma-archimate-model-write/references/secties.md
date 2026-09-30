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
| `## Beschrijving` | altijd | Het element zoals de gemeente erover praat |
| `## Kenmerken` | altijd | Tabel `\| Kenmerk \| Waarde \| Onderbouwing \| Bron \|` voor alle kenmerken (onderbouwing uit ASSESS) |
| `## GGM-bron` | grondslag `ggm-entiteit` | GGM-definitie als blockquote, matchsterkte, afwijkingen |
| `## Afleiding` / `## Procesbron` / `## Juridische bron` | per grondslag | Zie `grondslag.md` |
| `## GEMMA` | altijd | Matchsterkte en wat verandert ten opzichte van GEMMA, of "nieuw voor GEMMA" |
| `## Naamkeuze` | bij naamconflict | Overwogen namen met reden |
| `## Generalisatie` / `## Specialisaties` / `## GGM-componenten` | bij hiërarchie | Zie `hierarchie.md` |
| `## GGM-duplicaten` / `## Homoniemen` | bij naamgenoten in het GGM | Zie `ggm-match.md` |
| `## Tegenhanger` | bij tegenhanger | Zie `tegenhangers.md` |
| `## Relaties` | als er relaties zijn | Zie `relaties.md`; alleen uitgaande relaties |
| `## Bronnen` | altijd | Links naar de bronanalyses: `[titel](../../../../bronanalyses/<onderwerp>/<bron-id>.md)` |
| `## Ter discussie` | status `kandidaat` | Wat de redacteur moet beslissen, met de redenen uit de beslistabel |
| `## Terugmelding GGM` | bij terugmelding | Link naar `analyses/ggm-terugmeldingen.md` met het nummer |

Voor actor, rol, gebeurtenis, dienst, proces en functie gelden dezelfde secties; "welke rollen een actor vervult" of "wie een proces uitvoert" zijn relaties (toewijzing) in `## Relaties`, geen aparte secties. De omgekeerde kant ("vervuld door", "gebruikt door") is de backlink.
