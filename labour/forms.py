from django import forms
from . models import Helpers
# from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator


class Add_helper(forms.ModelForm):
    class Meta:
        model = Helpers
        fields = '__all__'
        exclude = ['is_assigned']