from rest_framework import generics,mixins
from rest_framework.decorators import api_view

from .models import product
from .serializers import ProductSerializer

class DetailedProductView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer # works fine till here but the content is set to none

    def perform_create(self, serializer):
        print(serializer.validated_data)  # prints the data in the server terminal
        title = serializer.validated_data.get('title') # getting the title from the database
        content = serializer.validated_data.get('content')or None
        if content is None:  #if content is none then title == content
            content = title
        serializer.save(content=content)  # this custom function just makes the content same as title

class ProductUpdateAPI(generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer): 
        instance = serializer.save
        if not instance.content:
            instance.content = instance.title


class product_delete_view(generics.DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance): 
       super().perform_destroy(instance)

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
          




        
 
