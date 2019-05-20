from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)
        if user is not None:
            print(user)
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {"error":"incorrect username or password."})
    return render(request, "account/login.html")

def signUp(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password = request.POST['password'])
            auth.login(request, user)
            return redirect('home')
    return render(request, "account/signUp.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request)
    return redirect('home')