<!-- gegenereerd door tools/ggm.py; hash: e3b305c17749b27db56e7ee604c84e5f721d6b6fb48f365833f46f6c5d5a4391 -->
# ICT

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Aanvraag | `EAID_446E3931_B9F2_4b5c_80E7_5B240B8F816F` | (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht. |  |
| Applicatie | `EAID_A8945FD7_EA20_418e_8E7F_18F13F16E338` | Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers. | naam, categorie, beheerstatus, packagingstatus, applicatieURL, guid, omschrijving, beleidsdomein |
| Attribuutsoort | `EAID_8D273DE5_3529_4652_BCA1_F86B28F26017` | Attribuutsoort – Stereotype «Attribuutsoort»: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass). Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in §2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype «Attribuutsoort». Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip ‘gegeven’. | naam, herkomst, definitie, herkomstDefinitie, datumOpname, domein, lengte, patroon, toelichting, indicatieMaterieleHistorie, kardinaliteit, authentiek, indicatieAfleidbaar, mogelijkGeenWaarde, identificerend, id, stereotype, precisie, ea_guid |
| Classificatie | `EAID_81F207D0_A071_48c7_8C4C_25F8D25A3DE8` | Ordening van informatieobjecten in een logisch verband, zoals vastgelegd in een classificatieschema. | bevatPersoonsgegevens, gerelateerdPersoonsgegevens |
| CMDB-item | `EAID_B027D022_41D9_4c63_A63D_8F5111689564` | Item in een Configuratie Management DataBase | naam, beschrijving |
| Database | `EAID_FFD22E11_7A3A_459a_B575_928C67E8D1F3` | Een applicatiecomponent die een dataset bevat. | databaseInstantie, omschrijving, DBMS, architectuur, OTAP, databaseVersie, vlan |
| Datatype | `EAID_7EFBF1CA_EC6E_4b8a_B97F_453CA32AB9A5` | Attribuutsoort – Stereotype «Attribuutsoort»: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass). Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in §2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype «Attribuutsoort». Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip ‘gegeven’. | naam, herkomst, definitie, datumOpname, domein, lengte, patroon, toelichting, id, ea_guid, kardinaliteit |
| Dienst | `EAID_45AFD4E2_9909_4c33_93CE_F2466B85CA0F` | Het uitvoeren van werkzaamheden met een continu of periodiek karakter om waarde te realiseren voor een afnemer. |  |
| Domein/Taakveld | `EAID_BEFEC56A_EF6C_49f0_9368_7E46F75D9562` | Kennisgebied of activiteit gekarakteriseerd door een verzameling van concepten, begrippen en/of waarden |  |
| Externe Bron | `EAID_144D1047_35BB_4926_9472_895D89DC2E0C` | Bron buiten de eigen organisatie | guid, naam |
| Gegeven | `EAID_E846CC36_DF4A_4398_AE4C_122CAFEBAEAA` | bekend feit waaruit je gevolgtrekkingen kunt maken | id, naam, alias, toelichting, stereotype, ea_guid |
| Generalisatie | `EAID_0CF1C34D_8AD5_4ac5_8538_87252E66A8C8` | De typering van het hiërarchische verband tussen een meer generiek object van een objecttype en een meer specifiek object van een ander objecttype waarbij het laatstgenoemde object eigenschappen van het eerstgenoemde object overerft. Toelichting Een generalisatierelatie geeft aan dat bepaalde eigenschappen van een objecttype (vaak attribuutsoorten en/of relatiesoorten) ook gelden voor de gerelateerde objecttypen, én dat deze qua semantiek, structuur en syntax gelijk zijn. We spreken dan van een supertype met subtypen. De modelelementen die generiek gelden worden in een generiek objecttype, het supertype, gemodelleerd en deze worden overerft door elk subtype (minimaal twee) die de generalisatie relatie legt naar dit generieke objecttype. Voorbeeld: PERCEEL is specialisatie van KADASTRAAL ONROERENDE ZAAK, APPARTEMENTSRECHT is specialisatie van KADASTRAAL ONROERENDE ZAAK. PERCEEL en APPARTEMENTSRECHT hebben beide ‘Kadastrale aanduiding’ en een ‘relatie met ONROERENDE ZAAK FILIATIE’. | naam, herkomst, definitie, herkomstDefinitie, datumOpname, id, ea_guid, toelichting, indicatieMaterieleHistorie |
| Hardware | `EAID_6C92F0F8_BC92_428c_B729_1A10D515DAEF` | Alle fysieke componenten of onderdelen die in een computer een rol spelen. |  |
| Inventaris | `EAID_D0AB8CF6_F6CC_4337_BE07_DFE6B3CEFBB3` | Een inboedel of een opsomming van voorwerpen op een bepaalde plaats, gemaakt volgens een vaste procedure. |  |
| Koppeling | `EAID_AB7CF266_388F_413a_92D0_B2FA67C75633` | Verbinding tussen twee systemen | direct, beschrijving, toelichting |
| Licentie | `EAID_2E5F9AF9_D1BA_4dc0_9621_4101D24B8ABD` | Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden |  |
| Linkbaar CMDB-item | `EAID_C0F1A08E_C6CD_4524_A2E0_0E5CA483DCFD` | Niet opnemen |  |
| Log | `EAID_5492ED6D_608E_465e_B975_BCADAAA3EE7F` | Registratie van gegevens. | tijd, korteOmschrijving, omschrijving |
| Melding | `EAID_6100B3C7_FBCE_434d_BA48_E067B9CF84A7` | De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend |  |
| Nertwerkcomponent | `EAID_DD277E82_0CA5_4460_918F_9178B5F01886` | Een *netwerkcomponent* is een hardware- of softwareonderdeel dat een **specifieke functie vervult binnen een netwerk** om communicatie, gegevensuitwisseling of het beheer van netwerkverkeer mogelijk te maken. |  |
| Notitie | `EAID_354E5545_D067_4b81_9D1D_C5F5FFB532C7` | Korte, zakelijke uiteenzetting op schrift | datum, inhoud |
| Objecttype | `EAID_A2451674_6C19_4bf9_81F9_57CDE2F60144` | De typering van een groep objecten (in de werkelijkheid) die binnen een domein relevant zijn en als gelijksoortig worden beschouwd. Toelichting Jan, Piet en Marie zijn mensen die vanuit het Burgerzaken-domein beschouwd worden als objecten van het type ‘natuurlijk persoon’. In een ander domein, ‘de volksmond’, noemen we dit ‘mens’ wat ook een objecttype is. In weer een ander domein is Jan van het type ‘vergunninghouder’ en Piet en Marie niet, omdat aan hen (nog) nooit een vergunning verleend is. Objecttypen zijn een abstractie van de werkelijkheid oftewel we beogen hiermee de werkelijkheid zo getrouw mogelijk te beschrijven, binnen de context van het domein. Dit staat geheel los van het vastleggen van gegevens over objecten van een type in een registratie. Daartoe is veelal een interpretatie nodig (van die werkelijkheid cq. die objecttypen) naar eenheden die in een registratie vastgelegd kunnen worden (records, entiteiten e.d.) op basis van andere overwegingen. | naam, herkomst, definitie, herkomstDefinitie, datumOpname, uniekeAanduiding, populatie, kwaliteit, toelichting, indicatieAbstract, id, stereotype, ea_guid |
| Onderwerp | `EAID_2AA9DB3B_D79C_490d_8776_DA1CB25E9B09` | Op de meest karakteristieke elementen gebaseerde en in woord of eenvoudige zinstructuur samengevatte aanduiding van de inhoud van een document |  |
| Package | `EAID_ACE86CFF_D6D0_4cbd_8395_99BD763F1B37` | Een samengesteld bestand of een directory die een aantal bestanden bevat, maar welke als één bestand aan de gebruiker getoond word | naam, status, proces, project, toelichting |
| Prijzenboek | `EAID_F1489610_1E50_4328_8CD8_F41E9CE0C0D8` | Beschrijving van gangbare onderhoudsactiviteiten met de bijbehorende, actuele prijzen en normen voor de uitvoering. |  |
| Product | `EAID_D5DD2F67_6A1F_46b0_972E_795ECC4B2E4F` | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. |  |
| Relatiesoort | `EAID_DFD2814E_7D36_45e2_B082_2ED574A409E1` | De typering van het structurele verband tussen een object van een objecttype en een (ander) object van een ander (of hetzelfde) objecttype. Toelichting Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen. Als het voor het desbetreffende domein van belang is om die eigenschap te modelleren als onderdeel van een ander objecttype, dan maakt de relatiesoort die eigenschap beschikbaar voor het eerstgenoemde objecttype. Bijvoorbeeld, een attribuutsoort van het objecttype PERSOON zou kunnen zijn ‘Naam geregistreerd partner’ (naast de attribuutsoort ‘Naam’ van PERSOON). De naam van de geregistreerde partner komt evenwel ook beschikbaar met een relatiesoort van PERSOON naar PERSOON: “heeft geregistreerd partnerschap met”. Zie ook het eerder genoemde voorbeeld van SCHIP en MOTOR. Voorbeeld: relatiesoorten “VERBLIJFSOBJECT is gelegen in een PAND” en “SUBJECT heeft als correspondentieadres WOONPLAATS”, of korter, “gelegen in”, “postadres”. Wanneer een relatie (UML-assocation) gebruikt wordt om objecten aan elkaar te verbinden, zonder dat er eigenschappen over deze relatie worden vastgelegd, dan heeft deze het stereotype «Relatiesoort». | naam, herkomst, definitie, herkomstDefinitie, datumOpname, toelichting, indicatieMaterieleHistorie, kardinaliteit, authentiek, unidirectioneel, id, indicatieAfleidbaar, ea_guid, mogelijkGeenWaarde |
| Server | `EAID_3AFD7E5F_8061_4776_A332_334AF4125E7D` | Computer die in een netwerk een ondersteunende taak vervult. | serverID, organisatie, servertype, IPAdres, vlan, serienummer, locatie, actief |
| Software | `EAID_0B3C37DD_42A1_4b6b_B534_CD276112FD3B` | Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren |  |
| Storing | `EAID_4E5F272E_00CA_481c_A51B_7D08B5E6B0A9` | Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren. |  |
| Telefoniegegevens | `EAID_DDD2167F_4A0F_468b_894E_6BB9ED9DA5E0` | Gegevens die worden bewaard van telefoongesprekken |  |
| Toegangsmiddel | `EAID_D67A4AC2_9A17_4cd0_82D7_732A89018FDA` | Een middel waarmee men zich toegang tot iets kan verschaffen. |  |
| Versie | `EAID_39445166_1EAB_43f8_9F5C_89EA606605EE` | De versie-aanduiding van een object. | versienummer, status, datumEindeSupport, licentie, aantal, kosten |
| Vervoersmiddel | `EAID_E8C75DAB_F9AE_4fe2_9114_870434F2EA80` | Een voertuig dat zich over het land verplaatst. |  |
| Wijzigingsverzoek | `EAID_EFBF46D1_6A51_44fd_BAEA_47BCDFEEE27A` | Een aanvraag voor wijziging |  |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Applicatie | Association | heeft versies | Versie | 1 → 1..* | `EAID_28D220D9_A7C8_4054_A2E4_2AB35D150EDA` |  |
| Applicatie | Association | heeft leverancier | Leverancier | 0..* → 0..1 | `EAID_35D9FE88_82DF_4953_881F_3AA8A3828695` |  |
| Applicatie | Association | heeft documenten | Document | 0..* → 0..* | `EAID_432403CA_DC70_4825_A02A_08D2207DF358` |  |
| Applicatie | Association | bevat | Gegeven | 0..1 → 0..* | `EAID_5125EA2E_16E9_411b_A20F_802E0B335037` |  |
| Applicatie | Association | rollen | Medewerker | 0..* → 0..* | `EAID_69D9DF4D_0CA8_46e6_8183_C7A6BA604AAC` |  |
| Applicatie | Association | heeft herkomst | Batch | 1..1 → 0..* | `EAID_B90C1086_1ADC_4b38_9B54_A709EBB2DAE3` |  |
| Applicatie | Association | heeft notities | Notitie | 1 → 0..* | `EAID_E8FABB8C_972D_43ce_805C_578C0E4B983B` |  |
| Applicatie | Association | heeft packages | Package | 1 → 0..* | `EAID_F0223073_605B_4920_ABF7_6620F13A1BB6` |  |
| Applicatie | Generalization |  | Linkbaar CMDB-item |  →  | `EAID_EBF0C505_6860_4103_A0D5_15DF00F88114` |  |
| Attribuutsoort | Association | heeft | Datatype | 0..* → 0..1 | `EAID_0A4EE071_9E38_4a5c_A701_0ECACC233BB1` |  |
| CMDB-item | Association | heeft changelog | Log | 1..1 → 0..* | `EAID_5410F48D_F52E_4ec6_A270_59AD05B60075` |  |
| Database | Association | server van database | Server | 0..* → 1 | `EAID_647B7DC0_6FCE_4d30_9CC7_9739BA6627E8` |  |
| Database | Generalization |  | Linkbaar CMDB-item |  →  | `EAID_D3B2CB64_5809_4f22_9702_11BF9D5D31E8` |  |
| Dienst | Association | valt binnen | Domein/Taakveld | 0..* → 1 | `EAID_14C5A9DD_7317_48cc_BDD1_1C2E91A58702` |  |
| Dienst | Association | start | Zaaktype | 0..* → 0..1 | `EAID_C447377F_C042_4e0b_A045_CCF4CD03698B` |  |
| Dienst | Association | heeft | Onderwerp | 0..* → 1 | `EAID_D3BFC0FC_375B_4acf_B588_D0C21597C84A` |  |
| Dienst | Association | betreft | Product | 0..* → 0..1 | `EAID_F800F9CB_3617_4d92_B5F4_5B5C9AF87002` |  |
| Domein/Taakveld | Association | valt binnen | Onderwerp | 1 → 0..* | `EAID_2B95DC1E_3A13_4c88_AD8F_D42DA96B45FD` |  |
| Domein/Taakveld | Association | valt binnen | Product | 1 → 0..* | `EAID_C5CAADE8_D3FE_4a2a_8CE0_8C3F5DC74DB1` |  |
| Externe Bron | Association | levert | Gegeven | 0..1 → 0..* | `EAID_42164840_C756_492e_A778_D778B6B90C19` |  |
| Gegeven | Association | geclassificeerd als | Classificatie | 0..* → 0..* | `EAID_827C0C04_BB19_4cca_B2D2_F8F589124A38` |  |
| Gegeven | Association | gedefinieerd door | Objecttype | 0..* → 0..1 | `EAID_D04B4B9C_15D5_4421_A672_0AA90EE62A1B` |  |
| Hardware | Generalization |  | CMDB-item |  →  | `EAID_DB85B252_E0E1_44a7_81E3_93C293FD9B8C` |  |
| Inventaris | Generalization |  | CMDB-item |  →  | `EAID_EFA338EB_CD5F_4dca_9AC1_505E986514EB` |  |
| Koppeling | Association | link naar | Linkbaar CMDB-item | 0..* → 1 | `EAID_6CA6F084_4DE0_4c35_AC1E_1E2F6FC54177` |  |
| Licentie | Generalization |  | CMDB-item |  →  | `EAID_5A9D905C_7FFC_4a63_A4EB_79CA083B2FD7` |  |
| Linkbaar CMDB-item | Association | link van | Koppeling | 1 → 0..* | `EAID_24F1516A_B3A7_4fb0_8FBA_5258470B7301` |  |
| Linkbaar CMDB-item | Generalization |  | CMDB-item |  →  | `EAID_90A8858D_F461_497b_A5B8_498FE330EE0B` |  |
| Nertwerkcomponent | Generalization |  | CMDB-item |  →  | `EAID_B8ECB96C_36B2_450e_AD4D_B1AA172E1BBF` |  |
| Notitie | Association | auteur | Medewerker | 0..* → 1 | `EAID_7BAEAE6A_9C78_49f7_BBC4_D7750ABA40F6` |  |
| Objecttype | Association | bezit | Relatiesoort | 1 → 0..* | `EAID_36EB4818_D2B7_4dc9_B3E3_9B4E71091C92` |  |
| Objecttype | Association |  | Generalisatie | 1 → 0..1 | `EAID_D4FC4F07_C62A_411b_9887_DFC4A31ABF95` |  |
| Objecttype | Association | bezit | Attribuutsoort | 0..1 → 0..* | `EAID_FB2504BA_3DEF_45eb_B581_79D4B7B6B7AA` |  |
| Prijzenboek | Association | heeft prijs | Product | 0..* → 0..* | `EAID_DD042091_C78F_421c_954A_3C8B4C688527` |  |
| Product | Association | betreft | Zaaktype | 0..1 → 0..* | `EAID_383C6482_162A_4406_A2A3_E0CBFAE01B24` |  |
| Relatiesoort | Association | gerelateerdObjecttype | Objecttype | 0..* → 1..1 | `EAID_3DEBAD4B_F4C6_42fc_9CC3_25E496DE744B` |  |
| Server | Association | heeft leverancier | Leverancier | 0..* → 0..1 | `EAID_6F613631_A22B_43ba_8D17_71ADC062BC2E` |  |
| Server | Generalization |  | Linkbaar CMDB-item |  →  | `EAID_A785B084_F178_41fa_869D_2AE6BEF5BE7C` |  |
| Software | Generalization |  | CMDB-item |  →  | `EAID_AD651614_CA9B_4f11_A212_CD12CB2830CD` |  |
| Toegangsmiddel | Generalization |  | CMDB-item |  →  | `EAID_36305C3C_7347_455c_85EB_A63018995066` |  |
| Vervoersmiddel | Generalization |  | CMDB-item |  →  | `EAID_B3EAA4F8_EB2B_438a_86BC_DDFBA14B473E` |  |
