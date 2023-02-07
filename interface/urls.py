from unicodedata import name
from django.urls import path, re_path
from django.contrib import admin
from interface import views
from .views import login_view



#url patterns


urlpatterns = [
    path("index",views.index, name="index"),

    path("signup",views.signup, name="signup"),

    path('profile',views.profile, name="profile"),

    path('login_view',views.login_view, name="login_view"),
    
    path('createuser_view',views.createuser_view, name="createuser_view"),

    path('logout_view', views.logout_view, name="logout_view"),

    path('about',views.about, name="about"),

    path('change_profile',views.changeprofile, name="change_profile")

]