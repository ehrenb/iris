# Iris
Iris is a Google Play Store metadata scraper.  Scraped metadata is stored in a Postgres database, and forwarded to a RabbitMQ service for additional processing.

# Setup dependencies
* Install Docker (https://docs.docker.com/engine/installation/)
* Install docker-compose (https://docs.docker.com/compose/install/)

# Build

```bash
docker-compose build
```

# Run

```bash
docker-compose up -d
```

## History
Iris is almost entirely forked from an abondoned project Manoj Saha (https://github.com/manojps/google-play-apps-crawler-scrapy) -- so credit goes to him for most of this.  My intentions are do dockerize both it and the postgresql storage into one easy to run application.

docker build . -t behren/gplaycrawler && docker push behren/gplaycrawler
docker-compose up --scale gplay-crawler=2