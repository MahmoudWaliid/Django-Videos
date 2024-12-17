from django import forms
from django.forms import TextInput

class PrimeForm(forms.Form):
    x = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'width: 120px; hieght: 50px;'}))

