from django.urls import path
from .views import ShowAllBlogsAPIView, CrudBlog

urlpatterns = [
    path('<int:pk>/',CrudBlog.as_view()),
    path('',ShowAllBlogsAPIView.as_view()),
]
