from django import forms
from store.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'size', 'price', 'amount', 'description', 'band_id']

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'image', 'about']