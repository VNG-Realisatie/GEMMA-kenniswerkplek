ICT - Gemeentelijk Gegevensmodel (GGM)

Ga naar inhoud

# ICT

De in de applicaties aanwezige gegevens zijn gestructureerd volgens bepaalde objecttypes. Deze zijn uitgewerkt in de in deze paragraaf uitgewerkte domeinmodellen.

In bovenstaand figuur is te zien hoe objecttypes zijn uitgewerkt. Een objecttype representeert de definitie van een bepaald objecttype. Zo’n objecttype kan nul of meer attributen hebben, die ieder volgens een bepaald datatype zijn. Objecttypes kunnen relaties hebben met andere objecttypes, volgens een bepaald relatiesoort. Ook kunnen objecttypes een generalisatie zijn van een ander objecttype. Hiermee wordt aangegeven dat het ene objecttype attributen en relaties overerft van het andere objecttype. Bovenstaande definitie is gebaseerd op MIM (Metamodel voor Informatiemodellen). Hieruit zijn alle relevante definities afgeleid.

Naast de zaken die onderdeel zijn van MIM is er het type Gegeven dat wordt gedefinieerd door een Objecttype. Een Gegeven kan één of meer classificaties hebben. In het huidige model wordt gewerkt met classificatie van persoonsgegevens:

- Geen Persoonsgegevens

- Algemene Persoonsgegevens

- Gevoelige Persoonsgegevens

- Bijzondere Persoonsgegevens

Gegevens kunnen geclassificeerd zijn conform bovenstaande lijst. Dit voor de gegevens zelf en de relaties met andere gegevens.
In bovenstaand figuur is ook te zien dat een Gegeven een Applicatie als authentieke bron kan hebben of dat gegevens afkomstig zijn uit een externe bron.

In voorgaande figuur is een uitwerking voor de CMDB-items gemaakt. Iedere CMDB-Item kan meerdere Log-items hebben waarbinnen aantekeningen worden gelogd. ‘Database’, ‘Server’ en ‘Applicatie’ zijn speciale Linkbare CMDB-items, en kunnen dus koppelingen hebben met andere Linkbare CMDB-Items. Applicaties en Servers kunnen een ‘Leverancier’ hebben.
Een ‘Applicatie’ kan daarnaast diverse medewerkers hebben gekoppeld met een eigen rol, zoals: functioneel beheerder, applicatie-eigenaar en superuser. Een Applicatie heeft één of meer versies en kan meerdere packages hebben. Daarnaast kunnen er documenten en notities zijn gekoppeld aan een ‘Applicatie’.

Naast de Linkbare CMDB-Items zijn er ook reguliere CMDB-Items (niet linkbaar aan andere CMDB-Items). Deze zijn uitgewerkt in

Het model kent naast de Linkbare CMDB-Items de volgende CMDB-Items die direct van CMDB-Item zijn afgeleid: ‘Licentie’, ‘Hardware’, ‘Vervoersmiddel’, ‘Netwerkcomponent’, ‘Toegangsmiddel’, ‘Inventaris’ en ‘Software’.
