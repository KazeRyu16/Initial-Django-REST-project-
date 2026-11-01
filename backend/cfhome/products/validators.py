from .models import product
from rest_framework import serializers

def validate_title(value):
    extra = product.objects.filter(title__iexact=value)
    if extra.exists():
        raise serializers.ValidationError(f"{value} already exists,try something different")
    return value