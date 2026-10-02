<!-- gegenereerd door tools/ggm.py; hash: bf1deaa1094d5222cdd827ce30603d5024f55ab07c9306be0beae73b47383676 -->
# Musea

Taakveld: 5 Sport, Cultuur en Recreatie. Alleen objecttypen; letterlijke definities uit het GGM.

## Activiteit

Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd.

Attributen: naam, omschrijving, aantalPersonen.

GUID: `EAID_A1C60F39_3074_4d1c_A37D_5F431F54DF92`

Relaties:

- bestaat uit → Activiteit (*Aggregation (shared)*, 1 → 0..*, `EAID_0EAACDC5_5694_4aa0_BEA7_F58A3CE9D73E`)
- van soort → Activiteitsoort (*Association*, 0..* → 1, `EAID_12BB2067_E3D9_416f_B77E_857C1AC23F7E`)
- heeft → Reservering (*Association*, 1..1 → 0..*, `EAID_228716A3_A8CB_429c_9478_21776C4D879F`)
- heeft → Rondleiding (*Association*, 0..* → 0..1, `EAID_0BF396DC_084B_4d64_8ED0_B60488A68871`)

## Activiteitsoort

Typering van een activiteit

Attributen: naam, omschrijving.

GUID: `EAID_D77AB8CF_E4B1_49fd_BE78_FE358FF76F13`

## Balieverkoop

Verkoop aan de balie

Attributen: verkooptijd, kanaal, aantal.

GUID: `EAID_EA2D32A2_5ED5_45c8_AC33_57C35981B3BC`

Relaties:

- tegen prijs → Prijs (*Association*, 0..* → 1, `EAID_D8CF5F7C_897F_4af8_B199_A0F5127C1236`)
- betreft → Product (*Association*, 0..* → 1, `EAID_F611E8C6_E0AB_4e4d_8CAD_C5E73A0F99C6`)

## Balieverkoop Entreekaart

Verkoop van een entreekaart aan de balie

Attributen: rondleiding, datumStart, datumEindeGeldigheid, gebruiktOp.

GUID: `EAID_90E24064_EBB7_4ffc_9640_F7C31678899F`

Relaties:

- → Balieverkoop (*Generalization*,  → , `EAID_623D1015_E0FF_4858_80FB_BDBF4B8EFF46`)

## Belanghebbende

Een persoon wiens belang rechtstreeks bij een besluit is betrokken.

Attributen: datumStart, datumTot.

GUID: `EAID_576642BA_9AF9_42fc_831A_F9D3138F20FC`

Relaties:

- → Rechtspersoon (*Generalization*,  → , `EAID_9D7F10C6_C706_4e62_875C_6FF5ECF460E8`)

## Bruikleen

Lening voor tijdelijk gebruik

Attributen: datumAanvraag, datumStart, datumEinde, aanvraagDoor, toestemmingDoor.

GUID: `EAID_452312FD_05FB_4abc_A48B_C605F7E3E193`

Relaties:

- is bedoeld voor → Tentoonstelling (*Association*, 0..* → 0..*, `EAID_AF0D1D06_F235_46c9_B49F_3ECC8618A332`)

## Collectie

Een verzameling van verworven voorwerpen die is samengesteld op grond van vastgestelde criteria.

Attributen: naam, omschrijving.

GUID: `EAID_6DC28A18_DF54_4b92_A592_5F717935CA67`

Relaties:

- bevat → Museumobject (*Association*, 0..* → 0..*, `EAID_85886C93_0900_42d4_8F6E_B6E36EE34BF8`)

## Doelgroep

Een groep mensen of klanten die een bedrijf of organisatie wil benaderen om een product, dienst of informatie onder de aandacht te brengen

Attributen: naam, omschrijving, branch, segment.

GUID: `EAID_0598561F_667E_4926_9BF5_66A928358E9F`

Relaties:

- bestaat uit → Doelgroep (*Aggregation (shared)*, 1 → 0..*, `EAID_D52C6261_341D_4891_993E_5A4CD1463033`)

## Entreekaart

Bewijs van toegang tot een gebouw of voorstelling

Attributen: rondleiding.

GUID: `EAID_E46CB962_A2BC_4656_A0C1_D7DBCCA0C528`

Relaties:

- → Product (*Generalization*,  → , `EAID_390CE5AC_9D1B_4dc6_A047_A464FDADFB84`)

## Incident

Niet-gepland(e) gebeurtenis die of voorval dat tot schade of verlies leidt

Attributen: naam, omschrijving, datum, locatie.

GUID: `EAID_CE85A5E9_AD75_40e7_8EBF_A484E4CBEEDC`

Relaties:

- betreft → Museumobject (*Association*, 0..* → 0..*, `EAID_73A00EBA_0891_4667_8046_57353BBB1539`)

## Lener

Iemand die iets te leen krijgt, met name iemand die boeken, digitale bestanden of apparatuur leent bij een museum, bibliotheek, mediatheek of een andere uitleeninstantie

Attributen: opmerkingen.

GUID: `EAID_68C42EEA_6985_483e_99E6_E0F1FB71D622`

