from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

es.indices.create(index='movies', ignore=400)

es.index(index="movies", doc_type="movie-type", id=42, body={"text": " ","timestamp": datetime.now()})

x = es.get(index="movies", doc_type="movie-type", id=42)['_source']
print(x)
