# Plan: ArchiMate-indeling, lichtere kenmerken, data-object en capability

Goedgekeurd door de redacteur op 2026-10-15. Basis: main op 98ff33f.

## Context

Twee vragen van de redacteur samen:

1. **Todo "ArchiMate-indeling als eerste selectie in de beslistabel".** Het doel heeft twee kanten:
   - beter overzicht en inzicht in de kenmerken en de beslisregels;
   - vooral een lichtere aanpak: minder werk en minder tokens voor het beoordelen en voor alles wat met kenmerken werkt.

   De AI kiest eerst het vak in de ArchiMate-matrix (laag, aspect, intern of extern). De kenmerken worden de controle op die keuze, en waar dat kan, leidt het script ze af.
2. **Twee elementtypen erbij**:
   - **Data-object** wordt een element (nu een annotatie). Eén of meer data-objecten realiseren een bedrijfsobject, met een terugmelding aan het GGM. Registratie is een eis voor een data-object; bij een bedrijfsobject mag registratietaal staan.
   - **Capability** wordt afgeleid, nadat we samen de kenmerken en het verschil met de bedrijfsfunctie hebben bepaald.

Besluiten van de redacteur (2026-10-15):

- één plan;
- *aard* heet voortaan **hoofdkenmerk**, het dominante kenmerk;
- een data-object is een veld bij het bedrijfsobject;
- bij een bedrijfsobject geen registr*-signaal meer, al blijft registratie geen argument voor het type;
- de naam blijft **Capability**;
- de technologielaag is een laag in de matrix: ze zit in GEMMA en komt misschien nog;
- Capability eerst samen bepalen, met het kader van de redacteur (deel 3).

