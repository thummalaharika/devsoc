from cgitb import text
from django.shortcuts import HttpResponse, redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import restaurants, menu, comment
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate



# Create your views here.

def home(request):
    
    rests = restaurants.objects.all()
    return  render(request,'home.html',{'rests':rests})

def details(request, namee):
    a = restaurants.objects.get(name=namee)
    b = menu.objects.filter(name=namee)
    c = comment.objects.filter(name=namee)
    return render(request, 'details.html', {'rest':a, 'menu':b, 'comment':c})
    
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    password2 = request.POST.get('pwd2')
    if password == password2:
        a = User(username=username, password=password)
        a.save()
        return render(request, 'register.html', {'msg': 'Registered successfuly!','error':False})
    else:
        return render(request,'register.html',{'msg':"Password didn't match ",'error':True})


    
    
def loginuser(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    u = authenticate(username=username, password=password)

    if u is not None:
        login(request, u)
        return render(request, 'login.html', {'msg':'Login successful!'})
    else:
        return render(request, 'login.html', {'msg':'Invalid login'})

def show_register(request):
    return render(request, 'register.html')

def show_login(request):
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')