# Parts-of-Speech Parser

This application takes a string of text as input and outputs identified noun phrases


### Dependancies

1. [Python 2.7 or 3.0](https://www.python.org/downloads/)
1. [Docker](http://docs.docker.com/mac/step_one/)
1. [spacy](https://honnibal.github.io/spaCy/quickstart.html#install)


### Running Locally

1. `docker build -t spacy_pre prebuild/.  # This takes forever.`
1. `docker build -t spacy_post .`
1. `docker run -p 5000:5000 spacy_post`


### Alternate Method 

1. `docker run -d -p 5000:5000 quay.io/hilem/pos`
1. `sudo gunicorn app:app -D -b 0.0.0.0:80`
1. `<Add in missing step>`
