from django.shortcuts import render
from .forms import Wow

# Create your views here.
def first_func(request):
    message = 'Hello From First Application'
    form = Wow()
    if request.method == 'POST':
        form = Wow(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = cd['x']
    return render(request, 'first_app/first_page.html', {'form': form, 'message': message})