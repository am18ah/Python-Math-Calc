from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='math-home'),
    path('register/', views.register, name='math-register'),
    path('about/', views.about, name='math-about'),
    path('login/', views.user_login, name='math-login'),
    path('signout/', views.signout, name='math-signout'),
    path('basicmath/', views.basicmath, name='basic-math'),
    path('trigonometry/', views.trigonometry, name='trigonometry'),
    path('algebra/', views.algebra, name='algebra'),
    path('statistics/', views.statistics, name='statistics'),
    path('history/', views.history, name='math-history'),
    path('calculation/', views.calculation)
    ]

urlpatterns += staticfiles_urlpatterns()
