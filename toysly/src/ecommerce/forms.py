from django import forms
from django.forms import ClearableFileInput
from . import models

class ProductForm(forms.ModelForm):
	class Meta:
		model = models.Product
		fields = ['product_name','product_brand','product_category','product_price','product_description','product_image_1','product_image_2']
"""
class ProductImagesForm(forms.ModelForm):
	class Meta:
		model = models.ProductImage
		fields = ['image','product_image_name']
		widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
            'product_image_name': forms.HiddenInput(),
        }
"""