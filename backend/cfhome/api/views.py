from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
        
#    return HttpResponse(json_data, headers={"content-type":"application/json"})