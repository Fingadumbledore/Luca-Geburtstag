#!/bin/sh
echo "" > backend/server/server.log
sudo systemctl disable wserver.service
rm /etc/systemd/system/wserver.service