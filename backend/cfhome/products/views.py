from rest_framework import generics
from rest_framework.decorators import api_view

from .models import product
from .serializers import ProductSerializer

class DetailedProductView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductUpdateAPI(generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer): 
        instance = serializer.save
        
 
