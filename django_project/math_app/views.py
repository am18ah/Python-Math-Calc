from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'math_app/home.html')

def about(request):
    return render(request, 'math_app/about.html', {'title': 'About'})

def basicmath(request):
    return render(request, 'math_app/basicmath.html', {'title': 'Basic Math'})

def trigonometry(request):
    return render(request, 'math_app/trigonometry.html', {'title': 'Trigonometry'})

def algebra(request):
    return render(request, 'math_app/algebra.html', {'title': 'Algebra'})

def login(request):
    if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("main:homepage")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="math_app/login.html", context={"login_form":form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="math_app/register.html", context={"register_form":form})
