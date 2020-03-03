from django import forms
from .models import Order
from django.core.exceptions import ValidationError


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),

        }

    def clean_phone_number(self):
        entered_number = self.cleaned_data.get('phone_number')
        if len(str(entered_number)) > 13:
            raise ValidationError('Enter the number correctly!')
        return entered_number
