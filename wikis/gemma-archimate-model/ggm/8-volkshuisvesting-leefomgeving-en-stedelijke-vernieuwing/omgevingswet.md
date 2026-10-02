<!-- gegenereerd door tools/ggm.py; hash: b316dad8f153bb620aa680dad0ec76f613cfb8825aeff31efebba8927d74f7b8 -->
# Omgevingswet

Taakveld: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing. Alleen objecttypen; letterlijke definities uit het GGM.

## Activiteit

Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd.

Attributen: naam, groep, NEN3610ID.

GUID: `EAID_8BE600D0_EBF4_475b_8801_F387A5D39009`

Relaties:

- gerelateerde activiteit → Activiteit (*Association*, 1 → 0..1, `EAID_1E3E1DDF_D648_4c8d_9142_623182ED7701`)
- bovenliggende activiteit → Activiteit (*Association*, 1 → 0..1, `EAID_4328D0AB_64ED_46a3_8820_42C6634E70EA`)
- is verbonden met → Locatie (*Association*, 0..* → 1..*, `EAID_552A06F1_91B6_4510_96FC_82C5E0C72951`)

## Beperkingsgebied

Een bij of krachtens de wet aangewezen gebied, waar vanwege de aanwezigheid van een werk of object regels gelden, ten aanzien van het beperken van activiteiten die gevolgen hebben of kunnen hebben voor dat werk of object.

Attributen: naam, groep.

GUID: `EAID_E93E03EF_259F_4bda_A875_A0E60CB18E89`

Relaties:

- → Gebiedsaanwijzing (*Generalization*,  → , `EAID_59758FFB_B19D_4c70_8A4B_0F4C2921035D`)

## Bevoegd Gezag

Bestuursorgaan dat bevoegd is tot het geven van een beschikking of het nemen van een ander besluit.

GUID: `EAID_FB771E02_8FE3_496b_B99B_CF4A496A7B80`

Relaties:

- → Rechtspersoon (*Generalization*,  → , `EAID_27A927F8_BCC3_419d_AF60_658CBF76E285`)

## Conclusie

Conclusie van de check. Antwoord op de vraag of ik een melding moet doen of een vergunning aan moet vragen voor een bepaalde activiteit.

GUID: `EAID_C2A7756C_87E9_44f0_85A9_673F3956BB48`

Relaties:

- → Toepasbare Regel (*Generalization*,  → , `EAID_1B9439BF_6E55_4046_AA5F_66B5697C9CE3`)

## Functie

Een samenhangende verzameling van rollen

Attributen: naam, groep.

GUID: `EAID_3BDD29C7_FBCD_4c90_A520_8187E2D9BD57`

Relaties:

- → Gebiedsaanwijzing (*Generalization*,  → , `EAID_89EBED65_532E_4bbf_AEA2_9D985FB0CB00`)

## Gebiedsaanwijzing

Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels.

Attributen: NEN3610ID, groep, naam.

GUID: `EAID_503BD06E_E063_46f2_8B43_BF75A143D6C4`

Relaties:

- verwijst naar → Locatie (*Association*, 0..* → 1..*, `EAID_D87D2273_95F5_41bd_A11A_2EB5E4686B22`)

## Gemachtigde

Een Natuurlijk Persoon of een Niet Natuurlijk Persoon die als vertegenwoordiger van een Initiatiefnemer optreedt.

GUID: `EAID_02BDED5E_9106_4aed_94C2_513689353284`

Relaties:

- dient in  → Verzoek (*Association*, 0..1 → 1..*, `EAID_A4AA28ED_CB05_48ee_A490_7E01CD0B7EA4`)
- → Rechtspersoon (*Generalization*,  → , `EAID_9FD4E06C_602A_4f17_94EF_FFF6768013F5`)
- is gemachtigd door → Initiatiefnemer (*Usage*, 0..1 → 1..*, `EAID_6F32D49E_6315_4594_9D48_76649170C2FD`)

## Idealisatie

Vastlegging van de manier de begrenzing van Locatie voor deze Juridische regel geïnterpreteerd moet worden en door het bevoegd gezag bedoeld is.

Attributen: naam, omschrijving.

GUID: `EAID_4942AB0A_804B_4043_BD3C_7F65E2D697E0`

## Indieningsvereisten

