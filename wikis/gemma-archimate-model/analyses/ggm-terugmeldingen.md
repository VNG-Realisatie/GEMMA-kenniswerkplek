---
id: ggm-terugmeldingen
type: analyse
titel: GGM-terugmeldingen
---

# GGM-terugmeldingen

Bevindingen uit de beoordeling van elementen die aan het GGM-beheer worden teruggekoppeld. Rijen worden alleen toegevoegd; de status wordt bijgewerkt.

## Terugmeldingen

| # | Domein | Entiteit | Type | Bevinding | Element | Status |
|---|---|---|---|---|---|---|
| 1 | Gemeentebegrafenissen | Gemeentebegrafenis | definitie | Definitie 'Teraardebestelling onder verantwoordelijjkheid van de gemeente' is te smal: de burgemeester draagt zorg voor de lijkbezorging als niemand daarin voorziet, en dat kan ook crematie zijn; alleen een lijk waarvan de identiteit niet kan worden vastgesteld, wordt begraven (Wet op de lijkbezorging art. 21 lid 1 en 6). Voorstel: 'Lijkbezorging waarvoor de gemeente zorgt en betaalt omdat niemand anders daarin voorziet.' Ook tikfout 'verantwoordelijjkheid'. | [gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) | open |
| 2 | Gemeentebegrafenissen | Gemeentebegrafenis | scope | Gemeentebegrafenis staat onder 6 Sociaal Domein. De lijkbezorging (graf, grafrecht, begraafplaats, gemeentebegrafenis) hoort bij Iv3-taakveld 7.5 Begraafplaatsen en crematoria (7 Volksgezondheid en Milieu); deze wiki plaatst het element daar. Overweeg een beleidsdomein Begraafplaatsen en crematoria, waarin ook de hiaten graf en grafrecht passen. | [gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) | open |
| 3 | Begraafplaatsen en crematoria | — | hiaat | Graf ontbreekt in het GGM, terwijl Gemeentebegrafenis er wel naar verwijst (attribuut datumRuimingGraf). Als houder van de gemeentelijke begraafplaats geeft de gemeente graven uit, onderhoudt en ruimt ze (Wet op de lijkbezorging art. 23, 27a, 28, 31); GEMMA kent de Gravenbeheercomponent en de applicatieservice Beheren van grafrechten. Relevante attributen: soort graf (algemeen/particulier), ligging op de begraafplaats, uitgiftetermijn, datum laatste begraving (ruimtermijn tien jaar), en per graf de begraven lijken en bijgezette asbussen met datum (register van begraven lijken, art. 27). Past in een beleidsdomein Begraafplaatsen en crematoria, naast Gemeentebegrafenis. | [graf](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) | open |
| 4 | Begraafplaatsen en crematoria | — | hiaat | Grafrecht (uitsluitend recht op een graf, art. 28) ontbreekt in het GGM. Het recht wordt schriftelijk gevestigd voor onbepaalde tijd of ten minste tien jaar, verlengd en kan vervallen bij verwaarlozing (Wet op de lijkbezorging art. 28); gemeenten heffen er lijkbezorgingsrechten voor. Relevante attributen: rechthebbende, graf, ingangsdatum, looptijd, verlengingen, datum verval. Past in een beleidsdomein Begraafplaatsen en crematoria. | [grafrecht](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafrecht.md) | open |

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
