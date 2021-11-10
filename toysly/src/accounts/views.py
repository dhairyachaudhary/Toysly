from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from . import forms

def signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('store:store')
    else:
        form = forms.SignUpForm()
    return render(request,"accounts/signup.html",{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('store:store')
    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('store:store')

@login_required(login_url="/accounts/login/")
def becomeseller_view(request):
    if request.method=='POST':
        seller_form = forms.SellerForm(request.POST, request.FILES)
        if seller_form.is_valid():
            seller_instance = seller_form.save(commit=False)
            seller_instance.user = request.user
            seller_instance.save()
            return redirect('store:store')
    else:
        seller_form = forms.SellerForm()
    return render(request,"accounts/becomeseller.html",{'seller_form':seller_form})


def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(6) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.POST.get("email")
     o=generateOTP()
     htmlgen = '<p>Your OTP is '+o+'</p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)
