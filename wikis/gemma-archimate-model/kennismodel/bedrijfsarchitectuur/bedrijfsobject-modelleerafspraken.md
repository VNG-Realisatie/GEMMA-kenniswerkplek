---
id: bedrijfsobject-modelleerafspraken
type: kennismodel
titel: Bedrijfsobject — modelleerafspraken
---

# Bedrijfsobject — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Object* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `bedrijfsobject`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. (GEMMA) |
| In Over GEMMA | ja (Bedrijfsobject) |
| Duiding | Een ding waar de gemeente mee werkt: het wordt geregistreerd, bijgewerkt of geraadpleegd door gemeentelijk gedrag. De soort regeling (Regeling) is ook een bedrijfsobject. |
| Herken je aan | geen aard (een ding); *afspraak* en *waarneembare vorm* nee. Moet ja: *wordt bewerkt* (kernrelatie); hoogstens 1 nee: *onderscheidbare exemplaren*, *levenscyclus*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsproces ─toegang→ Bedrijfsobject; Bedrijfsfunctie ─toegang→ Bedrijfsobject; Bedrijfsinteractie ─toegang→ Bedrijfsobject |
| Niveaus | kernobject: het object waarvan één levensloopproces de hele levensloop omvat · subobject: een deel van een kernobject, met een eigen bedrijfsproces · generiek object: dezelfde betekenis in veel onderwerpen; domeinspecialisaties krijgen geen pagina en staan in relaties met `via` · onderdeel zonder eigen proces, en invoer die een andere partij maakt: geen pagina |
| Eigenschappen | `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `ggm`: de match met het GGM: entiteit, sterkte en onderbouwing · `gemma`: de match met het GEMMA-model: het id gaat mee in de export · `data_object`: annotatie: het begrip wordt als gegevensstructuur geautomatiseerd verwerkt |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) |
| Naamvorm | de gangbare term uit beleid en praktijk, zonder lidwoord; de wetsterm wordt een synoniem met context "wet" |
| Afstemming | GGM: matchdoel en toets: entiteit, definitie en relaties; zonder match een GGM-terugmelding (hiaat) · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Graf; Aanvraag; Vergunning · niet: aanvraag ontvangen (gebeurtenis); register van begraven lijken (representatie) |

## Afspraken

- Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument voor een bedrijfsobject; alleen *geautomatiseerd verwerkt* telt, als annotatie.
- Een concreet benoemde regeling als geheel is een beleidskader; de soort ("verordening") is het bedrijfsobject Regeling.
- Een kernobject heeft één thuis: het onderwerp waar het ontstaat en beheerd wordt.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toegang | [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) | een verantwoordelijkheid: houder (lezen-schrijven), bronhouder (schrijven), beheerder (lezen-schrijven), verstrekker (lezen), afnemer (lezen), toezichthouder (lezen), betrokkene (lezen), partij (lezen-schrijven) |  | nee: uitbreiding op het GEMMA-kennismodel | een verantwoordelijkheid, als bij een rol |
| in | toegang | [Rol](rol-modelleerafspraken.md) | een verantwoordelijkheid: houder (lezen-schrijven), bronhouder (schrijven), beheerder (lezen-schrijven), verstrekker (lezen), afnemer (lezen), toezichthouder (lezen), betrokkene (lezen), partij (lezen-schrijven) |  | ja | een verantwoordelijkheid; *partij* alleen naar een afspraak |
| in | toegang | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | ja |  |
| in | toegang | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | ja |  |
| in | toegang | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | associatie (gericht) | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| uit | aggregatie | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | bevat |  | ja |  |
| uit | compositie | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | bevat |  | ja |  |
| uit | specialisatie | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | is een |  | ja |  |
| in | associatie (gericht) | [Afspraak](afspraak-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | associatie (gericht) | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | is grondslag voor, is model voor |  | nee: uitbreiding op het GEMMA-kennismodel | de regeling die het object regelt; *is model voor*: een VNG-model voor de soort regeling (Regeling) |
| in | realisatie | [Data-object](../applicatiearchitectuur/data-object-modelleerafspraken.md) | vrij, uit de bron |  | ja | nu een annotatie |
| in | aggregatie | [Groepering](../overig/groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Beleidsdomeinindeling |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Bedrijfsobject | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Rol ─associatie→ Bedrijfsobject | wat een rol met een object is, is toegang met een verantwoordelijkheid; een handeling is een toewijzing van de rol aan het proces |
| Dienst ─toegang→ Bedrijfsobject | een dienst heeft geen toegang tot een object; het proces dat haar realiseert wel |
| Gebeurtenis ─associatie→ Bedrijfsobject | het object volgt uit het levensloopproces waaronder de gebeurtenis hangt |
| Bedrijfsobject ─associatie→ Dienst | een object hangt via het proces dat de dienst realiseert (toegang) aan een dienst |
