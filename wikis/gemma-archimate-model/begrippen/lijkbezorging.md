---
id: lijkbezorging
type: onderwerp
naam: Lijkbezorging
status: afgerond
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-vng-wet-op-de-lijkbezorging
- 2026-vng-retributies
conclusie: '77 begrippen beoordeeld (run 2026-09-29T1123-c482): 56 elementen in 7 Volksgezondheid en Milieu / Begraafplaatsen en crematoria (52 goedgekeurd, 4 kandidaat: graf, grafrecht, register van begraven lijken, lijkbezorgingsrechten), 9 specialisaties of eigenschappen zonder pagina, 8 buiten scope of buiten het model, 4 zonder pagina op besluit van de redacteur (akte van overlijden en retributie verhuizen; beide verordeningen niet als element). Vier GGM-terugmeldingen: definitie en plaatsing van Gemeentebegrafenis, hiaten graf en grafrecht.'
bijgewerkt: '2026-09-29'
---

# Lijkbezorging

## Omschrijving

Wat de gemeente ziet, doet en beslist rond de lijkbezorging: lijkschouw door de gemeentelijke lijkschouwer, de verklaring van overlijden, verlof tot begraven of cremeren, de gemeentelijke begraafplaats met graven en grafrechten, ruiming, en de lijkbezorgingsrechten die de gemeente heft voor het gebruik van begraafplaats of crematorium. Van de VNG-pagina over retributies is alleen de paragraaf over lijkbezorgingsrechten in scope.

## Begrippen


