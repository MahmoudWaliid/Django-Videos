from .forms import PrimeForm
from django.shortcuts import render
from .prime import is_prime

def primo(request):
    b = False
    form = PrimeForm()
    if request.method == 'POST':
        form = PrimeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            b = is_prime(x)
    return render(request, 'pages/prime.html', {'form':form,'o':b})