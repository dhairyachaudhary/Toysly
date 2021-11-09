from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from . import forms
from ecommerce.models import Product,Category

def store_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_ynwI52voLx0Ltq", "IhbQPZoMLmDn2dgmRhhI7IpU"))

        payment = client.order.create({'amount': amount, 'currency': 'USD',
                                       'payment_capture': '1'})
    products = Product.objects.all().order_by('product_name');
    return render(request,'ecommerce/index.html',{ 'products': products })


def category_view(request, category):
    products = Product.objects.all().order_by('product_name');
    category_name = Category.objects.filter(category_slug=category)[0].category_name;
    return render(request,'ecommerce/category.html',{ 'products': products, 'category':category, 'category_name':category_name })

@login_required(login_url="/accounts/login/")
@permission_required("ecommerce.can_add_product", login_url="/accounts/become-seller/")
def add_product(request):
    if request.method=='POST':

        context = {
            'product_details_form': forms.ProductForm(request.POST, request.FILES),
            'product_images_form': forms.ProductImagesForm(request.POST, request.FILES)
        }
        # if context['product_details_form'].is_valid() and context['product_images_form'].is_valid():
        if context['product_details_form'].is_valid():
            prod_instance = context['product_details_form'].save(commit=False)
            prod_instance.product_seller = request.user
            prod_instance.save()
            """
            images = request.FILES.getlist('image')
            ctr = 0
            for i in range(len(images)):
                context['product_images_form'].product_image_name=str(ctr)
                context['product_images_form'].image=images[i]
                image_instance = context['product_images_form'].save(commit=False)
                image_instance.product = prod_instance
                image_instance.save()
                ctr += 1
            """
        return redirect('store:store')
    else:
        context = {
            'product_details_form': forms.ProductForm(),
            # 'product_images_form': forms.ProductImagesForm()
        }
    return render(request,'ecommerce/addproduct.html',context)