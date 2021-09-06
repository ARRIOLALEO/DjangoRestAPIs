from django.urls import path
from .views import PostCrudAPIView, ShowAllPostAPIView

urlpatterns =[
    path('<int:pk>/', PostCrudAPIView.as_view()),
    path('',ShowAllPostAPIView.as_view()),
]
