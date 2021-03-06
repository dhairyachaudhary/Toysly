from django.db import models
from django.contrib.auth.models import User

def product_image_path(instance, x):
    # file will be uploaded to MEDIA_ROOT/'product_images'/product_<id>/<image_id>
    return 'product_images/product_{0}/{1}'.format(instance.product.id, instance.product_image_name)

def product_image_path1(instance, x):
    # file will be uploaded to MEDIA_ROOT/'product_images'/product_<id>/<image_id>
    return 'product_images/{0}/{1}'.format(instance.product_name, 1)
def product_image_path2(instance, x):
    # file will be uploaded to MEDIA_ROOT/'product_images'/product_<id>/<image_id>
    return 'product_images/{0}/{1}'.format(instance.product_name, 2)
def category_image_path(instance, x):
    return 'category_images/{0}'.format(instance.category_name)  

class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_slug = models.SlugField()
	category_image = models.ImageField(upload_to=category_image_path,default=None)
	def __str__(self):
		return self.category_name

class Product(models.Model):
	product_seller = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	product_name = models.CharField(max_length=100)
	product_brand = models.CharField(max_length=100)
	product_category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
	product_description = models.TextField(max_length=500)
	product_price = models.DecimalField(max_digits=10, decimal_places=2)
	product_image_1 = models.ImageField(upload_to=product_image_path1,default=None)
	product_image_2 = models.ImageField(upload_to=product_image_path2,default=None)
	def __str__(self):
		return str(self.id) + ' ' + self.product_name

class Payment(models.Model):
	payment_user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	payment_product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	payment_time = models.DateTimeField()

"""
class ProductImage(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	product_image_name = models.CharField(max_length=100,default='0')
	image = models.ImageField(upload_to=product_image_path)
	def __str__(self):
		return str(self.id) + ' ' + str(self.product.id)

class Order(models.Model):
	order_amount = models.DecimalField(max_digits=10, decimal_places=2)
	order_timestamp = models.DateTimeField(auto_now_add=True)
	delivery_date = models.DateField(auto_now=False, auto_now_add=False)

class Shipping_Details(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE,primary_key=True,default=None)
	delivery_address = models.TextField(max_length=500)
	delivery_city = models.CharField(max_length=100)
	delivery_state = models.CharField(max_length=100)
	delivery_country = models.CharField(max_length=100)
	delivery_pincode = models.CharField(max_length=100)

class Payment(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE,default=None)

class Cart(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True,default=None)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	cart_total = models.DecimalField(max_digits=10, decimal_places=2)
"""