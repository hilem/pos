FROM spacy_pre

ENV HOST 0.0.0.0
EXPOSE 80 5000

ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./stopwords.csv /usr/src/app/stopwords.csv
ADD ./server.py /usr/src/app/server.py

RUN service nginx stop

CMD supervisord -c /etc/supervisord.conf -n
