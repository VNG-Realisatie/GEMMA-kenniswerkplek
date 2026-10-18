---
id: wijzigen-geslachtsvermelding
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Wijzigen geslachtsvermelding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen van de aangifte van een wijziging van het geslacht en het toevoegen daarvan als latere vermelding aan de geboorteakte.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Geslachtswijziging (HUP)
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen
- 2026-rvig-hup-geslachtswijziging
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-overschrijven-gegevens-bij-geslachtswijziging
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-van-rechtswege-vervallen-reisdocument
---

# Wijzigen geslachtsvermelding

<!-- Gegenereerd door tools/render.py uit de beoordeling wijzigen-geslachtsvermelding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het ontvangen van de aangifte van een wijziging van het geslacht en het toevoegen daarvan als latere vermelding aan de geboorteakte.

### Beschrijving

Aangifte kan een Nederlander van zestien jaar of ouder, of iemand met een verblijfstitel die een jaar in Nederland woont, bij de gemeente van geboorte; bij geboorte in het buitenland bij Den Haag. Alleen van man naar vrouw of omgekeerd; een non-binaire vermelding spreekt de rechter uit (BW 1 art. 28; Utrecht; HUP Geslachtswijziging). Op afspraak aan de balie, gratis (Utrecht).

De woongemeente verwerkt de wijziging in de BRP; een geldig Nederlands reisdocument vervalt van rechtswege. De persoon kan daarna verzoeken de vroegere gegevens te verwijderen of te overschrijven (Wet BRP art. 2.57; HUP Geslachtswijziging; HUP Overschrijven gegevens bij geslachtswijziging).

### Synoniemen

| Synoniem | Context |
|---|---|
| Geslachtswijziging | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een aangifte bij de ambtenaar van de burgerlijke stand die de gemeente verwerkt (BW 1 art. 28).
- **Eindigt in gebeurtenis**: [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geslacht, vermelding aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen.md), [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md) |
| **procesniveau**: bedrijfsproces, kernobject [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | Ja, van de aangifte tot de latere vermelding. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geslacht, vermelding aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen.md), [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geslacht, vermelding aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen.md), [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Aangifte geslachtswijziging gedaan (gebeurtenis, nog geen element): De aangifte van de persoon, met een deskundigenverklaring van hoogstens zes maanden oud (BW 1 art. 28, 28a). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geslacht, vermelding aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen.md), [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Wijzigen geslachtsvermelding | voegt latere vermelding toe aan *toegang (bijwerken)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28b) |
| Wijzigen geslachtsvermelding | realiseert *realisatie* | [Geslachtswijzigingsaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/geslachtswijzigingsaangifte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geslacht, vermelding aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen.md) (UPL nr. 159) |
| Wijzigen geslachtsvermelding | kan leiden tot *triggering* | [Behandelen verzoek om verwijdering van gegevens](behandelen-verzoek-om-verwijdering-van-gegevens.md) | [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md), [HUP BRP: Overschrijven gegevens bij geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overschrijven-gegevens-bij-geslachtswijziging.md) (art. 2.57 Wet BRP) |
| Wijzigen geslachtsvermelding | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Wijzigen geslachtsvermelding | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28) |
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | voegt latere vermelding toe *toewijzing* | Wijzigen geslachtsvermelding | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28b) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Wijzigen geslachtsvermelding | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28b) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Geslacht, vermelding aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geslacht-vermelding-aanpassen.md) | Gemeente Utrecht: Geslachtsregistratie |
| [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md) | HUP BRP: Geslachtswijziging |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP BRP: Overschrijven gegevens bij geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overschrijven-gegevens-bij-geslachtswijziging.md) | HUP BRP: Overschrijven gegevens bij geslachtswijziging |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.

### Besluiten redacteur

- 2026-10-15: Leidt tot gebeurtenis is ja: de triggering naar verval-van-het-reisdocument staat met bron en vindplaats in de beoordeling; de nee was een vergissing (omzetting naar de ArchiMate-indeling). *Zekerheid: logica.*
