from rest_framework import generics, permissions
from .serializers import PostSerializers
from .models import Post
# Create your views here.

class ShowAllPostAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostCrudAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
