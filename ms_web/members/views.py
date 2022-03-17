from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import logout


# Create your views here.



def register(response):
    #Prevent loged in user to go on register page
    if response.user.is_authenticated:
        return redirect(reverse('msagh_website:base'))
    else:
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                form.save()
                return render(response, 'registration/success_register.html')
        else:
            form = RegisterForm()
        return render(response, 'members/register.html', {"form": form})


def logoutUser(request):
    logout(request)
    return render(request,'members/logout.html')
