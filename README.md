#### Steps to run locally:
- docker build -t spacy_pre prebuild/.  # This takes forever.
- docker build -t spacy_post development/.
- docker run -p 80:80 -p 5000:5000 spacy_post

##### After Starting an instance
- copy login credentials command from quay
- docker pull quay/hilem/pos

> docker run -d -p 80:80 quay.io/hilem/pos
> sudo gunicorn app:app -D -b 0.0.0.0:80
