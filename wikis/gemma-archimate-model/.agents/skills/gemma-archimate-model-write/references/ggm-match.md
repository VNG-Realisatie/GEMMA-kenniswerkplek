# GGM-match

## Zoeken

`uv run python tools/ggm.py zoek <term>` (naam, synoniemen, definitie over alle beleidsdomeinen), `entiteit <guid|naam>`, `naamgenoten <naam>`. Nooit het XMI of `ggm/ggm_parsed.json` zelf doorzoeken ([SRC1]); `ggm/` is alleen om te lezen.

## Matchsterkte (`match.ggm`)

| Sterkte | Betekenis | Actie |
|---|---|---|
| `exact` | Zelfde begrip, definitie klopt | Overnemen |
| `sterk` | Zelfde begrip, definitie of reikwijdte wijkt licht af | Overnemen, afwijking in `## GGM-bron`, terugmelden |
| `partieel` | GGM dekt een deel, of het element bundelt meerdere entiteiten | Overnemen met toelichting, terugmelding overwegen |
| `zwak` | Verwant, maar wezenlijk andere reikwijdte of granulariteit | Niet als grondslag; hooguit een relatie noteren |
| `geen` | Geen GGM-entiteit | Grondslag zonder GGM |

Bij `data_object: ja` en een match zwakker dan `sterk` wordt het element voorgelegd.

## Mapping

- Bij voorkeur één-op-één. Aggregatie mag als het GGM te fijnmazig is; noem de samengevoegde entiteiten.
- **Duplicaat** (zelfde begrip in meerdere beleidsdomeinen, andere GUID): één element; de thematisch passende GUID wordt `ggm_guid`, de andere gaan in `ggm_duplicaat_entiteiten` (entiteit, guid, beleidsdomein, taakveld, afwijkende_attributen) en in `## GGM-duplicaten` (tabel `| Beleidsdomein | GUID | Status |` met primair/duplicaat en de reden). Leg de keuze van de primaire GUID voor. Terugmelden als `duplicaat`.
- **Homoniem** (zelfde naam, ander begrip): niet in `ggm_duplicaat_entiteiten`; wel in `## Homoniemen` (tabel met Begrip, Betekenis, Waar, Naamkeuze; zie `naamgeving.md`) met een link naar het andere element (als dat bestaat). Naam kiezen volgens `naamgeving.md`. Terugmelden als `homoniem`.

## Velden

Plak de uitvoer van `uv run python tools/ggm.py velden <guid>` ongewijzigd in de frontmatter. Lege velden laat de tool weg. Een nieuwe GGM-release ververst ze met `tools/ggm.py verrijk --run <run-id>`.

## `## GGM-bron`

De letterlijke GGM-definitie als blockquote, entiteit en beleidsdomein, de matchsterkte met toelichting, en eventuele afwijkingen (ook een afwijkende naam, zie `naamgeving.md`). Bij een afwijking: terugmelding.
