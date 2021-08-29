from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import Book

class BoosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','author','description')
