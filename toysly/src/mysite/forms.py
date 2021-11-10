from django import forms
from django.forms import ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)