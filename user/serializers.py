from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from django.core.mail import send_mail



class UserCreateSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(min_length=4, max_length=30)
    password = serializers.CharField(min_length=4, max_length=12, write_only=True)
    email = serializers.EmailField(validators=[
        UniqueValidator(queryset=get_user_model().objects.all(), message="이미 존재하는 이메일 입니다.")
    ])
    
    def create(self, validated_data):
            user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active = False,
        )
            return user

    
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password")


class QrCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Qrcode
		fields= '__all__'
  
