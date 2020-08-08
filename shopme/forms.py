from django import forms
from .models import *

class fur(forms.ModelForm):
    class Meta:
        model = furt
        fields = '__all__'

    
class purchaseuser(forms.ModelForm):

    class Meta:
        model = purchaseperuser
        fields = '__all__'
