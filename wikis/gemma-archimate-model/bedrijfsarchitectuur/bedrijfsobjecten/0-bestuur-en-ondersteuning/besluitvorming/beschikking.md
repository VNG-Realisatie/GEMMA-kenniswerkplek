---
id: beschikking
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Beschikking
onderwerpen:
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Besluit van een bestuursorgaan in een concreet geval, zoals het verlenen van een vergunning.
grondslag: ggm-entiteit
match:
  ggm: sterk
  gemma: sterk
data_object: nee
objectniveau: generiek
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
ggm_entiteit: Beschikking
ggm_guid: EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836
ggm_uml_type: Class
ggm_beleidsdomein: Generiek Jeugd en Wmo
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- 'Sociaal Domein Beschikking en Voorziening: Domain Objects'
- Beperkingen
- AanvraagOfMelding
ggm_diagram_ids:
- EAID_5AE29494_3572_4924_B2B8_3206E55D71BB
- EAID_9B278A50_862A_4085_B362_C41392101916
- EAID_5F3782EB_C416_461c_A9FA_40991A7F0165
ggm_definitie: 'In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.'
gemma_id: id-3d9b45d27b6840b39b99e8ede85db6f4
gemma_naam: Beschikking
gemma_type: business-object
gemma_definitie: 'In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.'
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-c481e8b8-f7d7-4979-b767-ebf2a9b04712
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{71D7E96D-641A-4b6a-A325-DED07C3B5836}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: c481e8b8-f7d7-4979-b767-ebf2a9b04712
---

# Beschikking

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/beschikking.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Besluit van een bestuursorgaan in een concreet geval, zoals het verlenen van een vergunning.

### Beschrijving

Een beschikking is een besluit dat niet van algemene strekking is, met inbegrip van de afwijzing van een aanvraag daarvan (Awb art. 1:3 lid 2). Een toestemming voor een handeling is een vergunning. Het element is generiek en domeinoverstijgend: het hoort niet bij één beleidsdomein (besluit redacteur 2026-09-30).

### Per onderwerp

#### [Lijkbezorging](../../../../begrippen/lijkbezorging.md)

Burgemeester, college en gemeenteraad nemen een reeks beschikkingen die elk een eigen wetsartikel hebben, maar geen eigen gegevens of levenscyclus. Ze zijn specialisaties zonder eigen pagina; de toestemmingen voor een handeling vallen onder Vergunning.

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Specialisaties per onderwerp

#### Lijkbezorging

