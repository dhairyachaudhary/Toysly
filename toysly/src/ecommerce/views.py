from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from . import forms
import razorpay
import time
import datetime as dt
from ecommerce.models import Product,Category,Payment
import json
import os

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
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_ynwI52voLx0Ltq", "IhbQPZoMLmDn2dgmRhhI7IpU"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
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
        prices={}
        for i in range(len(products)):
            prices[products[i]]=products[i].product_price/100
        return render(request,'ecommerce/index.html',{ 'prices': prices})


def category_view(request, category):
    products = Product.objects.all().order_by('product_name');
    category_name = Category.objects.filter(category_slug=category)[0].category_name;
    prices={}
    for i in range(len(products)):
        prices[products[i]]=products[i].product_price/100
    return render(request,'ecommerce/category.html',{ 'prices': prices, 'category':category, 'category_name':category_name })

@login_required(login_url="/accounts/login/")
@permission_required("ecommerce.can_add_product", login_url="/accounts/become-seller/")
def add_product(request):
    if request.method=='POST':
        context = {
            'product_details_form': forms.ProductForm(request.POST, request.FILES),'flag':0
            # 'product_images_form': forms.ProductImagesForm(request.POST, request.FILES)
        }
        # if context['product_details_form'].is_valid() and context['product_images_form'].is_valid():
        if context['product_details_form'].is_valid():
            prod_instance = context['product_details_form'].save(commit=False)
            prod_instance.product_seller = request.user
            prod_instance.product_price*=100
            if(prod_instance.product_price<100):
                context['flag']=1
                return render(request,'ecommerce/addproduct.html',context)
            prod_instance.save()
            return redirect('store:store')
    else:
        context = {
            'product_details_form': forms.ProductForm(), 'flag':0
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
    timestamp = resp['created_at']
    date_time = dt.datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    resp['created_at']=time.ctime(resp['created_at'])
    print(os.listdir())
    dict1={}
    dict1['product_id']=str(product_id)
    dict1['user_id']=str(user_id)
    dict1['id']=resp['id']
    dict1['entity']=resp['entity']
    dict1['amount']=resp['amount']
    dict1['currency']=resp['currency']
    dict1['created_at']=resp['created_at']
    with open('ecommerce/templates/ecommerce/transactions.log', 'a') as convert_file:
        # convert_file.write("{'product_id':"+str(product_id)+"'user_id':"+str(user_id)+"}")
        convert_file.write(json.dumps(dict1))
        convert_file.write("\n\n")
    product = Product.objects.filter(id=product_id)[0]
    payment_instance = Payment.objects.create(payment_user=user,payment_product=product,payment_time=date_time)
    payment_instance.save()
    return render(request,'ecommerce/success.html')


def log_view(request):
    if request.user.is_superuser:
        return render(request,'ecommerce/transactions.log',content_type='plain/text')
    return redirect('home')
        