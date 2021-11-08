from django.http import HttpResponse
from django.shortcuts import render
from ecommerce.models import Category

def home(request):
    categories = Category.objects.all().order_by('category_name');
    return render(request,'home.html',{ 'categories': categories })

def about(request):
    return render(request,'about.html')