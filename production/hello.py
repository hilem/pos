from __future__ import unicode_literals

import logging
import spacy.en

from flask import Flask
from flask import request
from spacy.parts_of_speech import NOUN

app = Flask(__name__)
nlp = spacy.en.English()
logging.basicConfig(format='%(asctime)s|%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

def filter_tokens(x):
    logging.warning('(%s, %s, %s HEAD %s)', x.orth_, x.pos_, x.dep_, x.head.orth_)
    [logging.warning('child is %s', y.orth_) for y in x.head.children]
    return x.pos == NOUN

@app.route('/')
def hello_world():
    query = request.args.get('q')
    if query is None:
        return "barf"
    app.logger.warning(query)
    tokens = nlp(query)
    filtered_tokens = filter(filter_tokens, tokens)
    if len(filtered_tokens) > 1:
        filtered_tokens = filter(lambda x: x.dep_ == 'OBJ', tokens)
    result = u''.join(tok.orth_ + ' ' for tok in filtered_tokens)
    app.logger.info(result)
    result = 'no subject' if len(result) == 0 else result
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
