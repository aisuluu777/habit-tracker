from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUsererializer, RegisterCodeVerify
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

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