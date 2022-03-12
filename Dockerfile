FROM ubuntu:latest

RUN apt update -y && apt upgrade -y
RUN apt install -y python3

ADD frontend/sites/ /frontend/sites

EXPOSE 8000

CMD [ "python3", "-m", "http.server", "--directory", "/frontend/sites", "8000" ]