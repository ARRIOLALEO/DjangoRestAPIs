from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title