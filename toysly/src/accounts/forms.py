from django import forms
from django.forms import ClearableFileInput
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SellerForm(forms.ModelForm):
	class Meta:
		model = models.Seller
		fields = ['agency_name','approval_doc']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )