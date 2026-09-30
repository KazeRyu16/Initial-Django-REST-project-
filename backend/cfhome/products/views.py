from rest_framework import generics

from .models import product
from .serializers import ProductSerializer

class DetailedProductView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

