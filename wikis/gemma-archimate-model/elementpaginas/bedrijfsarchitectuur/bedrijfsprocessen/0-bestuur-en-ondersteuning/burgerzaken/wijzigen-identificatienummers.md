---
id: wijzigen-identificatienummers
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Wijzigen identificatienummers
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het wijzigen van het burgerservicenummer of het administratienummer van een ingeschreven persoon.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Wijzigen BSN (HUP)
- Wijzigen A-nummer (HUP)
bronnen:
- 2026-rvig-hup-wijzigen-identificatienummers
- 2026-rvig-hup-wijzigen-bsn
- 2026-rvig-hup-wijzigen-administratienummer
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-van-rechtswege-vervallen-reisdocument
---

# Wijzigen identificatienummers

<!-- Gegenereerd door tools/render.py uit de beoordeling wijzigen-identificatienummers.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het wijzigen van het burgerservicenummer of het administratienummer van een ingeschreven persoon.

### Beschrijving

Het BSN wordt gewijzigd bij een dubbele inschrijving, zodat één juiste persoonslijst overblijft; het college van de bijhoudingsgemeente besluit, weegt de belangen van de persoon af (toeslagen, pensioen) en informeert hem; een geldig reisdocument vervalt dan van rechtswege (HUP Wijzigen BSN). Het A-nummer wordt gewijzigd als meer personen hetzelfde nummer hebben gekregen; de gemeente kent dan nieuwe nummers toe en meldt dat aan de andere gemeenten, de RNI en de BRP-verstrekkingsvoorziening (HUP Wijzigen administratienummer).

### Synoniemen

| Synoniem | Context |
|---|---|
| Wijzigen BSN | HUP |
| Wijzigen A-nummer | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Eindigt in gebeurtenis**: [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [HUP BRP: Wijzigen identificatienummers](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-identificatienummers.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, ambtshalve, van de melding van de dubbele inschrijving of de fout tot het gewijzigde nummer. [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). [HUP BRP: Wijzigen identificatienummers](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-identificatienummers.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een dubbele inschrijving of een foutvermoeden in het Foutenmeldpunt BSN, of meer personen met hetzelfde A-nummer (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [HUP BRP: Wijzigen identificatienummers](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-identificatienummers.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Wijzigen identificatienummers | wijzigt nummer van *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) (regel 19) |
| Wijzigen identificatienummers | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | besluit tot *toewijzing* | Wijzigen identificatienummers | [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) (regel 19-25) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Wijzigen identificatienummers | [HUP BRP: Wijzigen identificatienummers](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-identificatienummers.md) (regel 19) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Wijzigen identificatienummers | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Wijzigen identificatienummers](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-identificatienummers.md) | HUP BRP: Wijzigen identificatienummers |
| [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) | HUP BRP: Wijzigen bsn |
| [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) | HUP BRP: Wijzigen administratienummer |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-15: Leidt tot gebeurtenis is ja: de triggering naar verval-van-het-reisdocument staat met bron en vindplaats in de beoordeling; de nee was een vergissing (omzetting naar de ArchiMate-indeling). *Zekerheid: logica.*
