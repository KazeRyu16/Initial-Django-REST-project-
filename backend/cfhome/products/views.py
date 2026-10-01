from rest_framework import generics

from .models import product
from .serializers import ProductSerializer

class DetailedProductView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPI(generics.CreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = title
        serializer.save(content=content)