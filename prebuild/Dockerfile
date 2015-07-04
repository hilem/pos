FROM python:3.4-onbuild

RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
  && rm -rf /var/lib/apt/lists/*

RUN service supervisor stop

RUN python -m spacy.en.download