Wat gelijk blijft: de uitkomsten van de bestaande beoordelingen (type, status, pagina's, export), de publicatiegate en de herleidbaarheid.

## Analyse: waar de kenmerken zwaar zijn (gemeten 2026-10-15, 481 beoordelingen)

De kenmerken zijn 137.000 van de 249.000 woorden in de beoordelingen (55%), gemiddeld 23 per begrip. Per groep:

| Groep | Woorden | Aandeel | Wat opvalt |
|---|---|---|---|
| Poort | 52.000 | 38% | bijna altijd hetzelfde antwoord: *herkenbaar* 480 van 481 ja, *gemeentelijk* 475 ja, *buiten dit model* 5 ja, *slechts eigenschap* 27 ja |
| Gedrag | 33.000 | 24% | veel kenmerken herhalen een relatie (*toegewezen partij* = toewijzing, *gebruikt objecten* = toegang, *aanleiding* = triggering, *gerealiseerd door* = realisatie); *afnemer* 93 van 93 ja, *benoembaar resultaat* 189 van 189 ja |
| Passief | 17.000 | 12% | *geautomatiseerd verwerkt* 382 keer gevraagd, 19 keer ja |
| Specialisatie | 12.000 | 9% | *zelfstandige specialisatie* 380 van 432 ja (zonder breder begrip altijd ja); *generiek* 20 van 382 ja |
| Hoofdkenmerk (nu Aard) | 11.000 | 8% | acht vragen, precies één ja |
| Soort gedrag | 8.000 | 6% | zes vragen, precies één ja |
| Partij, Beleidskader | 4.500 | 3% | |

Een kenmerk *ja* steunt op een bron (regel Elke claim een bron). Een relatie in een beoordeling heeft al bronnen en een vindplaats, dus een kenmerk dat uit een relatie wordt afgeleid, blijft herleidbaar.

## Advies: vijf optimalisaties

Samen ongeveer 60–70% minder woorden in de kenmerken. Dat is een derde minder per beoordeling: minder schrijven in fase A en B, kortere precedenten om te lezen, en kortere uitvoer van `vragen` en het werkpakket.

| # | Optimalisatie | Besparing (schatting) | Besluit nodig |
|---|---|---|---|
| O1 | **Keuzevelden** in plaats van ja/nee-lijsten: `vak` (laag, aspect, extern), `hoofdkenmerk` (één waarde, of `ding`) en `soort_gedrag` (één waarde). Het script leidt de nee's af. | ongeveer 17.000 | nee: volgt uit de matrix |
| O2 | **Poort als uitzondering**: alleen een afwijking schrijven, met onderbouwing (niet herkenbaar, niet gemeentelijk, buiten dit model, eigenschap, onderdeel, ander onderwerp). Zonder afwijking geldt de poort als doorlopen; *herkenbaar* en *gemeentelijk* steunen dan op de bronnen bij de definitie. | ongeveer 45.000 | **ja**: raakt regel Elke claim een bron |
| O3 | **Kenmerken uit relaties**: het script leidt het kenmerk af uit de relatie met haar bronnen. Het gaat om *toegewezen partij*, *gebruikt objecten*, *aanleiding*, *gerealiseerd door*, *leidt tot gedrag*, *bedient gedrag*, *levert aanbod*, *leidt tot gebeurtenis*, *bijdrage aan groter proces*, *omvat processen*, *vervult een rol*, *voert gedrag uit*, *ontsluit een dienst*, *wordt bewerkt*, *is grondslag voor* en *in functie-indeling*. Het signaal "kernrelatie zonder relatie" valt weg, want de relatie ís het kenmerk. | ongeveer 18.000 | ja (licht): de vraag wordt "noem de relatie" |
| O4 | **Standaardwaarden**: *zelfstandige specialisatie* is ja tenzij `specialisatie_van` een breder begrip noemt; *generiek* is nee tenzij ja. | ongeveer 10.000 | nee |
| O5 | **Data-objecten in plaats van *geautomatiseerd verwerkt***: de lijst `data_objecten` is het antwoord (deel 2). | ongeveer 4.500 | al besloten |

Verder, minder groot:

- **`beslist` uit de beoordeling halen.** Het script schrijft het blok (23.000 woorden). Agenten lezen het mee als ze een precedent openen. Het kan naar een gegenereerd bestand per onderwerp. Dit is een ander onderwerp: ik zet het alleen in de todo.
- **Een overzicht van de beslisregels per vak.** `kenmerken-en-beslistabel.md` (4.200 woorden) krijgt bovenaan de matrix. Per vak volgt dan alleen wat daar gevraagd wordt; dat geeft overzicht en inzicht. De skill criteria verwijst ernaar in plaats van de vragen te herhalen.

## Uitkomst stap 2: besluiten over O2 en O3 (2026-10-15)

- **O2, poort als uitzondering: ja.** Zonder afwijking geldt de poort als doorlopen; *herkenbaar* en *gemeentelijk* steunen dan op de bronnen van de beoordeling (veld `bronnen`, ook die bij definitie en beschrijving). Een afwijking krijgt een onderbouwing en een bron. Het script controleert dat de beoordeling een bron heeft. Regel Elke claim een bron krijgt deze zin in stap 6, samen met het script.
- **O3, kenmerken uit relaties: ja.** Het script leidt ja en nee af voor de relationele kenmerken uit de relaties, ook die in andere beoordelingen; de bron is die van de relatie. In fase B wordt de vraag "leg de relatie vast". Het signaal "kernrelatie zonder relatie" vervalt. Een verschil tussen kenmerk en relatie bij de omzetting (stap 5) wordt per geval voorgelegd.
- Voorbeeld *Ruimen graf*: de kenmerken gaan van ongeveer 560 naar ongeveer 150 woorden.

## Uitkomst stap 3–7 (2026-10-15)

- **O3 bijgesteld door de redacteur.** Een kenmerk afleiden uit een relatie is fragiel: een relatie bestaat alleen zolang beide elementen bestaan, en een kenmerk kan ja zijn door een relatie met een element dat er nog niet is. Daarom blijft het kenmerk de bewering en noemt het zijn tegenpartij in `naar`: het id van een element, of naam en type van een potentieel element. Bestaat de relatie, dan steunt het kenmerk op haar bron (zonder eigen onderbouwing); anders met eigen onderbouwing en bron. Vervalt de relatie, dan blijft de uitkomst en meldt het script dat de bron ontbreekt. Een relatie bij een kenmerk nee is een signaal.
- **Gemeten vóór de omzetting**: 239 relationele kenmerken ja zonder relatie (bij elementen 104, het meest *aanleiding* 63 en *toegewezen partij* 17). Strikt afleiden had 80 processen tot geen element gemaakt. Ze blijven met hun onderbouwing staan; de tegenpartij met naam en type komt bij de volgende herbeoordeling (todo).
- **Per geval besloten**: vier processen hadden *leidt tot gebeurtenis* nee met een triggering naar een gebeurtenis; het kenmerk is ja. GGD heeft hoofdkenmerk *samenwerkingsverband* (altijd een samenwerkingsverband, als partij via een rol); *los van verantwoordelijkheid* mag daarom ook bij een samenwerkingsverband.
- **Beslistabel**: de regels voor een combinatie van aarden en voor gedrag zonder soort gedrag vervallen (één hoofdkenmerk; de soort gedrag is verplicht). Regel 7 (consistentie) toetst ook het vak. De regelnummers vanaf 8 schuiven op; ze staan niet op de pagina's.
- **Omzetting**: alle 481 beoordelingen met een script. Uitkomst: `beslist` gelijk aan main (op de regelnummers na); alleen de status van de 285 goedgekeurde elementen gaat naar review, omdat het akkoord-hash de kenmerken telt (nieuw AKKOORD, zoals in 13c5312). De sectie Kenmerken op de pagina's toont vak, hoofdkenmerk, soort gedrag, de poort en de kenmerken met ja, met de tegenpartij als link. Bronnen die alleen in geschrapte kenmerken stonden, staan nu in `bronnen` van de beoordeling, zodat de bronnenlijst gelijk blijft.
- **Woorden**: kenmerken van 136.947 naar 51.354, plus 1.210 voor de keuzevelden (−62%); de beoordelingen samen van 249.150 naar 166.584 (−33%).
- **Open punt Extern bij gedrag**: volgt uit het vak (`bedrijf/gedrag-extern` is de dienst).
- **Woordbudget** (besluit van de redacteur): kennismodel 21.100, skill beoordelen 6.700, AGENTS.md 1.720.

## Uitkomst stap 8–11 (2026-10-16)

Besluiten van de redacteur:

- **Naam**: `<naam van het element>-data` (Graf-data).
- **Wie data-objecten heeft**: bedrijfsobject (met de afspraak), rol, actor en gebeurtenis. Een ander type dat uit de GGM-match naar boven komt, wordt voorgelegd. De eenmalige controle: alleen bedrijfsobjecten hadden een GGM-match. Op naam zijn er GGM-entiteiten voor rollen (Belanghebbende, Aangever, Indiener, Rechthebbende), een actor (Gemeente) en gebeurtenissen (RSGBPlus: geboorte, overlijden, huwelijk, ontbinding, migratie); daarom kwam de gebeurtenis erbij.
- **Ontwerp bijgesteld**: de verwerking van de grondslagen blijft in de bedrijfslaag, en het data-object is de schakel naar het informatiemodel. Het veld `vastlegging` vervalt. Het script leidt het data-object af uit `ggm` van het element: een match (exact, sterk of partieel), of sterkte geen met een GGM-terugmelding hiaat. `data_objecten` staat alleen in de beoordeling voor een extra GGM-entiteit (naam en `ggm`, met een match). De GGM-velden erft het data-object van het element. Een `gemma`-veld is er niet: de 14 GEMMA-data-objecten zijn generiek (Zaakgegevens, Bericht …).
- **Relatie**: realisatie naar een bedrijfsobject of afspraak; associatie naar een rol, actor of gebeurtenis, omdat ArchiMate daar geen realisatie kent (een uitbreiding op het GEMMA-kennismodel).
- **Woordbudget**: [modelleerregels.md](../kennismodel/modelleerregels.md) is puntsgewijs herschreven (van 2.759 naar 2.217 woorden), zodat het kennismodel binnen 21.100 blijft (20.874). Het budget van skill beoordelen gaat van 6.700 naar 6.750; de uitleg staat als sectie in `references/ggm-match.md`, niet in een eigen `references/data-object.md`.

Uitvoering:

- Het kenmerk *geautomatiseerd verwerkt* en de annotatie `data_object` vervallen. Het kenmerk is uit 382 beoordelingen geschrapt, met een script. Bij 6 beoordelingen stond een bron alleen in dat kenmerk; die staat nu in `bronnen`.
- Het registr*-signaal geldt niet meer bij een bedrijfsobject of afspraak: van 154 naar 127 signalen. De andere signalen zijn gelijk gebleven.
- De pagina's staan in `elementpaginas/applicatiearchitectuur/data-objecten/`, naar de laag, en niet in `elementpaginas/data-object/`. Het element toont ze onder *Data-objecten*.
- De export zet het data-object in `Application / wiki-gemma-model / Data-objecten`. De concept-export heeft dezelfde 281 elementen en 18 relaties meer.
- Uitkomst: 18 afgeleide data-objecten. Dat zijn de 13 elementen met *geautomatiseerd verwerkt* ja, plus Aanvraag, Beschikking en Besluit (GGM sterk) en Bezwaarschrift en Schriftelijke klacht (hiaat 20 en 21). Bij Ingeschreven persoon komen er 3 extra bij: Gezag-data (Gezagsverhouding, sterk; ook curatele), Nationaliteit-data (exact) en Verblijfstitel-data (sterk). Signalering heeft geen GGM-entiteit; Akte van overlijden valt onder Akte van de burgerlijke stand-data.
- De 285 goedgekeurde elementen staan weer op review, omdat het akkoord-hash de kenmerken telt: een nieuw AKKOORD.

## Voorstel stap 12: Capability (ter bespreking, 2026-10-16)

Een voorstel zonder code, binnen het kader van de redacteur (deel 3). De keuzes K1–K8 worden voorgelegd; de besluiten komen in *Uitkomst stap 12*.

### Wat er nu staat

- **Over GEMMA** (kennismodel, regel 565): Capability is "Een vermogen waarover een organisatie, persoon of systeem beschikt", in de strategielaag. Relaties: Bedrijfsfunctie ─realisatie→ Capability, Resource ─toewijzing→ Capability, Capability ─invloed→ Waarde.
- **GEMMA-model** (2026-10-02): 26 capabilities, alle met bron *Thema-architectuur Common Ground*. Ze hangen alleen aan 8 groeperingen (Kanalen en toegang, Authenticatie en autorisatie, Verantwoording dienstgebruik, Connectiviteit, Datadiensten, Data-integratie, Gemeente en keten- en netwerkpartijen, Processen en bedrijfsregels); geen enkele wordt door een bedrijfsfunctie gerealiseerd. Het zijn vermogens van de informatievoorziening ("Dienstenafnemers moeten …"), geen kaart van wat de gemeente als organisatie moet kunnen.
- **De wiki**: Capability is *buiten dit model* (`tools/kennismodel.py`, poortkenmerk 3 noemt "vermogen", *gegroepeerd gedrag* sluit "wat de gemeente kan" uit). Geen beoordeling heeft Capability als uitkomst. Er zijn 7 bedrijfsfuncties (5 in burgerzaken, 2 in lijkbezorging) en 86 diensten; de 9 diensten van besluitvorming hebben geen functie.
- **Woordbudget** kennismodel: 20.874 van 21.100.

### Het voorstel

- **Definitie**: die van Over GEMMA, letterlijk. Duiding: wat de gemeente moet kunnen, los van hoe, door wie en in welke volgorde; het vermogen waarin zij investeert en waarvan zij de volwassenheid beoordeelt.
- **Vak** `strategie/gedrag`: in ArchiMate is Capability gedrag in de strategielaag. Hoofdkenmerk *vermogen* (volgt uit het vak), geen soort gedrag. Resource, Waardestroom (Value Stream) en Handelwijze (Course of Action) staan als weggefilterd in de laag strategie.
- **Fase A maakt het onderscheid met de functie**: het vak volgt uit de vraag die het begrip beantwoordt (kader: "Wat moet de gemeente kunnen?" tegenover "Welke activiteiten horen inhoudelijk bij elkaar?"). Een begrip met *gegroepeerd gedrag* dat die eerste vraag beantwoordt, is een conflict (regel 7) en wordt voorgelegd.
- **Kenmerken (fase B)**, de criteria uit het kader; *ontleedbaar* is de relatie naar een deelcapability, *niet uitvoeringsgericht* zit in het hoofdkenmerk:

| Kenmerk | Vraag | Ja | Nee | Bij nee |
|---|---|---|---|---|
| *vermogen* (hoofdkenmerk) | Beschrijft het wat de gemeente moet kunnen, los van hoe, door wie, in welke volgorde en met welk kanaal of systeem? | Identiteit vaststellen | Aanvraag controleren op volledigheid | te concreet: een functie, proces of processtap |
| *beoordeelbaar* (nieuw) | Kun je er volwassenheid of ontwikkelbehoefte van bepalen en er apart in investeren? Noem de investeringsvraag. | Identiteit vaststellen (fraudebestrijding, biometrie) | Dienstverlening | te breed: geen element |
| *onderscheidend* (nieuw) | Is het af te grenzen van de andere capabilities, zonder dat een functie er voor een deel in valt? Noem de naaste capability. | Personen registreren tegenover Identiteit vaststellen | Burgers helpen tegenover Dienstverlening | samenvoegen of splitsen: voorleggen |
| *stabiel over tijd* (bestaand, aangescherpt) | Blijft het bestaan als de organisatie, de werkwijze of de systemen veranderen, en is het geen opgave met een einde? | belastingheffing; Identiteit vaststellen | projectteam Omgevingswet; invoering van de Omgevingswet | een opgave: buiten dit model (doel of handelwijze) |
| *gerealiseerd door* † (bestaand, kernrelatie) | Realiseert een aanwijsbare bedrijfsfunctie het vermogen (en bij een dienst: een proces of functie)? Noem ze. | Personen registreren ← Bevolkingsadministratie bijhouding, Burgerlijke stand diensten | vermogen zonder functie | kernrelatie ontbreekt: signaal |

- **Splitsregel** (kader): splits een capability als de delen apart ontwikkeld, beoordeeld of bestuurd worden; het deel wordt een deelcapability (aggregatie). **Beslisregel** (kader): het grofste niveau dat genoeg onderscheid geeft.
- **Aanscherping van *gegroepeerd gedrag*** (kenmerk 23): "… op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd. Wat de gemeente moet kunnen, is een capability (vak strategie)." Het voorbeeld nee wordt "aanslag opleggen (proces)".
- **Kernrelatie** Bedrijfsfunctie ─realisatie→ Capability (K2); Capability ─aggregatie→ Capability voor de deelcapability (uitbreiding op het GEMMA-kennismodel). Welke diensten van hetzelfde vermogen afhangen, volgt uit dienst ← functie → capability; de render toont het op de pagina.
- **Gevolgen in het kennismodel**: Capability gaat van `motivatie/weggefilterd` naar een elementtype in de laag strategie, met een pagina `kennismodel/strategie/capability-modelleerafspraken.md` en `strategie/weggefilterd.md`; poortkenmerk 3 noemt "vermogen" niet meer; de duiding van de bedrijfsfunctie verwijst naar de capability. De elementpagina's komen in `elementpaginas/strategie/capabilities/`, de export zet ze in `Strategy / wiki-gemma-model`.

### Kalibratie op de 26 GEMMA-capabilities

| Groepering (aantal) | Voorbeelden | Oordeel |
|---|---|---|
| Kanalen en toegang (5) | Melden en doen van aanvragen door burgers en bedrijven; Bieden van 'regie op gegevens' aan burgers en bedrijven; Authenticeren en Autoriseren van eindgebruikers; Bieden van gebruikersinterfaces | de eerste twee zijn bedrijfsvermogens richting inwoner en ondernemer: kandidaat voor een match; de andere drie zijn systeemvermogens |
| Datadiensten (4, één ook in Verantwoording) | Vastleggen en verstrekken van data; Terugmelden van mogelijke datafouten; Abonneren en notificeren | informatievoorziening; Terugmelden raakt de terugmeldplicht van de gemeente als afnemer: hoogstens partieel |
| Gemeente en keten- en netwerkpartijen (4), Data-integratie (3) | Gestandaardiseerd vastleggen; Historie; Metadata; Protocolleren; Integreren; Transformeren; Pseudonimiseren | informatievoorziening |
| Authenticatie en autorisatie (2), Verantwoording dienstgebruik (3), Connectiviteit (4) | Autoriseren van dienstenafnemers; Controleren van doel en grondslag; Verbinden van afnemers en aanbieders | informatievoorziening en techniek |
| Processen en bedrijfsregels (2) | Bijhouden en toepassen van bedrijfsregels; Inrichten en uitvoeren van processen | vermogen om bedrijfsregels en workflow te ondersteunen: applicatie |

Toetsvragen: *waar investeren* en *welke competenties hergebruiken* zijn voor alle 26 ja, maar in de informatievoorziening; *welke diensten afhangen van hetzelfde vermogen* geeft bij allemaal "alle diensten": ze zijn horizontaal. Uitkomst: GEMMA heeft geen capabilitykaart van de bedrijfslaag. De wiki maakt bedrijfsvermogens; van de 26 komen er hoogstens 2 à 3 in aanmerking voor een match (K7).

### Kalibratie op diensten (22 diensten uit burgerzaken, lijkbezorging en besluitvorming)

| Kandidaat-capability | Gerealiseerd door (functie in de wiki) | Diensten | Waar investeren? | Competenties hergebruiken | Oordeel |
|---|---|---|---|---|---|
| Personen registreren | Bevolkingsadministratie bijhouding; Burgerlijke stand diensten | Verhuismelding, BRP-inschrijving, Geboorteaangifte, Overlijdensaangifte, Erkenning kind | kwaliteit van BRP en akten, adresonderzoek | registers bijhouden, brondocumenten beoordelen, personen- en familierecht | capability: bundelt twee functies onder één investeringsvraag |
| Identiteit vaststellen | Officiële documenten verstrekking; Bevolkingsadministratie bijhouding; Nederlanderschap diensten | Paspoort, Identiteitskaart, Rijbewijs aanvragen, BRP-inschrijving, Naturalisatieverzoek | identiteitsfraude, biometrie | documentcontrole, gezichtsvergelijking | capability, over functies heen: het inzicht dat de functie-indeling niet geeft; GEMMA-functie Identiteitvaststelling (Ontvangst) realiseert haar ook; Authenticeren van eindgebruikers is de digitale kant (partieel) |
| Lijkbezorging waarborgen | Exploiteren van begraafplaatsen; Vergunningenbeheer Publieksdiensten; Burgerlijke stand diensten | Grafuitgifte, Verlof tot begraven, Uitvaart vervroegen of uitstellen, Overlijdensakte | capaciteit van begraafplaatsen, termijnen | Wet op de lijkbezorging | capability over twee domeinen; tegenover "Lijkbezorging als functie" (niet) |
| Verkiezingen organiseren | Verkiezingen gerelateerde diensten | Kiezerspas, Stempas ontvangen, Volmachtbewijs verkiezingen | ja, apart (verkiezingsorganisatie) | weinig | één op één met een functie: K3 |
| Nationaliteit verlenen | Nederlanderschap diensten | Naturalisatieverzoek, Naturalisatieoptie | nauwelijks apart: de IND beslist | — | geen capability: niet apart ontwikkeld; valt onder Personen registreren en Identiteit vaststellen |
| Rechtsbescherming bieden | geen functie in de wiki (GEMMA: Klachten afhandeling) | Bezwaar, Beroep, Klacht, Dwangsom bij niet tijdig beslissen, Nadeelcompensatie | juridische kwaliteit | over alle domeinen | capability, maar zonder realiserende functie: eerst een functie (K2) |

Bevindingen:

- Een capability voegt het meest toe waar zij functies en domeinen overspant (Identiteit vaststellen, Lijkbezorging waarborgen, Personen registreren). Daar beantwoordt zij de drie toetsvragen anders dan de functie-indeling.
- Bij één op één met een functie (Verkiezingen, Nederlanderschap, Officiële documenten) is de capability bijna een kopie van de functie: K3.
- Een dienst hangt vaak van meer vermogens af (Paspoort: Identiteit vaststellen en het verstrekken van documenten); via de functies is dat zichtbaar.
- De diensten van besluitvorming hebben geen functie; een capability daar vraagt eerst een functie (GEMMA: Klachten afhandeling, Besluitvormings verantwoording).
- Bijvangst voor een terugmelding later: de GEMMA-functies onder *Ontvangst* (Identiteitvaststelling, Autorisatievaststelling, Voorwaardentoetsing, Vormacceptatie, Zelfredzaamheidbepaling) staan alleen in het domein Fysieke leefomgeving, maar zijn domeinoverstijgend en lijken op vermogens.

### Keuzes

| # | Keuze | Advies |
|---|---|---|
| K1 | Hoe een capability ontstaat | een beoordeling van de AI, afgeleid uit de functies en diensten van een onderwerp, met fase A en B, voorleggen en AKKOORD |
| K2 | Welk gedrag een capability realiseert | alleen de bedrijfsfunctie, zoals Over GEMMA |
| K3 | Wanneer een capability een element is | de criteria beslissen; één op één met een functie alleen als de toetsvragen een ander antwoord geven dan de functie |
| K4 | Naamvorm | object en werkwoord in de onbepaalde wijs (Identiteit vaststellen) |
| K5 | Indeling | een eigen capabilitykaart naar het GEMMA-domein: domein › capability › deelcapability |
| K6 | Bron | de bronnen van de realiserende functies (relationeel, `naar`); *beoordeelbaar* en *onderscheidend* zijn een oordeel met onderbouwing |
| K7 | GEMMA-match | optioneel, op betekenis; de 26 blijven matchdoel; één terugmelding aan het GEMMA-team over de ontbrekende capabilitykaart van de bedrijfslaag |
| K8 | Woordbudget kennismodel | ongeveer 700 woorden erbij (een pagina capability, weggefilterd in strategie, twee kenmerken): het budget naar 21.800 |

## Uitkomst stap 12 (2026-10-17)

Besluiten van de redacteur over het voorstel; de rest van het voorstel (definitie, vak `strategie/gedrag`, hoofdkenmerk *vermogen*, de kenmerken, de aanscherpingen en de gevolgen in het kennismodel) geldt zoals voorgesteld.

- **K1, ontstaan**: een beoordeling van de AI, afgeleid uit de functies en diensten van een onderwerp, met fase A en B, voorleggen en AKKOORD.
- **K2, relatie**: alleen de bedrijfsfunctie realiseert een capability (Bedrijfsfunctie ─realisatie→ Capability), plus Capability ─aggregatie→ Capability voor een deelcapability. De houder is altijd de gemeente: "uiteindelijk is alles gerelateerd aan de gemeente". Er komt dus geen relatie naar een actor of resource; Resource blijft weggefilterd.
- **K3, drempel: alleen bij bundeling.** Een capability is een element als ten minste twee bedrijfsfuncties haar realiseren. Valt zij één op één samen met een functie, dan is het geen element: de functie volstaat. De regel is toetsbaar *(script)*. In de kalibratie worden Personen registreren, Identiteit vaststellen en Lijkbezorging waarborgen een element. Verkiezingen organiseren en Nationaliteit verlenen worden het niet. Rechtsbescherming bieden wacht op realiserende functies.
- **K4, naamvorm**: object en werkwoord in de onbepaalde wijs (Identiteit vaststellen). Een capability heeft nooit dezelfde naam als een functie of proces.
- **K5, indeling**: een eigen *Capabilitykaart* naar het GEMMA-domein: domein › capability › deelcapability, met de bestaande domeingroeperingen van GEMMA en `domein` als verplicht veld. Een capability over meer domeinen komt onder Niet domeingebonden.
- **K6, bron: beide.** De realisatie steunt op de bronnen van de realiserende functies (relationeel, `naar`). Daarnaast zijn strategische bronnen die voor alle gemeenten gelden de bron van het vermogen zelf (*beoordeelbaar*, *onderscheidend*): VNG-impactanalyses, implementatieplannen en beleidsadviezen. Zonder zo'n bron zijn die kenmerken een oordeel met onderbouwing. Regel Elke claim een bron krijgt deze uitzondering in stap 13.
- **K7, GEMMA-match**: `gemma` is optioneel en matcht op betekenis; de 26 GEMMA-capabilities blijven matchdoel. Een zwakke match wordt voorgelegd. Er komt één terugmelding aan het GEMMA-team: GEMMA heeft geen capabilitykaart van de bedrijfslaag, en de import voegt die toe naast de 26.
- **K8, woordbudget**: kennismodel van 21.100 naar 21.800.

Open voor stap 13:

- **Brontype van een VNG-impactanalyse, een implementatieplan of een beleidsadvies**: in sources/index is dat nu `overig` (bijvoorbeeld de GEMMA-impactanalyse ketensamenwerking), niet `beleid`. Het brontype bepaalt de plaats in de regel Bronvoorrang. Dit wordt voorgelegd vóór de wijziging van de regel.
- **De GEMMA-functies onder *Ontvangst***: een kandidaat voor een terugmelding (zie de bevindingen van de kalibratie). Dit punt staat los van het bouwen.

## Uitkomst stap 13 (2026-10-17)

Vastgelegd in ARCHITECTURE.md (§3.4, §4.1 met het kader als tabel, §4.4, §7), AGENTS.md (regel Elke claim een bron), [modelleerregels](../kennismodel/modelleerregels.md) en het kennismodel (`tools/kennismodel.py`, `tools/bepaal_type.py`), na akkoord van de redacteur:

- **Brontype**: landelijke impactanalyses, implementatieplannen en beleidsadviezen zijn `richtlijn` (regel Bronvoorrang); geen nieuw brontype.
- **Strategisch tegenover uitvoerend**: een capability is strategisch en verandert met de opgaven van de gemeente; een functie is uitvoerend en verandert met de clustering van het werk. Het staat in de vragen bij *vermogen* en *gegroepeerd gedrag* en in de duiding van beide typen. Een vermogen met een uitvoerder (*toegewezen partij*) of objecten (*gebruikt objecten*) geeft een conflict (stap 3), omdat die kenmerken alleen bij gedrag passen.
- **Type**: kernrelatie *gerealiseerd door* (één kenmerk voor dienst en capability); *beoordeelbaar*, *onderscheidend* en *stabiel over tijd* zijn een eis. Laag Strategie: Resource, Waardestroom en Handelwijze zijn elementtypen zonder element; realisatie vanuit ander gedrag dan een functie valt buiten het kennismodel.
- **Woordbudget**: kennismodel 17.100 (het kennismodel was eerst ingekort, commit 487489b; K8 vervalt), AGENTS.md 1.740.
- **Nog niet**: de toets op ten minste twee realiserende functies (K3), de render, de export en de beoordelingen van capabilities: stap 14.

## Uitkomst stap 14 (2026-10-18)

- **Gebouwd** (commit d3bcbd6): de toets op ten minste twee realiserende functies (`tools/bepaal_type.py`: minder is *geen element*, voorgelegd), de grondslag via de realiserende functies (`tools/signalen.py`), geen registr*-signaal bij een capability, geen bron nodig voor *beoordeelbaar* en *onderscheidend* (K6, `tools/beslissen.py`), de render (Capabilitykaart, Gerealiseerd door, Diensten die van dit vermogen afhangen; bij de functie Realiseert capability), de indelingspagina `capabilities.md`, de export naar `Strategy / wiki-gemma-model / Capabilitykaart` met de aggregatie vanuit de domeingroepering, tests, en `references/capability.md` in skill beoordelen. Woordbudget skill beoordelen 7.050, criteria 981.
- **Afgeleid en goedgekeurd** (AKKOORD 2026-10-18): Personen registreren (Bevolkingsadministratie bijhouding, Burgerlijke stand diensten), Identiteit vaststellen (Officiële documenten verstrekking, Bevolkingsadministratie bijhouding, Nederlanderschap diensten) en Lijkbezorging waarborgen (Exploiteren van begraafplaatsen, Burgerlijke stand diensten, Vergunningenbeheer Publieksdiensten; Niet domeingebonden). Geen GEMMA-match: Authenticeren van eindgebruikers is de digitale kant, een koppeling zou haar overschrijven. Niet: Verkiezingen organiseren en Nationaliteit verlenen (K3). De zes functies kregen een realisatie en een nieuw akkoord.
- **Terugmelding** aan het GEMMA-team nummer 9: geen capabilitykaart van de bedrijfslaag (K7).
- **Bekend**: de diensten die van een capability afhangen, volgen uit de hele functie en zijn daardoor ruim (Lijkbezorging waarborgen telt via Burgerlijke stand diensten ook geboorte en huwelijk).

## Deel 1 — Matrix en lichtere kenmerken (denkniveau hoog)

### De matrix

| Laag | Actief intern | Actief extern | Gedrag intern | Gedrag extern | Passief | Samengesteld |
|---|---|---|---|---|---|---|
| bedrijf | Actor, Rol, Bedrijfssamenwerking | Kanaal | Bedrijfsproces, Bedrijfsfunctie, Bedrijfsinteractie, Gebeurtenis | Dienst | Bedrijfsobject, Afspraak, Representatie | Product |
| applicatie | weggefilterd | weggefilterd | weggefilterd | weggefilterd | Data-object (deel 2) | — |
| technologie | weggefilterd: komt misschien nog | | | | | |
| strategie | Capability (deel 3: het vak dan bevestigen) | | | | | |
| overig | | | | | | Locatie (geen pagina), Groepering |

**Motivatie** valt buiten de aspecten, zoals in ArchiMate: daar zijn geen aspecten. In die laag zijn twee typen onderdeel van het model:

- **Beleidskader** (Driver): een element met pagina, uit externe bronnen (Europese regelgeving, Rijksregelgeving, VNG-modelverordeningen);
- **Kwaliteitsdoel**: een matchdoel uit GEMMA.

De overige motivatietypen (doel, principe, eis, waarde, kernwaarde) blijven *buiten dit model*.

- **Product** krijgt `samengesteld`: ArchiMate noemt het een samengesteld element van de bedrijfslaag.
- **Locatie** krijgt laag `overig` en aspect `samengesteld`, en blijft zonder pagina.

Fase A wordt drie keuzes:

1. het vak;
2. het hoofdkenmerk binnen het vak; dat valt weg als het vak maar één hoofdkenmerk heeft;
3. bij gedrag de soort gedrag.

Een poortafwijking komt er alleen bij als die er is. Stap 3 (Consistentie) krijgt een regel: past het hoofdkenmerk niet bij het vak, dan is er een conflict en wordt het voorgelegd. Regels 8–21 van de stappentabel blijven, met het vak als voorwaarde.

### Stappen

1. Plan in `plannen/`; todo bijwerken (laag).
2. **Besluiten over O2 en O3** voorleggen, met regel Elke claim een bron en een voorbeeld vóór en na van één beoordeling (hoog).
3. **Schema en `tools/bepaal_type.py`** (hoog):
   - de keuzevelden `vak`, `hoofdkenmerk` en `soort_gedrag`;
   - `VAKKEN`, en `AARD` wordt `HOOFDKENMERK`;
   - poort met uitzonderingen;
   - kenmerken afleiden uit relaties (het script kijkt ook naar de relaties in andere beoordelingen, zoals de toewijzing van een rol aan een proces);
   - standaardwaarden;
   - de consistentieregel;
   - `vragen` en `fase_a` vragen alleen wat per vak nodig is;
   - `CRITERIA_VERSIE` omhoog.
4. **Kennismodel** (middel):
   - `tools/kennismodel.py` geeft elk `Elementtype` zijn vak;
   - de matrix komt in `kennismodel/README.md` en in `kenmerken-en-beslistabel.md`, met de vragen per vak;
   - "aard" wordt "hoofdkenmerk" in *Herken je aan*;
   - een weggefilterd-pagina voor de technologielaag.
5. **Omzetting met een script** (middel). Een eenmalig script in de scratchpad zet alle 481 beoordelingen om. Het vult de keuzevelden in uit de huidige ja's. Het schrapt wat nu wordt afgeleid of standaard is, maar alleen als de afleiding hetzelfde antwoord geeft. Een verschil (een kenmerk ja zonder relatie, of andersom) komt op een lijst om voor te leggen, per geval.
   - `tools/beslissen.py` draait vóór en na. De `beslist`-blokken, `elementpaginas/` en `archimate_export.py --check` blijven gelijk.
   - Telt een veld mee in de hash van het akkoord, dan wordt het uitgezonderd of de hash omgezet, zodat er geen nieuw AKKOORD nodig is voor een vormwijziging.
6. **Skills en uitleg** (middel):
   - skill `gemma-archimate-model-criteria` (fase A: vak, hoofdkenmerk, soort gedrag, poortafwijking);
   - skill `gemma-archimate-model-beoordelen` (fase B zonder afgeleide kenmerken);
   - `tools/sjablonen.py` (`STANDAARD_NEE` vervalt grotendeels), `tools/werkpakket.py`;
   - AGENTS.md van de wiki, en ARCHITECTURE.md §4.1 met de reden.
7. Commit `rules: …`, en de woordentelling vóór en na in de uitkomst van het plan.

## Deel 2 — Data-object als element (hoog voor het ontwerp, middel voor de uitvoering)

**Ontwerp:**

- **Veld `data_objecten`** bij een bedrijfsobject. Per item:
  - `naam` en `definitie`;
  - `vastlegging`: de eis, met citaat en bron van de registratie (register, basisregistratie, zaaksysteem). Zonder bron is het geen data-object (*script*);
  - `ggm` (entiteit, sterkte, onderbouwing);
  - `gemma`: optioneel, een match met een van de 14 GEMMA-data-objecten.
- **Het script maakt het element**: een element `data-object` (`<bedrijfsobject>-<slug>`), een pagina in `elementpaginas/data-object/` en *realisatie* Data-object → Bedrijfsobject. Het data-object volgt de status van zijn bedrijfsobject; de hash telt `data_objecten` mee. De annotatie `data_object` vervalt.
- **GGM-terugmelding**: een match zwakker dan `sterk` wordt voorgelegd (`REDEN_GEEN_GGM` bestaat al). Bij `geen` hoort een melding `hiaat` in `modellen/ggm/terugmeldingen.yaml` (*script*).
- **Registr*-signaal**: `tools/signalen.py` slaat `REGISTR_RE` over bij een bedrijfsobject en in `data_objecten`.
  - Regel Beslistabel beslist wordt: registratie is geen argument voor het type; bij een bedrijfsobject mag de tekst haar noemen; bij een data-object is ze de eis.
  - De afspraken in `tools/kennismodel.py` volgen.
- **Kennismodel en export**: Data-object krijgt paginatype `data-object` (geen annotatie meer), met *realisatie* naar Bedrijfsobject. `archimate_export.py` zet het in de applicatielaag.

**Stappen:**

8. Schema, `bepaal_type.py`, `kennismodel.py`, `signalen.py`, `modelleerregels.md` (hoog).
9. `beslissen.py`, `render.py`, `archimate_export.py`, tests; een nieuwe `references/data-object.md` in skill `gemma-archimate-model-beoordelen` (middel).
10. De 19 bedrijfsobjecten met *geautomatiseerd verwerkt: ja*, per geval (hoog): de data-objecten, de bron van de vastlegging, de GGM-match en de terugmeldingen. Eén tabel voorleggen; AKKOORD.
11. Commits `rules:` en `add:`.

## Deel 3 — Capability (eerst samen bepalen, denkniveau hoog)

**Kader van de redacteur.** Het abstractieniveau volgt uit de vraag die het model beantwoordt, niet uit omvang of detail.

| | Capability | Bedrijfsfunctie | Bedrijfsproces |
|---|---|---|---|
| Vraag | Wat moet de gemeente kunnen? | Welke activiteiten horen inhoudelijk bij elkaar? | Hoe wordt een dienst gerealiseerd? |
| Afbakening | vermogen of opgave | gedeelde aard van activiteiten, kennis of middelen | dienst, resultaat en kernobject |
| Verandert bij | andere strategische opgaven | andere clustering van activiteiten | andere uitvoering van de dienst |
| Niveau | strategisch/tactisch | tactisch | tactisch/operationeel |

**Criteria:**

- **Capability**: onderscheidend, beoordeelbaar (volwassenheid, ontwikkelbehoefte), ontleedbaar, duurzaam, niet uitvoeringsgericht. Splits een capability als de delen apart ontwikkeld, beoordeeld of bestuurd kunnen worden.
- **Bedrijfsfunctie**: inhoudelijke samenhang (aard, deskundigheid, middelen), procesoverstijgend, stabiel, geen processtap. Splits bij wezenlijk andere deskundigheid; voeg samen als het onderscheid geen inzicht geeft.
- **Bedrijfsproces**: dienstgericht, een eigen kernobject, een herkenbaar resultaat, afgrensbaar. Vergelijk met de bestaande kenmerken.

Eén toets per type, maar geen gelijke omvang afdwingen. Voorbeelden:

| Voorbeeld | Type | Oordeel |
|---|---|---|
| Dienstverlening | Capability | te breed |
| Aanvraag controleren op volledigheid | Capability | te concreet |
| Aanvragen beoordelen | Bedrijfsfunctie | passend als het over meer diensten terugkomt |
| Omgevingsvergunning verlenen | Bedrijfsfunctie | te dicht bij één proces |

**Beslisregel**: kies het grofste niveau dat genoeg onderscheid geeft; meer detail alleen als het een aantoonbare vraag beantwoordt.

**Stappen:**

12. **Voorstel ter bespreking** (geen code):
    - de definitie (Over GEMMA: "Een vermogen waarover een organisatie, persoon of systeem beschikt") en het vak;
    - de criteria als kenmerken in de vorm van de beslistabel, en daartegen aangescherpt *gegroepeerd gedrag* en *stabiel over tijd*;
    - de kernrelatie Bedrijfsfunctie ─realisatie→ Capability;
    - naamvorm, indeling, bron en GEMMA-match;
    - een kalibratie op de 26 GEMMA-capabilities en op 10 à 20 diensten uit de bestaande onderwerpen, met de toetsvragen: waar investeren, welke competenties hergebruiken, welke diensten afhangen van hetzelfde vermogen.
13. Besluiten vastleggen in ARCHITECTURE.md en het kennismodel. Capability gaat van `motivatie/weggefilterd` naar laag `strategie`.
14. Bouwen zoals in deel 2; capabilities afleiden; voorleggen; AKKOORD.

## Volgorde en Sessies

- **Sessie 1**: stap 1–2 (plan en besluiten O2/O3).
- **Sessie 2**: stap 3–7 (de omzetting).
- **Sessie 3**: deel 2.
- **Sessie 4**: deel 3, eerst als bespreking.
- Na elk deel: handoff.md en todo.md bijwerken.

## Open punten (regel Navragen, tijdens de uitvoering)

- **Naam van een data-object**: als het bedrijfsobject, of een gegevensnaam ("Zaakgegevens")?
- **Wie nog meer data-objecten heeft**: kan ook een afspraak, of een rol of actor met tegenhanger, data-objecten hebben?
- **Extern bij gedrag**: volgt uit het vak (opgelost in stap 3).

## Verificatie

- `uv run pytest wikis/gemma-archimate-model/tools/tests` is groen, met nieuwe tests:
  - vak en hoofdkenmerk in conflict;
  - een poortafwijking;
  - een kenmerk afgeleid uit een relatie in een andere beoordeling;
  - een data-object zonder vastlegging geeft een fout;
  - een bedrijfsobject geeft geen registr*-signaal, een proces wel;
  - de realisatie staat in de export.
- **Deel 1**: `tools/beslissen.py` vóór en na de omzetting. Het verschil in `beslist` en `elementpaginas/` is leeg, en `archimate_export.py --check` is gelijk. Er is een woordentelling van de kenmerken vóór en na.
- **Deel 2**: de 19 objecten hebben data-objectpagina's met realisatie; het GGM-register is bijgewerkt; de export heeft de applicatielaag.
- **Steeds**: `uv run python -m llmwiki lint` en `uv run python -m llmwiki commit-check`.
