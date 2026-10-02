<!-- gegenereerd door tools/ggm.py; hash: 42cedd9a6924ef868a837c9008f3c949de452692a954d409e6b537acfd55ead7 -->
# BAG

Taakveld: 99 Kern. Alleen objecttypen; letterlijke definities uit het GGM.

## AdresseerbaarObject

Een adresseerbaar object is een object waaraan formeel adressen kunnen en moeten worden toegekend: een verblijfsobject, standplaats of ligplaats. Toelichting: Een object dat een adres heeft of krijgt. Adresseerbare objecten zijn: een verblijfsobject, een standplaats en een ligplaats.

Attributen: identificatie, versie, typeAdresseerbaarObject.

GUID: `EAID_8A04280B_E0B4_4e36_B448_C99750393D0D`

Relaties:

- Heeft als hoofdadres → Nummeraanduiding (*Association*, 1 → 1, `EAID_99C5ED4C_329B_43db_8A66_590333D7BA35`)
- Heeft als Nevenadres → Nummeraanduiding (*Association*, 1 → 0..*, `EAID_E8F07323_40F0_461d_A545_8C770787F3B2`)
- heeft → Winkelvloeroppervlak (*Association*, 1 → 0..1, `EAID_6303A698_1CF8_4bef_8262_FD5C31CD2912`)
- → Object (*Generalization*,  → , `EAID_EB08C216_8BEA_4377_8A48_A60BCC114A68`)

## BinnenlandsAdres

De adresaanduiding van het WOZ-OBJECT

Attributen: straatnaam, gemeentenaam, huisnummer, huisletter, huisnummertoevoeging, postcode, BAGID.

GUID: `EAID_B7ABBC0B_7686_FEF4_AB14_1E9E649A722C`

## Buurt

Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen.

Attributen: code, naam, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, status, datumEinde, versie, Geconstateerd.

GUID: `EAID_38649FF6_88C6_437d_AF8E_A9023D55E16C`

Relaties:

- ligt in → Wijk (*Association*, 1..* → 1, `EAID_2D684491_7079_4805_AC0F_906DCD61D5E8`): De wijk waarin de buurt is gelegen.

## Gemeente

Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet.

Attributen: gemeentecode, gemeentenaam, gemeentenaam NEN, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, datumEinde, versie, Geconstateerd.

GUID: `EAID_EA6F820F_C458_4b24_8055_5C2CC76F5904`

Relaties:

- is overgegaan in → Gemeente (*Association*, 0..* → 0..*, `EAID_82776B18_BA57_4a96_94B7_564C96D364E5`): De nieuwe GEMEENTE waarin de GEMEENTE bij zijn opheffing c.q. na herindeling is overgegaan.

## Ligplaats

Definitie Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object Beschrijving Een plaats in het water met soms ook een (deel van een) terrein op de oever. Deze plaats moet kunnen worden gebruikt door een drijvend object dat langere tijd daar wordt vastgemaakt. Het drijvende object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Bijvoorbeeld een woonboot. De gemeente mag zeggen of er voor de BAG ergens een ligplaats komt.

Attributen: identificatie, geconstateerd, status, documentdatum, documentnummer, versie, geometrie, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde.

GUID: `EAID_785E3B69_19DA_4952_84A8_592965B9229A`

Relaties:

- is specialisatie van → AdresseerbaarObject (*Generalization*,  → , `EAID_5C7F4009_AC62_4a29_9530_94BCED16B754`)

## Nummeraanduiding

Een nummeraanduiding is een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een verblijfsobject, een standplaats of een ligplaats.

Attributen: huisletter, huisnummer, huisnummertoevoeging, postcode, beginGeldigheid, eindeGeldigheid, status, geconstateerd, identificatie, typeAdresseerbaarObject, datumIngang, datumEinde, versie, geometrie, documentdatum, documentnummer.

GUID: `EAID_32A22BC6_89EC_44af_8D7D_79B12311AE2D`

Relaties:

- Ligt in → Buurt (*Association*, 1 → 1, `EAID_C6631D50_E866_4650_A4E5_464864854E3B`)
- ligt in → Gebied (*Association*, 0..* → 0..*, `EAID_81BDFD99_069C_4922_BE85_483C4B9F23FA`)
- verwijst naar → LocatieaanduidingWozObject (*Association*, 0..1 → 1, `EAID_42CA7FC6_306E_47b1_9490_3A13CA9CAC3F`)
- Ligt aan → OpenbareRuimte (*Association*, 0..* → 1, `EAID_34F0EC28_CB38_4287_9F1F_10F93ADE6DB4`)
- heeft als locatie-adres → Vestiging (*Association*, 1 → 0..*, `EAID_2F6083B5_170E_46af_937A_5A13F67F58E6`): De ADRESSEERBAAR OBJECT AANDUIDING bij het BENOEMD OBJECT waarin de VESTIGING (één van) haar lokatie(s) heeft en die bij inschrijving gekozen is als vestigingssadres.
- Ligt in → Woonplaats (*Association*, 0..* → 0..1, `EAID_FC710755_30A1_4382_ADFC_F6EEAF4DE383`)

