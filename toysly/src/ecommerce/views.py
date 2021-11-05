from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

def store_view(request):
    return HttpResponse('Store')

def add_product(request):
    if request.method=='POST':
        """
        context = {
            'product_details_form': forms.ProductForm(request.POST, request.FILES),
            'product_images_form': forms.ProductImagesForm(request.POST, request.FILES)
        }
        if context['product_details_form'].is_valid() and context['product_images_form'].is_valid():
            context['product_details_form'].save()
            images = request.FILES.getlist('image')
            for i in images:
                image_instance = context['product_images_form'](image=i)
                image_instance.save()
        """
        return redirect('store:store')
    else:
        context = {
            'product_details_form': forms.ProductForm(),
            'product_images_form': forms.ProductImagesForm()
        }
    return render(request,'addproduct.html',context)