from django.urls import path
from .views import CrudPost, PostShowAll

urlpatterns =[
    path('<int:pk>/',CrudPost.as_view()),
    path('',PostShowAll.as_view()),
]
