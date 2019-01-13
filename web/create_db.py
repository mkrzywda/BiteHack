import os, glob
from datetime import datetime
from elasticsearch import Elasticsearch
from lib.normalization import normalize_srt
import json
import pprint

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_data():
    for path in glob.glob(os.path.join(DATA_DIR, '*.srt')):
        text = normalize_srt(path)
        yield {
            "title": path,
            "text":" ". join(text),
            "timestamp": datetime.now()
        }


def load_json():
    movies = json.load(open(os.path.join(DATA_DIR, 'movies.json')))
    for key, values in movies.items():
        path = os.path.join(DATA_DIR, values['filename'])
        assert os.path.exists(path)

        text = normalize_srt(path)


# load_json()

es = Elasticsearch()
es.indices.delete(index='movies', ignore=[400, 404])
es.indices.create(index='movies', ignore=400)

for i, record in enumerate(load_data()):
    es.index(index="movies", doc_type="movie-type", id=i, body=record)

x = es.get(index="movies", doc_type="movie-type", id=7)['_source']

pprint.pprint(x)
