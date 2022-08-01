#!/bin/bash

echo ------------------------[Überprüfung der Berechtigung]-----------------
if [ `/usr/bin/id -u` != "0" ]; then
      echo  fail "Digga wallah du brauchst Rechte für diesen Skript"
      exit 0
else 
    echo Digga tschüsch deine Rechte passen
fi

echo ------------------------[Prüfe ob System aktuell ist]------------------
sudo pacman -Syu python python-pip sqlite3 docker docker-compose python-flask

echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/server.log

echo -----------------------[Fertigstellung]------------------------------- 
echo Vielen Dank das sie sich entschieden haben, mit Bash zu fliegen. Wir wünschen ihnen noch einen schönen Aufenthalt Adios 
echo -----------------------[Starte Server]---------------------------------
export FLASK_APP=backend/server/new
flask run