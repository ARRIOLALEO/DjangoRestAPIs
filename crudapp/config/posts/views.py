from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers

# Create your views here.

class PostShowAll(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class CrudPost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

