Tooling voor manipulatie repository - Gemeentelijk Gegevensmodel (GGM)

Ga naar inhoud

# Tooling voor het manipuleren van het GGM

Dit package bevat tooling voor het manipuleren van de database van het GGM. Hiermee kunnen bijvoorbeeld uitwisselingen met derde partijen worden vormgegeven, wordt de migratie naar MIM bewerkstelligd of kan worden ingezet om JSON-LD of databaseschema's te genereren. De tooling maakt gebruik van het feit dat het GGM is vastgelegd in Enterprise Architect van Sparx en dat deze de repository van het GGM in Sqllite wordt bijgehouden. Uit deze SQLlite-database kan de data worden gelezen en gemanipuleerd. Ook kan de SQLlite-database worden aangepast.

De gebruikte tooling is gebaseerd op Jupyter Notebooks en Python.

## Aan de slag

Zorg dat je Docker en Docker-compose hebt geïnstalleerd. Dit project is voortgebouwd op Docker Jupyter Minimal Notebook. Om te kunnen werken met de Jupoyter notebooks moet je de hele repository van het Gemeentelijk Gegevensmodel hebben gedownload. De notebooks bevragen direct de EA 16-versie van het Gemeentelijk Gegevensmodel.

### Start de container

Ga vanuit de root directory van je download van het Gemeentetelijk Gegevensmodel naar de subdirectory 'tools'. Start de jupyter container met het commando 'docker compose up'.

$ docker-compose up

### Toegang tot de notebooks

Je kunt nu bij de jupyter notebooks via http://localhost:8888/. De directories "input" en "output" uit de tools-directory zijn nu ook binnen de container gekloppeld en zichtbaar bij de notebooks.

### Notebooks gebruiken

Binnen de huidige toolset zijn de volgende notebooks beschikbaar:

- Import from Gemma. Maakt onderdeel uit van de uitwisseling van entiteiten met de GEMMA. Bedoeld om exports uit de GEMMA te importeren;

- Export to Gemma. Maakt onderdeel uit van de uitwisseling van entiteiten met de GEMMA. Bedoeld om exports te maken die in GEMMA geïmporteerd kunnen worden;

- Export to MIM. Work in progress! Bedoeld voor de omzetting van het GGM naar MIM.
