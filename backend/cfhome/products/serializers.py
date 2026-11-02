from rest_framework import serializers
from .models import product
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from .validators import validate_title
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    date_joined = UserPublicSerializer(read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    My_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only =True)
    url = serializers.HyperlinkedIdentityField(
        view_name ='product-detail',
        lookup_field = 'pk')
    title = serializers.CharField(validators=[validate_title])
    #email = serializers.EmailField(write_only = True) # adds a email field on the apiview
    class Meta:
        model = product
        fields = [
            'owner',
            'date_joined',
            'title',
            'edit_url',
           #'email',
            'url',
            #'pk',
            'content',
            'price',
            'sale_price',
            'My_discount',
            # 'my_user_data'
        ]

    # def validate_title(self,value):   #validates and allows the serializer to not accept the same title twice
    #     extra = product.objects.filter(title__iexact=value)
    #     if extra.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    #def create(self,validated_data):  # to add take in email from the api-view and give us the emial address
        # email = validated_data.pop('email')
        # obj = super().create(validated_data)
        # print(email,obj)
        # return obj

    # def get_my_user_data(self,obj):
    #     return {
    #         "username": obj.user.username
    #     }

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
    
    def get_My_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,product):
            return None
        return obj.get_discount()
    