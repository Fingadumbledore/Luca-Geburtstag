#/bin/bash
echo ------------------------[Baue DB]--------------------------------------
docker-compose build #baut den Container
echo ------------------------[Starte DB]------------------------------------
docker-compose up -d #startet den Container im Hintergrund