from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from .chioses import DAYS_OF_THE_WEEK, STATUS
from django.conf import settings

User = get_user_model

class HabitModel(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_habits')
    title = models.CharField(max_length=100, verbose_name='Название')
    body = models.CharField(max_length=500, verbose_name='Описание')
    frequency = models.CharField(choices=DAYS_OF_THE_WEEK)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'

    def __str__(self):
        return f'{self.title} for {self.user_id.full_name}'
    

class ProgressModel(models.Model):
    habit_id = models.ForeignKey(HabitModel, on_delete=models.CASCADE, related_name='completed')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    status = models.BooleanField(default=False, verbose_name='status')
    note = models.TextField(verbose_name='Notes')
    date = models.DateField()