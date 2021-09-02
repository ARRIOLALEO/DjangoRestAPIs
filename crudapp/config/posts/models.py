from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    create_at = models.DateField(auto_now_add=True)
    modify_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title