Relaties:

- is → Bruikleen (*Association*, 1..* → 0..*, `EAID_0BC7385F_11F7_4e77_817A_74BF0E915274`)
- → Rechtspersoon (*Generalization*,  → , `EAID_BC9D9001_3F43_4652_BF4E_A4261D11DC50`)

## Mailing

Per post verstuurde inhoud

Attributen: naam, omschrijving, datum.

GUID: `EAID_48BCF2C2_609C_4e4c_991E_8BDA80E0C7C7`

Relaties:

- versturen aan → Museumrelatie (*Association*, 0..* → 0..*, `EAID_B8349E63_0501_4706_92CB_33056A09E646`)

## Museumobject

Beschrijving van een fenomeen in de werkelijkheid met een zekere cultuurhistorische waarde die deel uitmaakt van de culthuurhistorisch object index. Een museum object kan gedifiniëerd worden als een object met betrekking tot gebouwd, archeologisch, roerend of cultuurlandschappelijk erfgoed. Denk hierbij bijvoorbeeld aan een gebouwd of archeologisch rijksmonument, een schilderij of een beschermd stads- of dorpsgezicht.

Attributen: verkrijging, medium, afmeting, bezitVanaf, bezitTot.

GUID: `EAID_BBCF9DBE_70AD_431c_B698_7F0D69D07050`

Relaties:

- heeft → Belanghebbende (*Association*, 0..* → 0..*, `EAID_C1681AE0_B792_4bdb_B52E_16F7E28788E5`)
- betreft → Bruikleen (*Association*, 0..* → 0..1, `EAID_F84FAC06_CCCA_41b9_A510_916928881915`): In TMS loopt dit via LoanObjRefs
- heeft verbinding → Historisch Persoon (*Association*, 0..* → 0..*, `EAID_3E839A6C_553C_4d8f_9E43_AEFAB5959C2C`)
- locatie → Standplaats (*Association*, 0..* → 0..1, `EAID_F9228738_BF54_4296_BB71_7C509671C3D4`)
- onderdeel → Tentoonstelling (*Association*, 0..* → 0..*, `EAID_DE8C34A9_EA94_4c24_825D_C8C6D33AF4F5`)
- → Erfgoed Object (*Generalization*,  → , `EAID_10AE8788_4EA4_4f44_BA5D_96DC180DBA48`)

## Museumrelatie

Betrekking waarin het museum en personen tot elkaar staan

Attributen: relatiesoort.

GUID: `EAID_C73389B7_7BCD_4496_888B_6ABEE9DE01FB`

Relaties:

- valt binnen → Doelgroep (*Association*, 0..* → 0..*, `EAID_49D9A171_E6B2_45f7_9F9B_2E834A96EABF`)
- voor → Programma (*Association*, 1 → 0..*, `EAID_E2DB2551_BF37_4cf6_AAFB_7E4C84455BDD`)
- → Rechtspersoon (*Generalization*,  → , `EAID_E51FCBB9_D6DB_449c_B425_CFC01AE8C74E`)

## Omzetgroep

Artikelen worden gebruikt om omzet te registreren in de shop, de horeca of elders. De omzet wordt vervolgens getotaliseerd op rapportages. Om de artikelen te groeperen moet ieder artikel tot een omzetgroep behoren.

Attributen: naam, omschrijving.

GUID: `EAID_2A7D73D7_87EA_4b61_88BB_F061DDBF52D9`

## Prijs

De te betalen hoeveelheid geld

Attributen: bedrag, datumStart, datumEindeGeldigheid.

GUID: `EAID_BF7BAB5F_7025_4792_8288_47F5B1C53E95`

## Product

Het resultaat van een proces dat in het economisch verkeer een waarde bezit.

Attributen: omschrijving, prijs, datumStart, datumEindeGeldigheid, codeMuseumjaarkaart, entreekaart.

GUID: `EAID_FF566C6B_077B_4914_8AF7_40EB1EDD388A`

Relaties:

- leverancier → Leverancier (*Association*, 0..* → 0..1, `EAID_D68DAC72_0E04_4516_86B4_F3287714B891`)
- valt binnen → Omzetgroep (*Association*, 0..* → 0..*, `EAID_53371D60_C96C_4429_9C69_0ABB37C36838`)
- heeft prijs → Prijs (*Association*, 1 → 1..*, `EAID_298B2001_22B7_4eb0_BD63_2A58F87B3699`)
- valt binnen → Productgroep (*Association*, 0..* → 0..*, `EAID_50AA9F5C_F1FB_48cb_8D23_75AA9A14FA93`)

## Productgroep

Groepering van producten

Attributen: naam, omschrijving.

GUID: `EAID_42EBA101_3E51_46d5_A234_EC7BA991D3AF`

## Productie-eenheid

Een (deel van een) productiemiddel, dat zelfstandig (ofwel onafhankelijk van de andere delen van het desbetreffende productiemiddel) kan worden ingezet.

GUID: `EAID_D3EF17C3_8100_4a61_9E67_F20924C15CEA`

Relaties:

