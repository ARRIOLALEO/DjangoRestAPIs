from django.urls import path
from .views import CrudPostApi, GetAllPostAPIView

urlpatterns =[
    path('<int:pk>/',CrudPostApi.as_view()),
    path('',GetAllPostAPIView.as_view()),
]
