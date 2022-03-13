#!/bin/bash
#sudo apt install docker-compse python3  # installiert docker-compose und python3, um sicher zu gehen
echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/logging.txt 
echo ------------------------[Baue Server]----------------------------------
docker build -t luca -f Dockerfile .                  # baut docker container mit namen luca
echo ------------------------[Starte Server]--------------------------------
docker run --rm -it -p 8000:8000 luca        # startet docker container

