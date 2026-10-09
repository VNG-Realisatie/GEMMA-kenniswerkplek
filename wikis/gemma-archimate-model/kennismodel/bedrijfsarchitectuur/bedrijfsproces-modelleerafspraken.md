---
id: bedrijfsproces-modelleerafspraken
type: kennismodel
titel: Bedrijfsproces — modelleerafspraken
---

# Bedrijfsproces — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Process* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `bedrijfsproces`

| Afspraak | Inhoud |
|---|---|
| Definitie | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. (GEMMA) |
| In Over GEMMA | ja (Bedrijfsproces) |
| Duiding | Wordt per keer doorlopen en levert een resultaat op. Ook het levensloopproces en het cluster naar soort werk zijn in ArchiMate een bedrijfsproces. |
| Herken je aan | Bedrijfsproces: *gedrag* en *per keer doorlopen*. Moet ja: *toegewezen partij* (kernrelatie), *aanleiding*, *benoembaar resultaat*. Procescluster: *gedrag* en *groepeert processen*. Moet ja: *omvat processen* (kernrelatie). Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Rol ─toewijzing→ Bedrijfsproces; Bedrijfsproces ─aggregatie→ Bedrijfsproces |
| Niveaus | levensloopproces: het gedrag over de hele levensloop van één exemplaar van een kernobject, van begin tot eind (*omvat levensloop*); in GEMMA een cluster van bedrijfsprocessen over één thema, GEMMA type *Bedrijfsproces (cluster)* · bedrijfsproces: klant tot klant, onder verantwoordelijkheid van één organisatie; één mutatie in de levensloop van een kernobject, en het levert een product, dienst of besluit (*bijdrage aan groter proces* met *klant tot klant*) · deelproces: binnen één bedrijfsfunctie, levert een deeldienst; geen pagina, de tekst staat in `deelprocessen` van het bedrijfsproces · processtap en handeling: geen pagina · cluster naar soort werk: de bedrijfsprocessen van één soort werk, als specialisatie van een generiek GEMMA-bedrijfsproces (*groepeert processen*) |
| Eigenschappen | `kernobject`: het bedrijfsobject waarvan het proces de levensloop omvat (levensloopproces), waarin het een mutatie doet (bedrijfsproces), of dat door de keten gaat (bedrijfsinteractie) · `afnemer` (verplicht): voor wie het is: extern of intern (de bovenste laag van het processenlandschap, de rol Klant en de externe en interne UPL-lijst) (extern, intern) · `gemma_generiek`: het generieke GEMMA-element waarvan dit een specialisatie is (exacte match) · `deelprocessen`: de deelprocessen in volgorde, elk met één of twee zinnen en een bron (geen eigen pagina) · `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) (alleen een levensloopproces, onder het beleidsdomein van zijn kernobject); [Procesindeling naar kernobject](../indelingen.md) (levensloopproces en bedrijfsproces); [Procesindeling naar soort werk](../indelingen.md) (cluster naar soort werk en bedrijfsproces) |
| Naamvorm | infinitief met het object in GEMMA-volgorde, werkwoord eerst, zonder lidwoord (Behandelen aanvraag); bestaat er een GEMMA-proces met dezelfde betekenis, dan de GEMMA-naam; het zelfstandig naamwoord uit de bron wordt een synoniem met context "beleid" |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: een bedrijfsproces specialiseert vaak een generiek GEMMA-bedrijfsproces (`gemma_generiek`, exacte match); een cluster naar soort werk altijd |
| Voorbeeld | wel: Beheren grafrechten (levensloopproces); Verlenen grafrecht (bedrijfsproces); Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk) · niet: Uitreiken reisdocument (deelproces: volgt op de verstrekking, voor hetzelfde geval); Vergunningverlening (functie) |

## Afspraken

- Per kernobject één levensloopproces, met het taakveld en beleidsdomein van het kernobject. Alleen binnen een ketensamenwerking mag een kernobject er meer hebben, één per partij, die samen de bedrijfsinteractie met dat kernobject bedienen.
- Een bedrijfsproces begint bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt door tot het resultaat voor die klant, zonder de voortzetting te zijn van een ander proces voor hetzelfde geval. *Eigen besluit* en *eigen normering* bepalen het procesniveau niet; *levert aanbod* zonder *klant tot klant* wordt voorgelegd.
- Een bedrijfsproces hangt onder één levensloopproces. Triggert een bedrijfsproces een ander bedrijfsproces onder hetzelfde levensloopproces voor hetzelfde geval, dan wordt dat voorgelegd (mogelijk een deelproces).
- Een groepering van processen is alleen een cluster naar soort werk, met `gemma_generiek`, en alleen bij minstens twee bedrijfsprocessen; anders specialiseert het bedrijfsproces zelf. De taak is geen procesniveau: boven het levensloopproces staan beleidsdomein en taakveld uit de Beleidsdomeinindeling.
- Een ketenproces is geen procesniveau en geen element: waar de bedrijfsprocessen van meer partijen samenkomen, is dat een bedrijfsinteractie.
- Een rol mag aan een bedrijfsproces worden toegewezen, niet alleen aan een bedrijfsfunctie.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toewijzing | [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | ja |  |
| in | toewijzing | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit*, *toegewezen partij* | ja |  |
| uit | toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | ja |  |
| uit | toegang | [Afspraak](afspraak-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | realisatie | [Dienst](dienst-modelleerafspraken.md) | realiseert | *gerealiseerd door* | ja |  |
| in | bediening | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | bedient | *bedient gedrag* | ja |  |
| uit | bediening | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | bedient |  | ja |  |
| uit | bediening | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | de bedrijfsprocessen van de partijen bedienen de ketensamenwerking |
| uit | aggregatie | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | omvat | *omvat processen* | ja | levensloopproces of cluster naar soort werk → bedrijfsproces |
| uit | aggregatie | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | omvat |  | nee: uitbreiding op het GEMMA-kennismodel | levensloopproces → gebeurtenis van zijn kernobject |
| uit | specialisatie | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | is een |  | ja |  |
| uit | triggering | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | leidt tot |  | ja |  |
| uit | triggering | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | leidt tot |  | ja |  |
| uit | stroom | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | geeft iets door aan een ander proces |
| in | triggering | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | leidt tot | *leidt tot gedrag* | ja |  |
| in | bediening | [Dienst](dienst-modelleerafspraken.md) | bedient |  | ja |  |
| in | associatie (gericht) | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | is grondslag voor, werkt uit voor, geeft richtlijn voor | *is grondslag voor* | nee: uitbreiding op het GEMMA-kennismodel | de grondslag; bij voorkeur naar een product |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Bedrijfsproces | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Bedrijfsfunctie ─aggregatie of compositie→ Bedrijfsproces | een functie bedient een proces; processen groeperen in een cluster naar soort werk |
