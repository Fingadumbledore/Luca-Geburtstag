#!/bin/bash
#sudo apt install docker-compose python3 python3-pip && pip install mysql-connector-python  # installiert docker-compose und python3, um sicher zu gehen
echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/logging.txt 
echo ------------------------[Baue Server]----------------------------------
docker build -t luca -f Dockerfile .         # baut docker container mit namen luca
echo ------------------------[Initiiere Datenbank]--------------------------
cd backend
docker-compose --file docker-compose.yml up -d
cd ..
echo ------------------------[Starte Server]--------------------------------
docker run --rm -it -d -p 8000:8000 luca        # startet docker container
echo ========================[Alles bereit!]================================