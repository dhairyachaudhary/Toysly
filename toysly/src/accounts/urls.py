from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
]