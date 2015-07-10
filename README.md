# Parts-of-Speech Parser

This application takes a string of text as input and outputs identified noun phrases


### Dependancies

1. [Install Python](https://www.python.org/downloads/)
1. [Install Docker](http://docs.docker.com/mac/step_one/).
1. [Install spacy](https://honnibal.github.io/spaCy/quickstart.html#install)


### Steps to run locally

1. `docker build -t spacy_pre prebuild/.  # This takes forever.`
1. `docker build -t spacy_post .`
1. `docker run -p 5000:5000 spacy_post`



> docker run -d -p 5000:5000 quay.io/hilem/pos
> sudo gunicorn app:app -D -b 0.0.0.0:80