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
    val = 0
    var = request.POST['field1']
    val = math.sin(var)

    if request.method=="POST":
        if 'sin'==var:
            val = math.sin(x)

        elif 'cos'==request.POST['field1']:
            x = request.POST['cos']
            print(x)
            val = math.cos(x)

        elif 'tan'==request.POST['field1']:
            val = math.tan(x)

        elif 'cot'==request.POST['field1']:
            val = 1/math.tan(x)

        elif 'csc'==request.POST['field1']:
            val = 1/math.sin(x)

        elif 'sec'==request.POST['field1']:
            val = 1/math.cos(x)

    return render(request=request, template_name='math_app/trigonometry.html', context={'ans':val})

    #ans = request.POST.get('field1')
    #return render(request, 'math_app/trigonometry.html',{"answer":ans})

def algebra(request):
    return render(request, 'math_app/algebra.html', {'title': 'Algebra'})

def login(request):
    if request.method == "POST":
<<<<<<< Updated upstream
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
=======
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
>>>>>>> Stashed changes
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("main:homepage")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="math_app/login.html", context={"login_form":form})

<<<<<<< Updated upstream
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
=======
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
>>>>>>> Stashed changes
