FROM python:latest

COPY . .

ADD frontend/sites/ /sites
EXPOSE 8000

CMD [ "python3", "backend/server/server.py" ]