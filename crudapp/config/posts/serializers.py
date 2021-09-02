from rest_framework import fields, serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','author','body','create_at','modify_at')
