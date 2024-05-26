from django import forms
from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ('customer_name', 'email', 'address', 'phone')
        # exclude = ['assigned_helper']


