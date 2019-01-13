from django.shortcuts import render
from elasticsearch import Elasticsearch
# from .models import Question


es = Elasticsearch()

def index(request):

    query = request.GET.get('query', '')
    context = {
        'query': query,
    }

    if query:
        res = es.search(index="movies", body={
            "query": {
                "query_string" : {
                    # "default_field" : "text",
                    "fields": ["title^5", "text", "keywords^5", "actors^2", "scenario^2", "genres", "direction^2"],
                    "query" : query
                }
            }})

        results = []
        for hit in res['hits']['hits']:
            # title = hit['_source']['title']
            # del hit['_source']
            result = hit['_source']
            result['score'] = round(hit['_score'], 2)
            result['size'] = min(200, 40*result['score'])
            if(result['score'] < 0.5):
                continue
            results.append(result)
            # results.append((hit['_score'], title))

        context['results'] = results

    return render(request, 'search/index.html', context)


# Nazwy własne z dużej litery
# ingorowanie stopwordów/wielkości liter/(sprawdzić zaimki)
#
