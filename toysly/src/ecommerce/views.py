from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from . import forms

def store_view(request):
    return HttpResponse('Store')

@login_required(login_url="/accounts/login/")
@permission_required("ecommerce.can_add_product", login_url="/accounts/become-seller/")
def add_product(request):
    if request.method=='POST':

        context = {
            'product_details_form': forms.ProductForm(request.POST, request.FILES),
            'product_images_form': forms.ProductImagesForm(request.POST, request.FILES)
        }
        if context['product_details_form'].is_valid() and context['product_images_form'].is_valid():
            prod_instance = context['product_details_form'].save(commit=False)
            prod_instance.product_seller = request.user
            prod_instance.save()
            images = request.FILES.getlist('image')
            ctr = 0
            for i in range(len(images)):
                context['product_images_form'].product_image_name=str(ctr)
                context['product_images_form'].image=images[i]
                image_instance = context['product_images_form'].save(commit=False)
                image_instance.product = prod_instance
                image_instance.save()
                ctr += 1
        return redirect('store:store')
    else:
        context = {
            'product_details_form': forms.ProductForm(),
            'product_images_form': forms.ProductImagesForm()
        }
    return render(request,'ecommerce/addproduct.html',context)