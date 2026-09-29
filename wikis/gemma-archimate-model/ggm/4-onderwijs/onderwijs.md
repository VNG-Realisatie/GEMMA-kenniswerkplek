<!-- gegenereerd door tools/ggm.py; hash: 2aed694f43240ca6b05b98a2072ce799ba751d439a78b6d1d09023019260a5e3 -->
# Onderwijs

Taakveld: 4 Onderwijs. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Inschrijving | `EAID_CFFD5F20_5FA9_4d93_AD34_6867D64A58B9` | Deelname van iemand aan een opleiding bij een onderwijsinstelling. | datum |
| Leerjaar | `EAID_D7ECEB92_BE50_4e30_9F27_54A008BC75DF` | Is de codering van het jaar of het niveau waarin de leerling onderwijs volgt. | jaarStart, jaarEinde |
| Leerling | `EAID_266057AF_58BD_42e1_B4D5_16EB266B9B7A` | Mens die een opleiding volgt, heeft gevolgd of gaat volgen of opgaat of is opgegaan voor een toets. (Bron: KOI) | kwetsbareJongere |
| Locatie | `EAID_3119A4DB_BB23_4adc_98BD_82F2D7996C6B` | De locatie beschrijft middels coördinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW) | adres |
| Loopbaanstap | `EAID_0E3DE26B_C535_4a03_98A4_8D36DC3D5297` | Een logische en ook uitdagende stap naar een volgende functie binnen dezelfde functiefamilie of een andere, op hetzelfde schaalniveau of op een schaalniveau hoger. | schooljaar, onderwijstype, klas |
| Onderwijsloopbaan | `EAID_F47ACE79_C476_479f_A3A3_729E65AF3D32` | Loopbaan als leerling in het onderwijs; loopbaan als leerling op school; tijd die iemand als leerling heeft doorgebracht op school, vaak met de bijgedachte aan de daarbij opgedane kennis en ervaring; tijd die men schoolgegaan heeft; onderwijs carrière ; schoolloopbaan; school carrière ; schooltijd; de schooljaren |  |
| Onderwijsniveau | `EAID_96AB51D0_52E5_4515_B21F_98B30C4B9C42` | De hoogte van een soort onderwijs in relatie tot andere soorten onderwijs |  |
| Onderwijssoort | `EAID_8AF9FAE6_13D8_484d_97F5_2A3839BC8618` | Typologie voor onderwijs | onderwijstype, omschrijving |
| Ouder Of Verzorger | `EAID_51C8E3DF_FFF4_4a20_9CB2_AA5FA50579E2` | Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind. |  |
| School | `EAID_32DFC5DD_79D9_45d5_8F9D_7D5125961817` | Gebouw in gebruik voor basis, middelbaar of hoger onderwijs. | naam |
| Startkwalificatie | `EAID_E8301577_1A49_43cf_A2CA_0F042584EBB3` | Diploma van een opleiding als bedoeld in de WEB of een diploma hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs als bedoeld in de WVO; | datumBehaald |
| Uitschrijving | `EAID_133AF611_9FA0_4a09_BF12_74C5FA5F6F60` | Beeindiging van een inschrijving van een leerling bij een school | datum, diplomaBehaald |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Inschrijving | Association | heeft | School | 0..* → 1..1 | `EAID_E0BB1B06_DD1A_4a88_B7F2_D426177F8198` |  |
| Leerling | Association | heeft | Vrijstelling | 1..1 → 0..* | `EAID_0B21C716_7F3E_42e6_89D6_631C6ADCD215` |  |
| Leerling | Association | heeft | Startkwalificatie | 1..1 → 0..1 | `EAID_2DC85C4C_48E2_4017_809C_20F8347288FF` |  |
| Leerling | Association | heeft | Onderwijsloopbaan | 1..1 → 0..* | `EAID_32D089B1_51D3_4720_B2BC_E5475EE62FA3` |  |
| Leerling | Association | heeft | Inschrijving | 1..1 → 0..* | `EAID_333AC8C9_7443_4a49_A875_297B65FC944C` |  |
| Leerling | Association | betreft | Ziekmelding Leerlingenvervoer | 1 → 0..* | `EAID_6EA4316E_D98A_443a_AEF4_4A2CE3A40B37` |  |
| Leerling | Association | heeft | Uitschrijving | 1..1 → 0..* | `EAID_901A3590_2010_4e3f_954C_A0A3D9E7AF28` |  |
| Leerling | Association | heeft | Verzuimmelding | 1..1 → 0..* | `EAID_BC9B933D_E53D_4637_A451_AB7BC45BC048` |  |
| Leerling | Association | betreft leerling | Procesverbaal Onderwijs | 1..1 → 0..* | `EAID_DBBD5265_268F_46ea_A748_3BECEA8A9A4A` |  |
| Leerling | Generalization |  | IngeschrevenPersoon |  →  | `EAID_ACD49FC1_B6A0_4cc3_896E_285018F4F415` |  |
| Locatie | Generalization |  | Vastgoedobject |  →  | `EAID_718B694A_0C55_4fe7_B0BE_B55AEDCB0EC8` |  |
| Onderwijsloopbaan | Aggregation (composite) |  | Loopbaanstap | 1 → 0..* | `EAID_5DA8C8B3_BE1A_40bd_A4FF_980213D42E5C` |  |
| Ouder Of Verzorger | Generalization |  | IngeschrevenPersoon |  →  | `EAID_EE1A50E8_EF34_4a9e_AD32_D985C4EB6147` |  |
| School | Association | school heeft | Locatie | 0..1 → 1..* | `EAID_0B9864A5_0943_4b48_AB00_E932A450D1B7` |  |
| School | Association | heeft | Uitschrijving | 1..1 → 0..* | `EAID_234C124E_EB86_4555_93EC_22588C3A17A4` |  |
| School | Association | gebruikt | Sportlocatie | 0..* → 0..* | `EAID_2631E399_1628_4896_BFF1_21D643845E2C` |  |
| School | Association | heeft | Onderwijssoort | 0..* → 1..* | `EAID_CED5C094_5222_4347_9FE1_7D5B2DECA3DD` |  |
| School | Association | kent | Onderwijsloopbaan | 1..* → 0..* | `EAID_FA07FA3D_3EC3_450e_8FE0_766875D7CC5F` |  |
| School | Generalization |  | NietNatuurlijkPersoon |  →  | `EAID_22B1F924_145E_4d87_989E_08C68BAFD692` |  |
| School | Generalization |  | NietNatuurlijkPersoon |  →  | `EAID_CE5E97EC_7CA7_482f_9556_EDBB93B624CE` |  |
