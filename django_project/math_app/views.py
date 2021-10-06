from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'math_app/home.html')

def about(request):
    return render(request, 'math_app/about.html')
