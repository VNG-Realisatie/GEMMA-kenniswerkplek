---
id: verval-van-het-reisdocument
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Verval van het reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ongeldig worden van een reisdocument zonder besluit, onder meer door verlopen geldigheid, gewijzigde persoonsgegevens, overlijden of vermissing.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Van rechtswege vervallen (wet)
- Ongeldig worden (beleid)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-van-rechtswege-vervallen-reisdocument
---

# Verval van het reisdocument

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verval-van-het-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het ongeldig worden van een reisdocument zonder besluit, onder meer door verlopen geldigheid, gewijzigde persoonsgegevens, overlijden of vermissing.

### Beschrijving

Een reisdocument vervalt van rechtswege als de houder het Nederlanderschap verliest, de geldigheidsduur verstrijkt, de geslachtsnaam, voornamen, geboortedatum, het geslacht of het burgerservicenummer van de houder wijzigen, de houder overlijdt, het document is ingenomen, bij de aanvraag onjuiste gegevens zijn gebruikt of de houder het als vermist heeft gemeld (Paspoortwet art. 47 lid 1). Ook de intrekking van de verklaring van toestemming kan het document van rechtswege doen vervallen (art. 48).

De bijhoudingsgemeente registreert het verval alleen als het document niet al is ingehouden, ingeleverd of als vermist gemeld, en schrijft de houder aan om het in te leveren; bij overlijden en vermissing komen de gegevens automatisch in het basisregister reisdocumenten (HUP Van rechtswege vervallen). Levert de houder het niet in, dan deelt de burgemeester dat mee aan de minister, die hem in het register paspoortsignaleringen kan vermelden (Paspoortwet art. 47 lid 2; Paspoortbesluit art. 6.1).

### Synoniemen

| Synoniem | Context |
|---|---|
| Van rechtswege vervallen | wet |
| Ongeldig worden | beleid |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Inlevering van het reisdocument](inlevering-van-het-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip verval van rechtswege (Paspoortwet art. 47); de HUP beschrijft de registratie ervan (HUP Van rechtswege vervallen). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de bijhoudingsgemeente registreert het verval en schrijft de houder aan om het document in te leveren (HUP Van rechtswege vervallen). [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: de toestand van het reisdocument verandert (regel Thuishoren). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, het reisdocument wordt ongeldig zonder besluit, op het moment dat een van de gronden zich voordoet (Paspoortwet art. 47 lid 1). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk reisdocument waarvan de geldigheid verloopt of de houder zijn gegevens wijzigt. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, leidt via de inlevering tot Inhouden reisdocument: de houder levert een van rechtswege vervallen reisdocument in en het wordt ingehouden (Paspoortwet art. 54 lid 1 onder a, 56; HUP Van rechtswege vervallen). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verval van het reisdocument | verplicht de houder tot *triggering* | [Inlevering van het reisdocument](inlevering-van-het-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (art. 54 lid 1 onder a, 56) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md) | omvat *aggregatie* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) (art. 47) |
| [Naamswijziging](naamswijziging.md) | doet het reisdocument vervallen *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |
| [Overlijden](overlijden.md) | doet het reisdocument vervallen *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder f; HUP Van rechtswege vervallen) |
| [Verkrijging van het Nederlanderschap](verkrijging-van-het-nederlanderschap.md) | doet een reisdocument voor vluchtelingen of vreemdelingen vervallen *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) (Paspoortwet art. 47 lid 1 onder b) |
| [Verlies van het Nederlanderschap](verlies-van-het-nederlanderschap.md) | doet een Nederlands reisdocument vervallen *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) (Paspoortwet art. 47 lid 1 onder a; HUP Nationaliteit) |
| [Verwerken vermissing reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md) | leidt tot *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) (Paspoortwet art. 47 lid 1 onder j; HUP Inhouding) |
| [Wijzigen geslachtsvermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-geslachtsvermelding.md) | doet het reisdocument vervallen *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |
| [Wijzigen identificatienummers](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-identificatienummers.md) | doet het reisdocument vervallen *triggering* | Verval van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
