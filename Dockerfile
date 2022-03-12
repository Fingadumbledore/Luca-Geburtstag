FROM alpine:latest

COPY . .

RUN apk add python3

ADD frontend/sites/ /sites
EXPOSE 8000

CMD [ "python3", "backend/server/server.py" ]