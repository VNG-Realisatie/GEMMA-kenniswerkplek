---
id: nederlanderschap
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Nederlanderschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: De Nederlandse nationaliteit van een persoon, verkregen van rechtswege, door optie of door naturalisatie, tot het verlies ervan.
grondslag: ggm-entiteit
match:
  ggm: sterk
  gemma: geen
data_object: ja
objectniveau: kernobject
synoniemen:
- Nederlandse nationaliteit (beleid)
- NederlandseNationaliteitIngeschrevenPersoon (GGM)
bronnen:
- 2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-nederlandse-nationaliteit
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2026-rvig-hup-nationaliteit
ggm_entiteit: NederlandseNationaliteitIngeschrevenPersoon
ggm_guid: EAID_BA5F2281_466D_4c69_9EB8_D10614C5CD8E
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: 99 Kern
ggm_definitie: Gegevens over de nationaliteit.
---

# Nederlanderschap

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/nederlanderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

De Nederlandse nationaliteit van een persoon, verkregen van rechtswege, door optie of door naturalisatie, tot het verlies ervan.

### Beschrijving

Het Nederlanderschap wordt verkregen van rechtswege (bij geboorte, erkenning of adoptie), door optie of door verlening (naturalisatie), en gaat verloren door het vrijwillig verkrijgen van een andere nationaliteit, door een verklaring van afstand, door langdurig hoofdverblijf buiten het Koninkrijk en de Europese Unie of door intrekking door de minister (Rijkswet op het Nederlanderschap art. 3, 6, 7, 14, 15). Bij optie bevestigt de burgemeester de verkrijging; bij naturalisatie verleent de Koning het Nederlanderschap op voordracht van de minister van Justitie en Veiligheid (art. 6, 7; Besluit verkrijging en verlies Nederlanderschap art. 2, 11).

Het is het kernobject van Beheren Nederlanderschap. Bij optie en naturalisatie ontstaat het pas door de uitreiking van de bevestiging of van het uittreksel van het besluit, met terugwerkende kracht tot de dagtekening, na de verklaring van verbondenheid (Besluit art. 60a, 60b; Utrecht). Of iemand het Nederlanderschap bezit, stelt alleen de rechtbank Den Haag vast (Rijkswet art. 17); bewijs is onder meer een uittreksel uit de basisregistratie personen (Besluit art. 61).

In de basisregistratie personen staat het in categorie 04 Nationaliteit; naast de Nederlandse nationaliteit worden geen vreemde of onbekende nationaliteiten opgenomen (HUP Nederlandse nationaliteit). Wie als Nederlander wordt behandeld zonder het Nederlanderschap te bezitten, staat met de aanduiding bijzonder Nederlanderschap in dezelfde stapel (HUP Bijzonder Nederlanderschap).

### Synoniemen

| Synoniem | Context |
|---|---|
| Nederlandse nationaliteit | beleid |
| NederlandseNationaliteitIngeschrevenPersoon | GGM |

## Plaats in het model

### Typering

