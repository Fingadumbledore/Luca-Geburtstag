FROM ubuntu:latest

RUN apt update -y && apt upgrade -y
RUN apt install -y python3 python3-pip

ADD sites/ /sites
RUN cd /sites

EXPOSE 8000

CMD [ "python3", "-m", "http.server", "8000" ]