from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email')
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

