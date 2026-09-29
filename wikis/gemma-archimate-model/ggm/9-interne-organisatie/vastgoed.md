<!-- gegenereerd door tools/ggm.py; hash: eb0efe6d6c710e98478d5fdacf032a103a0004ce5aab7a6e94dfcc00f3623416 -->
# Vastgoed

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Aanbesteding Vastgoed | `EAID_17FCEF39_AB9D_4516_9C60_1DDA61D87356` | Een procedure waarbij een opdrachtgever bekendmaakt dat hij een opdracht of concessie wil laten uitvoeren en bedrijven uitnodigt om een offerte in te dienen. Dit in het kader van werkzaamheden rondom vastgoed. |  |
| Adresaanduiding | `EAID_909E635B_E33D_4ded_8471_900CD175B7D1` | De adresaanduiding van het WOZ-OBJECT | adres |
| Bouwdeel | `EAID_9A739672_6084_4c05_A13E_59DB13551E58` | Zelfstandig en aanwijsbaar deel van een element, onderscheiden naar samenstelling of constructiewijze, bestaande uit één of meer componenten waaraan technische eigenschappen en een onderhoudshistorie kunnen worden gerelateerd (bron: Conditiemeting gebouwde omgeving - Deel 1: Methodiek, code: 3.3) | code, omschrijving |
| Bouwdeelelement | `EAID_BE147761_326E_4859_9366_5157CE865EC1` | Onderdeeel van een bouwdeel | code, omschrijving |
| CultuurOnbebouwd | `EAID_01C1622D_23E7_4a63_9B63_F45CA63E76CA` | Een aanduiding voor de soort cultuur van het onbebouwde gedeelte van de onroerende zaak. | cultuurcodeOnbebouwd |
| Eigenaar | `EAID_5E06339C_13EE_44ca_BC40_0FC4B9DC8349` | Eigenaar is een persoon die de eigenaar is van een gebouw of stuk grond en ook alle rechten daarvan bezit. |  |
| Gebruiksdoel | `EAID_A5975EF7_558A_44fa_A656_AB43580D8C35` | Een aanduiding va alle waarden waarmee het gebruiksdoel van een object kan worden verbijzonderd. | gebruiksdoelGebouwdObject |
| Huurder | `EAID_B75EE7EF_DC1F_47da_A95C_B9662075684D` | Een partij die een zaak of een gedeelte daarvan in gebruik verstrekt heeft gekregen en zich heeft verbonden tot een tegenprestatie. |  |
| Inspectie | `EAID_A31C3B5D_EAC5_482d_8816_8B858EC4BE01` | het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen. | datum, bevindingen |
| KpBetrokkenBij | `EAID_D46DA88A_F3EB_4c72_85DA_C0C4239289E2` |  | datumBeginGeldigheid, datumEindeGeldigheid |
| KpOnstaanUit | `EAID_DCF0623A_694F_4b82_B615_F499F169C19A` |  | datumBeginGeldigheid, datumEindeGeldigheid |
| LocatieaanduidingWozObject | `EAID_0B3F8A89_F21E_4bea_9620_8D6713AB632C` | Nadere aanduiding van het WOZ-object | locatieOmschrijving, datumBeginGeldigheid, datumEindeGeldigheid, primair |
| Locatieonroerendezaak | `EAID_049E7FD0_D515_4057_9C87_A09980C5DE6A` | Locatie van een geregistreerd goed | locatieOmschrijving, cultuurcodeBebouwd, adrestype, datumBeginGeldigheid, datumEindeGeldigheid, geometrie |
| MJOP | `EAID_A110896B_0CAD_46cf_9226_840DEE3328F0` | Meerjaren Onderhoudsplanning | datum, omschrijving |
| MJOP-Item | `EAID_54697170_4C4D_40f6_9E08_35DF1970B8C6` | Onderdeel van een MJOP | code, omschrijving, kosten, datumStart, datumEinde, opzegtermijnAanbieder, opzegtermijnOntvanger, datumOpzeggingAanbieder, datumOpzeggingOntvanger |
| NADAanvullingBRP | `EAID_46386087_923F_402e_BB6B_6DE39D73349A` |  | opmerkingen |
| Objectrelatie | `EAID_3EA09322_144A_407d_86C4_FCC8C041C826` | Relatie tot een object | rol |
| Offerte | `EAID_EF55544A_F59B_4411_A3D2_9C1A2BA2663C` | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. |  |
| Pachter | `EAID_EDC8B01F_4802_4562_BC41_C2CAD76880B6` | Een persoon die een pachtovereenkomst heeft met de eigenaar van een perceel voor het gebruik als landbouwgrond. |  |
| Prijzenboekitem | `EAID_697512E4_0C8E_4be8_8E95_9E2E4BD50F85` | Onderdeel van een prijzenboek | verrichting, prijs, datumStart, datumEindeGeldigheid |
| Vastgoed Contract | `EAID_1C84E4B6_1BB5_4a0d_A945_FFFDFDFB544B` | Een contract is een afspraak tussen 2 of meer partijen. Sluit u een contract, dan moet u een bepaalde prestatie leveren of u heeft recht op een prestatie. Een ander woord voor een contract is een overeenkomst. Daarnaast komt de term overeenkomst van opdracht ook voor. | datumStart, datumEinde, maandbedrag, beschrijving, status, type, identificatie, opzegtermijn |
| Vastgoedcontractregel | `EAID_1C25D70B_AE22_4654_9190_2F55272D9BE6` | ONderdeel van een vastgoedcontract | type, omschrijving, status, datumStart, bedrag, datumEinde, frequentie, identificatie |
| Vastgoedobject | `EAID_28A6F2AC_5AB1_4f25_8876_931152CA28E0` | Perceel of vastgoed waar de gemeente een zakelijk recht heeft, en optioneel verhuurd, verpacht of anderzinds aan een derde partij. | adresaanduiding, WOZWaarde, marktwaarde, boekwaarde, verzekerdeWaarde, omschrijving, portefeuille, naam, bedragAankoop, aantalEtages, afgekochteErfpacht, afkoopwaarde, asbestrapportageAanwezig, datumAfstoten, datumBerekeningOppervlak, deelportefeuille, objecttype, fiscaleWaarde, gearchiveerd, herbouwwaarde, monument, onderhoudscategorie, provincie, verkoopbedrag, waardeGrond, waardeOpstal, wijk, energielabel, energieverbruik, energiekosten, CO2Uitstoot, jaarLaatsteRenovatie, aantalRioleringen, oppervlakteKantoor, conditiescore, aantalParkeerplaatsen, verkoopbaarheid, afgesprokenConditiescore, kostenplaats, bovenliggendNiveau, bestemmingsplan, locatie, bouwjaar, objectstatuscode, objectstatus, objecttypecode, portefeuillecode, bovenliggendNiveaucode, hoofdstuk, identificatie, foto, toelichting, datumEigendom, datumVerkoop, bouwwerk, brutoVloeroppervlakte, verhuurbaarVloeroppervlak |
| Verhuurbaar Eenheid | `EAID_98A7AE65_A061_449a_94CD_6218069CA86A` | Een Verhuurbare Eenheid (VHE) is een eenheid die individueel verhuurbaar is. Verhuurbaar komt voort uit 'exploitatie' | identificatie, naam, datumWerkelijkBegin, datumWerkelijkEinde, type, adres, datumStart, datumEinde, afmeting, opmerkingen, nettoOppervlak, nettoOmtrek, bezetting, huurprijs |
| Werkbon | `EAID_C5AA8835_219D_4bfa_85EF_8BA45F732BCD` | Document waarin een heoveelheid werk is beschreven |  |
| WOZ-Belang | `EAID_E71DC5EC_EEEB_4d27_A3C1_B46FD34AD41B` | hetgeen waaraan een persoon waarde hecht; zaak die of vorderingsrecht dat op geld waardeerbaar is, aan gevaar onderhevig en bij de wet niet uitgezonderd. De (rechts-)persoon die door de gemeente is aangewezen als "belanghebbende eigenaar", "belanghebbende gebruiker" of eventueel "medebelanghebbende" van het WOZ-object. | datumBeginGeldigheid, datumEindeGeldigheid, eigenaarGebruiker |
| Zakelijk Recht | `EAID_8D52E9F1_9CC9_42c6_A347_E68E29718E55` | Geeft een recht op een goed, zoals een onroerende zaak of een roerende zaak. | datumStart, datumEinde, soort, kosten |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Aanbesteding Vastgoed | Association | uitvoering van | Werkbon | 0..1 → 0..* | `EAID_7DA9022C_442D_404a_8B8D_FE7B0AD9E2AF` |  |
| Aanbesteding Vastgoed | Generalization |  | Aanbesteding |  →  | `EAID_DC5627CF_74C4_41e0_BA28_FD785F297154` |  |
| Bouwdeel | Association | bestaat uit | Bouwdeelelement | 1..1 → 0..* | `EAID_8C0FD59C_3646_41ca_89AE_81C4761B018F` |  |
| Eigenaar | Generalization |  | Rechtspersoon |  →  | `EAID_C3262888_F005_4505_A9C8_FB4E3404632B` |  |
| Huurder | Association | heeft huurrecht | Zakelijk Recht | 0..* → 1..* | `EAID_02F47C2D_6990_48f3_A445_0A1010D4A818` |  |
| Huurder | Generalization |  | Rechtspersoon |  →  | `EAID_05E467BB_6588_411b_9079_294A9FA41A1F` |  |
| Inspectie | Association | leidt tot | MJOP | 0..1 → 0..1 | `EAID_C2B5F5BE_EBBD_4eb1_B0B3_689D079662BE` |  |
| KpBetrokkenBij | Association |  | Appartementsrechtsplitsing | 0..* → 1..1 | `EAID_73891901_299C_4b86_B0BE_B9D85E13C08B` |  |
| KpBetrokkenBij | Association | is betrokken bij | ZakelijkRecht | 0..* → 1..1 | `EAID_F6CE3998_EF89_46c2_A99E_7D8F594782D5` |  |
| KpOnstaanUit | Association |  | Appartementsrechtsplitsing | 0..* → 1..1 | `EAID_B0C2A9A7_90BC_44d0_9F0B_BDF158E4CBDD` |  |
| KpOnstaanUit | Association | is ontstaan uit | ZakelijkRecht | 0..* → 1..1 | `EAID_B236458D_84DF_4f68_A42A_50E754D9CBA3` |  |
| LocatieaanduidingWozObject | Association | heeft | WOZ-object | 1 → 1 | `EAID_F2BB0B84_CC53_4d49_8F47_BF8032EF63DB` |  |
| Locatieonroerendezaak | Association | heeft Adresseerbaar object | AdresseerbaarObject | 0..* → 1 | `EAID_0D455136_E7F3_45b9_856F_99BD1C12F7EF` |  |
| Locatieonroerendezaak | Association | heeft adres | KadastraleOnroerendeZaak | 0..* → 1 | `EAID_A32B511F_6DE7_4c10_8F83_466FFB1BDCD6` |  |
| MJOP | Association | bestaat uit | MJOP-Item | 1..1 → 0..* | `EAID_0828CF48_6C0B_4f1a_A018_B192EBF74730` |  |
| MJOP | Association | betreft | Vastgoedobject | 0..* → 1 | `EAID_4BE0392A_61EB_4695_AC85_CBE33C9BE1FC` |  |
| MJOP | Association | gerealiseerd door | Werkbon | 1..1 → 0..* | `EAID_C4F076A9_6FD3_4ea4_9AEA_AEEDF986D4D8` |  |
| MJOP-Item | Association | op basis van | Prijzenboekitem | 0..* → 1..1 | `EAID_040E7F95_87E6_452f_B4A5_632CF872267A` |  |
| MJOP-Item | Association | betreft | Vastgoedobject | 0..* → 1..1 | `EAID_1EF013DA_6BD6_4829_8AD1_6F4065F52476` |  |
| MJOP-Item | Association | betreft | Bouwdeelelement | 0..* → 0..1 | `EAID_F7B09835_7FBB_4bff_8358_989D2394E13B` |  |
| MJOP-Item | Association | betreft | Bouwdeel | 0..* → 0..1 | `EAID_FA4C6F8E_34E2_4e27_B218_583EBE1FF701` |  |
| NADAanvullingBRP | Generalization |  | Nummeraanduiding |  →  | `EAID_D6C938D2_42AB_4780_884E_97918389B624` |  |
| Pachter | Generalization |  | Rechtspersoon |  →  | `EAID_F0BCB77A_4997_4d83_97EF_43AB2BA211E0` |  |
| Vastgoed Contract | Association | heeft | Rechtspersoon | 0..* → 1 | `EAID_A31F7870_F775_49c8_9702_98020B0CEA18` |  |
| Vastgoedcontractregel | Association | heeft | Vastgoed Contract | 1..* → 1..1 | `EAID_DC0B2F2C_B864_4290_AEDA_3BA3DF2ED022` |  |
| Vastgoedobject | Association | betreft | KadastraleOnroerendeZaak | 0..* → 0..* | `EAID_0B49106E_8E0D_4868_AD7B_FBE77EA922D9` |  |
| Vastgoedobject | Association | bestaat uit | Bouwdeel | 1..1 → 0..* | `EAID_93946505_11FE_4bb7_AE26_EF2BC4AE456A` |  |
| Vastgoedobject | Association | heeft | Verhuurbaar Eenheid | 1..1 → 0..* | `EAID_96F3EE4A_4E0B_4427_A6AC_941B7F0ACCD8` |  |
| Vastgoedobject | Association | betreft | Pand | 0..1 → 0..1 | `EAID_A65AF23A_C4D8_4679_8800_AD24C940D684` |  |
| Vastgoedobject | Association | heeft | Vastgoedcontractregel | 1.. → 0..1 | `EAID_A6A3C17F_1AF6_498b_B4CE_E7EDACC88D2C` |  |
| Vastgoedobject | Association | betreft | Inspectie | 1 → 0..* | `EAID_A6AE4BC0_4174_44c0_949D_2E04EF68C7C9` |  |
| Vastgoedobject | Association | heeft | Objectrelatie | 1..1 → 0..* | `EAID_B9AF179F_CA5C_4aa9_87C8_DE0731990450` |  |
| Vastgoedobject | Association | betreft | KadastraalPerceel | 0..* → 0..* | `EAID_BBEAE982_EA8B_4e71_8C55_7149B9143E9E` |  |
| Vastgoedobject | Association | betreft | Zakelijk Recht | 1..* → 0..* | `EAID_EB8D23E8_02B3_4898_831A_B2BE79831E38` |  |
| Verhuurbaar Eenheid | Association | betreft | Vastgoedcontractregel | 0..1 → 1..1 | `EAID_0D3ADE49_1F1E_4765_8CAC_CD50AE50E4AB` |  |
| Werkbon | Association | betreft | Bouwdeelelement | 0..* → 0..* | `EAID_171A032E_1B57_4780_A993_4E676DD67B5B` |  |
| Werkbon | Association | betreft | Vastgoedobject | 0..* → 1..1 | `EAID_8C08F940_4102_401d_827A_22095920AC7F` |  |
| Werkbon | Association | betreft | Bouwdeel | 0..* → 0..* | `EAID_AEE8935F_0754_4b89_A835_BAAB9099E663` |  |
| Zakelijk Recht | Association | heeft | Kostenplaats | 0..* → 1 | `EAID_A0BCF57E_3731_49c0_AC99_256F66DD032D` |  |
| Zakelijk Recht | Association | pacht | Pachter | 1..* → 0..* | `EAID_C15F1759_2467_477e_8A57_60AD1EA11BD5` |  |
| Zakelijk Recht | Association | heeft eigenaar | Eigenaar | 0..* → 0..* | `EAID_CB8AA91B_F488_4c76_A385_6989E086960E` |  |
| Zakelijk Recht | Generalization |  | ZakelijkRecht |  →  | `EAID_6B2C12F4_9570_41fc_A6D5_620F57C33612` |  |
