<!-- gegenereerd door tools/ggm.py; hash: 0251cc301eacea37a7040e9ce245259e1af16b184391a8d1d8be59358c806bfe -->
# Financien

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

## Activa

Bezittingen van een onderneming op een boekhoudkundige balans

Attributen: naam, omschrijving.

GUID: `EAID_7B8D0A8F_07BF_42bf_90B3_28A72BD4401A`

Relaties:

- is soort → Activasoort (*Association*, 0..* → 1..1, `EAID_BDB6C649_731B_45d7_84A2_AA3FBE5CD679`)

## Activasoort

Typering van activa

Attributen: naam, omschrijving.

GUID: `EAID_2483BD14_7FA7_4514_A565_C7F7967E226D`

## Bankafschrift

Overzicht van de bij- en afschrijvingen van een rekening

Attributen: nummer, datum.

GUID: `EAID_FC698CC3_7A64_4991_A751_B3B2A5DF77E3`

Relaties:

- heeft → Bankafschriftregel (*Association*, 1..1 → 0..*, `EAID_0E305A12_8F68_4386_BC11_13BDBE911426`)

## Bankafschriftregel

Een item op het bankafschrift

Attributen: bedrag, bij, datum, rekeningVan.

GUID: `EAID_764CE125_55C1_480d_90BA_745484CF3FC0`

Relaties:

- leidt tot → Mutatie (*Association*, 0..1 → 0..1, `EAID_1488955D_7866_448b_A697_E1CB459071A4`)

## Bankrekening

Een rekening-courant bij een bank

Attributen: nummer, bank, tennaamstelling.

GUID: `EAID_D87012E0_D2EB_4333_AD6C_1E43E6857304`

Relaties:

- heeft → Bankafschrift (*Association*, 1..1 → 0..*, `EAID_2A42756C_D8A3_421a_8AB5_430D80BAFEF4`)
- van → Betaling (*Association*, 1..1 → 0..*, `EAID_2CBFE5D9_98CF_48c2_B012_8C47E8059937`)
- naar → Betaling (*Association*, 1..1 → 0..*, `EAID_DBB3CA78_D0F1_42b0_A19B_05524EF200C0`)

## Batch

Verzameling van posten die in het kader van automatische verwerking een logisch geheel vormen.

Attributen: datum, tijd, nummer.

GUID: `EAID_A784A0ED_4451_4a92_B7C8_ABE528BA898F`

Relaties:

- heeft → Batchregel (*Association*, 1..1 → 0..*, `EAID_18DF7A1B_5396_42fe_8FDF_34812458527C`)
- heeft herkomst → ExterneBron (*Association*, 0..* → 1..1, `EAID_0391E42D_F622_483f_9441_820B9E511E22`)

## Batchregel

Een item uit een batch

Attributen: bedrag, omschrijving, datumBetaling, rekeningVan, rekeningNaar.

GUID: `EAID_9F935C8B_5B7C_4ce4_9360_04A91F4F70CC`

Relaties:

- leidt tot → Mutatie (*Association*, 0..1 → 0..1, `EAID_E6BACB34_2453_4892_847D_04A542D878FF`)

## Begroting

Een overzicht van de verwachte ontvangsten en voorziene uitgaven voor een bepaalde (meestal toekomstige) periode zodat hier een afstemming tussen plaats kan vinden om eventuele tekorten en overschotten vroegtijdig in kaart te kunnen brengen.

Attributen: naam, omschrijving, nummer.

GUID: `EAID_C95CF400_8487_4ff3_B475_CA1E01EBCA78`

Relaties:

- heeft → Begrotingregel (*Association*, 1..1 → 0..*, `EAID_6D11AF80_239E_4525_8000_2717D074149D`)
- valt binnen → Periode (*Association*, 0..* → 1..*, `EAID_9E1D220D_78AE_4d04_86D3_06F8766BA779`)

## Begrotingregel

Een item op de begroting

Attributen: bedrag, soortRegel, batenLasten.

GUID: `EAID_87964E36_9FEE_4b8f_A053_C4EDAF000646`

Relaties:

- betreft → Doelstelling (*Association*, 0..* → 0..1, `EAID_0B0D5623_4072_49bc_857A_F583A1C9B9CA`)
- betreft → Hoofdrekening (*Association*, 0..* → 0..1, `EAID_66D98C08_B17F_4919_89E2_41C2A36A0ABE`)
- betreft → Hoofdstuk (*Association*, 0..* → 1..1, `EAID_A0A62768_BD80_47c4_B869_6B33BC152824`)
- betreft → Kostenplaats (*Association*, 0..* → 0..1, `EAID_54C3102E_985B_4020_8B24_0F9D111C55DB`)
- betreft → Product (*Association*, 0..* → 0..1, `EAID_321293B0_DD5B_4fca_8289_FEF35DE4D09C`)

## Debiteur

Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan

GUID: `EAID_E74D0D46_66EB_4deb_A540_7AB08E95F956`

Relaties:

