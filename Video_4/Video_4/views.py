from .forms import InputForm
from django.shortcuts import render

def add(request):
    z = 0
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = x + y
    return render(request, 'pages/addition.html', {'form':form, 'output':z})