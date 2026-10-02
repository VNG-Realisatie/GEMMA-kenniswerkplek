<!-- gegenereerd door tools/ggm.py; hash: c66aaaf1143ee69c90f0d2e24d6dd22c2725a4b2927ae922707c6c352342f5a3 -->
# Reden aanvraag

Taakveld: Inkomen. Alleen objecttypen; letterlijke definities uit het GGM.

## Andere reden afwijkende startdatum

*Andere reden afwijkende startdatum* is een omschrijving van een **reden waarom de startdatum van een dienst of uitkering afwijkt van de standaard startdatum**, voor zover deze reden niet onder de standaardcategorieën valt.

Attributen: omschrijvingBijzondereReden.

GUID: `EAID_237c7e1c_5893_475f_be3f_49b629316e1e`

Relaties:

- Reden afwijkende startdatum generaliseert Andere r → Reden afwijkende startdatum (*Generalization*,  → , `EAID_634caf04_db91_43b0_8313_8e9670c5e246`)

## Andere reden verzoek

*Andere reden verzoek* is een categorie voor een **overige reden** waarom een aanvraag wordt gedaan die niet onder de standaard-redencategorieën valt binnen het *Reden aanvraag*-model.

Attributen: Opgave financiële ondersteuning, Specificatie geldtekort.

GUID: `EAID_1E8815BF_5BAC_6978_BF60_2791C1C96FC3`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Ander → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_12D51586_44A6_3CD2_BA7A_2791C4C3BEFF`)

## Diensten::Aanvraag

Een aanvraag is een verzoek van een burger, bedrijf of organisatie aan een overheid om een specifieke dienst te verkrijgen of een besluit te ontvangen (bijv. vergunning, subsidie, paspoort of beschikkingsbesluit).

GUID: `EAID_2D94CF02_97C5_4621_B225_EA742445A235`

Relaties:

- Is aanleiding tot → Reden aanvraag (*Aggregation (shared)*, 1..* → 0..*, `EAID_390DEF15_81E5_4d57_ABF8_2056B8229470`)

## Diensten::Aanvraag levensonderhoud

Een aanvraag levensonderhoud is het formele verzoek van een persoon aan een gemeentelijke of overheidsinstantie om een uitkering of financiële ondersteuning te verkrijgen die het inkomen aanvult zodat in het basislevensonderhoud kan worden voorzien.

GUID: `EAID_1F9DBD7C_EBF3_41c8_8F00_2F6169FE107C`

Relaties:

- → Diensten::Aanvraag (*Generalization*,  → , `EAID_DD6C1686_A422_41a2_879B_8F6B2D191A23`)

## Gestopt betaald werk

*Gestopt betaald werk* is de situatie waarin iemand **zijn of haar betaalde arbeidsrelatie heeft beëindigd**, waardoor het reguliere inkomen uit werk is komen te vervallen en dit relevant is voor de beoordeling van een uitkeringsaanvraag of inkomenssituatie.

Attributen: Afwijsreden WW-aanvraag, Bedrijfsadres, Bedrijfstelefoonnummer, Contractperiode, Laatste salarisdatum, Minimaal 26 weken van 36 gewerkt, Naam bedrijf, Ontslagbrief ontvangen, Ontslagvergoeding ontvangen, Reden einde werk, Specificatie reden einde werk, Wettelijke stappen gezet, WW-uitkering aangevraagd, Ziektewet-uitkering aangevraagd.

GUID: `EAID_16333246_B1C9_E9E9_D5B6_2791C02E05CB`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_1519A086_0786_B785_5064_2791C47EFB34`)

## Gestopt of verkocht eigen bedrijf

*Gestopt of verkocht eigen bedrijf* is de situatie waarin een persoon zijn of haar **bedrijf volledig beëindigt of overdraagt/verkoopt**, waardoor de zelfstandige activiteit ophoudt en de reguliere inkomsten uit de onderneming verdwijnen.

Attributen: Datum gestopt met eigen bedrijf, KvK-inschrijfnummer, Reden eigen bedrijfs gestopt, Uitgeschreven bij Kamer van Koophandel, Verkoopbedrag.

GUID: `EAID_0B7F7AD1_661C_8F1C_4F9A_2791C1C74BAB`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_1EE28C06_2D5D_9AC3_A86C_2791C4C1EDDD`)

## Gestopte bijstanduitkering

*Gestopte bijstandsuitkering* is een reden van aanvraag binnen de GBI-Ontologie die aanduidt dat een cliënt een inkomensdienst aanvraagt omdat **een eerder ontvangen bijstandsuitkering is beëindigd**.

Attributen: Reden einde bijstandsuitkering, Situatie gewijzigd, Specificatie reden einde bijstand, Specificatie wijziging situatie.

GUID: `EAID_15ABBF00_EC46_89CA_680B_2791C070D8E5`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_1A2A4C46_FBF3_C60A_9171_2791C4C06238`)

