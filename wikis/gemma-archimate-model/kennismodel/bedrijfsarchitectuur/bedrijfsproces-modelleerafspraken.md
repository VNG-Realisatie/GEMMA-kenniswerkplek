---
id: bedrijfsproces-modelleerafspraken
type: kennismodel
titel: Bedrijfsproces — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Bedrijfsproces — modelleerafspraken

*Business Process* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/gedrag-intern` · paginatype `bedrijfsproces`

| Afspraak | Inhoud |
|---|---|
| Definitie | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. (GEMMA) |
| In Over GEMMA | ja (Bedrijfsproces) |
| Duiding | Wordt per keer doorlopen en levert een resultaat op. Ook het levensloopproces en het cluster naar soort werk zijn in ArchiMate een bedrijfsproces. |
| Herken je aan | Bedrijfsproces: *gedrag* en *per keer doorlopen*. Toetskenmerken, alle ja: *toegewezen partij* †, *aanleiding* †, *benoembaar resultaat*. Procescluster: *gedrag* en *per keer doorlopen*, procesniveau *cluster naar soort werk*. Toetskenmerken, alle ja: *omvat processen* †. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Rol ─toewijzing→ Bedrijfsproces; Bedrijfsproces ─aggregatie→ Bedrijfsproces |
| Niveaus | levensloopproces: het gedrag over de hele levensloop van één exemplaar van een kernobject, van begin tot eind (*procesniveau* levensloopproces); in GEMMA een cluster van bedrijfsprocessen over één thema, GEMMA type *Bedrijfsproces (cluster)* · bedrijfsproces: klant tot klant, onder verantwoordelijkheid van één organisatie; één mutatie in de levensloop van een kernobject, en het levert een product, dienst of besluit (*procesniveau* bedrijfsproces) · deelproces (*afhankelijkheid*): binnen één bedrijfsfunctie, levert een deeldienst; geen pagina, de tekst staat in `deelprocessen` van het bedrijfsproces · processtap en handeling: geen pagina · cluster naar soort werk: de bedrijfsprocessen van één soort werk, als specialisatie van een generiek GEMMA-bedrijfsproces (*procesniveau* cluster naar soort werk) |
| Eigenschappen | `kernobject` · `afnemer` (verplicht) · `gemma_generiek` · `deelprocessen` · `taakveld` · `beleidsdomein` · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) (alleen een levensloopproces of een generiek bedrijfsproces, onder het beleidsdomein van zijn kernobject); [Procesindeling naar kernobject](../indelingen.md) (levensloopproces en bedrijfsproces); [Procesindeling naar soort werk](../indelingen.md) (cluster naar soort werk en bedrijfsproces) |
| Naamvorm | infinitief met het object in GEMMA-volgorde, werkwoord eerst, zonder lidwoord (Behandelen aanvraag); bestaat er een GEMMA-proces met dezelfde betekenis, dan de GEMMA-naam; het zelfstandig naamwoord uit de bron wordt een synoniem met context "beleid" |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: een bedrijfsproces specialiseert vaak een generiek GEMMA-bedrijfsproces (`gemma_generiek`, exacte match); een cluster naar soort werk altijd |
| Voorbeeld | wel: Beheren grafrechten (levensloopproces); Verlenen grafrecht (bedrijfsproces); Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk) · niet: Uitreiken reisdocument (deelproces: volgt op de verstrekking, voor hetzelfde geval); Vergunningverlening (functie) |

## Afspraken

- Per kernobject één levensloopproces, met het taakveld en beleidsdomein van het kernobject. Alleen binnen een ketensamenwerking mag een kernobject er meer hebben, één per partij, die samen de bedrijfsinteractie met dat kernobject bedienen.
- Een bedrijfsproces begint bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt door tot het resultaat voor die klant, zonder de voortzetting te zijn van een ander proces voor hetzelfde geval. *Eigen besluit* en *eigen normering* bepalen het procesniveau niet en zijn geen kenmerk meer.
- Een bedrijfsproces hangt onder één levensloopproces; een generiek bedrijfsproces, met een generiek object als kernobject (Uitvoeren uniforme openbare voorbereidingsprocedure, kernobject Besluit), hangt onder het beleidsdomein van zijn kernobject. Triggert een bedrijfsproces een ander bedrijfsproces onder hetzelfde levensloopproces voor hetzelfde geval, dan wordt dat voorgelegd (mogelijk een deelproces).
- Een groepering van processen is alleen een cluster naar soort werk, met `gemma_generiek`, en alleen bij minstens twee bedrijfsprocessen; anders specialiseert het bedrijfsproces zelf. De taak is geen procesniveau: boven het levensloopproces staan beleidsdomein en taakveld uit de Beleidsdomeinindeling.
- Een ketenproces is geen procesniveau en geen element: waar de bedrijfsprocessen van meer partijen samenkomen, is dat een bedrijfsinteractie.
- Een rol mag aan een bedrijfsproces worden toegewezen, niet alleen aan een bedrijfsfunctie.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een [handeling](../README.md#relatietypen) | *wordt bewerkt* | ja |  |
| toegang | [Afspraak](afspraak-modelleerafspraken.md) | een [handeling](../README.md#relatietypen) | *wordt bewerkt* | nee |  |
| realisatie | [Dienst](dienst-modelleerafspraken.md) | realiseert | *gerealiseerd door* | ja |  |
| bediening | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | bedient |  | ja |  |
| bediening | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | vrij, uit de bron |  | nee | de bedrijfsprocessen van de partijen bedienen de ketensamenwerking |
| aggregatie | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | omvat | *omvat processen* | ja | levensloopproces of cluster naar soort werk → bedrijfsproces |
| aggregatie | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | omvat |  | nee | levensloopproces → gebeurtenis van zijn kernobject |
| specialisatie | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | is een |  | ja |  |
| triggering | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | leidt tot |  | ja |  |
| triggering | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | leidt tot |  | ja |  |
| stroom | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron |  | nee | geeft iets door aan een ander proces |

Inkomend, bij het brontype: [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) (toewijzing); [Rol](rol-modelleerafspraken.md) (toewijzing); [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) (bediening); [Gebeurtenis](gebeurtenis-modelleerafspraken.md) (triggering); [Dienst](dienst-modelleerafspraken.md) (bediening); [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) (associatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
