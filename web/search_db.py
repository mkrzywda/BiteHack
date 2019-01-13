from datetime import datetime
from elasticsearch import Elasticsearch
import json
import os
import sys

es = Elasticsearch()
query = " ".join(sys.argv[1:])

res = es.search(index="movies", body={"query": {
        "query_string" : {
            "default_field" : "text",
            "query" : query
        }
    }})

print("Got %d Hits:" % res['hits']['total'])
print("Hits %s" % res)
