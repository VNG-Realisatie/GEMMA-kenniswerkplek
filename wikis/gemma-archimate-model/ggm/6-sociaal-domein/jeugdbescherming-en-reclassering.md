<!-- gegenereerd door tools/ggm.py; hash: a58fcc61bb23e3d0a91ca078b09fa82df195e4f05258b72f2cc8976843614e9b -->
# Jeugdbescherming en reclassering

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Informering | `EAID_ACC7A392_9A16_42a8_A58E_1E8E6826B2D0` |  | indicatieGeinformeerd, redenNietGeinformeerd, datum, reactie |
| Leefgebied | `EAID_B061E420_187A_49dd_B8DA_2AF3FC5D860F` | Een Leefgebied in het kader van jeugdbescherming verwijst naar een specifiek domein binnen het leven van een kind of jongere waarin factoren van invloed zijn op diens veiligheid, welzijn en ontwikkeling. Voorbeelden van leefgebieden zijn gezinssituatie, onderwijs, sociale relaties, gezondheid, vrije tijd en financiën. Bij jeugdbescherming wordt elk leefgebied onderzocht om risico’s en beschermende factoren te identificeren, zodat er een integraal plan kan worden opgesteld om de veiligheid en het welzijn van het kind of de jongere te waarborgen. Leefgebieden vormen daarmee een leidraad voor een holistische benadering in de ondersteuning en interventies. | toelichting, leefgebiedOmschrijving |
| Zorgelijke Situatie | `EAID_AEF1825F_C554_4490_975D_93AEA24991A9` | Een zorgelijke situatie in de context van jeugdbescherming is een omstandigheid waarin de veiligheid, gezondheid, of ontwikkeling van een kind of jongere in het geding is door bijvoorbeeld verwaarlozing, mishandeling, huiselijk geweld, of andere risicofactoren. Deze situaties worden gekenmerkt door signalen van fysieke, emotionele of sociale schade of het ontbreken van een veilige en stabiele omgeving. Een zorgelijke situatie kan leiden tot interventie door jeugdbeschermingsorganisaties om de risico’s te verminderen en het kind of de jongere te beschermen en ondersteunen bij een gezonde en veilige ontwikkeling. | sitiuatieschets, nadereOmschrijving |
| Zorgmelding | `EAID_B852AF03_A5E0_4148_AFC1_108509FF8BBD` | Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere. Deze melding kan worden gedaan door professionals, zoals leraren, huisartsen of politie, maar ook door burgers of familieleden. Een zorgmelding bevat signalen of concrete aanwijzingen van mogelijke risico’s, zoals mishandeling, verwaarlozing, huiselijk geweld, of een onveilige thuissituatie. Het doel van een zorgmelding is om de situatie te laten beoordelen en, indien nodig, passende hulp of bescherming te organiseren om het welzijn van het kind of de jongere te waarborgen. | zorgmeldingsoort, terugkoppelingGewenst, verzoek, omschrijving, nadereOmschrijving |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Informering | Association | informering | NatuurlijkPersoon | 0..* → 1 | `EAID_E23DE89E_E65E_449a_AF92_470FAA5C1FD9` |  |
| Zorgelijke Situatie | Association | berust op | Incident | 1 → 0..* | `EAID_73D8FF62_985C_497f_8196_D8FE3DACCB78` |  |
| Zorgelijke Situatie | Association | toelichting | Leefgebied | 1 → 0..* | `EAID_79624287_3216_40f0_895D_D5856745C0A6` |  |
| Zorgmelding | Association | betrokkenen | NatuurlijkPersoon | 0..* → 0..* | `EAID_097BCCA2_749E_4c0f_A72D_FC3F278C5EB8` |  |
| Zorgmelding | Association | betreft | NatuurlijkPersoon | 0..* → 1 | `EAID_228972BF_A0CA_4e2f_832D_954A15769C1B` |  |
| Zorgmelding | Association | naar aanleiding van | Zorgelijke Situatie | 1 → 1..* | `EAID_6D6EF335_FEA2_4da1_BE3A_40BB6E1B104C` |  |
| Zorgmelding | Association | betrokken professional | Medewerker | 0..* → 0..* | `EAID_F662BA2D_DE58_491d_8D8B_60659E99278C` |  |
| Zorgmelding | Generalization |  | AanvraagOfMelding |  →  | `EAID_E172FA03_7A24_4ee6_A477_56CC1175477B` |  |
