from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, UserSerializers
# Create your views here.

class ShowAllProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CrudAPIProcductsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
