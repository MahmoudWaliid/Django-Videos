from django.shortcuts import render
from .forms import WorldCupForm
import random

def world_cup(request):
    z = ""
    form = WorldCupForm()
    if request.method == 'POST':
        form = WorldCupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['countries'].split('-')
            for i in range(int(len(x)/2)):
                y = random.sample(x, 2)
                for i in y:
                    x.remove(i)
                z += y[0] + 'X' + y[1] + '\n'
    return render(request, 'pages/World Cup.html', {'form':form,'o':z})