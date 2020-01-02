from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django import forms
from django.conf import settings
from .forms import UserRegisterForm,UserEditForm,UserPwChange
from django.conf.urls.static import static
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            user.profile.first_name = form.cleaned_data.get('first_name')
            username = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            user =  authenticate(username= username , password = pw)
            login(response,user)
            return redirect('home')

    else:
        form = UserRegisterForm()

    return render(response,"auth/register.html",{"form":form})

def home(response):
    return render(response,"layouts/homeContent.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('..')
    else:
        form = AuthenticationForm()
        print("Erreur")


    return render(request,'auth/login.html',{'form':form})

def profile_view(request):
    args = { 'user' : request.user }
    return render (request,"register/profile.html",args)

def edit_view(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('../')

    else:
        form = UserEditForm(instance = request.user)
        args = { 'form' : form ,}
        return render(request,'register/edit.html',args)


def changePassword(request):
    if request.method =='POST':
        form=UserPwChange(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('../')
        else:
            return render(request,'register/changepassword.html')
    else:
        form=UserPwChange(user = request.user)
        args = {'form':form}
        return render(request,'register/changepassword.html',args)
