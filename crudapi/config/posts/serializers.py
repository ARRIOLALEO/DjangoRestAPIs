from rest_framework import fields, serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','body','create_at','modify_at',)
