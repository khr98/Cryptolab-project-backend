from django.shortcuts import render
import json, bcrypt, jwt, re

from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import User,Qrcode
from django.shortcuts import get_object_or_404
from .serializers import QrCodeSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.core import serializers

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


def CreateQrCode(request):
    data = json.loads(request.body)
    user = User.objects.order_by('?').first()
    if request.method == "POST":
        user=user
        latitude = data["latitude"]
        longitude = data["longitude"]
    Qrcode.objects.create(user=user, latitude=latitude, longitude=longitude)
    return JsonResponse({'message': 'SUCCESS!'})
    
def ReadQrCode(request):
    #locations = Qrcode.objects.all()
    locations = serializers.serialize("json", Qrcode.objects.all())
    return HttpResponse(locations)
    
def ReadDetailQrCode(request,pk):
    #location = Qrcode.objects.filter(pk=pk)
    location = serializers.serialize("json", Qrcode.objects.filter(pk=pk))
    return HttpResponse(location)
    
def UpdateQrCode(request):
    data = json.loads(request.body)
    location = Qrcode.objects.order_by('?').first()
    if request.method == "PUT":
        location.latitude = data["latitude"]
        location.longitude = data["longitude"]
        location.save()
    return JsonResponse({'message': 'Random object Update SUCCESS!'})
 
def UpdateDetailQrCode(request,pk):
    data = json.loads(request.body)
    location = Qrcode.objects.get(pk=pk)
    if request.method == "PUT":
        location.latitude = data["latitude"]
        location.longitude = data["longitude"]
        location.save()
        #location.update(latitude=data["latitude"],longitude=data["longitude"])
    return JsonResponse({'message': 'object Update SUCCESS!'})

def DeleteQrCode(request):
    location = Qrcode.objects.order_by('?').first()
    if request.method == "DELETE":
        location.delete()
    return JsonResponse({'message': 'Random object Delete SUCCESS!'})

  
def DeleteDetailQrCode(request,pk):
    location = Qrcode.objects.filter(pk=pk)
    if request.method == "DELETE":
        location.delete()
    return JsonResponse({'message': 'Delete SUCCESS!'})
    
   
class QRCodeView(APIView):
    def post(self, request):
        serializer = QrCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    def get_object(self, pk):
        return get_object_or_404(Qrcode, pk=pk)

    def get(self, pk):
        location = self.get_object(pk)
        serializer = QrCodeSerializer(location)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        location = self.get_object(pk)
        serializer = QrCodeSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        print(pk)
        location = self.get_object(pk)
        print(location)
        location.delete()
        return JsonResponse({'message': 'Delete SUCCESS!'}, status=201)