- heeft → Factuur (*Association*, 1..1 → 0..*, `EAID_E206BCA6_B3F5_4376_8CC4_67310C284E95`)
- → Rechtspersoon (*Generalization*,  → , `EAID_160B259E_634D_4b8a_A9BC_54EC52438F5F`)

## Doelstelling

Een op korte of middellange termijn nagestreefde situatie

Attributen: naam, omschrijving, nummer.

GUID: `EAID_2FFE3BAD_CB0E_43ea_A435_FD693B9255C3`

Relaties:

- is opdrachtgever → Opdrachtgever (*Association*, 1..* → 1..1, `EAID_A7B546AD_C824_410c_814E_168B39E9BA6A`)
- heeft → Product (*Association*, 1..1 → 0..*, `EAID_8EA25837_2624_4d49_AC94_79AFF4995ABC`)

## Factuur

Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten.

Attributen: datumFactuur, omschrijving, code, betaaltermijn, betaalbaarPer, factuurbedragExclusiefBTW, factuurbedragBTW.

GUID: `EAID_E1DA56C3_6ECA_4ec9_8CF4_FC57E1C43102`

Relaties:

- heeft → Factuurregel (*Association*, 1..1 → 1..*, `EAID_8FF67C2D_BF63_4860_9E51_C4BF24F61872`)
- gedekt via → Inkooporder (*Association*, 0..* → 0..1, `EAID_74E19019_808A_42c7_9881_B210F10203CC`)
- schrijft op → Kostenplaats (*Association*, 0..* → 0..1, `EAID_05D36DF8_E8DB_4273_B0C4_D1DDAB7070F4`)
- crediteur → Leverancier (*Association*, 0..* → 1, `EAID_9A061D5D_22D5_445b_8DA5_907EF432D5FD`)

## Factuurregel

Een item op de factuur

Attributen: nummer, omschrijving, aantal, bedragExBTW, bedragBTW, BTWPercentage.

GUID: `EAID_65E960EA_CC92_4af1_AF2B_B4625FA6AEA0`

Relaties:

- leidt tot → Mutatie (*Association*, 0..1 → 0..1, `EAID_6CFEC8E4_A77E_44d6_8AB7_8D425CB81C98`)

## Hoofdrekening

is kostensoort

Attributen: nummer, naam, omschrijving, subcode, subcodeOmschrijving, PIAHoofdcategorieCode, PIAHoofcategorieOmschrijving.

GUID: `EAID_0EEAF579_3F47_4551_B9F9_7367280EB3EB`

Relaties:

- heeft → Activa (*Association*, 0..* → 0..*, `EAID_8BE77D7B_E711_4db7_908F_04A150D26AB9`)
- valt binnen → Hoofdrekening (*Association*, 1..1 → 0..*, `EAID_64040FD4_B6BA_4e55_888A_3E35E6B2F658`)
- heeft → Kostenplaats (*Association*, 1..* → 0..*, `EAID_0D4DE7F7_8FFF_46fb_93EF_75C59A40402E`)
- heeft → Subrekening (*Association*, 1..1 → 0..*, `EAID_7361D015_36B8_4060_90DC_4675F7E67B02`)
- heeft → Werkorder (*Association*, 1..1 → 0..*, `EAID_D83126B9_06B7_4d92_AEB4_0A4E83CD17F8`)

## Hoofdstuk

Onderdeel van een langere tekst.

Attributen: naam, omschrijving, nummer.

GUID: `EAID_FFAA30D3_91C2_44aa_B52D_B21C51DB0326`

Relaties:

- heeft → Doelstelling (*Association*, 1..1 → 0..*, `EAID_A9F63505_885F_4702_8652_2374F2A395FD`)
- binnen → Periode (*Association*, 0..* → 1..*, `EAID_5F550A95_C5D4_49ad_9085_C03850713F40`)

## Inkooporder

Een opdracht (gezien vanuit de klant) voor één of meer leveringen door de leverancier aan die klant van een bepaalde hoeveelheid gespecificeerde goederen en/of diensten onder overeengekomen leveringsvoorwaarden en prijzen.

Attributen: ordernummer, omschrijving, totaalNettoBedrag, datumStart, datumEinde, betreft, saldo, wijzeVanAanbesteden, betalingMeerdereJaren, datumIngediend, artikelcode, goederencode.

GUID: `EAID_A91E9C27_C4FA_4e1b_A4FF_8AE74ED9B7EB`

Relaties:

- betreft → Contract (*Association*, 0..1 → 1, `EAID_741488BC_0571_413b_99F6_FC434B85F7B2`)
- wordt geschreven op → Hoofdrekening (*Association*, 0..* → 1..*, `EAID_BB1A104B_5484_454b_AE35_AA96D5BBAE72`)
- gerelateerd → Inkooporder (*Association*, 0..1 → 0..*, `EAID_B23EDC61_B59E_4366_A6D7_038C24AE04CF`)
- oorspronkelijk → Inkooporder (*Association*, 0..1 → 0..1, `EAID_B352FC5A_89BA_4c9c_9D7C_50CAD3BE05DE`)
- heeft → Inkooppakket (*Association*, 0..* → 1..1, `EAID_2C43B3E5_866D_4e62_9F6B_129BB99B685E`)
- verplichting aan → Leverancier (*Association*, 0..* → 1, `EAID_4F3749A3_9564_4f68_B9AB_FF9F3BDFCC9D`)
- hoort bij → Werkbon (*Association*, 1..1 → 0..*, `EAID_5C741153_4EE0_491d_9927_7ECB0A8B4F39`)

