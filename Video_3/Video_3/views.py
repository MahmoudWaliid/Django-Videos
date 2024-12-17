from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addxy(request):
    if request.method == 'POST':
        x = int(request.POST.get('n1'))
        y = int(request.POST.get('n2'))
        z = x + y
        return HttpResponse(f'''
        <div style="
            max-width: 200px;
            margin: 20px auto;
            padding: 10px;
            border: 1px solid #28a745;
            border-radius: 4px;
            background-color: #e9ffe9;
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 0.9em;">
            Result = {z}
        </div>
        ''')
    else:
        return HttpResponse('''
        <form method="POST" style="max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px; background-color: #f9f9f9;">
            <p>
                <label for="n1" style="display: block; margin-bottom: 5px;">Enter First Number</label>
                <input type="text" name="n1" style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;" required>
            </p>
            <p>
                <label for="n2" style="display: block; margin-bottom: 5px;">Enter Second Number</label>
                <input type="text" name="n2" style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;" required>
            </p>
            <input type="submit" value="ADD" style="background-color: #28a745; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer;">
        </form>
        ''')
