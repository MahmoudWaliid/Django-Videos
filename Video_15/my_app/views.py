from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def start_view(request):
    form = MyForm()
    x = "test"
    y = "test"
    z = "test"
    w = "test"
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = cd['z']
            w = cd['w']
            if z:
                z = 'Since you happy, give me 100$'
            else:
                z = 'I\'m sorry, but I can\'t give you 100$'
    return render(request, 'my_page.html', {'form' : form, 'output1' : x, 'output2': y, 'output3' : z, 'output4' : w})