from rest_framework import serializers
from .models import User,Qrcode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','password')
  
class QrCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Qrcode
		fields=('user','latitude','longitude')
  
