from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
# Create your views here.


def home(request):
    return render(request,'ap1/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return render(request,'ap1/home.html',{'user':user})
            else:
                return  render(request,'ap1/login.html',{'error_message':'user is disabled/not active'})
        else:
            return render(request,'ap1/login.html',{'error_message':'Invalid login'})
    return render(request, 'ap1/login.html')


def logout(request):
    logout(request)
    return render(request,'ap1/login.html')