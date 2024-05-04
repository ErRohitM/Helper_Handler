from django import forms
from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ('username', 'password', 'email', 'address', 'phone')
        # exclude = ['assigned_helper']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
