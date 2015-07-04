#### Steps to run locally:
- docker build -t spacy_pre prebuild/.  # This takes forever.
- docker build -t spacy_post .
- docker run -p 5000:5000 spacy_post



> docker run -d -p 5000:5000 quay.io/hilem/pos
> sudo gunicorn app:app -D -b 0.0.0.0:80