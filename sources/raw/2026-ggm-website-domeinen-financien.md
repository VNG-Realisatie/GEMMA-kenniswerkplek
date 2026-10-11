Financiën - Gemeentelijk Gegevensmodel (GGM)

Ga naar inhoud

# Financiën

De gegevensdefinities voor financiën zijn opgedeeld in:

- gegevens voor budgetverantwoordelijkheid en begroting;

- gegevens over verplichtingen en facturen;

- gegevens over batchverwerking en mutaties.

In onderstaand figuur is uitgewerkt hoe de begroting is opgebouwd, en welke verantwoordelijken er bij de begroting zijn.

De entiteit ‘Begroting’ is hiërarchisch opgebouwd uit: hoofdstukken, doelstellingen, producten en kostenplaatsen. Ieder van deze begrotingsonderdelen hebben begrotingsregels die optellen tot een sluitende ‘Begroting’. Met andere woorden: de som van alle begrotingsregels van de hoofdstukken van een ‘Begroting’ tellen op tot de ‘Begrotingsregel’ van de ‘Begroting’ binnen een bepaalde ‘Periode’. Hetzelfde geldt voor doelstellingen t.o.v. een ‘Hoofdstuk’, producten t.o.v. een ‘Doelstelling’ en kostenplaatsen t.o.v. een ‘Product’.
Kostenplaatsen kunnen meerdere hoofdrekeningen hebben om verschillende soorten kosten van elkaar te kunnen onderscheiden. Voorbeelden van verschillende soorten kostenplaatsen zijn: investeringskostenplaats, afdelingskostenplaats, projectkostenplaats en kostenplaatsen bij gemeentelijk vastgoed.

Opdrachtgevers kunnen opdrachtgever zijn naar doelstellingen of producten. Opdrachtnemers zijn budgetverantwoordelijk voor producten of kostenplaatsen. Opdrachtgevers zijn in de meeste gevallen programmanagers en opdrachtnemers hoofden van afdelingen.
In onderstaande figuur is weergegeven hoe verplichtingen en facturen zijn gestructureerd.

Om een verplichting aan een ‘Crediteur’ (vaak leverancier) aan te gaan is een ‘inkooporder’ nodig. Inkooporders kunnen meerdere kostenplaatsen hebben, die weer verschillende hoofdrekeningen kunnen hebben. Vanuit een ‘Inkooporder’ wordt er geschreven op 1 of meer hoofdrekeningen, zodat verschillende kostensoorten zijn te onderscheiden. Inkomende facturen worden gekoppeld aan de ‘Inkooporder’ en zijn zo gekoppeld aan de ‘Kostenplaats’. In het figuur is ook te zien hoe ‘Activa’ zijn gekoppeld aan hoofdrekeningen.
In de volgende figuur zijn mutaties uitgewerkt. Mutaties zijn wijzigingen van 1 hoofdrekening naar een andere hoofdrekening. Zoals voor begroting en uitgaven van ‘Begroot’ naar ‘Inkooporder’ of van ‘Inkooporder’ naar ‘Werkelijk’, of voor inkomsten van “Betaling onderweg" naar “Liquide”.
Mutaties vinden plaats op basis van diverse gebeurtenissen, zoals: verwerken van een binnenkomende ‘Batch’, het verwerken van een factuur of een bankafschrift. Batches, facturen en bankafschriften hebben ieder meerdere regels, en per regel wordt een ‘Mutatie’ aangemaakt en middelen van een hoofdrekening naar de ander geschreven, zoals hiervoor beschreven.

Mutaties hebben altijd betrekking op een ‘Kostenplaats’, en kunnen op een ‘Werkorder’ (niet hard afdwingbaar) of ‘Subrekening’ (gekoppeld aan kostenplaats vanwege BTW) worden geschreven.
Naast de gemodelleerde mutaties zijn er nog diverse mutaties die handmatig of binnen GFS automatisch worden aangemaakt en geboekt, zoals:

- Verkoop tot ontvangst.

- Inkoop tot betaling.

- BTW-compensatie.

- Vaste activa.

Debiteuren en crediteuren zijn afgeleid van ‘Rechtspersoon’. Het kunnen immers natuurlijke en niet-natuurlijke personen betreffen. Opdrachtgevers en opdrachtnemers zijn gekoppeld aan de Functie, en niet aan de persoon. Zo is zijn deze verantwoordelijkheden losgekoppeld van de persoon die de functie feitelijk invult. Zie hiervoor de volgende figuur.
