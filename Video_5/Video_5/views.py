from .forms import InputForm
from django.shortcuts import render

def perform_arithmetic(request):
    x = 1
    y = 1
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
    return render(request, 'pages/arithmetic.html', {'form':form,
                                                     'x':x,
                                                     'y':y,
                                                     'o1':x+y,
                                                     'o2':x-y,
                                                     'o3':x*y,
                                                     'o4':x/y,
                                                     'o5':x%y,})