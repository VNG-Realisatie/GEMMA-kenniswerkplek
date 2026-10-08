---
id: gemeentebegrafenis
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Gemeentebegrafenis
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Lijkbezorging waarvoor de gemeente zorgt en betaalt omdat niemand anders daarin voorziet.
grondslag: ggm-entiteit
match:
  ggm: sterk
  gemma: sterk
data_object: ja
objectniveau: kernobject
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
ggm_entiteit: Gemeentebegrafenis
ggm_guid: EAID_F2DBE01F_7535_4f26_9DF2_081EF8632F36
ggm_uml_type: Class
ggm_beleidsdomein: Gemeentebegrafenissen
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Gemeente Begrafenissen
ggm_diagram_ids:
- EAID_949AE9E2_95EB_4063_B7C5_E81971D410B3
ggm_definitie: Teraardebestelling onder verantwoordelijjkheid van de gemeente.
gemma_id: id-68085684cee7413c91bc027a0aaade82
gemma_naam: Gemeentebegrafenis
gemma_type: business-object
gemma_definitie: Teraardebestelling onder verantwoordelijjkheid van de gemeente.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-a0f96391-4935-4c7a-be2b-2fa1b00da57f
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{F2DBE01F-7535-4f26-9DF2-081EF8632F36}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: a0f96391-4935-4c7a-be2b-2fa1b00da57f
---

# Gemeentebegrafenis

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/gemeentebegrafenis.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Lijkbezorging waarvoor de gemeente zorgt en betaalt omdat niemand anders daarin voorziet.

### Beschrijving

Een gemeentebegrafenis is het geval dat ontstaat als de burgemeester de lijkbezorging op zich neemt (art. 21). De gemeente draagt de kosten en verhaalt die zo mogelijk op de nalatenschap, de onderhoudsplichtige verwanten of de werkgever (art. 22). Het GGM legt per geval onder meer de melder, de kosten en de datum van begrafenis en ruiming vast.

## Plaats in het model

### Typering

Bedrijfsobject, niveau kernobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: kernobject.
- **Levensloop bepaald door**: [Verzorgen gemeentebegrafenis](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verzorgen-gemeentebegrafenis.md).
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, GGM-entiteit en gangbare term. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente zorgt en betaalt (art. 21, 22). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per overledene. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, gemeld, uitgevoerd, kosten verhaald (art. 20–22). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, vastgelegd en afgehandeld in Verzorgen gemeentebegrafenis, met kostenverhaal (art. 21, 22). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, GGM-entiteit met attributen (melder, kosten, datum begrafenis en ruiming). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip in deze wiki. [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Gemeentebegrafenis | betreft *associatie (gericht)* | [Stoffelijk overschot](stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Verzorgen gemeentebegrafenis](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verzorgen-gemeentebegrafenis.md) | legt vast en handelt af *toegang (bijwerken)* | Gemeentebegrafenis | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21, 22) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *Gemeentebegrafenis* (beleidsdomein Gemeentebegrafenissen, taakveld 6 Sociaal Domein). Zelfde begrip; de GGM-definitie ('teraardebestelling onder verantwoordelijkheid van de gemeente') is te smal, want de burgemeester kan ook voor crematie zorgen (art. 21); terugmeldingen 1 (definitie) en 2 (scope: beleidsdomein).

> Teraardebestelling onder verantwoordelijjkheid van de gemeente.

GGM-terugmeldingen:

- [Nummer 1](../../../../terugmeldingen/ggm-terugmeldingen.md) (definitie, open): **GGM:** 'Teraardebestelling onder verantwoordelijjkheid van de gemeente'. **Bevinding:** de definitie is te smal. De burgemeester draagt zorg voor de lijkbezorging als niemand daarin voorziet, en dat kan ook crematie zijn; alleen een lijk waarvan de identiteit niet kan worden vastgesteld, wordt begraven (Wet op de lijkbezorging art. 21 lid 1 en 6). Ook tikfout 'verantwoordelijjkheid'. **Voorstel:** 'Lijkbezorging waarvoor de gemeente zorgt en betaalt omdat niemand anders daarin voorziet.'
- [Nummer 2](../../../../terugmeldingen/ggm-terugmeldingen.md) (scope, open): **GGM:** Gemeentebegrafenis staat onder 6 Sociaal Domein. **Bevinding:** de lijkbezorging (graf, grafrecht, begraafplaats, gemeentebegrafenis) hoort bij Iv3-taakveld 7.5 Begraafplaatsen en crematoria (7 Volksgezondheid en Milieu); deze wiki plaatst het element daar. **Voorstel:** een beleidsdomein Begraafplaatsen en crematoria, waarin ook de hiaten graf en grafrecht passen.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Gemeentebegrafenis* (business-object). Overgenomen uit het GGM. Nieuw: een definitie die ook crematie omvat, en plaatsing in beleidsdomein Begraafplaatsen en crematoria.

> Teraardebestelling onder verantwoordelijjkheid van de gemeente.
