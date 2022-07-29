#!/bin/bash

echo ------------------------[Überprüfung der Berechtigung]-----------------
if [ `/usr/bin/id -u` != "0" ]; then
      echo  fail "Du brauchst Rechte für dieses Skript"
      exit 0
else 
    echo Deine Rechte passen
fi

echo ------------------------[Prüfe ob System aktuell ist]------------------
sudo pacman -Syu python python3-pip sqlite3 docker docker-compose

echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/server.log

echo -----------------------[Fertigstellung]------------------------------- 
echo Vielen Dank das sie sich entschieden haben, mit Bash zu fliegen. Wir wünschen ihnen noch einen schönen Aufenthalt Adios 
echo -----------------------[Starte Server]---------------------------------
cd backend/server
python3 database.py
python3 server.py