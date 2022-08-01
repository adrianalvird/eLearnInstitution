from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donators', views.donators, name='donators'),
    path('blueprint', views.blueprint, name='blueprint'),
     
]