## Gestopte detentie

*Gestopte detentie* is een reden van aanvraag binnen het GBI-model die aangeeft dat een persoon **vrij is gekomen uit detentie**, waardoor de detentie-periode is beëindigd en dit relevant is voor de beoordeling van een nieuwe aanvraag of wijziging in de ondersteuningsbehoefte.

Attributen: Duur detentie, Einddatum detentie, Soort uitkering voor detentie, Specificatie uitkering voor detentie, Uitkering voor detentie.

GUID: `EAID_16F72E30_A6E2_CEC4_6AB8_2791C1C8CC09`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_08ECBD0C_12AE_9987_7FF8_2791C4C24BB1`)

## Gestopte of verlaagde alimentatie

*Gestopte of verlaagde alimentatie* is een reden van aanvraag binnen het GBI-Ontologiemodel die aangeeft dat een persoon een inkomensdienst aanvraagt omdat **alimentatiebetalingen zijn gestopt of verlaagd**, waardoor het reguliere ondersteuningsinkomen is verminderd.

Attributen: Einddatum alimentatie, LBIO ingeschakeld, Nabestaandeuitkering aangevraagd, Opgave financiële ondersteuning, Reden einde of verlaagde alimentatie.

GUID: `EAID_1632E282_377B_77CF_BF11_2791C070C097`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_17A964F7_091F_58CD_BA5F_2791C4C013D4`)

## Gestopte studiefinanciering

*Gestopte studiefinanciering* is een reden van aanvraag binnen de GBI-Ontologie die aangeeft dat een persoon een inkomensdienst aanvraagt omdat **de studiefinanciering is beëindigd of gestopt**, waardoor het (studie)inkomen wegvalt en inkomensondersteuning nodig kan zijn.

Attributen: Einddatum studiefinanciering, Specificatie studiefinanciering.

GUID: `EAID_1F0AACC8_0CDE_849C_C1CC_2791C070CCF8`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_0B1FEBBE_F717_2EF7_A7A3_2791C4C00CBC`)

## Gestopte uitkering

*Gestopte uitkering* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een cliënt een inkomensdienst aanvraagt omdat **een eerdere uitkering is beëindigd**, waardoor opnieuw inkomensondersteuning nodig is.

Attributen: Einddatum uitkering, Einde uitkering in bezwaar, Gedeeltelijk arbeidsongeschikt na 50e, Ingangsdatum WGA binnen periode, IOAW-uitkering ontvangen, minderDan35%AO, Reden einde uitkering, Specificatie andere uitkering, Specificatie reden einde uitkering, Startdatum WW- of WGA-uitkering, Uitkering, Werkloosperiode.

GUID: `EAID_1BDF5AAF_EDC4_87BC_16F2_2791C06DC1FA`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Gesto → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_144C04C1_6581_426A_113C_2791C493A420`)

## Ingang bijstandsuitkering

In de meeste gevallen is de startdatum van een dienst gelijk aan de datum eerste melding (melddatum). Echter, er zijn redenen om hiervan af te wijken. In dat geval wijkt de startdatum af van de melddatum. Ingangsdatum uitkering bevat een Reden afwijkende startdatum om op te nemen met welke reden een afwijkende ingangsdatum gehanteerd wordt. Ingang bijstandsuitkering kan, zoals de naam al doet vermoeden, alleen van toepassing zijn indien het een aanvraag betreft van het diensttype 'Aanvulling levensonderhoud' (ALO)'.

Attributen: Afwijkende ingangsdatum, Datum melding bij gemeente, Gewenste startdatum uitkering, Na melding gemeente digitaal verwezen.

GUID: `EAID_0572BF37_A778_273A_32B0_2791C2CC601A`

Relaties:

- Bevat → Diensten::Aanvraag levensonderhoud (*Aggregation (composite)*, 0..* → 1, `EAID_11ABCC81_EAA3_4451_9227_D7D29A1D5D68`)
- bevat → Reden afwijkende startdatum (*Aggregation (composite)*, 0..1 → 0..1, `EAID_8d96be6a_6ca5_4cc9_967f_f8fb099bc9c4`)

## Levenssituatie::Levenssituatie

De levenssituatie is de kwaliteit van de omgeving en omstandigheden waarin een persoon leeft en functioneert op een bepaald moment.

GUID: `EAID_4B7F5B5B_CCC7_465e_9908_E83620EEAE89`

Relaties:

- Is reden tot → Reden aanvraag (*Association*, 0..1 → 0..*, `EAID_DF1C9317_8A8A_49ec_B37E_560CE1C0C084`)

## Opname instelling

*Opname instelling* is een reden van aanvraag binnen de GBI-Ontologie die aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **(net) is opgenomen in of vrijgekomen uit een instelling**, wat financiële gevolgen heeft voor de inkomenssituatie.