## Onderzoek

Basisinformatie zet een kenmerk, waarvan een formele terugmelding of correctieverzoek niet binnen twee werkdagen is afgehandeld, in de Basisregistratie adressen en gebouwen in onderzoek.

Attributen: documentnummer, documentdatum, beginGeldigheid, eindGeldigheid, tijdstipRegistratie, eindRegistratie, identificatie, volgnummer, objecttype, inOnderzoek, datumActueelTot, kenmerk, objectIdentificatie.

GUID: `EAID_5DB3AE05_D225_403e_B376_F163CD463ECF`

Relaties:

- objectidentificatie → Ligplaats (*Association*, 0..1 → 1, `EAID_65C3179E_8A33_40ce_8D45_A54A7607B4F3`)
- objectidentificatie → Nummeraanduiding (*Association*, 0..1 → 1, `EAID_5B3FA5AC_04C1_48ed_8BAD_5C13734EDF0F`)
- objectidentificatie → OpenbareRuimte (*Association*, 0..1 → 1, `EAID_7189D7CE_B76E_48ce_966C_9AB15B106A5F`)
- objectidentificatie → Pand (*Association*, 0..1 → 1, `EAID_1F9E8A7E_8156_4e0a_8DAB_3C10605BFB19`)
- objectidentificatie → Standplaats (*Association*, 0..1 → 1, `EAID_0571314D_3B21_4a0f_91AB_BA987C8740E6`)
- objectidentificatie → Verblijfsobject (*Association*, 0..1 → 1, `EAID_BD54EBE9_8A70_4273_BD74_56753E7757A4`)
- objectidentificatie → Woonplaats (*Association*, 0..1 → 1, `EAID_DF16BEEE_FECB_48d9_B4D1_1F9E4CB9B23C`)

## OpenbareRuimte

Een openbare ruimte is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen. Beschrijving: Een buitenruimte die door de gemeente als openbare ruimte is aangewezen en waaraan de gemeente een naam heeft gegeven. Een openbare ruimte ligt binnen 1 woonplaats. De BAG kent 7 soorten openbare ruimten: weg, water, spoorbaan, terrein, kunstwerk, landschappelijk gebied en administratief gebied. Een openbare ruimte is meestal een straat(naam).

Attributen: identificatie, status, naamOpenbareruimte, geconstateerd, typeOpenbareruimte, straatnaam, Huisnummerrange even nummers, Huisnummerrange oneven nummers, Huisnummerrange even en oneven nummers, labelNaam, geometrie, wegsegment, begingeldigheid, eindGeldigheid, straatcode, versie, datumIngang, datumEinde, documentdatum, documentnummer.

GUID: `EAID_BFE30E32_8CB9_4272_A559_9FB3FD74DACC`

Relaties:

- ligt in → Buurt (*Association*, 1 → 1, `EAID_B29149D6_F8A3_4e94_8A7E_4A63AE9530B4`)
- Ligt in → Buurt (*Association*, 1 → 1..*, `EAID_BE45ABDD_36E0_496a_A91E_00404FBD5BDC`)
- Ligt in → Woonplaats (*Association*, 1..* → 1, `EAID_62D762C1_0619_4436_A35A_37EF3A010BE8`)

## Pand

Een pand is een kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is. Beschrijving: Een zelfstandig bouwwerk, zowel zelfstandig in de manier hoe het is gebouwd als waarvoor het is bedoeld om te gebruiken. Een pand voldoet ook aan de volgende eisen: een pand is direct en voor lange tijd met de aarde verbonden (een pand is niet makkelijk te verplaatsen) en een pand kun je binnengaan en afsluiten. Een eenheid kan alleen een pand zijn als het voldoet aan alle eisen uit de Catalogus BAG 2018.

Attributen: identificatie, status, statusVoortgangBouw, oorspronkelijkBouwjaar, oppervlakte, brutoInhoudPand, geconstateerd, hoogsteBouwlaag, laagsteBouwlaag, geometrieBovenaanzicht, geometrieMaaiveld, relatieveHoogteligging, documentnummer, documentdatum, beginGeldigheid, eindGeldigheid, geometriePunt, datumIngang, versie, datumEinde.

