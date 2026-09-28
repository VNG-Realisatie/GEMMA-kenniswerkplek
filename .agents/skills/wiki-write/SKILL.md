---
name: wiki-write
description: Schrijf de voorgestelde pagina's uit ASSESS als concept, gestaged in het kladblok van de run. Gebruik als derde fase van een wiki-update, na wiki-assess.
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "assessment"
  writes: "changeset"
---

# Skill wiki-write

Doel: de WRITE-fase. Schrijft concepten voor elke pagina uit `assessment.json`, maar
raakt de werkboom nog niet — alles wordt gestaged in `.work/runs/<run-id>/changeset/`.
Zo laat een afgebroken run niets achter in de wiki (`llmwiki run abandon`).

## Stappen

1. Voor elk voorstel met soort `nieuw` of `wijzigen`: schrijf de volledige
   paginatekst (met frontmatter) naar een bestand onder
   `.work/runs/<run-id>/changeset/<vrije-naam>.md`.
   - Zie `references/markdown.md` voor de frontmatter-conventie.
   - Nieuwe kandidaatpagina's krijgen `status: kandidaat`. Je mag een kandidaat naar
     `status: review` zetten als hij klaar is voor beoordeling; zet nooit zelf
     `status: goedgekeurd` (dat doet alleen `llmwiki promote apply`, ná akkoord).
2. Bouw `changeset.json` volgens schema `changeset`: per pagina het doelpad
   (relatief aan de wiki-root, bijvoorbeeld `kandidaten/kandidaat-zaakdossier.md`),
   het gestagede bestand, de actie (`nieuw`/`wijzigen`) en het paginatype.
3. Rond de fase af: `llmwiki run complete write --run <run-id> --data changeset.json`.

## Uitbreidingspunt

Een wiki-Workflow mag hier een aanvullende Skill laden voor domeinspecifieke
paginastructuur (bijvoorbeeld ArchiMate-paginatemplates). Schrijf ook die pagina's
naar `changeset/`, nooit direct naar de werkboom.
