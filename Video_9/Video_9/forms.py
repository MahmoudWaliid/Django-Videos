from django import forms

class OneInt(forms.Form):
    x = forms.IntegerField(label="Enter an integer")