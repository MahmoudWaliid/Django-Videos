from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def start_view(request):
    form = MyForm()
    x = "test"
    y = "test"
    z = "test"
    w = "test"
    x2 = "test"
    x3 = "test"
    x4 = "test"
    x5 = "test"
    x6 = "test"
    x7 = "test"
    x8 = "test"
    x9 = "test"
    x10 = "test"
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = cd['z']
            w = cd['w']
            x2 = cd['x2']
            x3 = cd['x3']
            x4 = cd['x4']
            x5 = cd['x5']
            x6 = cd['x6']
            x7 = cd['x7']
            x8 = cd['x8']
            x9 = cd['x9']
            x10 = cd['x10']
            if z:
                z = 'Since you happy, give me 100$'
            else:
                z = 'I\'m sorry, but I can\'t give you 100$'
    return render(request, 'my_page.html', {'form' : form, 'output1' : x, 'output2': y, 'output3' : z,
                                            'output4' : w, 'output5' : x2, 'output6' : x3,
                                            'output7' : x4, 'output8' : x5, 'output9' : x6,
                                            'output10' : x7, 'output11' : x8,
                                            'output12' : x9, 'output13' : x10})