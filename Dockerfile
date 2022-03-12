FROM ubuntu:latest

COPY . .
RUN apt update -y && apt upgrade -y
RUN apt install -y python3

ADD frontend/sites/ /sites

EXPOSE 8000

CMD [ "python3", "backend/server/server.py" ]