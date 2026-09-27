import json #imports json module
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from products.models import product
from products.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = product.objects.all().order_by("?").first()
    data = {}
    if instance :
       #data = model_to_dict(instance,fields=['id','title','price'])
       #return Response(data) # converts python dict to Json
       #json_data = json.dumps(data)
        data = ProductSerializer(instance).data
    return Response(data)
        
#    return HttpResponse(json_data, headers={"content-type":"application/json"})