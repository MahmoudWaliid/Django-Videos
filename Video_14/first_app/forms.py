from django import forms

class Wow(forms.Form):
    x = forms.CharField(label="Enter Your Preferred Message", initial="Sui", disabled=True)