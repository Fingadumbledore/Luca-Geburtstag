#!/bin/bash
#sudo apt install docker-compose python3  # installiert docker-compose und python3, um sicher zu gehen
echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/server.log 
echo ------------------------[Baue Server]----------------------------------
docker build -t luca -f Dockerfile .         # baut docker container mit namen luca
echo ------------------------[Starte Server]--------------------------------
docker run --rm -it -d -p 8000:8000 luca        # startet docker container
echo ------------------------[Initiiere Datenbank]--------------------------
docker-compose --file backend/docker-compose.yml up
echo ========================[Alles bereit!]================================