from django.shortcuts import render, reverse, redirect
from .forms import UserCreateForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            return redirect('success')

    else:
        form = UserCreateForm()
    return render(request, 'auth/user_form.html', {'form': form})


def index(request):
    return render(request, 'myapp/show.html')



def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)          
            if user is not None:
                if user.is_active:
                    login(request, user)    
                    return redirect('dashboard')
                    
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': login_form,})


def success(request):
    return render(request, 'myapp/success.html')