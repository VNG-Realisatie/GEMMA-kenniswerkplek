---
id: 2026-vng-over-gemma
titel: Over GEMMA (kennismodel en modelleerafspraken)
uitgever: VNG
datum: ''
versie: ''
pad: sources/raw/2026-vng-over-gemma.xml
hash: 2b80d21d844d9415535838dbf61feff156b6875babffc75035f8d2f8b6e21bfb
tags:
- gemma
- archimate
- kennismodel
brontype: overig
beschrijving: 'ArchiMate-model met het GEMMA-kennismodel: de gebruikte elementtypen,
  namen, definities en modelleerafspraken.'
url: https://raw.githubusercontent.com/VNG-Realisatie/Over-GEMMA-Archi-repository/Master/export/Over%20GEMMA.xml
url_pagina: https://github.com/VNG-Realisatie/Over-GEMMA-Archi-repository/blob/Master/export/Over%20GEMMA.xml
opgehaald: '2026-10-01'
---

# Over GEMMA (kennismodel en modelleerafspraken)

## Samenvatting

ArchiMate-model "Over GEMMA" van VNG Realisatie (Archi-repository, export in het Open Exchange-formaat), opgehaald op 1 oktober 2026. Het beschrijft hoe de GEMMA is opgezet: het GEMMA-kennismodel met de gebruikte ArchiMate-elementtypen, hun Nederlandse namen en definities (met herkomst GEMMA, NORA, ArchiMate of Wikipedia) en de toegestane relaties, plus modelleerafspraken per laag (bedrijfsobject, bedrijfsfunctie, bedrijfsproces, product en dienst, motivatie, informatie- en technische architectuur), de procesarchitectuur, de koppeling GEMMA-GGM, de portfolio van GEMMA-producten en de inrichting van repositories en publicatie. De view "GEMMA kennismodel" bevat de typen die GEMMA nu gebruikt; "GEMMA kennismodel uitgebreid" voegt gewenste uitbreidingen toe zoals dienst, product, gebeurtenis en kanaal. De Markdown is een letterlijke weergave per view (elementen, relaties, notities); de diagramopmaak ontbreekt.

## Trefwoorden

kennismodel, metamodel, ArchiMate-conventie, modelleerafspraken, elementtypen, definities, bedrijfslaag, bedrijfsobject, afspraak, contract, product, dienst, deelservice, bedrijfsproces, deelproces, werkproces, processtap, handeling, procescluster, ketenproces, bedrijfsfunctie, gebeurtenis, actor, rol, klant, doelgroep, bedrijfssamenwerking, kanaal, data-object, beleidskader, kwaliteitsdoel, kernwaarde, architectuurprincipe, implicatie, standaard, capability, beleidsdomein, domein, GGM, procesarchitectuur, softwarecatalogus, portfolio

## Begrippen

| Begrip | Regel | Soort |
|---|---|---|
| Bedrijfsobject | 182 | definitie |
| Afspraak (Contract) | 246 | definitie |
| Product | 76 | definitie |
| Dienst | 243 | definitie |
| Deelservice | 385 | definitie |
| Bedrijfsproces | 320 | definitie |
| Procescluster | 409 | regeling |
| Ketenproces | 564 | definitie |
| Deelproces (werkproces) | 388 | definitie |
| Processtap | 387 | definitie |
| Handeling | 412 | definitie |
| Bedrijfsfunctie | 325 | definitie |
| Gebeurtenis | 874 | definitie |
| Actor | 572 | definitie |
| Rol | 569 | definitie |
| Klant (intern of extern) | 567 | definitie |
| Doelgroep | 214 | definitie |
| Bedrijfssamenwerking | 817 | definitie |
| Kanaal | 870 | definitie |
| Data-object | 897 | definitie |
| Beleidskader | 448 | definitie |
| Kwaliteitsdoel | 447 | definitie |
| Architectuurprincipe | 446 | definitie |
| Implicatie | 450 | definitie |
| Standaard | 18 | definitie |
| Capability | 565 | definitie |
| Beleidsdomein | 54 | definitie |
| Domein | 183 | definitie |
| GEMMA kennismodel (view) | 800 | regeling |
| GEMMA kennismodel uitgebreid (view) | 859 | regeling |
| Rol toegewezen aan deelproces | 599 | regeling |
| Rol heeft toegang tot bedrijfsobject | 916 | regeling |

## Verwijst naar

