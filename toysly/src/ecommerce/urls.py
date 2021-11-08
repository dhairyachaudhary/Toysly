from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.store_view,name='store'),
    path('addproduct/',views.add_product,name='add_product'),
    path('toys/',views.toys_view,name='toys'),
]