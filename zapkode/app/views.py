from django.shortcuts import render,HttpResponseRedirect,redirect

from django.views import View
from .forms import RegistrationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
from django.views import View



def Registration(request):
    if request.method =="POST":
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('done')
    else:
         form =RegistrationForm()
    return render(request,'registration.html',{'form':form})   


def login_user(request):
    if request.method =="POST":
        form =AuthenticationForm(request.POST,data=request.POST)
        if form.is_valid():
            uname =form.cleaned_data['username']
            upass =form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
             login(request,user)
             print('done')
            
             return HttpResponseRedirect('/welcome/')

    else:
         form =AuthenticationForm()
    return render(request,'login.html',{'form':form})   

def Welcome(request):
    return render(request,'welcome.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



        

