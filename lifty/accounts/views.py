from django.shortcuts import render, HttpResponse

from .forms import UserRegistrationForm

# Create your views here.
def accounts_home(request):
    return render(request, 'accounts/base.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context=context)
