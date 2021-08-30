from django.test import TestCase
from .models import Todo
# Create your tests here.

class ModelsTestTodo(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo',description='description')

    def test_title_model(self):
        todo = Todo.objects.get(id=1)
        expect_name_todo = f'{todo.title}'
        self.assertEqual(expect_name_todo,'first todo')

    def test_desciption_todo(self):
        todo = Todo.objects.get(id=1)
        expect_description_todo = f'{todo.description}'
        self.assertEqual(expect_description_todo,'description')
