from django.core.cache import cache
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from simplejwt import
from .models import CustomUser
from .utils import send_otp_code, get_email_from_cache, generate_otp
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator

class CustomUseSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(validators=[EmailValidator],required=True)
    password = serializers.CharField(validators=[validate_password])

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с таким email уже существует')
        else:
            return email

    def create(self, validated_data):
        username = validated_data.get('username')
        full_name = validated_data.get('full_name')
        email = validated_data.get('email')
        user = CustomUser.objects.create(
            username=username, full_name=full_name, email=email
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


    def send_code(self):
        code = generate_otp()
        cache.set(self.validated_data['email'], code, settings.OTP_CACHE_TIMEOUT)
        send_otp_code(self.validated_data['email'], code)
        print(code)
        return {'data': 'сообщение было отправлено'}

    

class RegisterCodeVerify(serializers.Serializer):
    code = serializers.IntegerField(required=True)

    def validate_code(self, code):
        email = get_email_from_cache(code=code)
        if email:
            try:
                user = CustomUser.objects.get(email=email)
                return user
            
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User not found.")



    



    

