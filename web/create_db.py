import os, glob
from datetime import datetime
from elasticsearch import Elasticsearch
from lib.normalization import normalize_srt
import json
import pprint
from lib.word_counter import word_counter
from lib.percentage_of_words import percentage_of_words


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_data():
    for path in glob.glob(os.path.join(DATA_DIR, '*.srt')):
        text = normalize_srt(path)
        yield {
            "title": path,
            "text": " ". join(text),
            "timestamp": datetime.now()
        }


def load_json():
    movies = json.load(open(os.path.join(DATA_DIR, 'movies.json')))
    for key, values in movies.items():
        path = os.path.join(DATA_DIR, values['filename'])
        assert os.path.exists(path)
        values['text'] = normalize_srt(path)

        z = word_counter(values['text']).most_common(50)
        values['keywords'] = [i for i, _ in z]
        values['swearscore'] = round(100.0*percentage_of_words("swear_words", values['text']), 2)

        yield values


es = Elasticsearch()
es.indices.delete(index='movies', ignore=404)
es.indices.create(index='movies', body={
     "settings": {
       "analysis": {
         "analyzer": {
           "blogs_analyzer": {
             "type": "standard",
             "stopwords": "_english_"
           }
         }
       }
     }
    }, ignore=400)

for i, record in enumerate(load_json()):
    es.index(index="movies", doc_type="movie-type", id=i, body=record)

x = es.get(index="movies", doc_type="movie-type", id=7)['_source']

pprint.pprint(x)
