from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import UserRegistrationForm, UserLoginForm

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
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in!")
                return redirect('profile')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')