from algoliasearch_django import AlgoliaIndex  
from algoliasearch_django.decorators import register
from .models import product

@register(product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'public'
    ]
   
    tags = 'random_taglist'


