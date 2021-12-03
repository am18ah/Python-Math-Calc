from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

def statistics(request):
    return render(request, 'math_app/statistics.html', {'title': 'Statistics'})

def history(request):
    return render(request, 'math_app/history.html', {'title': 'Statistics'})

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect("http://127.0.0.1:8000/register/")
        elif User.objects.filter(email=email):
            messages.error(request, "Email already in use, try signing in instead")
            return redirect("http://127.0.0.1:8000/login/")
        elif len(username) > 15:
            messages.error(request, "Invald username")
            return redirect("http://127.0.0.1:8000/register/")
        elif len(pass1) < 8:
            messages.error(request, "Password must be under 15 characters") 
            return redirect("http://127.0.0.1:8000/register/")
        elif pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("http://127.0.0.1:8000/register/")
        elif not username.isalnum():
            messages.error(request, "Username must be alpha numeric")
            return redirect("http://127.0.0.1:8000/register/") 
        
        user = User.objects.create_user(username, email, pass1)
        user.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("http://127.0.0.1:8000/login/")

    return render (request, "math_app/register.html")

def user_login(request):
    if request.method == "POST":
            username = request.POST.get('username')
            pass1 = request.POST.get('pass1')

            user = authenticate(username=username, password=pass1)

            if user is not None:
                    login(request, user)
                    return redirect("http://127.0.0.1:8000/")
            else:
                    messages.error(request, "User does not exist")

    return render (request, "math_app/login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("http://127.0.0.1:8000/")


