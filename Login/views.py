from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request): 
    if request.method == "POST": 
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
    
    return render(request, 'Login_app/login.html', {})