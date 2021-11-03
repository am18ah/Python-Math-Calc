from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='math-home'),
    path('register/', views.register_request, name='math-register'),
    path('about/', views.about, name='math-about'),

]
