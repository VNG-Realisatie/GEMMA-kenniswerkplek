---
id: verval-van-het-grafrecht
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Verval van het grafrecht
onderwerpen:
- lijkbezorging
definitie: Het einde van een grafrecht door verloop van de termijn, afstand, opheffing van de begraafplaats of vervallenverklaring.
grondslag: bron
match:
  gemma: geen
data_object: nee
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
---

# Verval van het grafrecht

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verval-van-het-grafrecht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het einde van een grafrecht door verloop van de termijn, afstand, opheffing van de begraafplaats of vervallenverklaring.

### Beschrijving

Een grafrecht vervalt door het verlopen van de termijn, door afstand of door opheffing van de begraafplaats; het college kan het vervallen verklaren bij niet-betalen, verzuim of als het na overlijden van de rechthebbende niet wordt overgeschreven, en het recht vervalt na een niet opgevolgde verklaring van verwaarlozing (Groningen art. 20; art. 28 lid 6). Daarna kunnen de grafbedekking worden verwijderd en het graf worden geruimd (Groningen art. 20 lid 4, 26).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Kenmerken

Alleen de kenmerken met ja; de overige 37 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar in de verordening ('vervallen van grafrechten', art. 20). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, gevolgen voor de gemeente als houder: ruiming, verwijdering grafbedekking. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, gebeurt op één moment en heeft gevolgen. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij veel graven. [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Ruimen graf (Groningen art. 20 lid 4, 26, 27). [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere gebeurtenis in deze wiki. [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verval van het grafrecht | leidt tot *triggering* | [Ruimen graf](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/ruimen-graf.md) | [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 20 lid 4, 26) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Vervallen verklaren grafrecht](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vervallen-verklaren-grafrecht.md) | leidt tot *triggering* | Verval van het grafrecht | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 28 lid 6; Groningen art. 20) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