Attributen: Einddatum opname, Startdatum opname.

GUID: `EAID_1ac5aa8f_eb60_4683_acb8_ca3308da1c3d`

Relaties:

- Reden afwijkende startdatum generaliseert Opname i → Reden afwijkende startdatum (*Generalization*,  → , `EAID_479249f5_40e7_4dce_a4f5_cf17f49b5f7b`)

## Overleden partner

*Overleden partner* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat **de partner is overleden**, met als gevolg dat het huishoudinkomen is verminderd.

Attributen: Meer dan 45% arbeidsongeschikt, Nabestaandeuitkering aangevraagd, Reden ANW afgewezen.

GUID: `EAID_201D0432_BDE5_700A_13F6_2791C071691F`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Overl → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_1CFCA630_105B_574F_6231_2791C4C19256`)

## Reden aanvraag

Reden waarom dienst wordt aanvraagd bij gemeente.

Attributen: Diensttype, Gewenste ingangsdatum.

GUID: `EAID_cac6d8c1_42e6_41cb_9907_3c65c081afba`

## Reden aanvraag Levensonderhoud

*Reden aanvraag Levensonderhoud* is een categorie binnen het GBI-Ontologiemodel die aangeeft dat een cliënt een inkomensdienst aanvraagt vanwege een situatie waarin **middelen voor levensonderhoud ontbreken of zijn weggevallen**, en deze aanleiding geeft voor ondersteuning.

Attributen: Onvoldoende inkomen, Reden, Verblijfstatus, Wijziging gezin, Zelfstandige.

GUID: `EAID_0BCC5755_9F69_A5D7_4387_2791BFCD4782`

Relaties:

- Reden aanvraag generaliseert Reden aanvraag Levens → Reden aanvraag (*Generalization*,  → , `EAID_ee94718b_fbc9_44b6_a525_aca13716beb8`)

## Reden afwijkende startdatum

*Reden afwijkende startdatum* is een categorie binnen het GBI-Ontologiemodel die aangeeft **waarom de ingangsdatum van een dienst of uitkering afwijkt van de standaard startdatum** (bijv. de datum van eerste melding).

Attributen: Reden afwijking aanwezig, Reden Niet Eerder Aanvragen, RedenAfwijkendeStartdatumType.

GUID: `EAID_ed8f8dba_b936_40ad_b443_1ee91b8fe046`

## Verbroken relatie

*Verbroken relatie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt doordat **de (huwelijkse/samenlevings)relatie is beëindigd**, met financiële gevolgen voor het levensonderhoud.

Attributen: Afspraak onderhoudsbijdrage gemaakt, Datum relatie verbroken, Geregistreerde partner, Opgave financiële ondersteuning.

GUID: `EAID_273AA921_78AD_0107_6D04_2791C07149E9`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Verbr → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_056A531B_AB5F_21B7_009B_2791C4C14E2B`)

## Vertrek uit asielzoekerscentrum

*Vertrek uit asielzoekerscentrum* is een subtype van **Reden aanvraag** in het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **recentelijk een asielzoekerscentrum heeft verlaten**, waardoor de financiële situatie is veranderd.

Attributen: Bedrag weekgeld COA, Einddatum weekgeld COA, Ingangsdatum huurcontract, Weekgeld COA, Weekgeld COA stopt.

GUID: `EAID_109FA03E_8C65_8EF6_C7F0_2791C1C80AFE`

Relaties:

- Reden aanvraag Levensonderhoud generaliseert Vertr → Reden aanvraag Levensonderhoud (*Generalization*,  → , `EAID_0FCBF9AE_E399_53E2_3994_2791C4C114DA`)

## Wachten beslissing instantie

*Wachten beslissing instantie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **moet wachten op een besluit van een externe instantie**, waardoor de startdatum van de dienst afwijkt van de standaardprocedure.

Attributen: Ontvangstdatum beslissing instantie.

GUID: `EAID_008977a4_1342_42b2_be93_bda49931fa51`

Relaties:

- Reden afwijkende startdatum generaliseert Wachten  → Reden afwijkende startdatum (*Generalization*,  → , `EAID_ef35a8cc_43e5_45dc_a5ec_d5f6591ea179`)

## Wachten DigiD

*Wachten DigiD* is een subtype van **Reden afwijkende startdatum** binnen het GBI-Ontologiemodel dat aangeeft dat de ingangsdatum van een inkomensdienst **vertraging oploopt doordat een DigiD nog niet is aangevraagd, geactiveerd of bruikbaar is**.

Attributen: Aanvraagdatum DigiD.

GUID: `EAID_32633236_e5f5_40eb_a083_fc12c3e8a7f8`

Relaties:

- Reden afwijkende startdatum generaliseert Wachten  → Reden afwijkende startdatum (*Generalization*,  → , `EAID_a87f3135_a603_4f22_9811_be04ff4a796d`)
