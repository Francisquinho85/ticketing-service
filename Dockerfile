FROM python:3.9

MAINTAINER Francisco Monteiro

LABEL version="1.0"

RUN mkdir /app-ticketing

WORKDIR /app-ticketing

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080/tcp

ENTRYPOINT ["uvicorn", "main:app"]