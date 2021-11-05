from django import forms
from django.forms import ClearableFileInput
from . import models

class ProductForm(forms.ModelForm):
	class Meta:
		model = models.Product
		fields = ['product_name','product_brand','product_price','product_description','product_quantity_available','product_delivery_time']

class ProductImagesForm(forms.ModelForm):
	class Meta:
		model = models.ProductImage
		fields = ['image']
		widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }