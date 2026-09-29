---
title: "Basisregistratie Ondergrond Catalogus Grondwaterstandonderzoek (GLD)"
source: "https://docs.geostandaarden.nl/bro/gld/"
author: "Geonovum"
published: 2023-06-07
created: 2026-06-27
description: "BRO-catalogus voor het registratieobject Grondwaterstandonderzoek: entiteiten, attributen, kwaliteitsregimes en samenhang met GMN/GMW/GAR"
tags:
  - "Basisregistraties"
---

# Basisregistratie Ondergrond Catalogus Grondwaterstandonderzoek

**Versie:** Definitief, 07 juni 2023
**Informatiemodel door:** Geonovum
**Licentie:** CC-BY 4.0

## Doel en Scope

Deze catalogus beschrijft het registratieobject Grondwaterstandonderzoek (GLD) in detail. Het document dient voor alle gebruikers van de Basisregistratie Ondergrond en beantwoordt welke gegevens precies in het systeem zijn opgeslagen. Aanleveraars krijgen inzicht in verplichte gegevens en kwaliteitseisen; afnemers weten welke informatie zij kunnen verwachten.

## Context: Grondwatermonitoring in de BRO

Het grondwaterdomein in de BRO omvat vier registratieobjecten:

- **Grondwatermonitoringnet (GMN):** Verzameling van locaties voor periodiek onderzoek onder een bepaald monitoringdoel
- **Grondwatermonitoringput (GMW):** Fysieke constructie (buizen met filters) voor meting van grondwaterstand/-samenstelling
- **Grondwatersamenstellingsonderzoek (GAR):** Monitoring van grondwaterkwaliteit
- **Grondwaterstandonderzoek (GLD):** Monitoring van grondwaterkwantiteit (waterstand)

Een GLD betreft herhaaldelijke metingen van waterstand in een monitoringbuis. Het wordt uitgevoerd door of namens een bronhouder en levert beoordeelde tijd-meetwaardereeksen op.

## Het Proces van Grondwaterstandonderzoek

Het volledige proces van meting tot registratie omvat vijf stappen:

1. **Meten:** Waterstand wordt bepaald via handpeilingen, sensoren met datalogger, of telemetrische sensoren (GSM/LoRa)
2. **Omrekenen:** Meetwaarden worden omgerekend naar waterstand in meter t.o.v. NAP
3. **Controleren:** Tijdreeksen worden gecontroleerd op fouten en afwijkingen via integriteits-, representativiteits-, consistentie- en plausibiliteitschecks
4. **Corrigeren:** Systematische afwijkingen (sensordrift, tijdverschuiving) en fouten worden gecorrigeerd
5. **Keuren:** Eindoordeel over kwaliteit en bruikbaarheid bepaalt de status kwaliteitscontrole

## Entiteittypen en hun Attributen

### Grondwaterstandonderzoek (Hoofdentiteit)

Het registratieobject GLD bevat beoordeelde tijd-meetwaardereeksen van waterstand in meter NAP voor één filter van een GMW-put.

- **BRO-ID:** Unieke identificatie door BRO
- **Bronhouder:** Bestuursorgaan verantwoordelijk voor levering
- **Object-ID bronhouder:** Identificatienummer bij bronhouder
- **Dataleverancier:** Organisatie die data aanlevert
- **Kwaliteitsregime:** IMBRO (strikte eisen) of IMBRO/A (historische data met vrijstellingen)
- **Datum eerste meting / Datum recentste meting:** Afgeleid, wijzigbaar bij aanvullingen
- **Registratiegeschiedenis:** Formele geschiedenis van registratie in BRO
- **Grondwatermonitoringnet:** Verwijzing(en) naar een of meer monitornetten
- **Monitoringbuis:** Verwijzing naar de monitoringbuis (GMW + buisnummer)
- **TijdMeetwaardeWaarneming:** Observaties met meetwaardereeksen

### Registratiegeschiedenis

- Tijdstip registratie object, Registratiestatus, Tijdstip laatste aanvulling, Tijdstip voltooiing registratie
- Gecorrigeerd (boolean), Tijdstip laatste correctie
- In onderzoek (boolean), In onderzoek sinds
- Uit registratie genomen (boolean), Tijdstip uit/weer in registratie genomen

### Observatie

Geheel van gegevens en kenmerken van meetactiviteiten in bepaalde periode:

- **Observatie ID:** Unieke code (max. 40 tekens)
- **Observatieperiode:** Begindatum en einddatum
- **Tijdstip resultaat:** Moment waarop laatste proces werd afgerond
- **Metadata observatie:** Observatietype (regulier/controle), Mate beoordeling (volledig beoordeeld/voorlopig), Uitvoerder (KvK + naam)
- **Gerelateerd aan:** Verwijzingen naar bronobservaties en controlemetingen
- **Procedure:** Observatieproces met meetkenmerken
- **Resultaat:** Tijdmeetwaardereeks

### Observatieproces

- **Observatieproces ID:** Unieke code (max. 40 tekens)
- **Meetprocedure:** Werkvoorschrift (uit waardelijst)
- **Type meetinstrument:** Sensortype of handapparaat
- **Type luchtdrukcompensatie:** Voor druksensoren
- **Procestype:** Vast: "Algoritme"
- **Beoordelingsprocedure:** Procedure voor controle/correctie/keuring

### Tijdmeetwaardereeks en Tijdmeetwaardepaar

- **Tijdmeetwaardereeks ID:** Unieke code
- **Tijdmeetwaardepaar:** Tijdstip meting + Waterstand (m NAP)
- **Metadata:** Status kwaliteitscontrole (goedgekeurd/niet goedgekeurd/nog niet beoordeeld), Censuurreden, Censuurlimietwaarde, Interpolatietype

## Kwaliteitsregimes

**IMBRO:** Strikte eisen; alle verplichte gegevens moeten waarde hebben. Geldt voor gegevens na inwerkingtreding van de wet.

**IMBRO/A:** Versoepeld regime voor historische gegevens. Bepaalde verplichte attributen mogen "onbekend" zijn.

## Samenhang met Andere Registratieobjecten

- Elk GLD verwijst naar minstens één GMN (monitoringnet) en één GMW-buis (meetlocatie)
- De GMW moet bestaan voordat GLD kan worden aangeleverd
- De GMN moet consistent zijn: filters in GMW moeten op moment van meting meetpunten in die GMN zijn

## Relatie tot INSPIRE

Het registratieobject GLD valt onder INSPIRE-thema "Environmental Monitoring Facilities".

## Basering op WaterML 2.0

Het gegevensmodel volgt de OGC-standaard WaterML 2.0 voor uitwisseling van waterobservatiegegevens.
