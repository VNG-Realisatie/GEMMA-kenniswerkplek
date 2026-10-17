---
id: bedrijfsobject-modelleerafspraken
type: kennismodel
titel: Bedrijfsobject — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Bedrijfsobject — modelleerafspraken

*Business Object* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/passief` · paginatype `bedrijfsobject`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. (GEMMA) |
| In Over GEMMA | ja (Bedrijfsobject) |
| Duiding | Een ding waar de gemeente mee werkt: het wordt geregistreerd, bijgewerkt of geraadpleegd door gemeentelijk gedrag. De soort regeling (Regeling) is ook een bedrijfsobject. |
| Herken je aan | *ding*; *afspraak* en *waarneembare vorm* nee. Moet ja: *wordt bewerkt* (kernrelatie); hoogstens 1 nee: *onderscheidbare exemplaren*, *levenscyclus*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsproces ─toegang→ Bedrijfsobject; Bedrijfsfunctie ─toegang→ Bedrijfsobject; Bedrijfsinteractie ─toegang→ Bedrijfsobject |
| Niveaus | kernobject: het object waarvan één levensloopproces de hele levensloop omvat · subobject: een deel van een kernobject, met een eigen bedrijfsproces · generiek object: dezelfde betekenis in veel onderwerpen; domeinspecialisaties krijgen geen pagina en staan in relaties met `via` · onderdeel zonder eigen proces, en invoer die een andere partij maakt: geen pagina |
| Eigenschappen | `taakveld` · `beleidsdomein` · `ggm` · `gemma` · `data_objecten` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) |
| Naamvorm | de gangbare term uit beleid en praktijk, zonder lidwoord; de wetsterm wordt een synoniem met context "wet" |
| Afstemming | GGM: matchdoel en toets: entiteit, definitie en relaties; zonder match een GGM-terugmelding (hiaat) · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Graf; Aanvraag; Vergunning · niet: aanvraag ontvangen (gebeurtenis); register van begraven lijken (representatie) |

## Afspraken

- Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument voor een bedrijfsobject; de beschrijving mag de registratie noemen.
- Een concreet benoemde regeling als geheel is een beleidskader; de soort ("verordening") is het bedrijfsobject Regeling.
- Een kernobject heeft één thuis: het onderwerp waar het ontstaat en beheerd wordt.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| associatie (gericht) | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| aggregatie | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | bevat |  | ja |  |
| compositie | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | bevat |  | ja |  |
| specialisatie | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | is een |  | ja |  |

Inkomend, bij het brontype: [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) (toegang); [Rol](rol-modelleerafspraken.md) (toegang); [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) (toegang); [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) (toegang); [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) (toegang); [Afspraak](afspraak-modelleerafspraken.md) (associatie); [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) (associatie); [Data-object](../applicatiearchitectuur/data-object-modelleerafspraken.md) (realisatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
