from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

es.indices.create(index='my-index', ignore=400)

es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

x = es.get(index="my-index", doc_type="test-type", id=42)['_source']
print(x)
