FROM python:latest

<<<<<<< HEAD
RUN apt update -y && apt upgrade -y
RUN apt install -y python3

ADD frontend/sites/ /frontend/sites
=======
COPY . .
>>>>>>> develop

ADD frontend/sites/ /sites
EXPOSE 8000

<<<<<<< HEAD
CMD [ "python3", "-m", "http.server", "--directory", "/frontend/sites", "8000" ]
=======
CMD [ "python3", "backend/server/server.py" ]
>>>>>>> develop
