from django import forms

class MyForm(forms.Form):
    levels = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth')
    )
    x = forms.IntegerField(label="Enter a number", max_value=10, min_value=5)
    y = forms.CharField(label="Enter text", max_length=5, min_length=3, required=False)
    z = forms.BooleanField(label="Are you happy?", required=False)
    w = forms.ChoiceField(label="Select your level", choices=levels)