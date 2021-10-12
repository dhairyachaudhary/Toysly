from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('homepage')


def about(request):
    return HttpResponse('about')

