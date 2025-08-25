from rest_framework import serializers
from .models import HabitModel

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitModel
        fields = ['title', 'body', 'frequency']

        