from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm
# Create your views here.


def Login(request):
    if request.method == 'POST':
        username_email = request.POST.get('email_username')
        print(username_email)
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username_email,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            user = authenticate(
                request,
                username=User.objects.get(email=username_email),
                password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Email or Password are not correct.')
                return redirect('login')

    return render(request, 'users/login.html')
