from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
import math


def home(request):
    return render(request, 'math_app/home.html')

def about(request):
    return render(request, 'math_app/about.html', {'title': 'About'})

def basicmath(request):
    return render(request, 'math_app/basicmath.html', {'title': 'Basic Math'})

def trigonometry(request):
    return render(request, 'math_app/trigonometry.html', {'title': 'Trigonometry'})

def algebra(request):
    if request.method=="POST":
        values=request.POST['text_input']
        sub1 = 'log('
        sub2 = 'ln('
        sub3 = 'e('
        sub4 = 'sqrt('
        sub5 = 'pi'
        val = ''
        try:
            # Logarithmic Function
            if values is not None and sub1 in values:
                for i in range(4, len(values)):
                    val += values[i]
                if val is None:
                    ans = math.log10(1)
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
                else:
                    ans = math.log10(eval(val))
                return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
            # Natural logarithmic Function
            elif values is not None and sub2 in values:
                for i in range(3, len(values)):
                    val += values[i]
                if val is None:
                    ans = math.log1p(1)
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
                else:
                    ans = math.log1p(eval(val))
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
            # Euler exponential
            elif values is not None and sub3 in values:
                for i in range(2, len(values)):
                    val += values[i]
                if val is None:
                    ans = math.exp(1)
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
                else:
                    ans = math.exp(eval(val))
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
            # Square Root
            elif values is not None and sub4 in values:
                for i in range(5, len(values)):
                    val += values[i]
                if val is None:
                    ans = math.sqrt(0)
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
                else:
                    ans = math.sqrt(eval(val))
                    return render(request=request, template_name='math_app/algebra.html', context={'ans': ans})
            # Else just evaluates
            else:
                val = eval(values)
                return render(request=request, template_name='math_app/algebra.html', context={'ans': val})
            # Prevents website breaking errors
        except:
            return render(request=request, template_name='math_app/algebra.html', context={'ans': 'Error'})
    return render(request, 'math_app/algebra.html', {'title': 'Algebra'})

def statistics(request):
    return render(request, 'math_app/statistics.html', {'title': 'Statistics'})

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

