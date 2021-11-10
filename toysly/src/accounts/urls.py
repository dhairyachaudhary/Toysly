from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('become-seller/',views.becomeseller_view,name='become_seller'),
    path("send_otp/",views.send_otp,name="send otp"),
]