| Begrip | Uitkomst | Reden | Herkomst | GGM |
|---|---|---|---|---|
| [Overlijden](../bedrijfsarchitectuur/bedrijfsgebeurtenissen/overlijden.md) | business-event (review) | Gebeurtenis die de lijkschouwing en de lijkbezorging start | wet | — |
| [Lijk](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/lijk.md) | business-object (review) | Het lijk is het object van alle gedrag in de wet | wet | — |
| Doodgeborene | specialisatie/eigenschap van Lijk | Specialisatie zonder eigen pagina van Lijk | wet | — |
| [Lijkschouwing](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/lijkschouwing.md) | business-process (review) | Gemeentelijk raakvlak via de gemeentelijke lijkschouwer | wet | — |
| [Nader onderzoek naar de doodsoorzaak](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/nader-onderzoek-naar-de-doodsoorzaak.md) | business-process (review) | Proces van de gemeentelijke lijkschouwer bij minderjarigen | wet | — |
| [Gemeentelijke lijkschouwer](../bedrijfsarchitectuur/rollen/gemeentelijke-lijkschouwer.md) | business-role (review) | Rol die een arts vervult na benoeming door B&W | wet | — |
| [Verklaring van overlijden](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verklaring-van-overlijden.md) | business-object (review) | Invoer voor het verlof tot begraving of crematie (afbakening redacteur: blijft in scope) | wet | — |
| [Verklaring van geen bezwaar](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verklaring-van-geen-bezwaar.md) | business-object (review) | Invoer voor het verlof; de afweging van de officier van justitie zelf valt buiten scope | wet | — |
| [Ambtenaar van de burgerlijke stand](../bedrijfsarchitectuur/rollen/ambtenaar-van-de-burgerlijke-stand.md) | business-role (review) | Rol die ook bij het onderwerp burgerlijke stand hoort; hier opgenomen voor het verlof | wet | — |
| [Afgeven verlof tot begraving of crematie](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/afgeven-verlof-tot-begraving-of-crematie.md) | business-process (review) | Gemeentelijk proces rond het verlof | wet | — |
| [Verlof tot begraving of crematie](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlof-tot-begraving-of-crematie.md) | business-object (review) | Kernobject van het gemeentelijke deel | wet | homoniem Verlof (HR) |
| Akte van overlijden | business-object, geen pagina | Element (bedrijfsobject), maar verhuist naar een onderwerp burgerlijke stand; hier niet uitgewerkt | wet | — |
| Termijn van lijkbezorging | buiten het model (Constraint) | Norm, geen element van dit model | wet | — |
| [Besluit andere termijn lijkbezorging](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/besluit-andere-termijn-lijkbezorging.md) | business-object (review) | Eenzijdig besluit van de burgemeester, met eigen beroepsgang | wet | — |
| [Lijkbezorging](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/lijkbezorging.md) | business-process (review) | Generalisatie van begraving, crematie en ontleding | wet | — |
| [Begraving](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraving.md) | business-process (review) | Eigen processen en relaties (graf, begraafplaats): eigen element als specialisatie van lijkbezorging | wet | — |
| [Crematie](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematie.md) | business-process (review) | Eigen processen en relaties (crematorium, as): eigen element als specialisatie van lijkbezorging | wet | — |
| Ontleding | specialisatie/eigenschap van Lijkbezorging | Specialisatie zonder pagina van Lijkbezorging; de uitvoering zelf is medisch-wetenschappelijk (buiten scope) | wet | — |
| [Verlof tot ontleding](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlof-tot-ontleding.md) | business-object (review) | Besluit van de burgemeester | wet | — |
| [Opdrachtgever van de uitvaart](../bedrijfsarchitectuur/rollen/opdrachtgever-van-de-uitvaart.md) | business-role (review) | Rol van de aanvrager van het verlof | wet | — |
| Wilsbeschikking over de lijkbezorging | buiten scope | gemeentelijk: nee | wet | — |
| [Lijkbezorging door de burgemeester](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/lijkbezorging-door-de-burgemeester.md) | business-process (review) | Het vangnetproces | wet | — |
| [Gemeentebegrafenis](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) | business-object (review) | Match GGM Gemeentebegrafenis (EAID_F2DBE01F…) en GEMMA-bedrijfsobject Gemeentebegrafenis | wet | Gemeentebegrafenis (sterk) |
| [Kostenverhaal lijkbezorging](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/kostenverhaal-lijkbezorging.md) | business-process (review) | Deelproces van de lijkbezorging door de burgemeester; Participatiewet § 6 | wet | — |
| [Maatregel bij besmet lijk](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/maatregel-bij-besmet-lijk.md) | business-object (review) | Zeldzaam besluit van de burgemeester | wet | — |
| [Begraafplaats](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | business-object (review) | Generalisatie van gemeentelijke en bijzondere begraafplaats | wet | — |
| Gemeentelijke begraafplaats | specialisatie/eigenschap van Begraafplaats | Specialisatie zonder eigen pagina van Begraafplaats (besluit redacteur) | wet | — |
| Bijzondere begraafplaats | specialisatie/eigenschap van Begraafplaats | Specialisatie zonder eigen pagina van Begraafplaats (besluit redacteur) | wet | — |
| [Houder van de begraafplaats](../bedrijfsarchitectuur/rollen/houder-van-de-begraafplaats.md) | business-role (review) | Rol die de gemeente vervult bij een gemeentelijke begraafplaats; bij een bijzondere begraafplaats is het een externe partij (buiten scope) | wet | — |
| [Graf](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) | business-object (kandidaat) | Kernbegrip | wet | hiaat |
| Algemeen graf | specialisatie/eigenschap van Graf | Specialisatie zonder eigen pagina van Graf | wet | — |
| Particulier graf | specialisatie/eigenschap van Graf | Specialisatie zonder eigen pagina van Graf | wet | — |
| [Grafrecht](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafrecht.md) | contract (kandidaat) | Grafrecht | wet | hiaat |
| [Rechthebbende op het graf](../bedrijfsarchitectuur/rollen/rechthebbende-op-het-graf.md) | business-role (review) | Rol | wet | homoniem Rechthebbende (Archief) |
| [Uitgifte van een graf](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitgifte-van-een-graf.md) | business-process (review) | Kernproces van de begraafplaatsexploitatie; valt onder GEMMA-bedrijfsfunctie Exploiteren van begraafplaatsen | wet | — |
| [Verlenging van het grafrecht](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenging-van-het-grafrecht.md) | business-process (review) | Terugkerend proces rond grafrechten | wet | — |
| [Einde termijn grafrecht](../bedrijfsarchitectuur/bedrijfsgebeurtenissen/einde-termijn-grafrecht.md) | business-event (review) | Gebeurtenis die het verlengingsproces start | wet | — |
| [Einde uitgiftetermijn algemeen graf](../bedrijfsarchitectuur/bedrijfsgebeurtenissen/einde-uitgiftetermijn-algemeen-graf.md) | business-event (review) | Gebeurtenis die mededeling en ruiming start | wet | — |
| [Verklaring van verwaarlozing](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verklaring-van-verwaarlozing.md) | business-object (review) | Besluit van de houder over een particulier graf | wet | — |
| [Register van begraven lijken](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/register-van-begraven-lijken.md) | business-object (kandidaat) | Begraafregister van de gemeentelijke begraafplaats | wet | — |
| [Opgraving](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/opgraving.md) | business-process (review) | Proces op de begraafplaats dat een gemeentelijke vergunning vergt | wet | — |
| [Vergunning tot opgraving](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vergunning-tot-opgraving.md) | business-object (review) | Besluit van de burgemeester | wet | — |
| [Ruimen van graven](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/ruimen-van-graven.md) | business-process (review) | Proces van de houder van de begraafplaats | wet | — |
| [Onderhoud van graven](../bedrijfsarchitectuur/bedrijfsfuncties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/onderhoud-van-graven.md) | business-function (review) | Onderdeel van GEMMA-bedrijfsfunctie Exploiteren van begraafplaatsen | wet | — |
| [Besluit tot sluiting van een begraafplaats](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/besluit-tot-sluiting-van-een-begraafplaats.md) | business-object (review) | Besluit van B&W met beroepsgang en schadeloosstelling (art | wet | — |
| [Aanwijzing van grond voor een bijzondere begraafplaats](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/aanwijzing-van-grond-voor-een-bijzondere-begraafplaats.md) | business-object (review) | Raadsbesluit | wet | — |
| [Toestemming ingebruikneming bijzondere begraafplaats](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/toestemming-ingebruikneming-bijzondere-begraafplaats.md) | business-object (review) | Besluit van B&W over een begraafplaats van een derde | wet | — |
| [Kerkgenootschap](../bedrijfsarchitectuur/actoren/kerkgenootschap.md) | business-actor (review) | Generieke actor met directe samenwerking (art | wet | — |
| [Crematorium](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | business-object (review) | Generalisatie van gemeentelijk en bijzonder crematorium | wet | — |
| Gemeentelijk crematorium | specialisatie/eigenschap van Crematorium | Specialisatie zonder eigen pagina van Crematorium (besluit redacteur) | wet | — |
| Bijzonder crematorium | specialisatie/eigenschap van Crematorium | Specialisatie zonder eigen pagina van Crematorium (besluit redacteur) | wet | — |
| [Vergunning bijzonder crematorium](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vergunning-bijzonder-crematorium.md) | business-object (review) | Besluit van B&W | wet | — |
| [Houder van het crematorium](../bedrijfsarchitectuur/rollen/houder-van-het-crematorium.md) | business-role (review) | Rol; alleen in scope voor zover de gemeente houder is (gemeentelijk crematorium) | wet | — |
| [Asbus](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/asbus.md) | business-object (review) | Urn is gangbaar synoniem (retributies) | wet | — |
| Bestemming van de as | specialisatie/eigenschap van Asbus | Eigenschap van Asbus; bijzetting en verstrooiing worden als eigen processen beoordeeld | wet | — |
| [Bijzetting van een asbus](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzetting-van-een-asbus.md) | business-process (review) | Proces, ook op de gemeentelijke begraafplaats | wet | — |
| [Verstrooiing van as](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verstrooiing-van-as.md) | business-process (review) | Proces | wet | — |
| [Bewaarplaats voor asbussen](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bewaarplaats-voor-asbussen.md) | business-object (review) | Plaats die een gemeentelijke vergunning vergt | wet | — |
| [Vergunning bewaarplaats voor asbussen](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vergunning-bewaarplaats-voor-asbussen.md) | business-object (review) | Besluit van B&W | wet | — |
| [Verstrooiingsterrein](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verstrooiingsterrein.md) | business-object (review) | Plaats die een gemeentelijke vergunning vergt | wet | — |
| [Vergunning verstrooiingsterrein](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vergunning-verstrooiingsterrein.md) | business-object (review) | Besluit van B&W | wet | — |
| Register van gecremeerde lijken | buiten scope | gemeentelijk: nee | wet | — |
| Register van bijgezette asbussen | buiten scope | gemeentelijk: nee | wet | — |
| [Nabestaande](../bedrijfsarchitectuur/rollen/nabestaande.md) | business-role (review) | Rol | wet | — |
| [Burgemeester](../bedrijfsarchitectuur/actoren/burgemeester.md) | business-actor (review) | Generieke actor, ook buiten dit onderwerp | wet | — |
| [Burgemeester en wethouders](../bedrijfsarchitectuur/actoren/burgemeester-en-wethouders.md) | business-actor (review) | Generieke actor | wet | — |
| [Gemeenteraad](../bedrijfsarchitectuur/actoren/gemeenteraad.md) | business-actor (review) | Generieke actor | wet | — |
| [Officier van justitie](../bedrijfsarchitectuur/actoren/officier-van-justitie.md) | business-actor (review) | Externe actor met directe samenwerking; interne afweging buiten scope | wet | — |
| [GGD](../bedrijfsarchitectuur/actoren/ggd.md) | business-actor (review) | Actor met directe samenwerking | wet | — |
| Behandelend arts | buiten scope | gemeentelijk: nee | wet | — |
| Gedeputeerde staten | buiten scope | gemeentelijk: nee | wet | — |
| Beheersverordening begraafplaatsen | business-object, geen pagina | Regeling als geheel (bedrijfsobject volgens de beslistabel); de redacteur besloot op 2026-09-29 haar niet als element op te nemen | wet | — |
| [Lijkbezorgingsrechten](../bedrijfsarchitectuur/bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/lijkbezorgingsrechten.md) | business-object (kandidaat) | Specialisatie van GGM Heffing (RGBZPlus); raakt het onderwerp belastingen | overig | Heffing (zwak) |
| Verordening lijkbezorgingsrechten | business-object, geen pagina | Regeling als geheel (bedrijfsobject volgens de beslistabel); de redacteur besloot op 2026-09-29 haar niet als element op te nemen | overig | — |
| Retributie | business-object, geen pagina | Element (bedrijfsobject), maar verhuist naar een onderwerp belastingen; generalisatie van lijkbezorgingsrechten | overig | — |
| Gemeentelijke dienstverlening rond overlijden | buiten het model (Grouping) | Thema, geen element | overig | — |
| Nieuwe vormen van lijkbezorging | buiten scope | herkenbaar: nee; gemeentelijk: nee | overig | — |

## Open vragen

- Akte van overlijden en aangifte van overlijden horen bij de burgerlijke stand; hier alleen genoemd, uitwerken in een later onderwerp burgerlijke stand (redacteur, 2026-09-29).
- Afbakening (redacteur, 2026-09-29): alleen gemeentelijke raakvlakken van de medische en justitiële stappen; bij bijzondere begraafplaatsen en crematoria alleen de gemeentelijke besluiten, niet de administratie van de externe houder.
