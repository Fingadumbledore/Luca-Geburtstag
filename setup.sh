#!/bin/bash
#sudo apt install docker-compse python3  # installiert docker-compose und python3, um sicher zu gehen

docker build -t luca -f Dockerfile .                  # baut docker container mit namen luca
docker run --rm -it -p 8000:8000 luca        # startet docker container