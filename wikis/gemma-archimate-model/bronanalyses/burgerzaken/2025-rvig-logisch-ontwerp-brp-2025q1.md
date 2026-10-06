---
id: 2025-rvig-logisch-ontwerp-brp-2025q1
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2025-rvig-logisch-ontwerp-brp-2025q1
relevant: ja
korte_titel: Logisch Ontwerp BRP 2025.Q1
bijgewerkt: 2026-10-06
---

# Logisch Ontwerp BRP versie 2025.Q1

Bron: [tekst](../../../../sources/raw/2025-rvig-logisch-ontwerp-brp-2025q1.md) · [online](https://www.rvig.nl/sites/default/files/2024-12/Logisch%20Ontwerp%20BRP%202025.Q1.pdf)

## Samenvatting

Het Logisch Ontwerp BRP (LO BRP) van RvIG is de functionele en technische systeembeschrijving waar de Wet BRP, het Besluit BRP en de Regeling BRP naar verwijzen. Voor dit onderwerp is het gegevensbeschrijving (applicatielaag): alleen de objecten en groepen van gegevens zijn gelezen (hoofdstuk 1.5 stelselarchitectuur, 1.6 statuswijzigingen, 4.2 BRP-gegevens, 4.4 categorieën); de rubrieken, landelijke tabellen, het berichtenboek, de conversies en de dienstverleningsafspraken zijn buiten beschouwing gelaten.

De BRP is een landelijke registratie van personen die gedecentraliseerd bij de gemeenten (ingezetenen) en centraal in de RNI (niet-ingezetenen) wordt gevoerd. Het object dat alles draagt is de persoonslijst: "het geheel van persoonsgegevens dat over een persoon in de BRP is opgenomen". De persoonslijst is verdeeld in categorieën met bij elkaar horende gegevens: Persoon, Ouder1, Ouder2, Nationaliteit, Huwelijk/geregistreerd partnerschap, Overlijden, Inschrijving, Verblijfplaats, Kind, Verblijfstitel, Gezagsverhouding, Reisdocument, Kiesrecht, Tijdelijk verblijfsadres en Contactgegevens. Een persoonslijst van een voormalig ingezetene of nooit-ingezetene heeft er minder. Naast de persoonslijst kent het LO de verwijzing (afgeleid, wijst naar de volgende gemeente van inschrijving), de afnemersindicatie (hoort bij de persoonslijst in BRP-V, maakt er geen deel van uit) en de landelijke tabellen (coderingslijsten, geen onderdeel van de persoonslijst).

Het LO legt ook de rollen van partijen in het stelsel vast: gemeenten houden de persoonslijsten van ingezetenen bij, de minister van BZK is verantwoordelijk voor de RNI, aangewezen bestuursorganen (ABO) dienen verzoeken in voor niet-ingezetenen, de IND levert verblijfstitelgegevens, RvIG verstuurt berichten over landelijke tabellen en paspoortsignaleringen, en BRP-V verstrekt namens de minister gegevens aan afnemers. Paragraaf 1.6 beschrijft de statuswijzigingen van een persoonslijst als gebeurtenissen: eerste inschrijving als ingezetene (aangifte verblijf en adres, geboorte), inschrijving in de RNI, vervolginschrijving (intergemeentelijke adreswijziging, hervestiging), opschorting wegens emigratie, ministerieel besluit, overlijden of fout. De registratiestappen (hoofdstuk 2), verstrekkingen (hoofdstuk 3) en berichten (hoofdstuk 5) vallen buiten de afbakening.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| persoonslijst | het geheel van persoonsgegevens dat over een persoon in de BRP is opgenomen | PL | 4.2.1 (regel 4901) |
| categorie Persoon | gegevens over de ingeschrevene; komt 1 keer actueel voor | ingeschrevene | 4.4 (regel 5227) |
| categorie Ouder1 / Ouder2 | gegevens over de ouder1 resp. ouder2 van de ingeschrevene | ouder | 4.4 (regel 5231, 5239) |
| categorie Nationaliteit | gegevens over een nationaliteit van de ingeschrevene; 0, n keer | — | 4.4 (regel 5245) |
| categorie Huwelijk/geregistreerd partnerschap | gegevens over een gesloten of ontbonden huwelijk/geregistreerd partnerschap van de ingeschrevene; 0, n keer | — | 4.4 (regel 5247) |
| categorie Overlijden | gegevens over het overlijden van de ingeschrevene | — | 4.4 (regel 5261) |
| categorie Inschrijving | gegevens over de opneming en de status van de PL | — | 4.4 (regel 5263) |
| categorie Verblijfplaats | gegevens over het verblijf en adres van de ingeschrevene | — | 4.4 (regel 5267) |
| categorie Kind | gegevens over een kind van de ingeschrevene; 0, n keer | — | 4.4 (regel 5295) |
| categorie Verblijfstitel | gegevens over de verblijfsrechtelijke status van de ingeschrevene | — | 4.4 (regel 5317) |
| categorie Gezagsverhouding | gegevens betreffende het gezag over de ingeschrevene (gezag minderjarige of curatele) | — | 4.4 (regel 5319) |
| categorie Reisdocument | gegevens over een reisdocument van de ingeschrevene; 0, n keer | — | 4.4 (regel 5321) |
| categorie Kiesrecht | gegevens over het kiesrecht van de ingeschrevene (Europees kiesrecht, uitsluiting kiesrecht) | — | 4.4 (regel 5323) |
| categorie Tijdelijk verblijfsadres | adres waar betrokkene tijdelijk woont tijdens diens verblijf in Nederland; alleen in de RNI | — | 4.4 (regel 5327) |
| categorie Contactgegevens | telefoonnummer en/of e-mailadres waarop betrokkene bereikbaar is tijdens diens verblijf in Nederland; alleen in de RNI | — | 4.4 (regel 5331) |
| verwijzing | een van de persoonslijst afgeleide verzameling gegevens die verwijst naar een volgende, niet noodzakelijk huidige, gemeente van inschrijving | verwijsgegevens | 4.2.2 (regel 4943) |
| afnemersindicatie | geeft aan dat een persoonslijst wel of niet meer onderdeel is van de doelgroep van een afnemer of derde; staat bij de PL in BRP-V | categorie 14 | 4.2.3, 4.4 (regel 4957, 5325) |
| afnemer | overheidsorgaan waaraan of derde aan wie op systematische wijze gegevens worden verstrekt | overheidsorgaan, derde | 1.1 (regel 377) |
| reisdocument | Nederlands paspoort of Nederlandse Identiteitskaart | Nederlands reisdocument | 1.1 (regel 379) |
| ingezetene | persoon van wie de persoonslijst door de gemeente van inschrijving wordt bijgehouden | — | 1.5.2 (regel 449) |
| niet-ingezetene | persoon van wie de gegevens in de RNI worden bijgehouden; voormalig ingezetene of nooit-ingezetene | PL van een voormalig ingezetene, PL van een nooit-ingezetene | 1.6, 4.2.1 |
| Registratie niet-ingezetenen (RNI) | het systeem waarmee gegevens over niet-ingezetenen worden bijgehouden onder verantwoordelijkheid van de minister van BZK | RNI | 1.5.2 (regel 473) |
| BRP-Verstrekkingsvoorziening (BRP-V) | het onderdeel van de centrale voorzieningen dat de verstrekkingen van BRP-gegevens aan afnemers verzorgt; bevat een kopie van alle persoonslijsten | BRP-V | 1.5.2, 3.3.2 (regel 483, 4469) |
| eerste inschrijving | PL wordt actueel opgenomen als ingezetene bij aangifte verblijf en adres in Nederland of geboorte in Nederland | inschrijving | 1.6 (regel 553) |
| vervolginschrijving | inschrijving van een persoon die zich vestigt in een andere gemeente of vanuit de RNI; de gehele PL wordt overgebracht, de gemeente van vertrek of de RNI neemt verwijsgegevens op | hervestiging (vanuit de RNI) | 2.1.2 (regel 631) |
| opschorting bijhouding | status van een PL met reden E (emigratie), M (ministerieel besluit), R (aangelegd in de RNI), O (overlijden) of F (fout) | PL-status | 1.6 (regel 525) |
| aangewezen bestuursorgaan (ABO) | organisatie aangewezen in artikel 31 Besluit BRP vanwege een taak in de bijhouding van de gegevens van niet-ingezetenen | RNI-deelnemer | 1.5.2 (regel 477) |
| terugmeldvoorziening (TMV) | centrale voorziening waarmee afnemers aan de gemeenten kunnen terugmelden dat er gerede twijfel bestaat over een authentiek gegeven | terugmelding | 1.5.2 (regel 493) |
| informatieknooppunt (IKP) | centrale voorziening waar adresgegevenssignalen van signaalleveranciers bijeen worden gebracht en aan gemeenten worden geleverd voor adresonderzoek | — | 1.5.2 (regel 511) |
| ProtocolleringsOverzichtModule (POM) | tool die uit de vastgelegde verstrekkingen een voor de burger leesbaar overzicht produceert, uitsluitend op verzoek van de burger | — | 1.5.2 (regel 503) |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| gemeente | houdt bij (gedecentraliseerd) | persoonslijst van ingezetenen | 1.5.2 (regel 449) |
| gemeentelijke systemen | houden bij | persoonsgegevens van de burgers | 1.5.2 (regel 471) |
| minister van BZK | is verantwoordelijk voor | RNI | 1.5.2 (regel 473) |
| minister van BZK | verstrekt namens zich gegevens uit | BRP-V | 3.3.3 (regel 4479) |
| RNI | houdt bij | gegevens over niet-ingezetenen | 1.5.2 (regel 473) |
| aangewezen bestuursorgaan | dient in | inschrijvings- en bijhoudingsverzoeken (niet-ingezetenen) | 1.5.2 (regel 473) |
| IND | levert aan | verblijfstitelgegevens | 1.5.2 (regel 479) |
| RvIG | verstuurt | berichten over landelijke tabellen en paspoortsignaleringen | 1.5.2 (regel 481) |
| RvIG | draagt zorg voor de verspreiding van | landelijke tabellen | 1.5.2 (regel 457) |
| minister | stelt vast | landelijke tabellen | 1.5.2 (regel 457) |
| BRP-V | verzorgt | verstrekkingen van BRP-gegevens aan afnemers | 1.5.2 (regel 483) |
| BRP-V | bevat een kopie van | alle persoonslijsten | 3.3.2 (regel 4469) |
| afnemer | moet beschikken over | autorisatiebesluit | 3.3.3 (regel 4479) |
| afnemer | plaatst en verwijdert | afnemersindicatie | 4.2.3 (regel 4959) |
| afnemer | meldt terug aan gemeenten via | terugmeldvoorziening | 1.5.2 (regel 493) |
| gemeenten | reageren via de terugmeldvoorziening op | terugmelding | 1.5.2 (regel 493) |
| gemeente van vertrek of RNI | neemt op | verwijzing | 2.1.2 (regel 643) |
| gemeente van vestiging | voert uit | actualiseringsprocedures na ontvangst van de PL | 2.1.2 (regel 651) |
| ambtenaar | constateert | ten onrechte opgenomen PL (opschorting F) | 1.6 (regel 569) |
| persoonslijst | is onderverdeeld in | categorieën | 4.2.1 (regel 4903) |
| persoonslijst | bevat | categorie Verblijfplaats | 4.2.1 |
| persoonslijst | bevat | categorie Reisdocument | 4.2.1 |
| categorie Gezagsverhouding | wordt gebruikt voor | vaststelling van wettelijke vertegenwoordigers | 4.4 (regel 5319) |
| verwijzing | is afgeleid van | persoonslijst | 4.2.2 (regel 4943) |
| afnemersindicatie | hoort bij | persoonslijst in BRP-V | 4.2.3 (regel 4957) |
| persoonslijst | verhuist van de RNI naar | gemeente (vervolginschrijving) | 1.6 (regel 562) |
| IKP | levert signalen aan | gemeenten voor adresonderzoek | 1.5.2 (regel 511) |

## Relevantie voor de architectuur

- **Bedrijfsobjecten (kandidaten, gegevensbeschrijving):** persoonslijst met als onderdelen Persoon (ingeschrevene), Ouder, Kind, Huwelijk/geregistreerd partnerschap, Nationaliteit, Overlijden, Inschrijving, Verblijfplaats, Verblijfstitel, Gezagsverhouding, Reisdocument en Kiesrecht; daarnaast verwijzing en afnemersindicatie. Of elke categorie een eigen element wordt of een onderdeel van de persoonslijst, is een beoordeling; de afbakening noemt persoon, verblijfplaats, gezag, nationaliteit en reisdocument.
- **Gebeurtenissen:** eerste inschrijving, vervolginschrijving, hervestiging, opschorting bijhouding (emigratie, overlijden, fout).
- **Partijen:** gemeente (college), minister van BZK, RvIG, IND, aangewezen bestuursorgaan, afnemer.
- **Applicatielaag:** RNI, BRP-V, TMV, IKP, WALAA (webapplicatie voor adresonderzoek) en de berichtendienst zijn stelselcomponenten; kandidaten voor applicatiecomponenten, niet voor het bedrijfsmodel.
- **Buiten de afbakening gelaten:** rubrieken en elementen, landelijke tabellen, berichtenboek, conversies, dienstverleningsafspraken, verstrekkingsprocedures (autorisatietabel, spontane verstrekking, selectie).

## Citaten

> Een persoonslijst is het geheel van persoonsgegevens dat over een persoon in de BRP is opgenomen. (4.2.1)

> Een verwijzing is een van de persoonslijst afgeleide verzameling gegevens die verwijst naar een volgende, niet noodzakelijk huidige, gemeente van inschrijving. (4.2.2)

> Overheidsorgaan waaraan of derde aan wie op systematische wijze gegevens worden verstrekt of op grond van artikel 3.14 van de Wet BRP informatie beschikbaar wordt gesteld. (1.1, begrip Afnemer)

> Nederlands paspoort of Nederlandse Identiteitskaart. (1.1, begrip Reisdocument)

> Gegevens over de ingeschrevene. (4.4, categorie 01 Persoon)

> Gegevens over het verblijf en adres van de ingeschrevene. (4.4, categorie 08 Verblijfplaats)

> Gegevens betreffende het gezag over de ingeschrevene. (4.4, categorie 11 Gezagsverhouding)

> Bij een vervolginschrijving vestigt de persoon zich in een andere gemeente dan waar hij ingeschreven is (verder ook aangeduid als gemeente van vertrek) of hij vestigt zich in een gemeente terwijl hij thans als niet-ingezetene is ingeschreven. (2.1.2)

> Eenmaal ingeschreven, wordt de persoonslijst (PL) van een persoon niet meer verwijderd. (1.6)
