from django.shortcuts import render
from elasticsearch import Elasticsearch
# from .models import Question


es = Elasticsearch()

def index(request):

    query = request.GET.get('query')
    context = {
        'query': query,
    }

    if query:
        res = es.search(index="movies", body={
            "query": {
                "query_string" : {
                    "default_field" : "text",
                    "query" : query
                }
            }})

        results = []
        for hit in res['hits']['hits']:
            title = hit['_source']['title']
            # del hit['_source']
            hit['_source'] = title
            results.append((hit['_score'], title))

        context['results'] = results


    return render(request, 'search/index.html', context)


# Nazwy własne z dużej litery
# ingorowanie stopwordów/wielkości liter/(sprawdzić zaimki)
#