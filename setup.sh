#!/bin/bash
#sudo apt install docker-compose python3 python3-pip && pip install mysql-connector-python  # installiert docker-compose und python3, um sicher zu gehen
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

#echo ------------------------[Baue Server]----------------------------------
#docker build -t luca -f Dockerfile .         # baut docker container mit namen luca
#echo ------------------------[Initiiere Datenbank]--------------------------
#cd backend
#docker-compose --file docker-compose.yml up -d
#cd ..
#echo ------------------------[Starte Server]--------------------------------
#docker run --rm -it -d -p 8000:8000 luca        # startet docker container
