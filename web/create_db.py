import os, glob
from datetime import datetime
from elasticsearch import Elasticsearch
from lib.normalization import normalize_srt


def load_data():
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    for path in glob.glob(os.path.join(data_dir, '*.srt')):
        text = normalize_srt(path)
        yield {
            "title": path,
            "text": text,
            "timestamp": datetime.now()
        }


es = Elasticsearch()

es.indices.create(index='movies', ignore=400)

for i, record in enumerate(load_data()):
    es.index(index="movies", doc_type="movie-type", id=i, body=record)

x = es.get(index="movies", doc_type="movie-type", id=7)['_source']
print(x)