## Kostenplaats

Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven.

Attributen: naam, omschrijving, kostenplaatssoortCode, kostenplaatssoortOmschrijving, kostenplaatstypeCode, kostenplaatstypeOmschrijving, BTWCode, BTWOmschrijving.

GUID: `EAID_D90E822D_7EF8_4ea6_AF5C_4A4362577941`

Relaties:

- heeft → Inkooporder (*Association*, 0..* → 0..*, `EAID_11C86045_388F_48a6_8BD6_7BA9928D9D64`)
- is budgetverantwoordelijk → Opdrachtnemer (*Association*, 1..* → 1..1, `EAID_6FF88F9A_09E6_4941_9752_49B5B854D383`)
- heeft → Subrekening (*Association*, 1..1 → 0..*, `EAID_5DDB92ED_B5AD_49f8_92B7_76CC4B5C6177`)
- heeft → Taakveld (*Association*, 1..* → 1..*, `EAID_D9503D77_C2AE_4279_801D_A2916D66D72A`)
- heeft → Vastgoedobject (*Association*, 1..1 → 0..*, `EAID_C07FCDFF_6F36_4bb1_906A_79765C3577E6`)
- heeft → Werkorder (*Association*, 1..1 → 0..*, `EAID_1AF4A6F2_AE2B_454b_BF4E_9F4CC491CC73`)

## Mutatie

Wijziging van een situatie

Attributen: datum, bedrag.

GUID: `EAID_CB0A6B53_D263_459e_8C28_AD97E5552FFF`

Relaties:

- van → Hoofdrekening (*Association*, 0..* → 1..1, `EAID_59EC2AF5_43E6_49fd_94BD_9563BDDB5D8E`)
- naar → Hoofdrekening (*Association*, 0..* → 1..1, `EAID_ADC7B92C_E9E6_4067_A289_7746AF3306C0`)
- heeft betrekking op → Kostenplaats (*Association*, 0..* → 1..1, `EAID_4A07878B_1FE7_48d9_BBF1_C4D18F299E2B`)

## Opdrachtgever

Persoon die een opdracht verstrekt.

Attributen: naam, omschrijving, nummer, clustercode, clusterOmschrijving.

GUID: `EAID_C2520FC3_622B_4edf_B911_C661B0D710FE`

Relaties:

- uitgevoerd door → Functie (*Association*, 0..* → 1..1, `EAID_9B827D4A_7753_49c0_9378_C88F563052BE`)
- is opdrachtgever → Product (*Association*, 0..1 → 0..*, `EAID_98567643_D699_44fe_995E_BE51DC5CE53C`)

## Opdrachtnemer

Partij die een opdracht aanvaardt.

Attributen: naam, omschrijving, nummer, clustercode, clustercodeOmschrijving.

GUID: `EAID_9ABE303F_1E8D_407c_BBB8_E7DAC383E0C3`

Relaties:

- uitgevoerd door → Functie (*Association*, 0..* → 1..1, `EAID_A6483BC4_7D3D_4dee_B533_3C23F2236A96`)
- is opdrachtnemer → Product (*Association*, 0..1 → 0..*, `EAID_532D04B1_49B6_42ee_BBA0_318F384B8650`)

## Product

Het resultaat van een proces dat in het economisch verkeer een waarde bezit.

Attributen: naam, omschrijving, nummer.

GUID: `EAID_04439F81_75DB_45cf_BE7A_352A54A95D73`

Relaties:

- heeft → Kostenplaats (*Association*, 0..* → 1..1, `EAID_6651DFAB_6AA2_4754_987F_3F4635E0B941`)

## Subrekening

Ondergeschikte rekening van een hoofdrekening

Attributen: naam, omschrijving, nummer.

GUID: `EAID_1EC60172_CB6B_40c9_9818_C7A708C8540E`

## Taakveld

Een samenhangend geheel van activiteiten en taken en hangt onder een programma.

Attributen: hoofdfunctie, hoofdfunctieOmschrijving, functiecodeIV3, functieomschrijvingIV3, taakveldcode, taakveldOmschrijving, subtaakveldCode, subtaakveldOmschrijving.

GUID: `EAID_E81C0FA0_2203_489a_98E9_32F1CB200E75`

## Werkorder

Opdracht voor de uitvoering van een activiteit of een stap in een proces.

Attributen: naam, omschrijving, code, werkordertype, documentnummer.

GUID: `EAID_4AF7FA48_DFB0_474f_B797_A13D5FD37530`
