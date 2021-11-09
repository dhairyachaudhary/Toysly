from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from . import forms
import razorpay
import time
from ecommerce.models import Product,Category,Payment
import json

def check_search(query, item):
    query = query.lower()
    name = item.product_name.lower()
    category = item.product_category.category_name.lower()
    description = item.product_description.lower()
    if query in name or query in category or query in description:
        return True
    else:
        return False
"""
def search_view(request):
    query = request.GET.get('search')
    if len(query) > 200:
        products = []
    else:
        all_products = Product.objects.all().order_by('product_name')
        products = [item for item in all_products if check_search(query,item)]
    return render(request,'ecommerce/index.html',{ 'products': products })
"""
def store_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_ynwI52voLx0Ltq", "IhbQPZoMLmDn2dgmRhhI7IpU"))

        payment = client.order.create({'amount': amount, 'currency': 'USD',
                                       'payment_capture': '1'})
    else:
        query = request.GET.get('search')
        if query:
            if len(query) > 100 or len(query) < 3:
                products = []
            else:
                all_products = Product.objects.all().order_by('product_name')
                products = [item for item in all_products if check_search(query,item)]
        else:
            products = Product.objects.all().order_by('product_name')
    if len(products) == 0:
        return render(request,'ecommerce/nonefound.html')
    else:
        return render(request,'ecommerce/index.html',{ 'products': products})


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
            # 'product_images_form': forms.ProductImagesForm(request.POST, request.FILES)
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

def success_view(request):
    val=request.POST
    user = request.user
    product_id = val['product']
    user_id = request.user.id
    client = razorpay.Client(auth=("rzp_test_ynwI52voLx0Ltq", "IhbQPZoMLmDn2dgmRhhI7IpU"))
    payment_id = val['razorpay_payment_id']
    resp = client.payment.fetch(payment_id)
    resp['created_at']=time.ctime(resp['created_at'])
    with open('transaction_logs.txt', 'a') as convert_file:
        convert_file.write("{'product_id':"+str(product_id)+"'user_id':"+str(user_id)+"}")
        convert_file.write(json.dumps(resp))
        convert_file.write("\n\n")
    product = Product.objects.filter(id=product_id)[0];
    payment_instance = Payment.objects.create(payment_user=user,payment_product=product,payment_time=resp['created_at'])
    payment_instance.save()
    return render(request,'ecommerce/success.html')