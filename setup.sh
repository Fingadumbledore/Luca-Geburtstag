#!/bin/bash

echo ------------------------[Überprüfung der Berechtigung]-----------------
if [ `/usr/bin/id -u` != "0" ]; then
      echo  fail "Du brauchst Rechte für dieses Skript\n"
      exit 0
else 
    echo Deine Rechte passen
fi

echo ------------------------[Prüfe ob System aktuell ist]------------------
sudo apt update && sudo apt upgrade && sudo apt full-upgrade

echo ------------------------[Installiere zusätzliche Packete]--------------
sudo apt install python3 python3-pip && sudo apt install sqlite3

echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/server.log

echo -----------------------[Fertigstellung]------------------------------- 
echo Vielen Dank das sie sich entschieden haben, mit Bash zu fliegen. Wir wünschen ihnen noch einen schönen Aufenthalt Adios 
sleep 5
echo -----------------------[Starte Server]---------------------------------
cd backend/server
python3 database.py
python3 server.py