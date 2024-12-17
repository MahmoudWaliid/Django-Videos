from django import forms
from datetime import datetime

class MyForm(forms.Form):
    levels = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth')
    )
    departments = (
        ('CS', 'Computer Science'),
        ('IS', 'Information Systems'),
        ('IT', 'Information Technology'),
        ('AI', 'Artificial Intelligence')
    )
    x = forms.IntegerField(label="Enter a number", max_value=10, min_value=5)
    y = forms.CharField(label="Enter text", max_length=5, min_length=3, required=False)
    z = forms.BooleanField(label="Are you happy?", required=False)
    w = forms.ChoiceField(label="Select your level", choices=levels)
    x2 = forms.DateField(label="Enter your birthday", initial=datetime.now())
    x3 = forms.DateTimeField(label="Enter your birthday", initial=datetime.now())
    x4 = forms.DecimalField(label="Enter your GPA", decimal_places=4, max_digits=10)
    x5 = forms.FloatField(label="Enter your GPA", max_value=70.55, min_value=10.447)
    x6 = forms.DurationField(label="Enter Something")
    x7 = forms.EmailField(label="Enter your email")
    x8 = forms.URLField(label="Enter your URL")
    x9 = forms.TimeField(label="Enter your time", initial=datetime.now())
    x10 = forms.MultipleChoiceField(label="Select Preferred Department", choices=departments)