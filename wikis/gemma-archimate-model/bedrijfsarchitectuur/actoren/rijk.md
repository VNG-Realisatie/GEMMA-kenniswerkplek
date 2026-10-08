---
id: rijk
type: actor
archimate_type: business-actor
status: goedgekeurd
naam: Rijk
onderwerpen:
- algemeen
- burgerzaken
definitie: De Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft.
grondslag: bron
match:
  gemma: exact
data_object: nee
doelgroep: ketenpartners
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rijk-wet-brp-bwbr0033715
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-vng-gemma-2026-10-02
- 2026-rijk-bw2-rechtspersonen
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
gemma_id: id-9f6a80ba-b7fb-4a58-b599-b5f2b33b840e
gemma_naam: Rijk
gemma_type: business-actor
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: 9f6a80ba-b7fb-4a58-b599-b5f2b33b840e
---

# Rijk

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/rijk.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

De Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft.

### Beschrijving

Het Rijk handelt via zijn ministers, die elk een deel van de rijkstaken dragen, en hun diensten. Voor de gemeente gaat het om taken die in de wet naast de gemeentelijke taak staan: de minister van Binnenlandse Zaken en Koninkrijksrelaties (uitgevoerd door de Rijksdienst voor Identiteitsgegevens, RvIG) houdt de niet-ingezetenen bij in de BRP en de voorzieningen daarvoor in stand (Wet BRP art. 1.4 lid 2, 2.64), laat de reisdocumenten maken en houdt de registers van reisdocumenten bij (Paspoortwet art. 2 lid 3–4); de minister van Justitie en Veiligheid (uitgevoerd door de Immigratie- en Naturalisatiedienst, IND) beslist over de naturalisatie (Besluit verkrijging en verlies Nederlanderschap art. 37, 38) en, in de praktijk via Justis, over de afgifte van de verklaring omtrent het gedrag (Wet justitiële en strafvorderlijke gegevens art. 30, 37).

Het model kent het Rijk als één actor, de bestuurslaag als geheel, zoals Gemeente, Provincie en Waterschap; de afzonderlijke ministeries en rijksdiensten staan in de beschrijving en zijn geen eigen element. Waar de gemeente gegevens of registers van het Rijk gebruikt, zijn die invoer. De RDW en het CBR zijn zelfstandige bestuursorganen met een eigen rechtspersoonlijkheid; ze zijn geen eigen element en staan in de beschrijving van Beheren rijbewijzen (Wegenverkeerswet 1994 art. 4a, 4z).

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (kern ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar: de rijksoverheid; in de wetten handelt het Rijk via Onze Minister (Paspoortwet art. 1 onder l, art. 2 lid 3–4; Wet BRP art. 1.4 lid 2; Besluit verkrijging en verlies Nederlanderschap art. 37). GEMMA-actor Rijk. [Paspoortwet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, structurele, wettelijke relatie met elke gemeente: de minister van Justitie en Veiligheid beslist over het naturalisatieverzoek dat de burgemeester met advies toezendt (Besluit verkrijging en verlies Nederlanderschap art. 37), de minister van BZK houdt de niet-ingezetenen bij in de BRP en laat de reisdocumenten maken (Wet BRP art. 1.4 lid 2; Paspoortwet art. 2 lid 3). [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [Paspoortwet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig: de Staat der Nederlanden als bestuurslaag, met eigen organen. [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [BW Boek 2](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, generiek: het Rijk is partij in meer onderwerpen; thuis in Algemeen, zoals Gemeente (regel Thuishoren). [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) |
| **handelende partij**: Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | Ja, een partij die activiteiten uitvoert: beslist over naturalisatie, houdt registers bij en laat documenten maken (Besluit verkrijging en verlies Nederlanderschap art. 37, 38; Paspoortwet art. 2 lid 3). [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Paspoortwet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van elke verantwoordelijkheid in burgerzaken, met eigen taken op vele terreinen. [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) |
| **eigen rechtspersoon**: Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | Ja, de Staat is rechtspersoon (BW Boek 2 art. 1); de ministers zijn zijn organen. [BW Boek 2](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, ketenpartner in Beheren Nederlanderschap: de minister van Justitie en Veiligheid beslist over de naturalisatie (Besluit verkrijging en verlies Nederlanderschap art. 37, 38; besluit redacteur 2026-10-07). [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, de bestuurslaag als geheel, waarmee elke gemeente in dezelfde rol te maken heeft; zo ook Provincie en Waterschap (besluit redacteur 2026-10-07). Afzonderlijke ministeries en rijksdiensten zijn geen eigen actor. [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere actor in deze wiki. [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Rijk | vervult *toewijzing* | [Ketenpartner](../rollen/ketenpartner.md) | [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Wet justitiële en strafvorderlijke gegevens](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 37, 38; Wjsg art. 30, 37) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) | GEMMA-architectuurmodel |
| [BW Boek 2](../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) | Burgerlijk Wetboek Boek 2 Rechtspersonen (BWBR0003045) |
| [Wet justitiële en strafvorderlijke gegevens](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Rijk* (business-actor). GEMMA-actor Rijk (procesarchitectuur, actoren en rollen); zelfde begrip, in GEMMA zonder definitie en zonder relaties. Nieuw: een definitie (besluit redacteur 2026-10-07).

GEMMA-terugmeldingen:

- [Nummer 2](../../analyses/gemma-terugmeldingen.md) (definitie, open): **GEMMA:** de rol Kiezer en de actoren Gemeenteraad, College en Rijk (Procesarchitectuur, Actoren en rollen) hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../../sources/raw/2026-vng-gemma-2026-10-02.md)). Rijk heeft ook geen relaties. **Bevinding:** zonder definitie is niet te zien wat de elementen omvatten. Kiezer is een hoedanigheid (Kieswet art. D 1), de Gemeenteraad vertegenwoordigt de gehele bevolking (Gemeentewet art. 7), het College bestaat uit de burgemeester en de wethouders (Gemeentewet art. 34) en het Rijk is de Staat der Nederlanden als bestuurslaag. De naam College is bovendien niet eenduidig: de wiki noemt het element College van B&W. De wiki-elementen zijn gekoppeld aan deze GEMMA-elementen (exacte match), dus de import van het wiki-model werkt ze bij: de definities komen uit de wiki, en de naam College wordt College van B&W. **Voorstel:** controleer bij de import de definities die de wiki aan GEMMA toevoegt: Kiezer, "hoedanigheid van wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen"; Gemeenteraad, "bestuursorgaan van de gemeente dat de gehele bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt"; College (nieuwe naam College van B&W), "dagelijks bestuur van de gemeente, bestaande uit de burgemeester en de wethouders"; Rijk, "de Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft". Laat het GEMMA-team beslissen of de naam College van B&W en de relaties van het Rijk zo in GEMMA komen.

### Besluiten redacteur

- 2026-10-07: Rijkskant: één actor Rijk met de GEMMA-match, die de rol Ketenpartner vervult; de afzonderlijke ministers en rijksdiensten (minister van BZK met de RvIG, minister van JenV met de IND) staan in de beschrijving. Het Rijk is een soort partij: de bestuurslaag als geheel, waarmee elke gemeente te maken heeft, zoals Provincie en Waterschap.
