from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User
# Create your tests here.

class TestModelBlos(TestCase):
    @classmethod

    def setUpTestData(cls):
        user1 = User.objects.create_user(username='test1',password='12313232')
        user1.save()

        blog1 = Blog.objects.create(user =user1,title='title',body='body')
        blog1.save()

    def testBlogData(self):
        blog = Blog.objects.get(id=1)
        expected_user = f'{blog.user}'
        expected_title = f'{blog.title}'
        expected_body = f'{blog.body}'
        self.assertEqual(expected_user,'test1')
        self.assertEqual(expected_title,'title')
        self.assertEqual(expected_body,'body')
