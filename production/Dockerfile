FROM python:3.4-onbuild

RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
  && rm -rf /var/lib/apt/lists/*

RUN service supervisor stop

RUN python -m spacy.en.download

ENV HOST 0.0.0.0
EXPOSE 80

ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./server.py /usr/src/app/server.py

RUN service nginx stop

CMD supervisord -c /etc/supervisord.conf -n
