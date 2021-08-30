from django.urls import path
from .views import DescriptionTodo, TodosAPIView

urlpatterns =[
    path('<int:pk>/',DescriptionTodo.as_view()),
    path('',TodosAPIView.as_view()),
]
