from django.urls import path
from .views import CrudPost, ShowAllThePost

urlpatterns =[
    path('<int:pk>/',CrudPost.as_view()),
    path('',ShowAllThePost.as_view()),
]
