
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from interface.models import AddUser
from .models import User




# Cr eate your views here.


def index(request):
    return render(request, "interface/index.html")


def signup(request):
    return render(request, "interface/signup.html")

@login_required(login_url='login_view')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    return render(request, "interface/profile.html")


def login_view(request):
    error = None
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        try:
            user = User.objects.get(username=user_name, password=pass_word)
            # Do something with the user data
        except User.DoesNotExist:
            # Handle the case where the user doesn't exist
            error = "Invalid login"
        return redirect('home_view')
    return render(request, 'interface/login.html', {'error': error})

    
def createuser_view(request):
    if request.method == 'POST':
      if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('pass_word') and request.POST.get('user_name') and request.POST.get('Email'):
        saverrecord= AddUser()
        saverrecord.first_name=request.POST.get('first_name')
        saverrecord.last_name=request.POST.get('last_name')
        saverrecord.pass_word=request.POST.get('pass_word')
        saverrecord.user_name=request.POST.get('user_name')
        saverrecord.Email=request.POST.get('Email')
        saverrecord.save()
        return render(request, "interface/login.html", {})
    
    else: 
        return render(request, "interface/index.html", {})
     
     
     
        

    






def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


    
    
def about(request):
    return render(request,  "interface/blanco.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changeprofile(request):
    users = User.objects.all()
    if request.method == 'POST':
        oldname = request.POST.get('oldname')
        oldpass = request.POST.get('oldpas')
        newname = request.POST.get('newname')
        newpas = request.POST.get('newpas')


        if users.filter(username = oldname , password = oldpass).exists():
            user = User.objects.change_user(username = newname , password = newpas)
            user.save()
            return render(request, 'interface/profile.html', {})

    return render(request, 'interface/change_profile.html', {})

