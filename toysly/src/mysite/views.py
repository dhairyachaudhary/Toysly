from django.http import HttpResponse
from django.shortcuts import render,redirect
from ecommerce.models import Category
from . import forms

def home(request):
    categories = Category.objects.all().order_by('category_name');
    return render(request,'home.html',{ 'categories': categories })
    
def about(request):
    return render(request,'about.html')

def edit(request):
    if request.method == 'POST':
        form = forms.EditForm(request.POST)
        if form.is_valid():
            user_instance = form.save(commit = False)
            user = request.user
            user.username = user_instance.username
            user.save()
            return redirect('store:store')
    else:
        form = forms.EditForm()
    return render(request,'edit.html',{'form':form})