- betreft → Leverancier (*Association*, 0..* → 0..1, `EAID_04CEF004_3C07_4fe1_A1D0_41A5C8653C15`)

## Programma

Een tijdelijke, flexibele organisatiestructuur, die is opgezet om de implementatie van een verzameling met elkaar samenhangende projecten en activiteiten te coördineren, te sturen en te controleren teneinde te zorgen voor de realisatie van de eindresultaten en benefits die zijn gerelateerd aan de strategische doelstellingen van de organisatie.

Attributen: naam, omschrijving, starttijd, eindtijd, prijsExclusiefBTW, BTW, locatie, publiekstaak, schoolniveau.

GUID: `EAID_3B84D5F0_FCA3_47a5_B90C_F0834DAD6EBD`

Relaties:

- bestaat uit → Activiteit (*Aggregation (shared)*, 1 → 0..*, `EAID_5B1D060B_642D_4cef_9F62_6A1C89037F10`)
- heeft → Kostenplaats (*Association*, 0..* → 1, `EAID_E4131B79_73B1_4c98_9B5E_3663B17719CC`)
- voor → Programmasoort (*Association*, 0..* → 0..*, `EAID_AC9BCED2_3C4A_40b8_A069_97B0D868A302`)

## Programmasoort

Typering van een programma

Attributen: naam, omschrijving.

GUID: `EAID_43EF5733_B976_4f21_9906_5349FD861BB5`

## Reservering

Het vooraf bespreken van een plaats in een openbare gelegenheid, vervoermiddel, restaurant e.d.

Attributen: aantal, tijdVanaf, tijdTot, totaalprijs, BTW.

GUID: `EAID_11AB7925_5C96_4615_92F6_4055935221A0`

Relaties:

- betreft → Productie-eenheid (*Association*, 0..* → 0..1, `EAID_70909C72_21BC_44a6_A6C3_CC828D1E3045`)
- betreft → Voorziening (*Association*, 0..* → 0..1, `EAID_0514D2FD_B8CB_4b05_87FC_EFDB851FCA0B`)
- betreft → Zaal (*Association*, 0..* → 0..1, `EAID_157B8400_A07C_4ee7_8B80_F980D82B1471`)

## Rondleiding

Bezichtiging met toelichting

Attributen: naam, omschrijving, starttijd, eindtijd.

GUID: `EAID_2EE54C3D_0D8B_440e_A4A4_031273313901`

Relaties:

- voor → Tentoonstelling (*Association*, 0..* → 0..1, `EAID_6144A16A_F809_4685_BE15_3E8645BAD2DB`)

## Samensteller

Iemand die stukken informatie samenbrengt in tentoonstelingen, presentaties en naslagwerken.

Attributen: rol.

GUID: `EAID_E5566AF6_3D43_4b2f_B658_F67F6C1C511D`

Relaties:

- stelt samen → Tentoonstelling (*Association*, 0..* → 0..*, `EAID_B15FDBFD_05E6_4a55_81FF_DB6F287AE693`)
- → Medewerker (*Generalization*,  → , `EAID_9E3CADC4_EB76_4095_A1D4_361657422432`)

## Standplaats

vanaf een vaste locatie te koop aanbieden, verkopen of afleveren van goederen of aanbieden van diensten, gebruikmakend van fysieke middelen zoals een kraam, een wagen of een tafel

Attributen: beschrijving, adres, naamInstelling.

GUID: `EAID_98F3132E_F97A_4f49_B4F5_28618BB693F8`

## Tentoonstelling

Een uitstalling van voorwerpen om door het grote publiek bekeken te worden.

Attributen: titel, omschrijving, datumStart, datumEinde, subtitel.

GUID: `EAID_069C9894_5E07_4c95_AC28_EB4A5EBFD165`

Relaties:

- is gewijd aan → Historisch Persoon (*Association*, 0..* → 0..*, `EAID_71A3BEE0_D763_4683_8CC0_EBD7E32B5FB4`)
- → Zaal (*Association*, 0..* → 0..*, `EAID_021C5BC3_CCAE_4ea4_9B36_93810FAB81BF`)

## Voorziening

Middel om services/maatregelen in te vullen.

Attributen: naam, omschrijving, aantalBeschikbaar.

GUID: `EAID_8D3666E3_F2DA_4cba_BF67_EFED9AAD97CC`

## Winkelverkoopgroep

Groepering van winkelverkopen

GUID: `EAID_CE76218E_E56C_4c15_A29B_5EB14B7E084F`

## Winkelvoorraaditem

Onderdeel in de winkelvoorraad

Attributen: aantal, locatie, aantalInBestelling, datumLeveringBestelling.

GUID: `EAID_9D19BC40_5EED_408d_AFA3_7C16F8E7E65F`

Relaties:

- betreft → Product (*Association*, 0..1 → 1, `EAID_0B37A6D7_093C_43d4_80BC_1EAFF17DFB73`)

## Zaal

Grote ruimte in een gebouw

Attributen: naam, omschrijving, capaciteit, nummer.

GUID: `EAID_6850BC5E_444E_4d33_A8A7_9B345502E275`
