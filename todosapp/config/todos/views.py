from rest_framework import generics
from .serializers import TodoSerializers
from .models import Todo
# Create your views here.

class TodosAPIViews(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
