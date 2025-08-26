from rest_framework import serializers
from .models import HabitModel, HabitCompleteModel

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitModel
        fields = ['title', 'body', 'frequency']

class HabitCompleteSerializer(serializers.Serializer):
    class Meta:
        model = HabitCompleteModel
        fields = ['habit_id', 'status', 'note']


# class HabitStatistic(serializers.Serializer):
#     def statistic(self):


