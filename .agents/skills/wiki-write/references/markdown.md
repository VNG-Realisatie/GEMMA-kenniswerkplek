# Frontmatter-conventie voor Markdown-pagina's (curation/knowledge-base)

```yaml
---
id: kandidaat-zaakdossier            # stabiel, gelijk aan de bestandsnaam zonder .md
type: kandidaat                      # moet voorkomen in wiki.yaml page_types
status: review                       # alleen bij curated paginatypen; zie wiki.yaml curation.states
onderwerp: zaakgericht-werken        # id van de onderwerppagina
bronnen: [2026-vng-omgevingsplan]    # bron-id's uit sources/index/, voor herleidbaarheid
bijgewerkt: 2026-09-27
---
```

Regels:

- `id` moet gelijk zijn aan de bestandsnaam zonder `.md`.
- Gebruik alleen relatieve Markdown-links (`[tekst](../bronnen/x/y.md)`), nooit
  `[[wikilinks]]` en nooit een absoluut pad.
- Elke waarde in `bronnen:` moet bestaan in `sources/index/` en binnen de
  `sources.tags`-scope van deze wiki vallen; `llmwiki validate` meldt het anders.
- Verzin geen nieuwe paginatypen. Staat het type nog niet in `wiki.yaml
  page_types`, overleg dan met de redacteur voordat je verdergaat.
