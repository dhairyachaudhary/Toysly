from django.contrib import admin
from .models import *

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Shipping_Details)
admin.site.register(Cart)