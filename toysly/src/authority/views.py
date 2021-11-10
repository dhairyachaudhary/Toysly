from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random

def authority(request):
     return render(request, "authority/authority.html")

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(6) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.POST.get   ("email")
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is '+o+'</p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)
