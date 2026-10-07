---
id: opmaken-geboorteakte
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Opmaken geboorteakte
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen van de aangifte van een geboorte en het opmaken van de geboorteakte.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: deelproces
afnemer: extern
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-geboorte
---

# Opmaken geboorteakte

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/opmaken-geboorteakte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het ontvangen van de aangifte van een geboorte en het opmaken van de geboorteakte.

### Beschrijving

De aangever doet binnen drie dagen aangifte in de gemeente van geboorte; verplicht is de vader of de moeder uit wie het kind niet is geboren, anders wie bij de bevalling aanwezig was of het hoofd van de instelling. Elektronisch kan alleen de moeder of de andere ouder; de ambtenaar stelt de identiteit vast en controleert de verklaring van arts of verloskundige (BW 1 art. 19e; Besluit burgerlijke stand art. 27; Utrecht). Een te late aangifte meldt hij aan het openbaar ministerie (art. 19e lid 7).

De ambtenaar weigert ongepaste voornamen (BW 1 art. 4). Bij de aangifte kan ook een erkenning of een naamskeuze worden opgenomen. De geboorteakte gaat naar de woongemeente van de moeder, die het kind in de BRP inschrijft (HUP Geboorte; Utrecht).

## Plaats in het model

### Typering

Bedrijfsproces, niveau deelproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: deelproces.
- **Procesindeling naar taak, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een aangifte van een gebeurtenis van de burgerlijke stand die de gemeente verwerkt (BW 1 art. 19e).
- **Gestart door gebeurtenis**: [Geboorte](../../../gebeurtenissen/geboorte.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 45 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, de ambtenaar van de burgerlijke stand van de gemeente van geboorte maakt de akte van geboorte op na aangifte (BW 1 art. 19, 19e; Utrecht). [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, taak van de ambtenaar van de burgerlijke stand van de gemeente (BW 1 art. 19). [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, ambtenaar van de burgerlijke stand; de Aangever doet aangifte, meestal een Ouder (BW 1 art. 19e). [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, registreert de akte van geboorte (BW 1 art. 19). [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de geboorte en de aangifte daarvan, binnen drie dagen (BW 1 art. 19e). [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de geboorteakte; de aangever krijgt een uittreksel (Utrecht). [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, BW 1 art. 4, 5, 19-19e; Besluit burgerlijke stand art. 27, 43-47. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden burgerlijke stand: één akte in het register van geboorten. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst Geboorteaangifte (UPL nr. 136). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Opmaken geboorteakte | maakt geboorteakte op *toegang (registreren)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19) |
| Opmaken geboorteakte | realiseert *realisatie* | [Geboorteaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/geboorteaangifte.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (UPL nr. 136) |
| Opmaken geboorteakte | zendt geboorteakte aan *stroom* | [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | [HUP BRP: Geboorte](../../../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (HUP Geboorte inleiding; Utrecht Na de aangifte) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Opmaken geboorteakte | [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19e) |
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | maakt akte op *toewijzing* | Opmaken geboorteakte | [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Opmaken geboorteakte | [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19, 19e) |
| [Geboorte](../../../gebeurtenissen/geboorte.md) | leidt tot *triggering* | Opmaken geboorteakte | [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |
| [Ouder](../../../rollen/ouder.md) | doet aangifte *toewijzing* | Opmaken geboorteakte | [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Geboorteaangifte doen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |
| [Besluit burgerlijke stand 1994](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP BRP: Geboorte](../../../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md) | HUP BRP: Geboorte |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, open): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern).
