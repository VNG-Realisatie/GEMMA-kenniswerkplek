---
id: inschrijven-op-briefadres
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Inschrijven op briefadres
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beoordelen van een aangifte van een briefadres en het inschrijven van een persoon zonder woonadres op een briefadres.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Aangifte van een briefadres (HUP)
bronnen:
- 2026-nvvb-beleidsregel-briefadres
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-verblijfplaats
- 2026-rijk-wet-brp-bwbr0033715
---

# Inschrijven op briefadres

<!-- Gegenereerd door tools/render.py uit de beoordeling inschrijven-op-briefadres.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beoordelen van een aangifte van een briefadres en het inschrijven van een persoon zonder woonadres op een briefadres.

### Beschrijving

Een briefadres wordt geregistreerd als iemand geen woonadres heeft, in een aangewezen instelling verblijft of als de burgemeester opneming van het woonadres om veiligheidsredenen niet wenselijk vindt; de briefadresgever stemt schriftelijk in (HUP Verblijfplaats). Het college beoordeelt of de aangifte kan worden ingewilligd en wijst zo nodig een rechtspersoon als briefadresgever aan (HUP Verblijfplaats). Sinds 1 januari 2022 registreert de gemeente iemand zonder woonadres die geen aangifte doet ambtshalve op een briefadres; de NVVB heeft daarvoor een modelregeling met een aanvraagformulier, een toestemmingsverklaring en een beheerregeling (NVVB Beleidsregel briefadres).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aangifte van een briefadres | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Briefadres](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/briefadres.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een aanvraag die het college beoordeelt en honoreert (HUP Verblijfplaats; NVVB Beleidsregel briefadres).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md), [Briefadresgever](../../../rollen/briefadresgever.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Briefadres](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/briefadres.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, aangifte van een briefadres door wie geen woonadres heeft, of ambtshalve als die aangifte uitblijft (HUP Verblijfplaats; NVVB Beleidsregel briefadres). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een inschrijving op een briefadres (HUP Verblijfplaats). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.23, 2.40, 2.41 en 2.45 (UPL nr. 85; HUP Verblijfplaats); gemeentelijke beleidsregel naar het NVVB-model (NVVB Beleidsregel briefadres). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aangifte, of ambtshalve, tot de inschrijving op het briefadres. [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college beoordeelt of de aangifte van een briefadres kan worden ingewilligd (HUP Verblijfplaats). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Briefadres aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/briefadres-aanvragen.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inschrijven op briefadres | legt vast *toegang (registreren)* | [Briefadres](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/briefadres.md) | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.23) |
| Inschrijven op briefadres | realiseert *realisatie* | [Briefadres aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/briefadres-aanvragen.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 85; Wet BRP art. 2.23 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Inschrijven op briefadres | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Inschrijven op briefadres | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Briefadres) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Inschrijven op briefadres | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Briefadres) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Inschrijven op briefadres | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.23) |
| [Briefadresgever](../../../rollen/briefadresgever.md) | stemt in met *toewijzing* | Inschrijven op briefadres | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.23 lid 3, 2.45 lid 2) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Inschrijven op briefadres | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.23, 2.40, 2.41, 2.45) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) | NVVB: Beleidsregel briefadres |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
