from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"home.html")

def logins(request):
    if request.user.is_authenticated:
        messages.warning(request,'you logged in...')
        return redirect('homepage')
    if request.method=="POST":
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        print(uname,passw)
        result=authenticate(request,username=uname,password=passw)
        if result:
            login(request,result)
            if request.user.is_superuser:
                return redirect('admin/')
            else:
                return render(request,'profile.html')
        
        return redirect("loginpage")
    return render(request,"login.html")

@login_required(login_url="loginpage")
def create(request):
    return render(request,"create.html")

@login_required(login_url="loginpage")
def profile(request):
    if request.user.is_superuser:
        return redirect('/admin')
    
    return render(request,"profile.html")

def navbor(request):
    return render(request,"navbor.html")

def register(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        Email=request.POST.get('Email')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        print(uname,fname,lname,Email,passw,cpass)
        if User.objects.filter(username=uname).exists():
            messages.info(request,'username undi appude try cheyy kottadi..!')
            return redirect('registerpage')
        if len(passw)<8:
            messages.info(request,'password must be 8 chars')
            return redirect('registerpage')
        if (cpass!=passw):
            messages.info(request,'Bro password should not match')
            return redirect('registerpage')
        
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=Email,password=passw)
        obj.save()
        messages.success(request,'registration completed bro Now login now')
        return redirect('loginpage')
        return render(request,"login.html")

    return render(request,"register.html")

def display(request):
    return render(request,"display.html")

def logouts(request):
    logout(request)
    return redirect("loginpage")