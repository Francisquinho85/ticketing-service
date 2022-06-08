FROM python:3.9

MAINTAINER Francisco Monteiro

LABEL version="1.0"

RUN mkdir /ticketing-app

WORKDIR /ticketing-app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080/tcp

ENTRYPOINT ["uvicorn", "main:app"]