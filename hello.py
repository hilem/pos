from __future__ import unicode_literals

import logging
import spacy.en

from flask import Flask
from flask import jsonify
from flask import request
from sets import Set
from spacy.parts_of_speech import NOUN

app = Flask(__name__)
nlp = spacy.en.English()
logging.basicConfig(format='%(asctime)s|%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

### Logic:
##  Find non-compound nouns.
##  Create the expanded noun-phrase for each found noun by:
###  - Recursively collapse tree of children, if any, around the noun.
###  - Strip the resultant list of words on each end of any non-noun words.

def strip_non_nouns(children):
    seen_noun = False
    tmp_str = ''
    build_str = ''
    for c in children:
        if c.pos == NOUN:
            seen_noun = True
            build_str += tmp_str
            build_str = (build_str + ' ' + c.orth_).strip()
            tmp_str   = ''
        elif seen_noun:
            if c.pos_ == 'PRT':
                tmp_str = tmp_str + c.orth_ #).strip()
            else:
                tmp_str = ' ' + (tmp_str + ' ' + c.orth_).strip()
    return build_str

def collapse_tree(token):
    result = [token]
    for l in reversed(list(token.lefts)):
        if l.children:
            result = [item for sublist in [collapse_tree(l), result] for item in sublist]
        else:
            result.insert(0, l)
    for r in token.rights:
        if r.children:
            result = [item for sublist in [result, collapse_tree(r)] for item in sublist]
        else:
            result.append(r)
    return result

def find_noun_phrases(tokens):
    result_set = Set([])
    for i, t in enumerate(tokens):
        logging.info('(%s, %s, %s HEAD %s, l#%s, r#%s, iob=%s)', t.orth_, t.pos_, t.dep_, t.head.orth_, t.n_lefts, t.n_rights, t.ent_iob)
        ## need to find examples where a noun that is also a dobj would be the 'subject'
        if t.pos == NOUN and t.dep_ != 'compound':
            tmp_list = collapse_tree(t)
            tmp = strip_non_nouns(tmp_list)
            logging.info('join result |%s|', tmp)
            result_set.add(tmp)
    return list(result_set)

@app.route('/')
def query():
    logging.info(' v   START OF REQUEST   v')
    query = request.args.get('q')
    if query is None:
        return jsonify(msg="missing q parameter")
    logging.info('query = %s', query)
    tokens = nlp(query)
    result = find_noun_phrases(tokens)
    logging.info('result = %s', result)
    return jsonify(nouns=result)

@app.route('/info')
def info():
    return jsonify(hatch_version="1.0", spaCy_version="0.85")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

## Scratch:
# tmp = " ".join(map(lambda x: x.orth_ if x.dep_ == 'compound' else '', t.children))
# [logging.info('child is %s', y.orth_) for y in x.head.children]
