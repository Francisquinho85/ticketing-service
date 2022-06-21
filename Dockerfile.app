FROM python:3.9.4-slim

MAINTAINER Francisco Monteiro

LABEL version="1.0"

RUN mkdir /app-ticketing
RUN mkdir /app-ticketing/www

WORKDIR /app-ticketing

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080/tcp

VOLUME /app-ticketing/www

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]