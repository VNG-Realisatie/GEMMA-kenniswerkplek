---
id: gemma-terugmeldingen
type: analyse
titel: GEMMA-terugmeldingen
---

# GEMMA-terugmeldingen

<!-- Gegenereerd door tools/render.py uit beoordelingen/gemma-terugmeldingen.yaml. Wijzig de beoordeling, niet deze pagina. -->

Voorstellen voor het GEMMA-team over het GEMMA-model zelf: elementen die ontbreken, vervallen of herzien moeten worden, en afwijkende indelingen, definities en relaties. De export naar Archi werkt alleen elementen bij die de wiki kent; wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team erover besluit (besluit redacteur 2026-10-08).

## Terugmeldingen

### Element

Een GEMMA-element ontbreekt, hoort te vervallen of moet worden herzien.

| # | Betreft | Bevinding |
|---|---|---|
| 1 open | [Asverstrooiing](../bedrijfsarchitectuur/diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/asverstrooiing.md), Producten- en dienstenrealisatie veiligheidsdomein (GEMMA), Uitvoering openbare orde en veiligheid (GEMMA) | **GEMMA:** de bedrijfsfunctie Producten- en dienstenrealisatie veiligheidsdomein omvat Vergunningenbeheer evenementen, Horeca vergunningverlening en Preventiecampagnes, en valt onder Uitvoering openbare orde en veiligheid, die ook Toezicht en handhaving veiligheidsdomein, Casusregievoering veiligheidsdomein, Beheren openbare orde en veiligheid en Veiligheidsdata-analyse omvat ([2026-vng-gemma-2026-10-02](../../../sources/raw/2026-vng-gemma-2026-10-02.md)). De UPL rekent asverstrooiing tot het domein Openbare orde en veiligheid ([2025-vng-upl-producten-en-diensten-extern](../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 32).<br><br>**Bevinding:** het model geldt voor alle gemeenten en neemt daarom alleen elementen op met een landelijke wettelijke grondslag; een UPL-product zonder die grondslag blijft, maar wordt niet uitgewerkt in processen. Asverstrooiing steunt alleen op de Model-APV (art. 5:36): gemeenten kiezen daarin een variant of laten de bepaling weg ([2023-vng-model-apv](../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-vng-model-apv.md)). In de wiki was het het enige wat deze functies omvatten. Zonder proces om te bedienen vervallen beide functies in de wiki, en staat asverstrooiing onder Exploiteren van begraafplaatsen, bij de andere producten van de lijkbezorging. In GEMMA blijven de functies bestaan: ze omvatten producten en functies die de wiki nog niet heeft beoordeeld. Een deel daarvan steunt, net als asverstrooiing, alleen op de APV (zoals de evenementenvergunning).<br><br>**Voorstel:** neem asverstrooiing in GEMMA op onder Exploiteren van begraafplaatsen. Beoordeel bij een onderwerp Openbare orde en veiligheid per product en functie onder Uitvoering openbare orde en veiligheid of er een landelijke wettelijke grondslag is, en laat functies vervallen die alleen producten zonder die grondslag omvatten. |

### Definitie

De naam of definitie van een GEMMA-element wijkt af of ontbreekt.

| # | Betreft | Bevinding |
|---|---|---|
| 2 open | [Kiezer](../bedrijfsarchitectuur/rollen/kiezer.md), [Gemeenteraad](../bedrijfsarchitectuur/actoren/gemeenteraad.md), [College van B&W](../bedrijfsarchitectuur/actoren/college-van-b-w.md), [Rijk](../bedrijfsarchitectuur/actoren/rijk.md), Kiezer (GEMMA), Gemeenteraad (GEMMA), College (GEMMA), Rijk (GEMMA) | **GEMMA:** de rol Kiezer en de actoren Gemeenteraad, College en Rijk (Procesarchitectuur, Actoren en rollen) hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../sources/raw/2026-vng-gemma-2026-10-02.md)). Rijk heeft ook geen relaties.<br><br>**Bevinding:** zonder definitie is niet te zien wat de elementen omvatten. Kiezer is een hoedanigheid (Kieswet art. D 1), de Gemeenteraad vertegenwoordigt de gehele bevolking (Gemeentewet art. 7), het College bestaat uit de burgemeester en de wethouders (Gemeentewet art. 34) en het Rijk is de Staat der Nederlanden als bestuurslaag. De naam College is bovendien niet eenduidig: de wiki noemt het element College van B&W. De export vult de definities uit de wiki.<br><br>**Voorstel:** neem in GEMMA definities op: Kiezer, "hoedanigheid van wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen"; Gemeenteraad, "bestuursorgaan van de gemeente dat de gehele bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt"; College, "dagelijks bestuur van de gemeente, bestaande uit de burgemeester en de wethouders" onder de naam College van B&W; Rijk, "de Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft", met een relatie naar de rollen die het Rijk vervult. |
| 3 open | [Verblijfplaats](../bedrijfsarchitectuur/bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md), Verblijfplaats (GEMMA) | **GEMMA:** het bedrijfsobject Verblijfplaats is "de locatie waar een persoon feitelijk woont of verblijft", en verwijst naar de GGM-guid {0028CB85-5EF0-45aa-A06F-4A8F14E71AB8} ([2026-vng-gemma-2026-10-02](../../../sources/raw/2026-vng-gemma-2026-10-02.md)).<br><br>**Bevinding:** de definitie dekt het woonadres, niet het briefadres en niet de periode waarin het adres geldt; de BRP kent één categorie Verblijfplaats met woonadres en briefadres als soorten ([2026-rvig-hup-verblijfplaats](../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md); [2025-rvig-logisch-ontwerp-brp-2025q1](../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md)). De GGM-guid komt in het huidige GGM niet meer voor: de entiteit heet VerblijfadresIngeschrevenPersoon (GGM-terugmelding 13).<br><br>**Voorstel:** definieer Verblijfplaats als het adres waar een ingeschreven persoon woont of, zonder woonadres, zijn post ontvangt, met de periode waarin dat adres geldt, en werk de GGM-guid bij na de GGM-terugmelding. |

## Status

open → gemeld → opgelost of afgewezen (met reden).