Dat wat de initiatiefnemer moet aanleveren om het bevoegd gezag een aanvraag te kunnen laten beoordelen. De indieningsvereisten is de set aan informatie (gegevens en / of bijlagen) die aan een aanvraag moet worden toegevoegd voor een bepaalde vergunning of melding.

GUID: `EAID_8587D910_7A9C_46d8_BF27_27433E9B6DAD`

Relaties:

- → Toepasbare Regel (*Generalization*,  → , `EAID_12B5F13C_51AA_4cae_A23E_439F1EE85110`)

## Initiatiefnemer

Een Natuurlijk Persoon of een Niet Natuurlijk Persoon die het initiatief neemt tot (fysieke) ingrepen in de (leef)omgeving en daartoe een Verzoek bij het Bevoegd Gezag indient.

GUID: `EAID_E38BEAEF_03C4_439b_8A64_663886C1D6F9`

Relaties:

- heeft als verantwoordelijke → Verzoek (*Association*, 1 → 1..*, `EAID_93E13784_D545_4f09_85F0_4E459FBB4EED`)
- → Rechtspersoon (*Generalization*,  → , `EAID_55B2F56E_0907_49e4_B663_E71D0F8F7F4C`)

## Instructieregel

Objecttype Instructieregel Naam Definitie Toelichting Instructieregel De beschrijving van een juridische regel die een instructie is voor een extern omgevingsdocument of een orgaan. Het betreft hier juridische regel die instructie geeft aan andere overheden, gericht op externe omgevingsdocumenten, of een taakuitoefening. Een ander omgevingsdocument is bijvoorbeeld een Omgevingsplan, Omgevingsverordening en Waterschapsverordening. Een taakuitoefening is voor bijvoorbeeld een gemeentebestuur of een wildbeheereenheid. Een instructieregel is alleen gericht op een Omgevingsnorm of een Gebiedsaanduiding, zoals een Functie of een Beperkingengebied (en eventueel meerdere).

Attributen: instructieregelInstrument, instructieregelTaakuitoefening.

GUID: `EAID_A6C71E4C_CB46_41ae_8A61_C8080BB92A55`

Relaties:

- beschrijft gebiedsaanwijzing → Gebiedsaanwijzing (*Association*, 0..* → 0..*, `EAID_328C510A_1E45_4d18_885B_5D37558B5993`)
- → Juridische Regel (*Generalization*,  → , `EAID_51D0E188_C95B_43fe_B1EC_031D8BD13FA7`)

## Juridische Regel

De beschrijving van een regel met juridische werkingskracht. Een regel betreft binnen de Omgevingswet veelal activiteiten, en/of normen en/of functies en/of beperkingengebieden.

Attributen: omschrijving, thema, regeltekst, datumStart, datumEindeGeldigheid, datumInWerking, datumBekend.

GUID: `EAID_DDFF98D8_99FF_47b5_82D1_7FF2376750D6`

Relaties:

- geldt voor → Activiteit (*Association*, 1..* → 1..*, `EAID_AD68C58D_5F48_46ef_A232_5E5F1FEAE956`)
- heeft idealisatie → Idealisatie (*Association*, 0..* → 0..*, `EAID_FEF715EB_9E4F_42a4_8BF6_EE782C66738B`)
- werkingsgebied → Locatie (*Association*, 0..* → 1..*, `EAID_A05AFA08_D35E_4e53_A353_272267025927`)
- is opgenomen in → Regeltekst (*Association*, 1..* → 1, `EAID_650100B0_3544_4f97_90AF_1CA621FCD924`)
- heeft thema → Thema (*Association*, 0..* → 0..*, `EAID_18882E45_B285_482d_B88C_0A5650BD39DE`)

## Maatregelen

Beschrijft welke handelingen iemand moet uitvoeren om aan Voorschriften te kunnen voldoen.

GUID: `EAID_45591365_C55F_4735_9533_D3BBB0AB6571`

Relaties:

- → Toepasbare Regel (*Generalization*,  → , `EAID_AB6968AA_E169_4203_A1D4_C637CDFD6EFA`)

## Norm

Omgevingswaarde of een omgevingsnorm, met een normatief karakter, die beschreven worden middels normwaarden. Een normwaarde kan kwalitatief of kwantitatief zijn.

Attributen: NEN3610ID.

GUID: `EAID_081F7413_A4D0_49e7_98E2_E0F3F4299750`

Relaties:

