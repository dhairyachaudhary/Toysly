from django.http import HttpResponse
from django.shortcuts import render

def home(request):
<<<<<<< HEAD
    return render(request,'index.html')
=======
    return render(request,'home.html')
>>>>>>> a0ae616d5a4439f93b63511eee8373bff325da31


def about(request):
    return render(request,'about.html')

