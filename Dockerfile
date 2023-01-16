FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY ./src /app
COPY requirements.txt /app
RUN mkdir /static
RUN apt-get install inetutils-traceroute -y
RUN apt-get update && apt-get upgrade \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ENV  PORT 8080