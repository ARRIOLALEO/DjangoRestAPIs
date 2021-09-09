from django.urls import path
from .views import CrudPostAPIView, ShowAllPostAPIView


urlpatterns =[
    path('<int:pk>/',CrudPostAPIView.as_view()),
    path('',ShowAllPostAPIView.as_view()),
]
