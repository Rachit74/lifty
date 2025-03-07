from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def accounts_home(request):
    return render(request, 'accounts/base.html')

def user_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    print(user)
    return render(request, 'accounts/profile.html', context=context)

def register(request):
    # redirect to profile if logged in
    if request.user.is_authenticated():
        return redirect('profile')
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, "You are now registered!")
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context=context)

def login_user(request):
    # redirect the user to profile if already logged in
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() # get authenticated user
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('profile')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')