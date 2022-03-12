FROM ubuntu:latest

RUN apt update -y && apt upgrade -y
RUN apt install python3 pyton3-pip

ADD sites/ ~/
RUN cd ~/sites

RUN python3 -m http.server 8000