from django.shortcuts import render

# Create your views here.
def second_func(request):
    return render(request, 'second_app/second_page.html', {'message': 'Hello From Second Application'})