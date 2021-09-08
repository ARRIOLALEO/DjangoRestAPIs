from rest_framework import generics
from .models import Post
from .serializers import  PostSerializers

class ShowAllThePost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class CrudPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
