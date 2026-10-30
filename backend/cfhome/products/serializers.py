from rest_framework import serializers
from .models import product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    My_discount = serializers.SerializerMethodField(read_only=True )
    url = serializers.SerializerMethodField(read_only =True)
    class Meta:
        model = product
        fields = [
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'My_discount'
        ]

    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)
    
    def get_My_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,product):
            return None
        return obj.get_discount()
    