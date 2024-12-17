from django import forms
from django.forms import TextInput

class WorldCupForm(forms.Form):
    countries = forms.CharField(label='Enter countries separated by -', widget=forms.Textarea({'placeholder': 'Enter countries separated by commas'}))

