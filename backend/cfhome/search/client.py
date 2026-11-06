from algoliasearch_django import algolia_engine

def get_index(index_name='cf_products'):
    client = algolia_engine.client
    index =  client.init_index(index_name)
    return index

def perform_search(query,**kwargs):
    index = get_index()
    results = index.search(query)
    return results
