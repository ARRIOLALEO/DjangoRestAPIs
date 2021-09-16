from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','image','category','create_at','modify_at',)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username',)
