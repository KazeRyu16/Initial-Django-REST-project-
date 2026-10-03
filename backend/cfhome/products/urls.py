from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.DetailedProductView.as_view()),
    path('',views.ProductListCreateAPI.as_view()),
    path('<int:pk>/update',views.ProductUpdateAPI.as_view()),
]