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
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: deelproces
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

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/wijzigen-identificatienummers.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

Bedrijfsproces, niveau deelproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: deelproces.
- **Procesindeling naar taak, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Eindigt in gebeurtenis**: [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 45 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, begrip uit de HUP (Wijzigen identificatienummers, BSN en administratienummer). [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, het college van de bijhoudingsgemeente wijzigt het BSN; de gemeente kent nieuwe A-nummers toe (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente en Beslisser (college) (HUP Wijzigen BSN). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, werkt de identificatienummers van de ingeschreven persoon en zijn gerelateerden bij (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een dubbele inschrijving of een foutvermoeden in het Foutenmeldpunt BSN, of meer personen met hetzelfde A-nummer (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een gewijzigd BSN of A-nummer en een geïnformeerde persoon (HUP Wijzigen BSN). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md), [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP over het BSN en de afweging van belangen; nooit als correctie maar altijd als actualisering (HUP Wijzigen BSN; HUP Wijzigen administratienummer). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: één mutatie in de persoonslijst (HUP Wijzigen identificatienummers). [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college van de bijhoudingsgemeente besluit tot wijziging van het BSN, na afweging van het belang van de persoon (HUP Wijzigen BSN). [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in deze wiki. [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Wijzigen identificatienummers | wijzigt nummer van *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md), [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) (regel 19) |
| Wijzigen identificatienummers | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md) | [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | besluit tot *toewijzing* | Wijzigen identificatienummers | [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) (regel 19-25) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Wijzigen identificatienummers | [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md) (regel 19) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Wijzigen identificatienummers | [HUP BRP Achtergronden en begrippen](../../../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Wijzigen identificatienummers](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-identificatienummers.md) | HUP BRP: Wijzigen identificatienummers |
| [HUP BRP: Wijzigen bsn](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) | HUP BRP: Wijzigen bsn |
| [HUP BRP: Wijzigen administratienummer](../../../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-administratienummer.md) | HUP BRP: Wijzigen administratienummer |
| [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.
