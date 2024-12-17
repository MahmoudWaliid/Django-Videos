from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('''
    <h1
        style="border: 5px solid black;
        border-radius: 10px;
        background-color: rgb(105, 105, 105);
        padding: 15px;
        width: fit-content;
        color: white;">
        Hello From Django
    </h1>
    ''')