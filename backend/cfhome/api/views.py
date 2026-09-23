import json #imports json module
from django.http import JsonResponse
from products.models import product

def api_home(request, *args, **kwargs):
    model_data = product.objects.all().order_by("?").first()
    data = {}
    if model_data :
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)