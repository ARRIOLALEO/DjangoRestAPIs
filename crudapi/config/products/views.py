from django.contrib.auth import get_user_model
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer, UserSerializers
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
