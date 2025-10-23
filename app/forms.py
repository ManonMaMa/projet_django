from django import forms
from .models import MonTruc

class MonTrucForm(forms.ModelForm):
    class Meta:
        model = MonTruc
        fields = ['name', 'path']
