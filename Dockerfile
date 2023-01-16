FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY ./src /app
COPY requirements.txt /app
RUN mkdir /static
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install inetutils-traceroute -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV  PORT 8080