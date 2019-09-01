FROM alpine:latest

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    ca-certificates \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    openssl-dev \
    py-psycopg2 

RUN pip install Scrapy \
    && pip install pika \
    && pip install protobuf \
    && pip install gpapi \
    && rm -rf /var/cache/apk*

WORKDIR /app
COPY gplaycrawler /app

ENTRYPOINT cd /app && scrapy crawl playcrawler
