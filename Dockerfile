FROM ubuntu
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 pyton3-pip
RUN python3 -m http.server 8000