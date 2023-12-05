# login/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import LoginLog

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            LoginLog.objects.create(user=request.user)
            return redirect('dashboard')  # Redirect to the main page of HMS upon successful login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login/login.html')