- bevat → Normwaarde (*Association*, 1 → 1..*, `EAID_736850D3_26DB_40a3_8AF1_9FC395F0266C`)

## Normwaarde

Een van de kwantitatieve of kwalitatieve waarden van een norm. De normwaarde geeft aan wat de specifieke kwantitatieve of kwalitatieve eisen zijn, inclusief de toewijzing ervan aan de specifieke locatie(s) waar de normwaarde voor geldt.

Attributen: kwalitatieveWaarde, kwantitatieveWaardeOmvang, kwantitatieveWaardeEenheid.

GUID: `EAID_58656D46_644B_4779_A473_739C5636BA0A`

Relaties:

- geldt voor → Locatie (*Association*, 0..* → 1..*, `EAID_4E6B1E63_7D1A_4101_8409_9C024DAED35E`)

## Omgevingsdocument

In artikel 16.2 van de Omgevingswet aangemerkt instrument te weten: Omgevingsvisie, programma, omgevingsplan, waterschapsverordening, omgevingsverordening, projectbesluit of bij Algemene Maatregel van Bestuur (Omgevingsbesluit) aangewezen ander besluit of ander rechtsfiguur.

GUID: `EAID_F5434F00_CC0F_4d7b_91AE_20CBD3C60DFC`

Relaties:

- bevat → Regeltekst (*Association*, 1 → 1..*, `EAID_177A8717_5D9F_42cf_8A0A_C7F570684B01`)

## Omgevingsnorm

Een norm over de fysieke leefomgeving die in een kwantitatieve of kwalitatieve waarde wordt uitgedrukt en geen omgevingswaarde is.

Attributen: naam, omgevingsnormGroep.

GUID: `EAID_F90F8E5E_7402_4c44_AC69_91A4175E5D47`

Relaties:

- → Norm (*Generalization*,  → , `EAID_7C0BE110_2B2C_4e39_A8B8_EF105FBC6FA4`)

## Omgevingswaarde

Een norm die voor (een onderdeel van) de fysieke leefomgeving de gewenste staat of kwaliteit, de toelaatbare belasting door activiteiten en/of de toelaatbare concentratie of depositie van stoffen als beleidsdoel vastlegt.

Attributen: naam, omgevingswaardeGroep.

GUID: `EAID_6B1F7274_19A7_4349_835E_85CBEFFEE35A`

Relaties:

- → Norm (*Generalization*,  → , `EAID_AF7F4C05_D98D_4ddb_A0FE_F0361A1F9546`)

## Omgevingswaarderegel

De beschrijving van een juridische regel gericht op een gestelde omgevingswaarde. Het betreft hier een juridische regel die verplichtingen oplegt aan het bevoegd gezag dat deze regel opstelt. Een omgevingswaarderegel is alleen gericht op een Omgevingswaarde (eventueel meerdere).

Attributen: naam, groep.

GUID: `EAID_2FC6C6EB_DF35_49e6_9694_1B8BD53537B0`

Relaties:

- beschrijft → Omgevingsnorm (*Association*, 1..* → 0..*, `EAID_4AC0AAC1_7D95_463c_896B_6558A4B2BFB5`)
- beschrijft → Omgevingswaarde (*Association*, 1..* → 0..*, `EAID_D3B8659A_948C_4924_ADA3_02D6302838B7`)
- → Juridische Regel (*Generalization*,  → , `EAID_34FCD611_8785_4de3_995B_253643231D39`)

## Project

Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.

Attributen: naam, omschrijving.

GUID: `EAID_E1FAE16A_42AE_4b7d_88FC_F429079D1C4D`

Relaties:

- heeft → Projectactiviteit (*Association*, 1 → 0..*, `EAID_0F845181_E24A_470c_977D_39ED7375D456`)
- heeft → Projectlocatie (*Association*, 1 → 0..*, `EAID_04CF947C_03FA_49c9_BFC4_B20074B47588`)

## Projectactiviteit

Activiteit binnen het project

GUID: `EAID_B31B867F_061E_42d4_AB8A_DB5589602969`

Relaties:

- uitgevoerd op → Projectlocatie (*Association*, 1..* → 1, `EAID_37EC5804_46E0_4ce7_A773_E89651DBC4F1`)
- heeft betrekking op → Document (*Usage*,  → , `EAID_9AF385C9_F018_43ac_8D3A_AE960B46F8C0`)

