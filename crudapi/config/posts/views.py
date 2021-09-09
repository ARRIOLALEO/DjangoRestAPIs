from rest_framework import generics
from .models import Post
from .serializers import PostSerializers
# Create your views here.

class ShowAllPostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class CrudPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
