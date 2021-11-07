from django import forms
from django.forms import ClearableFileInput
from . import models

class SellerForm(forms.ModelForm):
	class Meta:
		model = models.Seller
		fields = ['agency_name','approval_doc']
