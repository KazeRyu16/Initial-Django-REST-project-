from .models import product
from rest_framework import viewsets

from .serializers import ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"