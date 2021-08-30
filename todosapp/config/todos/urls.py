from django.urls import path
from .views import TodosAPIViews, DetailTodo

urlpatterns =[
    path('<int:pk>/',DetailTodo.as_view()),
    path('',TodosAPIViews.as_view()),
]
