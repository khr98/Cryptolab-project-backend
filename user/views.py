from django.shortcuts import render
import json, bcrypt, jwt, re

from django.views   import View
from django.http    import JsonResponse, HttpResponse
from .models        import User

# Create your views here.
class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'ALREADY_EXISTS'}, status = 400)
            
            email = data['email']
            password = data['password'].encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        User.objects.create(email=email, password=password_crypt)
        return JsonResponse({'message': 'SUCCESS!'}, status=201)