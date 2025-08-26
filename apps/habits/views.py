from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.

from .models import HabitModel, HabitCompleteModel
from .serializers import HabitSerializer,  HabitCompleteSerializer

class HabitListCreateView(ListCreateAPIView):
    queryset = HabitModel
    serializer_class = HabitSerializer


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HabitModel
    serializer_class = HabitSerializer
    lookup_field = 'id'


class HabitCompleteMark(CreateAPIView):
    queryset = HabitCompleteModel
    serializer_class = HabitSerializer
    