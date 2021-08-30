from django.test import TestCase
from .models import Todo
# Create your tests here.

# Todos model test

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo",description='description')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expexted_object_name = f'{todo.title}'
        self.assertEqual(expexted_object_name,'first todo')

    def test_description_content(self):
        todo = Todo.objects.get(id=1)
        expexted_object_name=f'{todo.description}'
        self.assertEqual(expexted_object_name,'description')


