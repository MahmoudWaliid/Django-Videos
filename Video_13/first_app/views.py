from django.shortcuts import render

# Create your views here.
def first_func(request):
    return render(request, 'first_app/first_page.html', {'message': 'Hello From First Application'})