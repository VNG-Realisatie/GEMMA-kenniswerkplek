# Takenlijst

## Harde regelovergangen verwijderen

Regel: zie `AGENTS.md`, sectie Schrijfwijze. Bestaande bestanden zijn nog met harde regelovergangen binnen alinea's en lijstitems geschreven.

- [ ] Alle Markdown-bestanden integraal omzetten naar één regel per alinea, lijstitem en tabelrij: `AGENTS.md` (root en per wiki), `ARCHITECTURE.md` (root en per wiki), `README.md`, `docs/`, `.agents/skills/` en `wikis/*/.agents/skills/` (inclusief `references/`), `wikis/_template*/`, `sources/index/`.
- [ ] Niet aanpassen: codeblokken, frontmatter, tabellen die al één rij per regel hebben, `sources/raw/` (onveranderlijk) en `wikis/gemma/content/` (letterlijke werkkopie van de site).
- [ ] Gegenereerde tekst meenemen: de Markdown die `llmwiki` en de wiki-tools schrijven (bijv. `tools/bepaal_type.py markdown`, voorstellen, `voortgang.md`) mag geen harde regelovergangen binnen een alinea bevatten.
- [ ] Een controle in `llmwiki lint` toevoegen die harde regelovergangen binnen alinea's en lijstitems meldt, zodat het niet terugkomt.
