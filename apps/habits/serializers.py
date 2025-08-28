from rest_framework import serializers
from .models import HabitModel, ProgressModel

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitModel
        fields = ['title', 'body', 'frequency']

class ProgressSerializer(serializers.Serializer):
    class Meta:
        model = ProgressModel
        fields = ['habit_id', 'user', 'status', 'note']

class ProgressHistorySerializer(serializers.Serializer):
    progreses = ProgressSerializer(many=True, read_only=True)

    class Meta:
        model = HabitModel
        fields = '__all__'




