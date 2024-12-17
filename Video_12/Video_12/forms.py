from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label="Name: ")
    salary = forms.FloatField(label="Salary")
    email = forms.EmailField(label="Email: ")
    address = forms.CharField(label="Address: ")