from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Buyer


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class BuyerRegisterForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['phone_number']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['image']
