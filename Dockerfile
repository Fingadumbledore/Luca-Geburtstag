FROM ubuntu:latest

RUN apt update -y && apt upgrade -y
RUN apt install -y python3

ADD sites/ /sites

EXPOSE 8000

CMD [ "python3", "-m", "http.server", "--directory", "sites", "8000" ]