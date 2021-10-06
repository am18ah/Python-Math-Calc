from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='math-home'),
    path('about/', views.about, name='math-about'),
]

