from rest_framework import generics

from products.models import product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from . import client

 
class SearchListView(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        query = request.GET.get('q')
        if not query:
            return Response('',status=400)     
        results = client.perform_search(query)
        return Response(results)

class SearchListOldvView(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get('q')
        results = product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q,user = user)
        return results

