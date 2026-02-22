from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def home(request):
#     return render(request, 'base.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")  # your login template


def logout_view(request):
    logout(request)
    return redirect('login')


def dashboard_view(request):
    # Protect dashboard, only logged-in users
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, "home.html")  # your main dashboard template