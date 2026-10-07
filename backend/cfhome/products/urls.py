from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductMixinView.as_view()),
    path('',views.ProductMixinView.as_view()),
    path('<int:pk>/update',views.ProductUpdateAPI.as_view()),
    path('<int:pk>/delete',views.product_delete_view.as_view())
]