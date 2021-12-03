from django.http import HttpResponse
from django.shortcuts import  render, redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .mathfunctions import *
from .models import Equation

def home(request):
    return render(request, 'math_app/home.html')

def about(request):
    return render(request, 'math_app/about.html', {'title': 'About'})

def basicmath(request):
    num1 = request.POST.get('num1_input')
    num2 = request.POST.get('num2_input')
    add = 0
    sub = 0
    mult = 0
    div = 0

    if num1 == None:
        num1 = 0
    if num2 == None:
        num2 = 0

    isStr1 = isinstance(num1,str)
    if isStr1 == True:
        num1 = float(num1)

    isStr2 = isinstance(num2,str)
    if isStr2 == True:
       num2 = float(num2)

    add = Add(num1,num2)
    sub = Sub(num1,num2)
    mult = Multiply(num1,num2)
    div = Divide(num1,num2)
    pow = Power(num1,num2)





    return render(request, 'math_app/basicmath.html', {'add':add, 'sub':sub, 'mult':mult, 'div':div, 'pow':pow})
def trigonometry(request):
    num = request.POST.get('num_input')

    cos = 0
    sin = 0
    tan = 0
    sec = 0
    csc = 0
    cot = 0

    cos_d = 0
    sin_d = 0
    tan_d = 0
    sec_d = 0
    csc_d = 0
    cot_d = 0

    if num == None:
        num = 0

    isStr = isinstance(num,str)
    print(f"******** Num is a string: {isStr}")

    if isStr == True:
        num = float(num)

    cos = findCos(num,'R')
    sin = findSin(num,'R')
    tan = findTan(num,'R')

    sec = findSec(num,'R')
    csc = findCsc(num,'R')
    cot = findCot(num,'R')

    cos_d = findCos(num,'D')
    sin_d = findSin(num,'D')
    tan_d = findTan(num,'D')

    sec_d = findSec(num,'D')
    csc_d = findCsc(num,'D')
    cot_d = findCot(num,'D')

    return render(request, 'math_app/trigonometry.html', {'cos':cos, 'sin':sin, 'tan':tan, 'sec':sec, 'csc':csc, 'cot':cot, 'cos_d':cos_d, 'sin_d':sin_d, 'tan_d':tan_d, 'sec_d':sec_d, 'csc_d':csc_d, 'cot_d':cot_d})

    #ans = request.POST.get('field1')
    #return render(request, 'math_app/trigonometry.html',{"answer":ans})

def algebra(request):
    equation = Equation()
    user = User.objects.filter(username='kayleighelmo').first()
    values = ''
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
    
    v = list(values.split(" "))

    equation = Equation(type_of_math = "Algebra", math = v, author = user)
    equation.save()

    return render(request, 'math_app/algebra.html', {'title': 'Algebra'})

def statistics(request):
    stats = "statistics"
    user = User.objects.filter(username='kayleighelmo').first()
    equation = Equation()
    data = request.POST.get('dataset')
    mean = []
    median = []
    mode = []
    minimum = []
    maximum = []
    rangeVal = []
    stdDev = []
    var = []
    d = []
    flag = 0
    if data == None:
        data = 0
    else:
        data = data.strip()
        li = list(data.split(" "))
        numeric_filter = filter(str.isdigit, li)
        val = " ".join(numeric_filter)
        nums = list(val.split(" "))
    
        equation  = Equation(type_of_math = "Statistics", math = val, author = user)
        equation.save()
       
        for i in nums:
            if i == '':
                nums = 0
            else:  
                d = [float(x) for x in nums]
                median = findMean(d)
                mean = findMedian(d)
                mode = findMode(d)
                minimum = findMin(d)
                maximum = findMax(d)
                rangeVal = findRange(d)
                var = numpy.var(d)
                stdDev = numpy.std(d)

    return render(request, 'math_app/statistics.html', {'median':median, 'mean':mean, 'mode':mode, 'maximum':maximum, 'minimum':minimum, 'rangeVal':rangeVal,'stdDev':stdDev, 'var':var})

def history(request):
    #name = request.user
    #eq = {'equation': request.user.Equation.all()}
    eq = {'equation':Equation.objects.all()}
    return render(request, 'math_app/history.html', eq)

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

def calculation(request):
    if request.method=="POST":
        values=request.POST['text_input']
        print(values)
        return render(request=request, template_name='math_app/home.html', context={'result': 69})
    return render(request=request,template_name='math_app/home.html', context={'result' : 69})

