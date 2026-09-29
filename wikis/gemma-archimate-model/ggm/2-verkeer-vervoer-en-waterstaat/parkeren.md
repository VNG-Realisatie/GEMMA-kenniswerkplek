<!-- gegenereerd door tools/ggm.py; hash: 872675941e44038b822d59700594a755f7f7ac1e679679d9e12585a27342997c -->
# Parkeren

Taakveld: 2 Verkeer, Vervoer en Waterstaat. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Belprovider | `EAID_6C283ABA_C1A3_465b_B267_39E75D06E41F` | Leverancier of dienstverlener van modiele beldiensten | code |
| MulderFeit | `EAID_4EA4D754_FAD7_4caf_8060_342689EC16FE` | Een administratieve overtreding met betrekking tot parkeren, zoals bepaald onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (WAHV), ook wel bekend als de Mulderwet. | bonnummer, overtreding, vorderingnummer, dienstCD, bedrag, parkeertarief, datumBezwaar, bezwaarToegewezen, bezwaarIngetrokken, bezwaarAfgehandeld, datumGeseponeerd, datumBetaling, datumIndiening, redenSeponeren, organisatie |
| Naheffing | `EAID_4957AC99_3F36_4959_A210_9EC6759B87F8` | Het achteraf vorderen van te weinig betaalde belasting | bonnummer, overtreding, vorderingnummer, dienstCD, fiscaal, bedrag, parkeertarief, datumBezwaar, bezwaarToegewezen, bezwaarIngetrokken, bezwaarAfgehandeld, datumGeseponeerd, datumBetaling, datumIndiening, redenSeponeren, organisatie |
| Parkeergarage | `EAID_8F492648_6EF2_4f8a_87C9_2440230D4137` | Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen |  |
| Parkeerrecht | `EAID_9E0936E5_6B50_4205_BA5D_FEB80486D6F1` | Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren. | datumtijdStart, datumtijdEinde, aanmaaktijd, productnaam, productomschrijving, bedragAankoop, bedragBTW |
| Parkeerscan | `EAID_653EEEA7_ED82_427d_BD72_86C847793AD6` | Waarneming van een parkeeractie door een scanauto | transactieID, codeScanvoertuig, codeGebruiker, kenteken, coordinaten, parkeerrecht, tijdstip, foto |
| Parkeervergunning | `EAID_FF448272_AB9D_4ec9_B4BE_E60E2552817A` | Officiele toestemming dat je op een bepaalde plek mag parkeren | nummer, type, datumStart, datumEindeGeldigheid, datumReservering, minutenAfgeschreven, minutenGeldig, minutenResterend, kenteken |
| Parkeervlak | `EAID_5E5C58AD_1634_4656_A183_EBA00F18F30E` | Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen. | vlakID, doelgroep, plaats, coordinaten, fiscaal, aantal |
| Parkeerzone | `EAID_27219A32_3B52_4f54_AA67_A972F4B7D9D0` | Een afgebakend gebied binnen een gemeente waar specifieke parkeerregels en -voorwaarden van toepassing zijn. | geometrie, naam, sectorcode, typeCode, typeNaam, soortCode, IPMCode, IPMNaam, gebruik, aantalParkeervlakken, alleenDagtarief, uurtarief, dagtarief, starttarief, startdag, eindedag, starttijd, eindtijd, isParkeergarage |
| Productgroep | `EAID_209ACADD_34C7_4dc8_90AD_C6B3E092FBFD` | Groepering van producten | code, omschrijving, beslisboom |
| Productsoort | `EAID_1CB4051D_B78A_48f0_AE3E_A98D997A5612` | Typologie van een product | code, omschrijving, tarief, tariefperiode |
| Straatsectie | `EAID_339ACCD5_1D13_4a48_83DE_05A0A4A54C43` | Gedeelte van een straat | code, omschrijving, zoneCode |
| Voertuig | `EAID_6AD98160_FFE6_4105_A724_5D5733C87CD8` | Vervoermiddel bestemd voor het verkeer over wegen | kenteken, merk, kleur, type, land |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Belprovider | Generalization |  | Leverancier |  →  | `EAID_4986CADF_A6F2_4d01_B9B4_BBD2EF132544` |  |
| MulderFeit | Association | betreft voertuig | Voertuig | 0..* → 0..1 | `EAID_D16E2EF9_1913_44f1_8479_F9C3AD43E98F` |  |
| Parkeergarage | Generalization |  | Parkeerzone |  →  | `EAID_4CF50A56_FB68_465b_A8D0_FD6EA0E9753B` |  |
| Parkeerrecht | Association | betreft | Voertuig | 0..* → 1 | `EAID_A1D9E6C1_5A66_4cf7_A381_6BB023BAF9D8` |  |
| Parkeerrecht | Association | betreft | Parkeerzone | 0..* → 1..* | `EAID_DAB8A69C_0150_4f78_80B4_BBDF25BD0734` |  |
| Parkeerrecht | Association | leverancier | Belprovider | 0..* → 0..1 | `EAID_FA794E49_670B_4071_9AB0_16EE0E2BB363` |  |
| Parkeerscan | Association | uitgevoerd door | Medewerker | 0..* → 1 | `EAID_50A13B03_8117_4707_8DB3_8161452B7AEE` |  |
| Parkeerscan | Association | betreft | Voertuig | 0..* → 1 | `EAID_8346683D_99E3_4a0b_A741_2FBE97BE3FA7` |  |
| Parkeerscan | Association | betreft | Parkeervlak | 0..* → 1 | `EAID_8A63FBB4_9361_4b85_A66C_FBD554919BDC` |  |
| Parkeerscan | Association | komt voort uit | Naheffing | 0..1 → 0..1 | `EAID_DFD415FA_8E2B_40c0_ACC5_9FAE27393B25` |  |
| Parkeerscan | Association | verificatie | Parkeerrecht | 0..1 → 0..1 | `EAID_E6B1D422_FC65_4238_A32E_048C78380023` |  |
| Parkeervergunning | Association |  | Ingezetene | -1..* → 1..1 | `EAID_46AF6669_9D59_4e76_8C80_708A791D9650` |  |
| Parkeervergunning | Association | resulteert | Parkeerrecht | 0..1 → 0..1 | `EAID_A9A7708E_526C_41d5_9E5F_48EEAB4E93BD` |  |
| Parkeervergunning | Association | geldig voor | Parkeerzone | 0..* → 1..* | `EAID_C198CD7E_8F34_4925_A08C_5788991A2148` |  |
| Parkeervergunning | Association | houder | Rechtspersoon | 0..* → 1..1 | `EAID_E4ACAF3E_D89D_40d2_BE17_3BBA3AEB554B` |  |
| Parkeerzone | Association | bevat | Parkeervlak | 1..1 → 0..* | `EAID_6D09D9CB_DC86_45d7_A405_29ED9513F0ED` |  |
| Parkeerzone | Association | bevat | Straatsectie | 1..1 → 0..* | `EAID_D0AD7ED8_AC12_423d_AE20_567432B9F842` |  |
| Productgroep | Association | soort | Parkeervergunning | 1 → 0..* | `EAID_0A546271_B26F_46d3_879F_2A9EB756A642` |  |
| Productsoort | Association | soort | Parkeervergunning | 1 → 0..* | `EAID_210DF58C_2B9A_4384_B330_79C2B6CC8280` |  |
| Productsoort | Association | valt binnen | Productgroep | 0..* → 1..1 | `EAID_A7553E9F_B5BC_4bba_8ECA_55ECD6379F2C` |  |
| Straatsectie | Association | bevat | Parkeervlak | 1..1 → 0..* | `EAID_8D39515C_5C16_48dd_84E1_C30F381C17CB` |  |
