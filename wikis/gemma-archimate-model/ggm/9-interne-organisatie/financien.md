<!-- gegenereerd door tools/ggm.py; hash: 3edc202bc633219b5254d98c9cd7c29b27e0ea4b35fb5c2608e6cd1c3c4e4bea -->
# Financien

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Activa | `EAID_7B8D0A8F_07BF_42bf_90B3_28A72BD4401A` | Bezittingen van een onderneming op een boekhoudkundige balans | naam, omschrijving |
| Activasoort | `EAID_2483BD14_7FA7_4514_A565_C7F7967E226D` | Typering van activa | naam, omschrijving |
| Bankafschrift | `EAID_FC698CC3_7A64_4991_A751_B3B2A5DF77E3` | Overzicht van de bij- en afschrijvingen van een rekening | nummer, datum |
| Bankafschriftregel | `EAID_764CE125_55C1_480d_90BA_745484CF3FC0` | Een item op het bankafschrift | bedrag, bij, datum, rekeningVan |
| Bankrekening | `EAID_D87012E0_D2EB_4333_AD6C_1E43E6857304` | Een rekening-courant bij een bank | nummer, bank, tennaamstelling |
| Batch | `EAID_A784A0ED_4451_4a92_B7C8_ABE528BA898F` | Verzameling van posten die in het kader van automatische verwerking een logisch geheel vormen. | datum, tijd, nummer |
| Batchregel | `EAID_9F935C8B_5B7C_4ce4_9360_04A91F4F70CC` | Een item uit een batch | bedrag, omschrijving, datumBetaling, rekeningVan, rekeningNaar |
| Begroting | `EAID_C95CF400_8487_4ff3_B475_CA1E01EBCA78` | Een overzicht van de verwachte ontvangsten en voorziene uitgaven voor een bepaalde (meestal toekomstige) periode zodat hier een afstemming tussen plaats kan vinden om eventuele tekorten en overschotten vroegtijdig in kaart te kunnen brengen. | naam, omschrijving, nummer |
| Begrotingregel | `EAID_87964E36_9FEE_4b8f_A053_C4EDAF000646` | Een item op de begroting | bedrag, soortRegel, batenLasten |
| Debiteur | `EAID_E74D0D46_66EB_4deb_A540_7AB08E95F956` | Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan |  |
| Doelstelling | `EAID_2FFE3BAD_CB0E_43ea_A435_FD693B9255C3` | Een op korte of middellange termijn nagestreefde situatie | naam, omschrijving, nummer |
| Factuur | `EAID_E1DA56C3_6ECA_4ec9_8CF4_FC57E1C43102` | Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten. | datumFactuur, omschrijving, code, betaaltermijn, betaalbaarPer, factuurbedragExclusiefBTW, factuurbedragBTW |
| Factuurregel | `EAID_65E960EA_CC92_4af1_AF2B_B4625FA6AEA0` | Een item op de factuur | nummer, omschrijving, aantal, bedragExBTW, bedragBTW, BTWPercentage |
| Hoofdrekening | `EAID_0EEAF579_3F47_4551_B9F9_7367280EB3EB` | is kostensoort | nummer, naam, omschrijving, subcode, subcodeOmschrijving, PIAHoofdcategorieCode, PIAHoofcategorieOmschrijving |
| Hoofdstuk | `EAID_FFAA30D3_91C2_44aa_B52D_B21C51DB0326` | Onderdeel van een langere tekst. | naam, omschrijving, nummer |
| Inkooporder | `EAID_A91E9C27_C4FA_4e1b_A4FF_8AE74ED9B7EB` | Een opdracht (gezien vanuit de klant) voor één of meer leveringen door de leverancier aan die klant van een bepaalde hoeveelheid gespecificeerde goederen en/of diensten onder overeengekomen leveringsvoorwaarden en prijzen. | ordernummer, omschrijving, totaalNettoBedrag, datumStart, datumEinde, betreft, saldo, wijzeVanAanbesteden, betalingMeerdereJaren, datumIngediend, artikelcode, goederencode |
| Kostenplaats | `EAID_D90E822D_7EF8_4ea6_AF5C_4A4362577941` | Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven. | naam, omschrijving, kostenplaatssoortCode, kostenplaatssoortOmschrijving, kostenplaatstypeCode, kostenplaatstypeOmschrijving, BTWCode, BTWOmschrijving |
| Mutatie | `EAID_CB0A6B53_D263_459e_8C28_AD97E5552FFF` | Wijziging van een situatie | datum, bedrag |
| Opdrachtgever | `EAID_C2520FC3_622B_4edf_B911_C661B0D710FE` | Persoon die een opdracht verstrekt. | naam, omschrijving, nummer, clustercode, clusterOmschrijving |
| Opdrachtnemer | `EAID_9ABE303F_1E8D_407c_BBB8_E7DAC383E0C3` | Partij die een opdracht aanvaardt. | naam, omschrijving, nummer, clustercode, clustercodeOmschrijving |
| Product | `EAID_04439F81_75DB_45cf_BE7A_352A54A95D73` | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. | naam, omschrijving, nummer |
| Subrekening | `EAID_1EC60172_CB6B_40c9_9818_C7A708C8540E` | Ondergeschikte rekening van een hoofdrekening | naam, omschrijving, nummer |
| Taakveld | `EAID_E81C0FA0_2203_489a_98E9_32F1CB200E75` | Een samenhangend geheel van activiteiten en taken en hangt onder een programma. | hoofdfunctie, hoofdfunctieOmschrijving, functiecodeIV3, functieomschrijvingIV3, taakveldcode, taakveldOmschrijving, subtaakveldCode, subtaakveldOmschrijving |
| Werkorder | `EAID_4AF7FA48_DFB0_474f_B797_A13D5FD37530` | Opdracht voor de uitvoering van een activiteit of een stap in een proces. | naam, omschrijving, code, werkordertype, documentnummer |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Activa | Association | is soort | Activasoort | 0..* → 1..1 | `EAID_BDB6C649_731B_45d7_84A2_AA3FBE5CD679` |  |
| Bankafschrift | Association | heeft | Bankafschriftregel | 1..1 → 0..* | `EAID_0E305A12_8F68_4386_BC11_13BDBE911426` |  |
| Bankafschriftregel | Association | leidt tot | Mutatie | 0..1 → 0..1 | `EAID_1488955D_7866_448b_A697_E1CB459071A4` |  |
| Bankrekening | Association | heeft | Bankafschrift | 1..1 → 0..* | `EAID_2A42756C_D8A3_421a_8AB5_430D80BAFEF4` |  |
| Bankrekening | Association | van | Betaling | 1..1 → 0..* | `EAID_2CBFE5D9_98CF_48c2_B012_8C47E8059937` |  |
| Bankrekening | Association | naar | Betaling | 1..1 → 0..* | `EAID_DBB3CA78_D0F1_42b0_A19B_05524EF200C0` |  |
| Batch | Association | heeft herkomst | ExterneBron | 0..* → 1..1 | `EAID_0391E42D_F622_483f_9441_820B9E511E22` |  |
| Batch | Association | heeft | Batchregel | 1..1 → 0..* | `EAID_18DF7A1B_5396_42fe_8FDF_34812458527C` |  |
| Batchregel | Association | leidt tot | Mutatie | 0..1 → 0..1 | `EAID_E6BACB34_2453_4892_847D_04A542D878FF` |  |
| Begroting | Association | heeft | Begrotingregel | 1..1 → 0..* | `EAID_6D11AF80_239E_4525_8000_2717D074149D` |  |
| Begroting | Association | valt binnen | Periode | 0..* → 1..* | `EAID_9E1D220D_78AE_4d04_86D3_06F8766BA779` |  |
| Begrotingregel | Association | betreft | Doelstelling | 0..* → 0..1 | `EAID_0B0D5623_4072_49bc_857A_F583A1C9B9CA` |  |
| Begrotingregel | Association | betreft | Product | 0..* → 0..1 | `EAID_321293B0_DD5B_4fca_8289_FEF35DE4D09C` |  |
| Begrotingregel | Association | betreft | Kostenplaats | 0..* → 0..1 | `EAID_54C3102E_985B_4020_8B24_0F9D111C55DB` |  |
| Begrotingregel | Association | betreft | Hoofdrekening | 0..* → 0..1 | `EAID_66D98C08_B17F_4919_89E2_41C2A36A0ABE` |  |
| Begrotingregel | Association | betreft | Hoofdstuk | 0..* → 1..1 | `EAID_A0A62768_BD80_47c4_B869_6B33BC152824` |  |
| Debiteur | Association | heeft | Factuur | 1..1 → 0..* | `EAID_E206BCA6_B3F5_4376_8CC4_67310C284E95` |  |
| Debiteur | Generalization |  | Rechtspersoon |  →  | `EAID_160B259E_634D_4b8a_A9BC_54EC52438F5F` |  |
| Doelstelling | Association | heeft | Product | 1..1 → 0..* | `EAID_8EA25837_2624_4d49_AC94_79AFF4995ABC` |  |
| Doelstelling | Association | is opdrachtgever | Opdrachtgever | 1..* → 1..1 | `EAID_A7B546AD_C824_410c_814E_168B39E9BA6A` |  |
| Factuur | Association | schrijft op | Kostenplaats | 0..* → 0..1 | `EAID_05D36DF8_E8DB_4273_B0C4_D1DDAB7070F4` |  |
| Factuur | Association | gedekt via | Inkooporder | 0..* → 0..1 | `EAID_74E19019_808A_42c7_9881_B210F10203CC` |  |
| Factuur | Association | heeft | Factuurregel | 1..1 → 1..* | `EAID_8FF67C2D_BF63_4860_9E51_C4BF24F61872` |  |
| Factuur | Association | crediteur | Leverancier | 0..* → 1 | `EAID_9A061D5D_22D5_445b_8DA5_907EF432D5FD` |  |
| Factuurregel | Association | leidt tot | Mutatie | 0..1 → 0..1 | `EAID_6CFEC8E4_A77E_44d6_8AB7_8D425CB81C98` |  |
| Hoofdrekening | Association | heeft | Kostenplaats | 1..* → 0..* | `EAID_0D4DE7F7_8FFF_46fb_93EF_75C59A40402E` |  |
| Hoofdrekening | Association | valt binnen | Hoofdrekening | 1..1 → 0..* | `EAID_64040FD4_B6BA_4e55_888A_3E35E6B2F658` |  |
| Hoofdrekening | Association | heeft | Subrekening | 1..1 → 0..* | `EAID_7361D015_36B8_4060_90DC_4675F7E67B02` |  |
| Hoofdrekening | Association | heeft | Activa | 0..* → 0..* | `EAID_8BE77D7B_E711_4db7_908F_04A150D26AB9` |  |
| Hoofdrekening | Association | heeft | Werkorder | 1..1 → 0..* | `EAID_D83126B9_06B7_4d92_AEB4_0A4E83CD17F8` |  |
| Hoofdstuk | Association | binnen | Periode | 0..* → 1..* | `EAID_5F550A95_C5D4_49ad_9085_C03850713F40` |  |
| Hoofdstuk | Association | heeft | Doelstelling | 1..1 → 0..* | `EAID_A9F63505_885F_4702_8652_2374F2A395FD` |  |
| Inkooporder | Association | heeft | Inkooppakket | 0..* → 1..1 | `EAID_2C43B3E5_866D_4e62_9F6B_129BB99B685E` |  |
| Inkooporder | Association | verplichting aan | Leverancier | 0..* → 1 | `EAID_4F3749A3_9564_4f68_B9AB_FF9F3BDFCC9D` |  |
| Inkooporder | Association | hoort bij | Werkbon | 1..1 → 0..* | `EAID_5C741153_4EE0_491d_9927_7ECB0A8B4F39` |  |
| Inkooporder | Association | betreft | Contract | 0..1 → 1 | `EAID_741488BC_0571_413b_99F6_FC434B85F7B2` |  |
| Inkooporder | Association | gerelateerd | Inkooporder | 0..1 → 0..* | `EAID_B23EDC61_B59E_4366_A6D7_038C24AE04CF` |  |
| Inkooporder | Association | oorspronkelijk | Inkooporder | 0..1 → 0..1 | `EAID_B352FC5A_89BA_4c9c_9D7C_50CAD3BE05DE` |  |
| Inkooporder | Association | wordt geschreven op | Hoofdrekening | 0..* → 1..* | `EAID_BB1A104B_5484_454b_AE35_AA96D5BBAE72` |  |
| Kostenplaats | Association | heeft | Inkooporder | 0..* → 0..* | `EAID_11C86045_388F_48a6_8BD6_7BA9928D9D64` |  |
| Kostenplaats | Association | heeft | Werkorder | 1..1 → 0..* | `EAID_1AF4A6F2_AE2B_454b_BF4E_9F4CC491CC73` |  |
| Kostenplaats | Association | heeft | Subrekening | 1..1 → 0..* | `EAID_5DDB92ED_B5AD_49f8_92B7_76CC4B5C6177` |  |
| Kostenplaats | Association | is budgetverantwoordelijk | Opdrachtnemer | 1..* → 1..1 | `EAID_6FF88F9A_09E6_4941_9752_49B5B854D383` |  |
| Kostenplaats | Association | heeft | Vastgoedobject | 1..1 → 0..* | `EAID_C07FCDFF_6F36_4bb1_906A_79765C3577E6` |  |
| Kostenplaats | Association | heeft | Taakveld | 1..* → 1..* | `EAID_D9503D77_C2AE_4279_801D_A2916D66D72A` |  |
| Mutatie | Association | heeft betrekking op | Kostenplaats | 0..* → 1..1 | `EAID_4A07878B_1FE7_48d9_BBF1_C4D18F299E2B` |  |
| Mutatie | Association | van | Hoofdrekening | 0..* → 1..1 | `EAID_59EC2AF5_43E6_49fd_94BD_9563BDDB5D8E` |  |
| Mutatie | Association | naar | Hoofdrekening | 0..* → 1..1 | `EAID_ADC7B92C_E9E6_4067_A289_7746AF3306C0` |  |
| Opdrachtgever | Association | is opdrachtgever | Product | 0..1 → 0..* | `EAID_98567643_D699_44fe_995E_BE51DC5CE53C` |  |
| Opdrachtgever | Association | uitgevoerd door | Functie | 0..* → 1..1 | `EAID_9B827D4A_7753_49c0_9378_C88F563052BE` |  |
| Opdrachtnemer | Association | is opdrachtnemer | Product | 0..1 → 0..* | `EAID_532D04B1_49B6_42ee_BBA0_318F384B8650` |  |
| Opdrachtnemer | Association | uitgevoerd door | Functie | 0..* → 1..1 | `EAID_A6483BC4_7D3D_4dee_B533_3C23F2236A96` |  |
| Product | Association | heeft | Kostenplaats | 0..* → 1..1 | `EAID_6651DFAB_6AA2_4754_987F_3F4635E0B941` |  |
