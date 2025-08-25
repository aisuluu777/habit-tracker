from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from .chioses import DAYS_OF_THE_WEEK

User = get_user_model

class HabitModel(models.Model):
    user_id = models.ForeignKey(User, verbose_name='пользователь')
    title = models.CharField(max_length=100, verbose_name='Название')
    body = models.CharField(max_length=500, verbose_name='Описание')
    frequency = ArrayField(choices=DAYS_OF_THE_WEEK, size=7, default=list)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'

    def __str__(self):
        return f'{self.title} for {self.user_id.full_name}'
    

