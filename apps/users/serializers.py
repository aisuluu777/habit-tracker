from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from simplejwt import
from .models import CustomUser
from .utils import send_otp_code, get_email_from_cache
from django.contrib.auth.password_validation import validate_password

class CustomUsererializer(serializers.Serializer):
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(validators=[validate_password])

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
        return Response(data={'Otp code sent succesfully'})
    

class RegisterCodeVerify(serializers.Serializer):
    code = serializers.IntegerField(required=True)

    def validate_code(self, code):
        email = get_email_from_cache(code=code)
        if email:
            self.instance = CustomUser.objects.get(email=email)
            return code
        return Response(data='Wrong OTP code', status=HTTP_400_BAD_REQUEST)
    
    def update(self, instance, validated_data):
        instance.is_active = True
        instance.is_verified = True
        instance.save
        return instance
    
    


    

