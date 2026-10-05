---
id: ggm-terugmeldingen
type: analyse
titel: GGM-terugmeldingen
---

# GGM-terugmeldingen

<!-- Gegenereerd door tools/render.py uit beoordelingen/terugmeldingen.yaml. Wijzig de beoordeling, niet deze pagina. -->

Bevindingen uit de beoordeling van elementen die aan het GGM-beheer worden teruggekoppeld.

## Terugmeldingen

### Hiaat

Concept ontbreekt in het GGM.

| # | Element | Bevinding |
|---|---|---|
| 3 open | [Graf](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) (GGM: ontbreekt, past in Begraafplaatsen en crematoria) | **GGM:** Graf ontbreekt, terwijl Gemeentebegrafenis er wel naar verwijst (attribuut datumRuimingGraf).<br><br>**Bevinding:** als houder van de gemeentelijke begraafplaats geeft de gemeente graven uit, opent en sluit ze en ruimt ze (Wet op de lijkbezorging art. 23, 27, 31; beheersverordening Groningen art. 7, 11-16, 27). Relevante attributen:<br>• grafsoort (algemeen, particulier, kinder-, urnengraf, urnennis, partnergraf);<br>• ligging (vak, nummer);<br>• aantal grafruimtes;<br>• datum laatste begraving (ruimtermijn tien jaar);<br>• per graf de begraven lijken en bijgezette urnen met datum (register van begraven lijken, art. 27).<br><br>**Voorstel:** opnemen in een beleidsdomein Begraafplaatsen en crematoria, naast Gemeentebegrafenis. |
| 4 open | [Grafrecht](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafrecht.md) (GGM: ontbreekt, past in Begraafplaatsen en crematoria) | **GGM:** Grafrecht (uitsluitend recht op een graf, art. 28) ontbreekt.<br><br>**Bevinding:** het recht wordt schriftelijk gevestigd voor onbepaalde tijd of ten minste tien jaar, verlengd, overgeschreven en kan vervallen of vervallen worden verklaard (Wet op de lijkbezorging art. 28; beheersverordening Groningen art. 16, 18-20); gemeenten heffen er lijkbezorgingsrechten voor. Relevante attributen:<br>• rechthebbende;<br>• graf;<br>• ingangsdatum en looptijd;<br>• verlengingen en overschrijvingen;<br>• datum verval en reden.<br><br>**Voorstel:** opnemen in een beleidsdomein Begraafplaatsen en crematoria. |

### Definitie

Entiteit bestaat, maar de definitie is onjuist, onvolledig of geen begripsdefinitie.

| # | Element | Bevinding |
|---|---|---|
| 1 open | [Gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) (GGM: Gemeentebegrafenissen) | **GGM:** 'Teraardebestelling onder verantwoordelijjkheid van de gemeente'.<br><br>**Bevinding:** de definitie is te smal. De burgemeester draagt zorg voor de lijkbezorging als niemand daarin voorziet, en dat kan ook crematie zijn; alleen een lijk waarvan de identiteit niet kan worden vastgesteld, wordt begraven (Wet op de lijkbezorging art. 21 lid 1 en 6). Ook tikfout 'verantwoordelijjkheid'.<br><br>**Voorstel:** 'Lijkbezorging waarvoor de gemeente zorgt en betaalt omdat niemand anders daarin voorziet.' |
| 6 open | [Besluit](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) (GGM: RGBZPlus) | **GGM:** Besluit is 'een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval'.<br><br>**Bevinding:** die definitie beschrijft een beschikking. Volgens de Awb is een besluit een schriftelijke beslissing van een bestuursorgaan, inhoudende een publiekrechtelijke rechtshandeling (art. 1:3 lid 1), en omvat het ook besluiten van algemene strekking; een beschikking is een besluit dat niet van algemene strekking is (art. 1:3 lid 2).<br><br>**Voorstel:** de Awb-definitie overnemen. |

### Structuur

Onhandige modellering (overerving, ontbrekende relatie, granulariteit).

| # | Element | Bevinding |
|---|---|---|
| 8 open | [Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) (GGM: RGBZPlus) | **GGM:** Beschikking staat alleen in de beleidsdomeinen Generiek Jeugd en Wmo en Diensten (zie terugmelding 5), en niet als specialisatie van Besluit.<br><br>**Bevinding:** Beschikking is een domeinoverstijgend begrip: een besluit dat niet van algemene strekking is (Awb art. 1:3 lid 2).<br><br>**Voorstel:** één domeinoverstijgende entiteit Beschikking in RGBZPlus (99 Kern), als specialisatie van Besluit, waarnaar de domeinspecifieke beschikkingen verwijzen. |

