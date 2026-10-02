---
id: ggm-terugmeldingen
type: analyse
titel: GGM-terugmeldingen
---

# GGM-terugmeldingen

<!-- Gegenereerd door tools/render.py uit beoordelingen/terugmeldingen.yaml. Wijzig de beoordeling, niet deze pagina. -->

Bevindingen uit de beoordeling van elementen die aan het GGM-beheer worden teruggekoppeld.

## Terugmeldingen

| # | Domein | Entiteit | Type | Bevinding | Element | Status |
|---|---|---|---|---|---|---|
| 1 | Gemeentebegrafenissen | Gemeentebegrafenis | definitie | Definitie 'Teraardebestelling onder verantwoordelijjkheid van de gemeente' is te smal: de burgemeester draagt zorg voor de lijkbezorging als niemand daarin voorziet, en dat kan ook crematie zijn; alleen een lijk waarvan de identiteit niet kan worden vastgesteld, wordt begraven (Wet op de lijkbezorging art. 21 lid 1 en 6). Voorstel: 'Lijkbezorging waarvoor de gemeente zorgt en betaalt omdat niemand anders daarin voorziet.' Ook tikfout 'verantwoordelijjkheid'. | [Gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) | open |
| 2 | Gemeentebegrafenissen | Gemeentebegrafenis | scope | Gemeentebegrafenis staat onder 6 Sociaal Domein. De lijkbezorging (graf, grafrecht, begraafplaats, gemeentebegrafenis) hoort bij Iv3-taakveld 7.5 Begraafplaatsen en crematoria (7 Volksgezondheid en Milieu); deze wiki plaatst het element daar. Overweeg een beleidsdomein Begraafplaatsen en crematoria, waarin ook de hiaten graf en grafrecht passen. | [Gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) | open |
| 3 | Begraafplaatsen en crematoria | — | hiaat | Graf ontbreekt in het GGM, terwijl Gemeentebegrafenis er wel naar verwijst (attribuut datumRuimingGraf). Als houder van de gemeentelijke begraafplaats geeft de gemeente graven uit, opent en sluit ze en ruimt ze (Wet op de lijkbezorging art. 23, 27, 31; beheersverordening Groningen art. 7, 11-16, 27). Relevante attributen: grafsoort (algemeen, particulier, kinder-, urnengraf, urnennis, partnergraf), ligging (vak, nummer), aantal grafruimtes, datum laatste begraving (ruimtermijn tien jaar), en per graf de begraven lijken en bijgezette urnen met datum (register van begraven lijken, art. 27). Past in een beleidsdomein Begraafplaatsen en crematoria, naast Gemeentebegrafenis. | [Graf](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) | open |
| 4 | Begraafplaatsen en crematoria | — | hiaat | Grafrecht (uitsluitend recht op een graf, art. 28) ontbreekt in het GGM. Het recht wordt schriftelijk gevestigd voor onbepaalde tijd of ten minste tien jaar, verlengd, overgeschreven en kan vervallen of vervallen worden verklaard (Wet op de lijkbezorging art. 28; beheersverordening Groningen art. 16, 18-20); gemeenten heffen er lijkbezorgingsrechten voor. Relevante attributen: rechthebbende, graf, ingangsdatum, looptijd, verlengingen, overschrijvingen, datum verval en reden. Past in een beleidsdomein Begraafplaatsen en crematoria. | [Grafrecht](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafrecht.md) | open |
| 5 | Generiek Jeugd en Wmo | Beschikking | duplicaat | Beschikking komt twee keer voor met verschillende GUID's: Generiek Jeugd en Wmo (EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836, gekoppeld aan GEMMA-bedrijfsobject Beschikking) en Diensten (EAID_16ABCFF8_4817_6A73_59BA_281C3303F8D2, 'een voor beroep vatbaar overheidsbesluit'). Het is hetzelfde bestuursrechtelijke begrip; samenvoegen tot één generieke entiteit. De definitie van Generiek Jeugd en Wmo omvat ook de civielrechtelijke beschikking (rechterlijke uitspraak), die daarbij beter kan vervallen. | [Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | open |
| 6 | RGBZPlus | Besluit | definitie | De GGM-definitie van Besluit ('een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval') beschrijft een beschikking. Volgens de Awb is een besluit een schriftelijke beslissing van een bestuursorgaan, inhoudende een publiekrechtelijke rechtshandeling (art. 1:3 lid 1), en omvat het ook besluiten van algemene strekking; een beschikking is een besluit dat niet van algemene strekking is (art. 1:3 lid 2). Voorstel: de Awb-definitie overnemen. | [Besluit](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) | open |
| 7 | RGBZPlus | Besluit | duplicaat | Besluit komt twee keer voor met verschillende GUID's en dezelfde definitie: RGBZPlus (99 Kern, EAID_AFB100D2_8C68_4488_8949_13E945D15920, gekoppeld aan GEMMA-bedrijfsobject Besluit) en Diensten (Inkomen, EAID_0CA08ED2_6990_8292_BBC7_281C33037374). Samenvoegen tot de domeinoverstijgende entiteit in RGBZPlus. | [Besluit](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) | open |
| 8 | RGBZPlus | Beschikking | structuur | Beschikking is een domeinoverstijgend begrip: een besluit dat niet van algemene strekking is (Awb art. 1:3 lid 2). Het GGM kent Beschikking alleen in de beleidsdomeinen Generiek Jeugd en Wmo en Diensten (zie terugmelding 5), en niet als generalisatie-specialisatie van Besluit. Voorstel: één domeinoverstijgende entiteit Beschikking in RGBZPlus (99 Kern), als specialisatie van Besluit, waarnaar de domeinspecifieke beschikkingen verwijzen. | [Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | open |
| 9 | Musea | Belanghebbende | scope | Belanghebbende (definitie gelijk aan art. 1:2 Awb) is een algemeen begrip uit het bestuursrecht, maar staat in het GGM alleen in het beleidsdomein Musea. Voorstel: onderbrengen in een algemeen beleidsdomein (bijvoorbeeld Kern of Besluitvorming), zodat alle beleidsdomeinen ernaar kunnen verwijzen. | Belanghebbende | open |
| 10 | Model Inkomen | Regeling | homoniem | Het GGM gebruikt de naam Regeling voor een afspraak of regeling met een cliënt (Terug- en invordering, Diensten, Model Inkomen), terwijl GEMMA en het spraakgebruik Regeling gebruiken voor de soort wet of verordening (algemeen verbindend voorschrift; Gemeentewet art. 147, 149). Voorstel: de GGM-entiteiten een specifiekere naam geven, bijvoorbeeld Cliëntregeling of Betalingsregeling, en in alle drie de domeinen dezelfde naam gebruiken. | [Regeling](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/regeling.md) | open |
| 11 | Archief | Rechthebbende | homoniem | Het GGM gebruikt Rechthebbende in Archief voor iemand die rechten heeft op een goed. De Wet op de lijkbezorging en de beheersverordeningen gebruiken rechthebbende voor wie het uitsluitend recht op een particulier graf heeft (art. 23, 28). Deze wiki noemt dat element Rechthebbende op het graf. Voorstel: de GGM-definitie in Archief verbijzonderen (rechthebbende op archiefbescheiden), zodat de algemene naam niet aan één domein vastzit. | [Rechthebbende op het graf](../bedrijfsarchitectuur/rollen/rechthebbende-op-het-graf.md) | open |

## Typen

| Type | Betekenis |
|---|---|
| hiaat | Concept ontbreekt in het GGM |
| definitie | Entiteit bestaat, maar de definitie is onjuist, onvolledig of geen begripsdefinitie |
| structuur | Onhandige modellering (overerving, ontbrekende relatie, granulariteit) |
| scope | Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander |
| duplicaat | Zelfde concept met meerdere GUID's in verschillende beleidsdomeinen → samenvoegen |
| homoniem | Zelfde naam voor een ander concept in een ander beleidsdomein → hernoemen |
| relatie | Fout in een exact gematchte relatie (type, richting, kardinaliteit, naam, dubbel) |

## Status

open → gemeld → opgelost of afgewezen (met reden).
