from algoliasearch_django import algolia_engine


def getclient():
    return algolia_engine.client


def perform_search(query, **kwargs):
    client = getclient()

    search_params = {
        'query': query,
        **kwargs
    }

    results = client.search_single_index(
        index_name='product',
        search_params=search_params
    )

    return results.to_dict()
  
