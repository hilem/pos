FROM spacy_pre

ENV HOST 0.0.0.0
EXPOSE 5000

COPY server.py /usr/src/app/server.py

CMD ["python", "server.py"]
