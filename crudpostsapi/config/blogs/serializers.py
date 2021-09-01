
from rest_framework import fields, serializers
from .models import Blog

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields =('id','user','title','body','create_at','modify_at')
