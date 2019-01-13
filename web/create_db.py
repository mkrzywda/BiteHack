import os, glob
from datetime import datetime
from elasticsearch import Elasticsearch
from lib.normalization import normalize_srt
import json
import pprint

def load_data():
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    for path in glob.glob(os.path.join(data_dir, '*.srt')):
        print(path)
        text = normalize_srt(path)
        print(text)
        yield {
            "title": path,
            "text":" ". join(text),
            "timestamp": datetime.now()
        }

es = Elasticsearch()
es.indices.delete(index='movies', ignore=[400, 404])
es.indices.create(index='movies', ignore=400)

for i, record in enumerate(load_data()):
    es.index(index="movies", doc_type="movie-type", id=i, body=record)

x = es.get(index="movies", doc_type="movie-type", id=7)['_source']

pprint.pprint(x)
