from rest_framework import generics

from products.models import product
from products.serializers import ProductSerializer

class SearchListView(generics.ListAPIView):
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

