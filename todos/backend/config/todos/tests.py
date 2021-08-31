from django.test import TestCase
from .models import Todo
# Create your tests here.

class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='First Todo',description='description')

    def testTitleTodo(self):
        todo = Todo.objects.get(id=1)
        expect_title_todo = f'{todo.title}'
        self.assertEqual(expect_title_todo,'First Todo')

    def testDescriptionTodo(self):
        todo = Todo.objects.get(id=1)
        expect_desc_todo = f'{todo.description}'
        self.assertEqual(expect_desc_todo,'description')
