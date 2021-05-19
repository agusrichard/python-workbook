# Base image
FROM python:3.8

LABEL agusrichard "agus.richard21@gmail.com"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000