from django.urls import path
from .views import CrudAPIProcductsView, ShowAllProductsAPIView

urlpatterns=[
    path('<int:pk>/',CrudAPIProcductsView.as_view()),
    path('',ShowAllProductsAPIView.as_view()),
]
