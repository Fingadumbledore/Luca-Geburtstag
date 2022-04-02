#!/bin/sh

rm /etc/systemd/system/wserver.service
docker stop --force /backend-db-1 
docker stop --force luca
docker rmi luca --force
docker rmi mysql --force