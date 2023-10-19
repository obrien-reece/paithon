from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def profiles(request):
    return render(request, "users/profile.html")


def loginUser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("users:profiles")
        else:
            messages.error(request, 'The details provided are incorrect')
            return redirect("users:login")

    return render(request, "users/login.html")


def logoutUser(request):
    logout(request)
    return redirect("users:login")
