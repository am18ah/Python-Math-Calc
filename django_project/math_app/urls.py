from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='math-home'),
    path('register/', views.register_request, name='math-register'),
    path('about/', views.about, name='math-about'),
    path('login/', views.login, name='math-login'),
    ]