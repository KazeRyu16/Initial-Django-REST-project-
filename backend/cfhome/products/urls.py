from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.DetailedProductView.as_view()),
    path('',views.ProductCreateAPI.as_view()),
]