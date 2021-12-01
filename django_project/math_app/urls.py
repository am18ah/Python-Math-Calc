from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='math-home'),
    path('register/', views.register_request, name='math-register'),
    path('about/', views.about, name='math-about'),
    path('login/', views.login, name='math-login'),
    path('basicmath/', views.basicmath, name='basic-math'),
    path('trigonometry/', views.trigonometry, name='trigonometry'),
    path('algebra/', views.algebra, name='algebra'),
    ]

urlpatterns += staticfiles_urlpatterns()