- **Aanwijzing van grond voor bijzondere begraafplaats**: Specialisatie zonder pagina van Beschikking: aanwijzing door de gemeenteraad (art. 40 lid 1). Genoemd door [Verlenen toestemming bijzondere begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-toestemming-bijzondere-begraafplaats.md).
- **Andere termijn**: Specialisatie zonder pagina van Beschikking: door de burgemeester gestelde afwijkende termijn voor begraving of crematie (art. 17); gangbaar vervroegen of uitstellen van de uitvaart. Genoemd door [Stellen andere termijn](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md).
- **Maatregel bij besmet stoffelijk overschot**: Specialisatie zonder pagina van Beschikking: maatregel van de burgemeester na advies van de GGD (art. 22a); het treffen ervan is het proces Treffen maatregel bij besmet stoffelijk overschot. Genoemd door [Treffen maatregel bij besmet stoffelijk overschot](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md).
- **Sluiting van een begraafplaats**: Specialisatie zonder pagina van Beschikking: besluit van B&W tot sluiting of geslotenverklaring (art. 43, 44). Genoemd door [Sluiten begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/sluiten-begraafplaats.md).
- **Verklaring van verwaarlozing**: Specialisatie zonder pagina van Beschikking: verklaring van de houder dat het onderhoud van een particulier graf kennelijk verwaarloosd is (art. 28 lid 4). Genoemd door [Vervallen verklaren grafrecht](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vervallen-verklaren-grafrecht.md).

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, kernbegrip van de Awb (art. 1:3 lid 2). [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, gemeentelijke bestuursorganen nemen beschikkingen. [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elke beschikking apart. [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, aangevraagd, genomen, bekendgemaakt, in bezwaar, ingetrokken (Awb). [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, vastgelegd in Treffen maatregel bij besmet stoffelijk overschot en Vervallen verklaren grafrecht (Wlb art. 22a, 28 lid 4). [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, specialisatie van Besluit met eigen regels (bezwaar en beroep, aanvraag); eigen GEMMA-element. [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, een beschikking komt in elk onderwerp voor (Awb art. 1:3 lid 2; besluit redacteur 2026-09-30: generiek en domeinoverstijgend). [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

### Specialisaties

- **[Vergunning](vergunning.md)**: Beschikking die toestemming geeft voor een handeling.
- **Aanwijzing van grond voor bijzondere begraafplaats**: Door de gemeenteraad (art. 40 lid 1). Geen eigen pagina.
- **Sluiting van een begraafplaats**: Besluit van B&W tot sluiting of geslotenverklaring (art. 43, 44). Geen eigen pagina.
- **Andere termijn**: Door de burgemeester gestelde afwijkende termijn voor begraving of crematie (art. 17); gangbaar vervroegen of uitstellen van de uitvaart (Ondernemersplein). Geen eigen pagina.
- **Verklaring van verwaarlozing**: Schriftelijke verklaring van de houder dat het onderhoud van een particulier graf kennelijk verwaarloosd is (art. 28 lid 4). Geen eigen pagina.
- **Maatregel bij besmet stoffelijk overschot**: Maatregel van de burgemeester na advies van de GGD (art. 22a). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Beschikking | is een *specialisatie* | [Besluit](besluit.md) | [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Sluiten begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/sluiten-begraafplaats.md) | besluit tot *toegang (registreren)* | Beschikking | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43 lid 2, 44) |
| [Stellen andere termijn](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md) | stelt *toegang (registreren)* | Beschikking | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |
| [Treffen maatregel bij besmet stoffelijk overschot](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md) | treft *toegang (registreren)* | Beschikking | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |
| [Vergunning](vergunning.md) | is een *specialisatie* | Beschikking | [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (Awb art. 1:3 lid 2; Wlb art. 29, 53) |
| [Verlenen toestemming bijzondere begraafplaats](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-toestemming-bijzondere-begraafplaats.md) | wijst aan *toegang (registreren)* | Beschikking | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 40 lid 1) |
| [Vervallen verklaren grafrecht](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vervallen-verklaren-grafrecht.md) | stelt op *toegang (registreren)* | Beschikking | [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 28 lid 4) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *Beschikking* (beleidsdomein Generiek Jeugd en Wmo, taakveld 6 Sociaal Domein). Zelfde bestuursrechtelijke begrip; de GGM-definitie omvat ook de civielrechtelijke beschikking. Geen van de twee GUID's is primair; de GUID van Generiek Jeugd en Wmo blijft de koppeling (besluit redacteur 2026-09-30). Terugmeldingen 5 en 8.

> In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.

Duplicaten in het GGM:

| Entiteit | Toelichting |
|---|---|
| Beschikking (Diensten) | Beschikking in Diensten ('een voor beroep vatbaar overheidsbesluit'); terugmelding 5. |

GGM-terugmeldingen:

- [Nummer 5](../../../../analyses/ggm-terugmeldingen.md) (duplicaat, open): **GGM:** Beschikking komt twee keer voor met verschillende GUID's: Generiek Jeugd en Wmo (EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836, gekoppeld aan GEMMA-bedrijfsobject Beschikking); Diensten (EAID_16ABCFF8_4817_6A73_59BA_281C3303F8D2, 'een voor beroep vatbaar overheidsbesluit'). **Bevinding:** het is hetzelfde bestuursrechtelijke begrip. De definitie van Generiek Jeugd en Wmo omvat ook de civielrechtelijke beschikking (rechterlijke uitspraak). **Voorstel:** samenvoegen tot één generieke entiteit; de civielrechtelijke beschikking kan daarbij beter vervallen.
- [Nummer 8](../../../../analyses/ggm-terugmeldingen.md) (structuur, open): **GGM:** Beschikking staat alleen in de beleidsdomeinen Generiek Jeugd en Wmo en Diensten (zie terugmelding 5), en niet als specialisatie van Besluit. **Bevinding:** Beschikking is een domeinoverstijgend begrip: een besluit dat niet van algemene strekking is (Awb art. 1:3 lid 2). **Voorstel:** één domeinoverstijgende entiteit Beschikking in RGBZPlus (99 Kern), als specialisatie van Besluit, waarnaar de domeinspecifieke beschikkingen verwijzen.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Beschikking* (business-object). Gekoppeld aan dezelfde GGM-entiteit. Nieuw: een herkenbare definitie volgens de Awb.

> In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.

### Besluiten redacteur

- 2026-09-30: Generiek en domeinoverstijgend; de GUID van Generiek Jeugd en Wmo blijft de koppeling zolang het GGM geen domeinoverstijgende entiteit kent.
- 2026-10-05: Specialisatie Maatregel bij besmet lijk heet Maatregel bij besmet stoffelijk overschot.
