from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


#from views import api_home

urlpatterns = [
    path('auth/',obtain_auth_token),
    path('',views.api_home),

]