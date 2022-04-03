#!/bin/bash

# Dieses Skript ist dafür zuständig, die benötigte Umgebung für die Datenbank und den Server zu erstellen.
# Es werden folgende Packete geladen:
# Python3,
# python3 pip,
# mysql-connector-python.
# Folgende Ordner werden erstellt:
# /etc/systemd/system/wserver.service

bash clean.sh
echo ------------------------[Überprüfung der Berechtigung]-----------------
if [ `/usr/bin/id -u` != "0" ]; then
      echo  fail "Du brauchst Rechte für dieses Skript\n"
      exit 0
else 
    echo Deine Rechte passen
fi

echo ------------------------[schaue ob Dateien bereits existieren]---------
if [ ! -f /etc/systemd/system/wserver.service ]; then
    echo "Datei wurde nicht gefunden"
else 
    echo "Datei existiert bereits"
    exit 0
    
fi
echo ------------------------[Prüfe ob System aktuell ist]------------------
sudo apt update && sudo apt upgrade && sudo apt full-upgrade

echo ------------------------[Installiere zusätzliche Packete]--------------
sudo apt install docker-compose python3 python3-pip && pip install mysql-connector-python

echo ------------------------[Erstelle Service]-----------------------------
sudo touch /etc/systemd/system/wserver.service

echo  "Description = Web server" >> /etc/systemd/system/wserver.service
echo " After network.target = auditd.service"   >> /etc/systemd/system/wserver.service
echo " " >> /etc/systemd/system/wserver.service
echo " [Service] "  >> /etc/systemd/system/wserver.service
echo " Type = forking " >> /etc/systemd/system/wserver.service
echo " ExecStart = /home/$USER/Luca-Geburtstag/backend/run.sh " >> /etc/systemd/system/wserver.service
echo " " >> /etc/systemd/system/wserver.service
echo " [Install]"  >> /etc/systemd/system/wserver.service
echo " WantedBy = multi-user.target" >> /etc/systemd/system/wserver.service
echo ------------------------[Service wurde erstellt]-----------------------

echo ------------------------[Leere log Datei]------------------------------
echo "" > backend/server/server.log

cd /etc/systemd/system
systemctl enable wserver.service

echo ------------------------[Service wurde gestartet]---------------------

echo -----------------------[Fertigstellung]------------------------------- # der Neustart ist dafür dar, dass der Service 1A funktioniert
echo Vielen Dank das sie sich entschieden haben, mit Bash zu fliegen. Wir wünschen ihnen noch einen schönen Aufenthalt Adios 
echo $HOSTNAME wird automatisch neugestartet 
sleep 10
# sudo reboot now