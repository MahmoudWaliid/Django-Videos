from django import forms

class InputForm(forms.Form):
    x = forms.IntegerField(label='Enter First Number')
    y = forms.IntegerField(label='Enter Second Number')