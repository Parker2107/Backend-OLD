from django import forms
from .models import formData

class NSForm(forms.ModelForm):
    regno = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Registration Number'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    domain = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Domain'}))

    class Meta:
        model = formData
        fields = ['regno', 'name', 'domain']
