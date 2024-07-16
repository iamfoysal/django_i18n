from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .models import User
import json
import datetime
from django.conf import settings





@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if len(username) == 0 or len(password) <6:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
        else:
            user = User.objects.create(username=username, password=password)
            return JsonResponse({'success': 'Login success'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)
    

    

def list_of_users(request):
   users=User.objects.all()
   return render(request, 'index.html', {'users': users})