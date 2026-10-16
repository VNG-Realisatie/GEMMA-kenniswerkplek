---
id: wijzigen-identificatienummers
type: bedrijfsproces
archimate_type: business-process
status: review
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

**Status: review.** Wacht op het akkoord van de redacteur.

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

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Eindigt in gebeurtenis**: [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een dubbele inschrijving of een foutvermoeden in het Foutenmeldpunt BSN, of meer personen met hetzelfde A-nummer (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een gewijzigd BSN of A-nummer en een geïnformeerde persoon (HUP Wijzigen BSN). [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP BRP: Wijzigen identificatienummers](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP over het BSN en de afweging van belangen; nooit als correctie maar altijd als actualisering (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, ambtshalve, van de melding van de dubbele inschrijving of de fout tot het gewijzigde nummer. [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-administratienummer.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college van de bijhoudingsgemeente besluit tot wijziging van het BSN, na afweging van het belang van de persoon (HUP Wijzigen BSN). [HUP BRP: Wijzigen bsn](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) |
| **leidt tot gebeurtenis**: Eindigt het in een toestandsverandering die domeinexperts benoemen, of die een ander proces start? | Ja, met [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md). |

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