## Projectlocatie

Fysieke locatie waar een project betrekking op heeft of wordt uitgevoerd.

Attributen: adres, kadastraalPerceel, kadastraleGemeente, kadastraleSectie.

GUID: `EAID_D60910E1_6E36_4ebb_9687_2D2B1CE66E0B`

Relaties:

- betreft → Locatie (*Association*, 0..* → 0..1, `EAID_8BDF9281_E9D1_4266_8886_FD6328BD5AF7`)

## Regel voor Iedereen

Een Juridische regel die voor eenieder werking heeft

Attributen: activiteitRegelKwalificatie.

GUID: `EAID_3D9D2E7B_525E_43d9_B08F_EDE47F8A0C94`

Relaties:

- beschrijft activiteit → Activiteit (*Association*, 1..* → 0..*, `EAID_7ED27452_E047_40e4_91F4_C35FF382C609`)
- beschrijft gebiedsaanwijzing → Gebiedsaanwijzing (*Association*, 0..* → 0..*, `EAID_5F68CFAD_1BDE_4282_B752_C889A486A68A`)
- beschrijft norm → Omgevingsnorm (*Association*, 0..* → 0..*, `EAID_4059EA35_AB7B_4587_9EFA_CB8469B6A0DD`)
- → Juridische Regel (*Generalization*,  → , `EAID_E5871441_C7F2_431e_ABD9_3ABB20998E0B`)

## Regeltekst

De kleinste zelfstandige eenheid van (een of meer) bij elkaar horende juridische regels: een artikel en lid.

Attributen: tekst, identificatie, omschrijving.

GUID: `EAID_A744FAF8_16B7_4e5d_9C10_203AA8E7C440`

Relaties:

- heeft idealisatie → Idealisatie (*Association*, 0..* → 0..*, `EAID_85F36F5F_DB13_4679_BDE9_DBA0DB8668DF`)
- werkingsgebied → Locatie (*Association*, 0..* → 0..*, `EAID_E3CEF419_1FFF_41d2_A37B_30A3788D6FFB`)
- werkingsgebied → Regeltekst (*Association*, 0..1 → 0..*, `EAID_85D7732A_FD1F_428f_8293_CC41E211B76E`)
- is gerelateerd → Regeltekst (*Association*, 0..1 → 0..*, `EAID_915CBFAB_B8BD_4677_8678_C69406BF0280`)
- heeft thema → Thema (*Association*, 0..* → 0..*, `EAID_41876C31_8F0F_4b25_9638_B28C416FC0B5`)

## Specificatie

Gesplitste opgave, vermelding van de afzonderlijke onderdelen waaruit een verzameling of een totaal bestaat

Attributen: antwoord, groepering, publiceerbaar, vraagID, vraagClassificatie, vraagreferentie, vraagtekst.

GUID: `EAID_DF63FBD0_DCA2_45bd_81E8_EE5E72D38EDE`

Relaties:

- gedefinieerd door → Projectactiviteit (*Association*, 1..* → 0..1, `EAID_ABB18284_0742_4630_87C8_845B4D011157`)

## Thema

Kernachtige weergave van de grondgedachte achter een regel.

Attributen: naam, omschrijving.

GUID: `EAID_55FC829A_906B_4cb7_87D7_5BBAE59E07A8`

Relaties:

- subthema → Thema (*Association*, 0..1 → 0..*, `EAID_64AA92C3_5AC1_40d6_806D_A60B2036CCE0`)

## Toepasbare Regel

Vanwege de leesbaarheid wordt gewerkt met de term Toepasbare regel ipv regelbeheersobject Een regelbeheerobject heeft een koppeling met een samenhangende set met regels om een afleiding te kunnen doen. Het regelbeheerobject ‘conclusie gevelaanpassing’ kan een vraag beantwoorden zoals: “Heb ik een vergunning nodig voor het veranderen van een kozijn, kozijninvulling of gevelpaneel”. Het regelbeheerobject ‘melding lozing’ beantwoordt de vraag “Wat moet ik aan informatie (gegevens en documenten) aanleveren als ik ga lozen vanuit particuliere huishoudens”. Het regelbeheerobject “Opslaan van gasolie smeerolie of afgewerkte olie in een bovengrondse opslagtank” geeft aan welke maatregelen genomen dienen te worden. Het regelbeheerobject is onderdeel van de functionele structuur. De set met regels is gedefinieerd in het Toepasbare regelbestand2.

