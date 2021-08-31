from rest_framework import fields, serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description')
