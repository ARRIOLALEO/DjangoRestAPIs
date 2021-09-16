from django.urls import path
from .views import CrudAPIProcductsView, ShowAllProductsAPIView, UserDetails, UserList

urlpatterns=[
    path('users/',UserList.as_view()),
    path('users/<int:pk>/',UserDetails.as_view()),
    path('<int:pk>/',CrudAPIProcductsView.as_view()),
    path('',ShowAllProductsAPIView.as_view()),
]
