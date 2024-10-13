from django import forms   
from .models import Shop

class ShopRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Shop
        fields = ['name', 'email', 'latitude', 'longitude']