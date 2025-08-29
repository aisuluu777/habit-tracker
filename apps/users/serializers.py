from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from simplejwt import
from .models import CustomUser
from .utils import send_otp_code, get_email_from_cache
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator

class CustomUsererializer(serializers.Serializer):
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(validators=[EmailValidator],required=True)
    password = serializers.CharField(validators=[validate_password])

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            return serializers.ValidationError("Пользователь с таким email уже существует")
        else:
            return email

    def create(self, validated_data):
        username = validated_data.get('username')
        full_name = validated_data.get('full_name')
        email = validated_data.get('email')
        user = CustomUser.objects.create(
            username=username, full_name=full_name, email=email
        )
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


    def send_code(self):
        send_otp_code(self.validated_data['email'])
        return {'message' : 'otp code sent'}
    

class RegisterCodeVerify(serializers.Serializer):
    code = serializers.IntegerField(required=True)

    def validate_code(self, code):
        email = get_email_from_cache(code=code)
        if email:
            self.instance = CustomUser.objects.get(email=email)
            return code
        return Response(data='Wrong OTP code', status=HTTP_400_BAD_REQUEST)
    
    def update(self):
        self.instance.is_active = True
        self.instance.is_verified = True
        self.instance.save()
        return self.instance
    
    


    

