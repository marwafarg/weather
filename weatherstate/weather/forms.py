from django import forms
from django.forms import ModelForm
from .models import weather

class weatherforms(forms.ModelForm):
    class Meta:
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New city..'}))
        model=weather
        fields="__all__"