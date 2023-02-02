
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Like
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required




# Create your views here.


def index(request):
    return render(request, "interface/index.html")


def signup(request):
    return render(request, "interface/signup.html")

@login_required(login_url='login_view')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    return render(request, "interface/profile.html")



def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user = authenticate(request, username = user_name,
        password = pass_word)
        

        if user is None:
            context = {"error": "invalid username or password."}
            return render(request, "interface/login.html", context)
        
        else:
            login(request, user)
            return redirect("profile")



    return render(request, "interface/login.html", {})
    
def createuser_view(request):
    if request.method == 'POST':
        Firstname_ = request.POST.get('firstname')
        Lastname_ = request.POST.get('secondname')
        Email_ = request.POST.get('Email')
        Username_ = request.POST.get('username')
        Pasword_ = request.POST.get('pasword') 

        user = User.objects.create_user(username = Username_, password = Pasword_, email = Email_,first_name = Firstname_, last_name = Lastname_)

        user.save()

        

 
    return render(request, "interface/login.html", {})





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

