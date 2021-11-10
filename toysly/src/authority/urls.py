from django.contrib import admin
from django.urls import path,include
from . import views

app_name="authority"

urlpatterns = [
     path("",views.authority,name="authority"),
     path("send_otp/",views.send_otp,name="send otp"),
]