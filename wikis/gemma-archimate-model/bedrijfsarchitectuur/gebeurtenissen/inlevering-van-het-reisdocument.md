---
id: inlevering-van-het-reisdocument
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Inlevering van het reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop een reisdocument bij een tot inhouding bevoegde autoriteit komt, doordat de houder het inlevert of het aan de balie wordt ingenomen.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Inleveren (wet)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-inhouding-inlevering-vermissing
---

# Inlevering van het reisdocument

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/inlevering-van-het-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop een reisdocument bij een tot inhouding bevoegde autoriteit komt, doordat de houder het inlevert of het aan de balie wordt ingenomen.

### Beschrijving

De houder levert zijn oude Nederlandse reisdocumenten in bij de uitreiking van een nieuw document (Paspoortwet art. 32), en een vervallen of teruggevonden vermist document zo spoedig mogelijk bij een tot inhouding bevoegde autoriteit, of op haar verzoek (art. 56; HUP Inhouding). Een document wordt ook ingenomen als het aan de balie beschadigd, onbevoegd gewijzigd of foutief blijkt (art. 54 lid 1).

Inlevering gebeurt op initiatief van de houder, inhouding door een bevoegde autoriteit; een teruggevonden vermist document wordt niet meer teruggegeven (HUP Inhouding). De gemeente registreert de inlevering in de basisregistratie personen.

### Synoniemen

| Synoniem | Context |
|---|---|
| Inleveren | wet |

### Naamkeuze

Voltooide verandering in de vorm van Vermissing van het reisdocument, met de wetsterm inleveren (Paspoortwet art. 56). Was een processtap zonder pagina: Processtap zonder pagina: de houder levert zijn oude Nederlandse reisdocumenten in bij de uitreiking (Paspoortwet art. 32) en een vervallen of teruggevonden document bij een tot inhouding bevoegde autoriteit (art. 56; HUP Inhouding). Vermeld bij Uitreiken reisdocument en Inhouden reisdocument; de gemeente registreert de inlevering in de BRP.

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip inlevering (Paspoortwet art. 32, 56); HUP Inhouding. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente neemt het ingeleverde reisdocument in ontvangst en registreert de inlevering (HUP Inhouding). [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, ja, een eigen moment in de levensloop van het reisdocument, waarna het wordt ingehouden: de houder levert het in, of het blijkt aan de balie vervallen, beschadigd of foutief (Paspoortwet art. 54 lid 1, 56). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, ja, het reisdocument komt bij een tot inhouding bevoegde autoriteit en is niet meer bij de houder (Paspoortwet art. 56; HUP Inhouding). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, ja, bij elk vervallen, teruggevonden, beschadigd of te vervangen reisdocument (Paspoortwet art. 32, 54, 56). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, ja, start Inhouden reisdocument: het ingeleverde document wordt ingehouden en definitief aan het verkeer onttrokken (Paspoortwet art. 54, 56; HUP Inhouding). [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inlevering van het reisdocument | leidt tot *triggering* | [Inhouden reisdocument](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) (Paspoortwet art. 54, 56; HUP Inhouding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md) | omvat *aggregatie* | Inlevering van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) (art. 56) |
| [Verval van het reisdocument](verval-van-het-reisdocument.md) | verplicht de houder tot *triggering* | Inlevering van het reisdocument | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (art. 54 lid 1 onder a, 56) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Inhouding, inlevering of vermissing](../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-08: Nieuwe gebeurtenis Inlevering van het reisdocument (wetsterm, Paspoortwet art. 56), die Inhouden reisdocument triggert, in plaats van het verval van rechtswege; werkt de processtap Inlevering reisdocument bij.
