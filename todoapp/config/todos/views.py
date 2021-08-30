from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializers
# Create your views here.

class TodosAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DescriptionTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
