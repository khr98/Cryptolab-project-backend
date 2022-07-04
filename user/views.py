from django.http import JsonResponse, HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import QrCodeSerializer,UserCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from drf_yasg.utils       import swagger_auto_schema
from drf_yasg             import openapi
from rest_framework.permissions import AllowAny   
from rest_framework.decorators import permission_classes
from django.contrib.auth import get_user_model
from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

# Create your views here.
@permission_classes([AllowAny])
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None: # 해당 email의 user가 존재하지 않는 경우
            return Response(
                {"message": "존재하지않는 email입니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(password, user.password): # 비밀번호에서 틀린 경우
            return Response(
                {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        if user is not None: # 모두 성공 시
            token = RefreshToken.for_user(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response(
                {
                    "message": "login success",
                    "jwt_token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_200_OK
            )
            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        else: # 그 외
            return Response(
                {"message": "로그인에 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST
            )
        



# @method_decorator(name='post', decorator=swagger_auto_schema(
#     operation_summary='create an user account',
#     operation_id='createAccount',
#     tags=['accounts']))
@permission_classes([AllowAny])
class SignUpAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateSerializer



# @permission_classes([AllowAny])
# class SignUpAPIView(View):
#     def get(self,request):
#         serializer = UserCreateSerializer(User.objects.all(), many=True)
#         if len(serializer.data) == 0:
#             return Response({'error': 'User is empty'}, status=409)
#         return Response(serializer.data)

#     def post(self, request):
#         try:
#             data = json.loads(request.body)
            
#             if User.objects.filter(email=data['email']).exists():
#                 return Response({'message' : 'ALREADY_EXISTS'}, status = 400)
            
#             email = data['email']
#             username = data['username']
#             password = data['password'].encode('utf-8')
#             password_crypt = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            
#         except KeyError:
#             return Response({'message' : 'KEY_ERROR'}, status=400)
        
#         User.objects.create(email=email, password=password_crypt, username=username)
#         return Response({'message': 'SUCCESS!'}, status=201)


# def CreateQrCode(request):
#     data = json.loads(request.body)
#     user = User.objects.order_by('?').first()
#     if request.method == "POST":
#         user=user
#         latitude = data["latitude"]
#         longitude = data["longitude"]
#     Qrcode.objects.create(user=user, latitude=latitude, longitude=longitude)
#     return JsonResponse({'message': 'SUCCESS!'})
    
# def ReadQrCode(request):
#     if request.method == "GET":
#         locations = serializers.serialize("json", Qrcode.objects.all())
#     return HttpResponse(locations)
    
# def ReadDetailQrCode(request,pk):
#     if request.method == "GET":
#         location = serializers.serialize("json", Qrcode.objects.filter(pk=pk))
#     return HttpResponse(location)
    
# def UpdateQrCode(request):
#     data = json.loads(request.body)
#     location = Qrcode.objects.order_by('?').first()
#     if request.method == "PUT":
#         location.latitude = data["latitude"]
#         location.longitude = data["longitude"]
#         location.save()
#     return JsonResponse({'message': 'Random object Update SUCCESS!'})
 
# def UpdateDetailQrCode(request,pk):
#     data = json.loads(request.body)
#     location = Qrcode.objects.get(pk=pk)
#     if request.method == "PUT":
#         location.latitude = data["latitude"]
#         location.longitude = data["longitude"]
#         location.save()
#         #location.update(latitude=data["latitude"],longitude=data["longitude"])
#     return JsonResponse({'message': 'object Update SUCCESS!'})

# def DeleteQrCode(request):
#     location = Qrcode.objects.order_by('?').first()
#     if request.method == "DELETE":
#         location.delete()
#     return JsonResponse({'message': 'Random object Delete SUCCESS!'})

  
# def DeleteDetailQrCode(request,pk):
#     location = Qrcode.objects.filter(pk=pk)
#     if request.method == "DELETE":
#         location.delete()
#     return JsonResponse({'message': 'Delete SUCCESS!'})

@permission_classes([AllowAny])
class QrCodeAPIView(APIView):
    def get(self,request):
        serializer = QrCodeSerializer(Qrcode.objects.all(), many=True)
        if len(serializer.data) == 0:
            return Response({'error': 'QRcode is empty'}, status=409)
        return Response(serializer.data)
      
    def post(self, request):
        serializer = QrCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 
   
    def patch(self,request):
        location = Qrcode.objects.order_by('?').first()
        if location == None:
            return Response({'error': 'QRcode is empty'}, status=409)
        serializer = QrCodeSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
    
    def delete(self, request):
        location = Qrcode.objects.order_by('?').first()
        if location == None:
            return Response({'error': 'QRcode is empty'}, status=409)
        location.delete()
        return Response({'message':'delete Success'})

@permission_classes([AllowAny])
class QRCodeDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Qrcode, pk=pk)

    # @swagger_auto_schema(
    #     operation_summary='read QR code information of corresponding id',
    #     operation_id='getLocation',
    #     tags=['locationId'],
    #     responses={
    #         status.HTTP_201_CREATED: openapi.Schema(
    #             type=openapi.TYPE_OBJECT,
    #             properties={'data': LocationQrCodeSchema}
    #         ),
    #         status.HTTP_409_CONFLICT: openapi.Schema(
    #             type=openapi.TYPE_OBJECT,
    #             properties={
    #                 'error': openapi.Schema(
    #                     type=openapi.TYPE_STRING,
    #                     example='No matching object',
    #                 )
    #             }
    #         )
    #     }
    # )
    def get(self,request,pk):
        location = get_object_or_404(Qrcode, pk=pk)
        serializer = QrCodeSerializer(location)
        return Response(serializer.data)

    def patch(self, request, pk):
        location = get_object_or_404(Qrcode, pk=pk)
        serializer = QrCodeSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        location = get_object_or_404(Qrcode, pk=pk)
        location.delete()
        return JsonResponse({'message': 'Delete SUCCESS!'}, status=201)