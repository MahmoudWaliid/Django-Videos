from django.shortcuts import render
from .forms import OneInt

def test(request):
    output = ' '
    forms = []
    sum = 0
    for i in range(1, 101):
        form = OneInt(prefix=f'form{i}', initial={'x': i})
        forms.append(form)
    if request.method == 'POST':
        for i in range(1, 101):
            form = OneInt(request.POST, prefix=f'form{i}')
            if form.is_valid():
                cd = form.cleaned_data
                output += str(cd['x']) + ' + '
                sum += cd['x']
        output = output[:-2] + str(sum)
    return render(request, 'test.html', {'forms': forms, 'o': str(output) + ' = ' + str(sum) })