---
id: inschrijven-ingezetene
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Inschrijven ingezetene
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het inschrijven van een persoon die zich vanuit het buitenland in de gemeente vestigt als ingezetene in de basisregistratie personen.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: deelproces
afnemer: extern
synoniemen:
- Eerste inschrijving (LO BRP)
bronnen:
- 2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland
- 2026-rvig-hup-immigratie
- 2026-rvig-hup-hervestiging
- 2026-rijk-besluit-brp-bwbr0034306
- 2025-vng-upl-producten-en-diensten-extern
---

# Inschrijven ingezetene

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/inschrijven-ingezetene.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het inschrijven van een persoon die zich vanuit het buitenland in de gemeente vestigt als ingezetene in de basisregistratie personen.

### Beschrijving

Wie zich vanuit het buitenland in de gemeente vestigt, doet uiterlijk de vijfde dag na aanvang van het verblijf in persoon aangifte van verblijf en adres (HUP Immigratie). De gemeente stelt de identiteit vast, toetst de criteria (waaronder rechtmatig verblijf), gaat na of de persoon al in de BRP of RNI voorkomt, verifieert het adres en schrijft de persoon in met een A-nummer en een BSN; binnen vier weken stuurt zij een volledig overzicht van de persoonslijst (HUP Immigratie; Utrecht Inschrijven vanuit het buitenland). Kan de geboortedatum of de vreemde nationaliteit niet uit de gewone bronnen worden ontleend, dan vraagt de gemeente een mededeling ex artikel 2.17 Wet BRP op bij de IND (NVVB mededeling art. 2.17). Ontbreekt een brondocument, dan neemt de gemeente een verklaring onder eed of belofte af (HUP Immigratie; UPL nr. 335).

Bij een hervestiging staat de persoon al in de RNI: de gemeente wordt bijhoudingsgemeente en stelt alle gegevens vast aan de hand van brondocumenten (HUP Hervestiging). Het college beslist over de inschrijving (Besluit BRP art. 24).

### Synoniemen

| Synoniem | Context |
|---|---|
| Eerste inschrijving | LO BRP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau deelproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: deelproces.
- **Procesindeling naar taak, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. De inschrijving volgt op een aangifte van verblijf en adres die de basisregistratie bijwerkt (HUP Immigratie).
- **Gestart door gebeurtenis**: [Vestiging vanuit het buitenland](../../../gebeurtenissen/vestiging-vanuit-het-buitenland.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar als inschrijving of inschrijven vanuit het buitenland (Utrecht; HUP Immigratie: eerste inschrijving). [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente schrijft de persoon in en kent een BSN toe (HUP Immigratie; Utrecht). [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente en Beslisser (college); de Aangever doet de aangifte (HUP Immigratie; HUP Hervestiging). [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, legt de ingeschreven persoon en zijn verblijfplaats vast en raadpleegt akten en andere brondocumenten (HUP Immigratie). [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, aangifte van verblijf en adres, in persoon, uiterlijk de vijfde dag na aanvang van het verblijf (HUP Immigratie). [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een persoonslijst als ingezetene, met A-nummer en BSN, en binnen vier weken een overzicht van de persoonslijst (HUP Immigratie). [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, aangifte binnen vijf dagen in persoon (Besluit BRP art. 30), criterium van rechtmatig verblijf, overzicht binnen vier weken (HUP Immigratie); bij hervestiging vaststellen van alle gegevens aan de hand van brondocumenten (HUP Hervestiging, art. 2.63 lid 3 Wet BRP). [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md), [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: de inschrijving begint de administratieve levensloop (HUP Immigratie). [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college beslist over de inschrijving; bij een vreemdeling zendt het een afschrift van de beslissing aan de korpschef (Besluit BRP art. 24). [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de diensten BRP-inschrijving (UPL nr. 88) en Persoonsgegevens verklaring onder eed of belofte (UPL nr. 335). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in deze wiki. [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inschrijven ingezetene | schrijft in *toegang (registreren)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) (inleiding) |
| Inschrijven ingezetene | legt vast *toegang (registreren)* | [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md) | [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) (Stap 5) |
| Inschrijven ingezetene | ontleent gegevens aan *toegang (raadplegen)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) (Utrecht Wat neemt u mee) |
| Inschrijven ingezetene | realiseert *realisatie* | [BRP-inschrijving](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) (UPL nr. 88) |
| Inschrijven ingezetene | realiseert *realisatie* | [Persoonsgegevens verklaring onder eed of belofte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/persoonsgegevens-verklaring-onder-eed-of-belofte.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) (UPL nr. 335; HUP Immigratie categorie 04) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Inschrijven ingezetene | [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Inschrijven ingezetene | [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) (Besluit BRP art. 24) |
| [Besluit basisregistratie personen](../../../../motivatie/beleidskaders/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Inschrijven ingezetene | [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) (art. 24, 30) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Inschrijven ingezetene | [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) (HUP Immigratie; HUP Hervestiging) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Inschrijven ingezetene | [HUP BRP Achtergronden en begrippen](../../../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| [Vestiging vanuit het buitenland](../../../gebeurtenissen/vestiging-vanuit-het-buitenland.md) | leidt tot *triggering* | Inschrijven ingezetene | [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) (inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Inschrijven vanuit het buitenland](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) | Gemeente Utrecht: Inschrijven vanuit het buitenland |
| [HUP Immigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) | HUP BRP: Immigratie |
| [HUP Hervestiging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) | HUP BRP: Hervestiging |
| [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, open): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern).
