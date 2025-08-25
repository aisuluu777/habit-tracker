from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUsererializer, RegisterCodeVerify
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import urllib
import requests
import uuid
from django.shortcuts import redirect
from django.conf import settings

class RegisterUserView(CreateAPIView):
    queryset = CustomUser
    serializer_class = CustomUsererializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED)
    

class RegisterCodeVerifyView(CreateAPIView):
    queryset = CustomUser
    serializer_class = RegisterCodeVerify

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update()
        return Response(status=HTTP_200_OK)
    



User = get_user_model()
  
class GoogleLoginView(APIView):
    def get(self, request):
        query_params = {
        'client_id' : settings.GOOGLE_CLIENT_ID,
        'redirect_uri' : 'http://127.0.0.1:8000/users/google/token/',
        'response_type' : 'code',
        'scope' : ' '.join([
        'openid',
        'email',
        'profile'
        ]),
        'access_type' : 'online',
        #'state
    }
        query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
        base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
        return redirect(f'{base_url}?{query_string}')
   
class GoogleCallbackView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        print(code)
        if not code:
            return Response(
                {'error': 'Code not provided'},
                status=HTTP_400_BAD_REQUEST
            )

        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': 'http://127.0.0.1:8000/users/google/token/',
            'grant_type': 'authorization_code'
        }

        try:
            token_response = requests.post(token_url, data=token_data)
            token_response.raise_for_status()
            token_json = token_response.json()
            access_token = token_json.get('access_token')

            user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
            user_info_response = requests.get(
                user_info_url,
                headers={'Authorization': f'Bearer {access_token}'}
            )
            user_info_response.raise_for_status()
            user_info = user_info_response.json()

            email = user_info.get('email')
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    'username': user_info.get('email', str(uuid.uuid4())),
                    'first_name': user_info.get('given_name', ''),
                    'last_name': user_info.get('family_name', '')
                })


            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            })

        except requests.RequestException as e:
            return Response(
                {'error': 'Failed to authenticate with Google', 'details': str(e)},
                status=HTTP_400_BAD_REQUEST
            )
