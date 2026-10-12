---
id: aanvraag
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Aanvraag
onderwerpen:
- besluitvorming
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Verzoek van een belanghebbende aan een bestuursorgaan om een besluit te nemen.
match:
  ggm: sterk
  gemma: sterk
data_object: nee
objectniveau: generiek
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
ggm_entiteit: Aanvraag
ggm_guid: EAID_2F2A3590_9B34_4ec5_B0AE_B487ED241155
ggm_uml_type: Class
ggm_beleidsdomein: Archief
ggm_taakveld: Erfgoed
ggm_diagram:
- Archief Aanvragen
ggm_diagram_ids:
- EAID_8D468696_4B9D_40b4_92F0_3BED39502098
ggm_definitie: (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.
gemma_id: id-4c995e53fd534fb1895e557ad513c729
gemma_naam: Aanvraag
gemma_type: business-object
gemma_definitie: (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  Alternate name: Aanvraag (Archief)
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-6c992a39-ca0b-4d4c-b749-fe8167af540d
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{2F2A3590-9B34-4ec5-B0AE-B487ED241155}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: 6c992a39-ca0b-4d4c-b749-fe8167af540d
---

# Aanvraag

<!-- Gegenereerd door tools/render.py uit de beoordeling aanvraag.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verzoek van een belanghebbende aan een bestuursorgaan om een besluit te nemen.

### Beschrijving

Een aanvraag is een verzoek van een belanghebbende om een besluit te nemen (Awb art. 1:3 lid 3). Een aanvraag om een beschikking wordt schriftelijk ingediend bij het bevoegde bestuursorgaan, is ondertekend en bevat ten minste naam en adres van de aanvrager, de dagtekening en de gevraagde beschikking, met de gegevens en bescheiden die voor de beslissing nodig zijn (art. 4:1, 4:2). Het bestuursorgaan kan er een formulier voor vaststellen (art. 4:4) en kan een onvolledige aanvraag buiten behandeling laten (art. 4:5). De beschikking volgt binnen de wettelijke termijn, of anders binnen een redelijke termijn van ten hoogste acht weken (art. 4:13).

### Per onderwerp

#### [Burgerzaken](../../../../../onderwerpen/burgerzaken/begrippen.md)

De aanvraag van een reisdocument, rijbewijs of verklaring omtrent het gedrag start het bijbehorende bedrijfsproces; ze is daar een onderdeel van het proces, zonder eigen pagina (Paspoortwet art. 1 onder a).

### Naamkeuze

Aanvraag: de wetsterm (Awb art. 1:3 lid 3) en de gangbare term voor een verzoek aan de gemeente om een besluit. De interne aanvraag (ICT) is een ander begrip en krijgt hier geen pagina (besluit 2026-10-12).

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Aanvraag (GGM-entiteit Aanvraag in ICT (EAID_446E3931_B9F2_4b5c_80E7_5B240B8F816F) en GEMMA-bedrijfsobject Aanvraag (ICT, id-010e27e8116f407e94fdf4665bddf724)) | Interne aanvraag binnen de organisatie, bijvoorbeeld van een medewerker voor een ICT-voorziening; leidt niet tot een besluit in de zin van de Awb | Deze pagina heet Aanvraag: de externe aanvraag volgens de Awb; de interne aanvraag krijgt hier geen pagina. |

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, kernbegrip van de Awb (art. 1:3 lid 3, afdeling 4.1.1) en gangbaar in elk onderwerp: een vergunning of document aanvragen. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, het gemeentelijke bestuursorgaan ontvangt de aanvraag en beslist erop (art. 4:1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig als het verzoek waarop het bestuursorgaan beslist; het is geen onderdeel van het besluit (art. 1:3 lid 3, 4:1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij besluitvorming: de Awb regelt de aanvraag voor elk besluit (afdeling 4.1.1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elke aanvraag heeft een aanvrager, een dagtekening en een gevraagde beschikking (art. 4:2 lid 1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, wordt ingediend, eventueel aangevuld, en eindigt in een besluit of in het niet behandelen ervan (art. 4:1, 4:5, 4:13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, uitvoeren uniforme openbare voorbereidingsprocedure raadpleegt de aanvraag: het ontwerp gaat naar de aanvrager en het besluit volgt binnen zes maanden na ontvangst (art. 3:13, 3:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder object in deze wiki. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt met dezelfde betekenis voor in elk onderwerp waarin de gemeente op verzoek beslist (art. 1:3 lid 3). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

### Specialisaties

- **Aanvraag reisdocument**: Aanvraag van een paspoort of identiteitskaart (Paspoortwet art. 1 onder a); in Burgerzaken een onderdeel van Behandelen aanvraag reisdocument. Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Aanvraag | leidt tot *associatie (gericht)* | [Besluit](besluit.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 3, 4:1); GGM (EAID_1778947E_A0EE_C776_2C1C_281C33036576) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Uitvoeren uniforme openbare voorbereidingsprocedure](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md) | raadpleegt *toegang (raadplegen)* | Aanvraag | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:13, 3:18) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *Aanvraag* (beleidsdomein Archief, taakveld Erfgoed). Zelfde begrip; de GGM-definitie (verzoek aan een bevoegde macht) is algemener dan de Awb, die het verzoek aan een besluit koppelt. Diensten is een duplicaat met een smallere definitie; Aanvraag in ICT is een interne aanvraag en een homoniem.

> (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.

Duplicaten in het GGM:

| Entiteit | Toelichting |
|---|---|
| Aanvraag (Diensten) | Aanvraag in Diensten (Inkomen): ook een externe aanvraag volgens de Awb, met een definitie beperkt tot de Participatiewet en de relatie leidt tot Besluit. |

GGM-terugmeldingen:

- [Nummer 19](../../../../../modellen/ggm/terugmeldingen.md) (homoniem, open): **GGM:** Aanvraag komt voor in drie beleidsdomeinen: Archief (EAID_2F2A3590_9B34_4ec5_B0AE_B487ED241155): "(officieel) verzoek, iets (officieel) vragen aan een bevoegde macht"; een bezoeker doet een aanvraag voor een archiefstuk; ICT (EAID_446E3931_B9F2_4b5c_80E7_5B240B8F816F): dezelfde definitie, zonder relaties; Diensten (EAID_208D605F_BDE5_700A_13F6_281C3303691F): een verzoek om dienstverlening volgens de Participatiewet, dat leidt tot een besluit. **Bevinding:** de aanvraag in Archief en Diensten is een externe aanvraag van een inwoner of bedrijf. Volgens de Algemene wet bestuursrecht is dat een verzoek van een belanghebbende om een besluit te nemen (art. 1:3 lid 3, 4:1). De aanvraag in ICT, een domein van de interne organisatie, is een interne aanvraag, bijvoorbeeld van een medewerker voor een voorziening; die leidt niet tot een besluit. De GEMMA-procesarchitectuur onderscheidt ook processen met externe klanten (van aanvraag tot product) van processen met interne klanten ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), Typen processen; [2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), Klant intern of extern). Gelijke naam en definitie dekken hier dus twee begrippen. **Voorstel:** geef de entiteit in ICT een eigen naam en definitie, bijvoorbeeld Interne aanvraag, en laat de definitie van de externe aanvraag aansluiten op de Awb: verzoek van een belanghebbende aan een bestuursorgaan om een besluit te nemen. Toets bij andere naamgenoten in de domeinen van de interne organisatie (Financiën, HR, ICT, Inkoop, Organisatie, Vastgoed) op dezelfde manier of het om een interne of een externe klant gaat.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Aanvraag* (business-object). Gekoppeld aan dezelfde GGM-entiteit (Archief). Nieuw: een definitie volgens de Awb.

> (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.

GEMMA-terugmeldingen:

- [Nummer 7](../../../../../modellen/gemma/terugmeldingen/gemma-team.md) (element, open): **GEMMA:** de entiteiten van het GGM staan als bedrijfsobjecten in GEMMA, in de map Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten, met eigenschappen die het GGM beheert. Het GGM werkt bewust met duplicaten: hetzelfde begrip als losse entiteit in meer beleidsdomeinen. GEMMA neemt die over als losse bedrijfsobjecten met dezelfde naam, zoals Pand (BAG en RSGB Model) en Aanvraag (Archief en ICT) ([2026-vng-gemma-2026-10-02](../../../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). **Bevinding:** een bedrijfsobject in GEMMA is een begrip, geen gegevensset per beleidsdomein; één begrip hoort één bedrijfsobject te zijn. De wiki koppelt per begrip één GEMMA-object, het object van de GGM-entiteit die zij als primair kiest, en de import werkt alleen dat object bij; de andere blijven ongewijzigd staan, want de import verwijdert niets. Niet elke naamgenoot is een duplicaat: Aanvraag in Archief is de externe aanvraag volgens de Algemene wet bestuursrecht (de wiki koppelt dit object), Aanvraag in ICT een interne aanvraag die niet tot een besluit leidt, een ander begrip ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 1:3 lid 3). De wiki meldt duplicaten daarom niet per geval terug; deze melding geldt voor alle. **Voorstel:** neem per begrip één bedrijfsobject op en voeg de duplicaten daarin samen, het liefst in het object dat de wiki koppelt; geef een naamgenoot die een ander begrip is een onderscheidende naam, zoals Interne aanvraag. Het GGM kan zijn duplicaten houden: de koppeling tussen een bedrijfsobject en de GGM-entiteiten waarop het steunt, kan meer dan één GGM-entiteit omvatten.

### Besluiten redacteur

- 2026-10-12: Aanvraag is de externe aanvraag volgens de Awb: het verzoek van een belanghebbende om een besluit. GGM Archief is de primaire entiteit (met het GEMMA-object Aanvraag van Archief), Diensten een duplicaat. Aanvraag in ICT is een interne aanvraag die niet tot een besluit leidt: een homoniem, met een GGM-terugmelding; het GEMMA-object Aanvraag van ICT blijft ongekoppeld. Duplicaten worden niet per geval teruggemeld.
