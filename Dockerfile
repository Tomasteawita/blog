FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    gcc \
    libc-dev \
    mariadb-dev \
    linux-headers \
    musl-dev \
    pkgconfig

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt