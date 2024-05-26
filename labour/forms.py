from django import forms
from . models import Helpers

class Add_helper(forms.ModelForm):
    class Meta:
        model = Helpers
        fields = '__all__'
        exclude = ['is_assigned']