Bedrijfsobject, niveau kernobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: kernobject.
- **Levensloop bepaald door**: [Behandelen naturalisatieverzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md), [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md), [Behandelen verklaring van afstand](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verklaring-van-afstand.md), [Behandelen verkrijging en verlies Nederlanderschap](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verkrijging-en-verlies-nederlanderschap.md), [Beheren Nederlanderschap](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md), [Houden naturalisatieceremonie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/houden-naturalisatieceremonie.md).
- **Mutaties door deelprocessen**: [Behandelen naturalisatieverzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md), [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md), [Behandelen verklaring van afstand](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verklaring-van-afstand.md), [Houden naturalisatieceremonie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/houden-naturalisatieceremonie.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, kernbegrip van de Rijkswet op het Nederlanderschap en het Besluit verkrijging en verlies Nederlanderschap; in de praktijk ook de Nederlandse nationaliteit (Rijkswet art. 1, 3; Utrecht). [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de burgemeester neemt optieverklaringen, naturalisatieverzoeken en verklaringen van afstand in ontvangst, bevestigt de optie en reikt de bevestiging en het uittreksel van het naturalisatiebesluit uit (Besluit art. 2, 7, 11, 33, 60a, 60b, 63). [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een rechtsverhouding tussen persoon en Koninkrijk met een eigen begin (verkrijging) en einde (verlies), los van één ander begrip (Rijkswet art. 3 tot en met 16). [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: kernobject van Beheren Nederlanderschap (UPL taakveld 0.2). [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per persoon, met een eigen datum en reden van verkrijging en verlies (HUP Nederlandse nationaliteit). [HUP Nederlandse nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, ontstaat van rechtswege, door optie of door naturalisatie en eindigt door verlies, afstand of intrekking (Rijkswet art. 3, 6, 7, 14, 15). [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, beheren Nederlanderschap registreert en beëindigt het: de burgemeester bevestigt de optie, reikt de bevestiging of het uittreksel uit en neemt de verklaring van afstand in ontvangst; de gemeente neemt het op en beëindigt het in de persoonslijst (Besluit art. 11, 60a, 60b, 63, 64; HUP Nederlandse nationaliteit). [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nederlandse nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, categorie 04 Nationaliteit van de persoonslijst, met de reden van opnemen en beëindigen (HUP Nederlandse nationaliteit; LO BRP 4.4). [HUP Nederlandse nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, specialisatie van Nationaliteit die de gemeente anders behandelt: alleen voor het Nederlanderschap kent zij eigen processen (optie, naturalisatie, afstand) met eigen gegevens (reden van verkrijging en verlies, bijzonder Nederlanderschap); Nationaliteit zelf is een onderdeel van Ingeschreven persoon zonder pagina (Rijkswet; Besluit; HUP Nationaliteit). [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Nederlanderschap | is nationaliteit van *associatie (gericht)* | [Ingeschreven persoon](ingeschreven-persoon.md) | [HUP Nederlandse nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md), [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (HUP Nederlandse nationaliteit; Rijkswet art. 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md) | bevestigt de verkrijging *toegang (registreren)* | Nederlanderschap | [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (art. 6 lid 3) |
| [Behandelen verklaring van afstand](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verklaring-van-afstand.md) | beëindigt door afstand *toegang (beëindigen)* | Nederlanderschap | [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (Rijkswet art. 15 lid 1 onder b; Besluit art. 63) |
| [Behandelen verkrijging en verlies Nederlanderschap](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verkrijging-en-verlies-nederlanderschap.md) | bevestigt, doet in werking treden en beëindigt *toegang (registreren)* | Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 11, 60a, 60b, 63) |
| [Bijhouden persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | neemt de Nederlandse nationaliteit op en beëindigt haar *toegang (bijwerken)* | Nederlanderschap | [HUP Nederlandse nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) (HUP Nederlandse nationaliteit) |
| [Houden naturalisatieceremonie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/houden-naturalisatieceremonie.md) | doet in werking treden *toegang (registreren)* | Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 60a lid 1, 60b lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Rijkswet op het Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [Utrecht Nederlander worden](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) | Gemeente Utrecht: Nederlander worden door naturalisatie of optie |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP Nederlandse nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) | HUP BRP: Nederlandse nationaliteit |
| [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [HUP Nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) | HUP BRP: Nationaliteit |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *NederlandseNationaliteitIngeschrevenPersoon* (beleidsdomein RSGBPlus, taakveld 99 Kern). GGM-entiteit NederlandseNationaliteitIngeschrevenPersoon (RSGBPlus), met de reden van verkrijging en verlies van de Nederlandse nationaliteit en de aanduiding bijzonder Nederlanderschap: zelfde begrip, maar de definitie 'Gegevens over de nationaliteit' noemt het Nederlanderschap niet (GGM-terugmelding 15). De bredere entiteit Nationaliteit (EAID_69B41CDD_C3F1_449b_92B4_8F7657840646) blijft de match van het onderdeel Nationaliteit; het GGM legt de nationaliteit in vier entiteiten vast (GGM-terugmelding 16).

> Gegevens over de nationaliteit.

GGM-terugmeldingen:

- [Nummer 15](../../../../analyses/ggm-terugmeldingen.md) (definitie, open): **GGM:** NederlandseNationaliteitIngeschrevenPersoon heeft de definitie 'Gegevens over de nationaliteit.', met de attributen aanduidingBijzonderNederlanderschap, redenVerkrijgingNederlandseNationaliteit, redenVerliesNederlandseNationaliteit en nationaliteit. **Bevinding:** de entiteit gaat over het Nederlanderschap: de Nederlandse nationaliteit, verkregen van rechtswege, door optie of door verlening, en verloren door onder meer afstand ([2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738](../../../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), art. 3-7, 15; [2026-rvig-hup-nederlandse-nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md)). De definitie onderscheidt haar niet van de andere entiteiten voor de nationaliteit. **Voorstel:** 'De Nederlandse nationaliteit van een persoon, verkregen van rechtswege, door optie of door naturalisatie, tot het verlies ervan.', en de naam Nederlanderschap overwegen.
- [Nummer 16](../../../../analyses/ggm-terugmeldingen.md) (structuur, open): **GGM:** de nationaliteit staat in vier entiteiten in RSGBPlus: Nationaliteit (EAID_69B41CDD_C3F1_449b_92B4_8F7657840646), de rechtsverhouding, met redenen van verkrijging en verlies; Nationaliteit (EAID_71B3BE0D_2BF9_4740_9597_A0EEC75AFE9B), met dezelfde definitie maar met code, omschrijving en geldigheid: de referentielijst van nationaliteiten (in GEMMA de groepering Referentielijsten); NationaliteitIngeschrevenNatuurlijkPersoon (EAID_261B509E_6879_4475_B5F8_77E8428816CE), met reden verkrijging en verlies en buitenlands persoonsnummer; NederlandseNationaliteitIngeschrevenPersoon (EAID_BA5F2281_466D_4c69_9EB8_D10614C5CD8E), met de redenen voor de Nederlandse nationaliteit en de aanduiding bijzonder Nederlanderschap. **Bevinding:** de BRP kent één gegevensgroep nationaliteit per persoon, met de Nederlandse, vreemde en onbekende nationaliteit en staatloosheid als soorten, en het bijzonder Nederlanderschap in dezelfde stapel als de Nederlandse ([2026-rvig-hup-nationaliteit](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md)). Twee entiteiten met dezelfde naam en definitie voor een ander begrip (rechtsverhouding en referentielijst) zijn een homoniem; de reden van verkrijging en verlies staat drie keer. **Voorstel:** één entiteit Nationaliteit voor de rechtsverhouding, met Nederlanderschap als specialisatie; de referentielijst een eigen naam geven (bijvoorbeeld Nationaliteitentabel); de mGBA-entiteiten daarop afbeelden.

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen bedrijfsobject voor het Nederlanderschap; de GEMMA-bedrijfsobjecten Nationaliteit (RSGB Model en Referentielijsten) zijn breder of de referentielijst. Nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-07: Naam Nederlanderschap blijft (wetsterm en term van het besluit van 2026-10-07), met Nederlandse nationaliteit als synoniem (beleid).
