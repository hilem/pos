from __future__ import unicode_literals

import logging
import spacy.en
import subprocess

from flask import Flask
from flask import jsonify
from flask import request
try:    ## Note: Attempt to make file Python 2.7.x && 3.x compatible
    set
except NameError:
    from sets import Set as set
from spacy.parts_of_speech import NOUN

VERSION = "1.0.1"

app = Flask(__name__)
nlp = spacy.en.English(load_vectors=False) ## Passing the load_vectors params should save RAM
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
        ## Following 'or' was meant to handle things like 'head-to-head', needs further
        ## testing but I haven't found an instance where this creates a false-positive
        if c.pos == NOUN or (c.pos_ == 'ADV' and c.dep_ == 'compound'):
            seen_noun = True
            build_str += tmp_str
            if build_str.endswith('-'):
                build_str += c.orth_
            else:
                build_str = (build_str + ' ' + c.orth_).strip()
            tmp_str   = ''
        elif seen_noun:
            if c.pos_ == 'PRT' or c.pos_ == 'PUNCT': ## Possesive and/or punctuation
                tmp_str = tmp_str + c.orth_
            else:
                tmp_str = ' ' + (tmp_str + ' ' + c.orth_).strip()
    return build_str

def collapse_tree(token):
    result = [token]
    for l in reversed(list(token.lefts)):
        if l.pos_ == 'CONJ' or l.pos_ == 'PUNCT':    ## Break at conjuctives && punctuation
            break
        if l.children:
            result = [item for sublist in [collapse_tree(l), result] for item in sublist]
        else:
            result.insert(0, l)
    for r in token.rights:
        if r.pos_ == 'CONJ' or r.pos_ == 'PUNCT':    ## Break at conjuctives
            break
        if r.children:
            result = [item for sublist in [result, collapse_tree(r)] for item in sublist]
        else:
            result.append(r)
    return result

def find_noun_phrases(tokens):
    result_set = set([])
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
    return jsonify(
        pos_version=VERSION,
        spaCy_version=subprocess.check_output("pip list | grep spacy", shell=True).decode("utf-8"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

## Scratch:
# tmp = " ".join(map(lambda x: x.orth_ if x.dep_ == 'compound' else '', t.children))
# [logging.info('child is %s', y.orth_) for y in x.head.children]