### Scope

Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander.

| # | Element | Bevinding |
|---|---|---|
| 2 open | [Gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) (GGM: Gemeentebegrafenissen) | **GGM:** Gemeentebegrafenis staat onder 6 Sociaal Domein.<br><br>**Bevinding:** de lijkbezorging (graf, grafrecht, begraafplaats, gemeentebegrafenis) hoort bij Iv3-taakveld 7.5 Begraafplaatsen en crematoria (7 Volksgezondheid en Milieu); deze wiki plaatst het element daar.<br><br>**Voorstel:** een beleidsdomein Begraafplaatsen en crematoria, waarin ook de hiaten graf en grafrecht passen. |
| 9 open | Belanghebbende (GGM: Musea) | **GGM:** Belanghebbende (definitie gelijk aan art. 1:2 Awb) staat alleen in het beleidsdomein Musea.<br><br>**Bevinding:** het is een algemeen begrip uit het bestuursrecht.<br><br>**Voorstel:** onderbrengen in een algemeen beleidsdomein (bijvoorbeeld Kern of Besluitvorming), zodat alle beleidsdomeinen ernaar kunnen verwijzen. |

### Duplicaat

Zelfde concept met meerdere GUID's in verschillende beleidsdomeinen → samenvoegen.

| # | Element | Bevinding |
|---|---|---|
| 5 open | [Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) (GGM: Generiek Jeugd en Wmo) | **GGM:** Beschikking komt twee keer voor met verschillende GUID's:<br>• Generiek Jeugd en Wmo (EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836, gekoppeld aan GEMMA-bedrijfsobject Beschikking);<br>• Diensten (EAID_16ABCFF8_4817_6A73_59BA_281C3303F8D2, 'een voor beroep vatbaar overheidsbesluit').<br><br>**Bevinding:** het is hetzelfde bestuursrechtelijke begrip. De definitie van Generiek Jeugd en Wmo omvat ook de civielrechtelijke beschikking (rechterlijke uitspraak).<br><br>**Voorstel:** samenvoegen tot één generieke entiteit; de civielrechtelijke beschikking kan daarbij beter vervallen. |
| 7 open | [Besluit](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) (GGM: RGBZPlus) | **GGM:** Besluit komt twee keer voor met verschillende GUID's en dezelfde definitie:<br>• RGBZPlus (99 Kern, EAID_AFB100D2_8C68_4488_8949_13E945D15920, gekoppeld aan GEMMA-bedrijfsobject Besluit);<br>• Diensten (Inkomen, EAID_0CA08ED2_6990_8292_BBC7_281C33037374).<br><br>**Voorstel:** samenvoegen tot de domeinoverstijgende entiteit in RGBZPlus. |

### Homoniem

Zelfde naam voor een ander concept in een ander beleidsdomein → hernoemen.

| # | Element | Bevinding |
|---|---|---|
| 10 open | [Regeling](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/regeling.md) (GGM: Model Inkomen) | **GGM:** Regeling is een afspraak of regeling met een cliënt (Terug- en invordering, Diensten, Model Inkomen).<br><br>**Bevinding:** GEMMA en het spraakgebruik gebruiken Regeling voor de soort wet of verordening (algemeen verbindend voorschrift; Gemeentewet art. 147, 149).<br><br>**Voorstel:** de GGM-entiteiten een specifiekere naam geven, bijvoorbeeld Cliëntregeling of Betalingsregeling, en in alle drie de domeinen dezelfde naam gebruiken. |
| 11 open | [Rechthebbende op het graf](../bedrijfsarchitectuur/rollen/rechthebbende-op-het-graf.md) (GGM: Rechthebbende, Archief) | **GGM:** Rechthebbende in Archief is iemand die rechten heeft op een goed.<br><br>**Bevinding:** de Wet op de lijkbezorging en de beheersverordeningen gebruiken rechthebbende voor wie het uitsluitend recht op een particulier graf heeft (art. 23, 28). Deze wiki noemt dat element Rechthebbende op het graf.<br><br>**Voorstel:** de GGM-definitie in Archief verbijzonderen (rechthebbende op archiefbescheiden), zodat de algemene naam niet aan één domein vastzit. |

## Status

open → gemeld → opgelost of afgewezen (met reden).