Attributen: naam, omschrijving, domein, toestemming, soortAansluitpunt, datumBeginGeldigheid, datumEindeGeldigheid.

GUID: `EAID_10C06EB3_F94A_4005_9C66_0DAE61B96192`

Relaties:

- betreft → Activiteit (*Association*, 0..* → 1, `EAID_637A11D0_691A_4e67_8990_A924D984BD5C`)
- komt voort uit → Juridische Regel (*Association*, 0..* → 1..*, `EAID_24376BB8_FAE1_4a4b_AED2_61E7F212C79A`)
- betreft → Locatie (*Association*, 0..* → 0..*, `EAID_6DFEF1A2_B0BA_490d_AEC6_A4C777385616`)
- heeft → ToepasbareRegelBestand (*Association*, 0..* → 1..1, `EAID_DD86ACFC_507A_42ff_84CD_2ADA84514289`)
- heeft → Uitvoeringsregel (*Association*, 1..1 → 0..*, `EAID_CC057874_5639_42db_9AE1_18C649146197`)

## ToepasbareRegelBestand

Bestand met aangeleverde toepasbare regels

Attributen: datumStart, datumEindeGeldigheid.

GUID: `EAID_3120D398_95C1_42fe_B10F_4F3B6BF15D1A`

Relaties:

- bevat → Uitvoeringsregel (*Association*, 1 → 0..*, `EAID_4737BCD4_DF6F_4227_AB79_599CE2007080`)

## Uitvoerende instantie

Onderdeel van het bevoegd gezag dat uitvoering geeft aan wetten en besluiten

Attributen: naam.

GUID: `EAID_1B3A22D3_E2BA_440a_A2FD_B3D322FB1171`

## Uitvoeringsregel

De uitvoeringsregels bepalen hoe de benodigde gegevens (input data) wordt uitgevraagd. Dit kan op verschillende manieren gebeuren zoals een vraag aan een initiatiefnemer of een bevraging van een registratie.

Attributen: naam, omschrijving, regel.

GUID: `EAID_1528D03C_4F22_4d6b_A44F_605802C195C4`

## Verzoek

Een vraag aan het bevoegd gezag om een speficieke product of dienst te leveren.

Attributen: akkoordverklaring, ambtshalve, doel, datumIndiening, naam, referentieAanvrager, toelichtingLaterAanTeLeverenInformatie, toelichtingNietAanTeLeverenInformatie, toelichtingVerzoek, type, verzoeknummer, volgnummer.

GUID: `EAID_B18119D9_5BF8_498f_B9D3_ECCE7A770012`

Relaties:

- betreft → Activiteit (*Association*, 0..* → 1..*, `EAID_0064520F_0125_42ea_8D01_13183E102F6C`)
- verantwoordelijke → Bevoegd Gezag (*Association*, 0..* → 1, `EAID_2EE1E49A_814D_4f73_8F1B_D89646B57943`)
- betreft → Locatie (*Association*, 0..* → 1..*, `EAID_26D6F100_39D3_4123_86D8_C8D413E0508D`)
- betreft → Project (*Association*, 1..* → 1.., `EAID_9A2326F8_F317_4492_B873_43D70AC148E2`)
- betreft → Projectactiviteit (*Association*, 1..* → 0..*, `EAID_C0346725_D796_49c8_AF5D_0DB661B16BD1`)
- bevat → Specificatie (*Association*, 1 → 0..*, `EAID_39267C88_D96E_44bc_8455_D598A21C8799`)
- behandelaar → Uitvoerende instantie (*Association*, 0..* → 0..1, `EAID_B9B2B6A4_7021_4658_BAD1_E75645522CDC`)
- betreft eerder verzoek → Verzoek (*Association*, 0..1 → 0..*, `EAID_6CCDA8AA_865C_4096_8537_19014545BF35`)
- leidt tot → Zaak (*Association*, 0..1 → 0..1, `EAID_2E1D8835_BE1E_475b_8F1C_5815DB6EDFA8`)
- heeft bijlagen → Document (*Usage*,  → , `EAID_67DD89C8_BCAE_443e_B026_803BB7928BF6`)
- betreft → Projectlocatie (*Usage*, 1..* → 0..*, `EAID_DA6ACB79_B034_4d35_AB64_20499899A5C6`)
