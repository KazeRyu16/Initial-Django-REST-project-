from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    My_discount = serializers.SerializerMethodField(read_only=True )
    class Meta:
        model = product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'My_discount'
        ]
    def get_My_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,product):
            return None
        return obj.get_discount()
    