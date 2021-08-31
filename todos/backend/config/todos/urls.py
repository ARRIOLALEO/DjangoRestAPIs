from django.urls import path
from .views import TodoAPIView, TodoDescription

urlpatterns =[
    path('<int:pk>/',TodoDescription.as_view()),
    path('',TodoAPIView.as_view()),
]

