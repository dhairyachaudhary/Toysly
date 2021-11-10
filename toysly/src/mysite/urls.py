"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

# admin login using 2FA
from django_otp.admin import OTPAdminSite

class OTPAdmin(OTPAdminSite):
    pass

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

otp_admin_site = OTPAdmin(name='OTPAdmin')

for model_cls, model_admin in admin.site._registry.items():
   otp_admin_site.register(model_cls, model_admin.__class__)

urlpatterns = [
    path('admin/', otp_admin_site.urls),
    path('daddymin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('store/', include('ecommerce.urls')),
    path('authority/', include('authority.urls')),
    path('accounts/',include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)