GUID: `EAID_11595AD8_CE67_40dd_BDA9_489DC7D244ED`

Relaties:

- zonder verblijfsobject ligt in → Buurt (*Association*, 0..* → 0..1, `EAID_8C85AD33_E957_4c18_AC13_770D41B51F57`)
- zonder verblijfsobject ligt in → Buurt (*Association*, 0..* → 0..1, `EAID_DD1F44A8_B55B_40e6_A5CB_CC8555D9635D`): De BUURT waarin het PAND gelegen is waarbinnen zich geen verblijfsobjecten bevinden.
- heeft → Vastgoedobject (*Association*, 1 → 1, `EAID_8FC49C86_553F_43d0_A5A3_088421D55DEE`)
- → Geo-Object (*Generalization*,  → , `EAID_FB7E766B_36D8_4dfe_8B51_9CA3B61DD892`)

## Standplaats

Een standplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte. Beschrijving: Een terrein of een deel daarvan dat moet kunnen worden gebruikt om langere tijd een object neer te zetten. Dit object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Het moet verplaatsbaar zijn en mag dus niet helemaal vastgemaakt worden aan de grond. Bijvoorbeeld een woonwagen of strandtent. De gemeente mag zeggen of er voor de BAG ergens een standplaats komt.

Attributen: Identificatie, Geconstateerd, Status, Versie, Geometrie, documentdatum, documentnummer, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde.

GUID: `EAID_86952BDA_ADF6_4ff0_B8C7_BA3AA889A40B`

Relaties:

- is specialisatie van → AdresseerbaarObject (*Generalization*,  → , `EAID_191EBD95_B9FF_4ad2_AD5B_2116F1A010E1`)

## Verblijfsobject

Een verblijfsobject is een kleinste binnen één of meer panden gelegen en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is. Beschrijving: Een verblijfsobject is een ruimte in 1 of meer panden en voldoet aan de volgende eisen: kan worden gebruikt om in te wonen, een bedrijf in te hebben of om voor plezier in te verblijven, is bereikbaar via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, kan worden gekocht en verkocht, kan helemaal zelf worden gebruikt voor het doel dat ervoor is gegeven. Deze eisen voor verblijfsobjecten worden toegelicht in de Catalogus BAG 2018. Een verblijfsobject krijgt een adres.

Attributen: identificatie, status, geconstateerd, hoogsteBouwlaag, laagsteBouwlaag, toegangBouwlaag, soortWoonobject, aantalKamers, ontsluitingVerdieping, documentnummer, documentdatum, geometrie, Versie, gebruiksdoel, beginGeldigheid, eindGeldigheid, datumEinde, datumIngang, oppervlakte.

GUID: `EAID_461EFCF0_E65E_4c7c_B44D_8F36C36FDCE4`

Relaties:

- Maakt deel uit van → Pand (*Association*, 0..* → 1..*, `EAID_03B513CB_774A_4ecf_899B_C168775FBD1C`)
- heeft → Vastgoedobject (*Association*, 1 → 1, `EAID_73B0C853_9BFA_4759_8F5D_C54422F6BCB9`)
- is specialisatie van → AdresseerbaarObject (*Generalization*,  → , `EAID_12BB6081_6817_4985_A5C7_5609A46F7627`)

## Wijk

Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken.

Attributen: wijkcode, wijknaam, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, status, datumEinde, versie, Geconstateerd.

GUID: `EAID_120EA50B_B9A2_4869_A3BE_46931F631D33`

Relaties:

- Ligt in → Woonplaats (*Association*, 1..* → 1, `EAID_B5D02A06_9EDB_422c_A107_D4BDB500D438`)

## Woonplaats

Een woonplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente Beschrijving: Een stuk grond binnen de gemeente dat als woonplaats is aangewezen en waaraan de gemeente ook een naam heeft gegeven.

Attributen: identificatie, woonplaatsnaam, woonplaatsnaamNEN, geconstateerd, status, geometrie, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde, versie, documentnummer, documentdatum, voorkomen, tijdstipRegistratie, eindRegistratie, tijdstipActief.

GUID: `EAID_24BDA4BA_CFCC_4e3f_8305_671F4ED7C502`

Relaties:

- Ligt in → Gemeente (*Association*, 1..* → 1.., `EAID_4D07451D_3D01_44ef_A953_BF6727EB0186`)
