<!-- gegenereerd door tools/ggm.py; hash: 93ebc39c1d9b608567ff0a5431102ac6ff2d60aa3db0c3d200af0c8d1359d57c -->
# Parkeren

Taakveld: 2 Verkeer, Vervoer en Waterstaat. Alleen objecttypen; letterlijke definities uit het GGM.

## Belprovider

Leverancier of dienstverlener van modiele beldiensten

Attributen: code.

GUID: `EAID_6C283ABA_C1A3_465b_B267_39E75D06E41F`

Relaties:

- → Leverancier (*Generalization*,  → , `EAID_4986CADF_A6F2_4d01_B9B4_BBD2EF132544`)

## MulderFeit

Een administratieve overtreding met betrekking tot parkeren, zoals bepaald onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (WAHV), ook wel bekend als de Mulderwet.

Attributen: bonnummer, overtreding, vorderingnummer, dienstCD, bedrag, parkeertarief, datumBezwaar, bezwaarToegewezen, bezwaarIngetrokken, bezwaarAfgehandeld, datumGeseponeerd, datumBetaling, datumIndiening, redenSeponeren, organisatie.

GUID: `EAID_4EA4D754_FAD7_4caf_8060_342689EC16FE`

Relaties:

- betreft voertuig → Voertuig (*Association*, 0..* → 0..1, `EAID_D16E2EF9_1913_44f1_8479_F9C3AD43E98F`)

## Naheffing

Het achteraf vorderen van te weinig betaalde belasting

Attributen: bonnummer, overtreding, vorderingnummer, dienstCD, fiscaal, bedrag, parkeertarief, datumBezwaar, bezwaarToegewezen, bezwaarIngetrokken, bezwaarAfgehandeld, datumGeseponeerd, datumBetaling, datumIndiening, redenSeponeren, organisatie.

GUID: `EAID_4957AC99_3F36_4959_A210_9EC6759B87F8`

## Parkeergarage

Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen

GUID: `EAID_8F492648_6EF2_4f8a_87C9_2440230D4137`

Relaties:

- → Parkeerzone (*Generalization*,  → , `EAID_4CF50A56_FB68_465b_A8D0_FD6EA0E9753B`)

## Parkeerrecht

Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren.

Attributen: datumtijdStart, datumtijdEinde, aanmaaktijd, productnaam, productomschrijving, bedragAankoop, bedragBTW.

GUID: `EAID_9E0936E5_6B50_4205_BA5D_FEB80486D6F1`

Relaties:

- leverancier → Belprovider (*Association*, 0..* → 0..1, `EAID_FA794E49_670B_4071_9AB0_16EE0E2BB363`)
- betreft → Parkeerzone (*Association*, 0..* → 1..*, `EAID_DAB8A69C_0150_4f78_80B4_BBDF25BD0734`)
- betreft → Voertuig (*Association*, 0..* → 1, `EAID_A1D9E6C1_5A66_4cf7_A381_6BB023BAF9D8`)

## Parkeerscan

Waarneming van een parkeeractie door een scanauto

Attributen: transactieID, codeScanvoertuig, codeGebruiker, kenteken, coordinaten, parkeerrecht, tijdstip, foto.

GUID: `EAID_653EEEA7_ED82_427d_BD72_86C847793AD6`

Relaties:

- uitgevoerd door → Medewerker (*Association*, 0..* → 1, `EAID_50A13B03_8117_4707_8DB3_8161452B7AEE`)
- komt voort uit → Naheffing (*Association*, 0..1 → 0..1, `EAID_DFD415FA_8E2B_40c0_ACC5_9FAE27393B25`)
- verificatie → Parkeerrecht (*Association*, 0..1 → 0..1, `EAID_E6B1D422_FC65_4238_A32E_048C78380023`)
- betreft → Parkeervlak (*Association*, 0..* → 1, `EAID_8A63FBB4_9361_4b85_A66C_FBD554919BDC`)
- betreft → Voertuig (*Association*, 0..* → 1, `EAID_8346683D_99E3_4a0b_A741_2FBE97BE3FA7`)

## Parkeervergunning

Officiele toestemming dat je op een bepaalde plek mag parkeren

Attributen: nummer, type, datumStart, datumEindeGeldigheid, datumReservering, minutenAfgeschreven, minutenGeldig, minutenResterend, kenteken.

GUID: `EAID_FF448272_AB9D_4ec9_B4BE_E60E2552817A`

Relaties:

- → Ingezetene (*Association*, -1..* → 1..1, `EAID_46AF6669_9D59_4e76_8C80_708A791D9650`)
- resulteert → Parkeerrecht (*Association*, 0..1 → 0..1, `EAID_A9A7708E_526C_41d5_9E5F_48EEAB4E93BD`)
- geldig voor → Parkeerzone (*Association*, 0..* → 1..*, `EAID_C198CD7E_8F34_4925_A08C_5788991A2148`)
- houder → Rechtspersoon (*Association*, 0..* → 1..1, `EAID_E4ACAF3E_D89D_40d2_BE17_3BBA3AEB554B`)

## Parkeervlak

Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen.

Attributen: vlakID, doelgroep, plaats, coordinaten, fiscaal, aantal.

GUID: `EAID_5E5C58AD_1634_4656_A183_EBA00F18F30E`

## Parkeerzone

Een afgebakend gebied binnen een gemeente waar specifieke parkeerregels en -voorwaarden van toepassing zijn.

Attributen: geometrie, naam, sectorcode, typeCode, typeNaam, soortCode, IPMCode, IPMNaam, gebruik, aantalParkeervlakken, alleenDagtarief, uurtarief, dagtarief, starttarief, startdag, eindedag, starttijd, eindtijd, isParkeergarage.

GUID: `EAID_27219A32_3B52_4f54_AA67_A972F4B7D9D0`

Relaties:

- bevat → Parkeervlak (*Association*, 1..1 → 0..*, `EAID_6D09D9CB_DC86_45d7_A405_29ED9513F0ED`)
- bevat → Straatsectie (*Association*, 1..1 → 0..*, `EAID_D0AD7ED8_AC12_423d_AE20_567432B9F842`)

## Productgroep

Groepering van producten

Attributen: code, omschrijving, beslisboom.

GUID: `EAID_209ACADD_34C7_4dc8_90AD_C6B3E092FBFD`

Relaties:

- soort → Parkeervergunning (*Association*, 1 → 0..*, `EAID_0A546271_B26F_46d3_879F_2A9EB756A642`)

## Productsoort

Typologie van een product

Attributen: code, omschrijving, tarief, tariefperiode.

GUID: `EAID_1CB4051D_B78A_48f0_AE3E_A98D997A5612`

Relaties:

- soort → Parkeervergunning (*Association*, 1 → 0..*, `EAID_210DF58C_2B9A_4384_B330_79C2B6CC8280`)
- valt binnen → Productgroep (*Association*, 0..* → 1..1, `EAID_A7553E9F_B5BC_4bba_8ECA_55ECD6379F2C`)

## Straatsectie

Gedeelte van een straat

Attributen: code, omschrijving, zoneCode.

GUID: `EAID_339ACCD5_1D13_4a48_83DE_05A0A4A54C43`

Relaties:

- bevat → Parkeervlak (*Association*, 1..1 → 0..*, `EAID_8D39515C_5C16_48dd_84E1_C30F381C17CB`)

## Voertuig

Vervoermiddel bestemd voor het verkeer over wegen

Attributen: kenteken, merk, kleur, type, land.

GUID: `EAID_6AD98160_FFE6_4105_A724_5D5733C87CD8`
