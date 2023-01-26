FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY mains /mains
WORKDIR /mains


CMD [ "python3", "db.py", "run"]
CMD [ "python3", "main.py", "run"]