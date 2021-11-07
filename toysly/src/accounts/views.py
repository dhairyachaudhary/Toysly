from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('store:store')
    else:
        form = UserCreationForm()
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
        return redirect('accounts:login')
    else:
        seller_form = forms.SellerForm()
    return render(request,"accounts/becomeseller.html",{'seller_form':seller_form})