NORA (definities van dienst, kanaal, beleidskader, kwaliteitsdoel en kernwaarde; regel 243, 870, 448), ArchiMate (regel 569, 817), het Gemeentelijk Gegevensmodel (view GEMMA-GGM kennismodel, regel 43; bron-id 2026-vng-ggm-2-5-1), het GEMMA-architectuurmodel (bron-id 2026-vng-gemma-2026-07-01) en de GEMMA Softwarecatalogus (regel 1939).

## Inhoud

Tekst: `sources/raw/2026-vng-over-gemma.md`, 27527 woorden. Regel = regelnummer in die tekst.

| Kop | Regel | Woorden |
|---|---|---|
| Over GEMMA | 1 | 27524 |
| → GEMMA modellering buitengemeentelijk | 7 | 351 |
| → GEMMA-GGM kennismodel | 43 | 191 |
| → GEMMA modellering technische architectuur | 68 | 196 |
| → GEMMA specialisaties applicatiecomponent | 91 | 287 |
| → GEMMA modellering standaardenlijst | 118 | 353 |
| → Procesarchitectuur - Proceshiërarchie specialisatie | 153 | 142 |
| → GEMMA modellering bedrijfsobject | 174 | 162 |
| → GEMMA modellering informatiearchitectuur | 199 | 353 |
| → GEMMA modellering product en service | 233 | 265 |
| → GEMMA modelleerafspraken inheritance | 265 | 417 |
| → GEMMA modellering bedrijfsfunctie | 311 | 291 |
| → GEMMA modellering applicatie-interface | 346 | 248 |
| → Procesarchitectuur - Bouwstenen bedrijfsservices | 378 | 290 |
| → GEMMA modellering bedrijfsproces | 401 | 314 |
| → GEMMA modellering motivatie | 438 | 274 |
| → Procesarchitectuur - Proceshiërarchie samenstelling | 462 | 207 |
| → Motivatie overzicht Kwaliteitsdoelen | 481 | 185 |
| → Motivatie overzicht Kernwaarden | 502 | 185 |
| → Motivatie overzicht Architectuurprincipes | 523 | 185 |
| → Kennismodel procesarchitectuur | 544 | 956 |
| → Samenhang registers | 608 | 379 |
| → Common Ground modellering technische architectuur | 638 | 518 |
| → Common Ground en specialisaties | 678 | 844 |
| → GEMMA kennismodel technologielaag | 731 | 124 |
| → GEMMA kennismodel applicatielaag | 750 | 244 |
| → GEMMA kennismodel strategie en motivatie | 779 | 184 |
| → GEMMA kennismodel | 800 | 745 |
| → GEMMA kennismodel uitgebreid | 859 | 1622 |
| → GEMMA kennismodel bedrijfslaag | 980 | 276 |
| → GEMMA kennismodel uitgebreid (geen titel) | 1009 | 1555 |
| → GEMMA doelgroepen en VNG persona's | 1122 | 418 |
| → GEMMA portfolio indeling | 1179 | 270 |
| → GEMMA portfolio subproducten | 1197 | 1711 |
| → GEMMA portfolio compact | 1272 | 423 |
| → GEMMA portfolio | 1295 | 1190 |
| → KCA portfolio | 1347 | 269 |
| → KCA portfolio standaarden en projecten | 1371 | 1115 |
| → KCA kanalen | 1413 | 318 |
| → Wiki applicatiearchitectuur | 1437 | 681 |
| → GEMMA en Softwarecatalogus | 1483 | 637 |
| → Koppeling wiki en Architectuurtool | 1519 | 339 |
| → Koppeling GEMMA-GGM | 1550 | 398 |
| → Wiki technische architectuur | 1600 | 310 |
| → Koppeling wiki en Softwarecatalogus | 1638 | 773 |
| → Releasen ArchiMate-model | 1690 | 353 |
| → GitHub Archi-repositorie inrichting | 1736 | 368 |
| → Werken met Archi en git | 1769 | 642 |
| → Kenniscentrum architectuur repositories | 1820 | 420 |
| → Begrippen architectuurmodel | 1854 | 235 |
| → Begrippen architectuurmodel voorbeeld | 1890 | 475 |
| → Softwarecatalogus modellering pakketten | 1939 | 1178 |
| → Softwarecatalogus modellering koppelingen | 1987 | 749 |
| → Softwarecatalogus modellering AMEFF-export | 2017 | 1623 |
