from rest_framework import generics
from .serializers import TodoSerializers
from .models import Todo

# Create your views here.

class TodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoDescription(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
